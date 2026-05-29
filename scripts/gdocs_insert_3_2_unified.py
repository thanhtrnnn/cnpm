"""Insert section 3.2 content into Google Docs.

Three-phase approach (proven reliable):
1. Insert clean text (table rows as pipe-separated placeholders)
2. Apply formatting (headings, bold, bullets, inline code)
3. Replace table text with native Google Docs tables (bottom-to-top)
4. Insert PlantUML image via public URL

Bold in table cells: after inserting cell text, strip inherited bold,
then re-apply bold only to ranges that were **bold** in the markdown.
"""
import sys
import os
import re
import time
import zlib

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '.claude', 'skills', 'gdocs'))
from scripts.client import GDocsClient

DOC_ID = '1H0pFNhmbX9yDMObxERGsZ0RqKjpX9Je6N60n4tYrB6s'
TAB_TITLE = 'Dịch vụ & Sản phẩm'
MD_FILE = os.path.join(os.path.dirname(__file__), '..', 'docs', 'tabs', 'section-3.2-mvc.md')
RATE_LIMIT_DELAY = 3
BATCH_SIZE = 20


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


def get_section_range(client, doc_id, tab_title):
    """Find the start/end indices for section 3.2.

    Strategy:
    1. If "3.2. Thiết kế mô hình MVC" heading exists → use its endIndex as start
    2. Otherwise, find the end of section 3.1 (last content before "IV. PHA CÀI")
    3. End is always the start of "IV. PHA CÀI ĐẶT VÀ KIỂM THỬ"
    """
    tab = client.find_tab_by_title(doc_id, tab_title)
    tab_id = tab['tabProperties']['tabId']
    content = tab.get('documentTab', {}).get('body', {}).get('content', [])
    start = None
    end = None
    last_content_before_iv = None

    for element in content:
        if 'paragraph' in element:
            text = ''.join(e.get('textRun', {}).get('content', '') for e in element['paragraph'].get('elements', []))
            # Match section 3.2 heading
            if 'Thiết kế mô hình MVC' in text and ('3.2' in text or 'III.2' in text):
                start = element['endIndex']
            # Track the last content element before section IV
            if text.strip() and 'IV. PHA CÀI' not in text:
                last_content_before_iv = element['endIndex']
            # Find section IV boundary
            if 'IV. PHA CÀI ĐẶT VÀ KIỂM THỬ' in text:
                end = element['startIndex']
                break

    # If no section 3.2 heading found, insert after last content before IV
    if start is None and last_content_before_iv:
        start = last_content_before_iv

    return tab_id, start, end


def encode_plantuml(code):
    """Encode PlantUML text for URL usage."""
    alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-_'
    compressed = zlib.compress(code.encode('utf-8'))[2:-4]
    result = ''
    for i in range(0, len(compressed), 3):
        if i + 2 < len(compressed):
            b1, b2, b3 = compressed[i], compressed[i+1], compressed[i+2]
            result += _encode64((b1 << 16) + (b2 << 8) + b3, 4, alphabet)
        elif i + 1 < len(compressed):
            b1, b2 = compressed[i], compressed[i+1]
            result += _encode64((b1 << 16) + (b2 << 8), 4, alphabet)
        else:
            result += _encode64(compressed[i] << 16, 4, alphabet)
    return result


def _encode64(number, count, alphabet):
    result = ''
    for _ in range(count):
        result += alphabet[number & 0x3F]
        number >>= 6
    return result


def get_plantuml_url(code):
    """Get public PlantUML URL for rendering."""
    encoded = encode_plantuml(code)
    return f'https://www.plantuml.com/plantuml/png/{encoded}'


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


