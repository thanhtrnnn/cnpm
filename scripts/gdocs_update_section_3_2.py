"""Phase 4: Update section 3.2 in small batches with verification."""
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

    # Find section 3.2 and section 4
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


def parse_md_to_batches(md_content):
    """Parse markdown into batches (one per function a-d)."""
    # Split by function headers (### a), ### b), etc.)
    batches = []
    current_batch = None

    lines = md_content.split('\n')
    i = 0

    while i < len(lines):
        line = lines[i]

        # Skip the main heading (## III.2...)
        if line.startswith('## '):
            i += 1
            continue

        # Skip horizontal rules
        if line.strip() == '---':
            i += 1
            continue

        # Function header (### a), ### b), etc.)
        if line.startswith('### '):
            if current_batch:
                batches.append(current_batch)
            current_batch = {
                'title': line[4:].strip(),
                'content': []
            }
            i += 1
            continue

        # Content line
        if current_batch is not None:
            current_batch['content'].append(line)

        i += 1

    # Add last batch
    if current_batch:
        batches.append(current_batch)

    return batches


def clean_inline_formatting(text):
    """Remove markdown formatting markers from text."""
    text = re.sub(r'\*\*(.+?)\*\*', r'\1', text)
    text = re.sub(r'\*(.+?)\*', r'\1', text)
    text = re.sub(r'`(.+?)`', r'\1', text)
    text = re.sub(r'\[(.+?)\]\(.+?\)', r'\1', text)
    return text


def batch_to_text(batch):
    """Convert a batch to plain text for insertion."""
    lines = []
    for line in batch['content']:
        # Skip empty lines at the start
        if not lines and not line.strip():
            continue
        lines.append(line)
    return '\n'.join(lines)


def insert_batch(client, doc_id, tab_id, insert_index, text):
    """Insert a batch of text."""
    requests = [{
        'insertText': {
            'location': {'index': insert_index, 'tabId': tab_id},
            'text': text
        }
    }]
    client.batch_update(doc_id, requests)
    return len(text)


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
    client.batch_update(doc_id, requests)


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
    client.batch_update(doc_id, requests)


def apply_bold(client, doc_id, tab_id, start, end):
    """Apply bold formatting."""
    requests = [{
        'updateTextStyle': {
            'range': {
                'startIndex': start,
                'endIndex': end,
                'tabId': tab_id
            },
            'textStyle': {'bold': True},
            'fields': 'bold'
        }
    }]
    client.batch_update(doc_id, requests)


def apply_monospace(client, doc_id, tab_id, start, end):
    """Apply monospace font for code blocks."""
    requests = [{
        'updateTextStyle': {
            'range': {
                'startIndex': start,
                'endIndex': end,
                'tabId': tab_id
            },
            'textStyle': {'weightedFontFamily': {'fontFamily': 'Courier New'}},
            'fields': 'weightedFontFamily'
        }
    }]
    client.batch_update(doc_id, requests)


def format_inserted_content(client, doc_id, tab_id, start, end, original_lines):
    """Apply formatting to inserted content based on original markdown."""
    tab = client.find_tab_by_title(doc_id, TAB_TITLE)
    body = tab.get('documentTab', {}).get('body', {})
    content = body.get('content', [])

    # Find all paragraphs in our inserted range
    paragraphs = []
    for element in content:
        if 'paragraph' in element:
            elem_start = element['startIndex']
            elem_end = element['endIndex']

            if elem_start >= start and elem_start < end:
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

    print(f"  Found {len(paragraphs)} paragraphs to format")

    # Apply formatting to each paragraph
    for para in paragraphs:
        text = para['text']
        start_idx = para['start']
        end_idx = para['end']

        # Determine style based on content
        if text.startswith('### '):
            # Heading 3
            apply_heading_style(client, doc_id, tab_id, start_idx, end_idx, 'HEADING_3')
            print(f"    HEADING_3: {text[:50]}")
        elif text.startswith('**1.') or text.startswith('**2.') or text.startswith('**3.') or text.startswith('**4.'):
            # Bold numbered items
            apply_normal_style(client, doc_id, tab_id, start_idx, end_idx)
            # Apply bold to the text
            clean_text = clean_inline_formatting(text)
            if len(clean_text) < len(text):
                apply_bold(client, doc_id, tab_id, start_idx, start_idx + len(clean_text))
            print(f"    BOLD: {text[:50]}")
        elif text.startswith('|') and '|' in text[1:]:
            # Table row - keep as normal text
            apply_normal_style(client, doc_id, tab_id, start_idx, end_idx)
            print(f"    TABLE: {text[:50]}")
        elif text.startswith('- ') or text.startswith('* '):
            # Bullet item
            apply_normal_style(client, doc_id, tab_id, start_idx, end_idx)
            print(f"    BULLET: {text[:50]}")
        elif text.startswith('```') or text.startswith('@startuml') or text.startswith('@enduml'):
            # Code block
            apply_normal_style(client, doc_id, tab_id, start_idx, end_idx)
            apply_monospace(client, doc_id, tab_id, start_idx, end_idx)
            print(f"    CODE: {text[:50]}")
        else:
            # Normal text
            apply_normal_style(client, doc_id, tab_id, start_idx, end_idx)
            print(f"    NORMAL: {text[:50]}")


