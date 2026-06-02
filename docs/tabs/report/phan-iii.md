# PHẦN III. TỔNG HỢP CÁC MODULE

---

## 1. Tài khoản & Thành viên

### Danh sách Use Case chính

| ID | Tên UC | Actor chính |
|---|---|---|
| UC01 | Đăng nhập | Thành viên |
| UC02 | Đăng ký | Khách hàng |
| UC03 | Đổi mật khẩu | Thành viên |
| UC04 | Quản lý thông tin cá nhân | Khách hàng |
| UC20 | Quản lý tài khoản nhân viên | Chủ doanh nghiệp |

---

### I. PHÁP XÁC ĐỊNH YÊU CẦU

#### 1. Biểu đồ Use Case tổng quan

<!-- PLACEHOLDER: account_uc_overview -->

#### 2. Biểu đồ Use Case chi tiết

##### UC01 — Đăng nhập

<!-- PLACEHOLDER: account_uc_uc01 -->

##### UC02 — Đăng ký

<!-- PLACEHOLDER: account_uc_uc02 -->

##### UC03 — Đổi mật khẩu

<!-- PLACEHOLDER: account_uc_uc03 -->

##### UC04 — Quản lý thông tin cá nhân

<!-- PLACEHOLDER: account_uc_uc04 -->

##### UC20 — Quản lý tài khoản nhân viên

<!-- PLACEHOLDER: account_uc_uc20 -->

---

### II. PHÁP PHÂN TÍCH

#### 1. Biểu đồ thực thể (Entity Class)

<!-- PLACEHOLDER: account_entity -->

#### 2. Biểu đồ lớp phân tích BCE

<!-- PLACEHOLDER: account_bce -->

#### 3. Biểu đồ tuần tự phân tích

##### UC01 — Đăng nhập

<!-- PLACEHOLDER: account_seq_analysis_uc01 -->

##### UC02 — Đăng ký

<!-- PLACEHOLDER: account_seq_analysis_uc02 -->

##### UC03 — Đổi mật khẩu

<!-- PLACEHOLDER: account_seq_analysis_uc03 -->

##### UC04 — Quản lý thông tin cá nhân

<!-- PLACEHOLDER: account_seq_analysis_uc04 -->

##### UC20 — Quản lý tài khoản nhân viên

<!-- PLACEHOLDER: account_seq_analysis_uc20 -->

---

### III. PHÁP CÀI ĐẶT VÀ KIỂM THỬ

Module Account chỉ bao gồm Phase I (Yêu cầu) và Phase II (Phân tích). Không có phần thiết kế (Phase III) riêng.

**Nhận xét:** Module hoàn chỉnh nhất về yêu cầu — đủ 5 UC, kịch bản v2 + v3, 11 test case có CSDL trước/sau. Kiến trúc single-table inheritance cho User/Client/Employee gọn nhưng cần chú ý khi query phân vai trò.

---

## 2. Quản lý đặt & trả phòng

### Danh sách Use Case chính

| ID | Tên UC | Actor chính |
|---|---|---|
| UC05 | Đặt phòng (online + tại chi nhánh) | Khách hàng, NV lễ tân |
| UC06 | Hủy đặt phòng | Khách hàng, NV lễ tân |
| UC07 | Check-in | NV lễ tân |
| UC08 | Check-out & Thanh toán | NV lễ tân |

---

### I. PHÁP XÁC ĐỊNH YÊU CẦU

#### 1. Biểu đồ Use Case tổng quan

<!-- PLACEHOLDER: booking_uc_overview -->

#### 2. Biểu đồ Use Case chi tiết

##### UC05 — Đặt phòng

<!-- PLACEHOLDER: booking_uc_datphong -->

##### UC06 — Hủy phòng

<!-- PLACEHOLDER: booking_uc_huyphong -->

##### UC07 — Check-in

<!-- PLACEHOLDER: booking_uc_checkin -->

##### UC08 — Check-out & Thanh toán

<!-- PLACEHOLDER: booking_uc_checkout -->

---

### II. PHÁP PHÂN TÍCH