def parse_tables(md_content):
    """Extract all tables from markdown.

    Returns list of tables, each a list of rows (each row is a list of cell dicts).
    Each cell dict has 'clean' (bold markers stripped) and 'original' (raw markdown).
    Separator rows are excluded.
    """
    md_content, _ = strip_plantuml_block(md_content)
    tables = []
    current_table = []
    in_table = False

    for line in md_content.split('\n'):
        stripped = line.strip()
        if stripped.startswith('|') and '|' in stripped[1:]:
            if re.match(r'^\|[\s\-:|]+\|$', stripped):
                continue  # skip separator
            raw_cells = [c.strip() for c in stripped.split('|')[1:-1]]
            row = []
            for c in raw_cells:
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


def find_table_regions(elements):
    """Find consecutive paragraph elements that form table regions.

    Returns list of regions, each with start_idx, end_idx (character offsets),
    and the element indices that belong to the region.
    """
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


def build_text(md_content):
    """Convert markdown to clean text for insertion.

    Returns: (text, line_map) where line_map tracks original bold ranges per line.
    """
    # Remove PlantUML blocks first
    md_content, _ = strip_plantuml_block(md_content)

    lines = md_content.split('\n')
    text_lines = []
    line_info = []  # Track original text for each line (for bold extraction)

    # Skip the first ## heading (we'll add it separately)
    content_start = 0
    for i, line in enumerate(lines):
        if line.startswith('## '):
            content_start = i + 1
            break

    for line in lines[content_start:]:
        if not line.strip():
            continue

        # Table separator row — skip
        if re.match(r'^\|[\s\-:|]+\|$', line.strip()):
            continue

        # Table row — keep as pipe-separated text (will be replaced with native table)
        if line.strip().startswith('|') and '|' in line[1:]:
            cells = [c.strip() for c in line.strip().split('|')[1:-1]]
            clean_cells = [clean_inline(c) for c in cells]
            joined = ' | '.join(clean_cells)
            text_lines.append(joined)
            line_info.append({'type': 'table', 'original': line.strip(), 'clean_text': joined})
            continue

        # Heading (### or ####)
        m = re.match(r'^(#{2,4})\s+(.+)$', line)
        if m:
            level = len(m.group(1))
            clean_text = clean_inline(m.group(2).strip())
            text_lines.append(clean_text)
            line_info.append({'type': f'heading_{level}', 'original': m.group(2).strip(), 'clean_text': clean_text})
            continue

        # Bold paragraph heading (e.g., **1. Tầng giao diện (Boundary)**)
        bm_para = re.match(r'^\*\*(.+?)\*\*$', line.strip())
        if bm_para:
            clean_text = bm_para.group(1).strip()
            # Determine heading level based on content pattern
            if re.match(r'^[a-d]\) ', clean_text):
                line_info.append({'type': 'heading_3', 'original': clean_text, 'clean_text': clean_text})
            elif re.match(r'^\d+\. ', clean_text):
                line_info.append({'type': 'heading_4', 'original': clean_text, 'clean_text': clean_text})
            else:
                line_info.append({'type': 'bold_paragraph', 'original': clean_text, 'clean_text': clean_text})
            text_lines.append(clean_text)
            continue

        # Bullet list
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
    """Find bold ranges in original markdown text.

    Returns list of (clean_start, clean_end) in the CLEAN text.
    """
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
    """Find inline code ranges in original markdown text.

    Returns list of (clean_start, clean_end) in the CLEAN text.
    """
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


def get_elements(client, doc_id, tab_title):
    """Get all paragraph elements in section 3.2.

    Skips empty paragraphs to align with markdown line count.
    """
    tab = client.find_tab_by_title(doc_id, tab_title)
    tab_id = tab['tabProperties']['tabId']
    content = tab.get('documentTab', {}).get('body', {}).get('content', [])
    elements = []
    found = False
    for element in content:
        if 'paragraph' in element:
            text = ''.join(e.get('textRun', {}).get('content', '') for e in element['paragraph'].get('elements', []))
            # Match section 3.2 heading
            if 'Thiết kế mô hình MVC' in text and ('3.2' in text or 'III.2' in text):
                found = True
                continue
            if found:
                # Stop at next major section
                if 'IV. PHA CÀI' in text or '4. Thiết kế động' in text:
                    break
                # Stop at HEADING_1 that looks like a major section (Roman numeral pattern)
                style = element['paragraph'].get('paragraphStyle', {}).get('namedStyleType', '')
                if style == 'HEADING_1' and re.match(r'^[IVX]+\.\s', text.strip()):
                    break
                # Skip empty paragraphs to align with markdown line count
                if not text.strip():
                    continue
                elements.append({
                    'startIndex': element['startIndex'],
                    'endIndex': element['endIndex'],
                    'text': text.rstrip()
                })
    return elements, tab_id


