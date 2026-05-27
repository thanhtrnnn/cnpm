"""Insert section 3.2 with proper formatting - v2 approach.

Strategy:
1. Insert raw markdown text (with markers)
2. Apply formatting based on markers
3. Clean markers

This ensures formatting is applied to correct positions.
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


def parse_markdown(md_text):
    """Parse markdown into structured blocks."""
    lines = md_text.split('\n')
    blocks = []
    i = 0

    while i < len(lines):
        line = lines[i]

        # Skip empty lines
        if not line.strip():
            i += 1
            continue

        # Skip horizontal rules
        if re.match(r'^[\s]*[-*_]{3,}\s*$', line):
            i += 1
            continue

        # Heading (## or ###)
        heading_match = re.match(r'^(#{2,3})\s+(.+)$', line)
        if heading_match:
            level = len(heading_match.group(1))
            text = heading_match.group(2).strip()
            blocks.append({'type': 'heading', 'level': level, 'text': text})
            i += 1
            continue

        # Table (starts with |, next line is separator)
        if line.strip().startswith('|') and i + 1 < len(lines) and re.match(r'^\|[\s\-:|]+\|$', lines[i + 1].strip()):
            table_lines = []
            j = i
            while j < len(lines) and lines[j].strip().startswith('|'):
                table_lines.append(lines[j])
                j += 1
            blocks.append({'type': 'table', 'lines': table_lines})
            i = j
            continue

        # PlantUML code block
        if line.strip().startswith('```plantuml'):
            code_lines = []
            j = i + 1
            while j < len(lines) and not lines[j].strip().startswith('```'):
                code_lines.append(lines[j])
                j += 1
            blocks.append({'type': 'plantuml', 'code': '\n'.join(code_lines)})
            i = j + 1
            continue

        # Regular code block
        if line.strip().startswith('```'):
            code_lines = []
            j = i + 1
            while j < len(lines) and not lines[j].strip().startswith('```'):
                code_lines.append(lines[j])
                j += 1
            blocks.append({'type': 'code', 'code': '\n'.join(code_lines)})
            i = j + 1
            continue

        # List item (starts with - or *)
        if re.match(r'^[\s]*[-*]\s+', line):
            blocks.append({'type': 'list_item', 'text': line.rstrip()})
            i += 1
            continue

        # Paragraph
        if line.strip():
            blocks.append({'type': 'paragraph', 'text': line.rstrip()})
        i += 1

    return blocks


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


def insert_raw_text(client, doc_id, tab_id, index, text):
    """Insert text without cleaning markdown markers."""
    requests = [{
        'insertText': {
            'location': {'index': index, 'tabId': tab_id},
            'text': text
        }
    }]
    client.batch_update(doc_id, requests)
    return len(text)


def apply_style(client, doc_id, tab_id, start, end, style):
    """Apply paragraph style."""
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


def apply_bold(client, doc_id, tab_id, start, end):
    """Apply bold text style."""
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
    """Apply monospace font for code."""
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


def delete_text(client, doc_id, tab_id, start, end):
    """Delete text in range."""
    requests = [{
        'deleteContentRange': {
            'range': {
                'startIndex': start,
                'endIndex': end,
                'tabId': tab_id
            }
        }
    }]
    client.batch_update(doc_id, requests)


def main():
    client = GDocsClient()

    # Step 1: Parse markdown
    print("=" * 60)
    print("STEP 1: Parse markdown")
    print("=" * 60)

    with open(MD_FILE, 'r', encoding='utf-8') as f:
        md_content = f.read()

    blocks = parse_markdown(md_content)
    print(f"Parsed {len(blocks)} blocks")

    # Step 2: Delete old content
    print("\n" + "=" * 60)
    print("STEP 2: Delete old content")
    print("=" * 60)

    tab_id, insert_start, section_4_start = get_tab_info(client, DOC_ID, TAB_TITLE)
    print(f"Range: [{insert_start}, {section_4_start}]")

    delete_text(client, DOC_ID, tab_id, insert_start, section_4_start)
    time.sleep(2)

    # Re-read
    tab_id, insert_start, _ = get_tab_info(client, DOC_ID, TAB_TITLE)
    current_index = insert_start
    print(f"Fresh index: {current_index}")

    # Step 3: Insert all content as raw text
    print("\n" + "=" * 60)
    print("STEP 3: Insert raw text with markers")
    print("=" * 60)

    # Track positions for formatting
    positions = []

    for i, block in enumerate(blocks):
        try:
            if block['type'] == 'heading':
                text = block['text'] + '\n'
                char_count = insert_raw_text(client, DOC_ID, tab_id, current_index, text)
                positions.append({
                    'type': 'heading',
                    'level': block['level'],
                    'start': current_index,
                    'end': current_index + char_count,
                    'text': block['text']
                })
                print(f"  [{i}] HEADING_{block['level']}: {block['text'][:50]}")
                current_index += char_count
                time.sleep(0.5)

            elif block['type'] == 'paragraph':
                text = block['text'] + '\n'
                char_count = insert_raw_text(client, DOC_ID, tab_id, current_index, text)
                positions.append({
                    'type': 'paragraph',
                    'start': current_index,
                    'end': current_index + char_count,
                    'text': block['text']
                })
                print(f"  [{i}] PARA: {block['text'][:50]}")
                current_index += char_count
                time.sleep(0.5)

            elif block['type'] == 'list_item':
                text = block['text'] + '\n'
                char_count = insert_raw_text(client, DOC_ID, tab_id, current_index, text)
                positions.append({
                    'type': 'list_item',
                    'start': current_index,
                    'end': current_index + char_count,
                    'text': block['text']
                })
                print(f"  [{i}] LIST: {block['text'][:50]}")
                current_index += char_count
                time.sleep(0.5)

            elif block['type'] == 'table':
                # Insert table as pipe-separated text
                table_text = ''
                for line in block['lines']:
                    table_text += line + '\n'
                char_count = insert_raw_text(client, DOC_ID, tab_id, current_index, table_text)
                positions.append({
                    'type': 'table',
                    'start': current_index,
                    'end': current_index + char_count,
                    'lines': block['lines']
                })
                print(f"  [{i}] TABLE: {len(block['lines'])} lines")
                current_index += char_count
                time.sleep(0.5)

            elif block['type'] == 'plantuml':
                text = '```plantuml\n' + block['code'] + '\n```\n'
                char_count = insert_raw_text(client, DOC_ID, tab_id, current_index, text)
                positions.append({
                    'type': 'plantuml',
                    'start': current_index,
                    'end': current_index + char_count,
                    'code': block['code']
                })
                print(f"  [{i}] PLANTUML: {len(block['code'])} chars")
                current_index += char_count
                time.sleep(0.5)

            elif block['type'] == 'code':
                text = '```\n' + block['code'] + '\n```\n'
                char_count = insert_raw_text(client, DOC_ID, tab_id, current_index, text)
                positions.append({
                    'type': 'code',
                    'start': current_index,
                    'end': current_index + char_count,
                    'code': block['code']
                })
                print(f"  [{i}] CODE: {len(block['code'])} chars")
                current_index += char_count
                time.sleep(0.5)

        except Exception as e:
            print(f"  [{i}] ERROR: {e}")
            time.sleep(5)
            continue

    # Step 4: Apply formatting
    print("\n" + "=" * 60)
    print("STEP 4: Apply formatting")
    print("=" * 60)

    for pos in positions:
        try:
            if pos['type'] == 'heading':
                style = f"HEADING_{pos['level']}"
                apply_style(client, DOC_ID, tab_id, pos['start'], pos['end'], style)
                print(f"  {style}: {pos['text'][:50]}")
                time.sleep(0.5)

            elif pos['type'] == 'list_item':
                apply_style(client, DOC_ID, tab_id, pos['start'], pos['end'], 'NORMAL_TEXT')
                apply_bullet(client, DOC_ID, tab_id, pos['start'], pos['end'])
                print(f"  BULLET: {pos['text'][:50]}")
                time.sleep(0.5)

            elif pos['type'] == 'paragraph':
                apply_style(client, DOC_ID, tab_id, pos['start'], pos['end'], 'NORMAL_TEXT')
                # Apply bold for **text**
                for match in re.finditer(r'\*\*(.+?)\*\*', pos['text']):
                    clean_before = pos['text'][:match.start()]
                    bold_text = match.group(1)
                    start = pos['start'] + len(clean_before)
                    end = start + len(bold_text)
                    apply_bold(client, DOC_ID, tab_id, start, end)
                    time.sleep(0.3)
                # Apply code for `text`
                for match in re.finditer(r'`(.+?)`', pos['text']):
                    clean_before = pos['text'][:match.start()].replace('**', '')
                    code_text = match.group(1)
                    start = pos['start'] + len(clean_before)
                    end = start + len(code_text)
                    apply_code_font(client, DOC_ID, tab_id, start, end)
                    time.sleep(0.3)
                print(f"  NORMAL + inline: {pos['text'][:50]}")
                time.sleep(0.5)

            elif pos['type'] == 'plantuml' or pos['type'] == 'code':
                apply_style(client, DOC_ID, tab_id, pos['start'], pos['end'], 'NORMAL_TEXT')
                apply_code_font(client, DOC_ID, tab_id, pos['start'], pos['end'])
                print(f"  CODE_FONT: {pos['type']}")
                time.sleep(0.5)

        except Exception as e:
            print(f"  ERROR applying format: {e}")
            time.sleep(5)
            continue

    # Step 5: Clean markdown markers
    print("\n" + "=" * 60)
    print("STEP 5: Clean markdown markers")
    print("=" * 60)

    # Re-read to get fresh positions
    tab = client.find_tab_by_title(DOC_ID, TAB_TITLE)
    body = tab.get('documentTab', {}).get('body', {})
    content = body.get('content', [])

    found_3_2 = False
    clean_requests = []

    for element in content:
        if 'paragraph' in element:
            para = element['paragraph']
            para_text = ''
            for elem in para.get('elements', []):
                if 'textRun' in elem:
                    para_text += elem['textRun'].get('content', '')

            if '3.2. Thiết kế mô hình MVC' in para_text:
                found_3_2 = True
            if found_3_2 and '4. Thiết kế động' in para_text:
                break

            if found_3_2 and para_text.strip():
                # Clean **text** -> text
                if '**' in para_text:
                    clean_text = re.sub(r'\*\*(.+?)\*\*', r'\1', para_text)
                    if clean_text != para_text:
                        # Find the range to delete
                        start = element['startIndex']
                        end = element['endIndex']
                        # We'll need to delete and re-insert
                        clean_requests.append({
                            'start': start,
                            'end': end,
                            'old_text': para_text,
                            'new_text': clean_text
                        })

    print(f"Found {len(clean_requests)} paragraphs to clean")

    # Execute clean requests (delete old, insert new)
    for req in clean_requests:
        try:
            # Delete old text
            delete_text(client, DOC_ID, tab_id, req['start'], req['end'])
            time.sleep(0.3)
            # Insert clean text
            insert_raw_text(client, DOC_ID, tab_id, req['start'], req['new_text'])
            time.sleep(0.3)
        except Exception as e:
            print(f"  ERROR cleaning: {e}")
            time.sleep(5)
            continue

    print("\n=== Done! ===")


if __name__ == '__main__':
    main()