#### 1. Biểu đồ thực thể (Entity Class)

<!-- PLACEHOLDER: booking_entity -->

#### 2. Biểu đồ lớp phân tích BCE

<!-- PLACEHOLDER: booking_bce -->

#### 3. Biểu đồ tuần tự phân tích

##### UC05 — Đặt phòng

<!-- PLACEHOLDER: booking_seq_analysis_datphong -->

##### UC06 — Hủy phòng

<!-- PLACEHOLDER: booking_seq_analysis_huyphong -->

##### UC07 — Check-in

<!-- PLACEHOLDER: booking_seq_analysis_checkin -->

##### UC08 — Check-out & Thanh toán

<!-- PLACEHOLDER: booking_seq_analysis_checkout -->

---

### III. PHÁP THIẾT KẾ

#### 1. Biểu đồ thực thể thiết kế

<!-- PLACEHOLDER: booking_design_entity -->

#### 2. Thiết kế cơ sở dữ liệu (ERD)

<!-- PLACEHOLDER: booking_db -->

#### 3. Biểu đồ lớp thiết kế (MVC)

<!-- PLACEHOLDER: booking_design_class -->

#### 4. Biểu đồ tuần tự thiết kế

##### UC05 — Đặt phòng

<!-- PLACEHOLDER: booking_seq_design_datphong -->

##### UC07 — Check-in

<!-- PLACEHOLDER: booking_seq_design_checkin -->

#### 5. Giao diện (Wireframe)

<!-- PLACEHOLDER: booking_wireframe_01 -->

<!-- PLACEHOLDER: booking_wireframe_02 -->

<!-- PLACEHOLDER: booking_wireframe_03 -->

<!-- PLACEHOLDER: booking_wireframe_04 -->

<!-- PLACEHOLDER: booking_wireframe_05 -->

---

### IV. PHÁP CÀI ĐẶT VÀ KIỂM THỬ

15/15 test case đạt 100%. Lưu ý: `MemberRanking` không nhất quán với `MembershipTier` ở các module khác — cần chuẩn hóa khi tích hợp.

---

## 3. Dịch vụ & Sản phẩm

### Danh sách Use Case chính

| ID | Tên UC | Actor chính |
|---|---|---|
| UC09 | Quản lý order | NV phục vụ |
| UC10 | Báo cáo tình trạng hàng hóa | NV phục vụ |
| UC11 | Quản lý menu | Quản lý chi nhánh |
| UC12 | Quản lý kho | Quản lý chi nhánh |

---

### I. PHÁP XÁC ĐỊNH YÊU CẦU

#### 1. Biểu đồ Use Case tổng quan

<!-- PLACEHOLDER: services_uc_overview -->

#### 2. Biểu đồ Use Case chi tiết

##### UC09 — Quản lý order

<!-- PLACEHOLDER: services_uc_order -->

##### UC10 — Báo cáo tình trạng hàng hóa

<!-- PLACEHOLDER: services_uc_baocao -->

##### UC11 — Quản lý menu

<!-- PLACEHOLDER: services_uc_menu -->

##### UC12 — Quản lý kho

<!-- PLACEHOLDER: services_uc_kho -->

---

### II. PHÁP PHÂN TÍCH

#### 1. Biểu đồ thực thể (Entity Class)

<!-- PLACEHOLDER: services_entity -->

#### 2. Biểu đồ lớp phân tích BCE

<!-- PLACEHOLDER: services_bce -->

#### 3. Biểu đồ tuần tự phân tích

##### UC09 — Tạo order

<!-- PLACEHOLDER: services_seq_analysis_order -->

##### UC10 — Báo cáo tình trạng hàng

<!-- PLACEHOLDER: services_seq_analysis_baocao -->

##### UC11 — Quản lý menu

<!-- PLACEHOLDER: services_seq_analysis_menu -->

##### UC12 — Quản lý kho

<!-- PLACEHOLDER: services_seq_analysis_kho -->

---

### III. PHÁP THIẾT KẾ

#### 1. Biểu đồ thực thể thiết kế

<!-- PLACEHOLDER: services_design_entity -->

