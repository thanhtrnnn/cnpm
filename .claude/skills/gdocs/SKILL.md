---
name: gdocs
description: >
  Đọc và ghi nội dung lên Google Docs qua Google Docs API. Kích hoạt khi người dùng
  muốn: đọc nội dung từ Google Docs, cập nhật tài liệu Google Docs, đẩy nội dung
  markdown lên Google Docs, đồng bộ tài liệu UP với Google Docs, hoặc bất kỳ yêu cầu
  nào liên quan đến Google Docs API.
---

# Google Docs Integration Skill

Giao tiếp với Google Docs qua API để đọc/ghi/xoá nội dung tài liệu. Hỗ trợ workflow CNPM: sinh nội dung bằng skill `cnpm` → đẩy lên Google Docs.

---

## Yêu cầu

- Python 3.9+
- `credentials.json` từ Google Cloud Console (user tự cung cấp)
- Dependencies: `pip install -r .claude/skills/gdocs/scripts/requirements.txt`

---

## Setup

### Bước 1 — Cài dependencies

```bash
pip install -r .claude/skills/gdocs/scripts/requirements.txt
```

### Bước 2 — Xác thực

User đặt `credentials.json` vào root project, sau đó chạy:

```bash
cd .claude/skills/gdocs
python scripts/cli.py auth --verify
```

Lần đầu sẽ mở browser để OAuth2 consent. Token lưu vào `token.json` (auto-refresh).

---

## CLI Reference

### Auth

```bash
python scripts/cli.py auth                          # Authenticate (opens browser)
python scripts/cli.py auth --credentials creds.json # Setup credentials
python scripts/cli.py auth --verify                 # Verify token is valid
```

### Read

```bash
python scripts/cli.py read <document_id>              # Read as plain text
python scripts/cli.py read <document_id> --format json # Read full structure
```

### Write

```bash
python scripts/cli.py write <document_id> --file output.md           # Append markdown
python scripts/cli.py write <document_id> --section "II.3" --file section.md  # Update section
```

### List Sections

```bash
python scripts/cli.py sections <document_id>  # List all headings
```

### Render PlantUML

```bash
python scripts/cli.py render "@startuml\nA -> B\n@enduml"  # Render to PNG
python scripts/cli.py render --file diagram.puml --output out.png
```

---

## Workflow Integration với skill `cnpm`

```
1. User: "Viết tài liệu UP cho module X"
2. cnpm skill sinh markdown content (text + PlantUML)
3. converter.py parse markdown → Google Docs API requests
4. plantuml_renderer.py render diagrams → PNG
5. client.py batchUpdate lên Google Docs
6. User review trên Google Docs
```

### Quy trình chi tiết

Khi user yêu cầu viết tài liệu lên Google Docs:

1. **Invoke skill `cnpm`** để sinh nội dung markdown theo chuẩn UP
2. **Lưu markdown** vào file `.md` trong `output/` (nếu user muốn)
3. **Chạy converter** để chuyển markdown → Google Docs requests
4. **Render PlantUML** thành PNG (dùng PlantUML server)
5. **Push lên Google Docs** qua `client.py`
6. **Thông báo link** để user review

### Lấy document ID từ link

User cung cấp link Google Docs dạng:
```
https://docs.google.com/document/d/<DOCUMENT_ID>/edit
```

Trích xuất `<DOCUMENT_ID>` từ URL.

---

## Markdown Insertion Strategy (đã verify)

### 3-Phase Approach

1. **Phase 1 — Insert text:** Parse markdown → insert clean text (table rows as pipe-separated placeholders)
2. **Phase 2 — Apply formatting:** Re-read → classify paragraphs → apply heading, bold, bullets, inline code
3. **Phase 3 — Replace tables:** Re-read → find table regions → delete text → `insertTable` → populate cells (bottom-to-top)
4. **Phase 4 — PlantUML image:** `insertInlineImage` with public URL (đã hoạt động)

### Native Table Insertion

- `parse_tables()` returns `[{'clean': text, 'original': markdown}]` per cell
- Find table regions: consecutive paragraphs with ` | ` separators
- Process **bottom-to-top** to avoid index shifting
- Cell paragraphs: `table.tableRows[i].tableCells[j].content`
- Insert cells in **reverse order** (last cell first)

### Bold in Table Cells (critical)

`insertText` inherits formatting from adjacent text runs → causes unwanted bold.
Fix: after inserting cell text, strip inherited bold, then re-apply only where needed:
1. `updateTextStyle:bold=False` on full cell range
2. `updateTextStyle:bold=True` only on ranges from `**bold**` markers

### Rate Limiting

- 60 write requests/minute/user
- Batch 20 requests + 3s delay between batches
- Retry 3 times with exponential backoff on 429

## Hạn chế

- **PlantUML:** `insertInlineImage` with public URL đã hoạt động. Fallback: render PNG thủ công
- **Tables:** Native tables hỗ trợ tốt. Không merge cells phức tạp
- **Formatting:** Hỗ trợ bold, italic, heading, bullets, inline code (Courier New), native tables
- **Index arithmetic:** Google Docs dùng character index, phải re-read sau mỗi batchUpdate

---

## Error Handling

| Lỗi | Nguyên nhân | Giải pháp |
|-----|-------------|-----------|
| `credentials.json not found` | Chưa đặt credentials | User đặt file vào root project |
| `Token expired` | Token hết hạn | Auto-refresh, hoặc re-auth |
| `Document not found` | Sai document ID hoặc không có quyền | Kiểm tra link và quyền truy cập |
| `Invalid index` | Document thay đổi giữa read và write | Re-read document trước khi write |
| `Quota exceeded` | Quá nhiều request | Chờ 60s, retry |

---

## Files

```
.claude/skills/gdocs/
├── SKILL.md                    # File này
└── scripts/
    ├── requirements.txt        # Python dependencies
    ├── auth.py                 # OAuth2 authentication
    ├── client.py               # Google Docs API client
    ├── converter.py            # Markdown → Google Docs requests
    ├── plantuml_renderer.py    # PlantUML → PNG
    └── cli.py                  # CLI entry point
```
