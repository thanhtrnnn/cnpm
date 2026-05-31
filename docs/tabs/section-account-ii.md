## II. PHA PHÂN TÍCH

### 1. Kịch bản chuẩn

#### UC01 – Đăng nhập

| Use case | Đăng nhập |
|----------|----------|
| Actor | Khách hàng, Nhân viên |
| Tiền điều kiện | Người dùng chưa đăng nhập. Tài khoản đã tồn tại trong hệ thống. |
| Hậu điều kiện | Người dùng được xác thực thành công, hệ thống tạo session và chuyển hướng đến trang chủ tương ứng. |
| Kịch bản chính | 1. Người dùng truy cập màn hình "Đăng nhập".<br>2. Hệ thống hiển thị form gồm: Ô nhập SĐT/Email, Ô nhập Mật khẩu, Nút [Đăng nhập], Liên kết "Quên mật khẩu?" / "Đăng ký".<br>3. Người dùng nhập thông tin: SĐT = "0912345678", Mật khẩu = "Abc@1234".<br>4. Người dùng nhấn [Đăng nhập].<br>5. Hệ thống kiểm tra định dạng đầu vào.<br>6. Hệ thống truy vấn CSDL: tìm tài khoản, so sánh mật khẩu đã mã hóa.<br>7. Xác thực thành công, tạo session với vai trò "Khách hàng".<br>8. Chuyển hướng đến trang chủ, hiển thị "Đăng nhập thành công. Xin chào, Nguyễn Văn A!". |
| Ngoại lệ | 6a. Tài khoản không tồn tại: Hiển thị "Tài khoản không tồn tại. Vui lòng kiểm tra lại."<br>6b. Mật khẩu không khớp: Hiển thị "Mật khẩu không chính xác. Còn [N] lần thử." Sau 5 lần sai → khóa 15 phút. |

#### UC02 – Đăng ký

| Use case | Đăng ký |
|----------|--------|
| Actor | Khách hàng |
| Tiền điều kiện | Người dùng chưa có tài khoản. Hệ thống hoạt động bình thường. |
| Hậu điều kiện | Tài khoản mới được tạo, hạng "Thường", đăng nhập tự động. |
| Kịch bản chính | 1. Người dùng nhấn "Đăng ký" từ màn hình đăng nhập.<br>2. Hệ thống hiển thị form: Họ tên, SĐT, Email, Mật khẩu, Xác nhận MK.<br>3. Người dùng điền: Họ tên = "Nguyễn Thị Bình", SĐT = "0987654321", Email = "binh.nt@email.com", MK = "Pass@2025".<br>4. Người dùng nhấn [Tiếp tục].<br>5. Hệ thống kiểm tra định dạng, SĐT và email chưa tồn tại.<br>6. Hệ thống gửi OTP 6 chữ số đến SĐT.<br>7. Hiển thị màn hình "Xác nhận OTP".<br>8. Người dùng nhập OTP = "482917" và nhấn [Xác nhận].<br>9. Hệ thống xác minh OTP đúng và còn hiệu lực (≤ 5 phút).<br>10. Tạo tài khoản mới, hạng "Thường", điểm = 0.<br>11. Đăng nhập tự động, hiển thị "Đăng ký thành công! Chào mừng Nguyễn Thị Bình." |
| Ngoại lệ | 5a. SĐT đã tồn tại: "SĐT này đã được sử dụng."<br>5b. MK không khớp: Highlight ô xác nhận MK, "Mật khẩu không khớp."<br>9a. OTP sai: "Mã OTP không đúng. Vui lòng thử lại." (tối đa 3 lần)<br>9b. OTP hết hạn: "Mã OTP đã hết hạn." Nhấn "Gửi lại OTP". |

#### UC03 – Đổi mật khẩu

