# Task 2 — Deep Audit 5 Modules

> Nguồn: exports/ (text export từ Google Docs). Ảnh không inline — xem thực tế trong screenshots/.

---

## 1. Tài khoản & Thành viên

### Danh sách Use Case

| ID | Tên UC | Actor chính |
|---|---|---|
| UC01 | Đăng nhập | Thành viên (User) |
| UC02 | Đăng ký | Khách hàng |
| UC03 | Đổi mật khẩu | Thành viên (User) |
| UC04 | Quản lý thông tin cá nhân | Khách hàng |
| UC20 | Quản lý tài khoản nhân viên | Chủ doanh nghiệp (Admin) |

### Entity chính

| Class (Analysis) | Bảng CSDL |
|---|---|
| User | tblUser (single-table: Client + Employee + Admin) |
| Client (extends User) | tblUser (role = CLIENT) |
| Employee (extends User) | tblUser (role = EMPLOYEE) |
| MembershipTier | tblMembershipTier |
| OTP | tblOTP |
| LoginSession | tblLoginSession |

### Ảnh biểu đồ UC
- `exports/account/screenshots/` — 21 ảnh
- UC tổng quan: khoảng image_01–02; sequence diagrams từ image_03 trở đi (cần xác minh thủ công)

### Nhận xét
- Nội dung đầy đủ nhất trong 5 module: có đủ 4 pha, kịch bản v2 + v3, test case có CSDL trước/sau.
- **Tên khách hàng:** `Client` (kế thừa `User`)
- **Hạng hội viên:** `MembershipTier`
- UC20 ở đây = Quản lý tài khoản nhân viên → xung đột với Core module (UC20 = Quản lý phòng hát).

---

## 2. Quản lý đặt & trả phòng

### Danh sách Use Case

| ID | Tên UC | Actor chính |
|---|---|---|
| UC05 | Đặt phòng (online + tại chi nhánh) | Khách hàng + NV lễ tân |
| UC06 | Hủy đặt phòng | Khách hàng + NV lễ tân |
| UC07 | Check-in | NV lễ tân |
| UC08 | Check-out | NV lễ tân |

### Entity chính

| Class | Bảng CSDL |
|---|---|
| Client | tblClient |
| Branch | tblBranch |
| Room | tblRoom |
| Employee | tblEmployee |
| Room_receipt | tblRoom_receipt |
| Room_receipt_detail | tblRoom_receipt_detail |
| MemberRanking | tblMemberRanking |
| Promotion | tblPromotion |
| — (junction) | tblApply_promotion |

### Ảnh biểu đồ UC
- `exports/booking/screenshots/` — 21 ảnh
- UC tổng quan + phân rã (4 UC): khoảng image_01–05

### Nhận xét
- Đầy đủ 4 pha, kịch bản phân tích + thiết kế chi tiết, 15 test case.
- **Tên khách hàng:** `Client` — nhất quán với Account.
- **Hạng hội viên:** `MemberRanking` — KHÁC với Account/Core (`MembershipTier`). ⚠️ X02.
- `Room_receipt` thay vì `HoaDon` — thực ra nhất quán ở cấp class/bảng.

---

## 3. Dịch vụ & Sản phẩm

### Danh sách Use Case

| Chức năng | Actor chính |
|---|---|
| Tạo order / Quản lý order | NV phục vụ |
| Báo cáo tình trạng hàng hóa | NV phục vụ |
| Quản lý menu | Quản lý chi nhánh |
| Quản lý kho | Quản lý chi nhánh |

> **⚠️ Không có UC number** — module không gán UC01–UCxx. Cần bổ sung khi hoàn thiện.

### Entity chính

| Class | Bảng CSDL |
|---|---|
| Employee | tblEmployee |
| Room | tblRoom |
| Order | tblOrder |
| Order_detail | tblOrderDetail |
| Product | tblProduct |
| Room_receipt | tblRoomReceipt |
| Damage_report | tblDamageReport |
| Damage_detail | tblDamageDetail |
| Facility | tblFacility |
| Provider | tblProvider |
| Import_receipt | tblImportReceipt |
| Import_detail | tblImportDetail |

### Ảnh biểu đồ UC
- `exports/services/screenshots/` — 42 ảnh (nhiều nhất)
- UC tổng quan + 4 biểu đồ phân rã: khoảng image_01–05; sequence + MVC diagrams chiếm phần lớn còn lại.

### Nhận xét
- Module phong phú nhất về entity (12 bảng). Text export tương đối đầy đủ.
- **Không có khách hàng trực tiếp** — Khách hàng là actor gián tiếp (thông qua Room_receipt).
- **Provider** là entity đặc trưng riêng của module này.

---

## 4. Quản trị cốt lõi

### Danh sách Use Case

| ID | Tên UC | Actor chính |
|---|---|---|
| UC16 | Quản lý hệ thống chi nhánh | Admin |
| UC17 | Quản lý khách hàng toàn hệ thống | Admin |
| UC18 | Quản lý hạng hội viên | Admin |
| UC19 | Quản lý danh mục loại phòng | Admin |
| UC20 | Quản lý phòng hát chi nhánh | Quản lý chi nhánh |

