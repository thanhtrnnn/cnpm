# Tài khoản & Thành viên


MỤC LỤC

I. PHA XÁC ĐỊNH YÊU CẦU
1. Danh sách Use Case
2. Danh sách Actor
3. UC con và quan hệ Include/Extend
4. Biểu đồ Use Case tổng quan

Quy trình 4 bước:
Bước 1 – Copy UC + Actor từ hệ thống:
Bước 2 – Đề xuất UC con từ giao diện:
Bước 3 – Xác định quan hệ include/extend:
5. Biểu đồ Use Case chi tiết
UC01 – Đăng nhập

UC02 – Đăng ký

UC03 – Đổi mật khẩu

UC04 – Quản lý TTCN

UC20 – Quản lý nhân viên

 
II. PHA PHÂN TÍCH
1. Kịch bản chuẩn
UC01 – Đăng nhập
UC02 – Đăng ký
UC03 – Đổi mật khẩu
UC04 – Quản lý thông tin cá nhân
UC20 – Quản lý tài khoản nhân viên

2. Mô hình hóa lớp
Bước 1 – Mô tả chức năng bằng đoạn văn xuôi
Hệ thống cho phép khách hàng đăng ký tài khoản hội viên mới bằng cách cung cấp họ tên, số điện thoại, email và mật khẩu; sau đó xác minh số điện thoại qua mã OTP trước khi hoàn tất đăng ký. Mỗi tài khoản gắn liền với một hạng hội viên (Thường, Bạc, Vàng, Kim Cương) dựa trên điểm tích lũy. Người dùng sau khi đăng nhập có thể xem và cập nhật thông tin cá nhân như họ tên và email, hoặc thực hiện đổi mật khẩu bằng cách xác minh mật khẩu cũ rồi nhập mật khẩu mới. Hệ thống ghi nhận các phiên đăng nhập để phục vụ bảo mật và thu hồi phiên khi đổi mật khẩu. Ngoài ra, chủ doanh nghiệp có quyền quản lý tài khoản nhân viên: tạo, chỉnh sửa và xóa tài khoản nhân viên trong hệ thống.
Bước 2 + 3 – Trích danh từ và đánh giá
Hệ thống → loại: quá chung, không phải thực thể nghiệp vụ
Khách hàng → lớp User: hoTen, soDienThoai, email, matKhau, ngayTao
Tài khoản → thuộc về User (gộp vào User, tránh tách thừa)
Họ tên → thuộc tính của User
Số điện thoại → thuộc tính của User (dùng làm username đăng nhập)
Email → thuộc tính của User
Mật khẩu → thuộc tính của User (lưu dạng mã hóa)
Ngày tham gia → thuộc tính ngayTao của User
Hạng hội viên → lớp MembershipTier: tenHang, diemToiThieu, moTa, heSoUuDai
Điểm tích lũy → thuộc tính diemTichLuy của User
Mã OTP → lớp OTP: maOTP, loai, thoiHanHetHan, daXacMinh
Phiên đăng nhập → lớp LoginSession: tokenPhien, thoiGianDangNhap, thoiGianHetHan, thietBi
Lịch sử → loại: quá chung → cụ thể là LoginSession đã đủ
Danh sách → loại: không phải thực thể
Giao diện → loại: là Boundary, không phải Entity
Nhân viên → lớp Employee: hoTen, vaiTro, chiNhanh, trangThai
Chủ doanh nghiệp → loại: actor, không phải thực thể dữ liệu
Bước 4 – Xác định quan hệ số lượng
1 User có 1 MembershipTier → User – MembershipTier: n – 1 (nhiều người dùng có thể có cùng hạng)
1 User có nhiều OTP → User – OTP: 1 – n (mỗi lần đăng ký/đổi SĐT tạo 1 OTP mới)
1 User có nhiều LoginSession → User – LoginSession: 1 – n (người dùng có thể đăng nhập trên nhiều thiết bị)
Bước 5 – Bổ sung quan hệ
User gắn composition với OTP: một OTP không tồn tại độc lập nếu không có User tương ứng (khi xóa User thì xóa theo tất cả OTP). Tương tự, LoginSession không tồn tại độc lập khỏi User. Quan hệ với MembershipTier là aggregation: MembershipTier là dữ liệu danh mục tồn tại độc lập với User. Employee là lớp riêng biệt, không kế thừa từ User.
Biểu đồ thực thể Module Tài khoản & Thành viên:

