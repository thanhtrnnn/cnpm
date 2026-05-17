---
name: cnpm-vp
description: >
  Tạo biểu đồ UML trong Visual Paradigm thông qua VP MCP server, rồi xuất ảnh và nhúng vào
  tài liệu UP. Kích hoạt khi người dùng muốn: vẽ biểu đồ UML trong Visual Paradigm,
  tạo diagram trong VP, export ảnh VP, nhúng ảnh VP vào tài liệu, hoặc bất kỳ yêu cầu
  nào liên quan đến việc sử dụng Visual Paradigm kết hợp với tài liệu CNPM/UP.
  LUÔN dùng skill này khi người dùng nhắc đến "Visual Paradigm", "VP", "vẽ trong VP",
  "xuất ảnh VP", hoặc muốn diagram chuyên nghiệp thay vì PlantUML code block.
---

# CNPM-VP Skill — Visual Paradigm MCP Integration

Tạo biểu đồ UML trực tiếp trong Visual Paradigm qua VP MCP server, xuất ảnh, và nhúng vào
tài liệu UP. Kết hợp với skill `cnpm` để sinh nội dung tài liệu.

---

## Điều kiện tiên quyết

VP MCP server phải đang chạy và được đăng ký trong `.mcp.json`.

**Bước 1 — Khởi động VP MCP server:**
```bash
cd visual-paradigm-mcp-plugin
./run docker-up
```

**Bước 2 — Đăng ký MCP server với Claude Code:**
```bash
.claude/skills/cnpm-vp/scripts/vp-mcp-setup.sh
```
Script này tự tạo/cập nhật `.mcp.json` ở project root.

**Bước 3 — Xác nhận kết nối:**
```bash
.claude/skills/cnpm-vp/scripts/vp-mcp-verify.sh
```
Script kiểm tra: port mở, SSE endpoint reachable, MCP protocol respond, `.mcp.json` đúng cấu hình.

Sau đó restart Claude Code để nhận MCP config mới.

---

## Nguyên tắc cốt lõi

1. **Skill `cnpm` sinh nội dung, skill `cnpm-vp` vẽ trong VP.** Không tự viết PlantUML khi người dùng muốn dùng VP.
2. **Thứ tự tạo diagram:** Tạo diagram → thêm elements → thêm relationships → auto layout → export.
3. **Ảnh VP ưu tiên hơn PlantUML** khi người dùng yêu cầu hoặc khi diagram quá phức tạp cho code block.
4. **Luôn auto layout** sau khi thêm xong tất cả elements — VP layout engine tốt hơn sắp xếp thủ công.

---

## Danh sách MCP Tools (35 tools)

### Diagram Management

| Tool | Mô tả | Tham số chính |
|------|-------|---------------|
| `listDiagrams` | Liệt kê tất cả diagram (filter: UseCase/Class/Sequence/ER) | `type` ("" = all) |
| `getDiagramElements` | Lấy tất cả elements trên diagram | `diagramName` |
| `autoLayoutDiagram` | Tự động căn layout | `diagramName` |
| `removeDiagramElement` | Xóa element khỏi diagram | `diagramName`, `elementName` |

### Use Case Diagram

| Tool | Mô tả | Tham số chính |
|------|-------|---------------|
| `createUseCaseDiagram` | Tạo diagram mới | `diagramName` |
| `addActor` | Thêm actor | `actorName`, `diagramName` |
| `addUseCase` | Thêm use case | `useCaseName`, `diagramName` |
| `addRelationship` | Thêm Include/Extend/Generalization | `sourceName`, `targetName`, `relationshipType` |
| `generateUseCaseReport` | Sinh báo cáo phân tích | `diagramName` |

### Class Diagram

