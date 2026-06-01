## II. PHA PHÂN TÍCH

### 1. Kịch bản chuẩn

#### UC01 – Đăng nhập

| Use case | Đăng nhập |
|----------|----------|
| Actor | Khách hàng, Nhân viên |
| Tiền điều kiện | Người dùng chưa đăng nhập. Tài khoản đã tồn tại trong hệ thống. |
| Hậu điều kiện | Người dùng được xác thực thành công, hệ thống tạo session và chuyển hướng đến trang chủ tương ứng. |
| Kịch bản chính | 1. Người dùng truy cập màn hình "Đăng nhập".<br>2. Hệ thống hiển thị form gồm: Ô nhập SĐT/Email, Ô nhập Mật khẩu, Nút [Đăng nhập], Liên kết "Quên mật khẩu?" / "Đăng ký".<br>3. Người dùng nhập thông tin: SĐT = "0912345678", Mật khẩu = "Abc@1234".<br>4. Người dùng nhấn [Đăng nhập].<br>5. Hệ thống kiểm tra định dạng đầu vào.<br>6. Hệ thống truy vấn CSDL: tìm tài khoản, so sánh mật khẩu đã mã hóa.<br>7. Xác thực thành công, tạo session với vai trò "Khách hàng".<br>8. Chuyển hướng đến trang chủ, hiển thị "Đăng nhập thành công. Xin chào, Nguyễn Văn A!". |
| Ngoại lệ | 6.1. Tài khoản không tồn tại: Hiển thị "Tài khoản không tồn tại. Vui lòng kiểm tra lại."<br>6.2. Mật khẩu không khớp: Hiển thị "Mật khẩu không chính xác. Còn [N] lần thử." Sau 5 lần sai → khóa 15 phút. |

#### UC02 – Đăng ký

| Use case | Đăng ký |
|----------|--------|
| Actor | Khách hàng |
| Tiền điều kiện | Người dùng chưa có tài khoản. Hệ thống hoạt động bình thường. |
| Hậu điều kiện | Tài khoản mới được tạo, hạng "Thường", đăng nhập tự động. |
| Kịch bản chính | 1. Người dùng nhấn "Đăng ký" từ màn hình đăng nhập.<br>2. Hệ thống hiển thị form: Họ tên, SĐT, Email, Mật khẩu, Xác nhận MK.<br>3. Người dùng điền: Họ tên = "Nguyễn Thị Bình", SĐT = "0987654321", Email = "binh.nt@email.com", MK = "Pass@2025".<br>4. Người dùng nhấn [Tiếp tục].<br>5. Hệ thống kiểm tra định dạng, SĐT và email chưa tồn tại.<br>6. Hệ thống gửi OTP 6 chữ số đến SĐT.<br>7. Hiển thị màn hình "Xác nhận OTP".<br>8. Người dùng nhập OTP = "482917" và nhấn [Xác nhận].<br>9. Hệ thống xác minh OTP đúng và còn hiệu lực (≤ 5 phút).<br>10. Tạo tài khoản mới, hạng "Thường", điểm = 0.<br>11. Đăng nhập tự động, hiển thị "Đăng ký thành công! Chào mừng Nguyễn Thị Bình." |
| Ngoại lệ | 5.1. SĐT đã tồn tại: "SĐT này đã được sử dụng."<br>5.2. MK không khớp: Highlight ô xác nhận MK, "Mật khẩu không khớp."<br>9.1. OTP sai: "Mã OTP không đúng. Vui lòng thử lại." (tối đa 3 lần)<br>9.2. OTP hết hạn: "Mã OTP đã hết hạn." Nhấn "Gửi lại OTP". |

#### UC03 – Đổi mật khẩu