> **⚠️ UC20 xung đột:** Account module cũng gán UC20 = "Quản lý tài khoản nhân viên". Theo tab XÁC ĐỊNH YÊU CẦU, UC20 = Quản lý tài khoản nhân viên. Core module nên đổi UC phòng hát → UC19b hoặc tách riêng.

### Entity chính

| Class | Bảng CSDL |
|---|---|
| Branch | tblBranch |
| Customer | tblCustomer |
| MembershipTier | tblMembershipTier |
| RoomType | tblRoomType |
| Room | tblRoom |
| Booking | tblBooking (external/ngoại lai) |

### Ảnh biểu đồ UC
- `exports/core/screenshots/` — 28 ảnh
- UC tổng quan + 5 UC phân rã: khoảng image_01–07

### Nhận xét
- **Tên khách hàng:** `Customer` — KHÁC với Account/Booking (`Client`). ⚠️ X01.
- **Hạng hội viên:** `MembershipTier` — nhất quán với Account, KHÁC Booking. ⚠️ X02.
- `Booking` là entity ngoại lai — Core tham chiếu nhưng không sở hữu.
- Test case đầy đủ 22 TC, kịch bản v3 chi tiết từng bước.

---

## 5. Nhân sự & Báo cáo thống kê

### Danh sách Use Case

| ID | Tên UC | Actor chính |
|---|---|---|
| UC11 | Quản lý nhân viên chi nhánh | Quản lý chi nhánh |
| UC13 | Báo cáo số liệu chi nhánh | Quản lý chi nhánh |
| UC14 | Xem thông tin khách hàng chi nhánh | Quản lý chi nhánh |
| UC21 | Tổng hợp báo cáo toàn chuỗi | Chủ doanh nghiệp |

### Entity chính

| Class (Phân tích — tiếng Việt) | Bảng CSDL |
|---|---|
| Employee | tblEmployee |
| ChiNhanh | tblBranch (suy đoán) |
| CaLamViec | tblShift |
| ChamCong | tblTimekeeping |
| DanhGiaNhanVien | tblEvaluation |
| QuyetDinh | — (chưa rõ tên bảng) |
| KhachHang | tblCustomer |
| HoaDon | tblReceipt |
| BaoCao | — (tạo động, chưa rõ tên bảng) |

### Ảnh biểu đồ UC
- `exports/hr/screenshots/` — 24 ảnh
- UC tổng quan + 4 biểu đồ phân rã: khoảng image_01–06

### Nhận xét
- **⚠️ Tên entity dùng tiếng Việt** ở pha phân tích (`ChiNhanh`, `CaLamViec`, `KhachHang`, `HoaDon`) trong khi 4 module còn lại dùng tiếng Anh.
- **Tên khách hàng:** `KhachHang` — KHÁC tất cả module khác. ⚠️ X01.
- **Hóa đơn:** `HoaDon` / `tblReceipt` — Booking dùng `Room_receipt`. Tên bảng khác nhau.
- Test case ít (8 TC) so với các module khác, nhưng đủ 4 chức năng.

---

## Bảng cross-module entity

| Khái niệm | Account | Booking | Services | Core | HR |
|---|---|---|---|---|---|
| Khách hàng | `Client` | `Client` | (gián tiếp) | `Customer` | `KhachHang` |
| Nhân viên | `Employee` | `Employee` | `Employee` | (không dùng trực tiếp) | `Employee` |
| Hóa đơn | — | `Room_receipt` | `Room_receipt` | — | `HoaDon` / `tblReceipt` |
| Hạng hội viên | `MembershipTier` | `MemberRanking` | — | `MembershipTier` | — |
| Chi nhánh | — | `Branch` | — | `Branch` | `ChiNhanh` |
| Phòng | — | `Room` | `Room` | `Room` | — |
| Đặt phòng | — | `Room_receipt` | — | `Booking` (ngoại lai) | — |

**Vấn đề cần ghi nhận:**
- **X01 — Khách hàng phân mảnh 3 tên:** `Client` (Account, Booking) / `Customer` (Core) / `KhachHang` (HR). Core và HR nên thống nhất về `Client`.
- **X02 — Hạng hội viên:** `MembershipTier` (Account, Core) vs `MemberRanking` (Booking). Booking nên đổi sang `MembershipTier`.
- **X03 — Entity HR tiếng Việt:** Phase III của HR nên chuẩn hóa tên class/bảng sang tiếng Anh như các module khác.
- **X04 — UC20 xung đột:** Account UC20 = Quản lý tài khoản nhân viên; Core UC20 = Quản lý phòng hát. Theo XÁC ĐỊNH YÊU CẦU tab, đúng là UC20 = tài khoản nhân viên.

---

## Gaps theo rubric (tổng hợp)

| Mã | Vấn đề | Module ảnh hưởng |
|---|---|---|
| R01 | Không có bảng UC chuẩn (ID / Tên / Actor / Mô tả) | Tất cả 5 module |
| R03 | Không có bảng Include/Extend rõ ràng | Tất cả 5 module |
| Services | UC không có số ID (UC0x) | Services |
| X01 | Tên entity Khách hàng không nhất quán | Account/Booking vs Core/HR |
| X02 | Tên entity Hạng hội viên không nhất quán | Account/Core vs Booking |
| X03 | Entity HR dùng tên tiếng Việt ở pha thiết kế | HR |
| X04 | UC20 trùng số giữa Account và Core | Account, Core |
