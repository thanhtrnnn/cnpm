## IV. PHA CÀI ĐẶT VÀ KIỂM THỬ

### 1. Lập kế hoạch test

| TT | Module | Test case |
|----|--------|-----------|
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

### 2. Test case chi tiết

#### TC01: Đăng nhập thành công

**Trạng thái CSDL trước:**

tblHangHoiVien
| ma | tenHang | diemToiThieu | heSoUuDai |
|----|---------|-------------|-----------|
| 1 | Thường | 0 | 0.0 |
| 2 | Bạc | 1000 | 0.1 |

tblNguoiDung
| ma | hoTen | soDienThoai | email | matKhau | diemTichLuy | tblHangHoiVienMa |
|----|-------|-------------|-------|---------|-------------|-------------------|
| 1 | Nguyễn Văn A | 0912345678 | vana@email.com | $2a$10$hash... | 1250 | 2 |

**Kịch bản thực hiện:**

| Kịch bản | Kết quả mong đợi |
|----------|------------------|
| 1. Mở màn hình Đăng nhập | Hiển thị form SĐT/email + Mật khẩu |
| 2. Nhập: 0912345678 / Abc@1234 | Form hiển thị đầy đủ |
| 3. Nhấn [Đăng nhập] | Kiểm tra CSDL, tìm thấy tài khoản |
| 4. Xác thực mật khẩu | Mật khẩu khớp, tạo session |
| 5. Chuyển hướng trang chủ | Hiển thị "Đăng nhập thành công. Xin chào, Nguyễn Văn A!" |

**Trạng thái CSDL sau:**

tblPhienDangNhap (mới tạo)
| ma | tokenPhien | thoiGianDangNhap | thietBi | tblNguoiDungMa |
|----|-----------|-----------------|---------|----------------|
| 1 | abc123... | 2026-06-01 10:00 | Chrome/Mac | 1 |

---

#### TC09: Cập nhật thông tin thành công

**Trạng thái CSDL trước:**

tblNguoiDung
| ma | hoTen | email |
|----|-------|-------|
| 1 | Nguyễn Văn A | vana@email.com |

**Kịch bản thực hiện:**

| Kịch bản | Kết quả mong đợi |
|----------|------------------|
| 1. Nhấn vào hồ sơ cá nhân | Hiển thị thông tin hiện tại |
| 2. Nhấn [Chỉnh sửa thông tin] | Chế độ chỉnh sửa, SĐT bị khóa |
| 3. Sửa: Họ tên = "Nguyễn Văn An" | Ô Họ tên cập nhật |
| 4. Sửa: Email = "vanan@newemail.com" | Ô Email cập nhật |
| 5. Nhấn [Lưu thay đổi] | Kiểm tra email hợp lệ |
| 6. Cập nhật CSDL | Hiển thị "Cập nhật thành công!" |

**Trạng thái CSDL sau:**

tblNguoiDung
| ma | hoTen | email |
|----|-------|-------|
| 1 | **Nguyễn Văn An** | **vanan@newemail.com** |

---

#### TC11: Thêm nhân viên mới

**Trạng thái CSDL trước:**

tblNhanVien
| ma | hoTen | vaiTro | trangThai |
|----|-------|--------|-----------|
| 1 | Trần Thị B | Lễ tân | Đang làm |

**Kịch bản thực hiện:**

| Kịch bản | Kết quả mong đợi |
|----------|------------------|
| 1. Quản lý mở "Quản lý nhân viên" | Hiển thị danh sách nhân viên |
| 2. Nhấn [Thêm nhân viên] | Hiển thị form thêm mới |
| 3. Nhập: Họ tên = "Lê Văn C", Vai trò = "Phục vụ" | Form đầy đủ |
| 4. Nhấn [Lưu] | Kiểm tra SĐT chưa tồn tại |
| 5. Tạo tài khoản mới | Hiển thị "Thêm nhân viên thành công!" |

**Trạng thái CSDL sau:**

tblNhanVien
| ma | hoTen | vaiTro | trangThai |
|----|-------|--------|-----------|
| 1 | Trần Thị B | Lễ tân | Đang làm |
| 2 | **Lê Văn C** | **Phục vụ** | **Đang làm** |

---

#### TC02: Tài khoản không tồn tại

**Trạng thái CSDL trước:**

tblNguoiDung
| ma | hoTen | soDienThoai |
|----|-------|-------------|
| 1 | Nguyễn Văn A | 0912345678 |

**Kịch bản thực hiện:**

