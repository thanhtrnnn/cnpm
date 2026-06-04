# Tài khoản & Thành viên



| HỌC VIỆN CÔNG NGHỆ BƯU CHÍNH VIỄN THÔNG KHOA CÔNG NGHỆ THÔNG TIN 1 ______________ |
| --- |
| ![image_01](screenshots/image_01.png) |
| BÁO CÁO BÀI TẬP LỚN HỌC PHẦN: NHẬP MÔN CÔNG NGHỆ PHẦN MỀM Module: Tài khoản và thành viên |
| Giảng viên hướng dẫn: Đỗ Thị Liên Lớp học phần: D23CQCE01-B Nhóm thực hiện: Nhóm 7 SV thực hiện: Trần Xuân Thành MSV: B23DCAT280 |
| HÀ NỘI, THÁNG 5/2026 |

# MỤC LỤC
# 
# I. PHA XÁC ĐỊNH YÊU CẦU
## 1. Danh sách Use Case

| Mã UC | Tên Use Case | Actor chính | Mô tả ngắn |
| --- | --- | --- | --- |
| UC01 | Đăng nhập | Khách hàng, Nhân viên | Cho phép người dùng xác thực danh tính; bao gồm đăng ký tài khoản mới và đổi mật khẩu |
| UC02 | Đăng ký | Khách hàng | Tạo tài khoản mới (sub-UC của UC01, kích hoạt khi chọn Đăng ký) |
| UC03 | Đổi mật khẩu | Khách hàng, Nhân viên | Đổi mật khẩu tài khoản (sub-UC của UC01, kích hoạt từ trang Profile) |
| UC04 | Quản lý thông tin cá nhân | Khách hàng | Xem & cập nhật hồ sơ cá nhân |
| UC20 | Quản lý tài khoản nhân viên | Chủ Doanh nghiệp (Admin) | Tạo, sửa, xóa tài khoản nhân viên |

## 2. Danh sách Actor

| STT | Actor | Mô tả |
| --- | --- | --- |
| 1 | Khách hàng | Người dùng sử dụng dịch vụ karaoke, truy cập qua web/app để đăng ký, đăng nhập, quản lý tài khoản |
| 2 | Nhân viên | Nhân viên tại chi nhánh, sử dụng hệ thống để xử lý nghiệp vụ |
| 3 | Chủ Doanh nghiệp (Admin) | Chủ sở hữu chuỗi, quản lý tài khoản nhân viên toàn hệ thống |

## 3. UC con và quan hệ Include/Extend

| UC cha | UC con | Quan hệ | Lý do |
| --- | --- | --- | --- |
| UC01 – Xác thực người dùng | Nhập thông tin đăng nhập | include | Bắt buộc – luôn phải nhập tài khoản và mật khẩu |
| UC01 – Xác thực người dùng | Đăng ký | include | Khi người dùng chưa có tài khoản, nhấn Đăng ký |
| UC01 – Xác thực người dùng | Quên mật khẩu | extend | Khi người dùng nhấn "Quên mật khẩu?" |
| UC02 – Đăng ký | Điền thông tin đăng ký | include | Bắt buộc – không thể đăng ký mà không điền thông tin |
| UC02 – Đăng ký | Xác thực OTP | include | Bắt buộc – xác minh SĐT trước khi tạo tài khoản |
| UC03 – Đổi mật khẩu | Đổi mật khẩu | include | Khi người dùng muốn thay đổi mật khẩu |
| UC03 – Đổi mật khẩu | Nhập thông tin đổi mật khẩu | include | Bắt buộc – phải nhập MK mới và xác nhận |
| UC04 – Quản lý TTCN | Chỉnh sửa thông tin cá nhân | include | Khi người dùng chọn chỉnh sửa thông tin |
| UC04 – Quản lý TTCN | Chỉnh sửa thông tin | extend | Chỉ khi người dùng chọn chỉnh sửa |
| UC20 – Quản lý NV | Thêm nhân viên mới | include | Khi Admin chọn thêm nhân viên |
| UC20 – Quản lý NV | Thêm nhân viên | extend | Chỉ khi quản lý chọn thêm |
| UC20 – Quản lý NV | Sửa nhân viên | extend | Chỉ khi quản lý chọn sửa |
| UC20 – Quản lý NV | Xóa nhân viên | extend | Chỉ khi quản lý chọn xóa |

## 4. Biểu đồ Use Case tổng quan
![image_02](screenshots/image_02.png)
### Bước 1 – Copy UC + Actor từ hệ thống:

| Mã UC | Tên UC | Actor |
| --- | --- | --- |
| UC01 | Đăng nhập | Khách hàng, Nhân viên, Chủ DN |
| UC02 | Đăng ký | Khách hàng |
| UC03 | Đổi mật khẩu | Khách hàng, Nhân viên |
| UC04 | Quản lý TTCN | Khách hàng |
| UC20 | Quản lý NV | Chủ DN |

### Bước 2 – Đề xuất UC con từ giao diện:

| UC chính | Giao diện → UC con |
| --- | --- |
| UC01 | Form đăng nhập → Nhập thông tin đăng nhập; Đăng ký; Quên mật khẩu |
| UC02 | Form đăng ký → Điền thông tin đăng ký; Xác thực OTP |
| UC03 | Form đổi MK → Đổi mật khẩu; Nhập thông tin đổi mật khẩu |
| UC04 | Trang hồ sơ → Chỉnh sửa thông tin cá nhân; Chỉnh sửa thông tin |
| UC20 | Trang quản lý NV → Thêm NV (extend); Sửa NV (extend); Xóa NV (extend) |

### Bước 3 – Xác định quan hệ include/extend:

| UC cha | UC con | Quan hệ | Lý do |
| --- | --- | --- | --- |
| UC01 | Nhập thông tin đăng nhập | include | Bắt buộc – luôn phải nhập thông tin khi xác thực |
| UC01 | Đăng ký | include | Khi người dùng chưa có tài khoản, nhấn Đăng ký |
| UC01 | Quên mật khẩu | extend | Chỉ khi nhấn "Quên mật khẩu?" |
| UC02 | Điền thông tin đăng ký | include | Bắt buộc – không thể đăng ký mà không điền |
| UC02 | Xác thực OTP | include | Bắt buộc – phải xác minh SĐT |
| UC03 | Đổi mật khẩu | include | Khi actor muốn thay đổi mật khẩu |
| UC03 | Nhập thông tin đổi mật khẩu | include | Bắt buộc – phải nhập MK mới + xác nhận |
| UC04 | Chỉnh sửa thông tin cá nhân | include | Khi actor muốn cập nhật thông tin cá nhân |
| UC04 | Chỉnh sửa thông tin | extend | Chỉ khi chọn chỉnh sửa |
| UC20 | Xem danh sách NV | include | Khi Admin muốn thêm nhân viên mới |
| UC20 | Thêm NV | extend | Chỉ khi chọn thêm |
| UC20 | Sửa NV | extend | Chỉ khi chọn sửa |
| UC20 | Xóa NV | extend | Chỉ khi chọn xóa |

## 5. Biểu đồ Use Case chi tiết
### UC01 – Xác thực người dùng
![image_03](screenshots/image_03.png)![image_04](screenshots/image_04.png)
### UC02 – Đăng ký
![image_05](screenshots/image_05.png)
### UC03 – Đổi mật khẩu
![image_06](screenshots/image_06.png)
### UC04 – Quản lý TTCN
![image_07](screenshots/image_07.png)
### UC20 – Quản lý nhân viên
![image_08](screenshots/image_08.png)
 
# II. PHA PHÂN TÍCH
## 1. Kịch bản chuẩn
### UC01 – Xác thực người dùng

