"""Insert section 3.2 with proper Google Docs formatting.

Strategy:
1. Parse markdown into structured blocks
2. Delete old section 3.2 content
3. Insert blocks one by one with proper formatting:
   - Headings: HEADING_2/HEADING_3 styles
   - Tables: insertTable + populate cells
   - PlantUML: render to PNG → insert as images
   - Paragraphs: NORMAL_TEXT with inline formatting
4. Verify after each major step
"""
import sys
import os
import re
import time
import json

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '.claude', 'skills', 'gdocs'))

from scripts.client import GDocsClient
from scripts.plantuml_renderer import render_plantuml_to_png

DOC_ID = '1H0pFNhmbX9yDMObxERGsZ0RqKjpX9Je6N60n4tYrB6s'
TAB_TITLE = 'Dịch vụ & Sản phẩm'
MD_FILE = os.path.join(os.path.dirname(__file__), '..', 'docs', 'tabs', 'section-3.2-mvc.md')


# ─── Markdown Parser ───────────────────────────────────────────────

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
            i = j + 1  # Skip closing ```
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

        # List item (starts with - or * after optional whitespace)
        if re.match(r'^[\s]*[-*]\s+', line):
            blocks.append({'type': 'list_item', 'text': line.strip()})
            i += 1
            continue

        # Paragraph (single line, not a list item)
        if line.strip():
            blocks.append({'type': 'paragraph', 'text': line.strip()})
        i += 1

    return blocks


# ─── Table Parser ──────────────────────────────────────────────────

def parse_table(table_lines):
    """Parse markdown table into rows of cells."""
    rows = []
    for line in table_lines:
        line = line.strip()
        if not line.startswith('|'):
            continue
        # Skip separator line
        if re.match(r'^\|[\s\-:|]+\|$', line):
            continue
        cells = [c.strip() for c in line.split('|')[1:-1]]
        rows.append(cells)
    return rows


# ─── Google Docs Insertion ─────────────────────────────────────────

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
                section_3_2_start = element['endIndex']  # Insert after heading

            if section_3_2_start and '4. Thiết kế động' in para_text:
                section_4_start = element['startIndex']
                break

    return tab_id, section_3_2_start, section_4_start


def delete_section(client, doc_id, tab_id, start, end):
    """Delete content in range."""
    if end <= start:
        return
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
    print(f"  Deleted [{start}, {end})")


def cleanup_empty_headings(client, doc_id, tab_title):
    """Reset empty HEADING_2 paragraphs to NORMAL_TEXT."""
    tab = client.find_tab_by_title(doc_id, tab_title)
    body = tab.get('documentTab', {}).get('body', {})
    content = body.get('content', [])

    found_3_2 = False
    reset_requests = []

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

            if found_3_2 and named.startswith('HEADING') and not para_text.strip():
                reset_requests.append({
                    'updateParagraphStyle': {
                        'range': {
                            'startIndex': element['startIndex'],
                            'endIndex': element['endIndex'],
                            'tabId': tab['tabProperties']['tabId']
                        },
                        'paragraphStyle': {'namedStyleType': 'NORMAL_TEXT'},
                        'fields': 'namedStyleType'
                    }
                })

    if reset_requests:
        print(f"  Resetting {len(reset_requests)} empty headings...")
        # Execute in batches
        batch_size = 50
        for i in range(0, len(reset_requests), batch_size):
            batch = reset_requests[i:i + batch_size]
            client.batch_update(doc_id, batch)
            time.sleep(1)
        print(f"  Done")


def insert_text(client, doc_id, tab_id, index, text):
    """Insert plain text at index. Returns number of chars inserted."""
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