3. Biểu đồ lớp phân tích
3.1. Phân tích chi tiết chức năng "Đăng nhập"
Người dùng truy cập trang đăng nhập -> đề xuất lớp LoginView, có ô nhập SĐT, ô nhập mật khẩu, nút Đăng nhập.
Người dùng nhập SĐT, mật khẩu và nhấn nút Đăng nhập -> hệ thống cần xác thực tài khoản -> cần chức năng checkLogin() của đối tượng User.
Nếu tài khoản không tồn tại -> hệ thống hiển thị thông báo lỗi.
Nếu mật khẩu sai -> hệ thống hiển thị thông báo lỗi.
Hoàn tất, hệ thống tạo phiên đăng nhập và chuyển hướng trang chủ.
Boundary: LoginView
Entity: User
3.2. Phân tích chi tiết chức năng "Đăng ký"
Người dùng truy cập trang đăng ký -> đề xuất lớp RegisterView, có ô nhập Họ tên, SĐT, Email, Mật khẩu, Xác nhận MK, nút Tiếp tục.
Người dùng nhập thông tin và nhấn nút Tiếp tục -> hệ thống cần tạo tài khoản mới -> cần chức năng register() của đối tượng User.
Hệ thống gửi OTP đến SĐT -> đề xuất lớp OTPVerifyView, có ô nhập OTP, nút Xác nhận.
Người dùng nhập OTP và nhấn nút Xác nhận -> hệ thống cần xác minh OTP -> cần chức năng verifyOTP() của đối tượng OTP.
Hoàn tất, hệ thống tạo tài khoản mới và tự động đăng nhập.
Boundary: RegisterView, OTPVerifyView
Entity: User, OTP
3.3. Phân tích chi tiết chức năng "Đổi mật khẩu"
Người dùng truy cập trang bảo mật -> đề xuất lớp ChangePasswordView, có ô nhập MK hiện tại, MK mới, Xác nhận MK mới, nút Lưu.
Người dùng nhập MK hiện tại, MK mới và nhấn nút Lưu -> hệ thống cần đổi mật khẩu -> cần chức năng changePassword() của đối tượng User.
Nếu MK hiện tại sai -> hệ thống hiển thị thông báo lỗi.
Nếu MK mới không hợp lệ -> hệ thống hiển thị thông báo lỗi.
Hoàn tất, hệ thống cập nhật mật khẩu mới và thu hồi tất cả phiên đăng nhập khác.
Boundary: ChangePasswordView
Entity: User
3.4. Phân tích chi tiết chức năng "Quản lý thông tin cá nhân"
Người dùng nhấn vào ảnh đại diện -> đề xuất lớp ProfileView, có hiển thị Họ tên, SĐT, Email, Hạng hội viên, Điểm tích lũy, nút Chỉnh sửa.
Hệ thống cần lấy thông tin hồ sơ -> cần chức năng getProfile() của đối tượng User.
Người dùng nhấn Chỉnh sửa, sửa thông tin và nhấn Lưu -> hệ thống cần cập nhật hồ sơ -> cần chức năng updateProfile() của đối tượng User.
Nếu email không hợp lệ hoặc đã được dùng -> hệ thống hiển thị thông báo lỗi.
Hoàn tất, hệ thống cập nhật hồ sơ vào CSDL.
Boundary: ProfileView
Entity: User
3.5. Phân tích chi tiết chức năng "Quản lý nhân viên"
Admin truy cập trang quản lý nhân viên -> đề xuất lớp StaffManageView, có bảng danh sách nhân viên, nút Thêm, Sửa, Xóa.
Hệ thống cần tải danh sách nhân viên -> cần chức năng getAllStaff() của đối tượng Employee.
Admin nhấn Thêm, nhập thông tin và nhấn Lưu -> hệ thống cần tạo nhân viên mới -> cần chức năng addStaff() của đối tượng Employee.
Admin nhấn Sửa trên một dòng, cập nhật và nhấn Lưu -> hệ thống cần cập nhật nhân viên -> cần chức năng updateStaff() của đối tượng Employee.
Admin nhấn Xóa trên một dòng, xác nhận -> hệ thống cần xóa nhân viên -> cần chức năng deleteStaff() của đối tượng Employee.
Nếu nhân viên đang xử lý order -> hệ thống hiển thị thông báo lỗi.
Hoàn tất, hệ thống cập nhật danh sách nhân viên.
Boundary: StaffManageView
Entity: Employee
Sơ đồ lớp phân tích – Module Tài khoản & Thành viên

