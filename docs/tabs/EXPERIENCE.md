# EXPERIENCE — Ghi chú cải thiện skill `cnpm`

> File nháp, KHÔNG commit. Dùng để gom kinh nghiệm cho một session khác refine skill `cnpm`.

---

## Điều làm tốt (giữ lại)

- Cấu trúc UP 4 pha + 11 mục rõ ràng, dễ map sang rubric audit.
- Quy ước BCE + tách Boundary/Control/Entity giúp sequence & class diagram nhất quán.
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
- **Scenario text (kịch bản phiên bản 2) ở pha II phân tích → bullet; scenario (kịch bản phiên bản 3) ở pha III thiết kế → numbered list.**

## Vấn đề hạ tầng (không thuộc nội dung skill)

- **`main` branch: `.claude/skills/cnpm/SKILL.md` còn dấu xung đột `git stash` (dòng ~541–548)** chưa giải quyết, bị commit nhầm. Cần sửa trước khi merge `report` → `main`. (Đang xử lý ở task riêng.)

## Phát hiện từ rubric audit (chạy 2026-06-02, commit 24245b4)

- **Bản nháp local lệch nặng so với Google Docs.** Giả định services pha III lẫn code thư viện + pha IV trống là từ bản nháp local — bản Google Docs SẠCH, có 8 TC thật + tên bảng `tbl*`. → Audit PHẢI dựa trên export, không bản nháp. (Đã ghi vào skill audit.)
- **Text export không nhúng ảnh inline.** Các mục dựa trên ảnh (UC diagram, BCE, sequence, ERD, MVC) đọc text thấy "placeholder rỗng" nhưng ảnh có thật trong `screenshots/`. → Skill audit phải chấm mục ảnh theo SỐ LƯỢNG ẢNH + heading, không theo text. services có 42 ảnh nhưng text sơ sài → cần mắt người xác minh.
- **Lỗi hệ thống pha I: R01 + R03 ✗ ở CẢ 4 module.** Không module nào có bảng UC chính thức (ID/tên/actor/mô tả) hay bảng Include/Extend — chỉ có heading + narrative. → `cnpm` nên BẮT BUỘC sinh 2 bảng này ở pha I.
- **R07 (kịch bản ngoại lệ) thiếu gần như toàn bộ** — chỉ ghi inline trong sequence. → `cnpm` nên tách kịch bản ngoại lệ thành mục riêng.
- **R11 (thiết kế lớp thực thể 4 bước) hiếm khi tường minh** trừ khi có template rõ.
- **Tên entity khách hàng phân mảnh 3 cách:** `User` (account) / `Client` (booking, services) / `Customer` (core). Cần bảng entity chuẩn toàn hệ thống.
- **Đính chính cross-module:** receipt (`Room_receipt`) và nhân viên (`Employee`) thực ra NHẤT QUÁN ở cấp class/bảng — tên Việt (`HoaDon`/`NhanVien`/`Phong`) chỉ ở văn xuôi phân tích. Vấn đề thật chỉ còn: khách hàng (X01), hạng hội viên (X02: `MembershipTier` vs `MemberRanking`), gọi liên module (X06).
