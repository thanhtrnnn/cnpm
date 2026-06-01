# Tài khoản & Thành viên


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
UC01 – Đăng nhập (5 bước)

Kịch bản phiên bản 2 – UC01 Đăng nhập (5 bước)
1.     Người dùng chọn chức năng Đăng nhập.
2.     Lớp LoginView hiển thị giao diện đăng nhập.
3.     Người dùng nhập SĐT/Email và Mật khẩu, nhấn nút Đăng nhập.
4.     Lớp LoginView gọi hàm checkLogin() của đối tượng User để xác thực.
5.     Lớp LoginView chuyển hướng trang chủ, hiển thị "Đăng nhập thành công".
UC02 – Đăng ký (8 bước)

Kịch bản phiên bản 2 – UC02 Đăng ký (8 bước)
6.     Khách hàng chọn liên kết Đăng ký từ giao diện đăng nhập.
7.     Lớp RegisterView hiển thị giao diện đăng ký.
8.     Khách hàng nhập Họ tên, SĐT, Email, Mật khẩu, Xác nhận mật khẩu, nhấn Tiếp tục.
9.     Lớp RegisterView gọi hàm register() của đối tượng User.
10.  Lớp User kiểm tra thông tin hợp lệ, gọi hàm sendOTP() của đối tượng OTP.
11.  Lớp RegisterView hiển thị giao diện xác nhận OTP.
12.  Khách hàng nhập mã OTP, nhấn Xác nhận. Lớp OTPVerifyView gọi hàm verifyOTP() của đối tượng OTP.
13.  Lớp OTPVerifyView gọi hàm saveUser() của đối tượng User, hiển thị "Đăng ký thành công!".
UC03 – Đổi mật khẩu (5 bước)

Kịch bản phiên bản 2 – UC03 Đổi mật khẩu (5 bước)
14.  Người dùng chọn chức năng Đổi mật khẩu.
15.  Lớp ChangePasswordView hiển thị giao diện đổi mật khẩu.
16.  Người dùng nhập Mật khẩu hiện tại, Mật khẩu mới, Xác nhận mật khẩu mới, nhấn Lưu.
17.  Lớp ChangePasswordView gọi hàm changePassword() của đối tượng User.
18.  Lớp ChangePasswordView hiển thị "Đổi mật khẩu thành công", chuyển hướng về đăng nhập.
UC04 – Quản lý thông tin cá nhân (7 bước)

Kịch bản phiên bản 2 – UC04 Quản lý thông tin cá nhân (7 bước)
19.  Khách hàng chọn chức năng Hồ sơ cá nhân.
20.  Lớp ProfileView gọi hàm getProfile() của đối tượng User.
21.  Lớp ProfileView hiển thị trang hồ sơ cá nhân.
22.  Khách hàng nhấn nút Chỉnh sửa.
23.  Lớp ProfileView chuyển sang chế độ chỉnh sửa.
24.  Khách hàng cập nhật Họ tên, Email, nhấn Lưu. Lớp ProfileView gọi hàm updateProfile() của đối tượng User.
25.  Lớp ProfileView hiển thị "Cập nhật thành công!", quay về chế độ xem.
UC20 – Quản lý tài khoản nhân viên (14 bước)

Kịch bản phiên bản 2 – UC20 Quản lý tài khoản nhân viên (14 bước)
26.  Admin chọn chức năng Quản lý nhân viên.
27.  Lớp StaffManageView gọi hàm getAllStaff() của đối tượng Employee.
28.  Lớp StaffManageView hiển thị danh sách nhân viên.
29.  Admin nhấn nút Thêm nhân viên.
30.  Lớp StaffManageView hiển thị giao diện nhập thông tin.
31.  Admin nhập Họ tên, SĐT, Vai trò, Chi nhánh, nhấn Lưu.
32.  Lớp StaffManageView gọi hàm addStaff() của đối tượng Employee.
33.  Lớp StaffManageView hiển thị "Thêm nhân viên thành công!".
34.  Admin nhấn nút Sửa trên dòng Nguyễn Minh Tuấn.
35.  Lớp StaffManageView hiển thị giao diện chỉnh sửa.
36.  Admin cập nhật thông tin, nhấn Lưu.
37.  Lớp StaffManageView gọi hàm updateStaff() của đối tượng Employee.
38.  Admin nhấn nút Xóa trên dòng Lê Văn Khánh.
39.  Lớp StaffManageView yêu cầu xác nhận, hiển thị "Xóa nhân viên thành công!".

