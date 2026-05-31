## III. PHA THIẾT KẾ

### 1. Thiết kế lớp thực thể

#### Bước 1 – Bổ sung thuộc tính id

- NguoiDung: `id : int`
- HangHoiVien: `id : int`
- OTP: `id : int`
- PhienDangNhap: `id : int`
- NhanVien: `id : int`

#### Bước 2 – Thêm kiểu dữ liệu

- NguoiDung: `id : int`, `hoTen : String`, `soDienThoai : String`, `email : String`, `matKhau : String`, `ngayTao : Date`, `diemTichLuy : int`, `trangThai : String`
- HangHoiVien: `id : int`, `tenHang : String`, `diemToiThieu : int`, `moTa : String`, `heSoUuDai : double`
- OTP: `id : int`, `maOTP : String`, `loai : String`, `thoiHanHetHan : Date`, `daXacMinh : boolean`
- PhienDangNhap: `id : int`, `tokenPhien : String`, `thoiGianDangNhap : DateTime`, `thoiGianHetHan : DateTime`, `thietBi : String`
- NhanVien: `id : int`, `hoTen : String`, `vaiTro : String`, `trangThai : String`

#### Bước 3 – Chuyển quan hệ

- NguoiDung `o--` HangHoiVien: aggregation (hạng hội viên là danh mục độc lập)
- NguoiDung `*--` OTP: composition (OTP không tồn tại độc lập)
- NguoiDung `*--` PhienDangNhap: composition (phiên không tồn tại độc lập)

#### Bước 4 – Bổ sung thuộc tính kiểu đối tượng

- NguoiDung: `hangHoiVien : HangHoiVien`
- PhienDangNhap: `nguoiDung : NguoiDung`
- OTP: `nguoiDung : NguoiDung`

#### Biểu đồ lớp thực thể

<!-- PLACEHOLDER: account_entity_class -->
<!-- File: output/diagrams/account_entity_class.png -->

### 2. Thiết kế CSDL

#### Bước 1 – Tạo bảng

| Lớp thực thể | Tên bảng |
|--------------|----------|
| NguoiDung | tblNguoiDung |
| HangHoiVien | tblHangHoiVien |
| OTP | tblOTP |
| PhienDangNhap | tblPhienDangNhap |
| NhanVien | tblNhanVien |

#### Bước 2 – Chuyển kiểu dữ liệu

| Kiểu Java | Kiểu SQL |
|-----------|----------|
| int | integer(10) |
| String | varchar(255) |
| double | double(10) |
| Date | date |
| DateTime | datetime |

#### Bước 3 – Xử lý cardinality

- NguoiDung – HangHoiVien (n-1): tblNguoiDung có FK `tblHangHoiVienMa`
- NguoiDung – OTP (1-n): tblOTP có FK `tblNguoiDungMa`
- NguoiDung – PhienDangNhap (1-n): tblPhienDangNhap có FK `tblNguoiDungMa`

#### Bước 4 – PK/FK

- PK: `ma : integer(10) <<PK>>`
- FK: `tbl[TenBangCha]Ma : integer(10) <<FK>>`

#### Biểu đồ ERD

<!-- PLACEHOLDER: account_erd -->
<!-- File: output/diagrams/account_erd.png -->

### 3. Wireframe

<!-- PLACEHOLDER: WIREFRAMES -->
<!-- Wireframes sẽ được render thành monospace frames trong DOCX -->

#### Màn hình 1: LoginPage

```
+--------------------------------------------------+
|              Đăng nhập                           |
|                                                  |
|  SĐT / Email: [________________________]         |
|  Mật khẩu:    [________________________]         |
|                                                  |
|  [Đăng nhập]                                     |
|  Quên mật khẩu?  |  Đăng ký mới                 |
+--------------------------------------------------+
```

#### Màn hình 2: RegisterPage

```
+--------------------------------------------------+
|              Đăng ký tài khoản                    |
|                                                  |
|  Họ và tên:      [________________________]      |
|  Số điện thoại:   [________________________]      |
|  Email:           [________________________]      |
|  Mật khẩu:       [________________________]      |
|  Xác nhận MK:    [________________________]      |
|                                                  |
|  [Tiếp tục]                     [Hủy]           |
+--------------------------------------------------+
```

#### Màn hình 3: OTPVerifyPage

```
+--------------------------------------------------+
|           Xác nhận OTP                           |
|                                                  |
|  Mã OTP đã gửi đến 098****321                   |
|                                                  |
|  [__][__][__][__][__][__]                        |
|                                                  |
|  [Xác nhận]                                      |
|  Gửi lại OTP (60s)                              |
+--------------------------------------------------+
```

#### Màn hình 4: ChangePasswordPage

```
+--------------------------------------------------+
|           Đổi mật khẩu                           |
|                                                  |
|  Mật khẩu hiện tại: [________________________]  |
|  Mật khẩu mới:      [________________________]  |
|  Xác nhận MK mới:   [________________________]  |
|                                                  |
|  [Lưu thay đổi]              [Hủy]              |
+--------------------------------------------------+
```

#### Màn hình 5: ProfilePage

```
+--------------------------------------------------+
|           Hồ sơ cá nhân                          |
|                                                  |
|  Họ và tên:      Nguyễn Văn An                  |
|  Số điện thoại:   0912345678                     |
|  Email:           vana@email.com                 |
|  Hạng hội viên:  Bạc (1.250 điểm)              |
|  Ngày tham gia:   15/03/2024                     |
|                                                  |
|  [Chỉnh sửa thông tin]    [Đổi mật khẩu]        |
+--------------------------------------------------+
```

#### Màn hình 6: StaffManagePage

```
+--------------------------------------------------+
|        Quản lý tài khoản nhân viên               |
|                                                  |
|  [Thêm nhân viên]                                |
|                                                  |
| +----------+----------+----------+-------+-------+
| | hoTen    | vaiTro   | chiNhanh | trangThai| ... |
| |----------|----------|----------|---------|-----|
| | Trần A   | Lễ tân   | Q1       | Đang LD |     |
| | Lê B     | Phục vụ  | Q3       | Đang LD |     |
| +----------+----------+----------+-------+-------+
|                                                  |
|  [Sửa]  [Xóa]                                   |
+--------------------------------------------------+
```

### 4. MVC class diagram

Mô hình MVC thiết kế theo kiến trúc BCE:

**Boundary:** LoginPage, RegisterPage, OTPVerifyPage, ChangePasswordPage, ProfilePage, StaffManagePage

**Control:** AuthController, UserController

**Entity:** NguoiDung, HangHoiVien, OTP, PhienDangNhap, NhanVien

<!-- PLACEHOLDER: account_mvc_class -->
<!-- File: output/diagrams/account_mvc_class.png -->

### 5. Biểu đồ tuần tự thiết kế

#### Đăng nhập

<!-- PLACEHOLDER: account_seq_login -->
<!-- File: output/diagrams/account_seq_login.png -->

#### Đăng ký

<!-- PLACEHOLDER: account_seq_register -->
<!-- File: output/diagrams/account_seq_register.png -->

#### Đổi mật khẩu

<!-- PLACEHOLDER: account_seq_changepw -->
<!-- File: output/diagrams/account_seq_changepw.png -->

#### Quản lý TTCN

<!-- PLACEHOLDER: account_seq_profile -->
<!-- File: output/diagrams/account_seq_profile.png -->

#### Quản lý nhân viên

<!-- PLACEHOLDER: account_seq_staff -->
<!-- File: output/diagrams/account_seq_staff.png -->
