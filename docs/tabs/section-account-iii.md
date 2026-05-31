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
┌──────────────────────────────────────────────┐
│              Đăng nhập                       │
│                                              │
│  SĐT / Email: [________________________]     │
│  Mật khẩu:    [________________________]     │
│                                              │
│  [Đăng nhập]                                 │
│  Quên mật khẩu?  |  Đăng ký mới             │
└──────────────────────────────────────────────┘
```

#### Màn hình 2: RegisterPage

```
┌──────────────────────────────────────────────┐
│              Đăng ký tài khoản                │
│                                              │
│  Họ và tên:      [________________________]  │
│  Số điện thoại:   [________________________]  │
│  Email:           [________________________]  │
│  Mật khẩu:       [________________________]  │
│  Xác nhận MK:    [________________________]  │
│                                              │
│  [Tiếp tục]                 [Hủy]           │
└──────────────────────────────────────────────┘
```

#### Màn hình 3: OTPVerifyPage

```
┌──────────────────────────────────────────────┐
│           Xác nhận OTP                       │
│                                              │
│  Mã OTP đã gửi đến 098****321               │
│                                              │
│  [__][__][__][__][__][__]                    │
│                                              │
│  [Xác nhận]                                  │
│  Gửi lại OTP (60s)                          │
└──────────────────────────────────────────────┘
```

#### Màn hình 4: ChangePasswordPage

```
┌──────────────────────────────────────────────┐
│           Đổi mật khẩu                       │
│                                              │
│  Mật khẩu hiện tại: [________________________]│
│  Mật khẩu mới:      [________________________]│
│  Xác nhận MK mới:   [________________________]│
│                                              │
│  [Lưu thay đổi]          [Hủy]              │
└──────────────────────────────────────────────┘
```

#### Màn hình 5: ProfilePage

```
┌──────────────────────────────────────────────┐
│           Hồ sơ cá nhân                      │
│                                              │
│  Họ và tên:      Nguyễn Văn An              │
│  Số điện thoại:   0912345678                 │
│  Email:           vana@email.com             │
│  Hạng hội viên:  Bạc (1.250 điểm)          │
│  Ngày tham gia:   15/03/2024                 │
│                                              │
│  [Chỉnh sửa thông tin]  [Đổi mật khẩu]      │
└──────────────────────────────────────────────┘
```

#### Màn hình 6: StaffManagePage

```
┌──────────────────────────────────────────────┐
│        Quản lý tài khoản nhân viên           │
│                                              │
│  [Thêm nhân viên]                            │
│                                              │
│ ┌──────┬────────┬──────────┬──────────┐      │
│ │ Họ tên│ Vai trò│ Trạng thái│ ...     │      │
│ │ Trần A│ Lễ tân │ Đang LD  │         │      │
│ │ Lê B  │ Phục vụ│ Đang LD  │         │      │
│ └──────┴────────┴──────────┴──────────┘      │
│                                              │
│  [Sửa]  [Xóa]                               │
└──────────────────────────────────────────────┘
```

### 4. MVC class diagram

Mô hình thiết kế theo kiến trúc MVC (Boundary – Control – Entity):

**Boundary:** LoginPage, RegisterPage, OTPVerifyPage, ChangePasswordPage, ProfilePage, StaffManagePage

**Control:** AuthController, ProfileController, StaffController

**Entity:** NguoiDung, HangHoiVien, OTP, PhienDangNhap, NhanVien

**Quy trình xác định chữ ký hàm Controller:**

a) Đăng nhập => `login()`
- Input: sdt, matKhau
- Output: NguoiDung + Session
- Ứng viên tham số vào:
  - `login(sdt: String, matKhau: String)` → chọn (gom nhóm tham số)
- Ứng viên tham số ra:
  - `login(): void` → loại (cần trả về thông tin đăng nhập)
  - `login(): NguoiDung` → chọn (trả về thông tin người dùng)

b) Đăng ký => `register()`
- Input: hoTen, sdt, email, matKhau
- Output: NguoiDung (vừa tạo)
- Ứng viên tham số vào:
  - `register(hoTen: String, sdt: String, email: String, matKhau: String)` → chọn
- Ứng viên tham số ra:
  - `register(): NguoiDung` → chọn

c) Xác minh OTP => `verifyOTP()`
- Input: otp
- Output: boolean
- Ứng viên tham số vào:
  - `verifyOTP(otp: String)` → chọn
- Ứng viên tham số ra:
  - `verifyOTP(): boolean` → chọn (cần biết đúng/sai)

d) Đổi mật khẩu => `changePassword()`
- Input: mkHienTai, mkMoi
- Output: boolean
- Ứng viên tham số vào:
  - `changePassword(mkHienTai: String, mkMoi: String)` → chọn
- Ứng viên tham số ra:
  - `changePassword(): boolean` → chọn

e) Xem hồ sơ => `getProfile()`
- Input: userId
- Output: NguoiDung
- Ứng viên tham số vào:
  - `getProfile(userId: int)` → chọn
- Ứng viên tham số ra:
  - `getProfile(): NguoiDung` → chọn

f) Cập nhật hồ sơ => `updateProfile()`
- Input: userId, hoTen, email
- Output: NguoiDung
- Ứng viên tham số vào:
  - `updateProfile(userId: int, hoTen: String, email: String)` → chọn
- Ứng viên tham số ra:
  - `updateProfile(): NguoiDung` → chọn

g) Xem danh sách NV => `getStaffList()`
- Input: (không có)
- Output: List\<NhanVien\>
- Ứng viên tham số vào:
  - `getStaffList()` → chọn
- Ứng viên tham số ra:
  - `getStaffList(): List<NhanVien>` → chọn

h) Thêm NV => `addStaff()`
- Input: hoTen, vaiTro
- Output: NhanVien
- Ứng viên tham số vào:
  - `addStaff(hoTen: String, vaiTro: String)` → chọn
- Ứng viên tham số ra:
  - `addStaff(): NhanVien` → chọn

i) Sửa NV => `updateStaff()`
- Input: id, hoTen, vaiTro
- Output: NhanVien
- Ứng viên tham số vào:
  - `updateStaff(id: int, hoTen: String, vaiTro: String)` → chọn
- Ứng viên tham số ra:
  - `updateStaff(): NhanVien` → chọn

j) Xóa NV => `deleteStaff()`
- Input: id
- Output: boolean
- Ứng viên tham số vào:
  - `deleteStaff(id: int)` → chọn
- Ứng viên tham số ra:
  - `deleteStaff(): boolean` → chọn (cần biết thành công/thất bại)

<!-- PLACEHOLDER: account_dao_class -->
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
