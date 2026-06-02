# Tài khoản & Thành viên


MỤC LỤC

I. PHA XÁC ĐỊNH YÊU CẦU
1. Danh sách Use Case
2. Danh sách Actor
3. UC con và quan hệ Include/Extend
4. Biểu đồ Use Case tổng quan

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
 Actor → LoginView: chọn chức năng Đăng nhập.
 LoginView → Actor: hiển thị giao diện đăng nhập.
 Actor → LoginView: nhập txtPhoneNumber + txtPassword, nhấn Đăng nhập.
 LoginView → User: checkLogin(phoneNumber, password).
 User → LoginView: return kết quả xác thực.
 LoginView → HomeView: chuyển hướng, "Đăng nhập thành công".
 HomeView → Actor: hiển thị trang chủ.
UC02 – Đăng ký (17 bước)

Kịch bản phiên bản 2 – UC02 Đăng ký (17 bước)
 Actor → RegisterView: chọn liên kết Đăng ký.
 RegisterView → Actor: hiển thị giao diện đăng ký.
 Actor → RegisterView: nhập txtFullName, txtPhoneNumber, txtEmail, txtPassword, nhấn Tiếp tục.
 RegisterView → Client: register(fullName, phoneNumber, email, password).
 Client → OTP: sendOTP(phoneNumber, REGISTER).
 OTP → Client: return OTP đã gửi.
 Client → RegisterView: return kết quả.
 RegisterView → Actor: kiểm tra hợp lệ, gửi mã OTP.
 RegisterView → Actor: hiển thị giao diện xác nhận OTP.
Actor → OTPVerifyView: nhập txtOTP, nhấn Xác nhận.
OTPVerifyView → OTP: verifyOTP(otpCode).
OTP → OTPVerifyView: return xác minh thành công.
OTPVerifyView → Client: saveUser().
Client → OTPVerifyView: return tạo tài khoản thành công.
OTPVerifyView → Actor: "Đăng ký thành công!".
OTPVerifyView → HomeView: tự động đăng nhập, chuyển hướng.
HomeView → Actor: hiển thị trang chủ.
UC03 – Đổi mật khẩu (8 bước)

Kịch bản phiên bản 2 – UC03 Đổi mật khẩu (8 bước)
 Actor → ChangePasswordView: chọn chức năng Đổi mật khẩu.
 ChangePasswordView → Actor: hiển thị giao diện đổi mật khẩu.
 Actor → ChangePasswordView: nhập txtCurrentPassword, txtNewPassword, txtConfirmNewPassword, nhấn Lưu.
 ChangePasswordView → User: changePassword(currentPassword, newPassword).
 User → ChangePasswordView: return đổi mật khẩu thành công.
 ChangePasswordView → Actor: "Đổi mật khẩu thành công".
 ChangePasswordView → LoginView: chuyển hướng về giao diện Đăng nhập.
 LoginView → Actor: hiển thị trang đăng nhập.
UC04 – Quản lý thông tin cá nhân (10 bước)

Kịch bản phiên bản 2 – UC04 Quản lý thông tin cá nhân (10 bước)
 Actor → ProfileView: chọn chức năng Hồ sơ cá nhân.
 ProfileView → Client: getProfile(clientId).
 Client → ProfileView: return thông tin Client.
 ProfileView → Actor: hiển thị trang hồ sơ cá nhân.
 Actor → ProfileView: nhấn nút btnEdit.
 ProfileView → Actor: chuyển sang chế độ chỉnh sửa.
 Actor → ProfileView: cập nhật lblFullName, lblEmail, nhấn Lưu.
 ProfileView → Client: updateProfile(clientId, fullName, email).
 Client → ProfileView: return cập nhật thành công.
ProfileView → Actor: "Cập nhật thành công!", quay về chế độ xem.
UC20 – Quản lý tài khoản nhân viên (18 bước)

