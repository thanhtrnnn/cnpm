"""Fix paragraph styles in section 3.2 - reset to NORMAL_TEXT then apply correct styles."""
import sys
import os
import time

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '.claude', 'skills', 'gdocs'))

from scripts.client import GDocsClient

DOC_ID = '1H0pFNhmbX9yDMObxERGsZ0RqKjpX9Je6N60n4tYrB6s'
TAB_TITLE = 'Dịch vụ & Sản phẩm'


def get_tab_info(client, doc_id, tab_title):
    """Get tab info and section boundaries."""
    tab = client.find_tab_by_title(doc_id, tab_title)
    if not tab:
        raise ValueError(f"Tab '{tab_title}' not found")

    tab_id = tab['tabProperties']['tabId']
    body = tab.get('documentTab', {}).get('body', {})
    content = body.get('content', [])

    section_3_2_start = None
    section_3_2_end = None
    section_4_start = None

    for element in content:
        if 'paragraph' in element:
            para = element['paragraph']
            para_text = ''
            for elem in para.get('elements', []):
                if 'textRun' in elem:
                    para_text += elem['textRun'].get('content', '')

            if '3.2. Thiết kế mô hình MVC' in para_text:
                section_3_2_start = element['startIndex']
                section_3_2_end = element['endIndex']

            if section_3_2_end and '4. Thiết kế động' in para_text:
                section_4_start = element['startIndex']
                break

    return tab_id, section_3_2_start, section_4_start


def main():
    client = GDocsClient()

    # Step 1: Get current state
    print("=== Step 1: Get current state ===")
    tab_id, section_3_2_start, section_4_start = get_tab_info(client, DOC_ID, TAB_TITLE)
    print(f"Section 3.2: [{section_3_2_start}]")
    print(f"Section 4: [{section_4_start}]")

    # Step 2: Re-read to get all paragraphs
    print("\n=== Step 2: Find all paragraphs ===")
    tab = client.find_tab_by_title(DOC_ID, TAB_TITLE)
    body = tab.get('documentTab', {}).get('body', {})
    content = body.get('content', [])

    paragraphs = []
    for element in content:
        if 'paragraph' in element:
            elem_start = element['startIndex']
            elem_end = element['endIndex']

            if elem_start >= section_3_2_start and elem_start < section_4_start:
                para = element['paragraph']
                para_text = ''
                for elem in para.get('elements', []):
                    if 'textRun' in elem:
                        para_text += elem['textRun'].get('content', '')

                paragraphs.append({
                    'start': elem_start,
                    'end': elem_end,
                    'text': para_text.rstrip()
                })

    print(f"Found {len(paragraphs)} paragraphs")

    # Step 3: Reset all to NORMAL_TEXT
    print("\n=== Step 3: Reset all to NORMAL_TEXT ===")
    reset_requests = []
    for para in paragraphs:
        if para['text']:  # Skip empty paragraphs
            reset_requests.append({
                'updateParagraphStyle': {
                    'range': {
                        'startIndex': para['start'],
                        'endIndex': para['end'],
                        'tabId': tab_id
                    },
                    'paragraphStyle': {'namedStyleType': 'NORMAL_TEXT'},
                    'fields': 'namedStyleType'
                }
            })

    print(f"Resetting {len(reset_requests)} paragraphs...")

    # Execute in batches
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
                return
        time.sleep(2)

    # Step 4: Apply correct heading styles
    print("\n=== Step 4: Apply heading styles ===")
    heading_requests = []
    for para in paragraphs:
        text = para['text']
        if text.startswith('### '):
            heading_requests.append({
                'updateParagraphStyle': {
                    'range': {
                        'startIndex': para['start'],
                        'endIndex': para['end'],
                        'tabId': tab_id
                    },
                    'paragraphStyle': {'namedStyleType': 'HEADING_3'},
                    'fields': 'namedStyleType'
                }
            })
            print(f"  HEADING_3: {text[:60]}")
        elif text.startswith('**1.') or text.startswith('**2.') or text.startswith('**3.') or text.startswith('**4.'):
            # These are bold items, keep as NORMAL_TEXT
            pass

    if heading_requests:
        print(f"\nApplying {len(heading_requests)} heading styles...")
        try:
            client.batch_update(DOC_ID, heading_requests)
            print("Done")
        except Exception as e:
            print(f"Failed: {e}")
            time.sleep(5)
            try:
                client.batch_update(DOC_ID, heading_requests)
                print("Done (retry)")
            except Exception as e2:
                print(f"Failed again: {e2}")
                return

    # Step 5: Verify
    print("\n=== Step 5: Verify ===")
    tab = client.find_tab_by_title(DOC_ID, TAB_TITLE)
    body = tab.get('documentTab', {}).get('body', {})
    content = body.get('content', [])

    for element in content:
        if 'paragraph' in element:
            elem_start = element['startIndex']
            if elem_start >= section_3_2_start and elem_start < section_4_start:
                para = element['paragraph']
                style = para.get('paragraphStyle', {})
                named = style.get('namedStyleType', 'NORMAL_TEXT')

                para_text = ''
                for elem in para.get('elements', []):
                    if 'textRun' in elem:
                        para_text += elem['textRun'].get('content', '')

                para_text = para_text.rstrip()
                if para_text:
                    print(f"[{elem_start}] {named}: {para_text[:70]}")

    print("\n=== Done! ===")


if __name__ == '__main__':
    main()