| Use case | Đổi mật khẩu |
|----------|-------------|
| Actor | Khách hàng, Nhân viên (đã đăng nhập) |
| Tiền điều kiện | Người dùng đã đăng nhập thành công. |
| Hậu điều kiện | Mật khẩu mới được lưu (bcrypt). Tất cả session khác bị thu hồi. |
| Kịch bản chính | 1. Người dùng truy cập "Bảo mật" trong cài đặt.<br>2. Hiển thị form: MK hiện tại, MK mới, Xác nhận MK mới.<br>3. Người dùng nhập: MK hiện tại = "Abc@1234", MK mới = "NewPass@2025", xác nhận = "NewPass@2025".<br>4. Nhấn [Lưu thay đổi].<br>5. Hệ thống xác minh MK hiện tại khớp CSDL.<br>6. Kiểm tra MK mới: độ dài ≥ 8, có chữ hoa/thường/số/đặc biệt.<br>7. Kiểm tra MK mới ≠ MK hiện tại.<br>8. Mã hóa (bcrypt) và cập nhật.<br>9. Thu hồi tất cả session, hiển thị "Đổi mật khẩu thành công. Vui lòng đăng nhập lại."<br>10. Chuyển hướng về màn hình Đăng nhập. |
| Ngoại lệ | 5.1. MK hiện tại sai: "Mật khẩu hiện tại không chính xác."<br>6.1. MK mới không đủ mạnh: Highlight ô, hiển thị yêu cầu còn thiếu.<br>7.1. MK mới trùng MK cũ: "Mật khẩu mới không được trùng mật khẩu hiện tại." |

#### UC04 – Quản lý thông tin cá nhân

| Use case | Quản lý thông tin cá nhân |
|----------|--------------------------|
| Actor | Khách hàng (đã đăng nhập) |
| Tiền điều kiện | Khách hàng đã đăng nhập. Tài khoản tồn tại trong CSDL. |
| Hậu điều kiện | Thông tin cập nhật trong CSDL, hiển thị ngay trên giao diện. |
| Kịch bản chính | 1. Khách hàng nhấn vào ảnh đại diện / tên tài khoản.<br>2. Hệ thống hiển thị "Hồ sơ cá nhân":<br><table><tr><th>Họ tên</th><th>SĐT</th><th>Email</th><th>Hạng hội viên</th><th>Điểm tích lũy</th><th>Ngày tham gia</th></tr><tr><td>Nguyễn Văn An</td><td>0912345678</td><td>vana@email.com</td><td>Bạc</td><td>1.250</td><td>15/03/2024</td></tr></table><br>3. Nhấn [Chỉnh sửa thông tin].<br>4. Chuyển sang chế độ chỉnh sửa: Họ tên, Email có thể nhập; SĐT bị khóa.<br>5. Cập nhật: Họ tên = "Nguyễn Văn An", Email = "vanan@newemail.com".<br>6. Nhấn [Lưu thay đổi].<br>7. Kiểm tra email hợp lệ và chưa được dùng.<br>8. Cập nhật vào CSDL.<br>9. Hiển thị "Cập nhật thành công!" và quay về chế độ xem. |
| Ngoại lệ | 7.1. Email đã được dùng: "Email này đã được đăng ký bởi tài khoản khác."<br>3.1. Thay đổi SĐT: Yêu cầu xác minh OTP gửi đến SĐT hiện tại → SĐT mới → OTP mới. |

#### UC20 – Quản lý tài khoản nhân viên