def insert_table_with_content(client, doc_id, tab_id, index, rows):
    """Insert a table and populate cells with content.

    Returns the index after the table.
    """
    if not rows:
        return index

    num_rows = len(rows)
    num_cols = max(len(row) for row in rows)

    # Pad rows
    for row in rows:
        while len(row) < num_cols:
            row.append('')

    # Step 1: Insert table structure
    requests = [{
        'insertTable': {
            'location': {'index': index, 'tabId': tab_id},
            'rows': num_rows,
            'columns': num_cols
        }
    }]
    client.batch_update(doc_id, requests)
    time.sleep(0.5)

    # Step 2: Re-read to get actual cell indices
    tab = client.find_tab_by_title(doc_id, TAB_TITLE)
    body = tab.get('documentTab', {}).get('body', {})
    content = body.get('content', [])

    # Find the table element
    table_element = None
    for element in content:
        if 'table' in element:
            if element['startIndex'] >= index - 5:  # Allow small margin
                table_element = element
                break

    if not table_element:
        print(f"  WARNING: Could not find table at index {index}")
        # Estimate table end based on formula
        table_end = index + num_rows * (num_cols * 2 + 1) + 1
        return table_end

    # Step 3: Populate cells
    # Google Docs table structure:
    # - Table starts with tableStart marker
    # - Each row starts with rowStart marker
    # - Each cell starts with cellStart marker
    # - Each cell contains a paragraph with the content
    # - Cell content is between cellStart+1 and cellEnd-1

    table_start = table_element['startIndex']
    table_end = table_element['endIndex']

    # Find all paragraphs within the table
    cell_paragraphs = []
    for element in content:
        if 'paragraph' in element:
            elem_start = element['startIndex']
            if elem_start > table_start and elem_start < table_end:
                para = element['paragraph']
                para_text = ''
                for elem in para.get('elements', []):
                    if 'textRun' in elem:
                        para_text += elem['textRun'].get('content', '')
                # Empty paragraphs in cells (just newline)
                if para_text.strip() == '' or para_text == '\n':
                    cell_paragraphs.append({
                        'start': elem_start,
                        'end': element['endIndex']
                    })

    # Populate cells with content
    cell_idx = 0
    for row_idx, row in enumerate(rows):
        for col_idx, cell_text in enumerate(row):
            if cell_idx < len(cell_paragraphs) and cell_text.strip():
                cell_para = cell_paragraphs[cell_idx]
                # Insert text into cell (at cell start, before the newline)
                insert_index = cell_para['start']
                text = clean_inline_formatting(cell_text) + '\n'
                try:
                    insert_text(client, doc_id, tab_id, insert_index, text)
                    time.sleep(1)
                except Exception as e:
                    print(f"  WARNING: Failed to insert cell [{row_idx},{col_idx}]: {e}")
            cell_idx += 1

    return table_end


def insert_image_at_index(client, doc_id, tab_id, index, image_path, width=600, height=400):
    """Insert an image at the specified index."""
    # First insert a placeholder newline
    placeholder = '\n'
    insert_text(client, doc_id, tab_id, index, placeholder)
    time.sleep(0.5)

    # Re-read to get the actual index
    tab = client.find_tab_by_title(doc_id, TAB_TITLE)
    body = tab.get('documentTab', {}).get('body', {})
    content = body.get('content', [])

    # Find our inserted newline
    for element in content:
        if 'paragraph' in element:
            if element['startIndex'] == index:
                # Insert image at this position
                client.insert_image(doc_id, index, image_path, width, height)
                return index + 1

    # Fallback: insert at original index
    client.insert_image(doc_id, index, image_path, width, height)
    return index + 1


def clean_inline_formatting(text):
    """Remove markdown formatting markers."""
    text = re.sub(r'\*\*(.+?)\*\*', r'\1', text)
    text = re.sub(r'\*(.+?)\*', r'\1', text)
    text = re.sub(r'`(.+?)`', r'\1', text)
    text = re.sub(r'\[(.+?)\]\(.+?\)', r'\1', text)
    return text


# ─── Main Insertion Logic ──────────────────────────────────────────