Kịch bản phiên bản 2 – UC20 Quản lý tài khoản nhân viên (18 bước)
 Actor → StaffManageView: chọn chức năng Quản lý nhân viên.
 StaffManageView → Employee: getAllStaff().
 Employee → StaffManageView: return danh sách Employee.
 StaffManageView → Actor: hiển thị tblStaffList.
 Actor → StaffManageView: nhấn nút btnAdd.
 StaffManageView → Actor: hiển thị giao diện nhập thông tin.
 Actor → StaffManageView: nhập fullName, staffRole, nhấn Lưu.
 StaffManageView → Employee: addStaff(fullName, role).
 Employee → StaffManageView: return tạo thành công.
StaffManageView → Actor: "Thêm nhân viên thành công!".
Actor → StaffManageView: nhấn btnEdit trên dòng nhân viên.
StaffManageView → Actor: hiển thị giao diện chỉnh sửa.
Actor → StaffManageView: cập nhật thông tin, nhấn Lưu.
StaffManageView → Employee: updateStaff(id, data).
Employee → StaffManageView: return cập nhật thành công.
StaffManageView → Actor: "Cập nhật thành công!".
Actor → StaffManageView: nhấn btnDelete trên dòng nhân viên.
StaffManageView → Actor: yêu cầu xác nhận xóa, "Xóa nhân viên thành công!".

III. PHA THIẾT KẾ
1. Thiết kế lớp thực thể
1.1. Bước 1 – Bổ sung thuộc tính id
 User: id : int — lớp gốc; Client và Employee kế thừa id này
 MembershipTier: id : int
 OTP: id : int
 LoginSession: id : int
1.2. Bước 2 – Thêm kiểu dữ liệu
 User (lớp cha): id : int, fullName : String, phoneNumber : String, email : String, password : String, role : String, createdAt : Date
 Client (kế thừa User): loyaltyPoints : int, joinedAt : Date
 Employee (kế thừa User): staffRole : String, branch : String, status : String
 MembershipTier: id : int, tierName : String, minPoints : int, description : String, discountRate : double
 OTP: id : int, otpCode : String, type : String, expiresAt : Date, verified : boolean
LoginSession: id : int, sessionToken : String, loginTime : DateTime, expiresAt : DateTime, device : String
1.3. Bước 3 – Chuyển quan hệ
Client kế thừa User: generalization (khách hàng là User có vai trò CLIENT)
Employee kế thừa User: generalization (nhân viên là User có vai trò EMPLOYEE)
Client o-- MembershipTier: aggregation (hạng hội viên là danh mục độc lập, chỉ khách hàng có)
User *-- OTP: composition (OTP không tồn tại độc lập)
User *-- LoginSession: composition (phiên không tồn tại độc lập)
1.4. Bước 4 – Bổ sung thuộc tính kiểu đối tượng
Client: membershipTier : MembershipTier
OTP: user : User
LoginSession: user : User
1.5. Biểu đồ lớp thực thể

2. Thiết kế CSDL
2.1. Bước 1 – Tạo bảng
Ánh xạ kế thừa kiểu single-table: gộp User, Client, Employee vào một bảng tblUser, dùng cột role để phân biệt; thuộc tính riêng của Client/Employee để NULL khi không áp dụng.

2.2. Bước 2 – Chuyển kiểu dữ liệu
2.3. Bước 3 – Xử lý cardinality
Client – MembershipTier (n-1): tblUser có FK tblMembershipTierMa (chỉ dòng role = CLIENT dùng, NULL với dòng khác)
User – OTP (1-n): tblOTP có FK tblUserMa
User – LoginSession (1-n): tblLoginSession có FK tblUserMa
2.4. Bước 4 – PK/FK
PK: ma : integer(10) <<PK>>
FK: tbl[TenBangCha]Ma : integer(10) <<FK>>
Cột role (CLIENT / EMPLOYEE / ADMIN) phân biệt loại người dùng trong bảng tblUser gộp
2.5. Biểu đồ ERD