| Use case | Quản lý tài khoản nhân viên |
|----------|----------------------------|
| Actor | Chủ Doanh nghiệp (Admin) |
| Tiền điều kiện | Admin đã đăng nhập. Có quyền quản lý tài khoản nhân viên toàn hệ thống. |
| Hậu điều kiện | Tài khoản nhân viên được tạo/sửa/xóa trong CSDL. |
| Kịch bản chính | 1. Quản lý truy cập "Quản lý nhân viên".<br>2. Hệ thống hiển thị danh sách nhân viên:<br><table><tr><th>Họ tên</th><th>Vai trò</th><th>Trạng thái</th></tr><tr><td>Trần Văn A</td><td>Lễ tân</td><td>Đang làm việc</td></tr><tr><td>Lê Thị B</td><td>Phục vụ</td><td>Đang làm việc</td></tr><tr><td>Phạm Văn C</td><td>Quản lý</td><td>Đang làm việc</td></tr></table><br>3a. Thêm nhân viên: Nhấn [Thêm] → Nhập thông tin → Lưu.<br>3b. Sửa nhân viên: Chọn nhân viên → Chỉnh sửa → Lưu.<br>3c. Xóa nhân viên: Chọn nhân viên → Xác nhận xóa → Hệ thống chuyển trạng thái "Đã nghỉ". |
| Ngoại lệ | 3.1. SĐT đã tồn tại: "SĐT này đã được sử dụng."<br>3.2. Nhân viên đang xử lý order: Không thể xóa, hiển thị cảnh báo. |

### 2. Mô hình hóa lớp

**Bước 1 – Mô tả chức năng bằng đoạn văn xuôi**

Hệ thống cho phép khách hàng đăng ký tài khoản hội viên mới bằng cách cung cấp họ tên, số điện thoại, email và mật khẩu; sau đó xác minh số điện thoại qua mã OTP trước khi hoàn tất đăng ký. Mỗi tài khoản gắn liền với một hạng hội viên (Thường, Bạc, Vàng, Kim Cương) dựa trên điểm tích lũy. Người dùng sau khi đăng nhập có thể xem và cập nhật thông tin cá nhân như họ tên và email, hoặc thực hiện đổi mật khẩu bằng cách xác minh mật khẩu cũ rồi nhập mật khẩu mới. Hệ thống ghi nhận các phiên đăng nhập để phục vụ bảo mật và thu hồi phiên khi đổi mật khẩu. Ngoài ra, chủ doanh nghiệp có quyền quản lý tài khoản nhân viên: tạo, chỉnh sửa và xóa tài khoản nhân viên trong hệ thống.

**Bước 2 + 3 – Trích danh từ và đánh giá**

▪ Hệ thống → loại: quá chung, không phải thực thể nghiệp vụ
▪ Khách hàng → lớp User: hoTen, soDienThoai, email, matKhau, ngayTao
▪ Tài khoản → thuộc về User (gộp vào User, tránh tách thừa)
▪ Họ tên → thuộc tính của User
▪ Số điện thoại → thuộc tính của User (dùng làm username đăng nhập)
▪ Email → thuộc tính của User
▪ Mật khẩu → thuộc tính của User (lưu dạng mã hóa bcrypt)
▪ Ngày tham gia → thuộc tính ngayTao của User
▪ Hạng hội viên → lớp MembershipTier: tenHang, diemToiThieu, moTa, heSoUuDai
▪ Điểm tích lũy → thuộc tính diemTichLuy của User
▪ Mã OTP → lớp OTP: maOTP, loai (DANG_KY/DOI_SDT), thoiHanHetHan, daXacMinh
▪ Phiên đăng nhập → lớp LoginSession: tokenPhien, thoiGianDangNhap, thoiGianHetHan, thietBi
▪ Lịch sử → loại: quá chung → cụ thể là LoginSession đã đủ
▪ Danh sách → loại: không phải thực thể
▪ Giao diện → loại: là Boundary, không phải Entity
▪ Nhân viên → lớp Employee: hoTen, vaiTro, chiNhanh, trangThai
▪ Chủ doanh nghiệp → loại: actor, không phải thực thể dữ liệu

**Bước 4 – Xác định quan hệ số lượng**

▪ 1 User có 1 MembershipTier → User – MembershipTier: n – 1
(nhiều người dùng có thể có cùng hạng)
▪ 1 User có nhiều OTP → User – OTP: 1 – n
(mỗi lần đăng ký/đổi SĐT tạo 1 OTP mới)
▪ 1 User có nhiều LoginSession → User – LoginSession: 1 – n
(người dùng có thể đăng nhập trên nhiều thiết bị)

