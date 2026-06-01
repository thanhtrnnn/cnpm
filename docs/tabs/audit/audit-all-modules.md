# Audit tài liệu UP — Tất cả module

- **Ngày audit:** 2026-06-02
- **Commit:** `24245b4`
- **Nguồn:** `docs/tabs/exports/<module>/` (nội dung tải về từ Google Docs — KHÔNG phải bản nháp local)
- **Module audit:** account, booking, services, core
- **Số ảnh mỗi module:** account 13 · booking 21 · services 42 · core 18

> ⚠️ **Lưu ý phương pháp:** Bản text export KHÔNG nhúng ảnh inline — ảnh được tải riêng vào `screenshots/`. Vì vậy các mục **dựa trên ảnh** (R04, R05, R09, R10, R12, R14, R16) được chấm theo **số lượng ảnh + heading mục**, không theo nội dung text. Các mục text-based chấm theo text. Khi text báo "placeholder rỗng" nhưng module có nhiều ảnh → cần **mắt người xác minh** ảnh chứa gì (xem phần Cảnh báo services).

---

## ⚠️ Đính chính quan trọng (so với giả định ban đầu từ bản nháp local)

Giả định trong skill (lấy từ bản nháp local `services/full.md`) đã **SAI** so với bản Google Docs:

| Giả định cũ (bản nháp local) | Thực tế trên Google Docs (export) |
| --- | --- |
| services pha III lẫn code hệ thống thư viện (LibrarianDAO/Book...) | **SẠCH** — không có dấu vết thư viện, toàn bộ là nội dung karaoke |
| services pha IV: 0 test case | **8 test case thật**, có CSDL trước/sau |
| services không có tên bảng `tbl*` | **Có** — tblOrder, tblProduct, tblRoomReceipt, tblOrderDetail... |

→ Khẳng định lại nguyên tắc: **audit theo export Google Docs**, không theo bản nháp local.

---

## 1. Ma trận đầy đủ nội dung (R01–R21)

| #   | Pha | Hạng mục | account | booking | services | core |
| --- | --- | --- | :---: | :---: | :---: | :---: |
| R01 | I | Bảng UC (ID/tên/actor/mô tả) | ✗ | ✗ | ✗ | ✗ |
| R02 | I | Bảng Actor | ✗ | ⚠ | ⚠ | ✗ |
| R03 | I | Bảng Include/Extend | ✗ | ✗ | ✗ | ✗ |
| R04 | I | Ảnh UC tổng quan | ⚠ | ✓ | ⚠ | ✓ |
| R05 | I | Ảnh UC chi tiết (1/UC) | ⚠ | ✓ | ⚠ | ✗ |
| R06 | II | Bảng kịch bản chuẩn/UC | ✓ | ✓ | ✗ | ⚠ |
| R07 | II | Kịch bản ngoại lệ/UC | ⚠ | ✗ | ✗ | ✗ |
| R08 | II | Mô hình hóa lớp 5 bước | ✓ | ✓ | ✓ | ⚠ |
| R09 | II | Ảnh sơ đồ lớp phân tích (BCE) | ✓ | ✓ | ✓ | ✓ |
| R10 | II | Ảnh sequence phân tích/UC | ✓ | ✓ | ⚠ | ✓ |
| R11 | III | Thiết kế lớp thực thể 4 bước | ✗ | ⚠ | ✗ | ✗ |
| R12 | III | Ảnh ERD | ✗ | ✓ | ⚠ | ✗ |
| R13 | III | Wireframe/UC | ✗ | ✓ | ⚠ | ⚠ |
| R14 | III | Ảnh sơ đồ lớp thiết kế (MVC) | ✗ | ⚠ | ⚠ | ✗ |
| R15 | III | Bảng chữ ký hàm | ✗ | ✓ | ✗ | ✗ |
| R16 | III | Ảnh sequence thiết kế/UC | ✗ | ⚠ | ⚠ | ✗ |
| R17 | IV | Bảng kế hoạch test (TC ID) | ✗ | ✓ | ⚠ | ✓ |
| R18 | IV | CSDL trước/sau mỗi TC | ✗ | ✓ | ✓ | ✓ |
| R19 | IV | Bảng kịch bản UI từng bước/TC | ✗ | ⚠ | ✗ | ⚠ |
| R20 | IV | Phủ TC thành công + thất bại | ✗ | ✓ | ⚠ | ✓ |
| R21 | IV | Edge case (khóa/trùng/sai) | ✗ | ✓ | ⚠ | ⚠ |
| | | **Điểm ✓ (✓=1, ⚠=0.5)** | **~5.5/21** | **~15/21** | **~7/21** | **~8/21** |