def classify(text, line_info, last_matched_idx):
    """Classify a document element based on its content.

    Uses text-based matching: search line_info from last_matched_idx forward
    to find the entry whose cleaned text matches the document element.
    Returns (etype, matched_info_idx).
    """
    if not text.strip():
        return 'empty', last_matched_idx

    # Check if it matches a table row (contains | separators)
    if ' | ' in text and text.count('|') >= 2:
        return 'table_row', last_matched_idx

    # Text-based matching: find the line_info entry whose clean text
    # is a prefix or substring of the element text
    clean_elem = text.strip()
    for i in range(last_matched_idx, len(line_info)):
        info = line_info[i]
        info_clean = info.get('clean_text', '')
        if not info_clean:
            continue
        # Match: element text starts with or equals the clean text from line_info
        if clean_elem == info_clean or clean_elem.startswith(info_clean) or info_clean.startswith(clean_elem):
            etype = info['type']
            if etype.startswith('heading'):
                return etype, i + 1
            if etype == 'bold_paragraph':
                return 'bold_paragraph', i + 1
            if etype == 'bullet':
                return 'bullet', i + 1
            if etype == 'table':
                return 'table_row', i + 1
            return 'paragraph', i + 1

    # Fallback classification if no match found
    if re.match(r'^[a-d]\) .+', text):
        return 'heading_3', last_matched_idx
    if re.match(r'^\d+\. .+', text):
        return 'heading_4', last_matched_idx
    if text.startswith('- '):
        return 'bullet', last_matched_idx

    return 'paragraph', last_matched_idx