**Bước 5 – Bổ sung quan hệ**

User gắn composition với OTP: một OTP không tồn tại độc lập nếu không có User tương ứng (khi xóa User thì xóa theo tất cả OTP). Tương tự, LoginSession không tồn tại độc lập khỏi User. Quan hệ với MembershipTier là aggregation: MembershipTier là dữ liệu danh mục tồn tại độc lập với User. Employee là lớp riêng biệt, không kế thừa từ User.

<!-- PLACEHOLDER: account_entity_analysis -->

### 3. Biểu đồ lớp phân tích

**Kiến trúc chọn: React** ( Boundary class dùng hậu tố Page. Controller xử lý nghiệp vụ. Method names tiếng Việt ở pha phân tích )

**Bước 1 – Lớp Boundary từ giao diện**

| Giao diện | Lớp Boundary | Loại |
|-----------|-------------|------|
| Màn hình Đăng nhập | LoginPage | Page |
| Màn hình Đăng ký | RegisterPage | Page |
| Màn hình Xác nhận OTP | OTPVerifyPage | Page |
| Màn hình Đổi mật khẩu | ChangePasswordPage | Page |
| Trang Hồ sơ cá nhân | ProfilePage | Page |
| Trang Quản lý nhân viên | StaffManagePage | Page |

**Bước 2 – Phân loại thành phần giao diện**

LoginPage: inSDT, inMatKhau, subDangNhap, subQuenMatKhau, subDangKy
RegisterPage: inHoTen, inSDT, inEmail, inMatKhau, inXacNhanMK, subTiepTuc, subHuy
OTPVerifyPage: inOTP, subXacNhan, subGuiLai
ChangePasswordPage: inMKHienTai, inMKMoi, inXacNhanMKMoi, subLuu, subHuy
ProfilePage: outHoTen, outSDT, outEmail, outHang, outDiem, subChinhSua, subDoiMK
StaffManagePage: outDSEmployee, outsubChonNV, subThem, subSua, subXoa

**Bước 3 – Phương thức cho mỗi chức năng**

[1]. Giao diện LoginPage → lớp LoginPage
Phương thức: `dangNhap()` ← tên tiếng Việt, ngôn ngữ tự nhiên
Input: sdt, matKhau
Output: Session (token, vaiTro)
Lớp chủ thể: User

[2]. Giao diện RegisterPage → lớp RegisterPage
Phương thức: `dangKy()`
Input: hoTen, sdt, email, matKhau
Output: User (vừa tạo)
Lớp chủ thể: User

[3]. Giao diện OTPVerifyPage → lớp OTPVerifyPage
Phương thức: `xacMinhOTP()`
Input: maOTP
Output: boolean (đúng/sai)
Lớp chủ thể: OTP

[4]. Giao diện ChangePasswordPage → lớp ChangePasswordPage
Phương thức: `doiMatKhau()`
Input: mkHienTai, mkMoi
Output: boolean (thành công/thất bại)
Lớp chủ thể: User

[5]. Giao diện ProfilePage → lớp ProfilePage
Phương thức: `xemHoSo()`
Input: userId
Output: User (thông tin hồ sơ)
Lớp chủ thể: User

[6]. Giao diện ProfilePage → lớp ProfilePage
Phương thức: `capNhatHoSo()`
Input: userId, hoTen, email
Output: User (đã cập nhật)
Lớp chủ thể: User

[7]. Giao diện StaffManagePage → lớp StaffManagePage
Phương thức: `xemDanhSachNV()`
Input: (không có — tải toàn bộ)
Output: List\<Employee\>
Lớp chủ thể: Employee

