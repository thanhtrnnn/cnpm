"""Clean insert of section 3.2 - handles rate limiting properly.

Strategy:
1. Delete ALL old content in section 3.2
2. Insert all text as one big block (1 API call)
3. Apply formatting in batches with 3s delays
4. Verify after each major step
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

RATE_LIMIT_DELAY = 3  # seconds between API calls


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


def build_full_text(md_content):
    """Build the full insertion text from markdown, preserving structure markers."""
    lines = md_content.split('\n')
    # Skip the main ## heading
    content_start = 0
    for i, line in enumerate(lines):
        if line.startswith('## '):
            content_start = i + 1
            break

    content_lines = lines[content_start:]
    # Remove trailing empty lines
    while content_lines and not content_lines[-1].strip():
        content_lines.pop()

    return '\n'.join(content_lines)


def find_format_ranges(text, base_index):
    """Parse text and find ranges for formatting. Returns list of (type, start, end, extra)."""
    ranges = []
    lines = text.split('\n')
    current = base_index

    for line in lines:
        line_end = current + len(line)

        if line.startswith('### '):
            ranges.append(('heading_3', current, line_end, line))
        elif line.startswith('#### '):
            ranges.append(('heading_4', current, line_end, line))
        elif line.startswith('- ') or line.startswith('  - '):
            ranges.append(('bullet', current, line_end, line))
        elif line.startswith('|') and '|' in line[1:]:
            ranges.append(('table_row', current, line_end, line))
        elif line.strip():
            ranges.append(('normal', current, line_end, line))
            # Find bold spans
            for match in re.finditer(r'\*\*(.+?)\*\*', line):
                bold_start = current + match.start()
                bold_end = bold_start + len(match.group(1))
                ranges.append(('bold', bold_start, bold_end, match.group(1)))
            # Find code spans
            for match in re.finditer(r'`(.+?)`', line):
                code_start = current + match.start()
                code_end = code_start + len(match.group(1))
                ranges.append(('code', code_start, code_end, match.group(1)))

        current = line_end + 1  # +1 for \n

    return ranges


def main():
    client = GDocsClient()

    # Step 1: Read markdown
    print("=" * 60)
    print("STEP 1: Read markdown")
    print("=" * 60)

    with open(MD_FILE, 'r', encoding='utf-8') as f:
        md_content = f.read()

    full_text = build_full_text(md_content)
    print(f"Full text: {len(full_text)} chars, {full_text.count(chr(10))} lines")

    # Step 2: Delete old content
    print("\n" + "=" * 60)
    print("STEP 2: Delete old content")
    print("=" * 60)

    tab_id, insert_start, section_4_start = get_section_range(client, DOC_ID, TAB_TITLE)
    print(f"Range: [{insert_start}, {section_4_start}] ({section_4_start - insert_start} chars)")

    if section_4_start > insert_start:
        api_call(client, DOC_ID, [{
            'deleteContentRange': {
                'range': {
                    'startIndex': insert_start,
                    'endIndex': section_4_start,
                    'tabId': tab_id
                }
            }
        }], "delete old content")
        time.sleep(RATE_LIMIT_DELAY)

    # Re-read for fresh indices
    tab_id, insert_start, _ = get_section_range(client, DOC_ID, TAB_TITLE)
    print(f"Fresh index: {insert_start}")

    # Step 3: Insert all text as one block
    print("\n" + "=" * 60)
    print("STEP 3: Insert all text")
    print("=" * 60)

    api_call(client, DOC_ID, [{
        'insertText': {
            'location': {'index': insert_start, 'tabId': tab_id},
            'text': full_text
        }
    }], "insert all text")
    time.sleep(RATE_LIMIT_DELAY)
    print(f"Inserted {len(full_text)} chars")

    # Step 4: Apply formatting in batches
    print("\n" + "=" * 60)
    print("STEP 4: Apply formatting")
    print("=" * 60)

    ranges = find_format_ranges(full_text, insert_start)
    print(f"Found {len(ranges)} format operations")

    # Batch by type: headings first, then bullets, then inline
    heading_reqs = []
    bullet_reqs = []
    normal_reqs = []
    bold_reqs = []
    code_reqs = []

    for fmt_type, start, end, extra in ranges:
        if fmt_type == 'heading_3':
            heading_reqs.append({
                'updateParagraphStyle': {
                    'range': {'startIndex': start, 'endIndex': end, 'tabId': tab_id},
                    'paragraphStyle': {'namedStyleType': 'HEADING_3'},
                    'fields': 'namedStyleType'
                }
            })
        elif fmt_type == 'heading_4':
            heading_reqs.append({
                'updateParagraphStyle': {
                    'range': {'startIndex': start, 'endIndex': end, 'tabId': tab_id},
                    'paragraphStyle': {'namedStyleType': 'HEADING_4'},
                    'fields': 'namedStyleType'
                }
            })
        elif fmt_type == 'bullet':
            normal_reqs.append({
                'updateParagraphStyle': {
                    'range': {'startIndex': start, 'endIndex': end, 'tabId': tab_id},
                    'paragraphStyle': {'namedStyleType': 'NORMAL_TEXT'},
                    'fields': 'namedStyleType'
                }
            })
            bullet_reqs.append({
                'createParagraphBullets': {
                    'range': {'startIndex': start, 'endIndex': end, 'tabId': tab_id},
                    'bulletPreset': 'BULLET_DISC_CIRCLE_SQUARE'
                }
            })
        elif fmt_type == 'normal':
            normal_reqs.append({
                'updateParagraphStyle': {
                    'range': {'startIndex': start, 'endIndex': end, 'tabId': tab_id},
                    'paragraphStyle': {'namedStyleType': 'NORMAL_TEXT'},
                    'fields': 'namedStyleType'
                }
            })
        elif fmt_type == 'bold':
            bold_reqs.append({
                'updateTextStyle': {
                    'range': {'startIndex': start, 'endIndex': end, 'tabId': tab_id},
                    'textStyle': {'bold': True},
                    'fields': 'bold'
                }
            })
        elif fmt_type == 'code':
            code_reqs.append({
                'updateTextStyle': {
                    'range': {'startIndex': start, 'endIndex': end, 'tabId': tab_id},
                    'textStyle': {'weightedFontFamily': {'fontFamily': 'Courier New'}},
                    'fields': 'weightedFontFamily'
                }
            })

    # Apply in batches of 20 with delays
    def apply_batch(reqs, label, batch_size=20):
        if not reqs:
            return
        print(f"  Applying {len(reqs)} {label}...")
        for i in range(0, len(reqs), batch_size):
            batch = reqs[i:i + batch_size]
            ok = api_call(client, DOC_ID, batch, f"{label} batch {i//batch_size+1}")
            if not ok:
                print(f"    Stopping {label} at batch {i//batch_size+1}")
                break
            time.sleep(RATE_LIMIT_DELAY)
        print(f"  Done: {label}")

    apply_batch(heading_reqs, "headings")
    apply_batch(normal_reqs, "normal styles")
    apply_batch(bullet_reqs, "bullets")
    apply_batch(bold_reqs, "bold")
    apply_batch(code_reqs, "code fonts")

    # Step 5: Verify
    print("\n" + "=" * 60)
    print("STEP 5: Verify")
    print("=" * 60)

    tab = client.find_tab_by_title(DOC_ID, TAB_TITLE)
    content = tab.get('documentTab', {}).get('body', {}).get('content', [])

    found_3_2 = False
    stats = {'headings_3': 0, 'headings_4': 0, 'bullets': 0, 'normal': 0, 'tables': 0}
    for element in content:
        if 'paragraph' in element:
            para = element['paragraph']
            style = para.get('paragraphStyle', {}).get('namedStyleType', 'NORMAL_TEXT')
            text = ''.join(e.get('textRun', {}).get('content', '') for e in para.get('elements', []))

            if '3.2. Thiết kế mô hình MVC' in text:
                found_3_2 = True
            if found_3_2 and '4. Thiết kế động' in text:
                break
            if found_3_2:
                if style == 'HEADING_3':
                    stats['headings_3'] += 1
                elif style == 'HEADING_4':
                    stats['headings_4'] += 1
                elif text.startswith('- '):
                    stats['bullets'] += 1
                elif text.strip():
                    stats['normal'] += 1
        elif 'table' in element and found_3_2:
            stats['tables'] += 1

    print(f"Stats: {stats}")
    print("\nDone!")


if __name__ == '__main__':
    main()