| Kịch bản | Kết quả mong đợi |
|----------|------------------|
| 1. Mở màn hình Đăng nhập | Hiển thị form |
| 2. Nhập: 0999999999 / Abc@1234 | SĐT không tồn tại trong CSDL |
| 3. Nhấn [Đăng nhập] | Kiểm tra CSDL, không tìm thấy |
| 4. Hiển thị lỗi | "Tài khoản không tồn tại. Vui lòng kiểm tra lại." |

**Trạng thái CSDL sau:** Không thay đổi.

---

#### TC04: Đăng ký thành công với OTP

**Trạng thái CSDL trước:**

tblNguoiDung
| ma | hoTen | soDienThoai |
|----|-------|-------------|
| 1 | Nguyễn Văn A | 0912345678 |

**Kịch bản thực hiện:**

| Kịch bản | Kết quả mong đợi |
|----------|------------------|
| 1. Nhấn "Đăng ký" từ màn hình đăng nhập | Hiển thị form đăng ký |
| 2. Nhập: Họ tên = "Lê Thị D", SĐT = "0911111111", Email = "d.lt@email.com", MK = "Pass@2025" | Form đầy đủ |
| 3. Nhấn [Tiếp tục] | Kiểm tra SĐT, email chưa tồn tại |
| 4. Hệ thống gửi OTP đến 0911111111 | Hiển thị form OTP |
| 5. Nhập OTP = "123456" | OTP hợp lệ |
| 6. Nhấn [Xác nhận] | Tạo tài khoản, hạng "Thương", điểm = 0 |
| 7. Đăng nhập tự động | "Đăng ký thành công! Chào mừng Lê Thị D." |

**Trạng thái CSDL sau:**

tblNguoiDung
| ma | hoTen | soDienThoai | diemTichLuy | tblHangHoiVienMa |
|----|-------|-------------|-------------|-------------------|
| 1 | Nguyễn Văn A | 0912345678 | 1250 | 2 |
| 2 | **Lê Thị D** | **0911111111** | **0** | **1** |

---

#### TC07: Đổi mật khẩu thành công

**Trạng thái CSDL trước:**

tblNguoiDung
| ma | hoTen | matKhau |
|----|-------|---------|
| 1 | Nguyễn Văn A | $2a$10$hashAbc@1234 |

**Kịch bản thực hiện:**

| Kịch bản | Kết quả mong đợi |
|----------|------------------|
| 1. Truy cập "Bảo mật" | Hiển thị form đổi MK |
| 2. Nhập: MK hiện tại = "Abc@1234", MK mới = "NewPass@2025", xác nhận = "NewPass@2025" | Form đầy đủ |
| 3. Nhấn [Lưu thay đổi] | Xác minh MK hiện tại khớp |
| 4. Kiểm tra MK mới đủ mạnh | Đạt yêu cầu |
| 5. Cập nhật CSDL (bcrypt) | Thu hồi tất cả session |
| 6. Hiển thị thông báo | "Đổi mật khẩu thành công. Vui lòng đăng nhập lại." |

**Trạng thái CSDL sau:**

tblNguoiDung
| ma | hoTen | matKhau |
|----|-------|---------|
| 1 | Nguyễn Văn A | **$2a$10$hashNewPass@2025** |

tblPhienDangNhap
| ma | trangThai |
|----|-----------|
| 1 | **Đã thu hồi** |

---

#### TC08: Mật khẩu hiện tại sai

**Trạng thái CSDL trước:**

tblNguoiDung
| ma | hoTen | matKhau |
|----|-------|---------|
| 1 | Nguyễn Văn A | $2a$10$hashAbc@1234 |

**Kịch bản thực hiện:**

| Kịch bản | Kết quả mong đợi |
|----------|------------------|
| 1. Truy cập "Bảo mật" | Hiển thị form đổi MK |
| 2. Nhập: MK hiện tại = "SaiPass@123", MK mới = "NewPass@2025" | Form đầy đủ |
| 3. Nhấn [Lưu thay đổi] | Xác minh MK hiện tại SAI |
| 4. Hiển thị lỗi | "Mật khẩu hiện tại không chính xác." |

**Trạng thái CSDL sau:** Không thay đổi.

---

#### TC03: Mật khẩu sai 5 lần → khóa tài khoản

**Trạng thái CSDL trước:**

tblNguoiDung
| ma | hoTen | soDienThoai | matKhau | soLanSai | thoiGianKhoa |
|----|-------|-------------|---------|----------|--------------|
| 1 | Nguyễn Văn A | 0912345678 | $2a$10$hashAbc@1234 | 0 | null |

