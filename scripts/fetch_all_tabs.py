#!/usr/bin/env python3
"""Fetch all 5 tabs from Google Doc and save as markdown to exports/."""
import sys, os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '.claude', 'skills', 'gdocs'))

from scripts.client import GDocsClient

DOC_ID = "1H0pFNhmbX9yDMObxERGsZ0RqKjpX9Je6N60n4tYrB6s"
EXPORTS = os.path.join(os.path.dirname(__file__), '..', 'docs', 'tabs', 'exports')

# (tab_title, module_name) — title must match Google Docs tab title exactly
TABS = [
    ("Tài khoản & Thành viên", "account"),
    ("Quản lý đặt & trả phòng", "booking"),
    ("Dịch vụ & Sản phẩm", "services"),
    ("Quản trị cốt lõi", "core"),
    ("Nhân sự & Báo cáo thống kê", "report"),
]

client = GDocsClient()

for tab_title, module_name in TABS:
    print(f"\n{'='*60}")
    print(f"Fetching: {tab_title}")
    print(f"{'='*60}")

    try:
        md_content, images = client.tab_to_markdown(DOC_ID, tab_title)

        out_dir = os.path.join(EXPORTS, module_name)
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, f"{module_name}.md")

        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(md_content)

        lines = md_content.count('\n') + 1
        print(f"  Saved: {out_path}")
        print(f"  Lines: {lines}")
        print(f"  Images in doc: {len(images)}")

        # Show image info
        for img in images[:3]:
            print(f"    Image: {img.get('objectId', 'N/A')} (type: {img.get('mimeType', 'N/A')})")

    except Exception as e:
        print(f"  ERROR: {e}")
        import traceback
        traceback.print_exc()

print(f"\n{'='*60}")
print("Done.")