[8]. Giao diện StaffManagePage → lớp StaffManagePage
Phương thức: `themNV()`
Input: hoTen, vaiTro
Output: Employee (vừa tạo)
Lớp chủ thể: Employee

[9]. Giao diện StaffManagePage → lớp StaffManagePage
Phương thức: `suaNV()`
Input: id, hoTen, vaiTro
Output: Employee (đã cập nhật)
Lớp chủ thể: Employee

[10]. Giao diện StaffManagePage → lớp StaffManagePage
Phương thức: `xoaNV()`
Input: id
Output: boolean (thành công/thất bại)
Lớp chủ thể: Employee

<!-- PLACEHOLDER: account_bce_analysis -->

### 4. Biểu đồ tuần tự phân tích

#### UC01 – Đăng nhập

```plantuml
@startuml
title Đăng nhập – Tuần tự Phân tích

actor "Khách hàng" as KH
participant "LoginPage\n<<Boundary>>" as B1
participant "AuthController\n<<Control>>" as C1
entity "User\n<<Entity>>" as E1

KH -> B1 : 1: truy cập màn hình Đăng nhập
activate B1
B1 --> KH : 2: hiển thị form đăng nhập
KH -> B1 : 3: nhập SĐT + Mật khẩu + nhấn [Đăng nhập]
B1 -> C1 : 4: dangNhap(sdt, matKhau)
activate C1
C1 -> E1 : 5: timTheoSDT(sdt)
activate E1
E1 --> C1 : 6: User
deactivate E1
C1 -> C1 : 7: kiemTraMatKhau(matKhau, hash)
C1 --> B1 : 8: trả về User + Session
deactivate C1
B1 --> KH : 9: chuyển hướng trang chủ, hiển thị "Đăng nhập thành công"
deactivate B1

alt Ngoại lệ: tài khoản không tồn tại
  E1 --> C1 : trả về null
  C1 --> B1 : trả về null
  B1 --> KH : hiển thị "Tài khoản không tồn tại"
end

alt Ngoại lệ: mật khẩu sai
  C1 --> B1 : trả về sai mật khẩu
  B1 --> KH : hiển thị "Mật khẩu không chính xác. Còn [N] lần thử"
end
@enduml
```

**Kịch bản phiên bản 2 – UC01 Đăng nhập**

1. Khách hàng truy cập URL hệ thống để mở màn hình Đăng nhập.
2. Lớp LoginPage hiển thị form gồm ô nhập SĐT/Email, ô nhập Mật khẩu, nút [Đăng nhập], liên kết "Quên mật khẩu?" / "Đăng ký".
3. Khách hàng nhập SĐT = "0912345678" và Mật khẩu = "Abc@1234".
4. Khách hàng nhấn nút [Đăng nhập].
5. Lớp LoginPage gọi phương thức `dangNhap()` của AuthController với tham số sdt, matKhau.
6. AuthController gọi phương thức `findBySDT()` của User để tìm tài khoản theo SĐT.
7. User trả về đối tượng User cho AuthController.
8. AuthController gọi `checkPassword()` để so sánh mật khẩu.
9. AuthController trả kết quả về cho LoginPage.
10. Lớp LoginPage hiển thị "Đăng nhập thành công. Xin chào, Nguyễn Văn A!" và chuyển hướng trang chủ.

**Ngoại lệ: tài khoản không tồn tại**
- User trả về null (không tìm thấy tài khoản).
- AuthController trả về null cho LoginPage.
- LoginPage hiển thị "Tài khoản không tồn tại. Vui lòng kiểm tra lại."

**Ngoại lệ: mật khẩu sai**
- AuthController trả về sai mật khẩu cho LoginPage.
- LoginPage hiển thị "Mật khẩu không chính xác. Còn [N] lần thử."

#### UC02 – Đăng ký

