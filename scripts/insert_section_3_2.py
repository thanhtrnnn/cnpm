"""Insert section 3.2 at correct location with fixed formatting."""
import sys
import os
import time

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '.claude', 'skills', 'gdocs'))

from scripts.client import GDocsClient
from scripts.converter import convert_markdown_to_requests

DOC_ID = '1H0pFNhmbX9yDMObxERGsZ0RqKjpX9Je6N60n4tYrB6s'
TAB_TITLE = 'Dịch vụ & Sản phẩm'
MD_FILE = os.path.join(os.path.dirname(__file__), '..', 'docs', 'tabs', 'section-3.2-mvc.md')


def find_insert_location(client, doc_id, tab_title):
    """Find where to insert section 3.2 (after section 3.1, before section 4)."""
    tab = client.find_tab_by_title(doc_id, tab_title)
    if not tab:
        raise ValueError(f"Tab '{tab_title}' not found")

    tab_id = tab['tabProperties']['tabId']
    body = tab.get('documentTab', {}).get('body', {})
    content = body.get('content', [])

    # Find section 3.1 and section 4
    section_3_1_end = None
    section_4_start = None

    for i, element in enumerate(content):
        if 'paragraph' in element:
            para = element['paragraph']
            style = para.get('paragraphStyle', {})
            named = style.get('namedStyleType', 'NORMAL_TEXT')

            para_text = ''
            for elem in para.get('elements', []):
                if 'textRun' in elem:
                    para_text += elem['textRun'].get('content', '')

            if '3.1. Thiết kế giao diện' in para_text:
                # Found section 3.1, now find where it ends
                for j in range(i+1, len(content)):
                    elem2 = content[j]
                    if 'paragraph' in elem2:
                        para2 = elem2['paragraph']
                        style2 = para2.get('paragraphStyle', {})
                        named2 = style2.get('namedStyleType', 'NORMAL_TEXT')

                        para_text2 = ''
                        for e in para2.get('elements', []):
                            if 'textRun' in e:
                                para_text2 += e['textRun'].get('content', '')

                        # Look for next section heading
                        if named2.startswith('HEADING_2') and para_text2.strip():
                            if '4.' in para_text2 or 'Thiết kế động' in para_text2:
                                section_3_1_end = elem2.get('startIndex')
                                section_4_start = elem2.get('startIndex')
                                print(f"Section 3.1 ends at: {section_3_1_end}")
                                print(f"Section 4 starts at: {section_4_start}")
                                break
                break

    if section_3_1_end is None:
        raise ValueError("Could not find section 3.1 end")

    return tab_id, section_3_1_end


def main():
    client = GDocsClient()

    # Read MD file
    with open(MD_FILE, 'r', encoding='utf-8') as f:
        md_content = f.read()

    # Remove the first heading (## III.2...) since we'll insert it separately
    lines = md_content.split('\n')
    content_start = 0
    for i, line in enumerate(lines):
        if line.startswith('## '):
            content_start = i + 1
            break

    # Content to insert (everything after ## III.2 heading)
    content_to_insert = '\n'.join(lines[content_start:]).strip()

    print(f"Content length: {len(content_to_insert)} chars")

    # Find insert location
    tab_id, insert_index = find_insert_location(client, DOC_ID, TAB_TITLE)
    print(f"Insert index: {insert_index}")

    # Convert markdown to requests with fixed converter
    requests = convert_markdown_to_requests(content_to_insert, start_index=insert_index)

    if not requests:
        print("No requests generated!")
        return

    print(f"Generated {len(requests)} requests")

    # Add tabId to all requests
    for req in requests:
        for key in ['insertText', 'updateParagraphStyle', 'updateTextStyle',
                     'createParagraphBullets', 'deleteContentRange']:
            if key in req:
                loc = req[key].get('location') or req[key].get('range', {})
                if 'index' in loc or 'startIndex' in loc:
                    loc['tabId'] = tab_id

    # Execute requests in batches
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
            for j, req in enumerate(batch[:5]):
                print(f"  Request {j}: {list(req.keys())}")
            raise
        time.sleep(0.5)

    print("\nDone! Section 3.2 has been inserted with fixed formatting.")


if __name__ == '__main__':
    main()