| Tool | Mô tả | Tham số chính |
|------|-------|---------------|
| `createClassDiagram` | Tạo diagram mới | `diagramName` |
| `addClass` | Thêm class | `diagramName`, `className` |
| `addAttribute` | Thêm thuộc tính | `className`, `attributeName`, `attributeType`, `visibility` |
| `addOperation` | Thêm phương thức | `className`, `operationName`, `returnType`, `params` |
| `addAssociation` | Thêm association | `diagramName`, `fromClass`, `toClass`, multiplicities, `name` |
| `addGeneralization` | Thêm kế thừa | `diagramName`, `fromClass`, `toClass` |
| `addAggregation` | Thêm aggregation (◇) | `diagramName`, `fromClass`, `toClass`, multiplicities |
| `addComposition` | Thêm composition (◆) | `diagramName`, `fromClass`, `toClass`, multiplicities |
| `addDependency` | Thêm dependency (-->) | `diagramName`, `fromClass`, `toClass` |
| `addRealization` | Thêm implements | `diagramName`, `fromClass`, `toClass` |
| `addInterface` | Thêm interface | `diagramName`, `interfaceName` |
| `generateClassReport` | Sinh báo cáo | `diagramName` |

### ERD

| Tool | Mô tả | Tham số chính |
|------|-------|---------------|
| `createErd` | Tạo ERD mới | `diagramName` |
| `addTable` | Thêm bảng | `diagramName`, `tableName` |
| `addColumn` | Thêm cột | `tableName`, `columnName`, `columnType`, `length`, `scale`, `isPrimaryKey`, `isNullable` |
| `addForeignKey` | Thêm FK | `diagramName`, `fromTable`, `toTable`, columns, `relationshipName` |
| `addTableRelationship` | Thêm quan hệ bảng | `diagramName`, `fromTable`, `toTable`, `type`, multiplicities |
| `generateDdl` | Sinh DDL | `diagramName` |
| `generateErdReport` | Sinh báo cáo | `diagramName` |

### Sequence Diagram

| Tool | Mô tả | Tham số chính |
|------|-------|---------------|
| `createSequenceDiagram` | Tạo diagram mới | `diagramName` |
| `addLifeline` | Thêm lifeline | `diagramName`, `lifelineName`, `className` |
| `addActivation` | Thêm activation bar | `diagramName`, `lifelineName` |
| `addMessage` | Thêm message | `diagramName`, `fromLifeline`, `toLifeline`, `messageName`, `sequenceNumber`, `messageType` |
| `addReturnMessage` | Thêm return message | `diagramName`, `fromLifeline`, `toLifeline`, `messageName`, `sequenceNumber` |
| `addCombinedFragment` | Thêm alt/opt/loop | `diagramName`, `operator`, `guard`, `coveredLifelines` |
| `generateSequenceReport` | Sinh báo cáo | `diagramName` |

---

## Quy trình tạo diagram theo loại

### Use Case Diagram

```
1. createUseCaseDiagram(diagramName)
2. addActor(actorName, diagramName)        — cho mỗi actor
3. addUseCase(useCaseName, diagramName)    — cho mỗi UC (bao gồm UC con generalization)
4. addRelationship(source, target, type)   — Include, Extend, hoặc Generalization
5. autoLayoutDiagram(diagramName)          — LUÔN chạy cuối cùng
6. generateUseCaseReport(diagramName)      — optional, kiểm tra kết quả
```

**Thứ tự thêm relationships:**
1. Include (UC chính → UC phụ bắt buộc)
2. Extend (UC mở rộng → UC chính)
3. Generalization (UC con → UC cha, mũi tên tam giác rỗng)

**Layout:** UC chính ở giữa, UC include tỏa phải, UC extend tỏa dưới phải, UC generalization tỏa dưới. Tránh xếp dọc — luôn dàn ngang.

**Ví dụ: Module Quản lý Khách hàng**
```
createUseCaseDiagram("UC - QuanLyKhachHang")
addActor("NhanVien", "UC - QuanLyKhachHang")
addUseCase("Tim kiem khach hang", "UC - QuanLyKhachHang")
addUseCase("Them moi khach hang", "UC - QuanLyKhachHang")
addUseCase("Xac minh CCCD", "UC - QuanLyKhachHang")
addUseCase("Tim theo ten", "UC - QuanLyKhachHang")
addUseCase("Tim theo ma", "UC - QuanLyKhachHang")
addRelationship("Tim kiem khach hang", "Xac minh CCCD", "Include")
addRelationship("Tim theo ten", "Tim kiem khach hang", "Generalization")
addRelationship("Tim theo ma", "Tim kiem khach hang", "Generalization")
autoLayoutDiagram("UC - QuanLyKhachHang")
```

