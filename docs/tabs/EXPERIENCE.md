# EXPERIENCE — Ghi chú cải thiện skill `cnpm`

> File nháp, KHÔNG commit. Dùng để gom kinh nghiệm cho một session khác refine skill `cnpm`.

---

## Điều làm tốt (giữ lại)

- Cấu trúc UP 4 pha + 11 mục rõ ràng, dễ map sang rubric audit.
- Quy ước tách Boundary/Control/Entity + attribute prefix giúp sequence & class diagram nhất quán.
- Test case có CSDL trước/sau (booking, core) → rất dễ kiểm thử & audit (R18).

## Gaps phát hiện trong skill `cnpm`

- **Thiếu glossary entity dùng chung toàn hệ thống.** Cùng một khái niệm "khách hàng" bị đặt 4 tên khác nhau giữa các module: `User` (account), `KhachHang`/`Client` (booking), `Client` (services), `Customer` (core). → Nên thêm vào skill một **bảng entity chuẩn toàn hệ thống** (tên class + tên bảng `tbl*` cố định) để mọi module tham chiếu, tránh phân mảnh.
  - Tương tự: hạng hội viên (`MembershipTier` vs `HangHoiVien`/`MemberRanking`), hóa đơn (`HoaDon` vs `Room_receipt`), nhân viên (`Employee` vs `NhanVien`).
- **Quy ước đặt tên: tiếng Việt vs tiếng Anh chưa nhất quán.** Booking dùng tên Việt (`Phong`, `NhanVien`) ở pha analysis trong khi account/services/core dùng tiếng Anh. Skill nên nêu rõ: class/bảng pha III BẮT BUỘC tiếng Anh thống nhất, tên Việt chỉ ở văn xuôi.
- **Phụ thuộc liên module chưa được tài liệu hóa.** Core gọi `Booking.getBookingHistory()` nhưng module booking không khai báo method này là API liên module. Skill nên có mục "giao diện liên module" khi một module gọi sang module khác.
- **Không có cơ chế chống lệch giữa bản nháp local và Google Docs.** Bản nháp `services/full.md` từng có dấu hiệu lẫn code hệ thống thư viện, trong khi bản Google Docs (export) có tới 42 ảnh — đầy đủ hơn nhiều. Skill/workflow nên coi **export Google Docs là nguồn chuẩn** khi review.

## Ghi chú tích hợp gdocs (cho skill gdocs/cnpm)

- `cli.py tab-read <doc> "<tab>" --output <dir>`: lưu text vào `<dir>/<slug>.md` (slug có dấu tiếng Việt), ảnh vào `<dir>/screenshots/image_NN.png` theo thứ tự đọc tài liệu.
- Tải lại cùng một tab sẽ **ghi đè** `screenshots/image_NN.png` → nếu đọc nhiều tab vào cùng thư mục sẽ trộn ảnh. → Luôn tách `--output` theo module.
- Ảnh `image_NN.png` đánh số theo thứ tự xuất hiện trong tab → có thể map ảnh ↔ pha bằng heading lân cận.

## Chuẩn từ session booking ("DOCS mine 2" = module 2 = Quản lý đặt & trả phòng)

- **Heading 3 cấp chặt:** `N.` → H2, `N.N.` → H3, `N.N.N.` → H4, rồi `a) b) c)`; ý nhỏ hơn → **gạch đầu dòng (bullet)**, KHÔNG đánh số tiếp. (Tham chiếu `exports/heading_structure.json`.)
- **MVC PHẢI KHỚP analysis:** lớp ở pha thiết kế (entity + MVC) phải trùng bộ lớp pha phân tích — không thừa (vd booking từng có lớp `Customer` thừa), không thiếu (account từng THIẾU `Client`, gộp nhầm vào `User`).
- **Tên thuộc tính nhất quán EN xuyên II→III** (fullName/loyaltyPoints/staffRole), không đổi sang tiếng Việt ở pha III.
- "biểu đồ bao nhiêu bước thì scenario v3 bấy nhiêu", cỡ chữ 11, bảng kịch bản 30/70, DOCX để paste tay.

## Bug generator DOCX (đã sửa trong generate_account_docx.py — nên port sang booking + skill)

- **Numbered list dùng chung abstractNumId → Google Docs đánh số nối tiếp.** `startOverride` hoạt động trong Word nhưng Google Docs bỏ qua — nên khi paste vào Docs, danh sách UC02 tiếp tục số từ UC01 thay vì restart về 1. Fix đúng: mỗi `new_numbered_list()` tạo `w:abstractNum` hoàn toàn mới (độc lập), không tham chiếu chung `abstractNumId=2`. Không cần `startOverride` khi đã dùng abstractNum riêng. Xem `new_numbered_list()` trong `generate_account_docx.py`.
- **`determine_heading_level` map cả `N.` lẫn `N.N.` → H2** → loạn cấp. Fix: `N.N.`→3, `N.N.N.`→4, `a)`→4.
- **HTML comment `<!-- File: ... -->` lọt ra body text** (chỉ bắt comment chứa "PLACEHOLDER"). Fix: skip mọi dòng `<!--`.

## Bug `plantuml_renderer.py` (gdocs skill) — ĐÃ SỬA

- Nguyên nhân: `_encode_plantuml` prepend `len(compressed)` thừa ở đầu chuỗi base64 → URL hỏng → server trả ảnh lỗi "bad URL / HUFFMAN encoding". (KHÔNG cần `~1`.)
- **Đã sửa:** bỏ dòng `result = _encode64(len(compressed), 3, ...)`, để `result = ''`. Render lại 10 biểu đồ tuần tự OK qua chính renderer này.
- MCP `mcp__plantuml__generate_plantuml_diagram` vẫn là phương án dự phòng tốt (validate cú pháp).

## Chuẩn biểu đồ tuần tự + ngôn ngữ (chốt với user vòng này)

- **Mỗi mũi tên (kể cả return) = 1 bước đánh số**; kịch bản (v2 phân tích / v3 thiết kế) liệt kê 1:1 với mũi tên. `(N bước)` ở heading + title + bold kịch bản phải khớp số mũi tên.
- **BỎ QUA NGOẠI LỆ** trong biểu đồ tuần tự (không `alt`).
- 4.2: `a) b) c)…` là nhãn in đậm (KHÔNG heading) + gạch đầu dòng cho Input/Output/ứng viên.
- Heading: theo cnpm/canonical — `N.`→H2, `N.N.`→H3, `N.N.N.`→H4; `a)` KHÔNG phải heading.
- Script `scripts/_renumber_seq.py` (đã xoá sau khi dùng) đã tự động renumber + sinh kịch bản — có thể tái tạo nếu cần.
- **Biểu đồ PlantUML: TOÀN BỘ tiếng Anh** — bao gồm `title`, actor display name (`actor "KH" as KH`), arrow labels (`access /login`, `display login form`, `click btnLogin`…), `showMessage(...)` nội dung. KHÔNG có tiếng Việt trong block `@startuml…@enduml`. Khi hiển thị màn hình dùng `display [ScreenName]`, method call giữ tiếng Anh ngắn gọn.
- **Kịch bản phiên bản 2/3 text (ngoài PlantUML): giữ tiếng Việt** theo skill — đây là phần tài liệu hóa bằng ngôn ngữ tự nhiên của UP, không phải code.
- **Scenario text: cả v2 (phân tích) lẫn v3 (thiết kế) đều dùng DANH SÁCH ĐÁNH SỐ (1,2,3…)** — khớp giáo trình UP. (Note cũ "v2→bullet" đã sai, đã sửa trong skill 2026-06-07.)

## Quy ước arrow label & attribute prefix phân tích (confirmed từ ảnh 2026-06-09)

> Context: đọc images 08-12 (biểu đồ lớp phân tích chức năng) và 13-17, 25-29 (sequence diagrams) từ `docs/tabs/screenshots/` — biểu đồ thực từ Google Docs dự án karaoke.

### Arrow label trong sequence diagram

| Tình huống | Label chuẩn | Ví dụ từ ảnh |
|-----------|-------------|-------------|
| Actor → Boundary hành động | short English | `1: click btnManage`, `3: input info + click btnSave` |
| Boundary/Controller kích hoạt | `call` | `2: call`, `4: call` |
| Controller/DAO → Entity method | `methodName()` hoặc `methodName(params)` | `4: list()`, `5: listTiers()`, `6: save(order)` |
| Entity/Controller trả kết quả | `return` | `5: return`, `7: return` |
| Boundary → Actor hiển thị | `display` / `showMessage()` | `7: display`, `showMessage("saved")` |

- Pha phân tích: `methodName()` không tham số
- Pha thiết kế: `methodName(param: Type)` đầy đủ
- Đã cập nhật skill `cnpm` commit `237f8ed` (2026-06-09): principle #8 bổ sung bảng call/return, ii.4 + iii.4 + ii.3 templates.

### Attribute prefix `in_/out_/sub_` trong biểu đồ phân tích chức năng (confirmed)

Images 08-12 dùng **`in_/out_/sub_`** cho pha phân tích (II.3):
- `in_`: ô nhập liệu — `-inKeyword`, `-inFullName`, `-inThreshold`
- `out_`: hiển thị/bảng — `-outClientList`, `-outRoomTypeList`, `-outTierName`
- `sub_`: nút hành động — `-subSearch`, `-subEdit`, `-subSave`, `-subManualUpgrade`
- `outsub_`: bảng có thể click — `-outsubListSession`

**Lưu ý:** `in_/out_/sub_` là pha **phân tích (II.3)**; pha **thiết kế (III.3.2)** dùng `txt/btn/lbl/tbl` (React) hoặc `JTextField/JButton` (JFrame). Hai quy ước KHÔNG lẫn nhau.