| Use case | Đổi mật khẩu |
|----------|-------------|
| Actor | Khách hàng, Nhân viên (đã đăng nhập) |
| Tiền điều kiện | Người dùng đã đăng nhập thành công. |
| Hậu điều kiện | Mật khẩu mới được lưu (bcrypt). Tất cả session khác bị thu hồi. |
| Kịch bản chính | 1. Người dùng truy cập "Bảo mật" trong cài đặt.<br>2. Hiển thị form: MK hiện tại, MK mới, Xác nhận MK mới.<br>3. Người dùng nhập: MK hiện tại = "Abc@1234", MK mới = "NewPass@2025", xác nhận = "NewPass@2025".<br>4. Nhấn [Lưu thay đổi].<br>5. Hệ thống xác minh MK hiện tại khớp CSDL.<br>6. Kiểm tra MK mới: độ dài ≥ 8, có chữ hoa/thường/số/đặc biệt.<br>7. Kiểm tra MK mới ≠ MK hiện tại.<br>8. Mã hóa (bcrypt) và cập nhật.<br>9. Thu hồi tất cả session, hiển thị "Đổi mật khẩu thành công. Vui lòng đăng nhập lại."<br>10. Chuyển hướng về màn hình Đăng nhập. |
| Ngoại lệ | 5a. MK hiện tại sai: "Mật khẩu hiện tại không chính xác."<br>6a. MK mới không đủ mạnh: Highlight ô, hiển thị yêu cầu còn thiếu.<br>7a. MK mới trùng MK cũ: "Mật khẩu mới không được trùng mật khẩu hiện tại." |

#### UC04 – Quản lý thông tin cá nhân

| Use case | Quản lý thông tin cá nhân |
|----------|--------------------------|
| Actor | Khách hàng (đã đăng nhập) |
| Tiền điều kiện | Khách hàng đã đăng nhập. Tài khoản tồn tại trong CSDL. |
| Hậu điều kiện | Thông tin cập nhật trong CSDL, hiển thị ngay trên giao diện. |
| Kịch bản chính | 1. Khách hàng nhấn vào ảnh đại diện / tên tài khoản.<br>2. Hiển thị "Hồ sơ cá nhân": Họ tên, SĐT, Email, Hạng hội viên, Điểm tích lũy, Ngày tham gia.<br>3. Nhấn [Chỉnh sửa thông tin].<br>4. Chuyển sang chế độ chỉnh sửa: Họ tên, Email có thể nhập; SĐT bị khóa.<br>5. Cập nhật: Họ tên = "Nguyễn Văn An", Email = "vanan@newemail.com".<br>6. Nhấn [Lưu thay đổi].<br>7. Kiểm tra email hợp lệ và chưa được dùng.<br>8. Cập nhật vào CSDL.<br>9. Hiển thị "Cập nhật thành công!" và quay về chế độ xem. |
| Ngoại lệ | 7a. Email đã được dùng: "Email này đã được đăng ký bởi tài khoản khác."<br>3a. Thay đổi SĐT: Yêu cầu xác minh OTP gửi đến SĐT hiện tại → SĐT mới → OTP mới. |

#### UC20 – Quản lý tài khoản nhân viên

| Use case | Quản lý tài khoản nhân viên |
|----------|----------------------------|
| Actor | Chủ Doanh nghiệp (Admin) |
| Tiền điều kiện | Admin đã đăng nhập. Có quyền quản lý tài khoản nhân viên toàn hệ thống. |
| Hậu điều kiện | Tài khoản nhân viên được tạo/sửa/xóa trong CSDL. |
| Kịch bản chính | 1. Quản lý truy cập "Quản lý nhân viên".<br>2. Hiển thị danh sách nhân viên: họ tên, vai trò, trạng thái.<br>3a. Thêm nhân viên: Nhấn [Thêm] → Nhập thông tin → Lưu.<br>3b. Sửa nhân viên: Chọn nhân viên → Chỉnh sửa → Lưu.<br>3c. Xóa nhân viên: Chọn nhân viên → Xác nhận xóa → Hệ thống chuyển trạng thái "Đã nghỉ". |
| Ngoại lệ | 3a. SĐT đã tồn tại: "SĐT này đã được sử dụng."<br>3c. Nhân viên đang xử lý order: Không thể xóa, hiển thị cảnh báo. |