### Class Diagram

```
1. createClassDiagram(diagramName)
2. addClass(diagramName, className)                    — cho mỗi class
3. addAttribute(className, name, type, visibility)     — cho mỗi thuộc tính
4. addOperation(className, name, returnType, params)   — cho mỗi phương thức
5. addXxxRelationship(...)                             — association/aggregation/composition/generalization
6. addInterface(diagramName, interfaceName)             — nếu có interface
7. addRealization(diagramName, fromClass, toClass)      — implements
8. autoLayoutDiagram(diagramName)
```

**Thứ tự thêm relationships:** Generalization → Composition → Aggregation → Association → Dependency → Realization

**Ví dụ: Biểu đồ lớp thiết kế Module KH**
```
createClassDiagram("Class - QuanLyKhachHang")
addClass("Class - QuanLyKhachHang", "GDTimKHFrm")
addClass("Class - QuanLyKhachHang", "KhachHangDAO")
addClass("Class - QuanLyKhachHang", "KhachHang")
addClass("Class - QuanLyKhachHang", "DAO")
addAttribute("GDTimKHFrm", "inTen", "JTextField", "private")
addAttribute("GDTimKHFrm", "subTim", "JButton", "private")
addOperation("GDTimKHFrm", "actionPerformed", "void", "e:ActionEvent")
addAttribute("KhachHang", "ma", "int", "private")
addAttribute("KhachHang", "ten", "String", "private")
addOperation("KhachHangDAO", "timKH", "List<KhachHang>", "ten:String")
addGeneralization("Class - QuanLyKhachHang", "KhachHangDAO", "DAO")
addDependency("Class - QuanLyKhachHang", "GDTimKHFrm", "KhachHangDAO")
autoLayoutDiagram("Class - QuanLyKhachHang")
```

### ERD

```
1. createErd(diagramName)
2. addTable(diagramName, tableName)                               — cho mỗi bảng
3. addColumn(tableName, columnName, type, length, scale, PK, nullable)  — cho mỗi cột
4. addForeignKey(diagramName, from, to, columns, fkName)          — cho mỗi FK
5. addTableRelationship(diagramName, from, to, type, multiplicities)  — nếu cần
6. autoLayoutDiagram(diagramName)
7. generateDdl(diagramName)                                        — optional, sinh DDL
```

**Ví dụ:**
```
createErd("ERD - QuanLyKhachHang")
addTable("ERD - QuanLyKhachHang", "tblKhachHang")
addColumn("tblKhachHang", "ma", "INT", 10, 0, true, false)
addColumn("tblKhachHang", "ten", "VARCHAR", 255, 0, false, false)
addColumn("tblKhachHang", "cccd", "VARCHAR", 20, 0, false, false)
addTable("ERD - QuanLyKhachHang", "tblHopDong")
addColumn("tblHopDong", "ma", "INT", 10, 0, true, false)
addColumn("tblHopDong", "ngayKy", "DATE", 0, 0, false, false)
addColumn("tblHopDong", "tblKhachHangma", "INT", 10, 0, false, false)
addForeignKey("ERD - QuanLyKhachHang", "tblHopDong", "tblKhachHang", "tblKhachHangma", "ma", "FK_KH_HD")
autoLayoutDiagram("ERD - QuanLyKhachHang")
generateDdl("ERD - QuanLyKhachHang")
```

### Sequence Diagram

```
1. createSequenceDiagram(diagramName)
2. addLifeline(diagramName, lifelineName, className)   — cho mỗi participant
3. addActivation(diagramName, lifelineName)             — trước mỗi group message
4. addMessage(diagramName, from, to, name, seq, type)  — sync message
5. addReturnMessage(diagramName, from, to, name, seq)  — return
6. addCombinedFragment(diagramName, operator, guard, lifelines)  — alt/opt/loop
7. autoLayoutDiagram(diagramName)
```