Methods trong Entity luôn có `()`: `+list()`, `+create()`, `+update()`, `+delete()`, `+getBookingHistory()`.

## Lưu ý từ dự án UniVerse (universe project, 2026-06-06)

> Context: dùng skill `cnpm` để viết toàn bộ báo cáo TTCS (Nhập môn CNPM — PTIT) cho hệ thống UniVerse (NestJS + Next.js + PostgreSQL + MongoDB + Redis + Kafka). Sau đó sinh DOCX bằng `docx` npm v9.6.1 qua script Node.js.

### Skill `cnpm` — hoạt động tốt

- **BƯỚC 0 PLAN** rất hữu ích: xác nhận scope (all 3 modules, Pha II cho cả 3), xác nhận tech stack (React/HTML thay JFrame), chia việc 3 thành viên rõ ràng.
- Pha II (Phân tích) × 3 module hoàn thành đầy đủ: UC diagram, kịch bản, biểu đồ lớp phân tích chức năng, sequence diagram — nhất quán về tên lớp với codebase thực (đọc entity từ branch `biden` bằng `git show biden:...`).
- **Skill chỉ đăng ký trong project `cnpm-hrm`**, không tự dùng được ở project khác (`universe`). Khi `Skill("cnpm")` ở `universe` → "Unknown skill". Fix: implement thủ công theo SKILL.md.

### Kịch bản (scenario) table có nested HTML table

**Vấn đề:** Bảng kịch bản UC (Markdown table) có cột "Kịch bản chính" chứa các bước đánh số + **bảng dữ liệu mẫu inline** dạng `<table>…</table>` nằm trong cùng một cell của Markdown row. Khi split bằng `|`, cell text thu được bao gồm cả đoạn HTML. `parseInline()` không hiểu HTML → nội dung bảng con bị bỏ qua hoặc lọt ra dưới dạng text thô.

**Fix trong docx generator:**
```javascript
// 1. Tách cell text thành segments text | html_table xen kẽ
function splitCellContent(text) { /* regex /<table[\s\S]*?<\/table>/gi */ }

// 2. Chuyển mỗi segment thành Paragraph[] | nested Table
function makeCellChildren(cellText) {
  // text segment: <br> → '\n', strip tags, parseInline() từng dòng
  // table segment: parse <tr>/<th>/<td> → rows[] → makeTable() (đệ quy)
}

// 3. makeTable dùng makeCellChildren thay vì [new Paragraph({children: parseInline(cell)})]
new TableCell({ children: makeCellChildren(cell.trim()), ... })
```

**Quan trọng:** `makeCellChildren` và `makeTable` gọi nhau đệ quy → PHẢI dùng `function` declaration (hoisted), KHÔNG dùng `const`. `TableCell.children` trong docx v9 chấp nhận cả `Paragraph` lẫn `Table` objects xen kẽ.

### docx npm v9.6.1 — quirks cần nhớ

| Tình huống | Cách làm đúng |
|------------|---------------|
| Ngắt trang | `new Paragraph({ children: [new PageBreak()] })` — KHÔNG dùng `pageBreakBefore: true` (không render trong một số viewer) |
| Header shading | `shading: { type: ShadingType.CLEAR, color: 'auto', fill: 'D9D9D9' }` |
| Nested table trong cell | `TableCell.children = [Paragraph, Table, Paragraph, ...]` — hợp lệ trong v9 |
| Kích thước ảnh PNG | Đọc width/height từ header PNG (offset 16–23, big-endian UInt32) để tính aspect ratio |
| Line spacing 1.5 | `spacing: { line: 360, lineRule: 'auto' }` (240 × 1.5) |
| Millimeter → twip | `convertMillimetersToTwip` export sẵn từ `docx` |

### PlantUML MCP tool trong context

- `mcp__plantuml__generate_plantuml_diagram(plantuml_code, output_path, format)` — ghi thẳng PNG ra disk, trả về `{success, local_path}`.
- Sinh 16 biểu đồ (4 batch × 4 parallel) không lỗi, các biểu đồ sequence phức tạp với `alt` block hoạt động tốt.
- Map diagram → PNG file: duy trì danh sách theo thứ tự xuất hiện trong từng file markdown (`FILE_DIAGRAMS` constant), dùng index counter per-file trong `processFile()`.
- Chú thích "Hình N: [title từ `title` line trong PlantUML]" — extract bằng regex `/^title\s+(.+)/m`.

### Mức trừu tượng theo pha — I.1 & II.1 KHÔNG được lậm kỹ thuật (chốt với user 2026-06-08)

> Context: viết Module 3 (Điểm danh QR+GPS & Học vụ) cho UniVerse. User phản hồi gay gắt: "i.1 và ii.1 UC & scenario quá chi tiết... không có các thứ như redis, token, cập nhật cụ thể cái gì, TẬP TRUNG ACTOR HÀNH ĐỘNG VÀ HỆ THỐNG PHẢN HỒI".

- **Pha I (I.1) và Pha II.1 (kịch bản chức năng) chỉ mô tả "Actor hành động → Hệ thống phản hồi/hiển thị".** TUYỆT ĐỐI không nhắc chi tiết triển khai: Redis, JWT/QR token, HMAC-SHA256, Kafka event, công thức Haversine, TTL, tên field/cột (`status = absent`, `isPublished = true`), trọng số tính toán.
  - ❌ SAI (II.1): "GV nhấn Tạo QR → hệ thống sinh token HMAC-SHA256, lưu Redis TTL 5s, cập nhật trạng thái buổi 'đang diễn ra', hiển thị QR động".
  - ✅ ĐÚNG: "GV nhấn Tạo mã QR → hệ thống hiển thị mã QR điểm danh cho buổi học".
  - ❌ SAI: "hệ thống đánh dấu isPublished = true → phát event grade.published lên Kafka → NotificationModule gửi thông báo".
  - ✅ ĐÚNG: "hệ thống công bố điểm và gửi thông báo đến sinh viên".
- **Chi tiết kỹ thuật chỉ được phép xuất hiện lại TỪ Pha III**: III.1 (kiểu dữ liệu, enum), III.2 (DDL, tên cột, kiểu SQL), III.4 (tên hàm + tham số + kiểu). Đúng tinh thần UP: **phân tích = WHAT, thiết kế = HOW**.
- **UC con ở I.1 cũng phải là bước NGHIỆP VỤ, không phải bước kỹ thuật.** Bỏ sub-UC kiểu "Ký HMAC-SHA256 + lưu Redis", "Lưu Redis TTL 5s", "Xác minh chữ ký QR". Thay bằng functional thuần: "Tự động ghi vắng cho SV chưa điểm danh", "Tính điểm tổng kết", "Công bố điểm".
- **II.4 (tuần tự phân tích) kế thừa cùng mức**: thông điệp/tên hàm trừu tượng (`createQr`, `stopQr`, `updateStatus`, `saveGrades`, `publishGrades`) — KHÔNG "lưu Redis", "ký HMAC", "tính Haversine" trong message.
- **Đề xuất sửa skill:** thêm callout cảnh báo vào `i.1_mohinh_nghiepvu.md` và `ii.1_mohinh_hoa_chucnang.md`: *"Kịch bản & UC KHÔNG chứa từ khóa hạ tầng/công nghệ (Redis, token, HMAC, Kafka, TTL, tên cột DB, công thức). Nếu xuất hiện → sai pha, đẩy nội dung đó xuống Pha III."* Có thể kèm bảng ❌SAI/✅ĐÚNG như trên.

### Biểu đồ phân tích chức năng — tách riêng từng UC (chốt với user 2026-06-09)

> Context: Module 3 UniVerse ban đầu dùng 1 biểu đồ phân tích chức năng tổng hợp cho cả 4 UC. User yêu cầu "làm riêng & vẽ biểu đồ riêng từng UC".

- **Mỗi UC phải có 1 biểu đồ phân tích chức năng riêng** — không gộp nhiều UC vào chung 1 diagram.
  - ❌ SAI: 1 diagram chứa tất cả Boundary + Entity cho 4 UC08/09/10/11.
  - ✅ ĐÚNG: 4 diagram riêng biệt (UC08 diagram, UC09 diagram, UC10 diagram, UC11 diagram), mỗi cái chỉ vẽ Boundary và Entity liên quan đến UC đó.
- **Narrative II.3 dùng bullet points**, không phải code block. Format: in đậm tiêu đề "Phân tích chi tiết chức năng [Tên UC]:" rồi dùng `- bullet` để mô tả từng bước.
  - ❌ SAI: đặt narrative trong ``` ``` (code block).
  - ✅ ĐÚNG: `**Phân tích chi tiết...**` + danh sách `- GV vào giao diện → đề xuất lớp X...`

### Biểu đồ tuần tự — happy path only, không có ngoại lệ (chốt với user 2026-06-09)

> Context: user yêu cầu "biểu đồ tuần tự KHÔNG ĐƯỢC CÓ NGOẠI LỆ" cho cả II.4 và III.4.

- **Biểu đồ tuần tự II.4 và III.4 CHỈ vẽ happy path** — không có `alt`/`else`/`end` block.
  - ❌ SAI: dùng `alt Buổi đã có QR đang hoạt động … else … end`.
  - ✅ ĐÚNG: chỉ vẽ luồng thành công, bỏ hết ngoại lệ.