```plantuml
@startuml
title Đăng ký – Tuần tự Phân tích

actor "Khách hàng" as KH
participant "RegisterPage\n<<Boundary>>" as B1
participant "OTPVerifyPage\n<<Boundary>>" as B2
participant "AuthController\n<<Control>>" as C1
entity "User\n<<Entity>>" as E1
entity "OTP\n<<Entity>>" as E2

KH -> B1 : 1: nhấn "Đăng ký"
activate B1
B1 --> KH : 2: hiển thị form đăng ký
KH -> B1 : 3: nhập thông tin + nhấn [Tiếp tục]
B1 -> C1 : 4: dangKy(hoTen, sdt, email, matKhau)
activate C1
C1 -> E1 : 5: existsBySDT(sdt)
activate E1
E1 --> C1 : 6: true/false
deactivate E1
C1 -> E1 : 7: existsByEmail(email)
activate E1
E1 --> C1 : 8: true/false
deactivate E1
C1 -> E1 : 9: createUser()
activate E1
E1 --> C1 : 10: User
deactivate E1
C1 -> E2 : 11: guiOTP(sdt, DANG_KY)
activate E2
E2 --> C1 : 12: OTP đã gửi
deactivate E2
C1 --> B1 : 13: trả về User
deactivate C1
B1 --> KH : 14: hiển thị form xác nhận OTP
deactivate B1

KH -> B2 : 15: nhập OTP = "482917"
activate B2
B2 -> C1 : 16: xacMinhOTP(otp)
activate C1
C1 -> E2 : 17: verify(otp)
activate E2
E2 --> C1 : 18: true
deactivate E2
C1 -> E1 : 19: luuTaiKhoan()
activate E1
E1 --> C1 : 20: thanh cong
deactivate E1
C1 --> B2 : 21: thanh cong
deactivate C1
B2 --> KH : 22: "Đăng ký thành công! Chào mừng Nguyễn Thị Bình."
deactivate B2
@enduml
```

**Kịch bản phiên bản 2 – UC02 Đăng ký**

1. Khách hàng nhấn liên kết "Đăng ký" từ màn hình đăng nhập.
2. Lớp RegisterPage hiển thị form gồm: Họ tên, SĐT, Email, Mật khẩu, Xác nhận MK.
3. Khách hàng nhập: Họ tên = "Nguyễn Thị Bình", SĐT = "0987654321", Email = "binh.nt@email.com", MK = "Pass@2025".
4. Khách hàng nhấn [Tiếp tục].
5. RegisterPage gọi `dangKy()` của AuthController với các tham số hoTen, sdt, email, matKhau.
6. AuthController gọi `existsBySDT()` của User để kiểm tra SĐT chưa tồn tại.
7. AuthController gọi `existsByEmail()` của User để kiểm tra email chưa tồn tại.
8. AuthController gọi `createUser()` để tạo tài khoản mới.
9. AuthController gọi `guiOTP()` để gửi OTP đến SĐT.
10. AuthController trả kết quả về RegisterPage.
11. RegisterPage hiển thị form xác nhận OTP.
12. Khách hàng nhập OTP = "482917" và nhấn [Xác nhận].
13. OTPVerifyPage gọi `xacMinhOTP(otp)` của AuthController.
14. AuthController gọi `verify()` của OTP để kiểm tra OTP đúng và còn hiệu lực.
15. AuthController gọi `luuTaiKhoan()` để hoàn tất đăng ký.
16. Hiển thị "Đăng ký thành công! Chào mừng Nguyễn Thị Bình."

**Ngoại lệ: SĐT đã tồn tại**
- AuthController nhận false từ `existsBySDT()`.
- RegisterPage hiển thị "SĐT này đã được sử dụng."

**Ngoại lệ: OTP sai**
- AuthController nhận false từ `verify()`.
- OTPVerifyPage hiển thị "Mã OTP không đúng. Vui lòng thử lại."

#### UC03 – Đổi mật khẩu