| Use case | Đăng nhập |
| --- | --- |
| Actor | Khách hàng, Nhân viên |
| Tiền điều kiện | Người dùng chưa đăng nhập. Tài khoản đã tồn tại trong hệ thống. |
| Hậu điều kiện | Người dùng được xác thực, chuyển hướng đến trang chủ. |
| Kịch bản chính | 1. Người dùng chọn chức năng "Đăng nhập". 2. Hệ thống hiển thị giao diện đăng nhập có ô nhập SĐT/Email, ô nhập Mật khẩu, nút Đăng nhập, liên kết "Quên mật khẩu?" và "Đăng ký". 3. Người dùng nhập SĐT/Email và Mật khẩu. 4. Người dùng nhấn nút Đăng nhập. 5. Hệ thống xác thực thành công, chuyển hướng đến trang chủ và hiển thị thông báo "Đăng nhập thành công". |
| Ngoại lệ | 5. Hệ thống thông báo "Tài khoản không tồn tại". 5.1 Người dùng chọn liên kết "Đăng ký" (chuyển sang UC02). 5. Hệ thống thông báo "Sai mật khẩu". 5.1 Người dùng nhập lại mật khẩu (quay về Bước 4). |

### UC02 – Đăng ký

| Use case | Đăng ký |
| --- | --- |
| Actor | Khách hàng |
| Tiền điều kiện | Người dùng chưa có tài khoản. |
| Hậu điều kiện | Tài khoản mới được tạo, đăng nhập tự động. |
| Kịch bản chính | 1. Người dùng chọn liên kết "Đăng ký" từ giao diện đăng nhập. 2. Hệ thống hiển thị giao diện đăng ký có ô nhập Họ tên, SĐT, Email, Mật khẩu, Xác nhận mật khẩu, nút Tiếp tục. 3. Người dùng nhập Họ tên, SĐT, Email, Mật khẩu, Xác nhận mật khẩu. 4. Người dùng nhấn nút Tiếp tục. 5. Hệ thống gửi mã OTP 6 chữ số đến SĐT. 6. Hệ thống hiển thị giao diện xác nhận OTP có ô nhập mã OTP, nút Xác nhận, nút Gửi lại mã. 7. Người dùng nhập mã OTP và nhấn nút Xác nhận. 8. Hệ thống tạo tài khoản mới, tự động đăng nhập và hiển thị thông báo "Đăng ký thành công!". |
| Ngoại lệ | 4. Hệ thống thông báo "SĐT hoặc Email đã được sử dụng". 4.1 Người dùng nhập lại thông tin khác (quay về Bước 4). 7. Hệ thống thông báo "Mã OTP không hợp lệ hoặc đã hết hạn". 7.1 Người dùng nhấn nút Gửi lại mã (quay về Bước 6). |

### UC03 – Đổi mật khẩu

| Use case | Đổi mật khẩu |
| --- | --- |
| Actor | Khách hàng, Nhân viên (đã đăng nhập) |
| Tiền điều kiện | Người dùng đã đăng nhập. |
| Hậu điều kiện | Mật khẩu mới được lưu. Tất cả phiên đăng nhập khác bị thu hồi. |
| Kịch bản chính | 1. Người dùng chọn chức năng "Đổi mật khẩu". 2. Hệ thống hiển thị giao diện có ô nhập Mật khẩu hiện tại, Mật khẩu mới, Xác nhận mật khẩu mới, nút Lưu thay đổi. 3. Người dùng nhập Mật khẩu hiện tại, Mật khẩu mới, Xác nhận mật khẩu mới. 4. Người dùng nhấn nút Lưu thay đổi. 5. Hệ thống cập nhật mật khẩu, thu hồi các phiên khác, hiển thị thông báo "Đổi mật khẩu thành công. Vui lòng đăng nhập lại." và chuyển hướng về giao diện đăng nhập. |
| Ngoại lệ | 4. Hệ thống thông báo "Mật khẩu hiện tại không chính xác". 4.1 Người dùng nhập lại mật khẩu hiện tại (quay về Bước 4). 4. Hệ thống thông báo "Mật khẩu mới không hợp lệ". 4.1 Người dùng nhập lại mật khẩu mới (quay về Bước 4). |

### UC04 – Quản lý thông tin cá nhân

| Use case | Quản lý thông tin cá nhân |
| --- | --- |
| Actor | Khách hàng (đã đăng nhập) |
| Tiền điều kiện | Khách hàng đã đăng nhập. |
| Hậu điều kiện | Thông tin cá nhân được cập nhật. |
| Kịch bản chính | 1. Khách hàng chọn chức năng "Hồ sơ cá nhân". 2. Hệ thống hiển thị trang hồ sơ cá nhân: 3. Khách hàng nhấn nút Chỉnh sửa. 4. Hệ thống chuyển sang chế độ chỉnh sửa: Họ tên và Email cho phép sửa, SĐT bị khóa. 5. Khách hàng cập nhật Họ tên và Email. 6. Khách hàng nhấn nút Lưu thay đổi. 7. Hệ thống hiển thị thông báo "Cập nhật thành công!" và quay về chế độ xem. |
| Ngoại lệ | 6. Hệ thống thông báo "Email không hợp lệ hoặc đã được sử dụng". 6.1 Khách hàng nhập lại email khác (quay về Bước 6). |

### UC20 – Quản lý tài khoản nhân viên

| Use case | Quản lý tài khoản nhân viên |
| --- | --- |
| Actor | Chủ Doanh nghiệp (Admin) |
| Tiền điều kiện | Admin đã đăng nhập với quyền quản lý nhân viên. |
| Hậu điều kiện | Tài khoản nhân viên được tạo/sửa/xóa. |
| Kịch bản chính | 1. Admin chọn chức năng "Quản lý nhân viên". 2. Hệ thống hiển thị danh sách nhân viên: 3. Admin nhấn nút Thêm nhân viên. 4. Hệ thống hiển thị giao diện nhập Họ tên, SĐT, Vai trò, Chi nhánh. 5. Admin nhập thông tin và nhấn nút Lưu. 6. Hệ thống hiển thị thông báo "Thêm nhân viên thành công!" và cập nhật danh sách. 7. Admin nhấn nút Sửa trên dòng nhân viên Nguyễn Minh Tuấn. 8. Hệ thống hiển thị giao diện chỉnh sửa với thông tin hiện tại. 9. Admin cập nhật thông tin và nhấn nút Lưu. 10. Hệ thống hiển thị thông báo "Cập nhật thành công!". 11. Admin nhấn nút Xóa trên dòng nhân viên Lê Văn Khánh. 12. Hệ thống yêu cầu xác nhận xóa. 13. Admin xác nhận xóa. 14. Hệ thống hiển thị thông báo "Xóa nhân viên thành công!". |
| Ngoại lệ | 5. Hệ thống thông báo "SĐT đã được sử dụng". 5.1 Admin nhập lại SĐT khác (quay về Bước 5). 13. Hệ thống thông báo "Không thể xóa nhân viên đang xử lý order". 13.1 Admin hủy thao tác xóa. |