3. Thiết kế giao diện
3.1. Màn hình đăng nhập
┌──────────────────────────────────────────────┐ │           	Đăng nhập                       			                  	       │ │                                                                                                                                 │ │  txtPhoneNumber: [_______________________]                                                 │ │  txtPassword:	[_______________________]                                                │ │                                                                                                                                 │ │  [btnLogin]                              	                                                                               │ │  lnkForgotPassword  |  lnkRegister       	                                                              │ └──────────────────────────────────────────────┘
3.2. Màn hình đăng ký
┌──────────────────────────────────────────────┐ │       	Đăng ký tài khoản              	         				     │ │                                              					     │ │  txtFullName:    	[___________________]                                                            │ │  txtPhoneNumber: 	[___________________]   			     │ │  txtEmail:       	[___________________]   				     │ │  txtPassword:    	[___________________]   				      │ │  txtConfirmPassword: [___________________]                                                    │ │                                                                                                                                  │ │  [btnContinue]           	[Cancel]    	                                                      │ └──────────────────────────────────────────────┘
3.3. Màn hình xác nhận OTP
┌──────────────────────────────────────────────┐ │       	Xác nhận OTP                   	                                                                     │ │                                                                                                                                 │ │  txtOTP: [__][__][__][__][__][__]        	                                                     │ │                                              					     │ │  [btnConfirm]                            					     │ │  btnResendOTP                            					      │ └──────────────────────────────────────────────┘
3.4. Màn hình đổi mật khẩu
┌──────────────────────────────────────────────┐ │       	Đổi mật khẩu                   	│ │                                              │ │  txtCurrentPassword:	[________________]   │ │  txtNewPassword:    	[________________]   │ │  txtConfirmNewPassword: [________________]   │ │                                              │ │  [btnSave]               	[Cancel]    	│ └──────────────────────────────────────────────┘
3.5. Màn hình hồ sơ cá nhân
┌──────────────────────────────────────────────┐ │       	Hồ sơ cá nhân                  	│ │                                              │ │  lblFullName:   	[_____________________]  │ │  lblPhoneNumber:	[__________] (readonly)  │ │  lblEmail:      	[_____________________]  │ │  lblMembershipTier: [Bạc  	] (readonly)   │ │  lblLoyaltyPoints:  [1250     ] (readonly)   │ │                                              │ │  [btnEdit]	[btnChangePassword]        	│ └──────────────────────────────────────────────┘
3.6. Màn hình quản lý nhân viên
┌──────────────────────────────────────────────┐ │    	Quản lý tài khoản nhân viên       	│ │                                              │ │  [btnAdd]                                	│ │                                              │ │ ┌──────────┬───────────┬──────────┐          │ │ │ fullName │ staffRole │ status   │      	│ │ │ ........ │ ......... │ ........ │          │ │ │ ........ │ ......... │ ........ │          │ │ └──────────┴───────────┴──────────┘          │ │          	tblStaffList                	│ │                                              │ │  [btnEdit]	[btnDelete]                	│ └──────────────────────────────────────────────┘

4. Thiết kế mô hình MVC
4.1. Tổng quan kiến trúc
Mô hình thiết kế theo kiến trúc MVC (Boundary – Control – Entity):
Boundary: LoginPage, RegisterPage, OTPVerifyPage, ChangePasswordPage, ProfilePage, StaffManagePage
Control: AuthController, ProfileController, StaffController
Entity: User, Client, Employee, MembershipTier, OTP, LoginSession
4.2. Quy trình xác định chữ ký hàm Controller
a) Đăng nhập → checkLogin()
Input: username, password
Output: boolean
Ứng viên tham số vào: checkLogin() → chọn (gom nhóm tham số)
Ứng viên tham số ra: checkLogin(): boolean → chọn (trả về true/false xác thực)
b) Đăng ký → register()
Input: fullName, phoneNumber, email, password
Output: User (vừa tạo)
Ứng viên tham số vào: register() → chọn
Ứng viên tham số ra: register(): User → chọn
c) Xác minh OTP → verifyOTP()
Input: otp
Output: boolean
 Ứng viên tham số vào: verifyOTP() → chọn