4. Biểu đồ tuần tự phân tích
UC01 – Đăng nhập (7 bước)

Kịch bản phiên bản 2 – UC01 Đăng nhập (7 bước)
1.     Người dùng chọn chức năng Đăng nhập.
2.     Lớp LoginView hiển thị giao diện đăng nhập.
3.     Người dùng nhập SĐT/Email + Mật khẩu, nhấn Đăng nhập.
4.     Lớp LoginView gọi checkLogin(phoneNumber, password).
5.     Lớp User trả kết quả xác thực.
6.     Lớp LoginView chuyển hướng sang HomeView, "Đăng nhập thành công".
7.     Lớp HomeView hiển thị trang chủ.
UC02 – Đăng ký (17 bước)

Kịch bản phiên bản 2 – UC02 Đăng ký (17 bước)
1.     Khách hàng chọn liên kết Đăng ký.
2.     Lớp RegisterView hiển thị giao diện đăng ký.
3.     Khách hàng nhập Họ tên, SĐT, Email, Mật khẩu, nhấn Tiếp tục.
4.     Lớp RegisterView gọi register(fullName, phoneNumber, email, password).
5.     Lớp Client gọi sendOTP(phoneNumber, REGISTER).
6.     Lớp OTP OTP đã gửi.
7.     Lớp Client trả kết quả.
8.     Lớp RegisterView kiểm tra hợp lệ, gửi mã OTP.
9.     Lớp RegisterView hiển thị giao diện xác nhận OTP.
10.  Khách hàng nhập mã OTP, nhấn Xác nhận.
11.  Lớp OTPVerifyView gọi verifyOTP(otpCode).
12.  Lớp OTP xác minh thành công.
13.  Lớp OTPVerifyView gọi saveUser().
14.  Lớp Client tạo tài khoản thành công.
15.  Lớp OTPVerifyView "Đăng ký thành công!".
16.  Lớp OTPVerifyView tự động đăng nhập, chuyển hướng HomeView.
17.  Lớp HomeView hiển thị trang chủ.
UC03 – Đổi mật khẩu (8 bước)

Kịch bản phiên bản 2 – UC03 Đổi mật khẩu (8 bước)
1.     Người dùng chọn chức năng Đổi mật khẩu.
2.     Lớp ChangePasswordView hiển thị giao diện đổi mật khẩu.
3.     Người dùng nhập MK hiện tại, MK mới, Xác nhận MK mới, nhấn Lưu.
4.     Lớp ChangePasswordView gọi changePassword(currentPassword, newPassword).
5.     Lớp User đổi mật khẩu thành công.
6.     Lớp ChangePasswordView "Đổi mật khẩu thành công".
7.     Lớp ChangePasswordView chuyển hướng về giao diện Đăng nhập.
8.     Lớp LoginView hiển thị trang đăng nhập.
UC04 – Quản lý thông tin cá nhân (10 bước)

Kịch bản phiên bản 2 – UC04 Quản lý thông tin cá nhân (10 bước)
1.     Khách hàng chọn chức năng Hồ sơ cá nhân.
2.     Lớp ProfileView gọi getProfile(clientId).
3.     Lớp Client trả về thông tin Client.
4.     Lớp ProfileView hiển thị trang hồ sơ cá nhân.
5.     Khách hàng nhấn nút Chỉnh sửa.
6.     Lớp ProfileView chuyển sang chế độ chỉnh sửa.
7.     Khách hàng cập nhật Họ tên, Email, nhấn Lưu.
8.     Lớp ProfileView gọi updateProfile(clientId, fullName, email).
9.     Lớp Client cập nhật thành công.
10.  Lớp ProfileView "Cập nhật thành công!", quay về chế độ xem.
UC20 – Quản lý tài khoản nhân viên (18 bước)