## 2. Mô hình hóa lớp
### Bước 1 – Mô tả chức năng bằng đoạn văn xuôi
Hệ thống cho phép khách hàng đăng ký tài khoản hội viên mới bằng cách cung cấp họ tên, số điện thoại, email và mật khẩu; sau đó xác minh số điện thoại qua mã OTP trước khi hoàn tất đăng ký. Mỗi tài khoản gắn liền với một hạng hội viên (Thường, Bạc, Vàng, Kim Cương) dựa trên điểm tích lũy. Người dùng sau khi đăng nhập có thể xem và cập nhật thông tin cá nhân như họ tên và email, hoặc thực hiện đổi mật khẩu bằng cách xác minh mật khẩu cũ rồi nhập mật khẩu mới. Hệ thống ghi nhận các phiên đăng nhập để phục vụ bảo mật và thu hồi phiên khi đổi mật khẩu. Ngoài ra, chủ doanh nghiệp có quyền quản lý tài khoản nhân viên: tạo, chỉnh sửa và xóa tài khoản nhân viên trong hệ thống.
### Bước 2 + 3 – Trích danh từ và đánh giá
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
### Bước 4 – Xác định quan hệ số lượng
1 User có 1 MembershipTier → User – MembershipTier: n – 1 (nhiều người dùng có thể có cùng hạng)
1 User có nhiều OTP → User – OTP: 1 – n (mỗi lần đăng ký/đổi SĐT tạo 1 OTP mới)
1 User có nhiều LoginSession → User – LoginSession: 1 – n (người dùng có thể đăng nhập trên nhiều thiết bị)
### Bước 5 – Bổ sung quan hệ
User gắn composition với OTP: một OTP không tồn tại độc lập nếu không có User tương ứng (khi xóa User thì xóa theo tất cả OTP). Tương tự, LoginSession không tồn tại độc lập khỏi User. Quan hệ với MembershipTier là aggregation: MembershipTier là dữ liệu danh mục tồn tại độc lập với User. Employee là lớp riêng biệt, không kế thừa từ User.
Biểu đồ thực thể Module Tài khoản & Thành viên:
![image_09](screenshots/image_09.png)
## 3. Biểu đồ lớp phân tích
### 3.1. Phân tích chi tiết chức năng "Đăng nhập"
Người dùng truy cập trang đăng nhập -> đề xuất lớp LoginView, có ô nhập SĐT, ô nhập mật khẩu, nút Đăng nhập.
Người dùng nhập SĐT, mật khẩu và nhấn nút Đăng nhập -> hệ thống cần xác thực tài khoản -> cần chức năng checkLogin() của đối tượng User.
Nếu tài khoản không tồn tại -> hệ thống hiển thị thông báo lỗi.
Nếu mật khẩu sai -> hệ thống hiển thị thông báo lỗi.
Hoàn tất, hệ thống tạo phiên đăng nhập và chuyển hướng trang chủ.
Boundary: LoginView
Entity: User
### 3.2. Phân tích chi tiết chức năng "Đăng ký"
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
![image_10](screenshots/image_10.png)
## 4. Biểu đồ tuần tự phân tích
### UC01 – Xác thực người dùng (7 bước)
![image_11](screenshots/image_11.png)
Kịch bản phiên bản 2 – UC01 Đăng nhập (7 bước)
 Actor → LoginView: chọn chức năng Đăng nhập.
 LoginView → Actor: hiển thị giao diện đăng nhập.
 Actor → LoginView: nhập txtPhoneNumber + txtPassword, nhấn Đăng nhập.
 LoginView → User: checkLogin(phoneNumber, password).
 User → LoginView: return kết quả xác thực.
 LoginView → HomeView: chuyển hướng, "Đăng nhập thành công".
 HomeView → Actor: hiển thị trang chủ.
### UC02 – Đăng ký (17 bước)
![image_12](screenshots/image_12.png)
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
### UC03 – Đổi mật khẩu (8 bước)
![image_13](screenshots/image_13.png)
Kịch bản phiên bản 2 – UC03 Đổi mật khẩu (8 bước)
 Actor → ChangePasswordView: chọn chức năng Đổi mật khẩu.
 ChangePasswordView → Actor: hiển thị giao diện đổi mật khẩu.
 Actor → ChangePasswordView: nhập txtCurrentPassword, txtNewPassword, txtConfirmNewPassword, nhấn Lưu.
 ChangePasswordView → User: changePassword(currentPassword, newPassword).
 User → ChangePasswordView: return đổi mật khẩu thành công.
 ChangePasswordView → Actor: "Đổi mật khẩu thành công".
 ChangePasswordView → LoginView: chuyển hướng về giao diện Đăng nhập.
 LoginView → Actor: hiển thị trang đăng nhập.
### UC04 – Quản lý thông tin cá nhân (10 bước)
![image_14](screenshots/image_14.png)
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
### UC20 – Quản lý tài khoản nhân viên (18 bước)
![image_15](screenshots/image_15.png)
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
# 
# III. PHA THIẾT KẾ
## 1. Thiết kế lớp thực thể
### 1.1. Bước 1 – Bổ sung thuộc tính id
 User: id : int — lớp gốc; Client và Employee kế thừa id này
 MembershipTier: id : int
 OTP: id : int
 LoginSession: id : int
### 1.2. Bước 2 – Thêm kiểu dữ liệu
 User (lớp cha): id : int, fullName : String, phoneNumber : String, email : String, password : String, role : String, createdAt : Date
 Client (kế thừa User): loyaltyPoints : int, joinedAt : Date
 Employee (kế thừa User): staffRole : String, branch : String, status : String
 MembershipTier: id : int, tierName : String, minPoints : int, description : String, discountRate : double
 OTP: id : int, otpCode : String, type : String, expiresAt : Date, verified : boolean
LoginSession: id : int, sessionToken : String, loginTime : DateTime, expiresAt : DateTime, device : String
### 1.3. Bước 3 – Chuyển quan hệ
Client kế thừa User: generalization (khách hàng là User có vai trò CLIENT)
Employee kế thừa User: generalization (nhân viên là User có vai trò EMPLOYEE)
Client o-- MembershipTier: aggregation (hạng hội viên là danh mục độc lập, chỉ khách hàng có)
User *-- OTP: composition (OTP không tồn tại độc lập)
User *-- LoginSession: composition (phiên không tồn tại độc lập)
### 1.4. Bước 4 – Bổ sung thuộc tính kiểu đối tượng
Client: membershipTier : MembershipTier
OTP: user : User
LoginSession: user : User
### 1.5. Biểu đồ lớp thực thể
![image_16](screenshots/image_16.png)
## 2. Thiết kế CSDL
### 2.1. Bước 1 – Tạo bảng
Ánh xạ kế thừa kiểu single-table: gộp User, Client, Employee vào một bảng tblUser, dùng cột role để phân biệt; thuộc tính riêng của Client/Employee để NULL khi không áp dụng.

| Lớp thực thể | Tên bảng |
| --- | --- |
| User, Client, Employee (kế thừa) | tblUser |
| MembershipTier | tblMembershipTier |
| OTP | tblOTP |
| LoginSession | tblLoginSession |

### 
### 2.2. Bước 2 – Chuyển kiểu dữ liệu

| Kiểu Java | Kiểu SQL |
| --- | --- |
| int | integer(10) |
| String | varchar(255) |
| double | double(10) |
| Date | date |
| DateTime | datetime |
| boolean | bit |

