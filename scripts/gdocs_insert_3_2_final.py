"""Insert section 3.2 content into Google Docs.

Two-phase approach:
1. Delete old content, insert clean text
2. Re-read document, classify elements, apply formatting

Only modifies section 3.2 in tab 'Dịch vụ & Sản phẩm'.
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
    print(f"    FAILED: {label}")
    return False


def get_section_range(client, doc_id, tab_title):
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
            if start and element['paragraph'].get('paragraphStyle', {}).get('namedStyleType', '').startswith('HEADING_1') and '3.2' not in text:
                end = element['startIndex']
                break
    return tab_id, start, end


def parse_md(md_content):
    lines = md_content.split('\n')
    content_start = 0
    for i, line in enumerate(lines):
        if line.startswith('## '):
            content_start = i + 1
            break

    blocks = []
    i = content_start
    while i < len(lines):
        line = lines[i]
        if not line.strip():
            i += 1
            continue

        # Heading
        m = re.match(r'^(#{2,4})\s+(.+)$', line)
        if m:
            level = len(m.group(1))
            blocks.append({'type': 'heading', 'level': level, 'text': m.group(2).strip()})
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
        lm = re.match(r'^(\s*)[-*]\s+(.+)$', line)
        if lm:
            indent = len(lm.group(1))
            blocks.append({'type': 'list_item', 'text': lm.group(2).strip(), 'indent': indent})
            i += 1
            continue

        # Paragraph
        blocks.append({'type': 'paragraph', 'text': line.strip()})
        i += 1

    return blocks


def build_text(blocks):
    lines = []
    for b in blocks:
        if b['type'] == 'heading':
            lines.append(b['text'])
        elif b['type'] == 'table_row':
            lines.append(b['text'])
        elif b['type'] == 'list_item':
            prefix = '  ' if b.get('indent', 0) > 0 else ''
            lines.append(prefix + '- ' + b['text'])
        elif b['type'] == 'paragraph':
            lines.append(b['text'])
    return '\n'.join(lines)


def classify(text):
    if not text.strip():
        return 'empty'
    if re.match(r'^[a-d]\) .+', text):
        return 'heading_3'
    if re.match(r'^\d+\. .+', text):
        return 'heading_4'
    if text.startswith('- '):
        return 'bullet'
    if '|' in text and text.count('|') >= 2:
        return 'table_row'
    return 'paragraph'


def get_elements(client, doc_id, tab_title):
    tab = client.find_tab_by_title(doc_id, tab_title)
    tab_id = tab['tabProperties']['tabId']
    content = tab.get('documentTab', {}).get('body', {}).get('content', [])
    elements = []
    found = False
    for element in content:
        if 'paragraph' in element:
            text = ''.join(e.get('textRun', {}).get('content', '') for e in element['paragraph'].get('elements', []))
            if '3.2. Thiết kế mô hình MVC' in text:
                found = True
            if found:
                elements.append({
                    'startIndex': element['startIndex'],
                    'endIndex': element['endIndex'],
                    'text': text.rstrip()
                })
            if found and len(elements) > 1 and ('4. Thiết kế động' in text or element['paragraph'].get('paragraphStyle', {}).get('namedStyleType', '').startswith('HEADING_1')):
                if '3.2' not in text:
                    elements.pop()
                    break
    return elements, tab_id


def main():
    client = GDocsClient()

    # Step 1: Parse markdown
    print("=" * 60)
    print("STEP 1: Parse markdown")
    print("=" * 60)
    with open(MD_FILE, 'r', encoding='utf-8') as f:
        md = f.read()
    blocks = parse_md(md)
    print(f"Parsed {len(blocks)} blocks")

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

    # Re-read
    tab_id, insert_start, _ = get_section_range(client, DOC_ID, TAB_TITLE)
    print(f"Fresh index: {insert_start}")

    # Step 3: Insert clean text
    print("\n" + "=" * 60)
    print("STEP 3: Insert clean text")
    print("=" * 60)
    text = build_text(blocks)
    print(f"Text: {len(text)} chars, {text.count(chr(10))} lines")

    api_call(client, DOC_ID, [{
        'insertText': {
            'location': {'index': insert_start, 'tabId': tab_id},
            'text': text
        }
    }], "insert text")
    time.sleep(RATE_LIMIT_DELAY)

    # Step 4: Re-read and classify
    print("\n" + "=" * 60)
    print("STEP 4: Classify elements")
    print("=" * 60)
    elements, tab_id = get_elements(client, DOC_ID, TAB_TITLE)
    print(f"Found {len(elements)} elements")

    heading_reqs = []
    bullet_reqs = []
    normal_reqs = []
    bold_reqs = []

    for elem in elements:
        etype = classify(elem['text'])
        if etype == 'empty':
            continue

        if etype == 'heading_3':
            heading_reqs.append({
                'updateParagraphStyle': {
                    'range': {'startIndex': elem['startIndex'], 'endIndex': elem['endIndex'], 'tabId': tab_id},
                    'paragraphStyle': {'namedStyleType': 'HEADING_3'},
                    'fields': 'namedStyleType'
                }
            })
        elif etype == 'heading_4':
            heading_reqs.append({
                'updateParagraphStyle': {
                    'range': {'startIndex': elem['startIndex'], 'endIndex': elem['endIndex'], 'tabId': tab_id},
                    'paragraphStyle': {'namedStyleType': 'HEADING_4'},
                    'fields': 'namedStyleType'
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
        elif etype in ('paragraph', 'table_row'):
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

    # Step 5: Apply formatting
    print("\n" + "=" * 60)
    print("STEP 5: Apply formatting")
    print("=" * 60)

    def apply_batch(reqs, label, batch_size=20):
        if not reqs:
            return
        print(f"  {len(reqs)} {label}...")
        for i in range(0, len(reqs), batch_size):
            batch = reqs[i:i + batch_size]
            ok = api_call(client, DOC_ID, batch, f"{label} {i//batch_size+1}")
            if not ok:
                break
            time.sleep(RATE_LIMIT_DELAY)

    apply_batch(heading_reqs, "headings")
    apply_batch(normal_reqs, "normal")
    apply_batch(bullet_reqs, "bullets")

    # Step 6: Verify
    print("\n" + "=" * 60)
    print("STEP 6: Verify")
    print("=" * 60)
    elements, _ = get_elements(client, DOC_ID, TAB_TITLE)
    stats = {'headings': 0, 'bullets': 0, 'normal': 0}
    sample = []
    for elem in elements:
        text = elem['text']
        if not text.strip():
            continue
        etype = classify(text)
        if etype.startswith('heading'):
            stats['headings'] += 1
        elif etype == 'bullet':
            stats['bullets'] += 1
        else:
            stats['normal'] += 1
        if len(sample) < 15:
            sample.append(f"  {etype}: {text[:70]}")

    print(f"Stats: {stats}")
    for s in sample:
        print(s)
    print(f"\nTotal elements: {len(elements)}")
    print("Done!")


if __name__ == '__main__':
    main()