def main():
    client = GDocsClient()

    # Step 1: Parse markdown
    print("=" * 60)
    print("STEP 1: Parse markdown")
    print("=" * 60)
    with open(MD_FILE, 'r', encoding='utf-8') as f:
        md_content = f.read()

    # Parse tables separately
    parsed_tables = parse_tables(md_content)
    print(f"Parsed {len(parsed_tables)} tables")

    # Build clean text (table rows are skipped)
    clean_text, line_info = build_text(md_content)
    print(f"Clean text: {len(clean_text)} chars, {clean_text.count(chr(10))} lines")
    print(f"Line info: {len(line_info)} entries")

    # Show breakdown
    type_counts = {}
    for info in line_info:
        t = info['type']
        type_counts[t] = type_counts.get(t, 0) + 1
    print(f"Types: {type_counts}")

    # Step 2: Delete old content
    print("\n" + "=" * 60)
    print("STEP 2: Delete old content")
    print("=" * 60)
    tab_id, insert_start, section_end = get_section_range(client, DOC_ID, TAB_TITLE)
    print(f"Range: [{insert_start}, {section_end}]")

    if section_end and section_end > insert_start:
        api_call(client, DOC_ID, [{
            'deleteContentRange': {
                'range': {'startIndex': insert_start, 'endIndex': section_end, 'tabId': tab_id}
            }
        }], "delete old content")
        time.sleep(RATE_LIMIT_DELAY)

    # Re-read for fresh indices
    tab_id, insert_start, _ = get_section_range(client, DOC_ID, TAB_TITLE)
    print(f"Fresh index: {insert_start}")

    # Step 3: Insert non-table text
    print("\n" + "=" * 60)
    print("STEP 3: Insert non-table text")
    print("=" * 60)

    # Check if "3.2." heading already exists
    tab_check = client.find_tab_by_title(DOC_ID, TAB_TITLE)
    content_check = tab_check.get('documentTab', {}).get('body', {}).get('content', [])
    has_heading = False
    for elem in content_check:
        if 'paragraph' in elem:
            text = ''.join(e.get('textRun', {}).get('content', '') for e in elem['paragraph'].get('elements', []))
            if '3.2. Thiết kế mô hình MVC' in text:
                has_heading = True
                break

    if has_heading:
        full_text = clean_text
        print("  Heading already exists, inserting content only")
    else:
        full_text = '3.2. Thiết kế mô hình MVC\n' + clean_text
        print("  Inserting heading + content")

    # Insert a newline first to avoid first-char loss at paragraph boundary
    api_call(client, DOC_ID, [{
        'insertText': {
            'location': {'index': insert_start, 'tabId': tab_id},
            'text': '\n'
        }
    }], "insert newline buffer")
    time.sleep(RATE_LIMIT_DELAY)

    # Re-read for fresh index after buffer insertion
    tab_id, insert_start, _ = get_section_range(client, DOC_ID, TAB_TITLE)

    api_call(client, DOC_ID, [{
        'insertText': {
            'location': {'index': insert_start, 'tabId': tab_id},
            'text': full_text
        }
    }], "insert text")
    time.sleep(RATE_LIMIT_DELAY)

    # Step 4: Re-read and classify elements (skip table rows — they'll be native tables)
    print("\n" + "=" * 60)
    print("STEP 4: Classify elements")
    print("=" * 60)
    elements, tab_id = get_elements(client, DOC_ID, TAB_TITLE)
    print(f"Found {len(elements)} elements")

    # Build classification requests
    heading_reqs = []
    bullet_reqs = []
    normal_reqs = []
    bold_paragraph_reqs = []

    # Skip the first element (section heading 3.2.) — set to HEADING_3
    if elements:
        heading_reqs.append({
            'updateParagraphStyle': {
                'range': {'startIndex': elements[0]['startIndex'], 'endIndex': elements[0]['endIndex'], 'tabId': tab_id},
                'paragraphStyle': {'namedStyleType': 'HEADING_3'},
                'fields': 'namedStyleType'
            }
        })

    last_matched_idx = 0

    for idx, elem in enumerate(elements):
        if idx == 0:
            continue

        text = elem['text']
        if not text.strip():
            continue

        # Skip table rows — will be replaced with native tables
        if ' | ' in text and text.count('|') >= 2:
            continue

        etype, last_matched_idx = classify(text, line_info, last_matched_idx)

        if etype.startswith('heading'):
            style = etype.replace('heading_', 'HEADING_')
            if style not in ('HEADING_2', 'HEADING_3', 'HEADING_4', 'HEADING_5', 'HEADING_6'):
                style = 'HEADING_3'
            heading_reqs.append({
                'updateParagraphStyle': {
                    'range': {'startIndex': elem['startIndex'], 'endIndex': elem['endIndex'], 'tabId': tab_id},
                    'paragraphStyle': {'namedStyleType': style},
                    'fields': 'namedStyleType'
                }
            })
        elif etype == 'table_row':
            # Table rows get NORMAL_TEXT (will be replaced with native table)
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

    print(f"  Headings: {len(heading_reqs)}")
    print(f"  Normal: {len(normal_reqs)}")
    print(f"  Bullets: {len(bullet_reqs)}")
    print(f"  Bold paragraphs: {len(bold_paragraph_reqs)}")

    # Step 5: Apply formatting
    print("\n" + "=" * 60)
    print("STEP 5: Apply formatting")
    print("=" * 60)

    def apply_batch(reqs, label):
        if not reqs:
            return
        print(f"  {len(reqs)} {label}...")
        for i in range(0, len(reqs), BATCH_SIZE):
            batch = reqs[i:i + BATCH_SIZE]
            ok = api_call(client, DOC_ID, batch, f"{label} {i//BATCH_SIZE+1}")
            if not ok:
                break
            time.sleep(RATE_LIMIT_DELAY)

    apply_batch(heading_reqs, "headings")
    apply_batch(normal_reqs, "normal")
    apply_batch(bullet_reqs, "bullets")
    apply_batch(bold_paragraph_reqs, "bold paragraphs")

    # Step 6: Apply bold formatting (on non-table content)
    print("\n" + "=" * 60)
    print("STEP 6: Apply bold formatting")
    print("=" * 60)

    elements_bold, tab_id_bold = get_elements(client, DOC_ID, TAB_TITLE)

    md_bold, _ = strip_plantuml_block(md_content)
    md_lines = md_bold.split('\n')

    md_content_start = 0
    for i, line in enumerate(md_lines):
        if line.startswith('## '):
            md_content_start = i + 1
            break

    bold_reqs = []
    elem_search_start = 0

    for md_line in md_lines[md_content_start:]:
        if not md_line.strip():
            continue
        if re.match(r'^\|[\s\-:|]+\|$', md_line.strip()):
            continue
        if md_line.strip().startswith('```'):
            continue
        # Skip table rows
        if md_line.strip().startswith('|') and '|' in md_line.strip()[1:]:
            continue

        bold_ranges = extract_bold_ranges(md_line)
        if not bold_ranges:
            continue

        clean_md_check = clean_inline(md_line.strip())
        if re.match(r'^#{2,4}\s', md_line) or re.match(r'^[a-d]\)\s', clean_md_check) or re.match(r'^\d+\.\s', clean_md_check):
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

    # Step 7: Apply inline code formatting
    print("\n" + "=" * 60)
    print("STEP 7: Apply inline code formatting")
    print("=" * 60)

    elements_code, tab_id_code = get_elements(client, DOC_ID, TAB_TITLE)

    code_reqs = []
    elem_search_start = 0

    for md_line in md_lines[md_content_start:]:
        if not md_line.strip():
            continue
        if re.match(r'^\|[\s\-:|]+\|$', md_line.strip()):
            continue
        if md_line.strip().startswith('```'):
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
                            'textStyle': {
                                'weightedFontFamily': {'fontFamily': 'Courier New'}
                            },
                            'fields': 'weightedFontFamily'
                        }
                    })

    print(f"  Inline code ranges: {len(code_reqs)}")
    apply_batch(code_reqs, "inline code")

    # Step 8: Replace table text regions with native Google Docs tables
    print("\n" + "=" * 60)
    print("STEP 8: Replace tables with native tables")
    print("=" * 60)

    elements_tables, tab_id_t = get_elements(client, DOC_ID, TAB_TITLE)
    table_regions = find_table_regions(elements_tables)
    print(f"Found {len(table_regions)} table regions")

    # Process tables from bottom to top (avoids index shifting)
    for region_idx in reversed(range(len(table_regions))):
        region = table_regions[region_idx]
        elem_indices = region['elements']

        # Get the text range for this region
        start_elem = elements_tables[elem_indices[0]]
        end_elem = elements_tables[elem_indices[-1]]
        region_start = start_elem['startIndex']
        region_end = end_elem['endIndex']

        # Match this region to parsed table data
        if region_idx < len(parsed_tables):
            table_data = parsed_tables[region_idx]
        else:
            print(f"  WARNING: No parsed data for region {region_idx}, skipping")
            continue

        num_rows = len(table_data)
        num_cols = max(len(row) for row in table_data)

        # Pad rows
        for row in table_data:
            while len(row) < num_cols:
                row.append('')

        print(f"  Region {region_idx}: [{region_start}-{region_end}] {num_rows}x{num_cols}")

        # Delete the text region
        api_call(client, DOC_ID, [{
            'deleteContentRange': {
                'range': {'startIndex': region_start, 'endIndex': region_end, 'tabId': tab_id_t}
            }
        }], f"delete table {region_idx} text")
        time.sleep(RATE_LIMIT_DELAY)

        # Insert native table
        ok = api_call(client, DOC_ID, [{
            'insertTable': {
                'location': {'index': region_start, 'tabId': tab_id_t},
                'rows': num_rows,
                'columns': num_cols
            }
        }], f"insert table {region_idx}")
        time.sleep(RATE_LIMIT_DELAY)

        if not ok:
            print(f"  FAILED to insert table {region_idx}")
            continue

        # Re-read to find the table element and populate cells
        tab = client.find_tab_by_title(DOC_ID, TAB_TITLE)
        tab_id_t = tab['tabProperties']['tabId']
        content = tab.get('documentTab', {}).get('body', {}).get('content', [])

        # Find the table element near the insertion point
        table_element = None
        for elem in content:
            if 'table' in elem:
                if elem['startIndex'] >= region_start - 5:
                    table_element = elem
                    break

        if not table_element:
            print(f"  WARNING: Could not find table at index {region_start}")
            continue

        # Extract cell paragraphs from nested table structure
        cell_paragraphs = []
        table_rows = table_element['table'].get('tableRows', [])
        for row in table_rows:
            for cell in row.get('tableCells', []):
                for para_elem in cell.get('content', []):
                    if 'paragraph' in para_elem:
                        cell_paragraphs.append({
                            'start': para_elem['startIndex'],
                            'end': para_elem['endIndex']
                        })

        # Populate cells in REVERSE order to avoid index shifting
        # Build list of (row, col, clean_text, original_text, cell_para) tuples
        cell_inserts = []
        cell_idx = 0
        for row_idx, row in enumerate(table_data):
            for col_idx, cell_dict in enumerate(row):
                if cell_idx < len(cell_paragraphs) and cell_dict['clean'].strip():
                    cell_inserts.append((row_idx, col_idx, cell_dict['clean'], cell_dict['original'], cell_paragraphs[cell_idx]))
                cell_idx += 1

        # Insert in reverse order (last cell first)
        for row_idx, col_idx, clean_text, original_text, cell_para in reversed(cell_inserts):
            try:
                # Insert clean text
                api_call(client, DOC_ID, [{
                    'insertText': {
                        'location': {'index': cell_para['start'], 'tabId': tab_id_t},
                        'text': clean_text
                    }
                }], f"cell [{row_idx},{col_idx}]")
                time.sleep(1)

                # Strip inherited bold formatting from entire cell
                cell_end = cell_para['start'] + len(clean_text)
                api_call(client, DOC_ID, [{
                    'updateTextStyle': {
                        'range': {'startIndex': cell_para['start'], 'endIndex': cell_end, 'tabId': tab_id_t},
                        'textStyle': {'bold': False},
                        'fields': 'bold'
                    }
                }], f"unbold cell [{row_idx},{col_idx}]")
                time.sleep(1)

                # Re-apply bold only for ranges that should be bold
                bold_ranges = extract_bold_ranges(original_text)
                for (b_start, b_end) in bold_ranges:
                    bold_doc_start = cell_para['start'] + b_start
                    bold_doc_end = cell_para['start'] + b_end
                    api_call(client, DOC_ID, [{
                        'updateTextStyle': {
                            'range': {'startIndex': bold_doc_start, 'endIndex': bold_doc_end, 'tabId': tab_id_t},
                            'textStyle': {'bold': True},
                            'fields': 'bold'
                        }
                    }], f"bold cell [{row_idx},{col_idx}] range [{b_start}:{b_end}]")
                    time.sleep(1)

            except Exception as e:
                print(f"  WARNING: Failed to insert cell [{row_idx},{col_idx}]: {e}")

        print(f"  Populated {min(cell_idx, len(cell_paragraphs))} cells")

    # Step 9: Try PlantUML image insertion
    print("\n" + "=" * 60)
    print("STEP 9: PlantUML image")
    print("=" * 60)

    # Find where the PlantUML block should go (after "4. Sơ đồ lớp thiết kế" heading)
    _, plantuml_blocks = strip_plantuml_block(md_content)
    if plantuml_blocks:
        plantuml_code = plantuml_blocks[0]
        plantuml_url = get_plantuml_url(plantuml_code)
        print(f"  PlantUML URL: {plantuml_url[:80]}...")

        # Find the "4. Sơ đồ lớp thiết kế" heading in the document
        tab = client.find_tab_by_title(DOC_ID, TAB_TITLE)
        tab_id_p = tab['tabProperties']['tabId']
        content = tab.get('documentTab', {}).get('body', {}).get('content', [])

        found_heading = False
        insert_index = None
        for elem in content:
            if 'paragraph' in elem:
                text = ''.join(e.get('textRun', {}).get('content', '') for e in elem['paragraph'].get('elements', []))
                if 'Thiết kế mô hình MVC' in text and ('3.2' in text or 'III.2' in text):
                    found_heading = True
                    continue
                if found_heading:
                    if 'Sơ đồ lớp thiết kế' in text:
                        insert_index = elem['endIndex']
                        break
                    if 'IV. PHA CÀI' in text:
                        break

        if insert_index:
            print(f"  Inserting image at index {insert_index}")
            try:
                result = client.insert_image_by_url(
                    DOC_ID, tab_id_p, insert_index,
                    plantuml_url, width=600, height=400
                )
                # Check if image was actually inserted
                inline_objects = result.get('replies', [{}])[0].get('insertInlineImage', {})
                if inline_objects:
                    print("  Image inserted successfully!")
                else:
                    print("  WARNING: Image insertion returned no inline objects")
                    print(f"  Rendered PNG available at: output/diagrams/sodo_lop_thiet_ke.png")
            except Exception as e:
                print(f"  WARNING: Image insertion failed: {e}")
                print(f"  Rendered PNG available at: output/diagrams/sodo_lop_thiet_ke.png")
        else:
            print("  Could not find insertion point for image")
    else:
        print("  No PlantUML blocks found in markdown")

    # Step 10: Verify
    print("\n" + "=" * 60)
    print("STEP 10: Verify")
    print("=" * 60)

    tab = client.find_tab_by_title(DOC_ID, TAB_TITLE)
    tab_id_v = tab['tabProperties']['tabId']
    content = tab.get('documentTab', {}).get('body', {}).get('content', [])

    found = False
    stats = {'HEADING_1': 0, 'HEADING_3': 0, 'HEADING_4': 0, 'NORMAL_TEXT': 0, 'TABLE': 0}
    bold_count = 0
    code_count = 0
    total = 0
    for elem in content:
        if 'table' in elem:
            if found:
                stats['TABLE'] += 1
            continue
        if 'paragraph' in elem:
            text = ''.join(e.get('textRun', {}).get('content', '') for e in elem['paragraph'].get('elements', []))
            style = elem['paragraph'].get('paragraphStyle', {}).get('namedStyleType', 'NORMAL_TEXT')
            if 'Thiết kế mô hình MVC' in text and ('3.2' in text or 'III.2' in text):
                found = True
                stats[style] = stats.get(style, 0) + 1
                continue
            if found:
                if 'IV. PHA CÀI' in text:
                    break
                if text.strip():
                    total += 1
                    stats[style] = stats.get(style, 0) + 1
                    for el in elem['paragraph'].get('elements', []):
                        tr = el.get('textRun', {})
                        s = tr.get('textStyle', {})
                        if s.get('bold'):
                            bold_count += 1
                        if s.get('weightedFontFamily', {}).get('fontFamily') == 'Courier New':
                            code_count += 1

    print(f"Total elements: {total}")
    print(f"Styles: {stats}")
    print(f"Bold ranges: {bold_count}")
    print(f"Code ranges: {code_count}")
    print("Done!")


if __name__ == '__main__':
    main()