Kịch bản phiên bản 2 – UC20 Quản lý tài khoản nhân viên (18 bước)
1.     Admin chọn chức năng Quản lý nhân viên.
2.     Lớp StaffManageView gọi getAllStaff().
3.     Lớp Employee trả về danh sách Employee.
4.     Lớp StaffManageView hiển thị danh sách nhân viên.
5.     Admin nhấn nút Thêm nhân viên.
6.     Lớp StaffManageView hiển thị giao diện nhập thông tin.
7.     Admin nhập Họ tên, SĐT, Vai trò, Chi nhánh, nhấn Lưu.
8.     Lớp StaffManageView gọi addStaff(fullName, role).
9.     Lớp Employee tạo thành công.
10.  Lớp StaffManageView "Thêm nhân viên thành công!".
11.  Admin nhấn nút Sửa trên dòng Nguyễn Minh Tuấn.
12.  Lớp StaffManageView hiển thị giao diện chỉnh sửa.
13.  Admin cập nhật thông tin, nhấn Lưu.
14.  Lớp StaffManageView gọi updateStaff(id, data).
15.  Lớp Employee cập nhật thành công.
16.  Lớp StaffManageView "Cập nhật thành công!".
17.  Admin nhấn nút Xóa trên dòng Lê Văn Khánh.
18.  Lớp StaffManageView yêu cầu xác nhận xóa, "Xóa nhân viên thành công!".
 
III. PHA THIẾT KẾ
1. Thiết kế lớp thực thể
1.1. Bước 1 – Bổ sung thuộc tính id
19.  User: id : int — lớp gốc; Client và Employee kế thừa id này
20.  MembershipTier: id : int
21.  OTP: id : int
22.  LoginSession: id : int
1.2. Bước 2 – Thêm kiểu dữ liệu
23.  User (lớp cha): id : int, fullName : String, phoneNumber : String, email : String, password : String, role : String, createdAt : Date
24.  Client (kế thừa User): loyaltyPoints : int, joinedAt : Date
25.  Employee (kế thừa User): staffRole : String, branch : String, status : String
26.  MembershipTier: id : int, tierName : String, minPoints : int, description : String, discountRate : double
27.  OTP: id : int, otpCode : String, type : String, expiresAt : Date, verified : boolean
28.  LoginSession: id : int, sessionToken : String, loginTime : DateTime, expiresAt : DateTime, device : String
1.3. Bước 3 – Chuyển quan hệ
29.  Client kế thừa User: generalization (khách hàng là User có vai trò CLIENT)
30.  Employee kế thừa User: generalization (nhân viên là User có vai trò EMPLOYEE)
31.  Client o-- MembershipTier: aggregation (hạng hội viên là danh mục độc lập, chỉ khách hàng có)
32.  User *-- OTP: composition (OTP không tồn tại độc lập)
33.  User *-- LoginSession: composition (phiên không tồn tại độc lập)
1.4. Bước 4 – Bổ sung thuộc tính kiểu đối tượng
34.  Client: membershipTier : MembershipTier
35.  OTP: user : User
36.  LoginSession: user : User
1.5. Biểu đồ lớp thực thể

2. Thiết kế CSDL
2.1. Bước 1 – Tạo bảng
Ánh xạ kế thừa kiểu single-table: gộp User, Client, Employee vào một bảng tblUser, dùng cột role để phân biệt; thuộc tính riêng của Client/Employee để NULL khi không áp dụng.
2.2. Bước 2 – Chuyển kiểu dữ liệu
2.3. Bước 3 – Xử lý cardinality
37.  Client – MembershipTier (n-1): tblUser có FK tblMembershipTierMa (chỉ dòng role = CLIENT dùng, NULL với dòng khác)
38.  User – OTP (1-n): tblOTP có FK tblUserMa
39.  User – LoginSession (1-n): tblLoginSession có FK tblUserMa
2.4. Bước 4 – PK/FK
40.  PK: ma : integer(10) <<PK>>
41.  FK: tbl[TenBangCha]Ma : integer(10) <<FK>>
42.  Cột role (CLIENT / EMPLOYEE / ADMIN) phân biệt loại người dùng trong bảng tblUser gộp
2.5. Biểu đồ ERD