def main():
    client = GDocsClient()

    # Step 1: Read and parse markdown
    print("=" * 60)
    print("STEP 1: Parse markdown")
    print("=" * 60)

    with open(MD_FILE, 'r', encoding='utf-8') as f:
        md_content = f.read()

    blocks = parse_markdown(md_content)
    print(f"Parsed {len(blocks)} blocks:")
    type_counts = {}
    for b in blocks:
        t = b['type']
        type_counts[t] = type_counts.get(t, 0) + 1
    for t, c in type_counts.items():
        print(f"  {t}: {c}")

    # Step 2: Get current state and delete old content
    print("\n" + "=" * 60)
    print("STEP 2: Delete old section 3.2 content")
    print("=" * 60)

    tab_id, insert_start, section_4_start = get_tab_info(client, DOC_ID, TAB_TITLE)
    print(f"Insert start: {insert_start}")
    print(f"Section 4 start: {section_4_start}")

    delete_section(client, DOC_ID, tab_id, insert_start, section_4_start)
    time.sleep(1)

    # Cleanup any remaining empty headings
    cleanup_empty_headings(client, DOC_ID, TAB_TITLE)
    time.sleep(1)

    # Re-read to get fresh index
    tab_id, insert_start, _ = get_tab_info(client, DOC_ID, TAB_TITLE)
    current_index = insert_start
    print(f"Fresh insert index: {current_index}")

    # Step 3: Render PlantUML diagrams first (to avoid index shifting later)
    print("\n" + "=" * 60)
    print("STEP 3: Pre-render PlantUML diagrams")
    print("=" * 60)

    plantuml_images = {}
    for i, block in enumerate(blocks):
        if block['type'] == 'plantuml':
            print(f"  Rendering PlantUML block {i}...")
            try:
                image_path = render_plantuml_to_png(block['code'])
                plantuml_images[i] = image_path
                print(f"    -> {image_path}")
            except Exception as e:
                print(f"    FAILED: {e}")
                plantuml_images[i] = None

    # Step 4: Insert content block by block
    print("\n" + "=" * 60)
    print("STEP 4: Insert content blocks")
    print("=" * 60)

    for i, block in enumerate(blocks):
        block_type = block['type']

        try:
            if block_type == 'heading':
                # Insert heading text (without ### prefix)
                text = block['text'] + '\n'
                char_count = insert_text(client, DOC_ID, tab_id, current_index, text)
                time.sleep(1)

                # Apply heading style
                style = f"HEADING_{block['level']}"
                apply_style(client, DOC_ID, tab_id, current_index, current_index + char_count, style)
                time.sleep(1)

                print(f"  [{i}] HEADING_{block['level']}: {block['text'][:50]}")
                current_index += char_count

            elif block_type == 'table':
                rows = parse_table(block['lines'])
                if rows:
                    # Insert a newline before table
                    insert_text(client, DOC_ID, tab_id, current_index, '\n')
                    time.sleep(1)
                    current_index += 1

                    table_end = insert_table_with_content(client, DOC_ID, tab_id, current_index, rows)
                    print(f"  [{i}] TABLE: {len(rows)} rows x {max(len(r) for r in rows)} cols")
                    current_index = table_end

                    # Insert newline after table
                    insert_text(client, DOC_ID, tab_id, current_index, '\n')
                    time.sleep(1)
                    current_index += 1

            elif block_type == 'plantuml':
                image_path = plantuml_images.get(i)
                if image_path and os.path.exists(image_path):
                    # Insert newline before image
                    insert_text(client, DOC_ID, tab_id, current_index, '\n')
                    time.sleep(1)
                    current_index += 1

                    # Insert image
                    client.insert_image(DOC_ID, current_index, image_path, width_px=600, height_px=400)
                    time.sleep(1)
                    print(f"  [{i}] IMAGE: {os.path.basename(image_path)}")
                    current_index += 1  # Image takes 1 character

                    # Insert newline after image
                    insert_text(client, DOC_ID, tab_id, current_index, '\n')
                    time.sleep(1)
                    current_index += 1
                else:
                    # Fallback: insert as code block
                    text = block['code'] + '\n'
                    char_count = insert_text(client, DOC_ID, tab_id, current_index, text)
                    time.sleep(1)
                    print(f"  [{i}] CODE (fallback): PlantUML block")
                    current_index += char_count

            elif block_type == 'code':
                text = block['code'] + '\n'
                char_count = insert_text(client, DOC_ID, tab_id, current_index, text)
                time.sleep(1)

                # Apply monospace font
                apply_code_font(client, DOC_ID, tab_id, current_index, current_index + char_count)
                time.sleep(1)

                print(f"  [{i}] CODE: {block['code'][:50]}")
                current_index += char_count

            elif block_type == 'paragraph':
                text = clean_inline_formatting(block['text']) + '\n'
                char_count = insert_text(client, DOC_ID, tab_id, current_index, text)
                time.sleep(1)

                # Reset to NORMAL_TEXT
                apply_style(client, DOC_ID, tab_id, current_index, current_index + char_count, 'NORMAL_TEXT')
                time.sleep(1)

                # Apply inline formatting (bold, code)
                apply_inline_formatting(client, DOC_ID, tab_id, current_index, block['text'])
                time.sleep(1)

                print(f"  [{i}] PARA: {block['text'][:50]}")
                current_index += char_count

            elif block_type == 'list_item':
                # Remove leading whitespace and bullet marker
                text = re.sub(r'^[\s]*[-*]\s+', '', block['text'])
                text = clean_inline_formatting(text) + '\n'
                char_count = insert_text(client, DOC_ID, tab_id, current_index, text)
                time.sleep(1)

                # Reset to NORMAL_TEXT
                apply_style(client, DOC_ID, tab_id, current_index, current_index + char_count, 'NORMAL_TEXT')
                time.sleep(1)

                # Apply bullet formatting
                try:
                    requests = [{
                        'createParagraphBullets': {
                            'range': {
                                'startIndex': current_index,
                                'endIndex': current_index + char_count,
                                'tabId': tab_id
                            },
                            'bulletPreset': 'BULLET_DISC_CIRCLE_SQUARE'
                        }
                    }]
                    client.batch_update(DOC_ID, requests)
                    time.sleep(1)
                except Exception as e:
                    print(f"    WARNING: Failed to apply bullet: {e}")

                # Apply inline formatting
                apply_inline_formatting(client, DOC_ID, tab_id, current_index, block['text'])
                time.sleep(1)

                print(f"  [{i}] LIST: {block['text'][:50]}")
                current_index += char_count

        except Exception as e:
            print(f"  [{i}] ERROR: {e}")
            # Continue with next block
            continue

    # Step 5: Final verification
    print("\n" + "=" * 60)
    print("STEP 5: Verification")
    print("=" * 60)

    verify_result = verify_section(client, DOC_ID, TAB_TITLE)
    print(f"Verification: {'PASS' if verify_result else 'FAIL'}")

    print("\nDone!")