```plantuml
@startuml
title Đổi mật khẩu – Tuần tự Phân tích

actor "Người dùng" as User
participant "ChangePasswordPage\n<<Boundary>>" as B1
participant "AuthController\n<<Control>>" as C1
entity "User\n<<Entity>>" as E1

User -> B1 : 1: truy cập "Bảo mật"
activate B1
B1 --> User : 2: hiển thị form đổi mật khẩu
User -> B1 : 3: nhập MK hiện tại, MK mới + nhấn [Lưu]
B1 -> C1 : 4: doiMatKhau(mkHienTai, mkMoi)
activate C1
C1 -> E1 : 5: findByToken(session)
activate E1
E1 --> C1 : 6: User
deactivate E1
C1 -> C1 : 7: checkPassword(mkHienTai, hash)
C1 -> C1 : 8: hashPassword(mkMoi)
C1 -> E1 : 9: updatePassword(hash)
activate E1
E1 --> C1 : 10: thanh cong
deactivate E1
C1 -> E1 : 11: revokeAllSessions()
activate E1
E1 --> C1 : 12: thanh cong
deactivate E1
C1 --> B1 : 13: thanh cong
deactivate C1
B1 --> User : 14: "Đổi mật khẩu thành công. Vui lòng đăng nhập lại."
deactivate B1
@enduml
```

**Kịch bản phiên bản 2 – UC03 Đổi mật khẩu**

1. Người dùng truy cập mục "Bảo mật" trong cài đặt tài khoản.
2. Lớp ChangePasswordPage hiển thị form: MK hiện tại, MK mới, Xác nhận MK mới.
3. Người dùng nhập: MK hiện tại = "Abc@1234", MK mới = "NewPass@2025", xác nhận = "NewPass@2025".
4. Người dùng nhấn [Lưu thay đổi].
5. ChangePasswordPage gọi `doiMatKhau()` của AuthController với mkHienTai, mkMoi.
6. AuthController gọi `findByToken()` của User để lấy thông tin người dùng.
7. AuthController xác minh MK hiện tại khớp CSDL bằng `checkPassword()`.
8. AuthController mã hóa MK mới bằng `hashPassword()`.
9. AuthController gọi `updatePassword()` của User để cập nhật mật khẩu.
10. AuthController gọi `revokeAllSessions()` để thu hồi tất cả session.
11. ChangePasswordPage hiển thị "Đổi mật khẩu thành công. Vui lòng đăng nhập lại."

**Ngoại lệ: MK hiện tại sai**
- AuthController nhận false từ `checkPassword()`.
- ChangePasswordPage hiển thị "Mật khẩu hiện tại không chính xác."

**Ngoại lệ: MK mới không đủ mạnh**
- AuthController trả về lỗi validation.
- ChangePasswordPage highlight ô và hiển thị yêu cầu còn thiếu.

#### UC04 – Quản lý thông tin cá nhân

```plantuml
@startuml
title Quản lý TTCN – Tuần tự Phân tích

actor "Khách hàng" as KH
participant "ProfilePage\n<<Boundary>>" as B1
participant "ProfileController\n<<Control>>" as C1
entity "User\n<<Entity>>" as E1

KH -> B1 : 1: nhấn vào ảnh đại diện
activate B1
B1 -> C1 : 2: xemHoSo(userId)
activate C1
C1 -> E1 : 3: findById(userId)
activate E1
E1 --> C1 : 4: User
deactivate E1
C1 --> B1 : 5: trả về User
deactivate C1
B1 --> KH : 6: hiển thị hồ sơ cá nhân
KH -> B1 : 7: nhấn [Chỉnh sửa thông tin] + cập nhật + nhấn [Lưu]
B1 -> C1 : 8: capNhatHoSo(userId, hoTen, email)
activate C1
C1 -> E1 : 9: checkEmail(email)
activate E1
E1 --> C1 : 10: true/false
deactivate E1
C1 -> E1 : 11: update()
activate E1
E1 --> C1 : 12: thanh cong
deactivate E1
C1 --> B1 : 13: thanh cong
deactivate C1
B1 --> KH : 14: "Cập nhật thành công!"
deactivate B1
@enduml
```