3. Wireframe
3.1. Màn hình đăng nhập
┌──────────────────────────────────────────────┐ │          	Đăng nhập                   	│ │                                              │ │  txtSDT:   	[________________________] 	│ │  txtMatKhau:   [________________________] 	│ │                                              │ │  [btnDangNhap]                           	│ │  btnQuenMatKhau  |  btnDangKy            	│ └──────────────────────────────────────────────┘
3.2. Màn hình đăng ký
┌──────────────────────────────────────────────┐ │          	Đăng ký tài khoản            	│ │                                              │ │  txtHoTen:       	[________________________]  │ │  txtSoDienThoai: 	[________________________]  │ │  txtEmail:       	[________________________]  │ │  txtMatKhau:     	[________________________]  │ │  txtXacNhanMatKhau:  [________________________]  │ │                                              │ │  [btnTiepTuc]            	[btnHuy]    	│ └──────────────────────────────────────────────┘
3.3. Màn hình xác nhận OTP
┌──────────────────────────────────────────────┐ │       	Xác nhận OTP                   	│ │                                              │ │  txtOTP: [__][__][__][__][__][__]        	│ │                                              │ │  [btnXacNhan]                            	│ │  lblCountdown: Gửi lại OTP (60s)        	│ └──────────────────────────────────────────────┘
3.4. Màn hình đổi mật khẩu
┌──────────────────────────────────────────────┐ │       	Đổi mật khẩu                   	│ │                                              │ │  txtMatKhauHienTai: 	[________________________]│ │  txtMatKhauMoi:     	[________________________]│ │  txtXacNhanMatKhauMoi:  [________________________]│ │                                              │ │  [btnLuu]            	[btnHuy]        	│ └──────────────────────────────────────────────┘
3.5. Màn hình hồ sơ cá nhân
┌──────────────────────────────────────────────┐ │       	Hồ sơ cá nhân                  	│ │                                              │ │  txtHoTen:     	[________________________]  │ │  txtSoDienThoai:   [________________________]  │ │  txtEmail:     	[________________________]  │ │  lblMembershipTier: ........................  │ │  lblDiemTichLuy:   ........................  │ │                                              │ │  [btnChinhSua]  [btnDoiMatKhau]          	│ └──────────────────────────────────────────────┘
3.6. Màn hình quản lý nhân viên
┌──────────────────────────────────────────────┐ │    	Quản lý tài khoản nhân viên       	│ │                                              │ │  txtTimKiem: [________________________]  	│ │  [btnThem]                               	│ │                                              │ │ ┌──────┬────────┬──────────┬──────────┐      │ │ │ Họ tên│ Vai trò│ Trạng thái│ ...     │  	│ │ │ ......│ .......│ .........│         │  	│ │ │ ......│ .......│ .........│         │  	│ │ └──────┴────────┴──────────┴──────────┘      │ │  tblStaff                                	│ │                                              │ │  [btnSua]  [btnXoa]                      	│ └──────────────────────────────────────────────┘
4. MVC class diagram
4.1. Tổng quan kiến trúc
Mô hình thiết kế theo kiến trúc MVC (Boundary – Control – Entity):
Boundary: LoginPage, RegisterPage, OTPVerifyPage, ChangePasswordPage, ProfilePage, StaffManagePage
Control: AuthController, ProfileController, StaffController
Entity: User, Client, Employee, MembershipTier, OTP, LoginSession
4.2. Quy trình xác định chữ ký hàm Controller
a) Đăng nhập → checkLogin()
43.  Input: username, password
44.  Output: boolean
45.  Ứng viên tham số vào: checkLogin() → chọn (gom nhóm tham số)
46.  Ứng viên tham số ra: checkLogin(): boolean → chọn (trả về true/false xác thực)
b) Đăng ký → register()
47.  Input: fullName, phoneNumber, email, password
48.  Output: User (vừa tạo)
49.  Ứng viên tham số vào: register() → chọn
50.  Ứng viên tham số ra: register(): User → chọn
c) Xác minh OTP → verifyOTP()
51.  Input: otp
52.  Output: boolean
53.  Ứng viên tham số vào: verifyOTP() → chọn
54.  Ứng viên tham số ra: verifyOTP(): boolean → chọn (cần biết đúng/sai)
d) Đổi mật khẩu → changePassword()
55.  Input: currentPassword, newPassword
56.  Output: boolean
57.  Ứng viên tham số vào: changePassword() → chọn
58.  Ứng viên tham số ra: changePassword(): boolean → chọn
e) Xem hồ sơ → getProfile()
59.  Input: userId
60.  Output: User
61.  Ứng viên tham số vào: getProfile() → chọn
62.  Ứng viên tham số ra: getProfile(): User → chọn
f) Cập nhật hồ sơ → updateProfile()
63.  Input: userId, fullName, email
64.  Output: User
65.  Ứng viên tham số vào: updateProfile() → chọn
66.  Ứng viên tham số ra: updateProfile(): User → chọn
g) Xem danh sách NV → getAllStaff()
67.  Input: (không có)
68.  Output: List\<Employee\>
69.  Ứng viên tham số vào: getAllStaff() → chọn
70.  Ứng viên tham số ra: getAllStaff(): List<Employee> → chọn
h) Tìm kiếm NV → searchStaff()
71.  Input: keyword
72.  Output: List\<Employee\>
73.  Ứng viên tham số vào: searchStaff(keyword: String) → chọn
74.  Ứng viên tham số ra: searchStaff(): List<Employee> → chọn
i) Lấy NV theo id → getStaffById()
75.  Input: id
76.  Output: Employee
77.  Ứng viên tham số vào: getStaffById(id: int) → chọn
78.  Ứng viên tham số ra: getStaffById(): Employee → chọn
j) Thêm NV → saveStaff()
79.  Input: employee
80.  Output: boolean
81.  Ứng viên tham số vào: saveStaff(employee: Employee) → chọn
82.  Ứng viên tham số ra: saveStaff(): boolean → chọn (cần biết thành công/thất bại)
k) Sửa NV → updateStaff()
83.  Input: employee
84.  Output: boolean
85.  Ứng viên tham số vào: updateStaff() → chọn
86.  Ứng viên tham số ra: updateStaff(): boolean → chọn
l) Xóa NV → deleteStaff()
87.  Input: id
88.  Output: boolean
89.  Ứng viên tham số vào: deleteStaff() → chọn
90.  Ứng viên tham số ra: deleteStaff(): boolean → chọn (cần biết thành công/thất bại)