### 2.3. Bước 3 – Xử lý cardinality
Client – MembershipTier (n-1): tblUser có FK tblMembershipTierMa (chỉ dòng role = CLIENT dùng, NULL với dòng khác)
User – OTP (1-n): tblOTP có FK tblUserMa
User – LoginSession (1-n): tblLoginSession có FK tblUserMa
### 2.4. Bước 4 – PK/FK
PK: ma : integer(10) <<PK>>
FK: tbl[TenBangCha]Ma : integer(10) <<FK>>
Cột role (CLIENT / EMPLOYEE / ADMIN) phân biệt loại người dùng trong bảng tblUser gộp
### 2.5. Biểu đồ ERD
![image_17](screenshots/image_17.png)
## 3. Thiết kế giao diện
### 3.1. Màn hình đăng nhập
┌──────────────────────────────────────────────┐ │           	Đăng nhập                       			                  	       │ │                                                                                                                                 │ │  txtPhoneNumber: [_______________________]                                                 │ │  txtPassword:	[_______________________]                                                │ │                                                                                                                                 │ │  [btnLogin]                              	                                                                               │ │  lnkForgotPassword  |  lnkRegister       	                                                              │ └──────────────────────────────────────────────┘
### 3.2. Màn hình đăng ký
┌──────────────────────────────────────────────┐ │       	Đăng ký tài khoản              	         				     │ │                                              					     │ │  txtFullName:    	[___________________]                                                            │ │  txtPhoneNumber: 	[___________________]   			     │ │  txtEmail:       	[___________________]   				     │ │  txtPassword:    	[___________________]   				      │ │  txtConfirmPassword: [___________________]                                                    │ │                                                                                                                                  │ │  [btnContinue]           	[Cancel]    	                                                      │ └──────────────────────────────────────────────┘
### 3.3. Màn hình xác nhận OTP
┌──────────────────────────────────────────────┐ │       	Xác thực OTP                   	                                                                     │ │                                                                                                                                 │ │  txtOTP: [__][__][__][__][__][__]        	                                                     │ │                                              					     │ │  [btnConfirm]                            					     │ │  btnResendOTP                            					      │ └──────────────────────────────────────────────┘
### 3.4. Màn hình đổi mật khẩu
┌──────────────────────────────────────────────┐ │       	Đổi mật khẩu                   	│ │                                              │ │  txtCurrentPassword:	[________________]   │ │  txtNewPassword:    	[________________]   │ │  txtConfirmNewPassword: [________________]   │ │                                              │ │  [btnSave]               	[Cancel]    	│ └──────────────────────────────────────────────┘
### 3.5. Màn hình hồ sơ cá nhân
┌──────────────────────────────────────────────┐ │       	Hồ sơ cá nhân                  	│ │                                              │ │  lblFullName:   	[_____________________]  │ │  lblPhoneNumber:	[__________] (readonly)  │ │  lblEmail:      	[_____________________]  │ │  lblMembershipTier: [Bạc  	] (readonly)   │ │  lblLoyaltyPoints:  [1250     ] (readonly)   │ │                                              │ │  [btnEdit]	[btnChangePassword]        	│ └──────────────────────────────────────────────┘
### 3.6. Màn hình quản lý nhân viên
┌──────────────────────────────────────────────┐ │    	Quản lý tài khoản nhân viên       	│ │                                              │ │  [btnAdd]                                	│ │                                              │ │ ┌──────────┬───────────┬──────────┐          │ │ │ fullName │ staffRole │ status   │      	│ │ │ ........ │ ......... │ ........ │          │ │ │ ........ │ ......... │ ........ │          │ │ └──────────┴───────────┴──────────┘          │ │          	tblStaffList                	│ │                                              │ │  [btnEdit]	[btnDelete]                	│ └──────────────────────────────────────────────┘
## 
## 4. Thiết kế mô hình MVC
### 4.1. Tổng quan kiến trúc
Mô hình thiết kế theo kiến trúc MVC (Boundary – Control – Entity):
Boundary: LoginPage, RegisterPage, OTPVerifyPage, ChangePasswordPage, ProfilePage, StaffManagePage
Control: LoginController, ProfileController, StaffController
Entity: User, Client, Employee, MembershipTier, OTP, LoginSession
### 4.2. Quy trình xác định chữ ký hàm Controller
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
![image_18](screenshots/image_18.png)
## 5. Biểu đồ tuần tự thiết kế
### 5.1. Đăng nhập
![image_19](screenshots/image_19.png)
Kịch bản phiên bản 3 – UC01 Đăng nhập
 KH → LoginPage: truy cập URL /login.
 LoginPage → LoginPage: formLoad().
 LoginPage → KH: render form đăng nhập.
 KH → LoginPage: nhập txtPhoneNumber và txtPassword.
 KH → LoginPage: click btnLogin.
 LoginPage → LoginPage: btnLoginClick().
 LoginPage → LoginController: checkLogin().
 LoginController → User: findBySDT().
 User → LoginController: return User.
LoginController → LoginController: checkPassword().
LoginController → LoginPage: return true.
LoginPage → LoginPage: redirect /home.
LoginPage → KH: showMessage("Đăng nhập thành công").
### 5.2. Đăng ký
![image_20](screenshots/image_20.png)
Kịch bản phiên bản 3 – UC02 Đăng ký
 KH → RegisterPage: click lnkRegister từ trang /login.
 RegisterPage → RegisterPage: formLoad().
 RegisterPage → KH: render form đăng ký.
 KH → RegisterPage: nhập txtFullName, txtPhoneNumber, txtEmail, txtPassword.
 KH → RegisterPage: click btnContinue.
 RegisterPage → RegisterPage: btnTiepTucClick().
 RegisterPage → LoginController: register().
 LoginController → User: existsBySDT().
 User → LoginController: return false.
LoginController → User: existsByEmail().
User → LoginController: return false.
LoginController → User: save().
User → LoginController: return User.
LoginController → OTP: sendOTP().
OTP → LoginController: return OTP sent.
LoginController → RegisterPage: return User.
RegisterPage → KH: hiển thị OTPVerifyPage.
KH → OTPVerifyPage: nhập txtOTP.
KH → OTPVerifyPage: click btnConfirm.
OTPVerifyPage → OTPVerifyPage: btnXacNhanClick().
OTPVerifyPage → LoginController: verifyOTP().
LoginController → OTP: verify().
OTP → LoginController: return true.
LoginController → OTPVerifyPage: return true.
OTPVerifyPage → KH: showMessage("Đăng ký thành công!").
### 5.3. Đổi mật khẩu
![image_21](screenshots/image_21.png)
Kịch bản phiên bản 3 – UC03 Đổi mật khẩu
 Người dùng → ChangePasswordPage: truy cập URL /security.
 ChangePasswordPage → ChangePasswordPage: formLoad().
 ChangePasswordPage → Người dùng: render form đổi mật khẩu.
 Người dùng → ChangePasswordPage: nhập txtCurrentPassword, txtNewPassword, txtConfirmNewPassword.
 Người dùng → ChangePasswordPage: click btnSave.
 ChangePasswordPage → ChangePasswordPage: btnLuuClick().
 ChangePasswordPage → LoginController: changePassword().
 LoginController → User: findById().
 User → LoginController: return User.
  LoginController → LoginController: checkPassword().
LoginController → LoginController: hashPassword().
LoginController → User: updatePassword().
User → LoginController: return true.
LoginController → User: revokeAllSessions().
User → LoginController: return void.
LoginController → ChangePasswordPage: return true.
ChangePasswordPage → Người dùng: showMessage("Đổi mật khẩu thành công. Vui lòng đăng nhập lại.").
### 5.4. Quản lý TTCN
![image_22](screenshots/image_22.png)
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
### 5.5. Quản lý nhân viên
![image_23](screenshots/image_23.png)
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
 
# IV. PHA CÀI ĐẶT VÀ KIỂM THỬ
##  1. Lập kế hoạch test

| TT | Module | Test case |
| --- | --- | --- |
| TC01 | Đăng nhập | Đăng nhập thành công |
| TC02 | Đăng nhập | Tài khoản không tồn tại |
| TC03 | Đăng nhập | Mật khẩu sai 5 lần → khóa tài khoản |
| TC04 | Đăng ký | Đăng ký thành công với OTP |
| TC05 | Đăng ký | SĐT đã tồn tại |
| TC06 | Đăng ký | OTP sai 3 lần → hủy phiên |
| TC07 | Đổi mật khẩu | Đổi mật khẩu thành công |
| TC08 | Đổi mật khẩu | Mật khẩu hiện tại sai |
| TC09 | Quản lý TTCN | Cập nhật thông tin thành công |
| TC10 | Quản lý TTCN | Email đã được sử dụng |
| TC11 | Quản lý nhân viên | Thêm nhân viên mới |

## 2. Test case chi tiết
---
### TC01: Đăng nhập thành công
#### Trạng thái CSDL trước:
tblMembershipTier

| ma | tenHang | diemToiThieu | heSoUuDai |
| --- | --- | --- | --- |
| 1 | Thường | 0 | 0.0 |
| 2 | Bạc | 1000 | 0.1 |
| 3 | Vàng | 5000 | 0.2 |
| 4 | Kim Cương | 20000 | 0.5 |

tblUser

| ma | hoTen | soDienThoai | email | matKhau | diemTichLuy | trangThai | tblMembershipTierMa |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Nguyễn Văn A | 0912345678 | vana@email.com | $2a$10$hashAbc1234... | 1250 | Hoạt động | 2 |
| 2 | Lê Thị B | 0987654321 | b.lt@email.com | $2a$10$hashXyz5678... | 0 | Hoạt động | 1 |
| 3 | Phạm Minh C | 0909123456 | pmc@email.com | $2a$10$hashMno9012... | 5200 | Hoạt động | 3 |

tblLoginSession

| ma | tokenPhien | thoiGianDangNhap | thoiGianHetHan | thietBi | tblUserMa |
| --- | --- | --- | --- | --- | --- |
| 1 | tk_old_aaa... | 2026-05-31 08:00 | 2026-05-31 20:00 | Chrome/Win | 1 |

#### Kịch bản thực hiện:

| Bước | Hành động UI | Kết quả mong đợi |
| --- | --- | --- |
| 1 | Mở trình duyệt, truy cập /login | Hiển thị form đăng nhập với 2 ô: "SĐT hoặc Email" và "Mật khẩu", nút [Đăng nhập], link "Chưa có tài khoản? Đăng ký" |
| 2 | Click vào ô "SĐT hoặc Email", nhập 0912345678 | Ô nhập hiển thị 0912345678, viền xanh hợp lệ |
| 3 | Click vào ô "Mật khẩu", nhập Abc@1234 | Ô nhập hiển thị dấu chấm (masked), nút [Đăng nhập] chuyển sang trạng thái active |
| 4 | Nhấn nút [Đăng nhập] | Hệ thống truy vấn tblUser WHERE soDienThoai = '0912345678', tìm thấy ma=1. So sánh bcrypt(password, storedHash) → khớp |
| 5 | Hệ thống tạo LoginSession mới | Tạo token JWT, insert vào tblLoginSession. Chuyển hướng sang trang chủ |
| 6 | Trang chủ hiển thị | Header hiện avatar + "Xin chào, Nguyễn Văn A!", thông báo toast "Đăng nhập thành công" |

#### Trạng thái CSDL sau:
tblUser: Không thay đổi.
tblLoginSession (thêm 1 dòng mới)

| ma | tokenPhien | thoiGianDangNhap | thoiGianHetHan | thietBi | tblUserMa |
| --- | --- | --- | --- | --- | --- |
| 1 | tk_old_aaa... | 2026-05-31 08:00 | 2026-05-31 20:00 | Chrome/Win | 1 |
| 2 | tk_new_bbb... | 2026-06-01 10:00 | 2026-06-01 22:00 | Chrome/Mac | 1 |

---
### TC02: Tài khoản không tồn tại
#### Trạng thái CSDL trước:
tblMembershipTier

| ma | tenHang | diemToiThieu | heSoUuDai |
| --- | --- | --- | --- |
| 1 | Thường | 0 | 0.0 |
| 2 | Bạc | 1000 | 0.1 |
| 3 | Vàng | 5000 | 0.2 |
| 4 | Kim Cương | 20000 | 0.5 |

tblUser

| ma | hoTen | soDienThoai | email | matKhau | diemTichLuy | trangThai | tblMembershipTierMa |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Nguyễn Văn A | 0912345678 | vana@email.com | $2a$10$hashAbc1234... | 1250 | Hoạt động | 2 |
| 2 | Lê Thị B | 0987654321 | b.lt@email.com | $2a$10$hashXyz5678... | 0 | Hoạt động | 1 |
| 3 | Phạm Minh C | 0909123456 | pmc@email.com | $2a$10$hashMno9012... | 5200 | Hoạt động | 3 |

#### Kịch bản thực hiện:

| Bước | Hành động UI | Kết quả mong đợi |
| --- | --- | --- |
| 1 | Mở trình duyệt, truy cập /login | Hiển thị form đăng nhập |
| 2 | Click vào ô "SĐT hoặc Email", nhập 0999999999 | Ô nhập hiển thị 0999999999 |
| 3 | Click vào ô "Mật khẩu", nhập Abc@1234 | Ô nhập hiển thị dấu chấm (masked) |
| 4 | Nhấn nút [Đăng nhập] | Hệ thống truy vấn tblUser WHERE soDienThoai = '0999999999' → không tìm thấy dòng nào |
| 5 | Hiển thị lỗi | Ô SĐT viền đỏ, thông báo lỗi: "Tài khoản không tồn tại. Vui lòng kiểm tra lại." |

Trạng thái CSDL sau: Không thay đổi.
---
### TC03: Mật khẩu sai 5 lần → khóa tài khoản
#### Trạng thái CSDL trước:
tblMembershipTier

| ma | tenHang | diemToiThieu | heSoUuDai |
| --- | --- | --- | --- |
| 1 | Thường | 0 | 0.0 |
| 2 | Bạc | 1000 | 0.1 |
| 3 | Vàng | 5000 | 0.2 |
| 4 | Kim Cương | 20000 | 0.5 |

tblUser

| ma | hoTen | soDienThoai | email | matKhau | diemTichLuy | trangThai | soLanSai | thoiGianKhoa | tblMembershipTierMa |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Nguyễn Văn A | 0912345678 | vana@email.com | $2a$10$hashAbc1234... | 1250 | Hoạt động | 0 | null | 2 |
| 2 | Lê Thị B | 0987654321 | b.lt@email.com | $2a$10$hashXyz5678... | 0 | Hoạt động | 0 | null | 1 |
| 3 | Phạm Minh C | 0909123456 | pmc@email.com | $2a$10$hashMno9012... | 5200 | Hoạt động | 0 | null | 3 |

#### Kịch bản thực hiện:

| Bước | Hành động UI | Kết quả mong đợi |
| --- | --- | --- |
| 1 | Truy cập /login, nhập SĐT 0912345678, MK SaiPass1, nhấn [Đăng nhập] | Mật khẩu không khớp. soLanSai = 1. Hiển thị: "Mật khẩu không chính xác. Còn 4 lần thử." |
| 2 | Nhập lại MK SaiPass2, nhấn [Đăng nhập] | Mật khẩu không khớp. soLanSai = 2. Hiển thị: "Còn 3 lần thử." |
| 3 | Nhập lại MK SaiPass3, nhấn [Đăng nhập] | Mật khẩu không khớp. soLanSai = 3. Hiển thị: "Còn 2 lần thử." |
| 4 | Nhập lại MK SaiPass4, nhấn [Đăng nhập] | Mật khẩu không khớp. soLanSai = 4. Hiển thị: "Còn 1 lần thử." |
| 5 | Nhập lại MK SaiPass5, nhấn [Đăng nhập] | Mật khẩu không khớp. soLanSai = 5. Hệ thống cập nhật trangThai = "Bị khóa", thoiGianKhoa = hiện tại + 15 phút |
| 6 | Hiển thị cảnh báo | Ô SĐT viền đỏ, thông báo: "Tài khoản đã bị khóa do nhập sai quá nhiều lần. Vui lòng thử lại sau 15 phút." |
| 7 | Nhập lại MK đúng Abc@1234, nhấn [Đăng nhập] | Hệ thống kiểm tra trangThai = "Bị khóa", từ chối. Hiển thị: "Tài khoản đang bị khóa." |

#### Trạng thái CSDL sau:
tblUser

| ma | hoTen | soDienThoai | email | matKhau | diemTichLuy | trangThai | soLanSai | thoiGianKhoa | tblMembershipTierMa |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Nguyễn Văn A | 0912345678 | vana@email.com | $2a$10$hashAbc1234... | 1250 | Bị khóa | 5 | 2026-06-01 10:15 | 2 |
| 2 | Lê Thị B | 0987654321 | b.lt@email.com | $2a$10$hashXyz5678... | 0 | Hoạt động | 0 | null | 1 |
| 3 | Phạm Minh C | 0909123456 | pmc@email.com | $2a$10$hashMno9012... | 5200 | Hoạt động | 0 | null | 3 |

---
### TC04: Đăng ký thành công với OTP
#### Trạng thái CSDL trước:
tblMembershipTier

| ma | tenHang | diemToiThieu | heSoUuDai |
| --- | --- | --- | --- |
| 1 | Thường | 0 | 0.0 |
| 2 | Bạc | 1000 | 0.1 |
| 3 | Vàng | 5000 | 0.2 |
| 4 | Kim Cương | 20000 | 0.5 |

tblUser

| ma | hoTen | soDienThoai | email | matKhau | diemTichLuy | trangThai | tblMembershipTierMa |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Nguyễn Văn A | 0912345678 | vana@email.com | $2a$10$hashAbc1234... | 1250 | Hoạt động | 2 |
| 2 | Lê Thị B | 0987654321 | b.lt@email.com | $2a$10$hashXyz5678... | 0 | Hoạt động | 1 |
| 3 | Phạm Minh C | 0909123456 | pmc@email.com | $2a$10$hashMno9012... | 5200 | Hoạt động | 3 |

#### Kịch bản thực hiện:

