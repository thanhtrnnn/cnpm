"""Phase 1: Map Google Docs tab heading structure with indices."""
import sys
import os
import json

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '.claude', 'skills', 'gdocs'))

from scripts.client import GDocsClient

DOC_ID = '1H0pFNhmbX9yDMObxERGsZ0RqKjpX9Je6N60n4tYrB6s'
TAB_TITLE = 'Dịch vụ & Sản phẩm'


def map_heading_structure(client, doc_id, tab_title):
    """Read tab and dump all headings with indices."""
    tab = client.find_tab_by_title(doc_id, tab_title)
    if not tab:
        raise ValueError(f"Tab '{tab_title}' not found")

    tab_id = tab['tabProperties']['tabId']
    body = tab.get('documentTab', {}).get('body', {})
    content = body.get('content', [])

    headings = []
    current_heading_level = 0

    for element in content:
        if 'paragraph' in element:
            para = element['paragraph']
            style = para.get('paragraphStyle', {})
            named = style.get('namedStyleType', 'NORMAL_TEXT')

            if named.startswith('HEADING'):
                # Extract text
                para_text = ''
                for elem in para.get('elements', []):
                    if 'textRun' in elem:
                        para_text += elem['textRun'].get('content', '')

                para_text = para_text.strip()
                if not para_text:
                    continue

                # Determine level
                level = int(named.replace('HEADING_', ''))
                indent = '  ' * (level - 1)

                heading_info = {
                    'level': level,
                    'namedStyle': named,
                    'startIndex': element['startIndex'],
                    'endIndex': element['endIndex'],
                    'text': para_text
                }
                headings.append(heading_info)

                # Print with indentation
                print(f"{indent}{named} [{element['startIndex']}-{element['endIndex']}] \"{para_text}\"")

    return headings, tab_id


def main():
    client = GDocsClient()

    print(f"=== Mapping heading structure for tab: {TAB_TITLE} ===\n")

    headings, tab_id = map_heading_structure(client, DOC_ID, TAB_TITLE)

    print(f"\n=== Summary ===")
    print(f"Tab ID: {tab_id}")
    print(f"Total headings: {len(headings)}")

    # Find section 3.2 boundaries
    section_3_2 = None
    next_section = None

    for i, h in enumerate(headings):
        if '3.2.' in h['text'] and 'Thiết kế mô hình' in h['text']:
            section_3_2 = h
            # Find next section at same or higher level
            for j in range(i + 1, len(headings)):
                if headings[j]['level'] <= h['level']:
                    next_section = headings[j]
                    break
            break

    if section_3_2:
        print(f"\n=== Section 3.2 Boundaries ===")
        print(f"Start: {section_3_2['startIndex']} (end: {section_3_2['endIndex']})")
        print(f"Text: {section_3_2['text']}")
        if next_section:
            print(f"Next section: {next_section['startIndex']} - \"{next_section['text']}\"")
            print(f"Content range to update: [{section_3_2['endIndex']}, {next_section['startIndex']}]")
        else:
            print("No next section found (end of document)")
    else:
        print("\n=== Section 3.2 NOT FOUND ===")

    # Save to JSON for later use
    output_path = os.path.join(os.path.dirname(__file__), '..', 'docs', 'tabs', 'heading_structure.json')
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump({
            'tab_title': TAB_TITLE,
            'tab_id': tab_id,
            'headings': headings,
            'section_3_2': section_3_2,
            'next_section': next_section
        }, f, ensure_ascii=False, indent=2)
    print(f"\nSaved to: {output_path}")


if __name__ == '__main__':
    main()