5. Biểu đồ tuần tự thiết kế
5.1. Đăng nhập

Kịch bản phiên bản 3 – UC01 Đăng nhập
1.     Khách hàng truy cập URL /login.
2.     Lớp LoginPage gọi phương thức formLoad().
3.     Lớp LoginPage render form đăng nhập.
4.     Khách hàng nhập SĐT và Mật khẩu.
5.     Khách hàng click nút [Đăng nhập].
6.     Lớp LoginPage gọi phương thức btnLoginClick().
7.     Lớp LoginPage gọi phương thức checkLogin() của lớp AuthController.
8.     Lớp AuthController gọi phương thức findBySDT() của lớp User.
9.     Lớp User trả về User cho lớp AuthController.
10.  Lớp AuthController gọi phương thức checkPassword().
11.  Lớp AuthController trả về true cho lớp LoginPage.
12.  Lớp LoginPage redirect /home.
13.  Lớp LoginPage showMessage("Đăng nhập thành công").
5.2. Đăng ký

Kịch bản phiên bản 3 – UC02 Đăng ký
1.     Khách hàng click liên kết "Đăng ký" từ trang /login.
2.     Lớp RegisterPage gọi phương thức formLoad().
3.     Lớp RegisterPage render form đăng ký.
4.     Khách hàng nhập Họ tên, SĐT, Email, Mật khẩu.
5.     Khách hàng click nút [Tiếp tục].
6.     Lớp RegisterPage gọi phương thức btnTiepTucClick().
7.     Lớp RegisterPage gọi phương thức register() của lớp AuthController.
8.     Lớp AuthController gọi phương thức existsBySDT() của lớp User.
9.     Lớp User trả về false cho lớp AuthController.
10.  Lớp AuthController gọi phương thức existsByEmail() của lớp User.
11.  Lớp User trả về false cho lớp AuthController.
12.  Lớp AuthController gọi phương thức save() của lớp User.
13.  Lớp User trả về User cho lớp AuthController.
14.  Lớp AuthController gọi phương thức sendOTP() của lớp OTP.
15.  Lớp OTP OTP sent.
16.  Lớp AuthController trả về User cho lớp RegisterPage.
17.  Lớp RegisterPage hiển thị OTPVerifyPage.
18.  Khách hàng nhập mã OTP.
19.  Khách hàng click nút [Xác nhận].
20.  Lớp OTPVerifyPage gọi phương thức btnXacNhanClick().
21.  Lớp OTPVerifyPage gọi phương thức verifyOTP() của lớp AuthController.
22.  Lớp AuthController gọi phương thức verify() của lớp OTP.
23.  Lớp OTP trả về true cho lớp AuthController.
24.  Lớp AuthController trả về true cho lớp OTPVerifyPage.
25.  Lớp OTPVerifyPage showMessage("Đăng ký thành công!").
5.3. Đổi mật khẩu