#### 2. Thiết kế cơ sở dữ liệu (ERD)

<!-- PLACEHOLDER: services_db -->

#### 3. Biểu đồ lớp thiết kế

##### UC09 — Tạo order

<!-- PLACEHOLDER: services_design_class_order -->

##### UC10 — Báo cáo tình trạng hàng

<!-- PLACEHOLDER: services_design_class_baocao -->

##### UC11 — Quản lý menu

<!-- PLACEHOLDER: services_design_class_menu -->

##### UC12 — Quản lý kho

<!-- PLACEHOLDER: services_design_class_kho -->

#### 4. Biểu đồ tuần tự thiết kế

##### UC09 — Tạo order

<!-- PLACEHOLDER: services_seq_design_order -->

##### UC10 — Báo cáo tình trạng hàng

<!-- PLACEHOLDER: services_seq_design_baocao -->

##### UC11 — Quản lý menu

<!-- PLACEHOLDER: services_seq_design_menu -->

##### UC12 — Quản lý kho

<!-- PLACEHOLDER: services_seq_design_kho -->

#### 5. Giao diện (Wireframe)

<!-- PLACEHOLDER: services_wireframe_01 -->

<!-- PLACEHOLDER: services_wireframe_02 -->

<!-- PLACEHOLDER: services_wireframe_03 -->

<!-- PLACEHOLDER: services_wireframe_04 -->

<!-- PLACEHOLDER: services_wireframe_05 -->

<!-- PLACEHOLDER: services_wireframe_06 -->

<!-- PLACEHOLDER: services_wireframe_07 -->

<!-- PLACEHOLDER: services_wireframe_08 -->

<!-- PLACEHOLDER: services_wireframe_09 -->

<!-- PLACEHOLDER: services_wireframe_10 -->

<!-- PLACEHOLDER: services_wireframe_11 -->

<!-- PLACEHOLDER: services_wireframe_12 -->

<!-- PLACEHOLDER: services_wireframe_13 -->

<!-- PLACEHOLDER: services_wireframe_14 -->

<!-- PLACEHOLDER: services_wireframe_15 -->

<!-- PLACEHOLDER: services_wireframe_16 -->

<!-- PLACEHOLDER: services_wireframe_17 -->

<!-- PLACEHOLDER: services_wireframe_18 -->

<!-- PLACEHOLDER: services_wireframe_19 -->

<!-- PLACEHOLDER: services_wireframe_20 -->

<!-- PLACEHOLDER: services_wireframe_21 -->

---

### IV. PHÁP CÀI ĐẶT VÀ KIỂM THỬ

10/10 test case đạt. Module phong phú nhất về entity (11 bảng). Tích hợp chặt với Booking (Room_receipt) và quản lý kho đầy đủ vòng đời nhập-xuất.

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

---

### I. PHÁP XÁC ĐỊNH YÊU CẦU

#### 1. Biểu đồ Use Case tổng quan

<!-- PLACEHOLDER: core_uc_overview -->

#### 2. Biểu đồ Use Case chi tiết

##### UC16 — Quản lý hệ thống chi nhánh

<!-- PLACEHOLDER: core_uc_uc16 -->

##### UC17 — Quản lý khách hàng toàn hệ thống

<!-- PLACEHOLDER: core_uc_uc17 -->

##### UC18 — Quản lý hạng hội viên

<!-- PLACEHOLDER: core_uc_uc18 -->

##### UC19 — Quản lý danh mục loại phòng

<!-- PLACEHOLDER: core_uc_uc19 -->

##### UC20 — Quản lý phòng hát chi nhánh

<!-- PLACEHOLDER: core_uc_uc20 -->

---

### II. PHÁP PHÂN TÍCH

#### 1. Biểu đồ thực thể (Entity Class)

<!-- PLACEHOLDER: core_entity -->

#### 2. Biểu đồ lớp phân tích BCE

<!-- PLACEHOLDER: core_bce -->

#### 3. Biểu đồ tuần tự phân tích

##### UC16 — Quản lý chi nhánh

<!-- PLACEHOLDER: core_seq_analysis_uc16 -->

