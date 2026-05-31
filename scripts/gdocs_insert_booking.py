"""Insert booking module content into Google Docs TUẤN TEMP tab.

Bottom-to-top batch processing of 7 markdown files.
Based on gdocs_insert_3_2_unified.py, generalized for any tab.
"""
import sys
import os
import re
import time

# Force unbuffered stdout
sys.stdout.reconfigure(line_buffering=True)

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '.claude', 'skills', 'gdocs'))
from scripts.client import GDocsClient

DOC_ID = '1H0pFNhmbX9yDMObxERGsZ0RqKjpX9Je6N60n4tYrB6s'
TAB_TITLE = 'TUẤN TEMP'
TAB_ID = 't.9xhhz2bghmsr'
RATE_LIMIT_DELAY = 3
BATCH_SIZE = 20
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DOCS_DIR = os.path.join(SCRIPT_DIR, '..', 'docs', 'tabs')

# REVERSE order: first in list = inserted first = appears at TOP of tab.
# Files are inserted at END of tab, so first file stays on top.
INSERT_ORDER = [
    'section-booking-ii.1-fix.md',   # Phase II scenarios (top)
    'section-booking-iii.1.md',      # Entity class design
    'section-booking-iii.2.md',      # ERD + CSDL
    'section-booking-iii.3.1.md',    # Wireframes
    'section-booking-iii.3.2.md',    # MVC
    'section-booking-iii.4.md',      # Sequence diagrams
    'section-booking-iv.md',         # Test plan (bottom)
]


def api_call(client, doc_id, requests, label=""):
    for attempt in range(3):
        try:
            client.batch_update(doc_id, requests)
            return True
        except Exception as e:
            if '429' in str(e) or 'Quota' in str(e):
                wait = RATE_LIMIT_DELAY * (attempt + 2)
                print(f"    Rate limited ({label}), waiting {wait}s...")
                time.sleep(wait)
            else:
                print(f"    Error ({label}): {e}")
                if attempt < 2:
                    time.sleep(5)
    print(f"    FAILED: {label}")
    return False


def clean_inline(text):
    """Strip markdown inline formatting markers."""
    text = re.sub(r'\*\*(.+?)\*\*', r'\1', text)
    text = re.sub(r'\*(.+?)\*', r'\1', text)
    text = re.sub(r'`(.+?)`', r'\1', text)
    text = re.sub(r'\[(.+?)\]\(.+?\)', r'\1', text)
    return text


def strip_plantuml_block(md_content):
    """Remove PlantUML code blocks, return (clean_md, plantuml_blocks)."""
    blocks = []
    pattern = r'```plantuml\s*\n(.*?)```'
    for match in re.finditer(pattern, md_content, re.DOTALL):
        blocks.append(match.group(1).strip())
    clean = re.sub(pattern, '', md_content, flags=re.DOTALL)
    return clean, blocks


def strip_code_blocks(md_content):
    """Remove fenced code blocks (```), return clean markdown."""
    pattern = r'```\w*\s*\n(.*?)```'
    clean = re.sub(pattern, '', md_content, flags=re.DOTALL)
    return clean


def parse_tables(md_content):
    """Extract all tables from markdown. Returns list of tables, each a list of rows."""
    md_content, _ = strip_plantuml_block(md_content)
    tables = []
    current_table = []
    in_table = False

    for line in md_content.split('\n'):
        stripped = line.strip()
        if stripped.startswith('|') and '|' in stripped[1:]:
            if re.match(r'^\|[\s\-:|]+\|$', stripped):
                continue
            raw_cells = [c.strip() for c in stripped.split('|')[1:-1]]
            row = []
            for c in raw_cells:
                # Replace <br> with newline for proper line breaks in cells
                c = c.replace('<br>', '\n')
                row.append({'clean': clean_inline(c), 'original': c})
            current_table.append(row)
            in_table = True
        else:
            if in_table and current_table:
                tables.append(current_table)
                current_table = []
                in_table = False

    if current_table:
        tables.append(current_table)
    return tables


