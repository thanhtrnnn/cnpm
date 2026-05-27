"""Fix section 3.2 formatting by re-inserting content with fixed converter."""
import sys
import os
import re
import time

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '.claude', 'skills', 'gdocs'))

from scripts.client import GDocsClient
from scripts.converter import convert_markdown_to_requests

DOC_ID = '1H0pFNhmbX9yDMObxERGsZ0RqKjpX9Je6N60n4tYrB6s'
TAB_TITLE = 'Dịch vụ & Sản phẩm'
MD_FILE = os.path.join(os.path.dirname(__file__), '..', 'docs', 'tabs', 'section-3.2-mvc.md')


def get_tab_content(client, doc_id, tab_title):
    """Get tab content and find section boundaries."""
    tab = client.find_tab_by_title(doc_id, tab_title)
    if not tab:
        raise ValueError(f"Tab '{tab_title}' not found")

    tab_id = tab['tabProperties']['tabId']
    body = tab.get('documentTab', {}).get('body', {})
    content = body.get('content', [])

    # Find section 3.2 heading
    section_start = None
    for i, element in enumerate(content):
        if 'paragraph' in element:
            para = element['paragraph']
            para_text = ''
            for elem in para.get('elements', []):
                if 'textRun' in elem:
                    para_text += elem['textRun'].get('content', '')

            if 'III.2. Thiết kế mô hình MVC' in para_text:
                section_start = element['startIndex']
                print(f"Found section 3.2 at index {i}, start={section_start}: {para_text.strip()}")
                break

    if section_start is None:
        raise ValueError("Section 3.2 not found")

    # Find next section (look for patterns like '3.3', '4.', 'III.', etc.)
    section_end = None
    for i, element in enumerate(content):
        if element.get('startIndex', 0) <= section_start:
            continue
        if 'paragraph' in element:
            para = element['paragraph']
            style = para.get('paragraphStyle', {})
            named = style.get('namedStyleType', 'NORMAL_TEXT')

            para_text = ''
            for elem in para.get('elements', []):
                if 'textRun' in elem:
                    para_text += elem['textRun'].get('content', '')

            # Look for section headings that match patterns like '3.3', '4.', 'III.', etc.
            if named == 'HEADING_2' and para_text.strip():
                if re.match(r'^(\d+\.\s|III\.|IV\.|##\s\d)', para_text.strip()):
                    section_end = element['startIndex']
                    print(f"Found next section at index {i}, start={section_end}: {para_text.strip()[:60]}")
                    break

    if section_end is None and content:
        section_end = content[-1].get('endIndex', section_start + 1)

    return tab_id, section_start, section_end


def main():
    client = GDocsClient()

    # Read MD file
    with open(MD_FILE, 'r', encoding='utf-8') as f:
        md_content = f.read()

    # Remove the first heading (## III.2...) since it already exists in the doc
    # We'll keep it and just update content under it
    lines = md_content.split('\n')
    # Find where the content starts (after ## III.2 heading)
    content_start = 0
    for i, line in enumerate(lines):
        if line.startswith('## '):
            content_start = i + 1
            break

    # Content to insert (everything after ## III.2 heading)
    content_to_insert = '\n'.join(lines[content_start:]).strip()

    print(f"\nContent length: {len(content_to_insert)} chars")
    print(f"First 200 chars: {content_to_insert[:200]}")

    # Get tab boundaries
    tab_id, section_start, section_end = get_tab_content(client, DOC_ID, TAB_TITLE)

    print(f"\nTab ID: {tab_id}")
    print(f"Section range: {section_start} - {section_end}")

    # Step 1: Delete existing content under section 3.2
    if section_end > section_start + 1:
        print(f"\nDeleting content from {section_start + 1} to {section_end}...")
        delete_requests = [{
            'deleteContentRange': {
                'range': {
                    'startIndex': section_start + 1,
                    'endIndex': section_end,
                    'tabId': tab_id
                }
            }
        }]
        client.batch_update(DOC_ID, delete_requests)
        print("Deleted old content")
        time.sleep(1)

    # Step 2: Re-read to get updated indices after deletion
    tab = client.find_tab_by_title(DOC_ID, TAB_TITLE)
    body = tab.get('documentTab', {}).get('body', {})
    content = body.get('content', [])

    # Find section 3.2 heading index
    insert_index = None
    for element in content:
        if 'paragraph' in element:
            para = element['paragraph']
            para_text = ''
            for elem in para.get('elements', []):
                if 'textRun' in elem:
                    para_text += elem['textRun'].get('content', '')
            if '3.2' in para_text:
                insert_index = element['endIndex']
                break

    if insert_index is None:
        raise ValueError("Could not find section 3.2 heading after deletion")

    print(f"\nInsert index: {insert_index}")

    # Step 3: Convert markdown to requests with fixed converter
    requests = convert_markdown_to_requests(content_to_insert)

    if not requests:
        print("No requests generated!")
        return

    print(f"Generated {len(requests)} requests")

    # Add tabId to all requests
    for req in requests:
        # Add tabId to location-based requests
        for key in ['insertText', 'updateParagraphStyle', 'updateTextStyle',
                     'createParagraphBullets', 'deleteContentRange']:
            if key in req:
                loc = req[key].get('location') or req[key].get('range', {})
                if 'index' in loc or 'startIndex' in loc:
                    loc['tabId'] = tab_id

    # Step 4: Execute requests in batches (max 500 per batch)
    batch_size = 500
    for i in range(0, len(requests), batch_size):
        batch = requests[i:i + batch_size]
        print(f"\nExecuting batch {i // batch_size + 1} ({len(batch)} requests)...")
        try:
            client.batch_update(DOC_ID, batch)
            print(f"  Batch {i // batch_size + 1} done")
        except Exception as e:
            print(f"  Batch {i // batch_size + 1} failed: {e}")
            # Print first failing request for debugging
            for j, req in enumerate(batch):
                print(f"  Request {j}: {list(req.keys())}")
            raise
        time.sleep(0.5)

    print("\nDone! Section 3.2 has been re-inserted with fixed formatting.")


if __name__ == '__main__':
    main()
