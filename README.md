# CNPM Skills

Bộ skill Claude Code tự động tạo tài liệu phần mềm chuẩn **Unified Process (UP)** theo giáo trình **Nhập môn Công nghệ Phần mềm**. Hỗ trợ JFrame (Java Swing) và HTML (React).

---

## Cấu trúc

```
.claude/skills/
├── cnpm/                  → Tạo tài liệu UP (text + PlantUML)
│   ├── SKILL.md           → Skill chính (448 dòng)
│   ├── cnpm.skill         → Phiên bản nén (.zip)
│   └── references/        → 11 file tham khảo theo 4 pha UP
├── cnpm-vp/               → Vẽ biểu đồ trong Visual Paradigm
│   ├── SKILL.md           → Skill chính (420+ dòng)
│   ├── cnpm-vp.skill      → Phiên bản nén (.zip)
│   └── scripts/           → Setup & verify VP MCP server
└── notion-format/         → Format markdown cho Notion
```

---

## 2 Version: `cnpm` vs `cnpm-vp`

| | `cnpm` | `cnpm-vp` |
|---|---|---|
| **Mục đích** | Sinh nội dung tài liệu UP | Vẽ biểu đồ UML trong Visual Paradigm |
| **Đầu ra** | Text + bảng Markdown + PlantUML code block | Diagram trong VP → export PNG/SVG |
| **Output format** | Markdown, Notion, DOCX | VP diagram image |
| **Công nghệ** | Không cần cài thêm | Cần VP MCP server (Docker) |
| **Khi nào dùng** | Luôn dùng khi viết tài liệu UP | Khi muốn diagram chuyên nghiệp thay vì PlantUML |

**Workflow chuẩn:** Dùng `cnpm` sinh nội dung → Dùng `cnpm-vp` vẽ diagram → Nhúng ảnh vào tài liệu.

---

## cài đặt

### Yêu cầu

- Claude Code CLI
- Node.js (cho generate DOCX)
- Docker (cho VP MCP server — chỉ cần khi dùng `cnpm-vp`)
- Visual Paradigm (optional, cho standalone mode)

### Bước 1 — Copy skills vào project

```bash
# Clone repo hoặc copy thư mục .claude/skills/ vào project của bạn
cp -r .claude/skills/ /path/to/your-project/.claude/skills/
```

### Bước 2 — Cài dependencies (nếu cần generate DOCX)

```bash
cd output
npm install docx
```

### Bước 3 — Setup VP MCP Server (nếu dùng `cnpm-vp`)

```bash
# Khởi động server
cd visual-paradigm-mcp-plugin
./run docker-up

# Đăng ký MCP với Claude Code
.claude/skills/cnpm-vp/scripts/vp-mcp-setup.sh

# Kiểm tra kết nối
.claude/skills/cnpm-vp/scripts/vp-mcp-verify.sh

# Restart Claude Code để nhận MCP config mới
```

---

## Hướng dẫn sử dụng

### Skill `cnpm` — Tạo tài liệu UP

Mở Claude Code, yêu cầu:

```
"Viết tài liệu UP cho module Quản lý Mượn Sách"
"Làm phần requirements cho hệ thống"
"Viết analysis cho module Đặt phòng"
"Viết test case cho chức năng đăng nhập"
```

Skill sẽ tự động:
1. **BƯỚC 0 PLAN** — Sinh plan, hỏi công nghệ giao diện (JFrame/React), chờ xác nhận
2. **Giai đoạn 1** — Requirements toàn hệ thống (UC, thuật ngữ, mô hình nghiệp vụ)
3. **Giai đoạn 2** — Đề xuất phân module → chờ xác nhận
4. **Giai đoạn 3** — Triển khai từng module theo 4 pha:
   - Pha I: Requirements (UC chi tiết, kịch bản)
   - Pha II: Analysis (thực thể, lớp BCE, tuần tự)
   - Pha III: Design (lớp TT, ERD, wireframe, tuần tự TK)
   - Pha IV: Test (test plan, test case)

### Skill `cnpm-vp` — Vẽ biểu đồ trong VP

```
"Vẽ biểu đồ lớp trong VP cho module Mượn sách"
"Tạo UC diagram trong Visual Paradigm"
"Vẽ sequence diagram cho chức năng đăng nhập"
```

Skill sẽ tự động:
1. Tạo diagram trong VP qua MCP tools
2. Thêm elements theo đúng cấu trúc BCE (Boundary | DAO | Entity)
3. Auto layout
4. Export ảnh PNG/SVG

### Tạo DOCX

```bash
cd output
node generate_docx.js
# → De01_QuanLyMuonSach.docx
```

---

## VP MCP Server

> **Source:** [thanhtrnnn/vp-mcp](https://github.com/thanhtrnnn/vp-mcp)

### 35 Tools

| Nhóm | Tools |
|------|-------|
| Management | `listDiagrams`, `getDiagramElements`, `autoLayoutDiagram`, `removeDiagramElement` |
| Use Case | `createUseCaseDiagram`, `addActor`, `addUseCase`, `addRelationship`, `generateUseCaseReport` |
| Class | `createClassDiagram`, `addClass`, `addAttribute`, `addOperation`, `addAssociation`, `addGeneralization`, `addAggregation`, `addComposition`, `addDependency`, `addRealization`, `addInterface`, `generateClassReport` |
| ERD | `createErd`, `addTable`, `addColumn`, `addForeignKey`, `addTableRelationship`, `generateDdl`, `generateErdReport` |
| Sequence | `createSequenceDiagram`, `addLifeline`, `addActivation`, `addMessage`, `addReturnMessage`, `addCombinedFragment`, `generateSequenceReport` |

### Commands

```bash
cd visual-paradigm-mcp-plugin
./run build          # Build plugin
./run test           # Run tests
./run docker-up      # Start MCP server
./run docker-down    # Stop MCP server
```

---

## Files mẫu

| File | Mô tả |
|------|-------|
| [DE01.md](DE01.md) | Đề bài Quản lý Mượn Sách |
| [output/De01_QuanLyMuonSach.docx](output/De01_QuanLyMuonSach.docx) | Word document mẫu (UC + Kịch bản + Thực thể) |
| [docs/huong-dan-up-cnpm.md](docs/huong-dan-up-cnpm.md) | Hướng dẫn UP đầy đủ với PlantUML |
