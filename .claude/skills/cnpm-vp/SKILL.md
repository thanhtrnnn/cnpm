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

## Nguyên tắc cấu trúc (khi vẽ trong VP)

Khi tạo biểu đồ trong VP, PHẢI tuân thủ các quy tắc cấu trúc sau:

1. **BCE — phân tách bằng TÊN + BỐ CỤC, KHÔNG bằng package màu:** Class diagram tách 3 vai trò Boundary | Control/DAO | Entity qua **tên hậu tố** (Boundary = `View` (phân tích) / `Page` hoặc `Frm` (thiết kế), Control = `Controller`, DAO = `DAO`, Entity = PascalCase trơn) và **bố cục** (hàng Boundary trên cùng, Entity bên dưới). KHÔNG cần package bao quanh.
2. **Hộp lớp để TRẮNG (khớp biểu đồ mẫu):** Biểu đồ lớp tham chiếu của môn học (`exports/services/screenshots`, `exports/account/screenshots`) dùng **hộp trắng trơn — KHÔNG màu nền, KHÔNG package màu**.
   - Mặc định: gọi `addClass` **KHÔNG** truyền `packageName`/`packageColor` (để trắng).
   - Chỉ đóng package màu khi user yêu cầu tường minh.
   - Màu xanh `#7AD2FF` **chỉ** áp dụng cho actor / use case / lifeline / activation — VP MCP **tự tô** (xem mục Render). KHÔNG tô màu hộp lớp.
3. **Stereotype lớp: KHÔNG dùng trên class diagram (khớp mẫu):** Mẫu không hiển thị `<<Boundary>>`/`<<Entity>>` trên hộp lớp.
   - Mặc định: `addClass` **KHÔNG** truyền `stereotype`.
   - Ngoại lệ: sequence **lifeline** VẪN truyền `lifelineType` = `boundary`/`control`/`entity`/`actor` để VP hiển thị icon tròn-gạch đúng (đây là yêu cầu của mẫu tuần tự).

4. **Phân biệt ngôn ngữ theo pha (NGHIÊM NGẶT — khớp cnpm):**
   - **Arrow label trong biểu đồ VP (@message):** TOÀN BỘ tiếng Anh ngắn gọn trong cả hai pha (`enter keyword + click Search`, `checkLogin()`, `display results`). KHÔNG dùng tiếng Việt trong message VP.
   - **Pha Thiết kế:** Arrow = tên hàm tiếng Anh đầy đủ + kiểu dữ liệu (`searchFreeRoom(checkin: Date, checkout: Date): List<Room>`).
   - **Kịch bản phiên bản 2/3 (text bên ngoài biểu đồ):** Giữ tiếng Việt tự nhiên.
   - **Tên class/bảng DB:** BẮT BUỘC tiếng Anh PascalCase (`Client`, `Employee`, `tblClient`). Tên Việt chỉ trong văn xuôi.
   - **Tên method:** Luôn tiếng Anh mọi pha (`checkLogin`, `searchFreeRoom`).
5. **UC Decomposition:** Include → Extend → Generalization. UC chính ở giữa, UC con tỏa ra.
6. **Horizontal layout:** `autoLayoutDiagram` cố gắng dàn ngang — nhưng **KHÔNG có tool đặt toạ độ**. Nếu layout chồng/dọc sau autoLayout, phải mở VP chỉnh tay. Kiểm tra bằng `getDiagramElements` (x positions khác nhau = đã dàn ngang).
7. **Sequence participant order:** Actor → Boundary → [Control] → DAO → Entity
8. **Công nghệ giao diện:** Phải thống nhất JFrame (Java Swing) hoặc HTML (React) từ đầu. Ảnh hưởng đến Boundary class attributes.

### Chọn công nghệ giao diện

Hỏi người dùng ngay từ đầu:
- **JFrame (Java Swing):** Boundary = JFrame, attributes = JTextField/JButton/JTable, event = `actionPerformed(e: ActionEvent)`. Tên class: `[EnglishName]Frm` (VD: `LoginFrm`, `SearchRoomFrm`, `EditRoomFrm`). **KHÔNG dùng** tiền tố `GD` hay tên tiếng Việt.
- **HTML (React):** Boundary = Component, attributes = State/JSX, event = `handleSubmit/onClick`. Tên class: tiếng Anh + hậu tố loại component:

