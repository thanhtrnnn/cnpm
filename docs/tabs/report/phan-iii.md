# PHẦN III. TỔNG HỢP CÁC MODULE

## 1. Tài khoản & Thành viên

### Danh sách Use Case chính

| ID | Tên UC | Actor chính |
|---|---|---|
| UC01 | Đăng nhập | Thành viên |
| UC02 | Đăng ký | Khách hàng |
| UC03 | Đổi mật khẩu | Thành viên |
| UC04 | Quản lý thông tin cá nhân | Khách hàng |
| UC20 | Quản lý tài khoản nhân viên | Chủ doanh nghiệp |

<!-- PLACEHOLDER: account_uc_overview -->

### Biểu đồ Entity

<!-- PLACEHOLDER: account_entity -->

### Biểu đồ BCE phân tích

<!-- PLACEHOLDER: account_bce -->

### Entity chính

| Class | Bảng CSDL |
|---|---|
| User | tblUser (single-table: Client + Employee + Admin) |
| Client (extends User) | tblUser (role = CLIENT) |
| Employee (extends User) | tblUser (role = EMPLOYEE) |
| MembershipTier | tblMembershipTier |
| OTP | tblOTP |
| LoginSession | tblLoginSession |

**Nhận xét:** Module hoàn chỉnh nhất — đủ 4 pha, kịch bản v2 + v3, 11 test case có CSDL trước/sau. Kiến trúc single-table inheritance cho User/Client/Employee gọn nhưng cần chú ý khi query phân vai trò.

---

## 2. Quản lý đặt & trả phòng

### Danh sách Use Case chính

| ID | Tên UC | Actor chính |
|---|---|---|
| UC05 | Đặt phòng (online + tại chi nhánh) | Khách hàng, NV lễ tân |
| UC06 | Hủy đặt phòng | Khách hàng, NV lễ tân |
| UC07 | Check-in | NV lễ tân |
| UC08 | Check-out & Thanh toán | NV lễ tân |

<!-- PLACEHOLDER: booking_uc_overview -->

### Biểu đồ Entity

<!-- PLACEHOLDER: booking_entity -->

### Biểu đồ BCE phân tích

<!-- PLACEHOLDER: booking_bce -->

### Biểu đồ tuần tự

<!-- PLACEHOLDER: booking_seq -->

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

**Nhận xét:** Mô hình nghiệp vụ rõ ràng, luồng check-in/check-out chi tiết. Lưu ý: `MemberRanking` không nhất quán với `MembershipTier` ở các module khác — cần chuẩn hóa khi tích hợp.

---

## 3. Dịch vụ & Sản phẩm

### Danh sách Use Case chính

| Chức năng | Actor chính |
|---|---|
| Tạo order / Quản lý order | NV phục vụ |
| Báo cáo tình trạng hàng hóa | NV phục vụ |
| Quản lý menu | Quản lý chi nhánh |
| Quản lý kho | Quản lý chi nhánh |

<!-- PLACEHOLDER: services_uc_overview -->

### Biểu đồ Entity

<!-- PLACEHOLDER: services_entity -->

### Biểu đồ BCE phân tích

<!-- PLACEHOLDER: services_bce -->

### Biểu đồ tuần tự

<!-- PLACEHOLDER: services_seq -->

### Entity chính

| Class | Bảng CSDL |
|---|---|
| Employee | tblEmployee |
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

**Nhận xét:** Module phong phú nhất về entity (11 bảng). Tích hợp chặt với Booking (Room_receipt) và quản lý kho đầy đủ vòng đời nhập-xuất. UC chưa được gán số ID — cần bổ sung khi chuẩn hóa.

---

## 4. Quản trị cốt lõi

### Danh sách Use Case chính

| ID | Tên UC | Actor chính |
|---|---|---|
| UC16 | Quản lý hệ thống chi nhánh | Chủ doanh nghiệp |
| UC17 | Quản lý khách hàng toàn hệ thống | Chủ doanh nghiệp |
| UC18 | Quản lý hạng hội viên | Chủ doanh nghiệp |
| UC19 | Quản lý danh mục loại phòng | Chủ doanh nghiệp |
| UC20* | Quản lý phòng hát chi nhánh | Quản lý chi nhánh |

<!-- PLACEHOLDER: core_uc_overview -->

### Biểu đồ Entity

<!-- PLACEHOLDER: core_entity -->

### Biểu đồ BCE phân tích

<!-- PLACEHOLDER: core_bce -->

### Entity chính

| Class | Bảng CSDL |
|---|---|
| Branch | tblBranch |
| Customer | tblCustomer |
| MembershipTier | tblMembershipTier |
| RoomType | tblRoomType |
| Room | tblRoom |
| Booking | tblBooking (ngoại lai) |

**Nhận xét:** Module nền tảng — quản lý danh mục dùng chung toàn chuỗi. Tên entity `Customer` chưa thống nhất với `Client` (Account/Booking). UC20 xung đột số với Account module.

---

## 5. Nhân sự & Báo cáo thống kê

### Danh sách Use Case chính

| ID | Tên UC | Actor chính |
|---|---|---|
| UC11 | Quản lý nhân viên chi nhánh | Quản lý chi nhánh |
| UC13 | Báo cáo số liệu chi nhánh | Quản lý chi nhánh |
| UC14 | Xem thông tin khách hàng chi nhánh | Quản lý chi nhánh |
| UC21 | Tổng hợp báo cáo toàn chuỗi | Chủ doanh nghiệp |

<!-- PLACEHOLDER: hr_uc_overview -->

### Biểu đồ Entity

<!-- PLACEHOLDER: hr_entity -->

### Biểu đồ BCE phân tích

<!-- PLACEHOLDER: hr_bce -->

### Biểu đồ tuần tự

<!-- PLACEHOLDER: hr_seq -->

### Entity chính

| Class | Bảng CSDL |
|---|---|
| Employee | tblEmployee |
| CaLamViec | tblShift |
| ChamCong | tblTimekeeping |
| DanhGiaNhanVien | tblEvaluation |
| QuyetDinh | (chưa rõ tên bảng) |
| KhachHang | tblCustomer |
| HoaDon | tblReceipt |
| BaoCao | (tạo động) |

**Nhận xét:** Đủ 4 chức năng báo cáo và nhân sự. Tên entity dùng tiếng Việt ở pha phân tích (`CaLamViec`, `KhachHang`) — cần chuẩn hóa sang tiếng Anh để nhất quán với các module khác.