def verify_batch(client, doc_id, tab_title, start, end):
    """Verify inserted batch has correct formatting."""
    tab = client.find_tab_by_title(doc_id, tab_title)
    body = tab.get('documentTab', {}).get('body', {})
    content = body.get('content', [])

    print(f"\n  === Verification [{start}, {end}) ===")

    results = []
    for element in content:
        if 'paragraph' in element:
            elem_start = element['startIndex']
            elem_end = element['endIndex']

            if elem_start >= start and elem_start < end:
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
                    expected = 'HEADING_3'
                elif para_text.startswith('**') and para_text.endswith('**'):
                    expected = 'NORMAL_TEXT'  # Bold applied separately
                else:
                    expected = 'NORMAL_TEXT'

                status = '✓' if named == expected else '✗'
                results.append({
                    'text': para_text[:60],
                    'actual': named,
                    'expected': expected,
                    'status': status
                })

    # Print results
    for r in results:
        print(f"    {r['status']} {r['actual']} (expected: {r['expected']}): {r['text'][:60]}")

    # Summary
    passed = sum(1 for r in results if r['status'] == '✓')
    total = len(results)
    print(f"\n  Summary: {passed}/{total} passed")

    return passed == total


def main():
    client = GDocsClient()

    # Step 1: Read MD file
    print("=== Step 1: Read MD file ===")
    with open(MD_FILE, 'r', encoding='utf-8') as f:
        md_content = f.read()

    # Parse into batches
    batches = parse_md_to_batches(md_content)
    print(f"Parsed {len(batches)} batches:")
    for i, batch in enumerate(batches):
        text = batch_to_text(batch)
        print(f"  Batch {i+1}: {batch['title']} ({len(text)} chars)")

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
        time.sleep(1)

    # Step 3: Insert batches one by one
    print("\n=== Step 3: Insert batches ===")
    current_index = section_3_2_end

    for i, batch in enumerate(batches):
        print(f"\n--- Batch {i+1}: {batch['title']} ---")

        # Re-read to get fresh indices
        tab_id, section_3_2_end, section_4_start = get_tab_info(client, DOC_ID, TAB_TITLE)
        current_index = section_3_2_end

        # Insert batch
        text = batch_to_text(batch)
        chars_inserted = insert_batch(client, DOC_ID, tab_id, current_index, text)
        print(f"  Inserted {chars_inserted} chars at index {current_index}")
        time.sleep(1)

        # Re-read to get new indices
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

                if batch['title'] in para_text:
                    inserted_start = element['startIndex']
                if inserted_start and i < len(batches) - 1:
                    # Find end of this batch (start of next batch or section 4)
                    next_batch_title = batches[i + 1]['title'] if i + 1 < len(batches) else None
                    if next_batch_title and next_batch_title in para_text:
                        inserted_end = element['startIndex']
                        break
                    elif '4. Thiết kế động' in para_text:
                        inserted_end = element['startIndex']
                        break

        if inserted_start is None:
            print("  ERROR: Could not find inserted content")
            continue

        if inserted_end is None:
            # Use end of document or section 4
            inserted_end = section_4_start if section_4_start else current_index + len(text)

        print(f"  Content range: [{inserted_start}, {inserted_end}]")

        # Apply formatting
        print("  Applying formatting...")
        format_inserted_content(client, DOC_ID, tab_id, inserted_start, inserted_end, batch['content'])
        time.sleep(0.5)

        # Verify
        success = verify_batch(client, DOC_ID, TAB_TITLE, inserted_start, inserted_end)

        if not success:
            print(f"\n  ✗ Batch {i+1} failed verification!")
            print("  Fix issues before continuing.")
            return

        print(f"\n  ✓ Batch {i+1} passed!")

    print("\n=== All batches completed successfully! ===")


if __name__ == '__main__':
    main()