Ứng viên tham số ra: verifyOTP(): boolean → chọn (cần biết đúng/sai)
d) Đổi mật khẩu → changePassword()
 Input: currentPassword, newPassword
Output: boolean
Ứng viên tham số vào: changePassword() → chọn
Ứng viên tham số ra: changePassword(): boolean → chọn
e) Xem hồ sơ → getProfile()
Input: userId
Output: User
Ứng viên tham số vào: getProfile() → chọn
Ứng viên tham số ra: getProfile(): User → chọn
f) Cập nhật hồ sơ → updateProfile()
Input: userId, fullName, email
Output: User
Ứng viên tham số vào: updateProfile() → chọn
Ứng viên tham số ra: updateProfile(): User → chọn
g) Xem danh sách NV → getAllStaff()
Input: (không có)
Output: List<Employee>
Ứng viên tham số vào: getAllStaff() → chọn
Ứng viên tham số ra: getAllStaff(): List<Employee> → chọn
h) Tìm kiếm NV → searchStaff()
Input: keyword
Output: List<Employee>
Ứng viên tham số vào: searchStaff(keyword: String) → chọn
Ứng viên tham số ra: searchStaff(): List<Employee> → chọn
i) Lấy NV theo id → getStaffById()
Input: id
Output: Employee
Ứng viên tham số vào: getStaffById(id: int) → chọn
Ứng viên tham số ra: getStaffById(): Employee → chọn
j) Thêm NV → saveStaff()
Input: employee
Output: boolean
Ứng viên tham số vào: saveStaff(employee: Employee) → chọn
Ứng viên tham số ra: saveStaff(): boolean → chọn (cần biết thành công/thất bại)
k) Sửa NV → updateStaff()
Input: employee
Output: boolean
Ứng viên tham số vào: updateStaff() → chọn
Ứng viên tham số ra: updateStaff(): boolean → chọn
l) Xóa NV → deleteStaff()
Input: id
Output: boolean
Ứng viên tham số vào: deleteStaff() → chọn
Ứng viên tham số ra: deleteStaff(): boolean → chọn (cần biết thành công/thất bại)

5. Biểu đồ tuần tự thiết kế
5.1. Đăng nhập

Kịch bản phiên bản 3 – UC01 Đăng nhập
 KH → LoginPage: truy cập URL /login.
 LoginPage → LoginPage: formLoad().
 LoginPage → KH: render form đăng nhập.
 KH → LoginPage: nhập txtPhoneNumber và txtPassword.
 KH → LoginPage: click btnLogin.
 LoginPage → LoginPage: btnLoginClick().
 LoginPage → AuthController: checkLogin().
 AuthController → User: findBySDT().
 User → AuthController: return User.
AuthController → AuthController: checkPassword().
AuthController → LoginPage: return true.
LoginPage → LoginPage: redirect /home.
LoginPage → KH: showMessage("Đăng nhập thành công").
5.2. Đăng ký

Kịch bản phiên bản 3 – UC02 Đăng ký
 KH → RegisterPage: click lnkRegister từ trang /login.
 RegisterPage → RegisterPage: formLoad().
 RegisterPage → KH: render form đăng ký.
 KH → RegisterPage: nhập txtFullName, txtPhoneNumber, txtEmail, txtPassword.
 KH → RegisterPage: click btnContinue.
 RegisterPage → RegisterPage: btnTiepTucClick().
 RegisterPage → AuthController: register().
 AuthController → User: existsBySDT().
 User → AuthController: return false.
AuthController → User: existsByEmail().
User → AuthController: return false.
AuthController → User: save().
User → AuthController: return User.
AuthController → OTP: sendOTP().
OTP → AuthController: return OTP sent.
AuthController → RegisterPage: return User.
RegisterPage → KH: hiển thị OTPVerifyPage.
KH → OTPVerifyPage: nhập txtOTP.
KH → OTPVerifyPage: click btnConfirm.
OTPVerifyPage → OTPVerifyPage: btnXacNhanClick().
OTPVerifyPage → AuthController: verifyOTP().
AuthController → OTP: verify().
OTP → AuthController: return true.
AuthController → OTPVerifyPage: return true.
OTPVerifyPage → KH: showMessage("Đăng ký thành công!").
5.3. Đổi mật khẩu

