"""Phase 4: Update section 3.2 - simplified approach with rate limiting."""
import sys
import os
import re
import time

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '.claude', 'skills', 'gdocs'))

from scripts.client import GDocsClient

DOC_ID = '1H0pFNhmbX9yDMObxERGsZ0RqKjpX9Je6N60n4tYrB6s'
TAB_TITLE = 'Dịch vụ & Sản phẩm'
MD_FILE = os.path.join(os.path.dirname(__file__), '..', 'docs', 'tabs', 'section-3.2-mvc.md')


def get_tab_info(client, doc_id, tab_title):
    """Get tab info and section boundaries."""
    tab = client.find_tab_by_title(doc_id, tab_title)
    if not tab:
        raise ValueError(f"Tab '{tab_title}' not found")

    tab_id = tab['tabProperties']['tabId']
    body = tab.get('documentTab', {}).get('body', {})
    content = body.get('content', [])

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
                section_3_2_end = element['endIndex']

            if section_3_2_end and '4. Thiết kế động' in para_text:
                section_4_start = element['startIndex']
                break

    return tab_id, section_3_2_end, section_4_start


def clean_inline_formatting(text):
    """Remove markdown formatting markers."""
    text = re.sub(r'\*\*(.+?)\*\*', r'\1', text)
    text = re.sub(r'\*(.+?)\*', r'\1', text)
    text = re.sub(r'`(.+?)`', r'\1', text)
    text = re.sub(r'\[(.+?)\]\(.+?\)', r'\1', text)
    return text


def md_to_plain_text(md_content):
    """Convert markdown to plain text, removing the main heading."""
    lines = md_content.split('\n')
    result_lines = []
    skip_heading = True

    for line in lines:
        # Skip the main ## heading
        if skip_heading and line.startswith('## '):
            skip_heading = False
            continue

        # Skip horizontal rules
        if line.strip() == '---':
            continue

        # Clean the line
        cleaned = clean_inline_formatting(line)
        result_lines.append(cleaned)

    return '\n'.join(result_lines)


def batch_requests(requests, batch_size=100):
    """Split requests into smaller batches."""
    for i in range(0, len(requests), batch_size):
        yield requests[i:i + batch_size]


def main():
    client = GDocsClient()

    # Step 1: Read and convert MD
    print("=== Step 1: Read MD file ===")
    with open(MD_FILE, 'r', encoding='utf-8') as f:
        md_content = f.read()

    plain_text = md_to_plain_text(md_content)
    print(f"Plain text length: {len(plain_text)} chars")

    # Step 2: Delete existing content
    print("\n=== Step 2: Delete existing content ===")
    tab_id, section_3_2_end, section_4_start = get_tab_info(client, DOC_ID, TAB_TITLE)
    print(f"Current range: [{section_3_2_end}, {section_4_start}]")

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
        print("Deleted old content")
        time.sleep(2)

    # Step 3: Re-read to get fresh indices
    print("\n=== Step 3: Re-read indices ===")
    tab_id, section_3_2_end, section_4_start = get_tab_info(client, DOC_ID, TAB_TITLE)
    insert_index = section_3_2_end
    print(f"Insert at: {insert_index}")

    # Step 4: Insert plain text
    print("\n=== Step 4: Insert plain text ===")
    insert_requests = [{
        'insertText': {
            'location': {'index': insert_index, 'tabId': tab_id},
            'text': plain_text
        }
    }]
    client.batch_update(DOC_ID, insert_requests)
    print(f"Inserted {len(plain_text)} chars")
    time.sleep(2)

    # Step 5: Re-read to find inserted content
    print("\n=== Step 5: Find inserted content ===")
    tab = client.find_tab_by_title(DOC_ID, TAB_TITLE)
    body = tab.get('documentTab', {}).get('body', {})
    content = body.get('content', [])

    # Find our section 3.2 heading
    insert_start = None
    for element in content:
        if 'paragraph' in element:
            para = element['paragraph']
            para_text = ''
            for elem in para.get('elements', []):
                if 'textRun' in elem:
                    para_text += elem['textRun'].get('content', '')

            if '3.2. Thiết kế mô hình MVC' in para_text:
                insert_start = element['startIndex']
                print(f"Found section 3.2 at: {insert_start}")
                break

    if insert_start is None:
        print("ERROR: Could not find section 3.2")
        return

    # Step 6: Apply heading styles only
    print("\n=== Step 6: Apply heading styles ===")

    # Find all paragraphs and apply styles
    format_requests = []
    heading_count = 0

    for element in content:
        if 'paragraph' in element:
            elem_start = element['startIndex']
            elem_end = element['endIndex']

            if elem_start < insert_start:
                continue

            para = element['paragraph']
            para_text = ''
            for elem in para.get('elements', []):
                if 'textRun' in elem:
                    para_text += elem['textRun'].get('content', '')

            para_text = para_text.rstrip()

            # Stop at section 4
            if '4. Thiết kế động' in para_text:
                break

            # Apply heading styles
            if para_text.startswith('### '):
                format_requests.append({
                    'updateParagraphStyle': {
                        'range': {
                            'startIndex': elem_start,
                            'endIndex': elem_end,
                            'tabId': tab_id
                        },
                        'paragraphStyle': {'namedStyleType': 'HEADING_3'},
                        'fields': 'namedStyleType'
                    }
                })
                heading_count += 1
            elif para_text.startswith('## '):
                format_requests.append({
                    'updateParagraphStyle': {
                        'range': {
                            'startIndex': elem_start,
                            'endIndex': elem_end,
                            'tabId': tab_id
                        },
                        'paragraphStyle': {'namedStyleType': 'HEADING_2'},
                        'fields': 'namedStyleType'
                    }
                })
                heading_count += 1
            elif para_text.startswith('**1.') or para_text.startswith('**2.') or para_text.startswith('**3.') or para_text.startswith('**4.'):
                # Bold items - just reset to normal
                format_requests.append({
                    'updateParagraphStyle': {
                        'range': {
                            'startIndex': elem_start,
                            'endIndex': elem_end,
                            'tabId': tab_id
                        },
                        'paragraphStyle': {'namedStyleType': 'NORMAL_TEXT'},
                        'fields': 'namedStyleType'
                    }
                })

    print(f"Found {heading_count} headings to format")
    print(f"Total format requests: {len(format_requests)}")

    # Execute in small batches with delays
    batch_size = 20
    for i in range(0, len(format_requests), batch_size):
        batch = format_requests[i:i + batch_size]
        print(f"  Executing batch {i // batch_size + 1} ({len(batch)} requests)...")
        try:
            client.batch_update(DOC_ID, batch)
            print(f"  Batch {i // batch_size + 1} done")
        except Exception as e:
            print(f"  Batch {i // batch_size + 1} failed: {e}")
            # Wait and retry once
            time.sleep(5)
            try:
                client.batch_update(DOC_ID, batch)
                print(f"  Batch {i // batch_size + 1} done (retry)")
            except Exception as e2:
                print(f"  Batch {i // batch_size + 1} failed again: {e2}")
                return
        time.sleep(2)  # Rate limiting

    print("\n=== Done! ===")
    print("Section 3.2 has been inserted with basic formatting.")
    print("Heading styles applied (HEADING_2, HEADING_3).")
    print("Other content is NORMAL_TEXT (tables, code blocks as plain text).")


if __name__ == '__main__':
    main()