Kịch bản phiên bản 3 – UC03 Đổi mật khẩu
1.     Người dùng truy cập URL /security.
2.     Lớp ChangePasswordPage gọi phương thức formLoad().
3.     Lớp ChangePasswordPage render form đổi mật khẩu.
4.     Người dùng nhập Mật khẩu hiện tại, Mật khẩu mới, Xác nhận MK mới.
5.     Người dùng click nút [Lưu thay đổi].
6.     Lớp ChangePasswordPage gọi phương thức btnLuuClick().
7.     Lớp ChangePasswordPage gọi phương thức changePassword() của lớp AuthController.
8.     Lớp AuthController gọi phương thức findById() của lớp User.
9.     Lớp User trả về User cho lớp AuthController.
10.  Lớp AuthController gọi phương thức checkPassword().
11.  Lớp AuthController hashPassword().
12.  Lớp AuthController gọi phương thức updatePassword() của lớp User.
13.  Lớp User trả về true cho lớp AuthController.
14.  Lớp AuthController gọi phương thức revokeAllSessions() của lớp User.
15.  Lớp User trả về void cho lớp AuthController.
16.  Lớp AuthController trả về true cho lớp ChangePasswordPage.
17.  Lớp ChangePasswordPage showMessage("Đổi mật khẩu thành công. Vui lòng đăng nhập lại.").
5.4. Quản lý TTCN

Kịch bản phiên bản 3 – UC04 Quản lý TTCN
1.     Khách hàng click avatar / tên tài khoản.
2.     Lớp ProfilePage gọi phương thức formLoad().
3.     Lớp ProfilePage gọi phương thức getProfile() của lớp ProfileController.
4.     Lớp ProfileController gọi phương thức findById() của lớp User.
5.     Lớp User trả về User cho lớp ProfileController.
6.     Lớp ProfileController trả về User cho lớp ProfilePage.
7.     Lớp ProfilePage gọi phương thức displayProfile().
8.     Lớp ProfilePage render hồ sơ cá nhân.
9.     Khách hàng click nút [Chỉnh sửa].
10.  Khách hàng sửa Họ tên và Email.
11.  Khách hàng click nút [Lưu].
12.  Lớp ProfilePage gọi phương thức btnChinhSuaClick().
13.  Lớp ProfilePage gọi phương thức updateProfile() của lớp ProfileController.
14.  Lớp ProfileController gọi phương thức checkEmail() của lớp User.
15.  Lớp User trả về true cho lớp ProfileController.
16.  Lớp ProfileController gọi phương thức save() của lớp User.
17.  Lớp User trả về User cho lớp ProfileController.
18.  Lớp ProfileController trả về User cho lớp ProfilePage.
19.  Lớp ProfilePage gọi phương thức displayProfile().
20.  Lớp ProfilePage showMessage("Cập nhật thành công!").
5.5. Quản lý nhân viên