| Bước | Hành động UI | Kết quả mong đợi |
| --- | --- | --- |
| 1 | Truy cập /login, nhấn link "Chưa có tài khoản? Đăng ký" | Chuyển hướng sang trang /register, hiển thị form với các ô: Họ tên, SĐT, Email, Mật khẩu, Xác nhận mật khẩu |
| 2 | Nhập Họ tên = Lê Thị D, SĐT = 0911111111, Email = d.lt@email.com, MK = Pass@2025, xác nhận MK = Pass@2025 | Tất cả ô hiển thị giá trị, viền xanh hợp lệ |
| 3 | Nhấn nút [Tiếp tục] | Hệ thống kiểm tra: SĐT '0911111111' chưa tồn tại trong tblUser, email 'd.lt@email.com' chưa tồn tại. Hợp lệ → chuyển bước OTP |
| 4 | Hệ thống gửi OTP | Hiển thị form OTP với 6 ô nhập số, thông báo "Mã OTP đã được gửi đến 0911111111". Đồng thời insert 1 dòng vào tblOTP |
| 5 | Nhập OTP = 482917 vào 6 ô | Hệ thống kiểm tra maOTP khớp và chưa hết hạn |
| 6 | Nhấn nút [Xác nhận] | OTP hợp lệ. Hệ thống tạo tài khoản User mới: ma=4, hoTen="Lê Thị D", soDienThoai="0911111111", email="d.lt@email.com", diemTichLuy=0, trangThai="Hoạt động", tblMembershipTierMa=1 (Thường). Cập nhật tblOTP.daXacMinh = true |
| 7 | Tự động đăng nhập, chuyển trang chủ | Header hiện "Xin chào, Lê Thị D!", toast "Đăng ký thành công! Chào mừng bạn." |

#### Trạng thái CSDL sau:
tblUser (thêm 1 dòng mới)

| ma | hoTen | soDienThoai | email | matKhau | diemTichLuy | trangThai | tblMembershipTierMa |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Nguyễn Văn A | 0912345678 | vana@email.com | $2a$10$hashAbc1234... | 1250 | Hoạt động | 2 |
| 2 | Lê Thị B | 0987654321 | b.lt@email.com | $2a$10$hashXyz5678... | 0 | Hoạt động | 1 |
| 3 | Phạm Minh C | 0909123456 | pmc@email.com | $2a$10$hashMno9012... | 5200 | Hoạt động | 3 |
| 4 | Lê Thị D | 0911111111 | d.lt@email.com | $2a$10$hashPqr3456... | 0 | Hoạt động | 1 |

tblOTP (cập nhật dòng hiện có)

| ma | maOTP | loai | thoiHanHetHan | daXacMinh | tblUserMa |
| --- | --- | --- | --- | --- | --- |
| 1 | 482917 | DANG_KY | 2026-06-01 10:05 | true | 4 |

tblLoginSession (thêm 1 dòng mới)

| ma | tokenPhien | thoiGianDangNhap | thoiGianHetHan | thietBi | tblUserMa |
| --- | --- | --- | --- | --- | --- |
| 1 | tk_reg_ccc... | 2026-06-01 10:02 | 2026-06-01 22:02 | Chrome/Mac | 4 |

---
### TC05: SĐT đã tồn tại khi đăng ký
#### Trạng thái CSDL trước:
tblMembershipTier

| ma | tenHang | diemToiThieu | heSoUuDai |
| --- | --- | --- | --- |
| 1 | Thường | 0 | 0.0 |
| 2 | Bạc | 1000 | 0.1 |
| 3 | Vàng | 5000 | 0.2 |
| 4 | Kim Cương | 20000 | 0.5 |

tblUser

| ma | hoTen | soDienThoai | email | matKhau | diemTichLuy | trangThai | tblMembershipTierMa |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Nguyễn Văn A | 0912345678 | vana@email.com | $2a$10$hashAbc1234... | 1250 | Hoạt động | 2 |
| 2 | Lê Thị B | 0987654321 | b.lt@email.com | $2a$10$hashXyz5678... | 0 | Hoạt động | 1 |
| 3 | Phạm Minh C | 0909123456 | pmc@email.com | $2a$10$hashMno9012... | 5200 | Hoạt động | 3 |

#### Kịch bản thực hiện:

| Bước | Hành động UI | Kết quả mong đợi |
| --- | --- | --- |
| 1 | Truy cập /register | Hiển thị form đăng ký với các ô: Họ tên, SĐT, Email, Mật khẩu, Xác nhận mật khẩu |
| 2 | Nhập Họ tên = Trần Văn E, SĐT = 0912345678, Email = e.tv@email.com, MK = Pass@2025, xác nhận MK = Pass@2025 | Tất cả ô hiển thị giá trị |
| 3 | Nhấn nút [Tiếp tục] | Hệ thống kiểm tra: SĐT '0912345678' đã tồn tại trong tblUser (ma=1). Không hợp lệ |
| 4 | Hiển thị lỗi | Ô SĐT viền đỏ, thông báo: "Số điện thoại này đã được sử dụng bởi tài khoản khác." Form không chuyển bước OTP |

Trạng thái CSDL sau: Không thay đổi.
---
### TC06: OTP sai 3 lần → hủy phiên
#### Trạng thái CSDL trước:
tblMembershipTier

| ma | tenHang | diemToiThieu | heSoUuDai |
| --- | --- | --- | --- |
| 1 | Thường | 0 | 0.0 |
| 2 | Bạc | 1000 | 0.1 |
| 3 | Vàng | 5000 | 0.2 |
| 4 | Kim Cương | 20000 | 0.5 |

tblUser

| ma | hoTen | soDienThoai | email | matKhau | diemTichLuy | trangThai | tblMembershipTierMa |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Nguyễn Văn A | 0912345678 | vana@email.com | $2a$10$hashAbc1234... | 1250 | Hoạt động | 2 |
| 2 | Lê Thị B | 0987654321 | b.lt@email.com | $2a$10$hashXyz5678... | 0 | Hoạt động | 1 |
| 3 | Phạm Minh C | 0909123456 | pmc@email.com | $2a$10$hashMno9012... | 5200 | Hoạt động | 3 |

tblOTP

| ma | maOTP | loai | thoiHanHetHan | daXacMinh | tblUserMa |
| --- | --- | --- | --- | --- | --- |
| 1 | 482917 | DANG_KY | 2026-06-01 10:05 | false | null |

(Lưu ý: tblUserMa = null vì tài khoản mới chưa được tạo; OTP được tạo tạm trong phiên đăng ký)
#### Kịch bản thực hiện:

| Bước | Hành động UI | Kết quả mong đợi |
| --- | --- | --- |
| 1 | (Tiếp từ bước 4 TC04) Form OTP hiển thị, nhập 111111 vào 6 ô OTP | Hệ thống kiểm tra: maOTP '111111' ≠ '482917'. Sai. Hiển thị: "Mã OTP không chính xác. Còn 2 lần thử." |
| 2 | Nhập 222222 vào 6 ô OTP | Hệ thống kiểm tra: maOTP '222222' ≠ '482917'. Sai. Hiển thị: "Mã OTP không chính xác. Còn 1 lần thử." |
| 3 | Nhập 333333 vào 6 ô OTP | Hệ thống kiểm tra: maOTP '333333' ≠ '482917'. Sai lần 3 → hủy phiên OTP |
| 4 | Hệ thống đánh dấu OTP đã xác minh (hủy) | Cập nhật tblOTP.daXacMinh = true (đã xử lý). Xóa dữ liệu đăng ký tạm |
| 5 | Hiển thị lỗi | Thông báo: "Mã OTP sai 3 lần. Phiên đăng ký đã bị hủy. Vui lòng đăng ký lại." Chuyển hướng về /register |

#### Trạng thái CSDL sau:
tblOTP

| ma | maOTP | loai | thoiHanHetHan | daXacMinh | tblUserMa |
| --- | --- | --- | --- | --- | --- |
| 1 | 482917 | DANG_KY | 2026-06-01 10:05 | true | null |

tblUser: Không thay đổi. Không có tài khoản mới nào được tạo.
---
### TC07: Đổi mật khẩu thành công
#### Trạng thái CSDL trước:
tblMembershipTier

