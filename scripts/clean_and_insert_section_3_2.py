"""Clean up duplicate section 3.2 and insert once with correct formatting."""
import sys
import os
import re
import time

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '.claude', 'skills', 'gdocs'))

from scripts.client import GDocsClient

DOC_ID = '1H0pFNhmbX9yDMObxERGsZ0RqKjpX9Je6N60n4tYrB6s'
TAB_TITLE = 'Dịch vụ & Sản phẩm'
MD_FILE = os.path.join(os.path.dirname(__file__), '..', 'docs', 'tabs', 'section-3.2-mvc.md')


def find_delete_range(client, doc_id, tab_title):
    """Find range to delete (from first section 3.2 to next section)."""
    tab = client.find_tab_by_title(doc_id, tab_title)
    if not tab:
        raise ValueError(f"Tab '{tab_title}' not found")

    tab_id = tab['tabProperties']['tabId']
    body = tab.get('documentTab', {}).get('body', {})
    content = body.get('content', [])

    first_occurrence = None
    next_section = None

    for i, element in enumerate(content):
        if 'paragraph' in element:
            para = element['paragraph']
            para_text = ''
            for elem in para.get('elements', []):
                if 'textRun' in elem:
                    para_text += elem['textRun'].get('content', '')

            if 'III.2. Thiết kế mô hình MVC' in para_text and first_occurrence is None:
                first_occurrence = element.get('startIndex')
                print(f"First occurrence at: {first_occurrence}")

            if first_occurrence and '4. Thiết kế động' in para_text:
                next_section = element.get('startIndex')
                print(f"Next section at: {next_section}")
                break

    if first_occurrence is None or next_section is None:
        raise ValueError("Could not find section boundaries")

    return tab_id, first_occurrence, next_section


def find_insert_location(client, doc_id, tab_title, delete_end):
    """Find where to insert section 3.2 (before section 4)."""
    tab = client.find_tab_by_title(doc_id, tab_title)
    if not tab:
        raise ValueError(f"Tab '{tab_title}' not found")

    body = tab.get('documentTab', {}).get('body', {})
    content = body.get('content', [])

    # Find section 4
    for i, element in enumerate(content):
        if 'paragraph' in element:
            para = element['paragraph']
            para_text = ''
            for elem in para.get('elements', []):
                if 'textRun' in elem:
                    para_text += elem['textRun'].get('content', '')

            if '4. Thiết kế động' in para_text:
                insert_index = element.get('startIndex')
                print(f"Section 4 starts at: {insert_index}")
                return insert_index

    raise ValueError("Could not find section 4")


def clean_inline_formatting(text):
    """Remove markdown formatting markers from text."""
    text = re.sub(r'\*\*(.+?)\*\*', r'\1', text)
    text = re.sub(r'\*(.+?)\*', r'\1', text)
    text = re.sub(r'`(.+?)`', r'\1', text)
    text = re.sub(r'\[(.+?)\]\(.+?\)', r'\1', text)
    return text


def main():
    client = GDocsClient()

    # Read MD file
    with open(MD_FILE, 'r', encoding='utf-8') as f:
        md_content = f.read()

    # Extract the first heading
    lines = md_content.split('\n')
    first_heading = None
    content_start = 0
    for i, line in enumerate(lines):
        if line.startswith('## '):
            first_heading = line[3:].strip()  # Remove '## ' prefix
            content_start = i + 1
            break

    # Content to insert (everything after ## III.2 heading)
    content_to_insert = '\n'.join(lines[content_start:]).strip()

    print(f"Content length: {len(content_to_insert)} chars")

    # Find insert location (before section 4)
    tab = client.find_tab_by_title(DOC_ID, TAB_TITLE)
    if not tab:
        raise ValueError(f"Tab '{TAB_TITLE}' not found")

    tab_id = tab['tabProperties']['tabId']
    insert_index = find_insert_location(client, DOC_ID, TAB_TITLE, None)
    print(f"Insert index: {insert_index}")

    # Build content to insert (heading + content)
    heading_text = clean_inline_formatting(first_heading) + '\n' if first_heading else ''
    full_content = heading_text + content_to_insert

    # Insert content as plain text
    print(f"\nInserting {len(full_content)} chars of plain text...")
    insert_requests = [{
        'insertText': {
            'location': {'index': insert_index, 'tabId': tab_id},
            'text': full_content
        }
    }]
    client.batch_update(DOC_ID, insert_requests)
    print("Inserted plain text")
    time.sleep(1)

    # Re-read to get updated indices
    tab = client.find_tab_by_title(DOC_ID, TAB_TITLE)
    body = tab.get('documentTab', {}).get('body', {})
    content = body.get('content', [])

    # Find the inserted content
    insert_start = None
    for i, element in enumerate(content):
        if 'paragraph' in element:
            para = element['paragraph']
            para_text = ''
            for elem in para.get('elements', []):
                if 'textRun' in elem:
                    para_text += elem['textRun'].get('content', '')

            if 'III.2. Thiết kế mô hình MVC' in para_text:
                insert_start = element.get('startIndex')
                break

    if insert_start is None:
        print("Warning: Could not find inserted content")
        return

    insert_end = insert_start + len(full_content)
    print(f"Inserted content range: {insert_start} to {insert_end}")

    # Apply formatting
    print("\nApplying formatting...")
    format_requests = []

    # Apply heading style to first line
    heading_end = insert_start + len(heading_text)
    format_requests.append({
        'updateParagraphStyle': {
            'range': {
                'startIndex': insert_start,
                'endIndex': heading_end,
                'tabId': tab_id
            },
            'paragraphStyle': {'namedStyleType': 'HEADING_2'},
            'fields': 'namedStyleType'
        }
    })

    # Apply formatting to all paragraphs
    current_idx = heading_end
    for i, element in enumerate(content):
        if 'paragraph' in element:
            para_start = element.get('startIndex', 0)
            para_end = element.get('endIndex', 0)

            if para_start >= insert_start and para_start < insert_end:
                # This paragraph is in our inserted content
                if para_start > insert_start:
                    # Get paragraph text to check for headings
                    para = element['paragraph']
                    para_text = ''
                    for elem in para.get('elements', []):
                        if 'textRun' in elem:
                            para_text += elem['textRun'].get('content', '')

                    # Determine style based on content
                    if para_text.startswith('### '):
                        named_style = 'HEADING_3'
                    elif para_text.startswith('**1.') or para_text.startswith('**2.') or para_text.startswith('**3.') or para_text.startswith('**4.'):
                        named_style = 'HEADING_3'
                    else:
                        named_style = 'NORMAL_TEXT'

                    format_requests.append({
                        'updateParagraphStyle': {
                            'range': {
                                'startIndex': para_start,
                                'endIndex': para_end,
                                'tabId': tab_id
                            },
                            'paragraphStyle': {'namedStyleType': named_style},
                            'fields': 'namedStyleType'
                        }
                    })

    # Execute format requests in batches
    batch_size = 500
    for i in range(0, len(format_requests), batch_size):
        batch = format_requests[i:i + batch_size]
        print(f"  Executing batch {i // batch_size + 1} ({len(batch)} requests)...")
        client.batch_update(DOC_ID, batch)
        time.sleep(0.5)

    print(f"  Applied {len(format_requests)} formatting requests")
    print("\nDone! Section 3.2 has been cleaned and inserted with correct formatting.")


if __name__ == '__main__':
    main()