def build_text(md_content):
    """Convert markdown to clean text. Returns (text, line_info)."""
    md_content, _ = strip_plantuml_block(md_content)

    lines = md_content.split('\n')
    text_lines = []
    line_info = []

    for line in lines:
        if not line.strip():
            continue

        # Table separator row
        if re.match(r'^\|[\s\-:|]+\|$', line.strip()):
            continue

        # Table row — keep as pipe-separated text
        if line.strip().startswith('|') and '|' in line[1:]:
            cells = [c.strip() for c in line.strip().split('|')[1:-1]]
            clean_cells = [clean_inline(c.replace('<br>', ' ')) for c in cells]
            joined = ' | '.join(clean_cells)
            text_lines.append(joined)
            line_info.append({'type': 'table', 'original': line.strip(), 'clean_text': joined})
            continue

        # Heading
        m = re.match(r'^(#{1,4})\s+(.+)$', line)
        if m:
            level = len(m.group(1))
            clean_text = clean_inline(m.group(2).strip())
            text_lines.append(clean_text)
            line_info.append({'type': f'heading_{level}', 'original': m.group(2).strip(), 'clean_text': clean_text})
            continue

        # Bold paragraph
        bm_para = re.match(r'^\*\*(.+?)\*\*$', line.strip())
        if bm_para:
            clean_text = bm_para.group(1).strip()
            if re.match(r'^[a-d]\) ', clean_text):
                line_info.append({'type': 'heading_3', 'original': clean_text, 'clean_text': clean_text})
            elif re.match(r'^\d+\. ', clean_text):
                line_info.append({'type': 'heading_4', 'original': clean_text, 'clean_text': clean_text})
            else:
                line_info.append({'type': 'bold_paragraph', 'original': clean_text, 'clean_text': clean_text})
            text_lines.append(clean_text)
            continue

        # Bullet
        bm = re.match(r'^(\s*)[-]\s+(.+)$', line)
        if bm:
            indent = len(bm.group(1))
            clean_text = clean_inline(bm.group(2).strip())
            prefix = '  ' * (indent // 2)
            joined = prefix + '- ' + clean_text
            text_lines.append(joined)
            line_info.append({'type': 'bullet', 'original': bm.group(2).strip(), 'clean_text': joined})
            continue

        # Regular paragraph
        clean_text = clean_inline(line.strip())
        text_lines.append(clean_text)
        line_info.append({'type': 'paragraph', 'original': line.strip(), 'clean_text': clean_text})

    return '\n'.join(text_lines) + '\n', line_info


def extract_bold_ranges(text):
    """Find bold ranges in original markdown text."""
    ranges = []
    clean = ''
    i = 0
    while i < len(text):
        if text[i:i+2] == '**':
            j = text.find('**', i + 2)
            if j != -1:
                bold_start = len(clean)
                bold_content = text[i+2:j]
                clean += bold_content
                ranges.append((bold_start, len(clean)))
                i = j + 2
                continue
        clean += text[i]
        i += 1
    return ranges


def extract_inline_code_ranges(text):
    """Find inline code ranges in original markdown text."""
    ranges = []
    clean = ''
    i = 0
    while i < len(text):
        if text[i] == '`':
            j = text.find('`', i + 1)
            if j != -1:
                code_start = len(clean)
                code_content = text[i+1:j]
                clean += code_content
                ranges.append((code_start, len(clean)))
                i = j + 1
                continue
        clean += text[i]
        i += 1
    return ranges


def find_table_regions(elements):
    """Find consecutive paragraph elements that form table regions."""
    regions = []
    current_region = []

    for i, elem in enumerate(elements):
        text = elem['text']
        if ' | ' in text and text.count('|') >= 2:
            current_region.append(i)
        else:
            if len(current_region) >= 1:
                regions.append({
                    'elements': list(current_region),
                    'start_elem_idx': current_region[0],
                    'end_elem_idx': current_region[-1],
                })
            current_region = []

    if len(current_region) >= 1:
        regions.append({
            'elements': list(current_region),
            'start_elem_idx': current_region[0],
            'end_elem_idx': current_region[-1],
        })
    return regions


def get_tab_content(client, doc_id, tab_title):
    """Get tab content and tab_id."""
    tab = client.find_tab_by_title(doc_id, tab_title)
    if not tab:
        raise ValueError(f"Tab not found: {tab_title}")
    tab_id = tab['tabProperties']['tabId']
    content = tab.get('documentTab', {}).get('body', {}).get('content', [])
    return tab_id, content


def get_insert_index(content):
    """Get the last valid insertion index in the tab.

    Google Docs API requires insert index < segment end index.
    The segment always ends with a trailing newline at endIndex.
    So we must insert at endIndex - 1 (before the trailing newline).

    For empty tabs (only default paragraph [1,2] with '\n'), insert at index 1.
    For non-empty tabs, insert at endIndex - 1 of last element.
    """
    elements = [e for e in content if 'paragraph' in e or 'table' in e]

    # Empty tab: 1 paragraph with just '\n'
    if len(elements) == 1 and 'paragraph' in elements[0]:
        text = ''.join(
            e.get('textRun', {}).get('content', '')
            for e in elements[0]['paragraph'].get('elements', [])
        )
        if text.strip() in ('', '\n'):
            return 1

    # Non-empty: insert at endIndex - 1 (before trailing newline)
    last_end = 1
    for elem in elements:
        last_end = elem['endIndex']
    return last_end - 1


def get_elements_all(client, doc_id, tab_title):
    """Get all paragraph elements in the tab."""
    tab = client.find_tab_by_title(doc_id, tab_title)
    tab_id = tab['tabProperties']['tabId']
    content = tab.get('documentTab', {}).get('body', {}).get('content', [])
    elements = []
    for element in content:
        if 'paragraph' in element:
            text = ''.join(e.get('textRun', {}).get('content', '') for e in element['paragraph'].get('elements', []))
            if text.strip():
                elements.append({
                    'startIndex': element['startIndex'],
                    'endIndex': element['endIndex'],
                    'text': text.rstrip()
                })
    return elements, tab_id


def classify(text, line_info, last_matched_idx):
    """Classify a document element based on its content.

    Heading hierarchy (matches "Quản lý đặt & trả phòng" tab):
      H1: Phase headers (PHA XÁC ĐỊNH, II. PHA PHÂN TÍCH, III. PHA THIẾT KẾ, IV. PHA CÀI ĐẶT)
      H2: Section headers (Thiết kế lớp thực thể, Mô hình hóa chức năng, etc.)
      H2: Numbered sections (1.1., 2.1., 3.1., etc.)
      H3: Sub-sections (a) Tạo order, Bước 1, etc.)
      H4: Details (1. Tầng giao diện, Use case đặt phòng, etc.)
    """
    if not text.strip():
        return 'empty', last_matched_idx

    if ' | ' in text and text.count('|') >= 2:
        return 'table_row', last_matched_idx

    clean_elem = text.strip()

    # Match against line_info first
    for i in range(last_matched_idx, len(line_info)):
        info = line_info[i]
        info_clean = info.get('clean_text', '')
        if not info_clean:
            continue
        if clean_elem == info_clean or clean_elem.startswith(info_clean) or info_clean.startswith(clean_elem):
            etype = info['type']
            if etype.startswith('heading'):
                # Remap heading level based on content
                level = _determine_heading_level(clean_elem)
                return f'heading_{level}', i + 1
            if etype == 'bold_paragraph':
                return 'bold_paragraph', i + 1
            if etype == 'bullet':
                return 'bullet', i + 1
            if etype == 'table':
                return 'table_row', i + 1
            return 'paragraph', i + 1

    # Fallback classification
    level = _determine_heading_level(clean_elem)
    if level:
        return f'heading_{level}', last_matched_idx
    if text.startswith('- '):
        return 'bullet', last_matched_idx
    return 'paragraph', last_matched_idx


def _determine_heading_level(text):
    """Determine heading level based on content patterns.

    Returns 1-4 or None (not a heading).
    """
    t = text.strip()

    # H1: Phase headers
    if re.match(r'^[IVX]+\.\s+PHA\s', t) or t.startswith('PHA '):
        return 1
    if t in ('II. PHA PHÂN TÍCH', 'III. PHA THIẾT KẾ', 'IV. PHA CÀI ĐẶT VÀ KIỂM THỬ',
             'PHA XÁC ĐỊNH YÊU CẦU'):
        return 1

    # H2: Section headers with numbers (1.1., 2.1., 3.1., etc.)
    if re.match(r'^\d+\.\d+\.\s', t):
        return 2

    # H2: Major section names
    section_names = [
        'Bảng thuật ngữ', 'Mô hình hóa chức năng', 'Mô hình hóa lớp',
        'Mô hình hóa tĩnh', 'Mô hình hóa động', 'Thiết kế lớp thực thể',
        'Thiết kế CSDL', 'Thiết kế tĩnh', 'Thiết kế giao diện',
        'Thiết kế mô hình MVC', 'Kiểm thử chức năng',
        'Mô hình nghiệp vụ bằng ngôn ngữ tự nhiên',
        'Mô hình nghiệp vụ bằng UML',
    ]
    for name in section_names:
        if t.startswith(name):
            return 2

    # H2: Numbered sections without sub-number (e.g., "1.1. Lập kế hoạch test")
    if re.match(r'^\d+\.\d+\.\s', t):
        return 2

    # H3: Bold paragraph headers like "a) Tạo order", "Bước 1"
    if re.match(r'^[a-e]\)\s', t):
        return 3
    if re.match(r'^Bước\s\d', t):
        return 3

    # H4: Numbered details like "1. Tầng giao diện", "Use case đặt phòng"
    if re.match(r'^\d+\.\s+Tầng\s', t):
        return 4
    if t.startswith('Use case '):
        return 4
    if re.match(r'^\d+\.\s+Tầng', t):
        return 4

    # Not a heading
    return None


def process_file(client, doc_id, md_file, batch_num, total_batches):
    """Process a single markdown file and insert into the tab."""
    filename = os.path.basename(md_file)
    print(f"\n{'='*60}")
    print(f"BATCH {batch_num}/{total_batches}: {filename}")
    print(f"{'='*60}")

    # Step 1: Parse markdown
    with open(md_file, 'r', encoding='utf-8') as f:
        md_content = f.read()

    parsed_tables = parse_tables(md_content)
    clean_text, line_info = build_text(md_content)
    print(f"  Parsed: {len(parsed_tables)} tables, {len(line_info)} lines, {len(clean_text)} chars")

    if not clean_text.strip():
        print(f"  SKIP: empty content")
        return

    # Step 2: Insert text at end of tab
    tab_id, content = get_tab_content(client, doc_id, TAB_TITLE)
    insert_index = get_insert_index(content)
    print(f"  Inserting at index {insert_index}")

    full_text = clean_text

    ok = api_call(client, doc_id, [{
        'insertText': {
            'location': {'index': insert_index, 'tabId': tab_id},
            'text': full_text
        }
    }], f"insert text ({filename})")
    time.sleep(RATE_LIMIT_DELAY)

    if not ok:
        print(f"  FAILED to insert text")
        return

    # Step 3: Classify and apply formatting
    elements, tab_id = get_elements_all(client, doc_id, TAB_TITLE)
    print(f"  Found {len(elements)} elements")

    heading_reqs = []
    bullet_reqs = []
    normal_reqs = []
    bold_paragraph_reqs = []

    last_matched_idx = 0
    for elem in elements:
        text = elem['text']
        if not text.strip():
            continue
        if ' | ' in text and text.count('|') >= 2:
            continue

        etype, last_matched_idx = classify(text, line_info, last_matched_idx)

        if etype.startswith('heading'):
            level = etype.replace('heading_', 'HEADING_')
            if level not in ('HEADING_1', 'HEADING_2', 'HEADING_3', 'HEADING_4', 'HEADING_5', 'HEADING_6'):
                level = 'HEADING_3'
            heading_reqs.append({
                'updateParagraphStyle': {
                    'range': {'startIndex': elem['startIndex'], 'endIndex': elem['endIndex'], 'tabId': tab_id},
                    'paragraphStyle': {'namedStyleType': level},
                    'fields': 'namedStyleType'
                }
            })
        elif etype == 'table_row':
            normal_reqs.append({
                'updateParagraphStyle': {
                    'range': {'startIndex': elem['startIndex'], 'endIndex': elem['endIndex'], 'tabId': tab_id},
                    'paragraphStyle': {'namedStyleType': 'NORMAL_TEXT'},
                    'fields': 'namedStyleType'
                }
            })
        elif etype == 'bold_paragraph':
            normal_reqs.append({
                'updateParagraphStyle': {
                    'range': {'startIndex': elem['startIndex'], 'endIndex': elem['endIndex'], 'tabId': tab_id},
                    'paragraphStyle': {'namedStyleType': 'NORMAL_TEXT'},
                    'fields': 'namedStyleType'
                }
            })
            bold_paragraph_reqs.append({
                'updateTextStyle': {
                    'range': {'startIndex': elem['startIndex'], 'endIndex': elem['endIndex'], 'tabId': tab_id},
                    'textStyle': {'bold': True},
                    'fields': 'bold'
                }
            })
        elif etype == 'bullet':
            normal_reqs.append({
                'updateParagraphStyle': {
                    'range': {'startIndex': elem['startIndex'], 'endIndex': elem['endIndex'], 'tabId': tab_id},
                    'paragraphStyle': {'namedStyleType': 'NORMAL_TEXT'},
                    'fields': 'namedStyleType'
                }
            })
            bullet_reqs.append({
                'createParagraphBullets': {
                    'range': {'startIndex': elem['startIndex'], 'endIndex': elem['endIndex'], 'tabId': tab_id},
                    'bulletPreset': 'BULLET_DISC_CIRCLE_SQUARE'
                }
            })
        else:
            normal_reqs.append({
                'updateParagraphStyle': {
                    'range': {'startIndex': elem['startIndex'], 'endIndex': elem['endIndex'], 'tabId': tab_id},
                    'paragraphStyle': {'namedStyleType': 'NORMAL_TEXT'},
                    'fields': 'namedStyleType'
                }
            })

    def apply_batch(reqs, label):
        if not reqs:
            return
        for i in range(0, len(reqs), BATCH_SIZE):
            batch = reqs[i:i + BATCH_SIZE]
            api_call(client, doc_id, batch, f"{label} {i//BATCH_SIZE+1}")
            time.sleep(RATE_LIMIT_DELAY)

    print(f"  Headings: {len(heading_reqs)}, Normal: {len(normal_reqs)}, Bullets: {len(bullet_reqs)}")
    apply_batch(heading_reqs, "headings")
    apply_batch(normal_reqs, "normal")
    apply_batch(bullet_reqs, "bullets")
    apply_batch(bold_paragraph_reqs, "bold paragraphs")

    # Step 4: Apply bold sub-ranges
    elements_bold, tab_id_bold = get_elements_all(client, doc_id, TAB_TITLE)
    md_clean, _ = strip_plantuml_block(md_content)
    md_lines = md_clean.split('\n')

    bold_reqs = []
    elem_search_start = 0
    for md_line in md_lines:
        if not md_line.strip():
            continue
        if re.match(r'^\|[\s\-:|]+\|$', md_line.strip()):
            continue
        if md_line.strip().startswith('|') and '|' in md_line.strip()[1:]:
            continue

        bold_ranges = extract_bold_ranges(md_line)
        if not bold_ranges:
            continue

        clean_md = clean_inline(md_line.strip())
        matched_elem = None
        for ei in range(elem_search_start, len(elements_bold)):
            e_text = elements_bold[ei]['text'].strip()
            if e_text == clean_md or e_text.startswith(clean_md) or clean_md.startswith(e_text):
                matched_elem = elements_bold[ei]
                elem_search_start = ei + 1
                break

        if not matched_elem:
            continue

        text = matched_elem['text']
        for (b_start, b_end) in bold_ranges:
            bold_text = clean_inline(md_line)[b_start:b_end]
            doc_pos = text.find(bold_text)
            if doc_pos >= 0:
                doc_start = matched_elem['startIndex'] + doc_pos
                doc_end = doc_start + len(bold_text)
                if doc_start >= matched_elem['startIndex'] and doc_end <= matched_elem['endIndex']:
                    bold_reqs.append({
                        'updateTextStyle': {
                            'range': {'startIndex': doc_start, 'endIndex': doc_end, 'tabId': tab_id_bold},
                            'textStyle': {'bold': True},
                            'fields': 'bold'
                        }
                    })

    print(f"  Bold ranges: {len(bold_reqs)}")
    apply_batch(bold_reqs, "bold")

    # Step 5: Apply inline code
    elements_code, tab_id_code = get_elements_all(client, doc_id, TAB_TITLE)
    code_reqs = []
    elem_search_start = 0
    for md_line in md_lines:
        if not md_line.strip():
            continue
        if re.match(r'^\|[\s\-:|]+\|$', md_line.strip()):
            continue
        if md_line.strip().startswith('|') and '|' in md_line.strip()[1:]:
            continue

        code_ranges = extract_inline_code_ranges(md_line)
        if not code_ranges:
            continue

        clean_md = clean_inline(md_line.strip())
        matched_elem = None
        for ei in range(elem_search_start, len(elements_code)):
            e_text = elements_code[ei]['text'].strip()
            if e_text == clean_md or e_text.startswith(clean_md) or clean_md.startswith(e_text):
                matched_elem = elements_code[ei]
                elem_search_start = ei + 1
                break

        if not matched_elem:
            continue

        text = matched_elem['text']
        for (c_start, c_end) in code_ranges:
            code_text = clean_inline(md_line)[c_start:c_end]
            doc_pos = text.find(code_text)
            if doc_pos >= 0:
                doc_start = matched_elem['startIndex'] + doc_pos
                doc_end = doc_start + len(code_text)
                if doc_start >= matched_elem['startIndex'] and doc_end <= matched_elem['endIndex']:
                    code_reqs.append({
                        'updateTextStyle': {
                            'range': {'startIndex': doc_start, 'endIndex': doc_end, 'tabId': tab_id_code},
                            'textStyle': {'weightedFontFamily': {'fontFamily': 'Courier New'}},
                            'fields': 'weightedFontFamily'
                        }
                    })

    print(f"  Inline code ranges: {len(code_reqs)}")
    apply_batch(code_reqs, "inline code")

    # Step 6: Replace tables with native tables
    if not parsed_tables:
        print(f"  No tables to insert")
        return

    elements_tables, tab_id_t = get_elements_all(client, doc_id, TAB_TITLE)
    table_regions = find_table_regions(elements_tables)
    print(f"  Found {len(table_regions)} table regions, {len(parsed_tables)} parsed tables")

    for region_idx in reversed(range(len(table_regions))):
        if region_idx >= len(parsed_tables):
            print(f"  WARNING: No parsed data for region {region_idx}")
            continue

        region = table_regions[region_idx]
        elem_indices = region['elements']
        start_elem = elements_tables[elem_indices[0]]
        end_elem = elements_tables[elem_indices[-1]]
        region_start = start_elem['startIndex']
        region_end = end_elem['endIndex']
        table_data = parsed_tables[region_idx]

        num_rows = len(table_data)
        num_cols = max(len(row) for row in table_data)
        for row in table_data:
            while len(row) < num_cols:
                row.append({'clean': '', 'original': ''})

        print(f"  Table {region_idx}: [{region_start}-{region_end}] {num_rows}x{num_cols}")

        # Delete text region
        api_call(client, doc_id, [{
            'deleteContentRange': {
                'range': {'startIndex': region_start, 'endIndex': region_end, 'tabId': tab_id_t}
            }
        }], f"delete table {region_idx}")
        time.sleep(RATE_LIMIT_DELAY)

        # Insert native table
        ok = api_call(client, doc_id, [{
            'insertTable': {
                'location': {'index': region_start, 'tabId': tab_id_t},
                'rows': num_rows,
                'columns': num_cols
            }
        }], f"insert table {region_idx}")
        time.sleep(RATE_LIMIT_DELAY)

        if not ok:
            continue

        # Re-read to find table element
        tab = client.find_tab_by_title(doc_id, TAB_TITLE)
        tab_id_t = tab['tabProperties']['tabId']
        content = tab.get('documentTab', {}).get('body', {}).get('content', [])

        table_element = None
        for elem in content:
            if 'table' in elem:
                if elem['startIndex'] >= region_start - 5:
                    table_element = elem
                    break

        if not table_element:
            print(f"  WARNING: Could not find table at {region_start}")
            continue

        # Extract cell paragraphs
        cell_paragraphs = []
        for row in table_element['table'].get('tableRows', []):
            for cell in row.get('tableCells', []):
                for para_elem in cell.get('content', []):
                    if 'paragraph' in para_elem:
                        cell_paragraphs.append({
                            'start': para_elem['startIndex'],
                            'end': para_elem['endIndex']
                        })

        # Build cell insert list
        cell_inserts = []
        cell_idx = 0
        for row_idx, row in enumerate(table_data):
            for col_idx, cell_dict in enumerate(row):
                if cell_idx < len(cell_paragraphs) and cell_dict['clean'].strip():
                    cell_inserts.append((row_idx, col_idx, cell_dict['clean'], cell_dict['original'], cell_paragraphs[cell_idx]))
                cell_idx += 1

        # Insert cells in reverse order
        for row_idx, col_idx, clean_text, original_text, cell_para in reversed(cell_inserts):
            try:
                cell_end = cell_para['start'] + len(clean_text)
                cell_range = {'startIndex': cell_para['start'], 'endIndex': cell_end, 'tabId': tab_id_t}

                bold_ranges = extract_bold_ranges(original_text)
                has_markdown_bold = len(bold_ranges) > 0
                is_header = (row_idx == 0)

                # 1. Insert text
                api_call(client, doc_id, [{
                    'insertText': {
                        'location': {'index': cell_para['start'], 'tabId': tab_id_t},
                        'text': clean_text
                    }
                }], f"cell [{row_idx},{col_idx}]")
                time.sleep(1)

                # 2. Reset paragraph style
                api_call(client, doc_id, [{
                    'updateParagraphStyle': {
                        'range': cell_range,
                        'paragraphStyle': {'namedStyleType': 'NORMAL_TEXT'},
                        'fields': 'namedStyleType'
                    }
                }], f"para [{row_idx},{col_idx}]")
                time.sleep(1)

                # 3. Font size 12
                api_call(client, doc_id, [{
                    'updateTextStyle': {
                        'range': cell_range,
                        'textStyle': {'fontSize': {'magnitude': 12, 'unit': 'PT'}},
                        'fields': 'fontSize'
                    }
                }], f"font [{row_idx},{col_idx}]")
                time.sleep(1)

                # 4. Bold
                if is_header:
                    api_call(client, doc_id, [{
                        'updateTextStyle': {
                            'range': cell_range,
                            'textStyle': {'bold': True},
                            'fields': 'bold'
                        }
                    }], f"bold [{row_idx},{col_idx}]")
                    time.sleep(1)
                elif has_markdown_bold:
                    api_call(client, doc_id, [{
                        'updateTextStyle': {
                            'range': cell_range,
                            'textStyle': {'bold': False},
                            'fields': 'bold'
                        }
                    }], f"unbold [{row_idx},{col_idx}]")
                    time.sleep(1)
                    for (b_start, b_end) in bold_ranges:
                        bold_doc_start = cell_para['start'] + b_start
                        bold_doc_end = cell_para['start'] + b_end
                        api_call(client, doc_id, [{
                            'updateTextStyle': {
                                'range': {'startIndex': bold_doc_start, 'endIndex': bold_doc_end, 'tabId': tab_id_t},
                                'textStyle': {'bold': True},
                                'fields': 'bold'
                            }
                        }], f"bold [{row_idx},{col_idx}]")
                        time.sleep(1)
                else:
                    api_call(client, doc_id, [{
                        'updateTextStyle': {
                            'range': cell_range,
                            'textStyle': {'bold': False},
                            'fields': 'bold'
                        }
                    }], f"unbold [{row_idx},{col_idx}]")
                    time.sleep(1)

            except Exception as e:
                print(f"  WARNING: cell [{row_idx},{col_idx}]: {e}")

        print(f"  Populated {min(cell_idx, len(cell_paragraphs))} cells")

    # Step 7: Verify
    elements_v, tab_id_v = get_elements_all(client, doc_id, TAB_TITLE)
    stats = {'HEADING_1': 0, 'HEADING_2': 0, 'HEADING_3': 0, 'HEADING_4': 0, 'NORMAL_TEXT': 0}
    for elem in elements_v:
        # Only count elements that are part of this insertion
        pass
    print(f"  DONE: {filename}")


def main():
    client = GDocsClient()
    total = len(INSERT_ORDER)

    print(f"Inserting {total} files into tab '{TAB_TITLE}' ({TAB_ID})")
    print(f"Document: {DOC_ID}")

    for i, filename in enumerate(INSERT_ORDER):
        md_file = os.path.join(DOCS_DIR, filename)
        if not os.path.exists(md_file):
            print(f"\nSKIP: {filename} not found")
            continue
        process_file(client, DOC_ID, md_file, i + 1, total)

    print(f"\n{'='*60}")
    print(f"ALL DONE: {total} files processed")
    print(f"{'='*60}")


if __name__ == '__main__':
    main()
