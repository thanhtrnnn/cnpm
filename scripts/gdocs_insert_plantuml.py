"""Insert PlantUML diagrams as images using public URL.

Uses the PlantUML public server URL directly with insertInlineImage API,
bypassing the Drive upload that fails for service accounts.
"""
import sys
import os
import re
import time
import zlib
import urllib.request

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '.claude', 'skills', 'gdocs'))

from scripts.client import GDocsClient

DOC_ID = '1H0pFNhmbX9yDMObxERGsZ0RqKjpX9Je6N60n4tYrB6s'
TAB_TITLE = 'Dịch vụ & Sản phẩm'
MD_FILE = os.path.join(os.path.dirname(__file__), '..', 'docs', 'tabs', 'section-3.2-mvc.md')

RATE_LIMIT_DELAY = 3


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
    """Encode a number to PlantUML base64."""
    result = ''
    for _ in range(count):
        result += alphabet[number & 0x3F]
        number >>= 6
    return result


def get_plantuml_url(code):
    """Get public PlantUML URL for rendering."""
    encoded = encode_plantuml(code)
    return f'https://www.plantuml.com/plantuml/png/{encoded}'


def extract_plantuml_blocks(md_content):
    """Extract PlantUML blocks from markdown."""
    blocks = []
    lines = md_content.split('\n')
    i = 0
    while i < len(lines):
        if lines[i].strip().startswith('```plantuml'):
            code_lines = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith('```'):
                code_lines.append(lines[i])
                i += 1
            blocks.append('\n'.join(code_lines))
        i += 1
    return blocks


def get_section_elements(client, doc_id, tab_title):
    """Get all elements in section 3.2."""
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
            if found and '4. Thiết kế động' in text:
                break
            if found:
                elements.append({
                    'startIndex': element['startIndex'],
                    'endIndex': element['endIndex'],
                    'text': text.rstrip()
                })
    return elements, tab_id


def main():
    client = GDocsClient()

    # Step 1: Extract PlantUML blocks
    print("=" * 60)
    print("STEP 1: Extract PlantUML blocks")
    print("=" * 60)

    with open(MD_FILE, 'r', encoding='utf-8') as f:
        md_content = f.read()

    plantuml_blocks = extract_plantuml_blocks(md_content)
    print(f"Found {len(plantuml_blocks)} PlantUML blocks")

    for i, block in enumerate(plantuml_blocks):
        url = get_plantuml_url(block)
        print(f"  Block {i+1}: {len(block)} chars -> URL length {len(url)}")

    # Step 2: Find insertion points
    print("\n" + "=" * 60)
    print("STEP 2: Find insertion points")
    print("=" * 60)

    elements, tab_id = get_section_elements(client, DOC_ID, TAB_TITLE)

    # Find "4. Sơ đồ lớp thiết kế" headings
    insertion_points = []
    for elem in elements:
        if 'Sơ đồ lớp thiết kế' in elem['text']:
            # Insert after this heading
            insertion_points.append(elem['endIndex'])
            print(f"  Found at index {elem['endIndex']}: {elem['text'][:50]}")

    print(f"Found {len(insertion_points)} insertion points for {len(plantuml_blocks)} diagrams")

    # Step 3: Insert images (in reverse order to avoid index shifting)
    print("\n" + "=" * 60)
    print("STEP 3: Insert PlantUML images")
    print("=" * 60)

    # Insert in reverse order so indices don't shift
    for i in range(min(len(plantuml_blocks), len(insertion_points)) - 1, -1, -1):
        block = plantuml_blocks[i]
        insert_idx = insertion_points[i]
        url = get_plantuml_url(block)

        print(f"\n  Diagram {i+1}:")
        print(f"    Insert at: {insert_idx}")
        print(f"    URL: {url[:80]}...")

        try:
            # First insert a newline for spacing
            client.batch_update(DOC_ID, [{
                'insertText': {
                    'location': {'index': insert_idx, 'tabId': tab_id},
                    'text': '\n'
                }
            }])
            time.sleep(RATE_LIMIT_DELAY)

            # Insert image via public URL
            client.service.documents().batchUpdate(
                documentId=DOC_ID,
                body={
                    'requests': [{
                        'insertInlineImage': {
                            'location': {'index': insert_idx + 1, 'tabId': tab_id},
                            'uri': url,
                            'objectSize': {
                                'width': {'magnitude': 600, 'unit': 'PT'},
                                'height': {'magnitude': 400, 'unit': 'PT'}
                            }
                        }
                    }]
                }
            ).execute()
            print(f"    OK - image inserted")
            time.sleep(RATE_LIMIT_DELAY)

        except Exception as e:
            print(f"    ERROR: {e}")
            time.sleep(5)

    print("\nDone!")


if __name__ == '__main__':
    main()