| Hậu tố | Loại component | Ví dụ |
|--------|---------------|-------|
| `Page` | Trang gắn URL/Router | `RoomPage`, `OrderPage` |
| `Card` | Ô thông tin nhỏ trong danh sách | `RoomCard`, `ProductCard` |
| `Panel` | Vùng nội dung lớn trên trang | `SessionDetailPanel` |
| `Modal` | Hộp thoại bật lên | `ExtendTimeModal` |
| `Form` | Vùng nhập liệu | `OrderForm`, `AddClientForm` |
| `Table` | Bảng dữ liệu | `RoomListTable` |

### Tiền tố thuộc tính Boundary (Thiết kế — khớp cnpm)

Boundary class trong pha **thiết kế** dùng tiền tố chuẩn sau (khớp với `cnpm/references/iii.3.2_sodo_lop_thietke.md`):

**JFrame:**

| Tiền tố | Kiểu VP | Ví dụ |
|---------|---------|-------|
| `txt` | JTextField | `txtUsername`, `txtRoomName` |
| `btn` | JButton | `btnLogin`, `btnSearch` |
| `tbl` | JTable | `tblResults` |
| `lbl` | JLabel | `lblMessage` |

**React:**

| Tiền tố | Kiểu | Ví dụ |
|---------|------|-------|
| `txt` | TextBox | `txtUsername`, `txtRoomName` |
| `btn` | Button | `btnLogin`, `btnSearch` |
| `tbl` | Table | `tblActiveRooms` |
| `lbl` | Label | `lblRoomName` |

### Tiền tố thuộc tính Boundary (Phân tích — khớp mẫu image_08)

Boundary class pha **phân tích** dùng tiền tố **camelCase tiếng Anh, KHÔNG kiểu dữ liệu, KHÔNG dấu gạch dưới** (xác nhận từ `exports/services/screenshots/image_08.png`):

| Tiền tố | Ý nghĩa | Ví dụ từ mẫu |
|---------|---------|--------------|
| `in` | Ô nhập liệu | `-inUsername`, `-inPassword`, `-inRoomName`, `-inProductName` |
| `out` | Chỉ hiển thị | `-outRoomName`, `-outProductList`, `-outSuccess` |
| `sub` | Nút hành động | `-subLogin`, `-subSearchRoom`, `-subCreateOrder`, `-subAdd`, `-subSave`, `-subConfirm` |
| `outsub` | Bảng/danh sách click được | `-outsubRoomList` |

- Boundary phân tích **chỉ có attributes, KHÔNG có method**.
- Entity phân tích: attributes `-` (không kiểu) **VÀ** method `+methodName()` (có `()`, không tham số): `+checkLogin()`, `+searchActiveRoom()`, `+addOrder()`.

---

## Render: màu sắc tự động (khớp biểu đồ mẫu)

VP MCP **tự tô màu xanh `#7AD2FF`** cho actor / use case / lifeline / activation bar (biểu đồ UC + tuần tự) — không cần gọi tool tô màu. Hộp lớp (class) và bảng (ERD) giữ **trắng** mặc định. Đây là quy ước render khớp với biểu đồ mẫu của môn học và theme PlantUML của skill `cnpm`.

## Danh sách MCP Tools (39 tools)

### Diagram Management

| Tool | Mô tả | Tham số chính |
|------|-------|---------------|
| `listDiagrams` | Liệt kê tất cả diagram (filter: UseCase/Class/Sequence/ER) | `type` ("" = all) |
| `getDiagramElements` | Lấy tất cả elements + vị trí trên diagram | `diagramName` |
| `getElementCounts` | Lấy summary số lượng element theo loại | `diagramName` |
| `autoLayoutDiagram` | Tự động căn layout | `diagramName` |
| `removeDiagramElement` | Xóa element khỏi diagram | `diagramName`, `elementName` |

### Use Case Diagram

| Tool | Mô tả | Tham số chính |
|------|-------|---------------|
| `createUseCaseDiagram` | Tạo diagram mới | `diagramName` |
| `addActor` | Thêm actor | `actorName`, `diagramName` |
| `addUseCase` | Thêm use case | `useCaseName`, `diagramName` |
| `addRelationship` | Thêm Include/Extend/Generalization | `diagramName`, `sourceName`, `targetName`, `relationshipType` |
| `addSystemBoundary` | Bao tất cả use case trong khung hệ thống (hộp module) — gọi **SAU** `autoLayoutDiagram` | `diagramName`, `systemName` |
| `generateUseCaseReport` | Sinh báo cáo phân tích | `diagramName` |

### Class Diagram

