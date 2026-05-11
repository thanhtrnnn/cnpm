# CNPM-HRM

Hệ thống **Quản lý Nhân sự Khách sạn (HRM)** — dự án môn Nhập môn Công nghệ Phần mềm. Bao gồm tài liệu UP (Unified Process) đầy đủ, công cụ tạo biểu đồ UML qua Visual Paradigm, và tích hợp Notion.

---

## Cấu trúc dự án

| Thư mục | Mô tả | Link |
|---------|-------|------|
| `.claude/skills/cnpm/` | Skill tạo tài liệu UP (10 mục, JFrame/React) | [SKILL.md](.claude/skills/cnpm/SKILL.md) |
| `.claude/skills/cnpm-vp/` | Skill tích hợp Visual Paradigm (35 tools) | [SKILL.md](.claude/skills/cnpm-vp/SKILL.md) |
| `.claude/skills/notion-format/` | Skill format markdown cho Notion | [SKILL.md](.claude/skills/notion-format/SKILL.md) |
| `visual-paradigm-mcp-plugin/` | VP MCP Server (Java, Undertow, SSE) | [GitHub](https://github.com/thanhtrnnn/vp-mcp) |
| `docs/` | Hướng dẫn UP, Deployment, QA, SQL | [huong-dan-up-cnpm.md](docs/huong-dan-up-cnpm.md) |
| `src/` | Source code hệ thống HRM | |

```
cnpm-hrm/
├── .claude/skills/
│   ├── cnpm/                  → SKILL.md + references/
│   ├── cnpm-vp/               → SKILL.md + scripts/
│   ├── notion-format/         → SKILL.md
│   └── frontend-design/       → SKILL.md
├── docs/                      → UP guide, DEPLOYMENT, QA, SQL
├── visual-paradigm-mcp-plugin → submodule → github.com/thanhtrnnn/vp-mcp
├── src/                       → Java source
└── README.md
```

---

## Các Skills

### 1. `cnpm` — Tạo tài liệu UP

Tự động sinh tài liệu 10 mục theo quy trình Unified Process:

| Pha | Mục | Nội dung |
|-----|-----|----------|
| Requirements | 1–2 | UC chi tiết, Kịch bản chuẩn/ngoại lệ |
| Analysis | 3–5 | Thực thể, Lớp BCE, Tuần tự phân tích |
| Design | 6–9 | Lớp TK, ERD, Wireframe + Lớp TK, Tuần tự TK |
| Test | 10 | Test Plan + Test Case |

**Tùy chọn công nghệ giao diện** (chọn ở BƯỚC 0 PLAN):
- **JFrame (Java Swing)** — Desktop app, Boundary extends JFrame
- **HTML (React)** — Web app, Boundary là React component

### 2. `cnpm-vp` — Visual Paradigm Integration

Tạo biểu đồ UML trực tiếp trong Visual Paradigm qua MCP server ([35 tools](https://github.com/thanhtrnnn/vp-mcp)):
- Use Case, Class, ERD, Sequence diagrams
- Auto layout, generate reports, export DDL
- Scripts kiểm tra và setup kết nối
- [Source code](https://github.com/thanhtrnnn/vp-mcp) · [PR #1](https://github.com/orgatex/visual-paradigm-mcp-plugin/pull/1)

### 3. `notion-format` — Format cho Notion

Định dạng markdown chuẩn để import vào Notion qua API:
- Callout, columns, toggle, table
- PlantUML image embedding
- Rules cho bố cục 2–4 columns

---

## Quick Start

### Yêu cầu

- Node.js / Python 3
- Docker (cho VP MCP server)
- Visual Paradigm (optional, cho standalone mode)
- Claude Code CLI

### Bước 1 — Khởi động VP MCP Server

```bash
cd visual-paradigm-mcp-plugin
./run docker-up
```

Server chạy trên `http://localhost:2026/sse`.

### Bước 2 — Đăng ký MCP với Claude Code

```bash
.claude/skills/cnpm-vp/scripts/vp-mcp-setup.sh
```

### Bước 3 — Kiểm tra kết nối

```bash
.claude/skills/cnpm-vp/scripts/vp-mcp-verify.sh
```

### Bước 4 — Sử dụng

Mở Claude Code và yêu cầu:
- *"Viết tài liệu UP cho module Đặt phòng"* → dùng skill `cnpm`
- *"Vẽ biểu đồ lớp trong VP"* → dùng skill `cnpm-vp`
- *"Format tài liệu này cho Notion"* → dùng skill `notion-format`

---

## VP MCP Server

> **Source:** [thanhtrnnn/vp-mcp](https://github.com/thanhtrnnn/vp-mcp) · **PR:** [orgatex#1](https://github.com/orgatex/visual-paradigm-mcp-plugin/pull/1)

### Tools (35 total)

| Nhóm | Tools | Mô tả |
|------|-------|-------|
| Management | `listDiagrams`, `getDiagramElements`, `autoLayoutDiagram`, `removeDiagramElement` | Quản lý diagram |
| Use Case | `createUseCaseDiagram`, `addActor`, `addUseCase`, `addRelationship`, `generateUseCaseReport` | UC diagrams |
| Class | `createClassDiagram`, `addClass`, `addAttribute`, `addOperation`, `addAssociation`, `addGeneralization`, `addAggregation`, `addComposition`, `addDependency`, `addRealization`, `addInterface`, `generateClassReport` | Class diagrams |
| ERD | `createErd`, `addTable`, `addColumn`, `addForeignKey`, `addTableRelationship`, `generateDdl`, `generateErdReport` | ER diagrams |
| Sequence | `createSequenceDiagram`, `addLifeline`, `addActivation`, `addMessage`, `addReturnMessage`, `addCombinedFragment`, `generateSequenceReport` | Sequence diagrams |

### Commands

```bash
cd visual-paradigm-mcp-plugin

./run build          # Build plugin
./run test           # Run tests
./run package        # Package JAR
./run install        # Install to VP
./run docker-build   # Build Docker image
./run docker-up      # Start MCP server (Docker)
./run docker-down    # Stop MCP server
./run docker-logs    # View logs
```

---

## Tài liệu UP

File [docs/huong-dan-up-cnpm.md](docs/huong-dan-up-cnpm.md) chứa hướng dẫn đầy đủ 10 mục theo UP, với ví dụ cụ thể cho hệ thống HRM module Đặt phòng. File đã được format theo chuẩn Notion Enhanced Markdown (callout, columns, toggle) và có 9 biểu đồ PlantUML embedded.

---

## Hệ thống HRM

**Phạm vi:** Hệ thống quản lý nhân sự khách sạn, ứng dụng desktop dùng nội bộ.

**Actors:**
- Nhân viên lễ tân: Đặt/hủy phòng, check-in, check-out
- Nhân viên bán hàng: Đặt phòng qua điện thoại
- Người quản lý: Cập nhật KS/phòng, xem báo cáo
- Quản trị hệ thống: Quản lý tài khoản

**Đối tượng chính:** Khách sạn, Phòng, Khách hàng, Đặt phòng, Hóa đơn, Nhân viên, Tài khoản