- Ngoại lệ chỉ xuất hiện ở dạng **văn bản** trong bảng kịch bản II.1 (cột "Ngoại lệ") — không đưa vào diagram.
- **Bỏ luôn phần "Ngoại lệ" text** sau kịch bản phiên bản 2/3 trong II.4/III.4 — chỉ giữ narrative happy path.

### Thực thể Attendance — link ClassSession, không phải Schedule (chốt với user 2026-06-09)

> Context: docx section 3.2.4 xác nhận `ClassSession` (buổi học cụ thể theo ngày) là trung gian giữa `Schedule` (lịch học trong tuần) và `Attendance`.

- **Phân cấp thực thể đúng:** `ClassSection (=Class)` 1→n `Schedule` (lịch học trong tuần) 1→n `ClassSession` (buổi học cụ thể) 1-1 `QRCode`.
- `Attendance` FK phải là `classSessionId → tblClassSession`, KHÔNG phải `scheduleId → tblSchedule`.
  - ❌ SAI (II.2, III.1, III.2): `Attendance.scheduleId`, `Schedule "1" -- "n" Attendance`.
  - ✅ ĐÚNG: `Attendance.classSessionId`, `ClassSession "1" -- "n" Attendance`.
- `QRCode` là entity riêng (1-1 với ClassSession) — không phải thuộc tính của Attendance.
- Khi vẽ entity diagram II.2 phải hiện đủ: `Schedule → ClassSession → QRCode`, `ClassSession → Attendance ← User`.

## Chuẩn MVC class diagram – thiết kế (React MVC)

- **Boundary PHẢI có biến/list lưu entity nếu hiển thị hoặc thao tác với entity đó:**
  - `RegisterPage` → `- registeringUser: User`
  - `OTPVerifyPage` → `- user: User`, `- currentOTP: OTP`
  - `ProfilePage` / `ChangePasswordPage` → `- currentUser: User`
  - `EmployeeManagement` → `- staffList: List<Employee>`, `- selectedEmployee: Employee`
  - `LoginPage` không cần (chỉ gửi form input, không lưu/hiển thị entity nào)

- **Quan hệ trong class diagram thiết kế:**
  - Boundary — Control: `--` (**association thuần**, đường thẳng **KHÔNG mũi tên**)
  - Control — Entity: `--` (**association thuần**, đường thẳng **KHÔNG mũi tên**)
  - Entity — Entity (owned): `*--` (composition), `o--` (aggregation)
  - Entity — Entity (reference): `--` với multiplicity, ví dụ `Client "*" -- "1" MembershipTier`
  - KHÔNG dùng `-->` (directed association, có mũi tên) cho Boundary–Control hay Control–Entity
  - KHÔNG dùng `..>` (dependency, đường đứt) trong pha III class diagram

- **Tên thuộc tính Boundary theo pha:**
  - Pha **Phân tích**: dùng tiền tố `txt`, `btn`, `lbl`, `tbl`, `lnk` (VD: `txtPhoneNumber`, `btnLogin`, `tblStaffList`)
  - Pha **Thiết kế**: dùng **camelCase thuần**, KHÔNG tiền tố `in_`/`out_`/`sub_` (VD: `phoneNumber: String`, `staffList: List<Employee>`)
  - Attribute entity (biến lưu đối tượng) giữ camelCase: `currentUser: User`, `selectedEmployee: Employee`

- **KHÔNG dùng DTO trong class diagram thiết kế.** Method signature dùng trực tiếp entity type: `saveStaff(employee: Employee): Employee`, không phải `saveStaff(dto: EmployeeDTO): Employee`.

- **Attributes Entity PHẢI khớp codebase** – không được lược bỏ tùy tiện:
  - `User`: `id`, `username`, `phoneNumber`, `email`, `passwordHash`, `fullName`, `role`, `active`, `createdAt`, `failedAttempts`, `lockUntil`
  - `Employee`: `id`, `fullName`, `dob`, `tel`, `email`, `staffRole`, `status`, `active`, `username`, `password`, `branch`
  - `LoginSession`: `id`, `sessionToken`, `loginTime`, `expiresAt`, `device`, `trangThai`, `user: User`

- **Controller methods phải khớp codebase endpoints** – thêm `searchStaff`, `getProfile` nếu có trong code; không bịa thêm method không có.

## Audit skill `cnpm-vp` (2026-06-07, source code verified)

### Lỗi chữ ký tool VP MCP — ĐÃ SỬA trong commit `4cf6b9c`

- **`addRelationship` thiếu `diagramName`** — skill cũ dạy 3 params, thực ra 4 params (`diagramName, source, target, type`). Gọi sai → UC relationship không vẽ được.
- **`addAssociation`**: `fromMult, toMult, name` (6 params, không phải 5).
- **`addAggregation`/`addComposition`**: `fromMult, toMult` riêng (5 params, không phải 4).
- **`addForeignKey`**: `fromColumn, toColumn` riêng (6 params).
- **`addTableRelationship`**: `fromMult, toMult` riêng (6 params).
- **Tool count**: 38 (không phải 39); thiếu `getElementCounts` trong bảng.

### Giới hạn VP MCP — không có tool export ảnh

VP MCP **KHÔNG CÓ tool export ảnh** (xác nhận từ source). Workflow tự động "vẽ → lấy PNG" không thể hoàn toàn. Phải mở VP Export as Image tay.

### Khoảng trống khi vẽ trong VP — ĐÃ GHI CHÚ trong skill

- **Không có tool đặt toạ độ**: chỉ `autoLayoutDiagram`. Layout xấu → mở VP sửa tay.
- **`addAttribute`/`addOperation` tra class TOÀN PROJECT**: nếu tên class trùng giữa module → thêm nhầm. Đặt tên class unique hoặc làm từng diagram một.
- Workflow: gọi `listDiagrams` TRƯỚC `createXxx` để confirm tên unique.

### Đồng bộ cnpm-vp theo cnpm (sau sửa cnpm)