| Tool | Mô tả | Tham số chính |
|------|-------|---------------|
| `createClassDiagram` | Tạo diagram mới | `diagramName` |
| `addClass` | Thêm class | `diagramName`, `className`, `packageName`, `packageColor`, `stereotype`, `isAbstract`, `extendsClass`, `implementsInterfaces` |
| `addPackage` | Thêm package có màu nền | `diagramName`, `packageName`, `backgroundColor` |
| `setClassColor` | Đặt màu nền class | `diagramName`, `className`, `backgroundColor` |
| `addAttribute` | Thêm thuộc tính | `className`, `attributeName`, `attributeType`, `visibility` |
| `addOperation` | Thêm phương thức | `className`, `operationName`, `returnType`, `params` |
| `addAssociation` | Thêm association | `diagramName`, `fromClass`, `toClass`, `fromMult`, `toMult`, `name` |
| `addGeneralization` | Thêm kế thừa | `diagramName`, `fromClass`, `toClass` |
| `addAggregation` | Thêm aggregation (◇) | `diagramName`, `fromClass`, `toClass`, `fromMult`, `toMult` |
| `addComposition` | Thêm composition (◆) | `diagramName`, `fromClass`, `toClass`, `fromMult`, `toMult` |
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
| `addForeignKey` | Thêm FK | `diagramName`, `fromTable`, `toTable`, `fromColumn`, `toColumn`, `relationshipName` |
| `addTableRelationship` | Thêm quan hệ bảng | `diagramName`, `fromTable`, `toTable`, `type`, `fromMult`, `toMult` |
| `generateDdl` | Sinh DDL | `diagramName` |
| `generateErdReport` | Sinh báo cáo | `diagramName` |

### Sequence Diagram

| Tool | Mô tả | Tham số chính |
|------|-------|---------------|
| `createSequenceDiagram` | Tạo diagram mới | `diagramName` |
| `addLifeline` | Thêm lifeline | `diagramName`, `lifelineName`, `className`, `lifelineType`, `alias` |
| `addActivation` | Thêm activation bar | `diagramName`, `lifelineName` |
| `addMessage` | Thêm message | `diagramName`, `fromLifeline`, `toLifeline`, `messageName`, `sequenceNumber`, `messageType` |
| `addReturnMessage` | Thêm return message | `diagramName`, `fromLifeline`, `toLifeline`, `messageName`, `sequenceNumber` |
| `addCombinedFragment` | Thêm alt/opt/loop | `diagramName`, `operator`, `guard`, `coveredLifelines` |
| `generateSequenceReport` | Sinh báo cáo | `diagramName` |

---

## Quy trình tạo diagram theo loại

### Use Case Diagram

```
0. listDiagrams("UseCase") → xác nhận tên diagram chưa tồn tại (unique)
1. createUseCaseDiagram(diagramName)
2. addActor(actorName, diagramName)        — cho mỗi actor
3. addUseCase(useCaseName, diagramName)    — cho mỗi UC (bao gồm UC con generalization)
4. addRelationship(diagramName, source, target, type)   — Include, Extend, hoặc Generalization
5. autoLayoutDiagram(diagramName)          — LUÔN chạy trước khi bao khung
6. addSystemBoundary(diagramName, systemName)  — bao UC trong hộp module (tên module, VD "Dịch vụ và kho hàng"); actor nằm ngoài
7. generateUseCaseReport(diagramName)      — kiểm tra element counts
```