| ma | tenHang | diemToiThieu | heSoUuDai |
| --- | --- | --- | --- |
| 1 | Thường | 0 | 0.0 |
| 2 | Bạc | 1000 | 0.1 |
| 3 | Vàng | 5000 | 0.2 |
| 4 | Kim Cương | 20000 | 0.5 |

tblUser

| ma | hoTen | soDienThoai | email | matKhau | diemTichLuy | trangThai | tblMembershipTierMa |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Nguyễn Văn A | 0912345678 | vana@email.com | $2a$10$hashAbc1234... | 1250 | Hoạt động | 2 |
| 2 | Lê Thị B | 0987654321 | b.lt@email.com | $2a$10$hashXyz5678... | 0 | Hoạt động | 1 |
| 3 | Phạm Minh C | 0909123456 | pmc@email.com | $2a$10$hashMno9012... | 5200 | Hoạt động | 3 |

tblLoginSession

| ma | tokenPhien | thoiGianDangNhap | thoiGianHetHan | thietBi | tblUserMa |
| --- | --- | --- | --- | --- | --- |
| 1 | tk_sess_001... | 2026-06-01 09:00 | 2026-06-01 21:00 | Chrome/Mac | 1 |
| 2 | tk_sess_002... | 2026-06-01 08:30 | 2026-06-01 20:30 | Safari/iPhone | 1 |

#### Kịch bản thực hiện:

| Bước | Hành động UI | Kết quả mong đợi |
| --- | --- | --- |
| 1 | (Đã đăng nhập user ma=1) Nhấn avatar góc phải → chọn "Cài đặt tài khoản" | Chuyển sang trang /account/settings |
| 2 | Nhấn tab "Bảo mật" | Hiển thị form đổi mật khẩu với 3 ô: Mật khẩu hiện tại, Mật khẩu mới, Xác nhận mật khẩu mới |
| 3 | Nhập Mật khẩu hiện tại = Abc@1234 | Ô nhập masked, viền xanh |
| 4 | Nhập Mật khẩu mới = NewPass@2025 | Ô nhập masked. Thanh đánh giá độ mạnh hiển thị "Mạnh" (xanh lá) |
| 5 | Nhập Xác nhận = NewPass@2025 | Ô nhập masked, khớp với MK mới, viền xanh |
| 6 | Nhấn nút [Lưu thay đổi] | Hệ thống xác minh: bcrypt('Abc@1234', storedHash) → khớp. Kiểm tra MK mới ≠ MK cũ, đạt yêu cầu phức tạp |
| 7 | Hệ thống cập nhật CSDL | Cập nhật tblUser.matKhau = bcrypt('NewPass@2025'). Thu hồi TẤT CẢ LoginSession của user ma=1 (trangThai = "Đã thu hồi") |
| 8 | Hiển thị thông báo | Toast: "Đổi mật khẩu thành công. Vui lòng đăng nhập lại." Chuyển hướng về /login |

#### Trạng thái CSDL sau:
tblUser

| ma | hoTen | soDienThoai | email | matKhau | diemTichLuy | trangThai | tblMembershipTierMa |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Nguyễn Văn A | 0912345678 | vana@email.com | $2a$10$hashNewPwxyz... | 1250 | Hoạt động | 2 |
| 2 | Lê Thị B | 0987654321 | b.lt@email.com | $2a$10$hashXyz5678... | 0 | Hoạt động | 1 |
| 3 | Phạm Minh C | 0909123456 | pmc@email.com | $2a$10$hashMno9012... | 5200 | Hoạt động | 3 |

tblLoginSession

| ma | tokenPhien | thoiGianDangNhap | thoiGianHetHan | thietBi | trangThai | tblUserMa |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | tk_sess_001... | 2026-06-01 09:00 | 2026-06-01 21:00 | Chrome/Mac | Đã thu hồi | 1 |
| 2 | tk_sess_002... | 2026-06-01 08:30 | 2026-06-01 20:30 | Safari/iPhone | Đã thu hồi | 1 |

---
### TC08: Mật khẩu hiện tại sai
#### Trạng thái CSDL trước:
tblMembershipTier

| ma | tenHang | diemToiThieu | heSoUuDai |
| --- | --- | --- | --- |
| 1 | Thường | 0 | 0.0 |
| 2 | Bạc | 1000 | 0.1 |
| 3 | Vàng | 5000 | 0.2 |
| 4 | Kim Cương | 20000 | 0.5 |

tblUser

| ma | hoTen | soDienThoai | email | matKhau | diemTichLuy | trangThai | tblMembershipTierMa |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Nguyễn Văn A | 0912345678 | vana@email.com | $2a$10$hashAbc1234... | 1250 | Hoạt động | 2 |
| 2 | Lê Thị B | 0987654321 | b.lt@email.com | $2a$10$hashXyz5678... | 0 | Hoạt động | 1 |
| 3 | Phạm Minh C | 0909123456 | pmc@email.com | $2a$10$hashMno9012... | 5200 | Hoạt động | 3 |

tblLoginSession

| ma | tokenPhien | thoiGianDangNhap | thoiGianHetHan | thietBi | tblUserMa |
| --- | --- | --- | --- | --- | --- |
| 1 | tk_sess_001... | 2026-06-01 09:00 | 2026-06-01 21:00 | Chrome/Mac | 1 |

#### Kịch bản thực hiện:

| Bước | Hành động UI | Kết quả mong đợi |
| --- | --- | --- |
| 1 | (Đã đăng nhập user ma=1) Nhấn avatar → "Cài đặt tài khoản" → tab "Bảo mật" | Hiển thị form đổi mật khẩu |
| 2 | Nhập Mật khẩu hiện tại = SaiPass@123 | Ô nhập masked |
| 3 | Nhập Mật khẩu mới = NewPass@2025 | Thanh độ mạnh hiển thị "Mạnh" |
| 4 | Nhập Xác nhận = NewPass@2025 | Khớp với MK mới |
| 5 | Nhấn nút [Lưu thay đổi] | Hệ thống xác minh: bcrypt('SaiPass@123', storedHash) → KHÔNG khớp |
| 6 | Hiển thị lỗi | Ô "Mật khẩu hiện tại" viền đỏ, thông báo: "Mật khẩu hiện tại không chính xác." Form giữ nguyên dữ liệu đã nhập |

Trạng thái CSDL sau: Không thay đổi.
---
### TC09: Cập nhật thông tin thành công
#### Trạng thái CSDL trước:
tblMembershipTier

| ma | tenHang | diemToiThieu | heSoUuDai |
| --- | --- | --- | --- |
| 1 | Thường | 0 | 0.0 |
| 2 | Bạc | 1000 | 0.1 |
| 3 | Vàng | 5000 | 0.2 |
| 4 | Kim Cương | 20000 | 0.5 |

tblUser

| ma | hoTen | soDienThoai | email | matKhau | diemTichLuy | trangThai | tblMembershipTierMa |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Nguyễn Văn A | 0912345678 | vana@email.com | $2a$10$hashAbc1234... | 1250 | Hoạt động | 2 |
| 2 | Lê Thị B | 0987654321 | b.lt@email.com | $2a$10$hashXyz5678... | 0 | Hoạt động | 1 |
| 3 | Phạm Minh C | 0909123456 | pmc@email.com | $2a$10$hashMno9012... | 5200 | Hoạt động | 3 |

#### Kịch bản thực hiện:

| Bước | Hành động UI | Kết quả mong đợi |
| --- | --- | --- |
| 1 | (Đã đăng nhập user ma=1) Nhấn avatar góc phải → "Hồ sơ cá nhân" | Chuyển sang trang /account/profile. Hiển thị thông tin: Họ tên = "Nguyễn Văn A", SĐT = "0912345678" (mờ, không sửa được), Email = "vana@email.com" |
| 2 | Nhấn nút [Chỉnh sửa thông tin] | Các ô Họ tên, Email chuyển sang chế độ có thể chỉnh sửa. Ô SĐT vẫn bị khóa (disabled) |
| 3 | Xóa ô Họ tên, nhập Nguyễn Văn An | Ô Họ tên hiển thị "Nguyễn Văn An" |
| 4 | Xóa ô Email, nhập vanan@newemail.com | Ô Email hiển thị "vanan@newemail.com", viền xanh (hợp lệ) |
| 5 | Nhấn nút [Lưu thay đổi] | Hệ thống kiểm tra: email 'vanan@newemail.com' chưa tồn tại trong tblUser. Hợp lệ |
| 6 | Hệ thống cập nhật CSDL | Cập nhật tblUser: hoTen = "Nguyễn Văn An", email = "vanan@newemail.com" WHERE ma = 1 |
| 7 | Hiển thị thông báo | Toast: "Cập nhật thông tin thành công!" Header cập nhật: "Xin chào, Nguyễn Văn An" |