- Arrow label VP: tiếng Anh (khớp cnpm #8)
- JFrame naming: `[EnglishName]Frm` (không `GD...Frm`)
- Class/Entity/DAO/Table: tiếng Anh PascalCase
- Không dùng `alt` cho ngoại lệ trong sequence (khớp cnpm #10)
- Attribute prefix: `txt/btn/tbl/lbl` (khớp iii.3.2)

## Deep audit VP MCP vs biểu đồ mẫu (2026-06-10) — "vẽ như mẫu"

Đối chiếu plugin `visual-paradigm-mcp-plugin` với biểu đồ mẫu chuẩn của môn học
(`exports/services/screenshots`, `exports/account/screenshots`). Style đích trích từ ảnh:

| Loại | Phát hiện từ mẫu (gold standard) |
|------|----------------------------------|
| Class (phân tích chức năng/entity/MVC) — image_07,08,16,36 | **Hộp TRẮNG trơn — KHÔNG màu package, KHÔNG stereotype `<<...>>`**. Tách bằng tên hậu tố + bố cục, KHÔNG dùng package màu. |
| Boundary attr (phân tích) — image_08 | camelCase tiếng Anh, KHÔNG underscore, KHÔNG kiểu: `inUsername`, `subLogin`, `outsubRoomList`, `outRoomName`. Boundary chỉ có attr, không method. |
| Boundary attr (thiết kế) — image_36 | `txt/btn/lbl/tbl` + kiểu: `-txtUsername : TextBox`, `-btnLogin : Button`, `-tblActiveRooms : Table`. Có method + constructor. |
| UC tổng quan — image_02 | **Khung hệ thống** (rectangle) bao UC, nhãn = tên module; actor ngoài hai bên; actor xanh `#7AD2FF`. |
| Sequence — image_12 | Lifeline + activation bar **xanh `#7AD2FF`**. method() là **SELF-message trên Entity**: Boundary `-> Entity : call` → Entity `-> Entity : checkLogin()` → Entity `--> Boundary : return`. Actor↔Actor có `ask/reply`. |

### Mâu thuẫn skill cũ vs mẫu (đã sửa)
- cnpm-vp #2/#3 BẮT BUỘC package màu + stereotype → **mẫu KHÔNG có**. Đã đổi: hộp trắng mặc định, màu/stereotype optional.
- cnpm-vp bảng prefix phân tích dùng `in_ten` (underscore + tiếng Việt) → đổi camelCase EN `inUsername`.
- ii.4/iii.4/cnpm#8 đặt `methodName()` ngay trên mũi tên Boundary→Entity → đổi sang 3 bước self-message.

### Plugin đã sửa (repo `visual-paradigm-mcp-plugin`, commit `8108bc6`)
- `applyConventionalFill`: tự tô xanh `#7AD2FF` cho actor/use case/lifeline/activation; class + table giữ trắng.
- **Tool mới `addSystemBoundary(diagramName, systemName)`**: tạo `ISystem`, gom mọi use case vào, bao rectangle quanh bounding-box + padding, `sendToBack()`. Gọi SAU `autoLayoutDiagram`. Tool count 38 → **39**.
- Build SUCCESS (Java 11, 0 checkstyle violations). **Chưa verify runtime** — cần `./run install` + restart VP để plugin mới nạp vào VP (server đang chạy vẫn là plugin cũ).

### Skill đã đồng bộ (branch `main`, commit `04dae27`)
cnpm-vp + cnpm/SKILL #8 + ii.3 + ii.4 + iii.4 khớp style mẫu (hộp trắng, prefix camelCase EN, self-message, addSystemBoundary, tool count 39).

### LỖI GỐC biểu đồ tuần tự — alias làm mất hết mũi tên (test trực tiếp live MCP 2026-06-10)

**Triệu chứng:** biểu đồ tuần tự vẽ ra chỉ có lifeline, KHÔNG có mũi tên.

**Nguyên nhân:** skill cũ bắt mỗi lifeline có `alias` `B0`/`E1`. `addLifeline` set nickname=alias → VP `getName()` trả về **alias**, nhưng `addMessage` tham chiếu bằng `lifelineName` (`LoginView`) → `findLifelineByName` chỉ khớp `getName()` → **"lifeline not found" → 0 message**. Probe xác nhận: ref bằng `lifelineName` → 0 msg; ref bằng alias `B0` → OK.

**Đã sửa cả hai:**
1. **Skill (dùng NGAY, không restart VP)** — commit `main`: bỏ alias (`alias=""`), tham chiếu lifeline bằng `lifelineName`. Bonus: nhãn lifeline = tên class đúng mẫu (hết `B0`). Probe: full login+search 16 mũi tên (image_12) dựng OK gồm self-message + actor↔actor.
2. **Plugin (robustness, deploy khi restart VP)** — commit plugin `25e312d`: `findLifelineByName` khớp thêm caption (custom text = lifelineName) + classifier name.

**Lỗi phụ — nhãn classifier "ClassN" khi trùng tên:** VP từ chối `setName` class trùng tên → lifeline entity tái dùng nhiều SD lấy nhãn `Class8`. SD đơn lẻ tên unique thì OK. Chưa sửa.

**Verify trực tiếp live MCP:** raw HTTP JSON-RPC `localhost:2026` (GET `/sse` lấy session path → POST `{session}` `tools/call`), file `/tmp/vp_probe*.py`. Server đang chạy = plugin CŨ; bản vá cần `./run install` + restart VP.

### Class diagram — đã verify path (live MCP)
`addClass` không truyền package/stereotype → hộp trắng. `addAttribute` prefix camelCase + visibility `private` (render `-`). `addOperation` → `()`. `addAssociation`. autoLayout dàn ngang (~480px). Đúng cấu trúc image_08; còn lại kiểm tra mắt trong VP.

## Vấn đề hạ tầng (không thuộc nội dung skill)

- **`main` branch: `.claude/skills/cnpm/references/iii.4_tuantu_thietke.md` còn dấu xung đột** (đã giải quyết trong commit `14df9fc` ngày 2026-06-06).

## Phát hiện từ rubric audit (chạy 2026-06-02, commit 24245b4)

- **Bản nháp local lệch nặng so với Google Docs.** Giả định services pha III lẫn code thư viện + pha IV trống là từ bản nháp local — bản Google Docs SẠCH, có 8 TC thật + tên bảng `tbl*`. → Audit PHẢI dựa trên export, không bản nháp. (Đã ghi vào skill audit.)
- **Text export không nhúng ảnh inline.** Các mục dựa trên ảnh (UC diagram, biểu đồ phân tích chức năng, sequence, ERD, MVC) đọc text thấy "placeholder rỗng" nhưng ảnh có thật trong `screenshots/`. → Skill audit phải chấm mục ảnh theo SỐ LƯỢNG ẢNH + heading, không theo text. services có 42 ảnh nhưng text sơ sài → cần mắt người xác minh.
- **Lỗi hệ thống pha I: R01 + R03 ✗ ở CẢ 4 module.** Không module nào có bảng UC chính thức (ID/tên/actor/mô tả) hay bảng Include/Extend — chỉ có heading + narrative. → `cnpm` nên BẮT BUỘC sinh 2 bảng này ở pha I.
- **R07 (kịch bản ngoại lệ) thiếu gần như toàn bộ** — chỉ ghi inline trong sequence. → `cnpm` nên tách kịch bản ngoại lệ thành mục riêng.
- **R11 (thiết kế lớp thực thể 4 bước) hiếm khi tường minh** trừ khi có template rõ.
- **Tên entity khách hàng phân mảnh 3 cách:** `User` (account) / `Client` (booking, services) / `Customer` (core). Cần bảng entity chuẩn toàn hệ thống.
- **Đính chính cross-module:** receipt (`Room_receipt`) và nhân viên (`Employee`) thực ra NHẤT QUÁN ở cấp class/bảng — tên Việt (`HoaDon`/`NhanVien`/`Phong`) chỉ ở văn xuôi phân tích. Vấn đề thật chỉ còn: khách hàng (X01), hạng hội viên (X02: `MembershipTier` vs `MemberRanking`), gọi liên module (X06).

### Mức chi tiết narrative II.3 biểu đồ phân tích chức năng — bắt đầu từ HomeView + lý do method (chốt với user 2026-06-09)

> Context: Module 3 UniVerse, sau khi tách riêng từng UC, user yêu cầu narrative phải chi tiết như ví dụ: bắt đầu từ giao diện chính (HomeView), liệt kê đầy đủ attributes theo `in/out/sub`, và giải thích TẠI SAO method thuộc entity nào (entity đó sở hữu thuộc tính gì).

- **Narrative II.3 PHẢI bắt đầu từ giao diện Home của actor** — không nhảy thẳng vào giao diện chức năng.
  - ❌ SAI: "GV vào giao diện → đề xuất lớp `QRSessionView`..."
  - ✅ ĐÚNG: "Sau khi đăng nhập, hệ thống hiển thị giao diện chính → đề xuất lớp `LecturerHomeView`, có ít nhất nút `-subAttendance`. GV click → giao diện `QRSessionView` hiện lên..."
  - Mỗi UC cần xác định HomeView tương ứng: GV → `LecturerHomeView`, SV → `StudentHomeView`. HomeView phải có ít nhất 1 nút điều hướng vào UC đang phân tích.

- **Liệt kê ĐẦY ĐỦ attributes của View** — không chỉ những attribute "chính". Mỗi element giao diện = 1 attribute với đúng tiền tố:
  - `in`: ô nhập liệu (text input, dropdown filter)
  - `out`: chỉ hiển thị (bảng, nhãn không tương tác)
  - `sub`: nút hành động (Submit, Save, Search)
  - `outsub`: hiển thị + có thể click/chọn (clickable table/list)
  - `inout`: bảng vừa hiển thị vừa cho phép sửa inline
  - ❌ THIẾU (UC08 cũ): bỏ `-subSearch`, `-outsubListSession`, `-outQRCode`.
  - ✅ ĐỦ (UC08 mới): `-inClassSection`, `-subSearch`, `-outsubListClass`, `-outsubListSession`, `-outQRCode`, `-subGenerateQr`, `-subDeactivateQr`, `-outAttendanceList`.

- **Lý do chọn entity phải nêu thuộc tính entity đó sở hữu.** Format chuẩn:
  ```
  → cần chức năng `generateQr()` → chức năng này là hành động của đối tượng thực thể `Attendance`
  (lớp này sở hữu các thuộc tính `-classSessionId`, `-studentId`, `-status`, `-method`)
  ```
  - Không được viết "gọi `generateQr()` của lớp `Attendance`" mà không giải thích tại sao Attendance là đúng.

- **PlantUML entity class trong biểu đồ phân tích chức năng phải có cả attributes lẫn methods:**
  ```
  class Attendance {
    -classSessionId
    -studentId
    -status
    -method
    +generateQr()
    +deactivateQr()
  }
  ```
  - ❌ SAI: entity class chỉ có methods, không có attributes.

- **Pattern kết thúc flow:** sau create/update, thêm bước "hệ thống thông báo thành công, đồng thời tải lại [outXxx] thông qua hàm `getListXxx()`/`viewXxx()` và quay về [ViewName]".

- **Diagram phải vẽ LecturerHomeView/StudentHomeView** → đường mũi tên từ HomeView vào View chức năng:
  ```
  LecturerHomeView --> QRSessionView
  QRSessionView --> Attendance
  QRSessionView --> Class
  ```

### Quy trình 4 bước phân tích chức năng (nguyên văn từ giảng viên, chốt 2026-06-09)

- **Bước 1:** Một giao diện người dùng -- ngoại trừ cảnh báo/thông báo, hộp thoại xác nhận... -- tạo một lớp giao diện.
- **Bước 2:** Xem xét các thành phần cần thiết trong mỗi giao diện, đặt tên thành phần với tiền tố tương ứng loại của nó:
  - `in`: cho các thành phần nhập liệu -- ô nhập văn bản, ô nhập ngày tháng...
  - `out`: cho các thành phần hiển thị -- bảng, nội dung...
  - `sub`: cho các thành phần gửi dữ liệu -- nút bấm, liên kết...
  - và có thể kết hợp các loại trên.
- **Bước 3:** Xem xét xem chúng ta có cần thực hiện hành động/chức năng nào dưới lớp giao diện không. Với mỗi chức năng cần thiết, trả lời bốn câu hỏi:
  - Tên phù hợp của phương thức là gì -- có thể đặt tên theo quy ước mã nguồn
  - Các tham số đầu vào là gì?
  - Tham số đầu ra là gì?
  - Phương thức nên được gán vào lớp nào? Xem xét nguyên tắc sau:
    - Nếu tham số đầu ra là một loại lớp thực thể, thì phương thức được gán cho lớp thực thể đó.
    - Nếu không phải, xem xét các tham số đầu vào. Nếu chúng chỉ bao gồm một lớp thực thể, thì gán phương thức cho lớp thực thể đó. Nếu chúng bao gồm nhiều loại lớp thực thể, thì xem trong số đó lớp thực thể nào có thể chứa tất cả các tham số đầu vào để gán phương thức.
- **Bước 4:** Xây dựng sơ đồ lớp cho mô-đun.

## MVC JFrame+DAO class diagram trong VP — bài học từ universe Module 3 (2026-06-10)

> Context: vẽ 4 biểu đồ lớp thiết kế MVC (UC08–UC11, JFrame + DAO pattern) cho báo cáo UniVerse bằng VP MCP. Mất 2 session do lỗi naming VP.

### Vấn đề cốt lõi: VP MCP + tên class trùng → ClassXXX

- **Khi `addClass("TênClass", diagram)` mà "TênClass" đã tồn tại trong project VP** (dù ở diagram khác), VP tạo instance mới với tên tự sinh (`Class184`, `Class185`...) thay vì reuse model cũ. Kết quả: class hiển thị sai tên trong VP GUI.
  - ❌ SAI: addClass("LecturerHomeFrm") trong 4 diagram khác nhau → diagram 2/3/4 được "Class185", "Class190"...
  - ✅ ĐÚNG: đặt tên unique cho từng class: `LecturerHomeFrm` (UC08), `LecturerHomeFrm2` (UC09), `LecturerHomeFrm3` (UC11).

- **Class bị ClassXXX KHÔNG thể rename qua VP MCP** — không có rename tool. Phải đổi tên tay trong VP GUI (double-click header class).

- **getDiagramElements trả ClassXXX = tên MODEL thực sự** trong VP. Nếu thấy "Class: Class190 at..." → VP GUI cũng hiển thị "Class 190", không phải tên đúng.

### Quy tắc đặt tên tránh ClassXXX

- **Mỗi class phải có tên unique xuyên toàn project VP.** Nếu cùng tên cần xuất hiện nhiều diagram: thêm số (`2`, `3`...) cho lần xuất hiện sau.
  - Entity shared: `ClassSection` (UC08), `ClassSection2` (UC11); `Attendance` (UC08), `Attendance2` (UC09); `CourseRecord` (UC10), `CourseRecord2` (UC11).
  - Frm shared: `LecturerHomeFrm` (UC08), `LecturerHomeFrm2` (UC09), `LecturerHomeFrm3` (UC11).
  - DAO abstract: thêm vào từng diagram TUẦN TỰ (không song song) — VP reuse đúng model nếu thêm lần lượt.

- **DAO abstract dùng chung:** thêm vào UC08 trước (tạo model), rồi `addClass("DAO", diagramUC09)`, `addClass("DAO", diagramUC10)`... từng cái một. Nếu thêm song song → VP tạo duplicate `Class`/`Class2`/`Class3` thay vì reuse.

- **Interface cũng bị lỗi tương tự:** `addInterface("ActionListener", diagram)` lần 2/3/4 → `Class4`, `Class5`, `Class6`. Phải rename tay trong VP GUI.

### autoLayoutDiagram tạo lại package containers

- Gọi `autoLayoutDiagram` sau khi đã `removeDiagramElement` package → VP **tạo lại** các `crg: Boundary/Control/Entity` dựa trên `packageName` của classes.
- **Không gọi autoLayoutDiagram sau lần xoá package cuối cùng.** Nếu đã layout xong và xoá package sau → dừng lại, không layout lại.
- `boi: null` elements (VP internal grouping boxes) không remove được qua MCP (elementName "null" → not found). Bỏ qua; không hiển thị rõ trong VP GUI.

### Dependency arrows không xuất hiện trong getDiagramElements

- `addDependency` trả "Added dependency..." nhưng getDiagramElements KHÔNG liệt kê connector Dependency trong output. Chỉ hiện Association + Generalization.
- Không thể verify dependency qua MCP — phải mở VP GUI kiểm tra mắt.

### Workflow đúng cho 4 diagram MVC JFrame+DAO

1. **Dùng project VP sạch** (mới hoàn toàn) — tránh mọi orphaned class từ session cũ.
2. `createClassDiagram` cho tất cả diagrams.
3. Thêm DAO abstract vào diagram UC đầu tiên, sau đó thêm vào các diagram còn lại **TUẦN TỰ** (1 lệnh, chờ kết quả, rồi gọi tiếp).
4. Dùng tên unique (suffix số) cho tất cả class shared giữa các diagram.
5. Hoàn tất TỪNG diagram 100% (addClass → addAttribute → addOperation → addGeneralization → addAssociation) trước khi sang diagram tiếp. Lý do: `addAttribute/addOperation` match **tên class đầu tiên trong toàn project** — nếu diagram 2 có "LecturerHomeFrm2" và diagram 3 cũng có "LecturerHomeFrm3", không có conflict; nhưng nếu dùng lại tên giống thì nhầm.
6. Xoá packages sau khi layout, KHÔNG gọi autoLayoutDiagram thêm lần nào sau đó.
7. Khi cần rename ClassXXX → đúng tên: user làm tay trong VP GUI (double-click header).

### addAttribute/addOperation "first match" — ví dụ thực tế

| Lệnh MCP | Class thực sự nhận attr/op |
|----------|---------------------------|
| `addAttribute("DAO", ...)` | DAO trong diagram đầu tiên tạo nó |
| `addAttribute("Class", ...)` | Class VP-internal đầu tiên có model name "Class" trong project |
| `addAttribute("LecturerHomeFrm2", ...)` | Chỉ có 1 class tên này → đúng |
| `addOperation("ActionListener", ...)` | ActionListener trong UC08 (diagram đầu tiên có tên này) |

→ Chọn tên unique → không bao giờ nhầm. Đây là quy tắc quan trọng nhất khi dùng VP MCP cho multi-diagram project.

---

## Phân loại & kinh nghiệm vẽ biểu đồ lớp — từ ảnh mẫu `exports/services/screenshots`

> Context: phân tích 43 ảnh exports/services, đối chiếu với 5 file tham khảo `software-engineering-basics/references/`. Trích xuất 6 loại biểu đồ, mỗi loại có pattern VP chuẩn để tái tạo.

### Phân loại 6 loại biểu đồ lớp (từ ảnh mẫu)

| # | Tên chuẩn (trong tài liệu) | Tên gốc trước đây | Ảnh mẫu | Pha UP |
|---|----------------------------|--------------------|---------| -------|
| 1 | **Biểu đồ lớp phân tích chức năng** | BCE Analysis | 08–12 | II.3 |
| 2 | **Biểu đồ lớp thực thể phân tích** | Entity Analysis | 07 | II.2 |
| 3 | **Biểu đồ lớp thực thể thiết kế** | Design Entity | 17 | III.2 |
| 4 | **Biểu đồ lớp thiết kế MVC** | MVC Design | tham khảo `design_class_diagram.md` | III.3.2 |
| 5 | **ERD** (sơ đồ thực thể-tiêu đề) | — | 18 | III.1 |
| 6 | **UI Wireframe** (giao diện) | — | 19–30 | IV.1 |

---

### Kinh nghiệm loại 1: Biểu đồ lớp phân tích chức năng (II.3)

> Ảnh mẫu: image_08 (Manage order), image_10 (Report damage), image_11 (Manage menu), image_12 (Manage warehouse)
> Tên cũ: "BCE Analysis" — giờ gọi là **biểu đồ lớp phân tích chức năng**.

#### Layout chuẩn — bố cục 2 hàng ngang

```
HÀNG TRÊN (View classes — lớp giao diện):
  LoginView — StaffHomeView/ManagerHomeView — SearchRoomView — FunctionView — ConfirmView

HÀNG DƯỚI (Entity classes — lớp thực thể):
  Employee — Room — Product — Order — ...
```

- View classes **dàn ngang trên**, Entity classes **dàn ngang dưới**
- View → Entity: association plain `--` (KHÔNG mũi tên `-->`)
- Mỗi UC tách riêng 1 diagram, KHÔNG gộp nhiều UC
- **KHÔNG có package box 3 màu** — tất cả hộp trắng, bố cục tự do

#### Chi tiết bố cục từ ảnh thực

- **LoginView luôn ở góc trên-trái** — điểm bắt đầu flow
- **StaffHomeView/ManagerHomeView** nằm ngay bên phải LoginView — là trung chuyển
- **FunctionViews** (SearchRoomView, CreateOrderView, etc.) dàn tiếp sang phải
- **ConfirmView** (ConfirmOrderView, ConfirmReportView) ở góc trên-phải — bước cuối
- **Entity classes** dàn ngang bên dưới, Entity nào có quan hệ mạnh thì đặt gần nhau
- **Entity methods** (`+methodName()`) nằm ở cuối class box
- **LoginView KHÔNG có method** — chỉ có attrs `in_/sub_`
- **HomeView KHÔNG có method** — chỉ có 1–2 attrs `sub_`

#### Quy tắc đặt tên & attributes

| Thành phần | Quy tắc | Ví dụ từ ảnh |
|-----------|---------|--------------|
| View class name | `XxxView` (PascalCase) | `LoginView`, `SearchRoomView`, `DamageReportView` |
| Attr `in_` | ô nhập liệu | `-inUsername`, `-inPassword`, `-inProductName`, `-inProviderName` |
| Attr `out_` | chỉ hiển thị (label, text) | `-outRoomName`, `-outSuccess`, `-outProviderName` |
| Attr `sub_` | nút hành động | `-subLogin`, `-subSearch`, `-subSave`, `-subAdd` |
| Attr `outsub_` | bảng có thể click/chọn | `-outsubRoomList`, `-outsubListRoom` |
| Attr `inout_` | hiển thị + cho sửa inline | `-inoutName`, `-inoutCategory` |
| Entity method | `+methodName()` có `()` | `+checkLogin()`, `+searchActiveRoom()`, `+addOrder()` |

#### Entity class trong biểu đồ phân tích chức năng

- Entity class **PHẢI có cả attribute lẫn method** (khác biểu đồ thực thể thiết kế chỉ có attr)
- Entity KHÔNG có `in_/out_/sub_` prefix — dùng tên thuần
- Attribute Entity: `-attributeName` (KHÔNG typed, KHÔNG `: type`)
- **Cùng 1 entity có thể xuất hiện trong nhiều diagram phân tích** (VD: `Employee` xuất hiện trong cả 4 UC) → khi dùng VP MCP cần suffix số tránh trùng tên

#### Flow narrative cho II.3

1. Bắt đầu từ **HomeView** của actor (VD: `StaffHomeView`, `ManagerHomeView`)
2. HomeView có ít nhất 1 nút `sub_` điều hướng vào View chức năng
3. Liệt kê ĐẦY ĐỦ attributes của mỗi View theo `in/out/sub/outsub/inout`
4. Giải thích method thuộc entity nào + lý do (entity sở hữu attribute gì)

---

### Kinh nghiệm loại 2: Biểu đồ lớp thực thể phân tích (II.2)

> Ảnh mẫu: image_07 (entity trích xuất từ services)

#### Đặc điểm

- Hộp trắng, KHÔNG màu, KHÔNG stereotype
- **KHÔNG typed attribute** (chỉ `-attributeName`, không `-attributeName : type`)
- **KHÔNG method** — chỉ attributes
- Composition ◆ (diamond filled) + multiplicity cho "is part of"
- Aggregation ◇ (diamond open) + multiplicity cho "has a"
- Multiplicity ghi trên đường: `1`, `0..*`, `1..*`
- Association plain `--` cho quan hệ liên kết thường

#### Bố cục từ ảnh — Entity nào ở đâu?

```
  Room                    Order_detail
      \                      /
  Room_receipt  ◆------◆  Order
      \         /       \    \
  Damage_report ◇     Employee ◇--- Import_receipt ◇--- Provider
       |                        /          |
  Damage_detail ◇         Order        Import_detail
       |
  Facility
```

- **Entity trung tâm** (nhiều quan hệ nhất) đặt **ở giữa** — `Room_receipt`, `Employee`, `Order`
- **Entity "gốc"** (1 phía, ít quan hệ) đặt **ở biên** — `Room` (góc trên-trái), `Facility` (góc dưới-trái), `Provider` (góc dưới-phải)
- **Entity trung gian** (liên kết nhiều entity) đặt **gần entity gốc** — `Room_receipt` giữa `Room` và `Order`
- Entity cùng nhánh chức năng đặt **gần nhau**: nhóm Order (Order, Order_detail, Room_receipt) · nhóm Import (Import_receipt, Import_detail, Provider) · nhóm Damage (Damage_report, Damage_detail, Facility)

#### 3 loại quan hệ và khi nào dùng

| Loại quan hệ | Ký hiệu UML | Diamond | "Lực" quan hệ | Khi nào dùng |
|--------------|-------------|---------|---------------|---------------|
| **Composition** | `◆--` | Diamond filled (đen) | **Mạnh nhất** — entity con SỐNG VÀ CHẾT cùng entity cha | Entity con **không có ý nghĩa** nếu thiếu entity cha. VD: `Room_receipt ◆-- Room` (receipt không tồn tại nếu không có Room), `Order ◆-- Room_receipt` (order gắn với receipt) |
| **Aggregation** | `◇--` | Diamond open (trống) | **Trung bình** — entity con TỒN TẠI ĐỘC LẬP với entity cha | Entity con **vẫn có ý nghĩa** khi tách khỏi entity cha. VD: `Employee ◇-- Order` (employee tồn tại dù không có order), `Provider ◇-- Import_receipt` |
| **Association** | `--` | Không diamond | **Yếu nhất** — chỉ liên kết, không ownership | Quan hệ thuần túy, không có "sở hữu". VD: `Facility -- Damage_detail`, `Damage_report -- Employee` |

#### Quy tắc xác định lực quan hệ từ nghiệp vụ

1. **Hỏi: Entity A bị xóa thì Entity B có còn ý nghĩa không?**
   - B **chết** theo A → **Composition** ◆ (VD: Room_receipt chết nếu Room bị xóa)
   - B **vẫn sống** → **Aggregation** ◇ hoặc Association
2. **Hỏi: Entity A có "sở hữu" Entity B không?**
   - A tạo, quản lý, chứa B → **Composition** ◆
   - A chỉ "biết" B, B đến từ bên ngoài → **Aggregation** ◇
3. **Hỏi: Entity B có thể tồn tại độc lập không?**
   - KHÔNG — B luôn thuộc về A → **Composition** ◆
   - CÓ — B có lifecycle riêng → **Aggregation** ◇
   - KHÔNG SURE → dùng **Association** `--`

#### Multiplicity từ ảnh — bảng đầy đủ

| Entity A | Loại | Entity B | Multiplicity A | Multiplicity B | Giải thích |
|----------|------|----------|---------------|----------------|------------|
| Room | ◆ comp | Room_receipt | `1` | `0..*` | 1 phòng có nhiều receipt, receipt cần đúng 1 phòng |
| Room_receipt | ◆ comp | Order | `1` | `0..*` | 1 receipt có nhiều order |
| Room_receipt | ◆ comp | Damage_report | `1` | `0..*` | 1 receipt có nhiều report |
| Order | ◆ comp | Order_detail | `1` | `1..*` | 1 order PHẢI có ít nhất 1 detail |
| Import_receipt | ◆ comp | Import_detail | `1` | `1..*` | 1 receipt PHẢI có ít nhất 1 detail |
| Employee | ◇ agg | Order | `1` | `0..*` | 1 employee xử lý nhiều order |
| Employee | ◇ agg | Import_receipt | `1` | `0..*` | 1 employee tạo nhiều receipt |
| Provider | ◇ agg | Import_receipt | `1` | `0..*` | 1 provider có nhiều receipt |
| Facility | assoc | Damage_detail | `1` | `1..*` | facility có nhiều damage_detail |

#### Lưu ý nhỏ khi vẽ

- **Diamond luôn ở phía entity CHA** (entity "sở hữu"), KHÔNG ở phía entity con
- **Multiplicity ghi ở 2 đầu đường nối** — số ở phía entity tương ứng
- **`0..*` = optional, có thể 0** · `1..*` = mandatory, ít nhất 1 · `1` = đúng 1 · `0..1` = tối đa 1
- **Path tự động của VP**: khi thêm composition/aggregation, VP tự đặt diamond đúng hướng — nhưng cần verify sau khi autoLayout
- **Entity analysis KHÔNG có `id` attribute** — `id` chỉ thêm ở bước III.2 (thiết kế thực thể)
- **snake_case cho attribute names** — `-full_name`, `-order_time`, KHÔNG camelCase

---

### Kinh nghiệm loại 3: Biểu đồ lớp thực thể thiết kế (III.2)

> Ảnh mẫu: image_17

#### Khác biệt so với Biểu đồ lớp thực thể phân tích (II.2)

| Yếu tố | II.2 (Phân tích) | III.2 (Thiết kế) |
|--------|------------------|-----------------|
| Typed attribute | ❌ KHÔNG | ✅ `-name : String`, `-price : float` |
| PK attribute | ❌ KHÔNG | ✅ `-room_id : int`, `-emp_id : int` |
| Method | ❌ KHÔNG | ❌ KHÔNG |
| Composition/Aggregation | ✅ | ✅ |
| Multiplicity | ✅ | ✅ |
| Package grouping | ❌ | ❌ |
| snake_case attrs | ✅ | ✅ |

#### Bố cục từ ảnh — Entity Classes dàn tự do

- Entity classes **bố cục tự do**, KHÔNG theo hàng ngang hay cột dọc cứng
- Entity trung tâm (nhiều quan hệ nhất) đặt **ở giữa**: `Room_receipt`, `Employee`, `Order`
- Entity gốc ( 少 quan hệ) đặt **ở biên**: `Room` (góc trên-trái), `Facility` (góc dưới-trái), `Provider` (góc dưới-phải)
- Entity trung gian đặt **gần entity gốc** — VD: `Room_receipt` nằm giữa `Room` và `Order`
- **Diamond luôn ở phía entity cha** (entity "sở hữu")
- Entity classes **KHÔNG có methods** — chỉ có attributes (khác biệt với biểu đồ phân tích chức năng II.3)

#### 4 bước thiết kế lớp thực thể (giáo trình)

1. **Bước 1**: Thêm attribute `id` (PK) cho các lớp KHÔNG kế thừa từ lớp khác
2. **Bước 2**: Thêm kiểu dữ liệu cho mỗi attribute
3. **Bước 3**: Chuyển quan hệ liên kết → quan hệ kết tập/hợp thành (composition/aggregation)
4. **Bước 4**: Thêm attributes "đối tượng" cho quan hệ kết tập/hợp thành:
   - N-side của quan hệ 1-n → entity có `danh sách entity` kia
   - 1-side → entity có 1 entity kia
   - VD: `Room` là thành phần của `Hotel`, kiểu n-1 → Hotel có `danh sách Room`

#### Typed attribute pattern từ ảnh

```
-attribute_name : DataType
```

| DataType | Dùng cho | Ví dụ |
|----------|---------|-------|
| `int` | ID, quantity, capacity, stock | `-room_id : int`, `-capacity : int` |
| `String` | text fields | `-name : String`, `-status : String` |
| `float` | money, price | `-price : float`, `-total_amount : float` |
| `date` | ngày không giờ | `-import_date : date`, `-dob : date` |
| `datetime` | ngày có giờ | `-checkin_time : datetime`, `-order_time : datetime` |

#### PK/FK naming convention từ ảnh

- PK: `{entity}_id : int` — `room_id`, `emp_id`, `order_id`, `facility_id`
- FK: `{refEntity}_id : int` — `tblRoomReceiptID` trong ERD, hoặc `{refEntity}_id` trong class
- Attr name dùng **snake_case** (không camelCase): `room_fee`, `total_amount`, `unit_price`

#### Composition/Aggregation trong Design Entity

- Composition ◆ (diamond filled): `Room_receipt ◆-- Room` (receipt "owns" room reference)
- Aggregation ◇ (diamond open): `Employee ◇-- Order` (employee "has" orders)
- Plain association `--`: `Provider -- Import_receipt`

---

### Kinh nghiệm loại 4: Biểu đồ lớp thiết kế MVC (III.3.2)

> Tham khảo: `design_class_diagram.md`, `design_class_diagram_ALT.md`

#### Bố cục 3 TẦNG DỌC — quy tắc quan trọng nhất

```
┌─────────────────────────────────────────────────────────┐
│  TẦNG TRÊN: LỚP BIÊN (Boundary / Interface)            │
│  LoginFrm — StaffHomeFrm — SearchRoomFrm — ...          │
│  (JFrame classes / HTML pages)                           │
└─────────────────────────────────────────────────────────┘
                          │ association
                          ▼
┌─────────────────────────────────────────────────────────┐
│  TẦNG GIỮA: LỚP ĐIỀU KHIỂN (Control / DAO)             │
│  DAO (abstract) — UserDAO — RoomDAO — OrderDAO — ...    │
│  (JDBC classes)                                         │
└─────────────────────────────────────────────────────────┘
                          │ association
                          ▼
┌─────────────────────────────────────────────────────────┐
│  TẦNG DƯỚI: LỚP THỰC THỂ (Entity)                      │
│  User — Room — Order — Product — ...                    │
│  (POJO / data model)                                    │
└─────────────────────────────────────────────────────────┘
```

- **KHÔNG dùng package box 3 màu** (Boundary/Control/Entity boxes) — mẫu gốc KHÔNG có
- **KHÔNG dùng stereotype** `<<Boundary>>` `<<Control>>` `<<Entity>>` — mẫu gốc KHÔNG có
- **3 tầng xếp theo chiều DỌC**: Boundary trên, Control giữa, Entity dưới
- **Association lines `--`** nối giữa các tầng (Boundary→Control, Control→Entity) — KHÔNG mũi tên `-->`
- **Entity — Entity**: dùng composition/aggregation/multiplicity tùy quan hệ
- **Generalization** `▷` cho DAO abstract → DAO cụ thể (UserDAO extends DAO)

#### Bố cục chi tiết từng tầng (từ mẫu JFrame)

**Tầng Boundary (trên cùng):**
- Classes: `LoginFrm`, `ManagerHomeFrm`, `SearchRoomFrm`, `EditRoomFrm`...
- Named `XxxFrm` (JFrame pattern), KHÔNG phải `XxxView`
- Attrs dùng prefix `txt/btn/lbl/tbl/cbx` + typed: `-txtUsername : TextBox`, `-btnLogin : Button`
- Methods: `doGet()` (GET request), `doPost()` (POST request)
- **Constructor** `XxxFrm()` — mỗi form có constructor

**Tầng Control (giữa):**
- Abstract class `DAO` ở giữa — abstract, có `dbCon : Connection`
- Entity DAOs kế thừa từ `DAO`: `UserDAO`, `RoomDAO`, `OrderDAO`...
- Generalization arrows `▷` từ entity DAO → DAO abstract
- Methods của entity DAO: `getAll()`, `getById()`, `add()`, `update()`, `delete()`, `search()`
- **Boundary → Control**: association plain `--` (KHÔNG mũi tên)

**Tầng Entity (dưới cùng):**
- Typed attributes: `-name : String`, `-price : float`
- Constructor + getters/setters
- **KHÔNG dùng DTO** — method dùng trực tiếp entity type
- **Control → Entity**: association plain `--` (KHÔNG mũi tên)
- **Entity — Entity**: composition/aggregation + multiplicity

#### Direction arrow trong MVC

| Quan hệ | Arrow | Lý do |
|---------|-------|-------|
| Boundary → Control | `--` (plain association) | View gọi DAO để xử lý |
| Control → Entity | `--` (plain association) | DAO thao tác với Entity |
| Entity → Entity | `◆--` / `◇--` / `--` | Composition/Aggregation/Association tùy quan hệ |
| Control → Control (abstract) | `▷` (generalization) | Entity DAO kế thừa từ DAO abstract |
| KHÔNG dùng `-->` | directed association | Mẫu gốc KHÔNG có mũi tên ở bất kỳ association nào |
| KHÔNG dùng `..>` | dependency | Mẫu gốc KHÔNG dùng đường đứt |

#### Boundary attributes — bảng prefix đầy đủ

| Prefix | Loại | Kiểu | Ví dụ |
|--------|------|------|-------|
| `txt` | TextField/Input | `TextBox` | `-txtUsername : TextBox` |
| `btn` | Button | `Button` | `-btnLogin : Button` |
| `lbl` | Label | `Label` | `-lblSuccess : Label` |
| `tbl` | Table/List | `Table` | `-tblProductList : Table` |
| `cbx` | ComboBox/Select | `ComboBox` | `-cbxRoom : ComboBox` |

#### Boundary methods (thiết kế JFrame/Servlet)

| Method | Mô tả |
|--------|-------|
| `doGet()` | Tiếp nhận GET request, load form |
| `doPost()` | Tiếp nhận POST request, xử lý submit |

#### DAO Control class — chi tiết

- Abstract class `DAO` với `dbCon : Connection` + constructor kết nối
- Entity DAO kế thừa từ `DAO`: `RoomDAO`, `OrderDAO`, `ProductDAO`...
- Methods: `getAll()`, `getById()`, `add()`, `update()`, `delete()`, `search()`
- **Generalization `▷`**: `UserDAO ▷ DAO`, `RoomDAO ▷ DAO` (đường mũi tên rỗng đầu)
- DAO abstract **nằm giữa**, entity DAOs **bên phải hoặc dưới** DAO abstract

#### Entity class (thiết kế) — chi tiết

- Typed attributes (`: type`), có constructor + getters/setters
- KHÔNG dùng DTO trong class diagram — method dùng trực tiếp entity type
- Entity có thể có **methods** (khác II.2 và III.2): `+getBookingHistory()`, `+calculateTotal()`
- Attribute names dùng **camelCase** (không snake_case như II.2/III.2): `fullName`, `phoneNumber`, `staffRole`

#### Lưu ý nhỏ khi vẽ MVC trong VP

- **autoLayoutDiagram sẽ tạo package containers** nếu classes có `packageName` → cần remove sau khi layout
- **KHÔNG gọi autoLayoutDiagram sau khi đã xoá package** — sẽ tạo lại package
- **Entity có thể xuất hiện ở cả III.2 (design entity) và III.3.2 (MVC design)** — trong III.2 entities KHÔNG có methods, trong III.3.2 entities CÓ methods
- **Boundary names JFrame**: `XxxFrm` (không `XxxView`) — `LoginFrm`, `ManagerHomeFrm`, `SearchRoomFrm`
- **Boundary attrs**: prefix `txt/btn/lbl/tbl` — KHÔNG dùng `in_/out_/sub_` (đó là pha phân tích)

---

### Kinh nghiệm loại 5: ERD — Sơ đồ thực thể-tiêu đề (III.1)

> Ảnh mẫu: image_18

#### Bố cục từ ảnh — Entity-centric layout

```
           tblRoom
              |
       tblRoomReceipt  ◆---◆  tblOrder  ◆---◆  tblOrder_detail
        /          \        |            \         /
tblDamageReport   tblEmployee          tblProduct
       |            |          \              /
tblDamage_detail    |     tblImport_receipt  ◇--- tblProvider
       |            |          |
  tblFacility   tblImport_receipt  ◆---◆  tblImport_detail
```

- **Table trung tâm** (nhiều FK nhất) đặt **ở giữa**: `tblRoomReceipt`, `tblEmployee`, `tblOrder`
- **Table "gốc"** ( 少 FK) đặt **ở biên**: `tblRoom` (góc trên), `tblFacility` (góc dưới-trái), `tblProvider` (góc dưới-phải)
- **Table detail** đặt **gần parent**: `tblOrder_detail` gần `tblOrder`, `tblDamage_detail` gần `tblDamageReport`
- **Dashed lines** connect tables (VP default cho ERD)
- **FK column placement**: FK nằm ở table "con" (n-side), KHÔNG ở table "cha" (1-side)

#### Style VP ERD từ ảnh

| Yếu tố | Style chuẩn |
|---------|-------------|
| Table color | **Cam** (orange) — VP default cho ERD |
| Table name prefix | `tbl` — `tblRoom`, `tblOrder`, `tblProduct` |
| PK column | `ID` với PK key icon, `integer(10)` |
| FK column | `tblRefEntityID` với FK key icon, `integer(10)` |
| Column types | `integer(10)`, `varchar(50)`, `numeric(12,2)`, `datetime`, `date`, `timestamp` |
| Lines | **Dashed** lines between tables |
| Layout | Organic/compact — tables gần nhau, ngắn gọn |
| PK icon | 🔑 key icon bên trái tên column |
| FK icon | 🔑 key icon bên trái tên column + `U` badge |

#### Column type mapping

| Application type | SQL type |
|-----------------|----------|
| ID (integer) | `integer(10)` |
| Name/Text | `varchar(50)` hoặc `varchar(255)` |
| Price/Amount | `numeric(12, 2)` |
| Quantity/Stock | `integer(10)` |
| Date only | `date` |
| DateTime | `datetime` hoặc `timestamp` |
| Password | `varchar(50)` |
| Status | `varchar(50)` |

---

### Kinh nghiệm loại 6: UI Wireframe

> Ảnh mẫu: image_19–30

- Yellow (vàng) cho title bar + button
- Cyan (xanh nhạt) cho input field label
- White background
- Grid lines
- **Không vẽ bằng VP** — thường dùng Excel/Google Sheets hoặc tool wireframe riêng

---

### Checklist khi vẽ class diagram trong VP MCP

**Trước khi vẽ:**
- [ ] Xác định loại diagram (Phân tích chức năng / Thực thể phân tích / Thực thể thiết kế / MVC design / ERD)
- [ ] Xác định pha UP tương ứng (II.2 / II.3 / III.1 / III.2 / III.3.2)
- [ ] Kiểm tra tên class unique (tránh ClassXXX bug)
- [ ] Xác định actor nào (Staff, Manager, Client...) để biết HomeView tương ứng

**Khi vẽ Biểu đồ lớp phân tích chức năng (II.3):**
- [ ] Mỗi UC 1 diagram riêng
- [ ] Bố cục 2 hàng: View trên, Entity dưới
- [ ] LoginView góc trên-trái → HomeView bên phải → FunctionViews tiếp → ConfirmView góc phải
- [ ] View attrs: `in_/out_/sub_/outsub_` prefix, KHÔNG typed
- [ ] Entity attrs: KHÔNG typed, KHÔNG prefix
- [ ] Entity methods: `+methodName()` có `()`
- [ ] Association: `--` (KHÔNG `-->`)
- [ ] KHÔNG có package box màu
- [ ] Bắt đầu từ HomeView, liệt kê đầy đủ attrs

**Khi vẽ Biểu đồ lớp thực thể phân tích (II.2):**
- [ ] KHÔNG typed attrs, KHÔNG methods
- [ ] Composition ◆ / Aggregation ◇ + multiplicity
- [ ] Diamond ở phía entity CHA
- [ ] Entity trung tâm ở giữa, entity gốc ở biên
- [ ] snake_case cho attr names
- [ ] Xác định lực quan hệ: Composition (chết theo) → Aggregation (tồn tại độc lập) → Association (liên kết thuần)

**Khi vẽ Biểu đồ lớp thực thể thiết kế (III.2):**
- [ ] Typed attrs: `-name : String`, `-price : float`
- [ ] PK: `-entity_id : int`
- [ ] Composition/Aggregation + multiplicity
- [ ] snake_case cho attr names
- [ ] KHÔNG methods
- [ ] 4 bước: thêm id → thêm typed → chuyển quan hệ → thêm attrs đối tượng

**Khi vẽ Biểu đồ lớp thiết kế MVC (III.3.2):**
- [ ] Bố cục 3 TẦNG DỌC: Boundary (trên) → Control (giữa) → Entity (dưới)
- [ ] KHÔNG package box 3 màu
- [ ] KHÔNG stereotype `<<Boundary>>`/`<<Control>>`/`<<Entity>>`
- [ ] Association: `--` (KHÔNG `-->`, KHÔNG `..>`)
- [ ] Boundary names: `XxxFrm` (JFrame)
- [ ] Boundary attrs: `txt/btn/lbl/tbl` prefix + typed (`: TextBox`)
- [ ] Boundary methods: `doGet()`, `doPost()`
- [ ] Control: abstract `DAO` + `dbCon`, generalization `▷` cho entity DAOs
- [ ] Entity: typed attrs + methods + camelCase
- [ ] KHÔNG dùng DTO

**Khi vẽ ERD (III.1):**
- [ ] `tbl` prefix cho mọi table
- [ ] PK `ID : integer(10)` với PK key icon
- [ ] FK `tblRefEntityID : integer(10)` với FK key icon
- [ ] Typed columns: `varchar(50)`, `numeric(12,2)`, `integer(10)`
- [ ] Dashed lines giữa các table
- [ ] Table trung tâm ở giữa, detail gần parent

---

### Tổng hợp naming convention theo pha

| Yếu tố | II.2 (Thực thể PT) | II.3 (Phân tích chức năng) | III.1 (ERD) | III.2 (Thực thể TK) | III.3.2 (MVC) |
|--------|--------------------|-----------------------------|-------------|----------------------|----------------|
| Attr name | snake_case | snake_case | — | snake_case | camelCase |
| Attr prefix | KHÔNG | `in_/out_/sub_` | — | KHÔNG | `txt/btn/lbl/tbl` |
| Typed attr | ❌ | ❌ | — | ✅ | ✅ |
| Method | ❌ | ✅ Entity only | — | ❌ | ✅ Entity |
| PK/id | ❌ | ❌ | `ID` | ✅ | — |
| Entity name | PascalCase | PascalCase | `tbl*` | PascalCase | PascalCase |
| View name | — | `XxxView` | — | — | `XxxFrm` |
| Composition | ✅ | ❌ | — | ✅ | ✅ Entity↔Entity |
| Aggregation | ✅ | ❌ | — | ✅ | ✅ Entity↔Entity |
| Generalization | ❌ | ❌ | — | ❌ | ✅ DAO→DAO abstract |

---

## Kinh nghiệm mới — tổng hợp từ sessions (2026-06-13)

### Font = Dialog (VP + PlantUML)

VP dùng font `Dialog` mặc định trên MỌI platform (Java Swing default). PlantUML cũng nên dùng `defaultFontName "Dialog"` thay vì Arial/Segoe UI.

### Class diagram: HỘP TRẮNG, KHÔNG package, KHÔNG stereotype

Mẫu gold standard (image_07,08,16,36): **hộp trắng trơn, KHÔNG màu package, KHÔNG stereotype `<<...>>`**. BCE tách bằng tên hậu tố + bố cục (trái/giữa/phải), không bằng package màu.

- ❌ SAI: `package "Boundary" #DDEEFF { class LoginView <<Boundary>> { } }`
- ✅ ĐÚNG: `class LoginView { -txtUsername : TextBox }` (hộp trắng, không wrapper)

### Sequence: self-message pattern

Mẫu image_12: method() là **self-message trên Entity**, không phải arrow trực tiếp Boundary→Entity:

```
Boundary -> Entity : call
Entity -> Entity : checkLogin()
Entity --> Boundary : return
```

3 bước, không phải 1 bước `Boundary -> Entity : checkLogin()`.

### Arrow label conventions

| Tình huống | Label | Ví dụ |
|-----------|-------|-------|
| Actor → Boundary | short English | `1: click btnManage`, `3: input info + click btnSave` |
| Boundary/Control kích hoạt | `call` | `2: call`, `4: call` |
| Control/DAO → Entity method | `methodName()` | `4: list()`, `5: listTiers()`, `6: save(order)` |
| Entity/Control trả kết quả | `return` | `5: return`, `7: return` |
| Boundary → Actor hiển thị | `display` / `showMessage()` | `7: display`, `showMessage("saved")` |

Pha phân tích: `methodName()` không tham số. Pha thiết kế: `methodName(param: Type)` đầy đủ.

### Relationships trong class diagram thiết kế

- Boundary — Control: `--` (association thuần, **KHÔNG mũi tên**)
- Control — Entity: `--` (association thuần, **KHÔNG mũi tên**)
- Entity — Entity (owned): `*--` (composition), `o--` (aggregation)
- Entity — Entity (reference): `--` với multiplicity
- KHÔNG dùng `-->` (directed association) cho Boundary–Control hay Control–Entity
- KHÔNG dùng `..>` (dependency) trong pha III class diagram

### UC tổng quan: khung hệ thống rectangle

Mẫu image_02: **khung hệ thống** (rectangle) bao UC, nhãn = tên module; actor ngoài hai bên; actor xanh `#7AD2FF`.

### Narrative format

- **Phân tích (II.3):** dùng bullet points `-`, KHÔNG code block
- **Kịch bản (II.4, III.4):** dùng danh sách đánh số `1, 2, 3…`, KHÔNG bullet

### Biểu đồ tuần tự: happy path only

II.4 và III.4 CHỈ vẽ luồng thành công — không có `alt`/`else`/`end` block. Ngoại lệ chỉ ở văn bản II.1.

### Mỗi UC = 1 BCE diagram riêng

Không gộp nhiều UC vào chung 1 diagram.

### Phase I/II: KHÔNG lậm kỹ thuật

Chỉ mô tả "Actor hành động → Hệ thống phản hồi". KHÔNG nhắc Redis, JWT, HMAC, Kafka, TTL, tên field/cột, công thức. Chi tiết kỹ thuật chỉ từ Pha III.

### Heading convention

`N.`→H2, `N.N.`→H3, `N.N.N.`→H4, `a)` KHÔNG phải heading (dùng bullet).

### KHÔNG dùng DTO trong class diagram thiết kế

Method signature dùng trực tiếp entity type: `saveStaff(employee: Employee)`, không phải `saveStaff(dto: EmployeeDTO)`.

### Boundary PHẢI có biến lưu entity

Nếu hiển thị/thao tác entity → PHẢI có attribute `-tênEntity: Entity`. LoginPage không cần (chỉ gửi form input).

### Entity attributes PHẢI khớp codebase

Không lược bỏ tùy tiện fields. Controller methods phải khớp codebase endpoints.

### Skill chỉ đăng ký trong project `cnpm-hrm`

Không tự dùng được ở project khác. Khi `Skill("cnpm")` ở project khác → "Unknown skill". Fix: implement thủ công theo SKILL.md.