> Biểu đồ UC tổng quan của mẫu (image_02) có **khung hệ thống** bao quanh toàn bộ use case, gắn nhãn tên module, với actor ở ngoài hai bên. `addSystemBoundary` tạo đúng khung này — phải gọi **sau** `autoLayoutDiagram` để khung ôm trọn UC đã được dàn.

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
addRelationship("UC - QuanLyKhachHang", "Tim kiem khach hang", "Xac minh CCCD", "Include")
addRelationship("UC - QuanLyKhachHang", "Tim theo ten", "Tim kiem khach hang", "Generalization")
addRelationship("UC - QuanLyKhachHang", "Tim theo ma", "Tim kiem khach hang", "Generalization")
autoLayoutDiagram("UC - QuanLyKhachHang")
```

### Class Diagram

**Quy tắc BCE (BẮT BUỘC):** Class diagram PHẢI phân rõ 3 nhóm class:
- **Boundary** (trái): Giao diện — JFrame (Swing) hoặc Component (React)
  - **JFrame:** tên class = `[EnglishName]Frm`
  - **React:** tên class = tiếng Anh + hậu tố (`Page`, `Card`, `Panel`, `Modal`, `Form`, `Table`) — xem bảng ở mục "Chọn công nghệ giao diện"
- **DAO/Control** (giữa): Abstract DAO + DAO con kế thừa
- **Entity** (phải): Lớp thực thể từ phân tích

**Mẫu Abstract DAO (Pha Thiết kế — BẮT BUỘC):**
Class diagram thiết kế PHẢI có class AbstractDAO:
```
1. addClass(diagram, "AbstractDAO", packageName="DAO", packageColor="#FFE0B2", stereotype="DAO", isAbstract=true)
2. addAttribute("AbstractDAO", "conn", "Connection", "#")  // protected
3. addOperation("AbstractDAO", "AbstractDAO", "void", "")  // constructor
4. addGeneralization(diagram, "BookDAO", "AbstractDAO")    // mỗi DAO con kế thừa
```

**Màu sắc package (BẮT BUỘC):**
Dùng `addClass` với tham số `packageName` + `packageColor` để tự động đặt class vào package có màu:
```
addClass("Class - BorrowBook", "LoginFrm", "Boundary", "#DDEEFF", "Boundary", false, "", "")
addClass("Class - BorrowBook", "AbstractDAO", "DAO", "#FFE0B2", "DAO", true, "", "")
addClass("Class - BorrowBook", "BookDAO", "DAO", "#FFE0B2", "DAO", false, "AbstractDAO", "")
addClass("Class - BorrowBook", "Book", "Entity", "#FFF3CD", "Entity", false, "", "")
```

**Thứ tự tạo class diagram:**
```
0. listDiagrams("Class") → xác nhận tên diagram chưa tồn tại (unique)
   ⚠️  addAttribute/addOperation tra class theo TOÀN PROJECT — nếu tên class trùng giữa
   các module/diagram sẽ thêm nhầm. Đặt tên class UNIQUE toàn project (vd thêm module
   prefix: "BorrowBook_Reader") hoặc hoàn thành diagram này trước khi tạo diagram khác.
1. createClassDiagram(diagramName)
2. addClass — Boundary classes (mỗi giao diện = 1 class)
3. addClass — Abstract DAO class
4. addClass — DAO classes (kế thừa Abstract DAO)
5. addClass — Entity classes (từ phân tích thực thể — khớp 1:1 với II.2)
6. addAttribute — cho mỗi class (Boundary: UI components; Entity: private fields)
7. addOperation — cho mỗi class (Boundary: actionPerformed; DAO: CRUD methods)
8. addRelationships — theo thứ tự (sau khi thêm ĐỦ classes):
   a. addGeneralization — DAO extends Abstract DAO
   b. addComposition — Entity lifetime-dependent (ReaderCard◆Reader, SlipDetail◆BorrowSlip)
   c. addAggregation — Entity independent (BookTitle◇SlipDetail)
   d. addDependency — Boundary --> DAO
   e. addAssociation — Entity ↔ Entity (structural links)
