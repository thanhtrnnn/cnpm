"""Push updated 3.1 (Actor) and 3.2 (UC) tables to XÁC ĐỊNH YÊU CẦU tab.

Strategy: find the two target tables by their header row, then update
each cell in-place using deleteContentRange + insertText requests.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '.claude', 'skills', 'gdocs'))
from scripts.client import GDocsClient

DOC_ID  = '1H0pFNhmbX9yDMObxERGsZ0RqKjpX9Je6N60n4tYrB6s'
TAB     = 'XÁC ĐỊNH YÊU CẦU'

# ── New data ────────────────────────────────────────────────────────────────

ACTOR_ROWS = [
    ['STT', 'Actor', 'Mô tả'],
    ['1', 'Khách hàng',
     'Người sử dụng dịch vụ karaoke, truy cập qua web/app để đặt phòng và quản lý tài khoản cá nhân.'],
    ['2', 'Nhân viên lễ tân',
     'Nhân viên tại quầy, xử lý đặt phòng, check-in/check-out và thanh toán.'],
    ['3', 'Nhân viên phục vụ',
     'Nhân viên nhận order gọi món, phục vụ đồ ăn/uống và báo cáo tình trạng hàng hóa trong phòng.'],
    ['4', 'Quản lý chi nhánh',
     'Quản lý một chi nhánh: nhân sự, kho hàng, menu, phòng hát và xem báo cáo hoạt động.'],
    ['5', 'Chủ doanh nghiệp',
     'Chủ sở hữu toàn chuỗi, quản lý chi nhánh, danh mục, khách hàng, hạng hội viên và xem báo cáo tổng hợp.'],
    ['6', 'Thành viên',
     'Actor trừu tượng, là cha của tất cả actor cụ thể trong hệ thống.'],
    ['7', 'Nhân viên',
     'Actor trừu tượng, là cha của NV lễ tân và NV phục vụ.'],
]

UC_ROWS = [
    ['Actor', 'Use Case'],
    ['Thành viên (tổng quát)', 'UC01 – Đăng nhập'],
    ['', 'UC03 – Đổi mật khẩu'],
    ['Khách hàng', 'UC02 – Đăng ký'],
    ['', 'UC04 – Quản lý thông tin cá nhân'],
    ['', 'UC05 – Đặt phòng'],
    ['', 'UC06 – Gọi món / Quản lý order'],
    ['NV lễ tân', 'UC05 – Đặt phòng'],
    ['', 'UC07 – Quản lý đặt phòng (check-in)'],
    ['', 'UC08 – Quản lý trả phòng (check-out)'],
    ['NV phục vụ', 'UC06 – Gọi món / Quản lý order'],
    ['', 'UC10 – Báo cáo tình trạng hàng hóa'],
    ['Quản lý chi nhánh', 'UC11 – Quản lý nhân viên chi nhánh'],
    ['', 'UC12 – Quản lý kho'],
    ['', 'UC13 – Báo cáo số liệu chi nhánh'],
    ['', 'UC14 – Xem thông tin khách hàng chi nhánh'],
    ['', 'UC15 – Quản lý menu'],
    ['', 'UC19 – Quản lý phòng hát'],
    ['Chủ doanh nghiệp', 'UC16 – Quản lý hệ thống chi nhánh'],
    ['', 'UC17 – Quản lý khách hàng toàn hệ thống'],
    ['', 'UC18 – Quản lý hạng hội viên'],
    ['', 'UC19 – Quản lý phòng hát'],
    ['', 'UC20 – Quản lý tài khoản nhân viên'],
    ['', 'UC21 – Tổng hợp báo cáo toàn chuỗi'],
]

# ── Helpers ──────────────────────────────────────────────────────────────────

def get_tab_id(client, doc_id, tab_title):
    tabs = client.get_all_tabs(doc_id)
    def search(tabs):
        for t in tabs:
            if t['title'].strip().lower() == tab_title.strip().lower():
                return t['tabId']
            found = search(t.get('children', []))
            if found:
                return found
        return None
    return search(tabs)


def find_tables(client, doc_id, tab_title):
    """Return list of table elements (with startIndex) from the tab."""
    tab = client.find_tab_by_title(doc_id, tab_title)
    body = tab.get('documentTab', {}).get('body', {})
    tables = []
    for el in body.get('content', []):
        if 'table' in el:
            tables.append(el)
    return tables


def get_cell_content_range(table_el, row_idx, col_idx):
    """Return (startIndex, endIndex) of the text content inside a cell."""
    row  = table_el['table']['tableRows'][row_idx]
    cell = row['tableCells'][col_idx]
    # Each cell has ≥1 paragraph; we want the span covering all content
    paras = cell.get('content', [])
    if not paras:
        return None
    start = paras[0].get('startIndex', None)
    end   = paras[-1].get('endIndex', None)
    return start, end


def cell_text_index(table_el, row_idx, col_idx):
    """Return the index just inside the cell paragraph (where text starts)."""
    row  = table_el['table']['tableRows'][row_idx]
    cell = row['tableCells'][col_idx]
    paras = cell.get('content', [])
    if not paras:
        return None
    first_para = paras[0]
    return first_para.get('startIndex', None)


def get_cell_existing_text(cell):
    """Extract existing plain text from a cell (excluding trailing newlines)."""
    text = ''
    for para in cell.get('content', []):
        if 'paragraph' not in para:
            continue
        for elem in para['paragraph'].get('elements', []):
            if 'textRun' in elem:
                text += elem['textRun'].get('content', '')
    # Strip trailing newlines added by Docs
    return text.rstrip('\n')


def build_cell_update(tab_id, table_el, row_idx, col_idx, new_text):
    """Build requests to clear a cell and write new_text.
    Uses text-length-based deletion to avoid multi-paragraph index issues.
    """
    requests = []
    row  = table_el['table']['tableRows'][row_idx]
    cell = row['tableCells'][col_idx]
    paras = cell.get('content', [])
    if not paras:
        return requests

    # Find the insert point: start of the first paragraph
    first_start = paras[0].get('startIndex')
    if first_start is None:
        return requests

    # Measure existing text length to delete (textRun content only, no newlines)
    existing = get_cell_existing_text(cell)
    del_len  = len(existing)

    if del_len > 0:
        requests.append({
            'deleteContentRange': {
                'range': {
                    'startIndex': first_start,
                    'endIndex':   first_start + del_len,
                    'tabId':      tab_id,
                }
            }
        })

    if new_text:
        requests.append({
            'insertText': {
                'location': {
                    'index': first_start,
                    'tabId': tab_id,
                },
                'text': new_text,
            }
        })

    return requests


def update_table(client, doc_id, tab_id, table_el, new_rows):
    """Update all cells one-at-a-time (re-reads indices before each cell)."""
    from scripts.client import GDocsClient as _GDC

    actual_rows = len(table_el['table']['tableRows'])
    actual_cols = len(table_el['table']['tableRows'][0]['tableCells'])
    print(f"  Table: {actual_rows}r × {actual_cols}c → new data: {len(new_rows)}r × {len(new_rows[0])}c")

    if actual_rows != len(new_rows):
        print(f"  ⚠ Row count mismatch: doc={actual_rows}, new={len(new_rows)}")
        return False

    total = 0
    # Process in REVERSE order (high index → low) so each update doesn't shift
    # indices of cells not yet processed.
    for r in range(actual_rows - 1, -1, -1):
        for c in range(actual_cols - 1, -1, -1):
            new_text = new_rows[r][c] if c < len(new_rows[r]) else ''

            # Re-read the table to get fresh indices for this specific cell
            fresh_tab   = client.find_tab_by_title(doc_id, TAB)
            fresh_body  = fresh_tab.get('documentTab', {}).get('body', {})
            # Find our table again by position — pick table with same startIndex
            orig_start  = table_el.get('startIndex')
            fresh_table = None
            for el in fresh_body.get('content', []):
                if 'table' in el and el.get('startIndex') == orig_start:
                    fresh_table = el
                    break
            if fresh_table is None:
                # fallback: find by row/col count
                for el in fresh_body.get('content', []):
                    if 'table' in el:
                        tr = el['table'].get('tableRows', [])
                        if len(tr) == actual_rows:
                            tc = tr[0].get('tableCells', [])
                            if len(tc) == actual_cols:
                                fresh_table = el
                                break
            if fresh_table is None:
                print(f"  ✗ Could not re-find table at r={r} c={c}"); return False

            reqs = build_cell_update(tab_id, fresh_table, r, c, new_text)
            if reqs:
                client.batch_update(doc_id, reqs)
                total += len(reqs)

    print(f"  ✓ {total} requests sent ({actual_rows * actual_cols} cells)")
    return True


# ── Main ─────────────────────────────────────────────────────────────────────

def main():
    client = GDocsClient()

    print("Finding tab ID...")
    tab_id = get_tab_id(client, DOC_ID, TAB)
    if not tab_id:
        print("ERROR: tab not found"); sys.exit(1)
    print(f"Tab ID: {tab_id}")

    print("\nReading tables from tab...")
    tables = find_tables(client, DOC_ID, TAB)
    print(f"Found {len(tables)} tables total")

    # Identify tables by header row
    actor_table = None
    uc_table    = None

    for i, tbl in enumerate(tables):
        rows = tbl['table']['tableRows']
        if not rows: continue
        first_row_cells = rows[0]['tableCells']
        first_cell_text = ''
        for el in first_row_cells[0].get('content', []):
            if 'paragraph' in el:
                for run in el['paragraph'].get('elements', []):
                    if 'textRun' in run:
                        first_cell_text += run['textRun'].get('content', '')
        first_cell_text = first_cell_text.strip()

        print(f"  Table {i}: first cell = {first_cell_text!r}, rows={len(rows)}")

        if 'STT' in first_cell_text:
            actor_table = tbl
            print(f"    → Actor table")
        elif first_cell_text.strip() in ('Actor', 'actor'):
            # Check second cell
            if len(first_row_cells) >= 2:
                second_text = ''
                for el in first_row_cells[1].get('content', []):
                    if 'paragraph' in el:
                        for run in el['paragraph'].get('elements', []):
                            if 'textRun' in run:
                                second_text += run['textRun'].get('content', '')
                if 'Use Case' in second_text or 'use case' in second_text.lower():
                    uc_table = tbl
                    print(f"    → UC table")

    if actor_table is None:
        print("ERROR: Actor table (3.1) not found"); sys.exit(1)
    if uc_table is None:
        print("ERROR: UC table (3.2) not found"); sys.exit(1)

    print("\nUpdating 3.1 Actor table...")
    update_table(client, DOC_ID, tab_id, actor_table, ACTOR_ROWS)

    # Re-read tables after 3.1 update — indices have shifted
    print("\nRe-reading tables after 3.1 update...")
    tables = find_tables(client, DOC_ID, TAB)
    uc_table = None
    for tbl in tables:
        rows = tbl['table']['tableRows']
        if not rows: continue
        first_cell_text = ''
        for el in rows[0]['tableCells'][0].get('content', []):
            if 'paragraph' in el:
                for run in el['paragraph'].get('elements', []):
                    if 'textRun' in run:
                        first_cell_text += run['textRun'].get('content', '')
        if first_cell_text.strip().lower() == 'actor' and len(rows[0]['tableCells']) == 2:
            second_text = ''
            for el in rows[0]['tableCells'][1].get('content', []):
                if 'paragraph' in el:
                    for run in el['paragraph'].get('elements', []):
                        if 'textRun' in run:
                            second_text += run['textRun'].get('content', '')
            if 'Use Case' in second_text:
                uc_table = tbl
                print(f"  UC table found: startIndex={tbl.get('startIndex')}, rows={len(rows)}")
                break
    if uc_table is None:
        print("ERROR: UC table not found after re-read"); sys.exit(1)

    print("\nUpdating 3.2 UC table...")

    actual_uc_rows = len(uc_table['table']['tableRows'])
    needed = len(UC_ROWS)
    print(f"  Actual rows in doc: {actual_uc_rows}, new data rows: {needed}")

    # Insert missing rows (append at end — we'll overwrite content anyway)
    if actual_uc_rows < needed:
        diff = needed - actual_uc_rows
        print(f"  Inserting {diff} new row(s)...")
        insert_reqs = []
        # Find the table start index to compute row insertion location
        # We insert after the last existing row (insertBelow=True on last row)
        last_row_idx = actual_uc_rows - 1
        table_start  = uc_table.get('startIndex', None)
        # Use insertTableRow: requires tableStartLocation
        for _ in range(diff):
            insert_reqs.append({
                'insertTableRow': {
                    'tableCellLocation': {
                        'tableStartLocation': {
                            'index':  table_start,
                            'tabId':  tab_id,
                        },
                        'rowIndex':    last_row_idx,
                        'columnIndex': 0,
                    },
                    'insertBelow': True,
                }
            })
            last_row_idx += 1
        client.batch_update(DOC_ID, insert_reqs)
        print(f"  ✓ Rows inserted")

        # Re-read the table so indices are fresh
        print("  Re-reading updated table...")
        tables2 = find_tables(client, DOC_ID, TAB)
        for tbl in tables2:
            rows = tbl['table']['tableRows']
            if not rows: continue
            first_cell_text = ''
            for el in rows[0]['tableCells'][0].get('content', []):
                if 'paragraph' in el:
                    for run in el['paragraph'].get('elements', []):
                        if 'textRun' in run:
                            first_cell_text += run['textRun'].get('content', '')
            if first_cell_text.strip() in ('Actor', 'actor'):
                if len(rows[0]['tableCells']) >= 2:
                    second_text = ''
                    for el in rows[0]['tableCells'][1].get('content', []):
                        if 'paragraph' in el:
                            for run in el['paragraph'].get('elements', []):
                                if 'textRun' in run:
                                    second_text += run['textRun'].get('content', '')
                    if 'Use Case' in second_text:
                        uc_table = tbl
                        print(f"  UC table refreshed: {len(rows)} rows")
                        break

    update_table(client, DOC_ID, tab_id, uc_table, UC_ROWS)

    print("\nDone.")


if __name__ == '__main__':
    main()
