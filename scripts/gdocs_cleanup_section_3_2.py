"""Cleanup and fix formatting for section 3.2."""
import sys
import os
import re
import time

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '.claude', 'skills', 'gdocs'))

from scripts.client import GDocsClient

DOC_ID = '1H0pFNhmbX9yDMObxERGsZ0RqKjpX9Je6N60n4tYrB6s'
TAB_TITLE = 'Dịch vụ & Sản phẩm'


def get_section_elements(client, doc_id, tab_title):
    """Get all elements in section 3.2."""
    tab = client.find_tab_by_title(doc_id, tab_title)
    if not tab:
        raise ValueError(f"Tab '{tab_title}' not found")

    tab_id = tab['tabProperties']['tabId']
    body = tab.get('documentTab', {}).get('body', {})
    content = body.get('content', [])

    elements = []
    found_3_2 = False

    for element in content:
        if 'paragraph' in element:
            para = element['paragraph']
            style = para.get('paragraphStyle', {})
            named = style.get('namedStyleType', 'NORMAL_TEXT')

            para_text = ''
            for elem in para.get('elements', []):
                if 'textRun' in elem:
                    para_text += elem['textRun'].get('content', '')

            if '3.2. Thiết kế mô hình MVC' in para_text:
                found_3_2 = True
                elements.append({
                    'type': 'heading',
                    'startIndex': element['startIndex'],
                    'endIndex': element['endIndex'],
                    'style': named,
                    'text': para_text.rstrip()
                })
                continue

            if found_3_2 and '4. Thiết kế động' in para_text:
                break

            if found_3_2:
                elements.append({
                    'type': 'paragraph',
                    'startIndex': element['startIndex'],
                    'endIndex': element['endIndex'],
                    'style': named,
                    'text': para_text.rstrip()
                })

        elif 'table' in element and found_3_2:
            elements.append({
                'type': 'table',
                'startIndex': element['startIndex'],
                'endIndex': element['endIndex']
            })

    return elements, tab_id