Kịch bản phiên bản 3 – UC20 Quản lý nhân viên
1.     Admin truy cập URL /admin/staff.
2.     Lớp StaffManagePage gọi phương thức formLoad().
3.     Lớp StaffManagePage gọi phương thức getAllStaff() của lớp StaffController.
4.     Lớp StaffController gọi phương thức findAll() của lớp Employee.
5.     Lớp Employee trả về List<Employee> cho lớp StaffController.
6.     Lớp StaffController trả về List<Employee> cho lớp StaffManagePage.
7.     Lớp StaffManagePage gọi phương thức displayStaffList().
8.     Lớp StaffManagePage render bảng nhân viên.
9.     Admin click nút [Thêm nhân viên].
10.  Admin nhập Họ tên và Vai trò.
11.  Admin click nút [Lưu].
12.  Lớp StaffManagePage gọi phương thức btnThemClick().
13.  Lớp StaffManagePage gọi phương thức saveStaff() của lớp StaffController.
14.  Lớp StaffController gọi phương thức save() của lớp Employee.
15.  Lớp Employee trả về Employee cho lớp StaffController.
16.  Lớp StaffController trả về true cho lớp StaffManagePage.
17.  Lớp StaffManagePage gọi phương thức displayStaffList().
18.  Lớp StaffManagePage showMessage("Thêm nhân viên thành công!").
19.  Admin click nút [Xóa] trên một dòng nhân viên.
20.  Lớp StaffManagePage gọi phương thức btnXoaClick().
21.  Lớp StaffManagePage gọi phương thức deleteStaff() của lớp StaffController.
22.  Lớp StaffController gọi phương thức deleteById() của lớp Employee.
23.  Lớp Employee trả về true cho lớp StaffController.
24.  Lớp StaffController trả về true cho lớp StaffManagePage.
25.  Lớp StaffManagePage gọi phương thức displayStaffList().
26.  Lớp StaffManagePage showMessage("Xóa nhân viên thành công!").
 
IV. PHA CÀI ĐẶT VÀ KIỂM THỬ
1. Lập kế hoạch test
2. Test case chi tiết
---
TC01: Đăng nhập thành công
Trạng thái CSDL trước:
tblMembershipTier
tblUser
tblLoginSession
Kịch bản thực hiện:
Trạng thái CSDL sau:
tblUser: Không thay đổi.
tblLoginSession (thêm 1 dòng mới)
---
TC02: Tài khoản không tồn tại
Trạng thái CSDL trước:
tblMembershipTier
tblUser
Kịch bản thực hiện:
Trạng thái CSDL sau: Không thay đổi.
---
TC03: Mật khẩu sai 5 lần → khóa tài khoản
Trạng thái CSDL trước:
tblMembershipTier
tblUser
Kịch bản thực hiện:
Trạng thái CSDL sau:
tblUser
---
TC04: Đăng ký thành công với OTP
Trạng thái CSDL trước:
tblMembershipTier
tblUser
Kịch bản thực hiện:
Trạng thái CSDL sau:
tblUser (thêm 1 dòng mới)
tblOTP (cập nhật dòng hiện có)
tblLoginSession (thêm 1 dòng mới)
---
TC05: SĐT đã tồn tại khi đăng ký
Trạng thái CSDL trước:
tblMembershipTier
tblUser
Kịch bản thực hiện:
Trạng thái CSDL sau: Không thay đổi.
---
TC06: OTP sai 3 lần → hủy phiên
Trạng thái CSDL trước:
tblMembershipTier
tblUser
tblOTP
(Lưu ý: tblUserMa = null vì tài khoản mới chưa được tạo; OTP được tạo tạm trong phiên đăng ký)
Kịch bản thực hiện:
Trạng thái CSDL sau:
tblOTP
tblUser: Không thay đổi. Không có tài khoản mới nào được tạo.
---
TC07: Đổi mật khẩu thành công
Trạng thái CSDL trước:
tblMembershipTier
tblUser
tblLoginSession
Kịch bản thực hiện:
Trạng thái CSDL sau:
tblUser
tblLoginSession
---
TC08: Mật khẩu hiện tại sai
Trạng thái CSDL trước:
tblMembershipTier
tblUser
tblLoginSession
Kịch bản thực hiện:
Trạng thái CSDL sau: Không thay đổi.
---
TC09: Cập nhật thông tin thành công
Trạng thái CSDL trước:
tblMembershipTier
tblUser
Kịch bản thực hiện:
Trạng thái CSDL sau:
tblUser
---
TC10: Email đã được sử dụng khi cập nhật hồ sơ
Trạng thái CSDL trước:
tblMembershipTier
tblUser
Kịch bản thực hiện:
Trạng thái CSDL sau: Không thay đổi.
---
TC11: Thêm nhân viên mới
Trạng thái CSDL trước:
tblMembershipTier
tblUser
tblEmployee
Kịch bản thực hiện:
Trạng thái CSDL sau:
tblUser (thêm 1 dòng mới)
tblEmployee (thêm 1 dòng mới)
 