#### Trạng thái CSDL sau:
tblUser

| ma | hoTen | soDienThoai | email | matKhau | diemTichLuy | trangThai | tblMembershipTierMa |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Nguyễn Văn An | 0912345678 | vanan@newemail.com | $2a$10$hashAbc1234... | 1250 | Hoạt động | 2 |
| 2 | Lê Thị B | 0987654321 | b.lt@email.com | $2a$10$hashXyz5678... | 0 | Hoạt động | 1 |
| 3 | Phạm Minh C | 0909123456 | pmc@email.com | $2a$10$hashMno9012... | 5200 | Hoạt động | 3 |

---
### TC10: Email đã được sử dụng khi cập nhật hồ sơ
#### Trạng thái CSDL trước:
tblMembershipTier

| ma | tenHang | diemToiThieu | heSoUuDai |
| --- | --- | --- | --- |
| 1 | Thường | 0 | 0.0 |
| 2 | Bạc | 1000 | 0.1 |
| 3 | Vàng | 5000 | 0.2 |
| 4 | Kim Cương | 20000 | 0.5 |

tblUser

| ma | hoTen | soDienThoai | email | matKhau | diemTichLuy | trangThai | tblMembershipTierMa |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Nguyễn Văn A | 0912345678 | vana@email.com | $2a$10$hashAbc1234... | 1250 | Hoạt động | 2 |
| 2 | Lê Thị B | 0987654321 | b.lt@email.com | $2a$10$hashXyz5678... | 0 | Hoạt động | 1 |
| 3 | Phạm Minh C | 0909123456 | pmc@email.com | $2a$10$hashMno9012... | 5200 | Hoạt động | 3 |

#### Kịch bản thực hiện:

| Bước | Hành động UI | Kết quả mong đợi |
| --- | --- | --- |
| 1 | (Đã đăng nhập user ma=1) Nhấn avatar → "Hồ sơ cá nhân" | Hiển thị thông tin: Họ tên = "Nguyễn Văn A", SĐT = "0912345678", Email = "vana@email.com" |
| 2 | Nhấn nút [Chỉnh sửa thông tin] | Ô Họ tên, Email chuyển sang chế độ chỉnh sửa. Ô SĐT bị khóa |
| 3 | Xóa ô Email, nhập b.lt@email.com | Ô Email hiển thị "b.lt@email.com" |
| 4 | Nhấn nút [Lưu thay đổi] | Hệ thống kiểm tra: email 'b.lt@email.com' đã tồn tại trong tblUser (ma=2). Không hợp lệ |
| 5 | Hiển thị lỗi | Ô Email viền đỏ, thông báo: "Email này đã được đăng ký bởi tài khoản khác." Form giữ nguyên, không cập nhật CSDL |

Trạng thái CSDL sau: Không thay đổi.
---
### TC11: Thêm nhân viên mới
#### Trạng thái CSDL trước:
tblMembershipTier

| ma | tenHang | diemToiThieu | heSoUuDai |
| --- | --- | --- | --- |
| 1 | Thường | 0 | 0.0 |
| 2 | Bạc | 1000 | 0.1 |
| 3 | Vàng | 5000 | 0.2 |
| 4 | Kim Cương | 20000 | 0.5 |

tblUser

| ma | hoTen | soDienThoai | email | matKhau | diemTichLuy | trangThai | tblMembershipTierMa |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Nguyễn Văn A | 0912345678 | vana@email.com | $2a$10$hashAbc1234... | 1250 | Hoạt động | 2 |
| 2 | Lê Thị B | 0987654321 | b.lt@email.com | $2a$10$hashXyz5678... | 0 | Hoạt động | 1 |
| 3 | Phạm Minh C | 0909123456 | pmc@email.com | $2a$10$hashMno9012... | 5200 | Hoạt động | 3 |

tblEmployee

| ma | hoTen | soDienThoai | email | vaiTro | trangThai | tblUserMa |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Trần Thị F | 0977111222 | f.tt@karaoke.com | Lễ tân | Đang làm | 1 |
| 2 | Hoàng Văn G | 0966333444 | g.hv@karaoke.com | Quản lý | Đang làm | 3 |

#### Kịch bản thực hiện:

| Bước | Hành động UI | Kết quả mong đợi |
| --- | --- | --- |
| 1 | (Đăng nhập với quyền Quản lý) Nhấn menu "Quản lý" → "Nhân viên" | Chuyển sang trang /admin/employees. Hiển thị bảng danh sách 2 nhân viên hiện có (Trần Thị F, Hoàng Văn G) với các cột: Mã, Họ tên, Vai trò, Trạng thái, Thao tác |
| 2 | Nhấn nút [Thêm nhân viên] | Hiển thị modal/dialog "Thêm nhân viên mới" với các ô: Họ tên, SĐT, Email, Vai trò (dropdown: Lễ tân, Phục vụ, Quản lý, Kỹ thuật), Trạng thái (dropdown: Đang làm, Tạm nghỉ) |
| 3 | Nhập Họ tên = Lê Văn H | Ô nhập hiển thị "Lê Văn H" |
| 4 | Nhập SĐT = 0955666777 | Ô nhập hiển thị "0955666777", viền xanh (hợp lệ, 10 số) |
| 5 | Nhập Email = h.lv@karaoke.com | Ô nhập hiển thị "h.lv@karaoke.com", viền xanh (hợp lệ) |
| 6 | Chọn Vai trò = Phục vụ từ dropdown | Dropdown hiển thị "Phục vụ" |
| 7 | Chọn Trạng thái = Đang làm từ dropdown | Dropdown hiển thị "Đang làm" |
| 8 | Nhấn nút [Lưu] | Hệ thống kiểm tra: SĐT '0955666777' chưa tồn tại trong tblEmployee. Email 'h.lv@karaoke.com' chưa tồn tại. Hợp lệ |
| 9 | Hệ thống tạo Employee mới | Insert tblEmployee: ma=3, hoTen="Lê Văn H", soDienThoai="0955666777", email="h.lv@karaoke.com", vaiTro="Phục vụ", trangThai="Đang làm". Đồng thời tạo tài khoản User tương ứng (ma=4) |
| 10 | Hiển thị thông báo | Toast: "Thêm nhân viên thành công!" Modal đóng, bảng danh sách cập nhật hiển thị 3 nhân viên |

#### Trạng thái CSDL sau:
tblUser (thêm 1 dòng mới)

| ma | hoTen | soDienThoai | email | matKhau | diemTichLuy | trangThai | tblMembershipTierMa |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Nguyễn Văn A | 0912345678 | vana@email.com | $2a$10$hashAbc1234... | 1250 | Hoạt động | 2 |
| 2 | Lê Thị B | 0987654321 | b.lt@email.com | $2a$10$hashXyz5678... | 0 | Hoạt động | 1 |
| 3 | Phạm Minh C | 0909123456 | pmc@email.com | $2a$10$hashMno9012... | 5200 | Hoạt động | 3 |
| 4 | Lê Văn H | 0955666777 | h.lv@karaoke.com | $2a$10$hashStu7890... | 0 | Hoạt động | 1 |

tblEmployee (thêm 1 dòng mới)

| ma | hoTen | soDienThoai | email | vaiTro | trangThai | tblUserMa |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Trần Thị F | 0977111222 | f.tt@karaoke.com | Lễ tân | Đang làm | 1 |
| 2 | Hoàng Văn G | 0966333444 | g.hv@karaoke.com | Quản lý | Đang làm | 3 |
| 3 | Lê Văn H | 0955666777 | h.lv@karaoke.com | Phục vụ | Đang làm | 4 |

 