**Kịch bản phiên bản 2 – UC04 Quản lý TTCN**

1. Khách hàng nhấn vào ảnh đại diện / tên tài khoản ở góc trên phải.
2. ProfilePage gọi `xemHoSo(userId)` của ProfileController.
3. ProfileController gọi `findById(userId)` của User.
4. User trả về đối tượng User cho ProfileController.
5. ProfileController trả kết quả về ProfilePage.
6. ProfilePage hiển thị: Họ tên, SĐT, Email, Hạng hội viên, Điểm tích lũy.
7. Khách hàng nhấn [Chỉnh sửa thông tin], cập nhật họ tên và email, nhấn [Lưu].
8. ProfilePage gọi `capNhatHoSo()` của ProfileController với userId, hoTen, email.
9. ProfileController gọi `checkEmail()` của User để kiểm tra email hợp lệ.
10. ProfileController gọi `update()` của User để cập nhật.
11. ProfilePage hiển thị "Cập nhật thành công!"

**Ngoại lệ: Email đã được dùng**
- User trả về false từ `checkEmail()`.
- ProfilePage hiển thị "Email này đã được đăng ký bởi tài khoản khác."

#### UC20 – Quản lý tài khoản nhân viên

```plantuml
@startuml
title Quản lý tài khoản nhân viên – Tuần tự Phân tích

actor "Admin" as Admin
participant "StaffManagePage\n<<Boundary>>" as B1
participant "StaffController\n<<Control>>" as C1
entity "Employee\n<<Entity>>" as E1

Admin -> B1 : 1: truy cập "Quản lý nhân viên"
activate B1
B1 -> C1 : 2: xemDanhSachNV()
activate C1
C1 -> E1 : 3: findAll()
activate E1
E1 --> C1 : 4: List Employee
deactivate E1
C1 --> B1 : 5: List Employee
deactivate C1
B1 --> Admin : 6: hiển thị danh sách nhân viên

Admin -> B1 : 7: nhấn [Thêm nhân viên] + nhập thông tin + nhấn [Lưu]
B1 -> C1 : 8: themNV(hoTen, vaiTro)
activate C1
C1 -> E1 : 9: save()
activate E1
E1 --> C1 : 10: Employee vừa tạo
deactivate E1
C1 --> B1 : 11: Employee vừa tạo
deactivate C1
B1 --> Admin : 12: "Thêm nhân viên thành công!"
deactivate B1
@enduml
```

**Kịch bản phiên bản 2 – UC20 Quản lý tài khoản nhân viên**

1. Admin truy cập "Quản lý nhân viên" từ trang quản trị.
2. StaffManagePage gọi `xemDanhSachNV()` của StaffController.
3. StaffController gọi `findAll()` của Employee.
4. Employee trả về danh sách nhân viên cho StaffController.
5. StaffController trả kết quả về StaffManagePage.
6. StaffManagePage hiển thị bảng: họ tên, vai trò, trạng thái.
7. Admin nhấn [Thêm nhân viên], nhập thông tin, nhấn [Lưu].
8. StaffManagePage gọi `themNV(hoTen, vaiTro)` của StaffController.
9. StaffController gọi `save()` của Employee.
10. StaffManagePage hiển thị "Thêm nhân viên thành công!"

**Ngoại lệ: SĐT đã tồn tại**
- StaffController nhận lỗi từ Employee.
- StaffManagePage hiển thị "SĐT này đã được sử dụng."

**Ngoại lệ: Nhân viên đang xử lý order**
- StaffController nhận lỗi từ Employee.
- StaffManagePage hiển thị cảnh báo "Nhân viên đang xử lý order, không thể xóa."