**Kịch bản thực hiện:**

| Kịch bản | Kết quả mong đợi |
|----------|------------------|
| 1. Mở màn hình Đăng nhập | Hiển thị form |
| 2. Nhập: 0912345678 / SaiPass1 | Mật khẩu sai, soLanSai = 1 |
| 3. Nhập: 0912345678 / SaiPass2 | Mật khẩu sai, soLanSai = 2 |
| 4. Nhập: 0912345678 / SaiPass3 | Mật khẩu sai, soLanSai = 3 |
| 5. Nhập: 0912345678 / SaiPass4 | Mật khẩu sai, soLanSai = 4 |
| 6. Nhập: 0912345678 / SaiPass5 | Mật khẩu sai, soLanSai = 5 → khóa 15 phút |
| 7. Nhập: 0912345678 / Abc@1234 | "Tài khoản đã bị khóa. Vui lòng thử lại sau 15 phút." |

**Trạng thái CSDL sau:**

tblNguoiDung
| ma | hoTen | soDienThoai | soLanSai | thoiGianKhoa |
|----|-------|-------------|----------|--------------|
| 1 | Nguyễn Văn A | 0912345678 | **5** | **2026-06-01 10:15** |

---

#### TC05: SĐT đã tồn tại khi đăng ký

**Trạng thái CSDL trước:**

tblNguoiDung
| ma | hoTen | soDienThoai | email |
|----|-------|-------------|-------|
| 1 | Nguyễn Văn A | 0912345678 | vana@email.com |

**Kịch bản thực hiện:**

| Kịch bản | Kết quả mong đợi |
|----------|------------------|
| 1. Nhấn "Đăng ký" | Hiển thị form đăng ký |
| 2. Nhập: Họ tên = "Test", SĐT = "0912345678", Email = "test@email.com", MK = "Pass@2025" | Form đầy đủ |
| 3. Nhấn [Tiếp tục] | Kiểm tra SĐT → đã tồn tại |
| 4. Hiển thị lỗi | "SĐT này đã được sử dụng." |

**Trạng thái CSDL sau:** Không thay đổi.

---

#### TC06: OTP sai 3 lần → hủy phiên

**Trạng thái CSDL trước:**

tblNguoiDung
| ma | hoTen | soDienThoai |
|----|-------|-------------|
| 1 | Nguyễn Văn A | 0912345678 |

tblOTP
| ma | maOTP | loai | thoiHanHetHan | daXacMinh | tblNguoiDungMa |
|----|-------|------|---------------|-----------|----------------|
| 1 | 482917 | DANG_KY | 2026-06-01 10:05 | false | 1 |

**Kịch bản thực hiện:**

| Kịch bản | Kết quả mong đợi |
|----------|------------------|
| 1. Nhập OTP = "111111" | Sai OTP, soLanSai = 1 |
| 2. Nhập OTP = "222222" | Sai OTP, soLanSai = 2 |
| 3. Nhập OTP = "333333" | Sai OTP, soLanSai = 3 → hủy phiên |
| 4. Hiển thị lỗi | "Mã OTP sai 3 lần. Vui lòng đăng ký lại." |

**Trạng thái CSDL sau:**

tblOTP
| ma | maOTP | loai | daXacMinh | tblNguoiDungMa |
|----|-------|------|-----------|----------------|
| 1 | 482917 | DANG_KY | **true** | 1 |

tblNguoiDung: Tài khoản chưa tạo (đăng ký bị hủy).

---

#### TC10: Email đã được sử dụng khi cập nhật hồ sơ

**Trạng thái CSDL trước:**

tblNguoiDung
| ma | hoTen | soDienThoai | email |
|----|-------|-------------|-------|
| 1 | Nguyễn Văn A | 0912345678 | vana@email.com |
| 2 | Lê Thị B | 0987654321 | b.lt@email.com |

**Kịch bản thực hiện:**

| Kịch bản | Kết quả mong đợi |
|----------|------------------|
| 1. Nhấn vào hồ sơ cá nhân (user 1) | Hiển thị thông tin hiện tại |
| 2. Nhấn [Chỉnh sửa] | Chế độ chỉnh sửa |
| 3. Sửa Email = "b.lt@email.com" | Email trùng với user 2 |
| 4. Nhấn [Lưu thay đổi] | Kiểm tra email → đã tồn tại |
| 5. Hiển thị lỗi | "Email này đã được đăng ký bởi tài khoản khác." |

**Trạng thái CSDL sau:** Không thay đổi.
