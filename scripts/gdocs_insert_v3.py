"""Insert section 3.2 - v3 simplified approach.

Strategy:
1. Delete old content
2. Insert each function (a-d) as a single chunk
3. Apply formatting after each chunk
4. No cleanup step (avoid index shifting issues)
"""
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

    section_3_2_start = None
    section_4_start = None

    for element in content:
        if 'paragraph' in element:
            para = element['paragraph']
            para_text = ''
            for elem in para.get('elements', []):
                if 'textRun' in elem:
                    para_text += elem['textRun'].get('content', '')

            if '3.2. Thiết kế mô hình MVC' in para_text:
                section_3_2_start = element['endIndex']

            if section_3_2_start and '4. Thiết kế động' in para_text:
                section_4_start = element['startIndex']
                break

    return tab_id, section_3_2_start, section_4_start


def split_into_functions(md_content):
    """Split markdown into function blocks (a, b, c, d)."""
    # Remove the main ## heading
    lines = md_content.split('\n')
    content_start = 0
    for i, line in enumerate(lines):
        if line.startswith('## '):
            content_start = i + 1
            break

    content = '\n'.join(lines[content_start:]).strip()

    # Split by ### headers
    functions = []
    current_func = None

    for line in content.split('\n'):
        if line.startswith('### '):
            if current_func:
                functions.append(current_func)
            current_func = {
                'title': line[4:].strip(),
                'lines': []
            }
        elif current_func is not None:
            current_func['lines'].append(line)

    if current_func:
        functions.append(current_func)

    return functions


def insert_chunk(client, doc_id, tab_id, index, text):
    """Insert a chunk of text."""
    requests = [{
        'insertText': {
            'location': {'index': index, 'tabId': tab_id},
            'text': text
        }
    }]
    client.batch_update(doc_id, requests)
    return len(text)


def apply_heading(client, doc_id, tab_id, start, end, level):
    """Apply heading style."""
    requests = [{
        'updateParagraphStyle': {
            'range': {
                'startIndex': start,
                'endIndex': end,
                'tabId': tab_id
            },
            'paragraphStyle': {'namedStyleType': f'HEADING_{level}'},
            'fields': 'namedStyleType'
        }
    }]
    client.batch_update(doc_id, requests)


def apply_normal(client, doc_id, tab_id, start, end):
    """Apply NORMAL_TEXT style."""
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


def apply_bullet(client, doc_id, tab_id, start, end):
    """Apply bullet formatting."""
    requests = [{
        'createParagraphBullets': {
            'range': {
                'startIndex': start,
                'endIndex': end,
                'tabId': tab_id
            },
            'bulletPreset': 'BULLET_DISC_CIRCLE_SQUARE'
        }
    }]
    client.batch_update(doc_id, requests)


def apply_bold(client, doc_id, tab_id, start, end):
    """Apply bold."""
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


def apply_code_font(client, doc_id, tab_id, start, end):
    """Apply monospace font."""
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


def format_chunk(client, doc_id, tab_id, start, end, text):
    """Apply formatting to a chunk of text."""
    # Split into lines and format each
    lines = text.split('\n')
    current = start

    for line in lines:
        line_end = current + len(line) + 1  # +1 for newline

        if line.startswith('### '):
            # Heading
            apply_heading(client, doc_id, tab_id, current, line_end, 3)
            time.sleep(0.3)
        elif line.startswith('- ') or line.startswith('  - '):
            # List item
            apply_normal(client, doc_id, tab_id, current, line_end)
            apply_bullet(client, doc_id, tab_id, current, line_end)
            time.sleep(0.3)
        elif line.startswith('|') and '|' in line[1:]:
            # Table row
            apply_normal(client, doc_id, tab_id, current, line_end)
            time.sleep(0.3)
        elif line.startswith('```'):
            # Code block
            apply_normal(client, doc_id, tab_id, current, line_end)
            apply_code_font(client, doc_id, tab_id, current, line_end)
            time.sleep(0.3)
        elif line.strip():
            # Regular paragraph
            apply_normal(client, doc_id, tab_id, current, line_end)
            # Apply bold for **text**
            for match in re.finditer(r'\*\*(.+?)\*\*', line):
                bold_start = current + match.start()
                bold_end = bold_start + len(match.group(1))
                apply_bold(client, doc_id, tab_id, bold_start, bold_end)
                time.sleep(0.2)
            # Apply code for `text`
            for match in re.finditer(r'`(.+?)`', line):
                code_start = current + match.start()
                code_end = code_start + len(match.group(1))
                apply_code_font(client, doc_id, tab_id, code_start, code_end)
                time.sleep(0.2)

        current = line_end