def main():
    client = GDocsClient()

    print("=== Getting section 3.2 elements ===")
    elements, tab_id = get_section_elements(client, DOC_ID, TAB_TITLE)
    print(f"Found {len(elements)} elements")

    # Step 1: Reset empty HEADING_2 paragraphs to NORMAL_TEXT
    print("\n=== Step 1: Reset empty HEADING_2 paragraphs ===")
    reset_requests = []
    for elem in elements:
        if elem['type'] == 'paragraph' and elem['style'].startswith('HEADING') and not elem['text']:
            reset_requests.append({
                'updateParagraphStyle': {
                    'range': {
                        'startIndex': elem['startIndex'],
                        'endIndex': elem['endIndex'],
                        'tabId': tab_id
                    },
                    'paragraphStyle': {'namedStyleType': 'NORMAL_TEXT'},
                    'fields': 'namedStyleType'
                }
            })

    print(f"Found {len(reset_requests)} empty headings to reset")
    if reset_requests:
        batch_size = 50
        for i in range(0, len(reset_requests), batch_size):
            batch = reset_requests[i:i + batch_size]
            try:
                client.batch_update(DOC_ID, batch)
                print(f"  Batch {i // batch_size + 1} done")
            except Exception as e:
                print(f"  Batch {i // batch_size + 1} failed: {e}")
                time.sleep(5)
                try:
                    client.batch_update(DOC_ID, batch)
                    print(f"  Batch {i // batch_size + 1} done (retry)")
                except Exception as e2:
                    print(f"  Batch {i // batch_size + 1} failed again: {e2}")
            time.sleep(2)

    # Step 2: Apply bullet formatting to list items
    print("\n=== Step 2: Apply bullet formatting to list items ===")
    bullet_requests = []
    for elem in elements:
        if elem['type'] == 'paragraph' and elem['text'].startswith('- '):
            bullet_requests.append({
                'createParagraphBullets': {
                    'range': {
                        'startIndex': elem['startIndex'],
                        'endIndex': elem['endIndex'],
                        'tabId': tab_id
                    },
                    'bulletPreset': 'BULLET_DISC_CIRCLE_SQUARE'
                }
            })

    print(f"Found {len(bullet_requests)} list items to format")
    if bullet_requests:
        batch_size = 50
        for i in range(0, len(bullet_requests), batch_size):
            batch = bullet_requests[i:i + batch_size]
            try:
                client.batch_update(DOC_ID, batch)
                print(f"  Batch {i // batch_size + 1} done")
            except Exception as e:
                print(f"  Batch {i // batch_size + 1} failed: {e}")
                time.sleep(5)
                try:
                    client.batch_update(DOC_ID, batch)
                    print(f"  Batch {i // batch_size + 1} done (retry)")
                except Exception as e2:
                    print(f"  Batch {i // batch_size + 1} failed again: {e2}")
            time.sleep(2)

    # Step 3: Apply code font to inline code
    print("\n=== Step 3: Apply code font to inline code ===")
    code_requests = []
    for elem in elements:
        if elem['type'] == 'paragraph' and '`' in elem['text']:
            # Find code spans
            for match in re.finditer(r'`(.+?)`', elem['text']):
                # Calculate offset in clean text
                clean_text = elem['text'][:match.start()].replace('`', '')
                code_text = match.group(1)
                start = elem['startIndex'] + len(clean_text)
                end = start + len(code_text)
                code_requests.append({
                    'updateTextStyle': {
                        'range': {
                            'startIndex': start,
                            'endIndex': end,
                            'tabId': tab_id
                        },
                        'textStyle': {'weightedFontFamily': {'fontFamily': 'Courier New'}},
                        'fields': 'weightedFontFamily'
                    }
                })

    print(f"Found {len(code_requests)} code spans to format")
    if code_requests:
        batch_size = 50
        for i in range(0, len(code_requests), batch_size):
            batch = code_requests[i:i + batch_size]
            try:
                client.batch_update(DOC_ID, batch)
                print(f"  Batch {i // batch_size + 1} done")
            except Exception as e:
                print(f"  Batch {i // batch_size + 1} failed: {e}")
                time.sleep(5)
                try:
                    client.batch_update(DOC_ID, batch)
                    print(f"  Batch {i // batch_size + 1} done (retry)")
                except Exception as e2:
                    print(f"  Batch {i // batch_size + 1} failed again: {e2}")
            time.sleep(2)

    # Step 4: Apply bold to **text** markers
    print("\n=== Step 4: Apply bold formatting ===")
    bold_requests = []
    for elem in elements:
        if elem['type'] == 'paragraph' and '**' in elem['text']:
            for match in re.finditer(r'\*\*(.+?)\*\*', elem['text']):
                clean_before = elem['text'][:match.start()].replace('**', '')
                bold_text = match.group(1)
                start = elem['startIndex'] + len(clean_before)
                end = start + len(bold_text)
                bold_requests.append({
                    'updateTextStyle': {
                        'range': {
                            'startIndex': start,
                            'endIndex': end,
                            'tabId': tab_id
                        },
                        'textStyle': {'bold': True},
                        'fields': 'bold'
                    }
                })

    print(f"Found {len(bold_requests)} bold spans to format")
    if bold_requests:
        batch_size = 50
        for i in range(0, len(bold_requests), batch_size):
            batch = bold_requests[i:i + batch_size]
            try:
                client.batch_update(DOC_ID, batch)
                print(f"  Batch {i // batch_size + 1} done")
            except Exception as e:
                print(f"  Batch {i // batch_size + 1} failed: {e}")
                time.sleep(5)
                try:
                    client.batch_update(DOC_ID, batch)
                    print(f"  Batch {i // batch_size + 1} done (retry)")
                except Exception as e2:
                    print(f"  Batch {i // batch_size + 1} failed again: {e2}")
            time.sleep(2)

    print("\n=== Done! ===")


if __name__ == '__main__':
    main()
