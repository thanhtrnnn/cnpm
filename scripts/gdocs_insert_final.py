"""Final clean insert of section 3.2 - two-phase approach.

Phase 1: Insert clean text (markdown converted to plain text)
Phase 2: Re-read document, find elements, apply formatting

This avoids index calculation errors by using actual document positions.
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

RATE_LIMIT_DELAY = 3


def api_call(client, doc_id, requests, label=""):
    """Make an API call with retry on rate limit."""
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
                time.sleep(5)
    print(f"    FAILED after 3 attempts: {label}")
    return False


def get_section_range(client, doc_id, tab_title):
    """Get section 3.2 boundaries."""
    tab = client.find_tab_by_title(doc_id, tab_title)
    tab_id = tab['tabProperties']['tabId']
    content = tab.get('documentTab', {}).get('body', {}).get('content', [])

    start = None
    end = None
    for element in content:
        if 'paragraph' in element:
            text = ''.join(e.get('textRun', {}).get('content', '') for e in element['paragraph'].get('elements', []))
            if '3.2. Thiết kế mô hình MVC' in text:
                start = element['endIndex']
            if start and '4. Thiết kế động' in text:
                end = element['startIndex']
                break
    return tab_id, start, end


def parse_md_to_blocks(md_content):
    """Parse markdown into structured blocks."""
    lines = md_content.split('\n')

    # Skip main heading
    content_start = 0
    for i, line in enumerate(lines):
        if line.startswith('## '):
            content_start = i + 1
            break

    blocks = []
    i = content_start
    in_plantuml = False

    while i < len(lines):
        line = lines[i]

        if not line.strip():
            i += 1
            continue

        # Skip horizontal rules
        if re.match(r'^[\s]*[-*_]{3,}\s*$', line):
            i += 1
            continue

        # PlantUML code block - skip
        if line.strip().startswith('```plantuml'):
            in_plantuml = True
            i += 1
            continue
        if in_plantuml:
            if line.strip().startswith('```'):
                in_plantuml = False
            i += 1
            continue

        # Regular code block - skip
        if line.strip().startswith('```'):
            i += 1
            while i < len(lines) and not lines[i].strip().startswith('```'):
                i += 1
            i += 1
            continue

        # Heading
        heading_match = re.match(r'^(#{2,4})\s+(.+)$', line)
        if heading_match:
            level = len(heading_match.group(1))
            text = heading_match.group(2).strip()
            blocks.append({'type': 'heading', 'level': level, 'text': text, 'raw': line})
            i += 1
            continue

        # Table row
        if line.strip().startswith('|') and '|' in line[1:]:
            if re.match(r'^\|[\s\-:|]+\|$', line.strip()):
                i += 1
                continue
            cells = [c.strip() for c in line.strip().split('|')[1:-1]]
            blocks.append({'type': 'table_row', 'text': ' | '.join(cells)})
            i += 1
            continue

        # List item
        list_match = re.match(r'^(\s*)[-*]\s+(.+)$', line)
        if list_match:
            indent = len(list_match.group(1))
            blocks.append({'type': 'list_item', 'text': list_match.group(2).strip(), 'indent': indent, 'raw': line})
            i += 1
            continue

        # Paragraph
        if line.strip():
            blocks.append({'type': 'paragraph', 'text': line.strip(), 'raw': line})
        i += 1

    return blocks


def clean_md(text):
    """Remove markdown syntax from text."""
    text = re.sub(r'\*\*(.+?)\*\*', r'\1', text)
    text = re.sub(r'`(.+?)`', r'\1', text)
    return text


def build_insert_text(blocks):
    """Build clean text to insert."""
    lines = []
    for block in blocks:
        if block['type'] == 'heading':
            lines.append(clean_md(block['text']))
        elif block['type'] == 'table_row':
            lines.append(block['text'])
        elif block['type'] == 'list_item':
            prefix = '  ' if block.get('indent', 0) > 0 else ''
            lines.append(prefix + '- ' + clean_md(block['text']))
        elif block['type'] == 'paragraph':
            lines.append(clean_md(block['text']))
    return '\n'.join(lines)


def get_section_elements(client, doc_id, tab_title):
    """Read section 3.2 and return all elements with positions."""
    tab = client.find_tab_by_title(doc_id, tab_title)
    tab_id = tab['tabProperties']['tabId']
    content = tab.get('documentTab', {}).get('body', {}).get('content', [])

    elements = []
    found = False
    for element in content:
        if 'paragraph' in element:
            para = element['paragraph']
            style = para.get('paragraphStyle', {}).get('namedStyleType', 'NORMAL_TEXT')
            text = ''.join(e.get('textRun', {}).get('content', '') for e in para.get('elements', []))

            if '3.2. Thiết kế mô hình MVC' in text:
                found = True
            if found and '4. Thiết kế động' in text:
                break
            if found:
                elements.append({
                    'startIndex': element['startIndex'],
                    'endIndex': element['endIndex'],
                    'style': style,
                    'text': text.rstrip()
                })
    return elements, tab_id


def classify_element(text):
    """Classify what formatting a paragraph needs based on its text content."""
    if not text.strip():
        return 'empty'

    # Check if it's a function heading (a, b, c, d)
    if re.match(r'^[a-d]\) .+', text):
        return 'heading_3'

    # Check if it's a sub-heading like "1. Tầng giao diện..."
    if re.match(r'^\d+\. .+', text):
        return 'heading_4'

    # Check if it's a list item
    if text.startswith('- '):
        return 'bullet'

    # Check if it's a table row (contains |)
    if '|' in text and text.count('|') >= 2:
        return 'table_row'

    return 'paragraph'


def find_md_formats(raw_text):
    """Find bold and code spans in raw markdown text. Returns list of (type, start, end)."""
    formats = []
    for match in re.finditer(r'\*\*(.+?)\*\*', raw_text):
        formats.append(('bold', match.start() + 2, match.start() + 2 + len(match.group(1))))
    for match in re.finditer(r'`(.+?)`', raw_text):
        formats.append(('code', match.start() + 1, match.start() + 1 + len(match.group(1))))
    return formats


def main():
    client = GDocsClient()

    # Step 1: Parse markdown
    print("=" * 60)
    print("STEP 1: Parse markdown")
    print("=" * 60)

    with open(MD_FILE, 'r', encoding='utf-8') as f:
        md_content = f.read()

    blocks = parse_md_to_blocks(md_content)
    print(f"Parsed {len(blocks)} blocks")

    # Step 2: Delete old content
    print("\n" + "=" * 60)
    print("STEP 2: Delete old content")
    print("=" * 60)

    tab_id, insert_start, section_4_start = get_section_range(client, DOC_ID, TAB_TITLE)
    print(f"Range: [{insert_start}, {section_4_start}]")

    api_call(client, DOC_ID, [{
        'deleteContentRange': {
            'range': {'startIndex': insert_start, 'endIndex': section_4_start, 'tabId': tab_id}
        }
    }], "delete old content")
    time.sleep(RATE_LIMIT_DELAY)

    # Re-read
    tab_id, insert_start, _ = get_section_range(client, DOC_ID, TAB_TITLE)
    print(f"Fresh index: {insert_start}")

    # Step 3: Insert clean text
    print("\n" + "=" * 60)
    print("STEP 3: Insert clean text")
    print("=" * 60)

    insert_text = build_insert_text(blocks)
    print(f"Insert text: {len(insert_text)} chars, {insert_text.count(chr(10))} lines")

    api_call(client, DOC_ID, [{
        'insertText': {
            'location': {'index': insert_start, 'tabId': tab_id},
            'text': insert_text
        }
    }], "insert text")
    time.sleep(RATE_LIMIT_DELAY)

    # Step 4: Re-read and classify elements
    print("\n" + "=" * 60)
    print("STEP 4: Re-read and classify elements")
    print("=" * 60)

    elements, tab_id = get_section_elements(client, DOC_ID, TAB_TITLE)
    print(f"Found {len(elements)} elements")

    # Build a mapping from block index to element
    # We match by text content since we know the order
    block_idx = 0
    heading_reqs = []
    bullet_reqs = []
    normal_reqs = []
    bold_reqs = []
    code_reqs = []

    for elem in elements:
        text = elem['text']
        if not text.strip():
            continue

        # Find matching block
        matched_block = None
        for bi in range(block_idx, len(blocks)):
            b = blocks[bi]
            clean = clean_md(b['text']) if b['type'] != 'table_row' else b['text']
            if b['type'] == 'list_item':
                prefix = '  ' if b.get('indent', 0) > 0 else ''
                clean = prefix + '- ' + clean
            if clean == text:
                matched_block = b
                block_idx = bi + 1
                break

        if not matched_block:
            # Try partial match
            for bi in range(block_idx, len(blocks)):
                b = blocks[bi]
                clean = clean_md(b['text']) if b['type'] != 'table_row' else b['text']
                if b['type'] == 'list_item':
                    prefix = '  ' if b.get('indent', 0) > 0 else ''
                    clean = prefix + '- ' + clean
                if text in clean or clean in text:
                    matched_block = b
                    block_idx = bi + 1
                    break

        # Classify and build format requests
        etype = classify_element(text)

        if etype == 'heading_3':
            heading_reqs.append({
                'updateParagraphStyle': {
                    'range': {'startIndex': elem['startIndex'], 'endIndex': elem['endIndex'], 'tabId': tab_id},
                    'paragraphStyle': {'namedStyleType': 'HEADING_3'},
                    'fields': 'namedStyleType'
                }
            })
            print(f"  HEADING_3: {text[:50]}")

        elif etype == 'heading_4':
            heading_reqs.append({
                'updateParagraphStyle': {
                    'range': {'startIndex': elem['startIndex'], 'endIndex': elem['endIndex'], 'tabId': tab_id},
                    'paragraphStyle': {'namedStyleType': 'HEADING_4'},
                    'fields': 'namedStyleType'
                }
            })
            print(f"  HEADING_4: {text[:50]}")

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

        elif etype == 'paragraph':
            normal_reqs.append({
                'updateParagraphStyle': {
                    'range': {'startIndex': elem['startIndex'], 'endIndex': elem['endIndex'], 'tabId': tab_id},
                    'paragraphStyle': {'namedStyleType': 'NORMAL_TEXT'},
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
            code_reqs.append({
                'updateTextStyle': {
                    'range': {'startIndex': elem['startIndex'], 'endIndex': elem['endIndex'], 'tabId': tab_id},
                    'textStyle': {'weightedFontFamily': {'fontFamily': 'Courier New'}},
                    'fields': 'weightedFontFamily'
                }
            })

        # Apply inline formatting from matched block
        if matched_block and matched_block['type'] in ('paragraph', 'list_item', 'heading'):
            raw = matched_block.get('raw', matched_block['text'])
            for fmt_type, fmt_start, fmt_end in find_md_formats(raw):
                # Convert raw positions to clean positions
                # Count removed chars before fmt_start
                removed = 0
                for m in re.finditer(r'\*\*(.+?)\*\*', raw):
                    if m.start() < fmt_start:
                        removed += 4
                for m in re.finditer(r'`(.+?)`', raw):
                    if m.start() < fmt_start:
                        removed += 2

                clean_start = elem['startIndex'] + fmt_start - removed
                clean_end = clean_start + (fmt_end - fmt_start)

                if fmt_type == 'bold':
                    bold_reqs.append({
                        'updateTextStyle': {
                            'range': {'startIndex': clean_start, 'endIndex': clean_end, 'tabId': tab_id},
                            'textStyle': {'bold': True},
                            'fields': 'bold'
                        }
                    })
                elif fmt_type == 'code':
                    code_reqs.append({
                        'updateTextStyle': {
                            'range': {'startIndex': clean_start, 'endIndex': clean_end, 'tabId': tab_id},
                            'textStyle': {'weightedFontFamily': {'fontFamily': 'Courier New'}},
                            'fields': 'weightedFontFamily'
                        }
                    })

    print(f"\nFormat requests:")
    print(f"  Headings: {len(heading_reqs)}")
    print(f"  Normal: {len(normal_reqs)}")
    print(f"  Bullets: {len(bullet_reqs)}")
    print(f"  Bold: {len(bold_reqs)}")
    print(f"  Code: {len(code_reqs)}")

    # Step 5: Apply formatting
    print("\n" + "=" * 60)
    print("STEP 5: Apply formatting")
    print("=" * 60)

    def apply_batch(reqs, label, batch_size=20):
        if not reqs:
            return
        print(f"  Applying {len(reqs)} {label}...")
        for i in range(0, len(reqs), batch_size):
            batch = reqs[i:i + batch_size]
            ok = api_call(client, DOC_ID, batch, f"{label} {i//batch_size+1}")
            if not ok:
                print(f"    Stopping {label}")
                break
            time.sleep(RATE_LIMIT_DELAY)
        print(f"  Done: {label}")

    apply_batch(heading_reqs, "headings")
    apply_batch(normal_reqs, "normal")
    apply_batch(bullet_reqs, "bullets")
    apply_batch(bold_reqs, "bold")
    apply_batch(code_reqs, "code")

    # Step 6: Verify
    print("\n" + "=" * 60)
    print("STEP 6: Verify")
    print("=" * 60)

    elements, _ = get_section_elements(client, DOC_ID, TAB_TITLE)
    stats = {'headings': 0, 'bullets': 0, 'normal': 0}
    sample = []
    for elem in elements:
        style = elem['style']
        text = elem['text']
        if not text.strip():
            continue
        if style.startswith('HEADING'):
            stats['headings'] += 1
        elif text.startswith('- '):
            stats['bullets'] += 1
        else:
            stats['normal'] += 1
        if len(sample) < 20:
            sample.append(f"  {style}: {text[:70]}")

    print(f"Stats: {stats}")
    print("Sample:")
    for s in sample:
        print(s)
    print("\nDone!")


if __name__ == '__main__':
    main()
