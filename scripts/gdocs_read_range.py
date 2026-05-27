"""Read content in a specific index range from Google Docs tab."""
import sys
import os
import json

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '.claude', 'skills', 'gdocs'))

from scripts.client import GDocsClient

DOC_ID = '1H0pFNhmbX9yDMObxERGsZ0RqKjpX9Je6N60n4tYrB6s'
TAB_TITLE = 'Dịch vụ & Sản phẩm'


def read_range(client, doc_id, tab_title, start_index, end_index):
    """Read content in range [start_index, end_index)."""
    tab = client.find_tab_by_title(doc_id, tab_title)
    if not tab:
        raise ValueError(f"Tab '{tab_title}' not found")

    tab_id = tab['tabProperties']['tabId']
    body = tab.get('documentTab', {}).get('body', {})
    content = body.get('content', [])

    print(f"=== Reading range [{start_index}, {end_index}) ===\n")

    for element in content:
        elem_start = element.get('startIndex', 0)
        elem_end = element.get('endIndex', 0)

        # Skip elements outside range
        if elem_end <= start_index or elem_start >= end_index:
            continue

        if 'paragraph' in element:
            para = element['paragraph']
            style = para.get('paragraphStyle', {})
            named = style.get('namedStyleType', 'NORMAL_TEXT')

            # Extract text
            para_text = ''
            for elem in para.get('elements', []):
                if 'textRun' in elem:
                    para_text += elem['textRun'].get('content', '')

            # Show with style info
            if named != 'NORMAL_TEXT':
                print(f"[{elem_start}-{elem_end}] {named}: {para_text.rstrip()}")
            else:
                print(f"[{elem_start}-{elem_end}] {para_text.rstrip()}")

        elif 'table' in element:
            print(f"[{elem_start}-{elem_end}] TABLE")
        elif 'sectionBreak' in element:
            print(f"[{elem_start}-{elem_end}] SECTION_BREAK")
        else:
            print(f"[{elem_start}-{elem_end}] {list(element.keys())}")


def main():
    client = GDocsClient()

    # Read from section 3.2 heading end to section 4 start
    # From Phase 1: section 3.2 ends at 20303, section 4 starts at 20418
    start = 20303
    end = 20418

    read_range(client, DOC_ID, TAB_TITLE, start, end)

    # Also read a bit more to see what's there
    print(f"\n=== Extended range [20277, 20500) ===\n")
    read_range(client, DOC_ID, TAB_TITLE, 20277, 20500)


if __name__ == '__main__':
    main()
