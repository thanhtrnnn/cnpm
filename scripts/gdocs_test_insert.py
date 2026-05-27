"""Phase 3: Test insert small content to verify formatting."""
import sys
import os
import time

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '.claude', 'skills', 'gdocs'))

from scripts.client import GDocsClient

DOC_ID = '1H0pFNhmbX9yDMObxERGsZ0RqKjpX9Je6N60n4tYrB6s'
TAB_TITLE = 'Dịch vụ & Sản phẩm'


def get_tab_and_indices(client, doc_id, tab_title):
    """Get tab info and section 3.2 boundaries."""
    tab = client.find_tab_by_title(doc_id, tab_title)
    if not tab:
        raise ValueError(f"Tab '{tab_title}' not found")

    tab_id = tab['tabProperties']['tabId']
    body = tab.get('documentTab', {}).get('body', {})
    content = body.get('content', [])

    # Find section 3.2 heading
    section_3_2_end = None
    section_4_start = None

    for i, element in enumerate(content):
        if 'paragraph' in element:
            para = element['paragraph']
            para_text = ''
            for elem in para.get('elements', []):
                if 'textRun' in elem:
                    para_text += elem['textRun'].get('content', '')

            if '3.2. Thiết kế mô hình MVC' in para_text:
                section_3_2_end = element['endIndex']
                print(f"Section 3.2 heading: [{element['startIndex']}-{element['endIndex']}]")

            if section_3_2_end and '4. Thiết kế động' in para_text:
                section_4_start = element['startIndex']
                print(f"Section 4 heading: [{element['startIndex']}-{element['endIndex']}]")
                break

    return tab_id, section_3_2_end, section_4_start


def test_insert(client, doc_id, tab_id, insert_index, test_content):
    """Insert test content and return the requests."""
    requests = [{
        'insertText': {
            'location': {'index': insert_index, 'tabId': tab_id},
            'text': test_content
        }
    }]
    return requests


def apply_heading_style(client, doc_id, tab_id, start, end, style):
    """Apply heading style to a paragraph."""
    requests = [{
        'updateParagraphStyle': {
            'range': {
                'startIndex': start,
                'endIndex': end,
                'tabId': tab_id
            },
            'paragraphStyle': {'namedStyleType': style},
            'fields': 'namedStyleType'
        }
    }]
    return requests


def apply_normal_style(client, doc_id, tab_id, start, end):
    """Reset paragraph to NORMAL_TEXT."""
    requests = [{
        'updateParagraphStyle': {
            'range': {
                'startIndex': start,
                'endIndex': end,
                'tabId': tab_id
            },
            'paragraphStyle': {'namedStyleType': 'NORMAL_TEXT'},
            'fields': 'namedStyleType'
        }
    }]
    return requests


def verify_formatting(client, doc_id, tab_title, expected_start, expected_end):
    """Verify inserted content has correct styles."""
    tab = client.find_tab_by_title(doc_id, tab_title)
    body = tab.get('documentTab', {}).get('body', {})
    content = body.get('content', [])

    print("\n=== Verification ===")
    results = []

    for element in content:
        elem_start = element.get('startIndex', 0)
        elem_end = element.get('endIndex', 0)

        if elem_end <= expected_start or elem_start >= expected_end:
            continue

        if 'paragraph' in element:
            para = element['paragraph']
            style = para.get('paragraphStyle', {})
            named = style.get('namedStyleType', 'NORMAL_TEXT')

            para_text = ''
            for elem in para.get('elements', []):
                if 'textRun' in elem:
                    para_text += elem['textRun'].get('content', '')

            para_text = para_text.rstrip()
            if not para_text:
                continue

            # Determine expected style
            if para_text.startswith('### '):
                expected_style = 'HEADING_3'
            elif para_text.startswith('## '):
                expected_style = 'HEADING_2'
            else:
                expected_style = 'NORMAL_TEXT'

            status = '✓' if named == expected_style else '✗'
            results.append({
                'text': para_text[:60],
                'actual': named,
                'expected': expected_style,
                'status': status
            })

            print(f"{status} [{elem_start}-{elem_end}] {named} (expected: {expected_style}): {para_text[:60]}")

    # Summary
    passed = sum(1 for r in results if r['status'] == '✓')
    total = len(results)
    print(f"\n=== Summary: {passed}/{total} passed ===")

    return passed == total