9. autoLayoutDiagram(diagramName)
10. getDiagramElements(diagramName) → kiểm tra x-positions khác nhau (= đã dàn ngang)
```

**Bảng hướng dẫn chọn relationship:**

| Quan hệ | Ký hiệu | Khi nào dùng |
|---------|---------|---------------|
| Generalization | Tam giác rỗng | DAO kế thừa AbstractDAO; UC con kế thừa UC cha |
| Composition (◆) | Hình thoi đặc | Lifetime dependent — ReaderCard-Reader, SlipDetail-BorrowSlip |
| Aggregation (◇) | Hình thoi rỗng | Independent, shared — BookTitle-SlipDetail |
| Association | Đường liền | General structural link giữa entities |
| Dependency | Đường chấm | Boundary "sử dụng" DAO |

**Ví dụ: Biểu đồ lớp Module Mượn Sách (JFrame)**
```
createClassDiagram("Class - BorrowBook")
// Boundary (package #DDEEFF)
addClass("Class - BorrowBook", "BorrowBookFrm", "Boundary", "#DDEEFF", "Boundary", false, "", "")
addAttribute("BorrowBookFrm", "txtReaderId", "JTextField", "private")
addAttribute("BorrowBookFrm", "btnSearch", "JButton", "private")
addAttribute("BorrowBookFrm", "tblResults", "JTable", "private")
addOperation("BorrowBookFrm", "actionPerformed", "void", "e:ActionEvent")
// Abstract DAO (package #FFE0B2)
addClass("Class - BorrowBook", "AbstractDAO", "DAO", "#FFE0B2", "DAO", true, "", "")
addAttribute("AbstractDAO", "conn", "Connection", "#")
addOperation("AbstractDAO", "AbstractDAO", "void", "")
// DAO (kế thừa AbstractDAO)
addClass("Class - BorrowBook", "ReaderDAO", "DAO", "#FFE0B2", "DAO", false, "AbstractDAO", "")
addClass("Class - BorrowBook", "BorrowSlipDAO", "DAO", "#FFE0B2", "DAO", false, "AbstractDAO", "")
addOperation("ReaderDAO", "findById", "Reader", "id:String")
addOperation("BorrowSlipDAO", "createSlip", "boolean", "slip:BorrowSlip")
// Entity (package #FFF3CD)
addClass("Class - BorrowBook", "Reader", "Entity", "#FFF3CD", "Entity", false, "", "")
addClass("Class - BorrowBook", "ReaderCard", "Entity", "#FFF3CD", "Entity", false, "", "")
addClass("Class - BorrowBook", "BorrowSlip", "Entity", "#FFF3CD", "Entity", false, "", "")
addClass("Class - BorrowBook", "BorrowSlipDetail", "Entity", "#FFF3CD", "Entity", false, "", "")
addClass("Class - BorrowBook", "BookTitle", "Entity", "#FFF3CD", "Entity", false, "", "")
addAttribute("Reader", "id", "String", "private")
addAttribute("Reader", "name", "String", "private")
addAttribute("BorrowSlip", "borrowDate", "Date", "private")
// Relationships
addComposition("Class - BorrowBook", "Reader", "ReaderCard", "1", "1")
addComposition("Class - BorrowBook", "Reader", "BorrowSlip", "1", "n")
addComposition("Class - BorrowBook", "BorrowSlip", "BorrowSlipDetail", "1", "n")
addAggregation("Class - BorrowBook", "BookTitle", "BorrowSlipDetail", "1", "n")
addDependency("Class - BorrowBook", "BorrowBookFrm", "ReaderDAO")
addDependency("Class - BorrowBook", "BorrowBookFrm", "BorrowSlipDAO")
autoLayoutDiagram("Class - BorrowBook")
```

### ERD

**Quy tắc đặt tên ERD (BẮT BUỘC):**

| Quy tắc | Mẫu | Ví dụ |
|---------|-----|-------|
| Tên bảng | `tbl` + TênEntity | `tblSach`, `tblNhanVien` |
| Cột PK | `ma` hoặc `id` | `ma : integer(10) <<PK>>` |
| Cột FK | `tbl` + TênBangCha + `ma` | `tblNhanVienma : integer(10) <<FK>>` |
| Quan hệ FK | Parent `1` to Child `n` | `tblNhanVien \|\|--o{ tblSach` |

**Ánh xạ kiểu dữ liệu:**

| Java Type | SQL Type |
|-----------|----------|
| String | varchar(255) |
| int | integer(10) |
| double | double(10) |
| Date | date |

```
1. createErd(diagramName)
2. addTable(diagramName, tableName)                               — cho mỗi bảng (dùng `tbl` + tên entity)
3. addColumn(tableName, columnName, type, length, scale, PK, nullable)  — cho mỗi cột
4. addForeignKey(diagramName, from, to, fromColumn, toColumn, fkName)   — cho mỗi FK
5. addTableRelationship(diagramName, from, to, type, fromMult, toMult)  — nếu cần
6. autoLayoutDiagram(diagramName)
7. generateDdl(diagramName)                                        — optional, sinh DDL
```

**Ví dụ:**
```
createErd("ERD - ClientManagement")
addTable("ERD - ClientManagement", "tblClient")
addColumn("tblClient", "id", "INT", 10, 0, true, false)
addColumn("tblClient", "name", "VARCHAR", 255, 0, false, false)
addColumn("tblClient", "idCard", "VARCHAR", 20, 0, false, false)
addTable("ERD - ClientManagement", "tblContract")
addColumn("tblContract", "id", "INT", 10, 0, true, false)
addColumn("tblContract", "signDate", "DATE", 0, 0, false, false)
addColumn("tblContract", "tblClientid", "INT", 10, 0, false, false)
addForeignKey("ERD - ClientManagement", "tblContract", "tblClient", "tblClientid", "id", "FK_Client_Contract")
autoLayoutDiagram("ERD - ClientManagement")
generateDdl("ERD - ClientManagement")
```

### Sequence Diagram

**Thứ tự participant (BẮT BUỘC):**
```
Actor → [TênView] (Boundary) → [EntityController] (Control) → [Entity] (Entity)
```

**Alias lifeline (BẮT BUỘC):**
Mỗi lifeline PHẢI có alias ngắn gọn để layout đọc được:

| Vai trò | Mẫu alias | Ví dụ |
|---------|----------|-------|
| Actor | `Actor` | `Actor` |
| Boundary | `B` + index | `B0`, `B1` |
| Control | `C` + index | `C0` |
| Entity | `E` + index | `E1` |

**Lifeline type (BẮT BUỘC):**
Dùng `boundary`, `control`, `entity` khi khai báo lifeline (không dùng `participant`) để hiển thị ký hiệu tròn gạch.

Dùng `addLifeline` với tham số `alias`. Alias xuất hiện làm label của lifeline.

**Lifeline type (BẮT BUỘC):**
Mỗi lifeline PHẢI có type stereotype để VP hiển thị icon đúng:
- `actor` — stick figure
- `boundary` — circle + line
- `control` — arrow
- `entity` — rectangle

Dùng `addLifeline` với tham số `lifelineType`.

**Số thứ tự thông điệp (BẮT BUỘC):**
Tất cả messages PHẢI được đánh số tuần tự:
- Dùng tham số `sequenceNumber` trên `addMessage` và `addReturnMessage`
- Bắt đầu từ `1`, tăng dần cho mỗi message
- Return message dùng số thứ tự tiếp theo (hoặc cùng số với call)
- Combined fragment: message bên trong tiếp tục đánh số

Ví dụ: 1, 2, 3, 4, 5, 6 — nếu dùng opt/loop (luồng chính): sub-message = 5.1, 5.2 (không dùng alt)

**Ngôn ngữ theo pha (khớp cnpm #8):**
- **Arrow label trong VP (addMessage/addReturnMessage):** TOÀN BỘ tiếng Anh trong cả 2 pha (`enter keyword + click Search`, `checkLogin()`, `display results`, `List<Room>`).
- **Phân tích:** Dùng từ khoá: `click btnX` (Actor→Boundary), `call` (Boundary/Control kích hoạt lớp kế), `return` (phản hồi), `display` (Boundary→Actor hiển thị).
- **`methodName()` là SELF-MESSAGE trên Entity (khớp mẫu image_12):** Khi Boundary/Control gọi nghiệp vụ của Entity, vẽ **3 bước**:
  1. Boundary/Control → Entity: `call`
  2. Entity → **chính Entity** (self): `methodName()` — VD `checkLogin()`, `searchActiveRoom()`, `addOrder()`
  3. Entity → Boundary/Control: `return`

  Trong VP MCP: bước 2 gọi `addMessage(diagram, "Entity", "Entity", "methodName()", n, "sync")` (from == to → VP vẽ mũi tên tự gọi).
- **Tương tác Actor↔Actor:** mẫu có `ask X` / `reply X` giữa hai actor (VD Service Staff hỏi Client) — dùng câu tiếng Anh ngắn.
- **Thiết kế:** `methodName()` self-message mang tham số + kiểu (`searchRoomByName(roomName: String): List<Room>`); event Boundary self-call `btnSearchRoomClick()` / `actionPerformed(e: ActionEvent)`.
- **Tên method luôn tiếng Anh** mọi pha (checkLogin, searchProduct, addOrder...).
- **Kịch bản text (v2/v3 bên ngoài biểu đồ):** Giữ tiếng Việt.

**Diễn giải tuần tự (BẮT BUỘC alongside diagram):**

Bên cạnh biểu đồ sequence diagram, PHẢI viết thêm block diễn giải tuần tự dưới dạng danh sách đánh số:
- **Phân tích → Kịch bản phiên bản 2:** Danh sách bước bằng tiếng Việt tự nhiên, mô tả Actor ↔ Boundary ↔ Entity. Xem `cnpm/references/ii.4_tuantu_phantich.md` để biết format chi tiết.
- **Thiết kế → Kịch bản phiên bản 3:** Danh sách bước có tên hàm Java + kiểu dữ liệu, mô tả Actor ↔ Boundary ↔ Control ↔ Entity. Xem `cnpm/references/iii.4_tuantu_thietke.md` để biết format chi tiết.

Block diễn giải giúp người đọc hiểu luồng xử lý mà không cần đọc biểu đồ UML. Luôn đặt ngay sau biểu đồ, trong callout `📖` màu green.

```
0. listDiagrams("Sequence") → xác nhận tên diagram chưa tồn tại (unique)
1. createSequenceDiagram(diagramName)
2. addLifeline — theo thứ tự: Actor, Boundary, [Control], DAO, Entity
3. addActivation — 1 lần cho mỗi lifeline khi nó bắt đầu chuỗi xử lý (không cần mỗi message)
4. addMessage — sync message (thứ tự tăng dần, tiếng Anh). Gọi nghiệp vụ Entity = 3 bước: `call` → `methodName()` self-message (from==to là Entity) → `return`
5. addReturnMessage — return / display (mỗi `call` cần 1 `return`)
6. autoLayoutDiagram(diagramName)
7. getDiagramElements(diagramName) → xác nhận participants đúng thứ tự, message count đúng
```

**Lưu ý Combined Fragment (khớp cnpm #10):**
Biểu đồ sequence **chỉ vẽ luồng chính** — không dùng `alt` để mô tả ngoại lệ. Ngoại lệ → viết block text "Ngoại lệ" sau biểu đồ.
Tool `addCombinedFragment` vẫn sẵn có (operators: `alt`, `opt`, `loop`, `break`, `par`) — chỉ dùng khi user yêu cầu tường minh hoặc cần `loop`/`opt` cho luồng chính.
- `opt` = bước tùy chọn trong luồng chính
- `loop` = lặp lại trong luồng chính

**Ví dụ: Sequence Diagram "Tạo order" (Phân tích)**
```
createSequenceDiagram("SD - TaoOrder_PhanTich")
addLifeline("SD - TaoOrder_PhanTich", "Actor", "NhanVien", "actor", "Actor")
addLifeline("SD - TaoOrder_PhanTich", "LoginView", "LoginView", "boundary", "B0")
addLifeline("SD - TaoOrder_PhanTich", "SearchRoomView", "SearchRoomView", "boundary", "B1")
addLifeline("SD - TaoOrder_PhanTich", "Employee", "Employee", "entity", "E1")
addLifeline("SD - TaoOrder_PhanTich", "Room", "Room", "entity", "E2")
addActivation("SD - TaoOrder_PhanTich", "LoginView")
// --- Đăng nhập: Boundary call Entity → Entity self-method() → return ---
addMessage("SD - TaoOrder_PhanTich", "Actor", "LoginView", "Login", "1", "sync")
addMessage("SD - TaoOrder_PhanTich", "LoginView", "Employee", "call", "2", "sync")
addMessage("SD - TaoOrder_PhanTich", "Employee", "Employee", "checkLogin()", "3", "sync")   // self-message
addReturnMessage("SD - TaoOrder_PhanTich", "Employee", "LoginView", "return", "4")
addMessage("SD - TaoOrder_PhanTich", "LoginView", "SearchRoomView", "call", "5", "sync")
addReturnMessage("SD - TaoOrder_PhanTich", "SearchRoomView", "Actor", "display", "6")
// --- Tìm phòng: cùng mẫu call → searchActiveRoom() self → return → display ---
addMessage("SD - TaoOrder_PhanTich", "Actor", "SearchRoomView", "enter room name and click search", "7", "sync")
addMessage("SD - TaoOrder_PhanTich", "SearchRoomView", "Room", "call", "8", "sync")
addMessage("SD - TaoOrder_PhanTich", "Room", "Room", "searchActiveRoom()", "9", "sync")       // self-message
addReturnMessage("SD - TaoOrder_PhanTich", "Room", "SearchRoomView", "return", "10")
addReturnMessage("SD - TaoOrder_PhanTich", "SearchRoomView", "Actor", "display", "11")
autoLayoutDiagram("SD - TaoOrder_PhanTich")
// Ngoại lệ (text block bên ngoài biểu đồ):
// - searchActiveRoom() trả về rỗng → SearchRoomView hiển thị "No rooms found"
```

---

## Xuất ảnh và nhúng vào tài liệu

### Cách xuất ảnh từ VP

> **⚠️ GIỚI HẠN QUAN TRỌNG:** VP MCP **KHÔNG CÓ tool export ảnh** (đã xác minh từ source code `tools/*.java`). Workflow "vẽ → tự lấy PNG" là **KHÔNG THỂ tự động hoàn toàn**. Khâu xuất ảnh là **thủ công bắt buộc** — đừng kỳ vọng MCP làm thay. `cnpm-vp` vẽ được biểu đồ trong VP; bạn phải mở VP và export tay.

Các cách thay thế:

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

## Kiểm tra cấu trúc sau khi vẽ (Verification)

Sau khi tạo xong diagram, **BẮT BUỘC** chạy verification trước khi export:

### Class Diagram verification
```
1. getDiagramElements(diagramName) → kiểm tra cấu trúc:
   - Có đủ 3 nhóm: Boundary, DAO (thiết kế), Entity classes
   - Phân tích BCE: Mỗi Boundary class có attributes với prefix in_/out_/sub_/outsub_
     (VD: -inKeyword, -outClientList, -subSearch) — KHÔNG dùng txt/btn ở pha phân tích
   - Thiết kế JFrame: attributes = JTextField/JButton/JTable
   - Thiết kế React: attributes = State/JSX (VD: roomList, selectedRoom)
   - Mỗi Entity class có private attributes với kiểu dữ liệu VÀ methods có ()
   - Mỗi DAO class extends AbstractDAO
   - Relationships: >= 1 Generalization (DAO→AbstractDAO), N Dependencies (Boundary→DAO)
2. autoLayoutDiagram(diagramName)
3. getDiagramElements(diagramName) → kiểm tra bố cục x/y:
   - Layout tốt: x positions phân tán theo nhóm
     VD: Boundary x ≈ 100, DAO x ≈ 400, Entity x ≈ 700 — khoảng cách >= 200px mỗi nhóm
   - Layout tốt: y positions đa dạng trong cùng nhóm — khoảng cách >= 100px giữa các class
   - Layout xấu: nhiều class cùng x hoặc y → đang chồng chất → mở VP chỉnh tay
   - MCP không có tool đặt toạ độ trực tiếp — phải chỉnh tay trong VP nếu layout xấu
```

### Sequence Diagram verification
```
1. getDiagramElements(diagramName) → kiểm tra cấu trúc:
   - Lifelines đúng thứ tự: Actor → Boundary → [Control] → DAO → Entity
   - Số lifeline khớp với số participant đã lên kế hoạch
   - Số message = số bước trong kịch bản (v2 hoặc v3)
   - Mỗi sync message có ít nhất 1 return message
   - Arrow labels đúng quy ước:
     · Actor→Boundary: "click btnX" hoặc "input X + click btnY"
     · Boundary/Controller kích hoạt: "call"
     · Entity/DAO method call: "methodName()" (phân tích không tham số; thiết kế có param:Type)
     · Phản hồi: "return"
     · Hiển thị kết quả: "display" hoặc "showMessage(\"msg\")"
   - KHÔNG có combined fragment alt (ngoại lệ → viết text block bên ngoài biểu đồ)
2. autoLayoutDiagram(diagramName)
```

### UC Diagram verification
```
1. getDiagramElements(diagramName) → kiểm tra cấu trúc:
   - Số actor đúng dự kiến (thường 1 actor chính + 1 guest nếu có phân quyền)
   - Số UC đúng dự kiến (= số chức năng trong module, gồm UC con generalization)
   - Có đủ relationship types: Include (<<include>>), Extend (<<extend>>), Generalization
2. autoLayoutDiagram(diagramName)
3. getDiagramElements(diagramName) → kiểm tra bố cục:
   - Actor nằm ngoài cụm UC: x của actor nhỏ hơn x nhỏ nhất của tất cả UC (actor bên trái)
   - UC spread theo chiều dọc (y positions đa dạng, khoảng cách >= 80px) — tránh chồng
   - Nếu có nhiều actor: actor thứ 2 nằm bên phải (x lớn hơn x lớn nhất của UC)
```

### ERD verification
```
1. getDiagramElements(diagramName) → kiểm tra cấu trúc:
   - Số bảng đúng dự kiến (mỗi entity chính = 1 bảng)
   - Mỗi bảng có primary key column (isPrimary=true hoặc PK stereotype)
   - FK columns tồn tại ở bảng phía N của quan hệ 1:N
   - Số relationship đúng dự kiến (mỗi cặp bảng liên quan có 1 relationship)
   - Multiplicities đúng nghiệp vụ: "1..*" / "0..*" / "1" đặt đúng chiều
2. autoLayoutDiagram(diagramName)
3. getDiagramElements(diagramName) → kiểm tra bố cục:
   - Bảng trung tâm (nhiều FK nhất) nằm gần trung tâm sơ đồ
   - Các bảng liên quan spread xung quanh, x và y positions đa dạng
```

### Report verification
```
generateUseCaseReport / generateClassReport / generateSequenceReport / generateErdReport
→ trả về element counts — so sánh với expected counts từ plan:
   UC: actor count, use case count, relationship count
   Class: class count per package, attribute count, method count, relationship count
   Sequence: lifeline count, message count
   ERD: table count, column count, relationship count
```

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