def main():
    client = GDocsClient()

    # Step 1: Read and split markdown
    print("=" * 60)
    print("STEP 1: Read and split markdown")
    print("=" * 60)

    with open(MD_FILE, 'r', encoding='utf-8') as f:
        md_content = f.read()

    functions = split_into_functions(md_content)
    print(f"Split into {len(functions)} functions:")
    for func in functions:
        text = '\n'.join(func['lines'])
        print(f"  {func['title']}: {len(text)} chars")

    # Step 2: Delete old content
    print("\n" + "=" * 60)
    print("STEP 2: Delete old content")
    print("=" * 60)

    tab_id, insert_start, section_4_start = get_tab_info(client, DOC_ID, TAB_TITLE)
    print(f"Range: [{insert_start}, {section_4_start}]")

    requests = [{
        'deleteContentRange': {
            'range': {
                'startIndex': insert_start,
                'endIndex': section_4_start,
                'tabId': tab_id
            }
        }
    }]
    client.batch_update(DOC_ID, requests)
    time.sleep(2)

    # Re-read
    tab_id, insert_start, _ = get_tab_info(client, DOC_ID, TAB_TITLE)
    current_index = insert_start
    print(f"Fresh index: {current_index}")

    # Step 3: Insert introduction paragraph
    print("\n" + "=" * 60)
    print("STEP 3: Insert introduction")
    print("=" * 60)

    intro = "Mô hình MVC được thiết kế theo kiến trúc BCE (Boundary – Control – Entity) với 3 tầng:\n"
    intro += "- Boundary (Giao diện): React components xử lý giao diện người dùng\n"
    intro += "- Control (DAO): Spring Boot Controllers + JPA Repositories xử lý nghiệp vụ và truy cập dữ liệu\n"
    intro += "- Entity (Thực thể): JPA Entities biểu diễn dữ liệu lưu trữ\n"

    char_count = insert_chunk(client, DOC_ID, tab_id, current_index, intro)
    format_chunk(client, DOC_ID, tab_id, current_index, current_index + char_count, intro)
    print(f"Inserted and formatted introduction ({char_count} chars)")
    current_index += char_count
    time.sleep(2)

    # Step 4: Insert each function
    print("\n" + "=" * 60)
    print("STEP 4: Insert functions")
    print("=" * 60)

    for i, func in enumerate(functions):
        print(f"\n--- Function {i+1}: {func['title']} ---")

        # Build text for this function
        text = func['title'] + '\n' + '\n'.join(func['lines']) + '\n'

        # Insert
        try:
            char_count = insert_chunk(client, DOC_ID, tab_id, current_index, text)
            print(f"  Inserted {char_count} chars")
            time.sleep(1)

            # Format
            format_chunk(client, DOC_ID, tab_id, current_index, current_index + char_count, text)
            print(f"  Formatted")
            time.sleep(1)

            current_index += char_count

        except Exception as e:
            print(f"  ERROR: {e}")
            time.sleep(5)
            continue

    # Step 5: Verify
    print("\n" + "=" * 60)
    print("STEP 5: Verify")
    print("=" * 60)

    tab = client.find_tab_by_title(DOC_ID, TAB_TITLE)
    body = tab.get('documentTab', {}).get('body', {})
    content = body.get('content', [])

    found_3_2 = False
    stats = {'tables': 0, 'headings': 0, 'lists': 0, 'paragraphs': 0}
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
            if found_3_2 and '4. Thiết kế động' in para_text:
                break
            if found_3_2:
                if named.startswith('HEADING'):
                    stats['headings'] += 1
                elif para_text.strip():
                    stats['paragraphs'] += 1
                    if para_text.startswith('- '):
                        stats['lists'] += 1
        elif 'table' in element and found_3_2:
            stats['tables'] += 1

    print(f"Stats: {stats}")
    print("\nDone!")


if __name__ == '__main__':
    main()