**Số UC / số TC mỗi module:**

| Module | UC | Test case | Pha có nội dung text |
| --- | --- | --- | --- |
| account | 5 (UC01–04, UC20) | 0 | I (sơ sài), II (tốt). III + IV **chưa đẩy lên Docs** |
| booking | 4 (đặt/huỷ/check-in/check-out) | **15** | I, II, III, IV — đầy đủ nhất |
| services | 4 (order/báo hỏng/menu/kho) | 8 | II + IV có nội dung; I, III nhiều ảnh nhưng text sơ sài |
| core | 5 (UC16–UC20: branch/customer/tier/roomtype/room) | **22** | I, II, IV có nội dung; III sơ sài |

---

## 2. Nhất quán biến đổi liên pha (T01–T04)

| #   | Kiểm tra | account | booking | services | core |
| --- | --- | :---: | :---: | :---: | :---: |
| T01 | Entity II → III khớp | N/A* | ✓ | ✓ | ✓ |
| T02 | Bảng ERD `tbl*` ↔ entity class | N/A* | ✓ | ✓ | ✗ (không có ERD) |
| T03 | Method controller có trong bảng chữ ký | N/A* | ✓ | ⚠ (method ở narrative IV, thiếu bảng III) | ✗ (không có bảng) |
| T04 | Số Boundary ≥ số wireframe | ✗ (6 BC / 0 wf) | ✓ (7/7) | ⚠ (8 heading wf rỗng) | ✗ (0 wf / 5 UC) |

\* account: pha III chưa có trên Docs → không kiểm tra được. 6 Boundary class đã định nghĩa ở pha II (LoginView, RegisterView, OTPVerifyView, ChangePasswordView, ProfileView, StaffManageView) nhưng 0 wireframe.

**Phần tử lệch đáng chú ý:**
- **booking:** rất khớp — entity {Client, Branch, Room, Employee, Room_receipt, Room_receipt_detail, MemberRanking, Promotion} đồng nhất II↔III↔tbl*; method {searchFreeRoom, createBooking, checkIn, calculateInvoice...} có trong cả bảng chữ ký lẫn sequence thiết kế.
- **core:** thiếu ERD và bảng chữ ký hàm → không kiểm chứng được biến đổi; method (searchBranch, addBranch, lockAccount...) chỉ nằm rải rác trong văn xuôi.

---

## 3. Nhất quán entity/bảng liên module (X01–X06)

| #   | Khái niệm | account | booking | services | core | Trạng thái |
| --- | --- | --- | --- | --- | --- | --- |
| X01 | Khách hàng | `User` | `Client` | `Client` | `Customer` | ✗ **3 tên: User / Client / Customer** |
| X02 | Hạng hội viên | `MembershipTier` | `MemberRanking` | (ẩn) | `MembershipTier` | ✗ booking lệch (`MemberRanking`) |
| X03 | Hóa đơn/receipt | — | `Room_receipt` | `Room_receipt` | — | ✓ **nhất quán** (đính chính: KHÔNG còn `HoaDon`) |
| X04 | Phòng | — | `Room` | `Room` | `Room` | ✓ nhất quán (class/bảng dùng tiếng Anh) |
| X05 | Nhân viên | `Employee` | `Employee` | `Employee` | (ẩn) | ✓ **nhất quán** (đính chính: class dùng `Employee`, không phải `NhanVien`) |
| X06 | Gọi liên module | — | — | — | gọi `Booking.getBookingHistory()` | ⚠ phụ thuộc chưa tài liệu hóa phía booking |

**Đính chính so với giả định ban đầu:** X03 (receipt) và X05 (Employee) thực ra **nhất quán** ở cấp class/bảng — tên tiếng Việt (`HoaDon`, `NhanVien`, `Phong`) chỉ xuất hiện trong văn xuôi phân tích, không phải tên class. Vấn đề thật chỉ còn **X01 (khách hàng: 3 tên)**, **X02 (hạng hội viên)**, và **X06 (gọi liên module)**.

---

## 4. Khoảng trống & gợi ý sửa