Kịch bản phiên bản 3 – UC03 Đổi mật khẩu
 Người dùng → ChangePasswordPage: truy cập URL /security.
 ChangePasswordPage → ChangePasswordPage: formLoad().
 ChangePasswordPage → Người dùng: render form đổi mật khẩu.
 Người dùng → ChangePasswordPage: nhập txtCurrentPassword, txtNewPassword, txtConfirmNewPassword.
 Người dùng → ChangePasswordPage: click btnSave.
 ChangePasswordPage → ChangePasswordPage: btnLuuClick().
 ChangePasswordPage → AuthController: changePassword().
 AuthController → User: findById().
 User → AuthController: return User.
  AuthController → AuthController: checkPassword().
AuthController → AuthController: hashPassword().
AuthController → User: updatePassword().
User → AuthController: return true.
AuthController → User: revokeAllSessions().
User → AuthController: return void.
AuthController → ChangePasswordPage: return true.
ChangePasswordPage → Người dùng: showMessage("Đổi mật khẩu thành công. Vui lòng đăng nhập lại.").
5.4. Quản lý TTCN

Kịch bản phiên bản 3 – UC04 Quản lý TTCN
 KH → ProfilePage: click avatar / tên tài khoản.
 ProfilePage → ProfilePage: formLoad().
 ProfilePage → ProfileController: getProfile().
 ProfileController → User: findById().
 User → ProfileController: return User.
 ProfileController → ProfilePage: return User.
 ProfilePage → ProfilePage: displayProfile().
 ProfilePage → KH: render hồ sơ cá nhân.
 KH → ProfilePage: click btnEdit.
KH → ProfilePage: sửa lblFullName và lblEmail.
KH → ProfilePage: click [Lưu].
ProfilePage → ProfilePage: btnChinhSuaClick().
ProfilePage → ProfileController: updateProfile().
ProfileController → User: checkEmail().
User → ProfileController: return true.
ProfileController → User: save().
User → ProfileController: return User.
ProfileController → ProfilePage: return User.
ProfilePage → ProfilePage: displayProfile().
ProfilePage → KH: showMessage("Cập nhật thành công!").
5.5. Quản lý nhân viên

Kịch bản phiên bản 3 – UC20 Quản lý nhân viên
 Admin → StaffManagePage: truy cập URL /admin/staff.
 StaffManagePage → StaffManagePage: formLoad().
 StaffManagePage → StaffController: getAllStaff().
 StaffController → Employee: findAll().
 Employee → StaffController: return List<Employee>.
 StaffController → StaffManagePage: return List<Employee>.
 StaffManagePage → StaffManagePage: displayStaffList().
 StaffManagePage → Admin: render tblStaffList.
 Admin → StaffManagePage: click btnAdd.
Admin → StaffManagePage: nhập fullName và staffRole.
Admin → StaffManagePage: click [Lưu].
StaffManagePage → StaffManagePage: btnThemClick().
StaffManagePage → StaffController: saveStaff().
StaffController → Employee: save().
Employee → StaffController: return Employee.
StaffController → StaffManagePage: return true.
StaffManagePage → StaffManagePage: displayStaffList().
StaffManagePage → Admin: showMessage("Thêm nhân viên thành công!").
Admin → StaffManagePage: click btnDelete trên dòng nhân viên.
StaffManagePage → StaffManagePage: btnXoaClick().
StaffManagePage → StaffController: deleteStaff().
StaffController → Employee: deleteById().
Employee → StaffController: return true.
StaffController → StaffManagePage: return true.
StaffManagePage → StaffManagePage: displayStaffList().
StaffManagePage → Admin: showMessage("Xóa nhân viên thành công!").
 
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
 