def main():
    client = GDocsClient()

    # Step 1: Get current state
    print("=== Step 1: Get current state ===")
    tab_id, section_3_2_end, section_4_start = get_tab_and_indices(client, DOC_ID, TAB_TITLE)

    if not section_3_2_end or not section_4_start:
        print("ERROR: Could not find section boundaries")
        return

    print(f"Content range: [{section_3_2_end}, {section_4_start}]")

    # Step 2: Delete placeholder content
    print("\n=== Step 2: Delete placeholder content ===")
    if section_4_start > section_3_2_end:
        delete_requests = [{
            'deleteContentRange': {
                'range': {
                    'startIndex': section_3_2_end,
                    'endIndex': section_4_start,
                    'tabId': tab_id
                }
            }
        }]
        client.batch_update(DOC_ID, delete_requests)
        print(f"Deleted content from {section_3_2_end} to {section_4_start}")
        time.sleep(1)

    # Step 3: Re-read to get fresh indices
    print("\n=== Step 3: Re-read indices ===")
    tab_id, section_3_2_end, section_4_start = get_tab_and_indices(client, DOC_ID, TAB_TITLE)
    insert_index = section_3_2_end
    print(f"Insert at: {insert_index}")

    # Step 4: Insert test content
    print("\n=== Step 4: Insert test content ===")
    test_content = "### a) Chức năng tạo order\nĐây là nội dung test formatting.\n"
    requests = test_insert(client, DOC_ID, tab_id, insert_index, test_content)
    client.batch_update(DOC_ID, requests)
    print(f"Inserted {len(test_content)} chars")
    time.sleep(1)

    # Step 5: Re-read to get new indices
    print("\n=== Step 5: Re-read after insert ===")
    tab = client.find_tab_by_title(DOC_ID, TAB_TITLE)
    body = tab.get('documentTab', {}).get('body', {})
    content = body.get('content', [])

    # Find our inserted content
    inserted_start = None
    inserted_end = None
    for element in content:
        if 'paragraph' in element:
            para = element['paragraph']
            para_text = ''
            for elem in para.get('elements', []):
                if 'textRun' in elem:
                    para_text += elem['textRun'].get('content', '')

            if 'a) Chức năng tạo order' in para_text:
                inserted_start = element['startIndex']
                print(f"Found heading at: {inserted_start}")

            if inserted_start and 'Đây là nội dung test' in para_text:
                inserted_end = element['endIndex']
                print(f"Found paragraph at: {inserted_end}")
                break

    if not inserted_start or not inserted_end:
        print("ERROR: Could not find inserted content")
        return

    # Step 6: Apply formatting
    print("\n=== Step 6: Apply formatting ===")

    # Apply HEADING_3 to the heading line
    heading_end = inserted_start + len("### a) Chức năng tạo order\n")
    format_requests = apply_heading_style(client, DOC_ID, tab_id, inserted_start, heading_end, 'HEADING_3')
    client.batch_update(DOC_ID, format_requests)
    print("Applied HEADING_3 to heading")

    # Apply NORMAL_TEXT to the paragraph
    para_start = heading_end
    para_end = inserted_end
    format_requests = apply_normal_style(client, DOC_ID, tab_id, para_start, para_end)
    client.batch_update(DOC_ID, format_requests)
    print("Applied NORMAL_TEXT to paragraph")

    # Step 7: Verify
    print("\n=== Step 7: Verify ===")
    success = verify_formatting(client, DOC_ID, TAB_TITLE, inserted_start, inserted_end)

    if success:
        print("\n✓ Test passed! Formatting is correct.")
        print("Proceed to Phase 4: Insert full content.")
    else:
        print("\n✗ Test failed. Check formatting issues.")
        print("Fix converter.py before proceeding.")


if __name__ == '__main__':
    main()