##### UC17 — Quản lý khách hàng

<!-- PLACEHOLDER: core_seq_analysis_uc17 -->

##### UC18 — Quản lý hạng hội viên

<!-- PLACEHOLDER: core_seq_analysis_uc18 -->

##### UC19 — Quản lý loại phòng

<!-- PLACEHOLDER: core_seq_analysis_uc19 -->

##### UC20 — Quản lý phòng hát

<!-- PLACEHOLDER: core_seq_analysis_uc20 -->

---

### III. PHÁP THIẾT KẾ

#### 1. Biểu đồ thực thể thiết kế

<!-- PLACEHOLDER: core_design_entity -->

#### 2. Thiết kế cơ sở dữ liệu (ERD)

<!-- PLACEHOLDER: core_db -->

#### 3. Biểu đồ lớp thiết kế

<!-- PLACEHOLDER: core_design_class -->

#### 4. Giao diện (Wireframe)

<!-- PLACEHOLDER: core_wireframe_01 -->

<!-- PLACEHOLDER: core_wireframe_02 -->

---

### IV. PHÁP CÀI ĐẶT VÀ KIỂM THỬ

22/22 test case đạt 100%. Module nền tảng — quản lý danh mục dùng chung toàn chuỗi. Tên entity `Customer` chưa thống nhất với `Client` (Account/Booking). UC20 xung đột số với Account module.

---

## 5. Nhân sự & Báo cáo thống kê

### Danh sách Use Case chính

| ID | Tên UC | Actor chính |
|---|---|---|
| UC11 | Quản lý nhân viên chi nhánh | Quản lý chi nhánh |
| UC13 | Báo cáo số liệu chi nhánh | Quản lý chi nhánh |
| UC14 | Xem thông tin khách hàng chi nhánh | Quản lý chi nhánh |
| UC21 | Tổng hợp báo cáo toàn chuỗi | Chủ doanh nghiệp |

---

### I. PHÁP XÁC ĐỊNH YÊU CẦU

#### 1. Biểu đồ Use Case tổng quan

<!-- PLACEHOLDER: hr_uc_overview -->

#### 2. Biểu đồ Use Case chi tiết

##### UC11 — Quản lý nhân viên chi nhánh

<!-- PLACEHOLDER: hr_uc_nhanvien -->

##### UC13 — Báo cáo số liệu chi nhánh

<!-- PLACEHOLDER: hr_uc_baocao -->

##### UC14 — Xem thông tin khách hàng chi nhánh

<!-- PLACEHOLDER: hr_uc_khachhang -->

##### UC21 — Tổng hợp báo cáo toàn chuỗi

<!-- PLACEHOLDER: hr_uc_tonghop -->

---

### II. PHÁP PHÂN TÍCH

Module Report không có ảnh phân tích riêng (chỉ có design-phase diagrams). Entity class diagram thể hiện mô hình phân tích.

#### 1. Biểu đồ thực thể (Entity Class)

<!-- PLACEHOLDER: hr_entity -->

---

### III. PHÁP THIẾT KẾ

#### 1. Biểu đồ lớp BCE / Thiết kế

<!-- PLACEHOLDER: hr_bce -->

#### 2. Biểu đồ tuần tự thiết kế

##### UC11 — Quản lý nhân viên chi nhánh

<!-- PLACEHOLDER: hr_seq_design_nhanvien -->

##### UC13 — Báo cáo số liệu chi nhánh

<!-- PLACEHOLDER: hr_seq_design_baocao -->

##### UC14 — Xem thông tin khách hàng chi nhánh

<!-- PLACEHOLDER: hr_seq_design_khachhang -->

##### UC21 — Tổng hợp báo cáo toàn chuỗi

<!-- PLACEHOLDER: hr_seq_design_tonghop -->

---

### IV. PHÁP CÀI ĐẶT VÀ KIỂM THỬ

9 test case. Tên entity dùng tiếng Việt ở pha phân tích (`CaLamViec`, `KhachHang`) — cần chuẩn hóa sang tiếng Anh để nhất quán với các module khác.