def apply_inline_formatting(client, doc_id, tab_id, base_index, original_text):
    """Apply bold and code formatting based on original markdown text."""
    # Find bold markers **text**
    for match in re.finditer(r'\*\*(.+?)\*\*', original_text):
        # Calculate offset in cleaned text
        clean_before = clean_inline_formatting(original_text[:match.start()])
        clean_match = clean_inline_formatting(match.group(1))
        start = base_index + len(clean_before)
        end = start + len(clean_match)
        try:
            apply_bold(client, doc_id, tab_id, start, end)
        except Exception:
            pass  # Skip if range is invalid

    # Find code markers `text`
    for match in re.finditer(r'`(.+?)`', original_text):
        clean_before = clean_inline_formatting(original_text[:match.start()])
        clean_match = clean_inline_formatting(match.group(1))
        start = base_index + len(clean_before)
        end = start + len(clean_match)
        try:
            apply_code_font(client, doc_id, tab_id, start, end)
        except Exception:
            pass


def verify_section(client, doc_id, tab_title):
    """Verify section 3.2 has correct formatting."""
    tab = client.find_tab_by_title(doc_id, tab_title)
    body = tab.get('documentTab', {}).get('body', {})
    content = body.get('content', [])

    found_3_2 = False
    stats = {
        'headings': 0,
        'tables': 0,
        'images': 0,
        'paragraphs': 0,
        'empty_headings': 0
    }

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
                print(f"  Found section 3.2 at [{element['startIndex']}]")
                continue

            if found_3_2:
                if '4. Thiết kế động' in para_text:
                    print(f"  Found section 4 at [{element['startIndex']}]")
                    break

                if named.startswith('HEADING'):
                    stats['headings'] += 1
                    if not para_text.strip():
                        stats['empty_headings'] += 1
                    print(f"    {named}: {para_text.rstrip()[:60]}")
                elif para_text.strip():
                    stats['paragraphs'] += 1

        elif 'table' in element:
            if found_3_2:
                stats['tables'] += 1
                print(f"    TABLE at [{element['startIndex']}]")

        elif 'inlineObjectElement' in element:
            if found_3_2:
                stats['images'] += 1
                print(f"    IMAGE at [{element['startIndex']}]")

    print(f"\n  Stats:")
    print(f"    Headings: {stats['headings']}")
    print(f"    Empty headings: {stats['empty_headings']}")
    print(f"    Tables: {stats['tables']}")
    print(f"    Images: {stats['images']}")
    print(f"    Paragraphs: {stats['paragraphs']}")

    return stats['tables'] > 0 or stats['images'] > 0


if __name__ == '__main__':
    main()