### account (ưu tiên cao — đang là module đang làm)
- **R01–R03 ✗:** Pha I chỉ có heading, thiếu bảng UC / bảng Actor / bảng Include-Extend. → Bổ sung 3 bảng từ nội dung pha II đã có.
- **Pha III + IV ✗:** Chưa đẩy lên Google Docs. → User dán tay phần III (Design) và IV (Test) từ bản nháp local `account/iii-design.md`, `account/iv-test.md`.
- **R07 ⚠:** Ngoại lệ chỉ ghi inline trong sequence. → Tách thành kịch bản ngoại lệ riêng cho UC01 (sai mật khẩu/khóa), UC02 (OTP sai).

### services (ưu tiên cao — text sơ sài dù nhiều ảnh)
- **R01, R03–R07 ✗/⚠:** Pha I–II nhiều mục là **placeholder rỗng trong text** dù module có **42 ảnh**. → **Cần mắt người xác minh** 42 ảnh chứa gì; nếu ảnh đã có biểu đồ/kịch bản thì bổ sung phần text/bảng tương ứng cho khớp.
- **R15 ✗:** Thiếu bảng chữ ký hàm pha III. → Bổ sung bảng method (createOrder, searchProduct, updateStock...) với input/output.
- **R19 ✗:** Test case chỉ có CSDL trước/sau, thiếu bảng kịch bản UI từng bước. → Thêm cột Bước/Hành động.
- **R20–R21 ⚠:** 8 TC, phủ chưa đều (Tạo order có cả success/fail; 3 UC còn lại chủ yếu 1 success). → Thêm TC thất bại cho menu/kho/báo hỏng.

### core
- **Pha III ✗ gần như toàn bộ:** Thiếu ERD, thiết kế lớp thực thể 4 bước, wireframe, sơ đồ lớp thiết kế, bảng chữ ký hàm. → Đây là khoảng trống lớn nhất; cần dựng đủ pha III.
- **R08 ⚠:** Mô hình hóa lớp thiếu Bước 2 (trích danh từ chi tiết). 
- **R07 ✗:** Thiếu kịch bản ngoại lệ.
- **X06:** Tài liệu hóa việc gọi `Booking.getBookingHistory()` như một giao diện liên module.
- ✓ Mạnh ở pha IV: **22 TC**, có CSDL trước/sau.

### booking (mốc tham chiếu)
- **R01, R03 ✗:** Vẫn thiếu bảng UC chính thức + bảng quan hệ (dù nội dung narrative đầy đủ).
- **R07 ✗:** Thiếu kịch bản ngoại lệ tách riêng.
- **R11 ⚠:** Thiếu 4 bước thiết kế lớp thực thể tường minh.
- **R19 ⚠:** TC có CSDL trước/sau nhưng thiếu bảng kịch bản UI từng bước.
- Tổng thể tốt nhất: đủ 4 pha, biến đổi liên pha khớp, 15 TC phủ success/fail/edge.

---

## 5. So sánh độ hoàn thiện (mốc = booking)

```
booking   ███████████████░░░░░  ~15/21  ← đầy đủ nhất, 4 pha, 15 TC, biến đổi khớp
core      ████████░░░░░░░░░░░░   ~8/21  ← mạnh pha IV (22 TC), yếu pha III
services  ███████░░░░░░░░░░░░░   ~7/21  ← nhiều ảnh (42) nhưng text sơ sài, 8 TC thật
account   █████░░░░░░░░░░░░░░░░  ~5.5/21 ← mới I+II trên Docs, III+IV chờ dán tay
```

**Điểm chung cần khắc phục toàn hệ thống:**
1. **R01 + R03 ✗ ở CẢ 4 module:** không module nào có bảng UC chính thức (ID/tên/actor/mô tả) và bảng Include/Extend. → Lỗi hệ thống của quy trình pha I; nên thêm vào skill `cnpm`.
2. **R07 ✗ gần như toàn bộ:** thiếu kịch bản ngoại lệ tách riêng (chỉ ghi inline).
3. **R11 yếu:** "thiết kế lớp thực thể 4 bước" hiếm khi tường minh.
4. **Thống nhất tên entity khách hàng** (User/Client/Customer → chọn 1).

> Khuyến nghị: cập nhật skill `cnpm` để bắt buộc bảng UC + bảng quan hệ (pha I), kịch bản ngoại lệ (pha II), và một **bảng entity chuẩn toàn hệ thống** để chống phân mảnh tên (xem `docs/tabs/EXPERIENCE.md`).