**Ví dụ:**
```
createSequenceDiagram("SD - TimKH")
addLifeline("SD - TimKH", "Actor", "NhanVien")
addLifeline("SD - TimKH", "GDTimKHFrm", "GDTimKHFrm")
addLifeline("SD - TimKH", "KhachHangDAO", "KhachHangDAO")
addActivation("SD - TimKH", "GDTimKHFrm")
addMessage("SD - TimKH", "Actor", "GDTimKHFrm", "nhap tu khoa + nhan Tim", "1", "sync")
addMessage("SD - TimKH", "GDTimKHFrm", "KhachHangDAO", "timKH(ten:String)", "2", "sync")
addReturnMessage("SD - TimKH", "KhachHangDAO", "GDTimKHFrm", "List<KhachHang>", "3")
addReturnMessage("SD - TimKH", "GDTimKHFrm", "Actor", "hien thi danh sach", "4")
addCombinedFragment("SD - TimKH", "alt", "timKH() tra ve rong", "GDTimKHFrm,Actor")
autoLayoutDiagram("SD - TimKH")
```

---

## Xuất ảnh và nhúng vào tài liệu

### Cách xuất ảnh từ VP

VP MCP hiện tại **không có tool export ảnh trực tiếp**. Các cách thay thế:

**Cách 1 — Screenshot từ VP application (khuyến nghị):**
1. Mở diagram trong Visual Paradigm
2. Menu: Diagram → Export as Image → PNG/SVG
3. Lưu vào thư mục `docs/images/`
4. Nhúng vào markdown: `![Tên biểu đồ](images/ten-file.png)`

**Cách 2 — VP Command Line (nếu có):**
```bash
# Export diagram as PNG via VP CLI (nếu cài đặt)
vpcmd -export diagram "Diagram Name" -format png -output docs/images/
```

**Cách 3 — Generate Report thay thế:**
Nếu không cần ảnh, dùng `generateXxxReport` để lấy text report nhúng vào tài liệu.

### Nhúng ảnh vào tài liệu Notion

Sau khi có file ảnh, dùng Notion API để upload và nhúng:

```markdown
![Biểu đồ lớp – Module KH](images/class-quanlykhachhang.png)
```

Hoặc nếu ảnh đã upload lên hosting khác:
```markdown
![Biểu đồ lớp – Module KH](https://url-to-image.png)
```

---

## Quy trình tổng hợp: cnpm + cnpm-vp

Khi người dùng muốn tài liệu UP với biểu đồ VP:

```
1. Dùng skill cnpm → BƯỚC 0 PLAN (hỏi cả công nghệ giao diện + có dùng VP không)
2. Dùng skill cnpm → sinh nội dung các mục (text + bảng)
3. Dùng skill cnpm-vp → tạo diagram trong VP theo nội dung đã sinh
4. Dùng skill cnpm-vp → export ảnh từ VP
5. Dùng skill notion-format → nhúng ảnh vào tài liệu Notion
```

**Khi nào dùng VP thay vì PlantUML:**
- Diagram phức tạp (nhiều class, nhiều relationship)
- Cần diagram chuyên nghiệp cho báo cáo/presentation
- Người dùng yêu cầu
- Diagram cần chỉnh sửa trực quan (drag & drop)

**Khi nào giữ PlantUML:**
- Diagram đơn giản
- Chỉ cần text-based documentation
- Không có VP MCP server đang chạy
- Người dùng không yêu cầu VP

---

## Constraints

- VP MCP server phải chạy trên `localhost:2026` (hoặc URL tùy chỉnh)
- Tên diagram trong VP phải unique — nếu trùng sẽ lỗi
- Tham số rỗng: truyền `""` (empty string), KHÔNG truyền null
- Tên element trong VP KHÔNG được chứa ký tự đặc biệt (dùng tiếng Việt không dấu nếu cần)
- `addColumn`: `length` và `scale` là integer, không phải string
- `addMessage`: `messageType` chỉ nhận `"sync"` hoặc `"async"`
- `addCombinedFragment`: `operator` chỉ nhận `"alt"`, `"opt"`, `"loop"`, `"break"`, `"par"`
- Relationship trong class diagram: thêm **sau khi** đã add tất cả classes và attributes
- Sequence diagram: add lifelines **trước**, messages **sau**
