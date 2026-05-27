"""Insert section 3.2 using two-pass approach: plain text first, then formatting."""
import sys
import os
import re
import time

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '.claude', 'skills', 'gdocs'))

from scripts.client import GDocsClient

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
                                print(f"Section 3.1 ends at: {section_3_1_end}")
                                break
                break

    if section_3_1_end is None:
        raise ValueError("Could not find section 3.1 end")

    return tab_id, section_3_1_end


def parse_markdown_to_structure(md_text):
    """Parse markdown into a list of (type, content) tuples."""
    lines = md_text.split('\n')
    structure = []
    i = 0

    while i < len(lines):
        line = lines[i]

        # Skip empty lines
        if not line.strip():
            i += 1
            continue

        # Heading
        heading_match = re.match(r'^(#{1,6})\s+(.+)$', line)
        if heading_match:
            level = len(heading_match.group(1))
            text = heading_match.group(2)
            structure.append(('heading', level, text))
            i += 1
            continue

        # Table
        if line.strip().startswith('|') and i + 1 < len(lines) and re.match(r'^\|[\s\-:|]+\|$', lines[i + 1].strip()):
            table_lines = [line]
            j = i + 1
            while j < len(lines) and lines[j].strip().startswith('|'):
                table_lines.append(lines[j])
                j += 1
            structure.append(('table', table_lines))
            i = j
            continue

        # PlantUML code block
        if line.strip().startswith('```plantuml'):
            code_lines = []
            j = i + 1
            while j < len(lines) and not lines[j].strip().startswith('```'):
                code_lines.append(lines[j])
                j += 1
            structure.append(('plantuml', '\n'.join(code_lines)))
            i = j + 1
            continue

        # Other code block
        if line.strip().startswith('```'):
            code_lines = []
            j = i + 1
            while j < len(lines) and not lines[j].strip().startswith('```'):
                code_lines.append(lines[j])
                j += 1
            structure.append(('code', '\n'.join(code_lines)))
            i = j + 1
            continue

        # Bullet list
        if re.match(r'^[\s]*[-*]\s+', line):
            text = re.sub(r'^[\s]*[-*]\s+', '', line)
            structure.append(('bullet', text))
            i += 1
            continue

        # Numbered list
        if re.match(r'^[\s]*\d+\.\s+', line):
            text = re.sub(r'^[\s]*\d+\.\s+', '', line)
            structure.append(('numbered', text))
            i += 1
            continue

        # Horizontal rule
        if re.match(r'^[\s]*[-*_]{3,}\s*$', line):
            structure.append(('hr', ''))
            i += 1
            continue

        # Regular paragraph
        structure.append(('paragraph', line))
        i += 1

    return structure


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

    # Find insert location
    tab_id, insert_index = find_insert_location(client, DOC_ID, TAB_TITLE)
    print(f"Insert index: {insert_index}")

    # Parse markdown to structure
    structure = parse_markdown_to_structure(content_to_insert)
    print(f"Parsed {len(structure)} elements")

    # PASS 1: Insert all text as plain text
    print("\nPass 1: Inserting plain text...")
    current_index = insert_index
    text_insertions = []

    # Insert the main heading first
    if first_heading:
        clean_heading = clean_inline_formatting(first_heading) + '\n'
        text_insertions.append({
            'type': 'heading',
            'level': 2,  ## is HEADING_2
            'text': clean_heading,
            'original_text': first_heading,
            'start': current_index,
            'end': current_index + len(clean_heading)
        })
        current_index += len(clean_heading)

    # Skip the first element if it's the heading we just inserted
    start_idx = 1 if first_heading and structure and structure[0][0] == 'heading' else 0

    for item in structure[start_idx:]:
        item_type = item[0]
        if item_type == 'heading':
            level = item[1]
            text = item[2]
            clean_text = clean_inline_formatting(text) + '\n'
            text_insertions.append({
                'type': 'heading',
                'level': level,
                'text': clean_text,
                'original_text': text,
                'start': current_index,
                'end': current_index + len(clean_text)
            })
            current_index += len(clean_text)
        elif item_type == 'table':
            table_lines = item[1]
            # Parse table
            rows = []
            for line in table_lines:
                line = line.strip()
                if not line.startswith('|'):
                    continue
                if re.match(r'^\|[\s\-:|]+\|$', line):
                    continue
                cells = [c.strip() for c in line.split('|')[1:-1]]
                rows.append(cells)

            if rows:
                num_rows = len(rows)
                num_cols = max(len(row) for row in rows)

                # Insert table as plain text (one row per line)
                table_text = ''
                for row in rows:
                    while len(row) < num_cols:
                        row.append('')
                    table_text += ' | '.join(row) + '\n'

                text_insertions.append({
                    'type': 'table',
                    'rows': rows,
                    'num_rows': num_rows,
                    'num_cols': num_cols,
                    'text': table_text,
                    'original_text': table_text,
                    'start': current_index,
                    'end': current_index + len(table_text)
                })
                current_index += len(table_text)
        elif item_type == 'plantuml':
            code = item[1]
            text = code + '\n'
            text_insertions.append({
                'type': 'plantuml',
                'text': text,
                'original_text': code,
                'start': current_index,
                'end': current_index + len(text)
            })
            current_index += len(text)
        elif item_type == 'code':
            code = item[1]
            text = code + '\n'
            text_insertions.append({
                'type': 'code',
                'text': text,
                'original_text': code,
                'start': current_index,
                'end': current_index + len(text)
            })
            current_index += len(text)
        elif item_type == 'bullet':
            text = item[1] + '\n'
            text_insertions.append({
                'type': 'bullet',
                'text': text,
                'original_text': item[1],
                'start': current_index,
                'end': current_index + len(text)
            })
            current_index += len(text)
        elif item_type == 'numbered':
            text = item[1] + '\n'
            text_insertions.append({
                'type': 'numbered',
                'text': text,
                'original_text': item[1],
                'start': current_index,
                'end': current_index + len(text)
            })
            current_index += len(text)
        elif item_type == 'hr':
            text = '─' * 50 + '\n'
            text_insertions.append({
                'type': 'hr',
                'text': text,
                'original_text': '',
                'start': current_index,
                'end': current_index + len(text)
            })
            current_index += len(text)
        elif item_type == 'paragraph':
            text = clean_inline_formatting(item[1]) + '\n'
            text_insertions.append({
                'type': 'paragraph',
                'text': text,
                'original_text': item[1],
                'start': current_index,
                'end': current_index + len(text)
            })
            current_index += len(text)

    # Build insert requests (all text first)
    insert_requests = []
    for insertion in text_insertions:
        insert_requests.append({
            'insertText': {
                'location': {'index': insertion['start'], 'tabId': tab_id},
                'text': insertion['text']
            }
        })

    # Execute insert requests in batches
    batch_size = 500
    for i in range(0, len(insert_requests), batch_size):
        batch = insert_requests[i:i + batch_size]
        print(f"  Executing batch {i // batch_size + 1} ({len(batch)} requests)...")
        client.batch_update(DOC_ID, batch)
        time.sleep(0.5)

    print(f"  Inserted {len(text_insertions)} text elements")

    # PASS 2: Apply formatting
    print("\nPass 2: Applying formatting...")
    format_requests = []

    for insertion in text_insertions:
        if insertion['type'] == 'heading':
            # Apply heading style
            level = insertion['level']
            named_style = f'HEADING_{level}'
            format_requests.append({
                'updateParagraphStyle': {
                    'range': {
                        'startIndex': insertion['start'],
                        'endIndex': insertion['end'],
                        'tabId': tab_id
                    },
                    'paragraphStyle': {'namedStyleType': named_style},
                    'fields': 'namedStyleType'
                }
            })
            # Apply inline formatting (bold, italic, etc.)
            apply_inline_formatting(format_requests, insertion['original_text'], insertion['start'], tab_id)
        elif insertion['type'] == 'table':
            # Apply table formatting (convert to actual table)
            # This is complex, so we'll skip it for now and keep as plain text
            pass
        elif insertion['type'] == 'plantuml' or insertion['type'] == 'code':
            # Apply monospace font
            format_requests.append({
                'updateTextStyle': {
                    'range': {
                        'startIndex': insertion['start'],
                        'endIndex': insertion['end'],
                        'tabId': tab_id
                    },
                    'textStyle': {'weightedFontFamily': {'fontFamily': 'Courier New'}},
                    'fields': 'weightedFontFamily'
                }
            })
        elif insertion['type'] == 'bullet':
            # Reset paragraph style
            format_requests.append({
                'updateParagraphStyle': {
                    'range': {
                        'startIndex': insertion['start'],
                        'endIndex': insertion['end'],
                        'tabId': tab_id
                    },
                    'paragraphStyle': {'namedStyleType': 'NORMAL_TEXT'},
                    'fields': 'namedStyleType'
                }
            })
            # Apply bullet formatting
            format_requests.append({
                'createParagraphBullets': {
                    'range': {
                        'startIndex': insertion['start'],
                        'endIndex': insertion['end'],
                        'tabId': tab_id
                    },
                    'bulletPreset': 'BULLET_DISC_CIRCLE_SQUARE'
                }
            })
            # Apply inline formatting
            apply_inline_formatting(format_requests, insertion['original_text'], insertion['start'], tab_id)
        elif insertion['type'] == 'numbered':
            # Reset paragraph style
            format_requests.append({
                'updateParagraphStyle': {
                    'range': {
                        'startIndex': insertion['start'],
                        'endIndex': insertion['end'],
                        'tabId': tab_id
                    },
                    'paragraphStyle': {'namedStyleType': 'NORMAL_TEXT'},
                    'fields': 'namedStyleType'
                }
            })
            # Apply numbered formatting
            format_requests.append({
                'createParagraphBullets': {
                    'range': {
                        'startIndex': insertion['start'],
                        'endIndex': insertion['end'],
                        'tabId': tab_id
                    },
                    'bulletPreset': 'NUMBERED_DECIMAL_ALPHA_ROMAN'
                }
            })
            # Apply inline formatting
            apply_inline_formatting(format_requests, insertion['original_text'], insertion['start'], tab_id)
        elif insertion['type'] == 'paragraph':
            # Reset paragraph style
            format_requests.append({
                'updateParagraphStyle': {
                    'range': {
                        'startIndex': insertion['start'],
                        'endIndex': insertion['end'],
                        'tabId': tab_id
                    },
                    'paragraphStyle': {'namedStyleType': 'NORMAL_TEXT'},
                    'fields': 'namedStyleType'
                }
            })
            # Apply inline formatting
            apply_inline_formatting(format_requests, insertion['original_text'], insertion['start'], tab_id)

    # Execute format requests in batches
    for i in range(0, len(format_requests), batch_size):
        batch = format_requests[i:i + batch_size]
        print(f"  Executing batch {i // batch_size + 1} ({len(batch)} requests)...")
        client.batch_update(DOC_ID, batch)
        time.sleep(0.5)

    print(f"  Applied {len(format_requests)} formatting requests")
    print("\nDone! Section 3.2 has been inserted with fixed formatting.")


def apply_inline_formatting(requests, original_text, base_index, tab_id):
    """Apply bold, italic, etc. formatting to inserted text."""
    # Find bold markers
    for match in re.finditer(r'\*\*(.+?)\*\*', original_text):
        start = base_index + match.start()
        end = base_index + match.start() + len(match.group(1))
        requests.append({
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

    # Find italic markers (single *)
    for match in re.finditer(r'(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)', original_text):
        start = base_index + match.start()
        end = base_index + match.start() + len(match.group(1))
        requests.append({
            'updateTextStyle': {
                'range': {
                    'startIndex': start,
                    'endIndex': end,
                    'tabId': tab_id
                },
                'textStyle': {'italic': True},
                'fields': 'italic'
            }
        })


if __name__ == '__main__':
    main()
