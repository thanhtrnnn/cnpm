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

---

#### TC01: Đăng nhập thành công

**Trạng thái CSDL trước:**

tblMembershipTier
| ma | tenHang | diemToiThieu | heSoUuDai |
|----|---------|-------------|-----------|
| 1 | Thường | 0 | 0.0 |
| 2 | Bạc | 1000 | 0.1 |
| 3 | Vàng | 5000 | 0.2 |
| 4 | Kim Cương | 20000 | 0.5 |

tblUser
| ma | hoTen | soDienThoai | email | matKhau | diemTichLuy | trangThai | tblMembershipTierMa |
|----|-------|-------------|-------|---------|-------------|-----------|---------------------|
| 1 | Nguyễn Văn A | 0912345678 | vana@email.com | $2a$10$hashAbc1234... | 1250 | Hoạt động | 2 |
| 2 | Lê Thị B | 0987654321 | b.lt@email.com | $2a$10$hashXyz5678... | 0 | Hoạt động | 1 |
| 3 | Phạm Minh C | 0909123456 | pmc@email.com | $2a$10$hashMno9012... | 5200 | Hoạt động | 3 |

tblLoginSession
| ma | tokenPhien | thoiGianDangNhap | thoiGianHetHan | thietBi | tblUserMa |
|----|-----------|-----------------|----------------|---------|-----------|
| 1 | tk_old_aaa... | 2026-05-31 08:00 | 2026-05-31 20:00 | Chrome/Win | 1 |

**Kịch bản thực hiện:**

| Bước | Hành động UI | Kết quả mong đợi |
|------|-------------|------------------|
| 1 | Mở trình duyệt, truy cập `/login` | Hiển thị form đăng nhập với 2 ô: "SĐT hoặc Email" và "Mật khẩu", nút [Đăng nhập], link "Chưa có tài khoản? Đăng ký" |
| 2 | Click vào ô "SĐT hoặc Email", nhập `0912345678` | Ô nhập hiển thị `0912345678`, viền xanh hợp lệ |
| 3 | Click vào ô "Mật khẩu", nhập `Abc@1234` | Ô nhập hiển thị dấu chấm (masked), nút [Đăng nhập] chuyển sang trạng thái active |
| 4 | Nhấn nút [Đăng nhập] | Hệ thống truy vấn tblUser WHERE soDienThoai = '0912345678', tìm thấy ma=1. So sánh bcrypt(password, storedHash) → khớp |
| 5 | Hệ thống tạo LoginSession mới | Tạo token JWT, insert vào tblLoginSession. Chuyển hướng sang trang chủ |
| 6 | Trang chủ hiển thị | Header hiện avatar + "Xin chào, Nguyễn Văn A!", thông báo toast "Đăng nhập thành công" |

**Trạng thái CSDL sau:**

tblUser: Không thay đổi.

tblLoginSession (thêm 1 dòng mới)
| ma | tokenPhien | thoiGianDangNhap | thoiGianHetHan | thietBi | tblUserMa |
|----|-----------|-----------------|----------------|---------|-----------|
| 1 | tk_old_aaa... | 2026-05-31 08:00 | 2026-05-31 20:00 | Chrome/Win | 1 |
| **2** | **tk_new_bbb...** | **2026-06-01 10:00** | **2026-06-01 22:00** | **Chrome/Mac** | **1** |

---

#### TC02: Tài khoản không tồn tại

**Trạng thái CSDL trước:**

tblMembershipTier
| ma | tenHang | diemToiThieu | heSoUuDai |
|----|---------|-------------|-----------|
| 1 | Thường | 0 | 0.0 |
| 2 | Bạc | 1000 | 0.1 |
| 3 | Vàng | 5000 | 0.2 |
| 4 | Kim Cương | 20000 | 0.5 |

tblUser
| ma | hoTen | soDienThoai | email | matKhau | diemTichLuy | trangThai | tblMembershipTierMa |
|----|-------|-------------|-------|---------|-------------|-----------|---------------------|
| 1 | Nguyễn Văn A | 0912345678 | vana@email.com | $2a$10$hashAbc1234... | 1250 | Hoạt động | 2 |
| 2 | Lê Thị B | 0987654321 | b.lt@email.com | $2a$10$hashXyz5678... | 0 | Hoạt động | 1 |
| 3 | Phạm Minh C | 0909123456 | pmc@email.com | $2a$10$hashMno9012... | 5200 | Hoạt động | 3 |

**Kịch bản thực hiện:**

| Bước | Hành động UI | Kết quả mong đợi |
|------|-------------|------------------|
| 1 | Mở trình duyệt, truy cập `/login` | Hiển thị form đăng nhập |
| 2 | Click vào ô "SĐT hoặc Email", nhập `0999999999` | Ô nhập hiển thị `0999999999` |
| 3 | Click vào ô "Mật khẩu", nhập `Abc@1234` | Ô nhập hiển thị dấu chấm (masked) |
| 4 | Nhấn nút [Đăng nhập] | Hệ thống truy vấn tblUser WHERE soDienThoai = '0999999999' → không tìm thấy dòng nào |
| 5 | Hiển thị lỗi | Ô SĐT viền đỏ, thông báo lỗi: "Tài khoản không tồn tại. Vui lòng kiểm tra lại." |

**Trạng thái CSDL sau:** Không thay đổi.

---

#### TC03: Mật khẩu sai 5 lần → khóa tài khoản

**Trạng thái CSDL trước:**

tblMembershipTier
| ma | tenHang | diemToiThieu | heSoUuDai |
|----|---------|-------------|-----------|
| 1 | Thường | 0 | 0.0 |
| 2 | Bạc | 1000 | 0.1 |
| 3 | Vàng | 5000 | 0.2 |
| 4 | Kim Cương | 20000 | 0.5 |

tblUser
| ma | hoTen | soDienThoai | email | matKhau | diemTichLuy | trangThai | soLanSai | thoiGianKhoa | tblMembershipTierMa |
|----|-------|-------------|-------|---------|-------------|-----------|----------|--------------|---------------------|
| 1 | Nguyễn Văn A | 0912345678 | vana@email.com | $2a$10$hashAbc1234... | 1250 | Hoạt động | 0 | null | 2 |
| 2 | Lê Thị B | 0987654321 | b.lt@email.com | $2a$10$hashXyz5678... | 0 | Hoạt động | 0 | null | 1 |
| 3 | Phạm Minh C | 0909123456 | pmc@email.com | $2a$10$hashMno9012... | 5200 | Hoạt động | 0 | null | 3 |

**Kịch bản thực hiện:**

| Bước | Hành động UI | Kết quả mong đợi |
|------|-------------|------------------|
| 1 | Truy cập `/login`, nhập SĐT `0912345678`, MK `SaiPass1`, nhấn [Đăng nhập] | Mật khẩu không khớp. soLanSai = 1. Hiển thị: "Mật khẩu không chính xác. Còn 4 lần thử." |
| 2 | Nhập lại MK `SaiPass2`, nhấn [Đăng nhập] | Mật khẩu không khớp. soLanSai = 2. Hiển thị: "Còn 3 lần thử." |
| 3 | Nhập lại MK `SaiPass3`, nhấn [Đăng nhập] | Mật khẩu không khớp. soLanSai = 3. Hiển thị: "Còn 2 lần thử." |
| 4 | Nhập lại MK `SaiPass4`, nhấn [Đăng nhập] | Mật khẩu không khớp. soLanSai = 4. Hiển thị: "Còn 1 lần thử." |
| 5 | Nhập lại MK `SaiPass5`, nhấn [Đăng nhập] | Mật khẩu không khớp. soLanSai = 5. Hệ thống cập nhật trangThai = "Bị khóa", thoiGianKhoa = hiện tại + 15 phút |
| 6 | Hiển thị cảnh báo | Ô SĐT viền đỏ, thông báo: "Tài khoản đã bị khóa do nhập sai quá nhiều lần. Vui lòng thử lại sau 15 phút." |
| 7 | Nhập lại MK đúng `Abc@1234`, nhấn [Đăng nhập] | Hệ thống kiểm tra trangThai = "Bị khóa", từ chối. Hiển thị: "Tài khoản đang bị khóa." |

**Trạng thái CSDL sau:**

tblUser
| ma | hoTen | soDienThoai | email | matKhau | diemTichLuy | trangThai | soLanSai | thoiGianKhoa | tblMembershipTierMa |
|----|-------|-------------|-------|---------|-------------|-----------|----------|--------------|---------------------|
| 1 | Nguyễn Văn A | 0912345678 | vana@email.com | $2a$10$hashAbc1234... | 1250 | **Bị khóa** | **5** | **2026-06-01 10:15** | 2 |
| 2 | Lê Thị B | 0987654321 | b.lt@email.com | $2a$10$hashXyz5678... | 0 | Hoạt động | 0 | null | 1 |
| 3 | Phạm Minh C | 0909123456 | pmc@email.com | $2a$10$hashMno9012... | 5200 | Hoạt động | 0 | null | 3 |

---

#### TC04: Đăng ký thành công với OTP

**Trạng thái CSDL trước:**

tblMembershipTier
| ma | tenHang | diemToiThieu | heSoUuDai |
|----|---------|-------------|-----------|
| 1 | Thường | 0 | 0.0 |
| 2 | Bạc | 1000 | 0.1 |
| 3 | Vàng | 5000 | 0.2 |
| 4 | Kim Cương | 20000 | 0.5 |

tblUser
| ma | hoTen | soDienThoai | email | matKhau | diemTichLuy | trangThai | tblMembershipTierMa |
|----|-------|-------------|-------|---------|-------------|-----------|---------------------|
| 1 | Nguyễn Văn A | 0912345678 | vana@email.com | $2a$10$hashAbc1234... | 1250 | Hoạt động | 2 |
| 2 | Lê Thị B | 0987654321 | b.lt@email.com | $2a$10$hashXyz5678... | 0 | Hoạt động | 1 |
| 3 | Phạm Minh C | 0909123456 | pmc@email.com | $2a$10$hashMno9012... | 5200 | Hoạt động | 3 |

**Kịch bản thực hiện:**

| Bước | Hành động UI | Kết quả mong đợi |
|------|-------------|------------------|
| 1 | Truy cập `/login`, nhấn link "Chưa có tài khoản? Đăng ký" | Chuyển hướng sang trang `/register`, hiển thị form với các ô: Họ tên, SĐT, Email, Mật khẩu, Xác nhận mật khẩu |
| 2 | Nhập Họ tên = `Lê Thị D`, SĐT = `0911111111`, Email = `d.lt@email.com`, MK = `Pass@2025`, xác nhận MK = `Pass@2025` | Tất cả ô hiển thị giá trị, viền xanh hợp lệ |
| 3 | Nhấn nút [Tiếp tục] | Hệ thống kiểm tra: SĐT '0911111111' chưa tồn tại trong tblUser, email 'd.lt@email.com' chưa tồn tại. Hợp lệ → chuyển bước OTP |
| 4 | Hệ thống gửi OTP | Hiển thị form OTP với 6 ô nhập số, thông báo "Mã OTP đã được gửi đến 0911111111". Đồng thời insert 1 dòng vào tblOTP |
| 5 | Nhập OTP = `482917` vào 6 ô | Hệ thống kiểm tra maOTP khớp và chưa hết hạn |
| 6 | Nhấn nút [Xác nhận] | OTP hợp lệ. Hệ thống tạo tài khoản User mới: ma=4, hoTen="Lê Thị D", soDienThoai="0911111111", email="d.lt@email.com", diemTichLuy=0, trangThai="Hoạt động", tblMembershipTierMa=1 (Thường). Cập nhật tblOTP.daXacMinh = true |
| 7 | Tự động đăng nhập, chuyển trang chủ | Header hiện "Xin chào, Lê Thị D!", toast "Đăng ký thành công! Chào mừng bạn." |

**Trạng thái CSDL sau:**

tblUser (thêm 1 dòng mới)
| ma | hoTen | soDienThoai | email | matKhau | diemTichLuy | trangThai | tblMembershipTierMa |
|----|-------|-------------|-------|---------|-------------|-----------|---------------------|
| 1 | Nguyễn Văn A | 0912345678 | vana@email.com | $2a$10$hashAbc1234... | 1250 | Hoạt động | 2 |
| 2 | Lê Thị B | 0987654321 | b.lt@email.com | $2a$10$hashXyz5678... | 0 | Hoạt động | 1 |
| 3 | Phạm Minh C | 0909123456 | pmc@email.com | $2a$10$hashMno9012... | 5200 | Hoạt động | 3 |
| **4** | **Lê Thị D** | **0911111111** | **d.lt@email.com** | **$2a$10$hashPqr3456...** | **0** | **Hoạt động** | **1** |

tblOTP (cập nhật dòng hiện có)
| ma | maOTP | loai | thoiHanHetHan | daXacMinh | tblUserMa |
|----|-------|------|---------------|-----------|-----------|
| 1 | 482917 | DANG_KY | 2026-06-01 10:05 | **true** | 4 |

tblLoginSession (thêm 1 dòng mới)
| ma | tokenPhien | thoiGianDangNhap | thoiGianHetHan | thietBi | tblUserMa |
|----|-----------|-----------------|----------------|---------|-----------|
| **1** | **tk_reg_ccc...** | **2026-06-01 10:02** | **2026-06-01 22:02** | **Chrome/Mac** | **4** |

---

#### TC05: SĐT đã tồn tại khi đăng ký

**Trạng thái CSDL trước:**

tblMembershipTier
| ma | tenHang | diemToiThieu | heSoUuDai |
|----|---------|-------------|-----------|
| 1 | Thường | 0 | 0.0 |
| 2 | Bạc | 1000 | 0.1 |
| 3 | Vàng | 5000 | 0.2 |
| 4 | Kim Cương | 20000 | 0.5 |

tblUser
| ma | hoTen | soDienThoai | email | matKhau | diemTichLuy | trangThai | tblMembershipTierMa |
|----|-------|-------------|-------|---------|-------------|-----------|---------------------|
| 1 | Nguyễn Văn A | 0912345678 | vana@email.com | $2a$10$hashAbc1234... | 1250 | Hoạt động | 2 |
| 2 | Lê Thị B | 0987654321 | b.lt@email.com | $2a$10$hashXyz5678... | 0 | Hoạt động | 1 |
| 3 | Phạm Minh C | 0909123456 | pmc@email.com | $2a$10$hashMno9012... | 5200 | Hoạt động | 3 |

**Kịch bản thực hiện:**

| Bước | Hành động UI | Kết quả mong đợi |
|------|-------------|------------------|
| 1 | Truy cập `/register` | Hiển thị form đăng ký với các ô: Họ tên, SĐT, Email, Mật khẩu, Xác nhận mật khẩu |
| 2 | Nhập Họ tên = `Trần Văn E`, SĐT = `0912345678`, Email = `e.tv@email.com`, MK = `Pass@2025`, xác nhận MK = `Pass@2025` | Tất cả ô hiển thị giá trị |
| 3 | Nhấn nút [Tiếp tục] | Hệ thống kiểm tra: SĐT '0912345678' đã tồn tại trong tblUser (ma=1). Không hợp lệ |
| 4 | Hiển thị lỗi | Ô SĐT viền đỏ, thông báo: "Số điện thoại này đã được sử dụng bởi tài khoản khác." Form không chuyển bước OTP |

**Trạng thái CSDL sau:** Không thay đổi.

---

#### TC06: OTP sai 3 lần → hủy phiên

**Trạng thái CSDL trước:**

tblMembershipTier
| ma | tenHang | diemToiThieu | heSoUuDai |
|----|---------|-------------|-----------|
| 1 | Thường | 0 | 0.0 |
| 2 | Bạc | 1000 | 0.1 |
| 3 | Vàng | 5000 | 0.2 |
| 4 | Kim Cương | 20000 | 0.5 |

tblUser
| ma | hoTen | soDienThoai | email | matKhau | diemTichLuy | trangThai | tblMembershipTierMa |
|----|-------|-------------|-------|---------|-------------|-----------|---------------------|
| 1 | Nguyễn Văn A | 0912345678 | vana@email.com | $2a$10$hashAbc1234... | 1250 | Hoạt động | 2 |
| 2 | Lê Thị B | 0987654321 | b.lt@email.com | $2a$10$hashXyz5678... | 0 | Hoạt động | 1 |
| 3 | Phạm Minh C | 0909123456 | pmc@email.com | $2a$10$hashMno9012... | 5200 | Hoạt động | 3 |

tblOTP
| ma | maOTP | loai | thoiHanHetHan | daXacMinh | tblUserMa |
|----|-------|------|---------------|-----------|-----------|
| 1 | 482917 | DANG_KY | 2026-06-01 10:05 | false | null |

(Lưu ý: tblUserMa = null vì tài khoản mới chưa được tạo; OTP được tạo tạm trong phiên đăng ký)

**Kịch bản thực hiện:**

| Bước | Hành động UI | Kết quả mong đợi |
|------|-------------|------------------|
| 1 | (Tiếp từ bước 4 TC04) Form OTP hiển thị, nhập `111111` vào 6 ô OTP | Hệ thống kiểm tra: maOTP '111111' ≠ '482917'. Sai. Hiển thị: "Mã OTP không chính xác. Còn 2 lần thử." |
| 2 | Nhập `222222` vào 6 ô OTP | Hệ thống kiểm tra: maOTP '222222' ≠ '482917'. Sai. Hiển thị: "Mã OTP không chính xác. Còn 1 lần thử." |
| 3 | Nhập `333333` vào 6 ô OTP | Hệ thống kiểm tra: maOTP '333333' ≠ '482917'. Sai lần 3 → hủy phiên OTP |
| 4 | Hệ thống đánh dấu OTP đã xác minh (hủy) | Cập nhật tblOTP.daXacMinh = true (đã xử lý). Xóa dữ liệu đăng ký tạm |
| 5 | Hiển thị lỗi | Thông báo: "Mã OTP sai 3 lần. Phiên đăng ký đã bị hủy. Vui lòng đăng ký lại." Chuyển hướng về `/register` |

**Trạng thái CSDL sau:**

tblOTP
| ma | maOTP | loai | thoiHanHetHan | daXacMinh | tblUserMa |
|----|-------|------|---------------|-----------|-----------|
| 1 | 482917 | DANG_KY | 2026-06-01 10:05 | **true** | null |

tblUser: Không thay đổi. Không có tài khoản mới nào được tạo.

---

#### TC07: Đổi mật khẩu thành công

**Trạng thái CSDL trước:**

tblMembershipTier
| ma | tenHang | diemToiThieu | heSoUuDai |
|----|---------|-------------|-----------|
| 1 | Thường | 0 | 0.0 |
| 2 | Bạc | 1000 | 0.1 |
| 3 | Vàng | 5000 | 0.2 |
| 4 | Kim Cương | 20000 | 0.5 |

tblUser
| ma | hoTen | soDienThoai | email | matKhau | diemTichLuy | trangThai | tblMembershipTierMa |
|----|-------|-------------|-------|---------|-------------|-----------|---------------------|
| 1 | Nguyễn Văn A | 0912345678 | vana@email.com | $2a$10$hashAbc1234... | 1250 | Hoạt động | 2 |
| 2 | Lê Thị B | 0987654321 | b.lt@email.com | $2a$10$hashXyz5678... | 0 | Hoạt động | 1 |
| 3 | Phạm Minh C | 0909123456 | pmc@email.com | $2a$10$hashMno9012... | 5200 | Hoạt động | 3 |

tblLoginSession
| ma | tokenPhien | thoiGianDangNhap | thoiGianHetHan | thietBi | tblUserMa |
|----|-----------|-----------------|----------------|---------|-----------|
| 1 | tk_sess_001... | 2026-06-01 09:00 | 2026-06-01 21:00 | Chrome/Mac | 1 |
| 2 | tk_sess_002... | 2026-06-01 08:30 | 2026-06-01 20:30 | Safari/iPhone | 1 |

**Kịch bản thực hiện:**

| Bước | Hành động UI | Kết quả mong đợi |
|------|-------------|------------------|
| 1 | (Đã đăng nhập user ma=1) Nhấn avatar góc phải → chọn "Cài đặt tài khoản" | Chuyển sang trang `/account/settings` |
| 2 | Nhấn tab "Bảo mật" | Hiển thị form đổi mật khẩu với 3 ô: Mật khẩu hiện tại, Mật khẩu mới, Xác nhận mật khẩu mới |
| 3 | Nhập Mật khẩu hiện tại = `Abc@1234` | Ô nhập masked, viền xanh |
| 4 | Nhập Mật khẩu mới = `NewPass@2025` | Ô nhập masked. Thanh đánh giá độ mạnh hiển thị "Mạnh" (xanh lá) |
| 5 | Nhập Xác nhận = `NewPass@2025` | Ô nhập masked, khớp với MK mới, viền xanh |
| 6 | Nhấn nút [Lưu thay đổi] | Hệ thống xác minh: bcrypt('Abc@1234', storedHash) → khớp. Kiểm tra MK mới ≠ MK cũ, đạt yêu cầu phức tạp |
| 7 | Hệ thống cập nhật CSDL | Cập nhật tblUser.matKhau = bcrypt('NewPass@2025'). Thu hồi TẤT CẢ LoginSession của user ma=1 (trangThai = "Đã thu hồi") |
| 8 | Hiển thị thông báo | Toast: "Đổi mật khẩu thành công. Vui lòng đăng nhập lại." Chuyển hướng về `/login` |

**Trạng thái CSDL sau:**

tblUser
| ma | hoTen | soDienThoai | email | matKhau | diemTichLuy | trangThai | tblMembershipTierMa |
|----|-------|-------------|-------|---------|-------------|-----------|---------------------|
| 1 | Nguyễn Văn A | 0912345678 | vana@email.com | **$2a$10$hashNewPwxyz...** | 1250 | Hoạt động | 2 |
| 2 | Lê Thị B | 0987654321 | b.lt@email.com | $2a$10$hashXyz5678... | 0 | Hoạt động | 1 |
| 3 | Phạm Minh C | 0909123456 | pmc@email.com | $2a$10$hashMno9012... | 5200 | Hoạt động | 3 |

tblLoginSession
| ma | tokenPhien | thoiGianDangNhap | thoiGianHetHan | thietBi | trangThai | tblUserMa |
|----|-----------|-----------------|----------------|---------|-----------|-----------|
| 1 | tk_sess_001... | 2026-06-01 09:00 | 2026-06-01 21:00 | Chrome/Mac | **Đã thu hồi** | 1 |
| 2 | tk_sess_002... | 2026-06-01 08:30 | 2026-06-01 20:30 | Safari/iPhone | **Đã thu hồi** | 1 |

---

#### TC08: Mật khẩu hiện tại sai

**Trạng thái CSDL trước:**

tblMembershipTier
| ma | tenHang | diemToiThieu | heSoUuDai |
|----|---------|-------------|-----------|
| 1 | Thường | 0 | 0.0 |
| 2 | Bạc | 1000 | 0.1 |
| 3 | Vàng | 5000 | 0.2 |
| 4 | Kim Cương | 20000 | 0.5 |

tblUser
| ma | hoTen | soDienThoai | email | matKhau | diemTichLuy | trangThai | tblMembershipTierMa |
|----|-------|-------------|-------|---------|-------------|-----------|---------------------|
| 1 | Nguyễn Văn A | 0912345678 | vana@email.com | $2a$10$hashAbc1234... | 1250 | Hoạt động | 2 |
| 2 | Lê Thị B | 0987654321 | b.lt@email.com | $2a$10$hashXyz5678... | 0 | Hoạt động | 1 |
| 3 | Phạm Minh C | 0909123456 | pmc@email.com | $2a$10$hashMno9012... | 5200 | Hoạt động | 3 |

tblLoginSession
| ma | tokenPhien | thoiGianDangNhap | thoiGianHetHan | thietBi | tblUserMa |
|----|-----------|-----------------|----------------|---------|-----------|
| 1 | tk_sess_001... | 2026-06-01 09:00 | 2026-06-01 21:00 | Chrome/Mac | 1 |

**Kịch bản thực hiện:**

| Bước | Hành động UI | Kết quả mong đợi |
|------|-------------|------------------|
| 1 | (Đã đăng nhập user ma=1) Nhấn avatar → "Cài đặt tài khoản" → tab "Bảo mật" | Hiển thị form đổi mật khẩu |
| 2 | Nhập Mật khẩu hiện tại = `SaiPass@123` | Ô nhập masked |
| 3 | Nhập Mật khẩu mới = `NewPass@2025` | Thanh độ mạnh hiển thị "Mạnh" |
| 4 | Nhập Xác nhận = `NewPass@2025` | Khớp với MK mới |
| 5 | Nhấn nút [Lưu thay đổi] | Hệ thống xác minh: bcrypt('SaiPass@123', storedHash) → KHÔNG khớp |
| 6 | Hiển thị lỗi | Ô "Mật khẩu hiện tại" viền đỏ, thông báo: "Mật khẩu hiện tại không chính xác." Form giữ nguyên dữ liệu đã nhập |

**Trạng thái CSDL sau:** Không thay đổi.

---

#### TC09: Cập nhật thông tin thành công

**Trạng thái CSDL trước:**

tblMembershipTier
| ma | tenHang | diemToiThieu | heSoUuDai |
|----|---------|-------------|-----------|
| 1 | Thường | 0 | 0.0 |
| 2 | Bạc | 1000 | 0.1 |
| 3 | Vàng | 5000 | 0.2 |
| 4 | Kim Cương | 20000 | 0.5 |

tblUser
| ma | hoTen | soDienThoai | email | matKhau | diemTichLuy | trangThai | tblMembershipTierMa |
|----|-------|-------------|-------|---------|-------------|-----------|---------------------|
| 1 | Nguyễn Văn A | 0912345678 | vana@email.com | $2a$10$hashAbc1234... | 1250 | Hoạt động | 2 |
| 2 | Lê Thị B | 0987654321 | b.lt@email.com | $2a$10$hashXyz5678... | 0 | Hoạt động | 1 |
| 3 | Phạm Minh C | 0909123456 | pmc@email.com | $2a$10$hashMno9012... | 5200 | Hoạt động | 3 |

**Kịch bản thực hiện:**

| Bước | Hành động UI | Kết quả mong đợi |
|------|-------------|------------------|
| 1 | (Đã đăng nhập user ma=1) Nhấn avatar góc phải → "Hồ sơ cá nhân" | Chuyển sang trang `/account/profile`. Hiển thị thông tin: Họ tên = "Nguyễn Văn A", SĐT = "0912345678" (mờ, không sửa được), Email = "vana@email.com" |
| 2 | Nhấn nút [Chỉnh sửa thông tin] | Các ô Họ tên, Email chuyển sang chế độ có thể chỉnh sửa. Ô SĐT vẫn bị khóa (disabled) |
| 3 | Xóa ô Họ tên, nhập `Nguyễn Văn An` | Ô Họ tên hiển thị "Nguyễn Văn An" |
| 4 | Xóa ô Email, nhập `vanan@newemail.com` | Ô Email hiển thị "vanan@newemail.com", viền xanh (hợp lệ) |
| 5 | Nhấn nút [Lưu thay đổi] | Hệ thống kiểm tra: email 'vanan@newemail.com' chưa tồn tại trong tblUser. Hợp lệ |
| 6 | Hệ thống cập nhật CSDL | Cập nhật tblUser: hoTen = "Nguyễn Văn An", email = "vanan@newemail.com" WHERE ma = 1 |
| 7 | Hiển thị thông báo | Toast: "Cập nhật thông tin thành công!" Header cập nhật: "Xin chào, Nguyễn Văn An" |

**Trạng thái CSDL sau:**

tblUser
| ma | hoTen | soDienThoai | email | matKhau | diemTichLuy | trangThai | tblMembershipTierMa |
|----|-------|-------------|-------|---------|-------------|-----------|---------------------|
| 1 | **Nguyễn Văn An** | 0912345678 | **vanan@newemail.com** | $2a$10$hashAbc1234... | 1250 | Hoạt động | 2 |
| 2 | Lê Thị B | 0987654321 | b.lt@email.com | $2a$10$hashXyz5678... | 0 | Hoạt động | 1 |
| 3 | Phạm Minh C | 0909123456 | pmc@email.com | $2a$10$hashMno9012... | 5200 | Hoạt động | 3 |

---

#### TC10: Email đã được sử dụng khi cập nhật hồ sơ

**Trạng thái CSDL trước:**

tblMembershipTier
| ma | tenHang | diemToiThieu | heSoUuDai |
|----|---------|-------------|-----------|
| 1 | Thường | 0 | 0.0 |
| 2 | Bạc | 1000 | 0.1 |
| 3 | Vàng | 5000 | 0.2 |
| 4 | Kim Cương | 20000 | 0.5 |

tblUser
| ma | hoTen | soDienThoai | email | matKhau | diemTichLuy | trangThai | tblMembershipTierMa |
|----|-------|-------------|-------|---------|-------------|-----------|---------------------|
| 1 | Nguyễn Văn A | 0912345678 | vana@email.com | $2a$10$hashAbc1234... | 1250 | Hoạt động | 2 |
| 2 | Lê Thị B | 0987654321 | b.lt@email.com | $2a$10$hashXyz5678... | 0 | Hoạt động | 1 |
| 3 | Phạm Minh C | 0909123456 | pmc@email.com | $2a$10$hashMno9012... | 5200 | Hoạt động | 3 |

**Kịch bản thực hiện:**

| Bước | Hành động UI | Kết quả mong đợi |
|------|-------------|------------------|
| 1 | (Đã đăng nhập user ma=1) Nhấn avatar → "Hồ sơ cá nhân" | Hiển thị thông tin: Họ tên = "Nguyễn Văn A", SĐT = "0912345678", Email = "vana@email.com" |
| 2 | Nhấn nút [Chỉnh sửa thông tin] | Ô Họ tên, Email chuyển sang chế độ chỉnh sửa. Ô SĐT bị khóa |
| 3 | Xóa ô Email, nhập `b.lt@email.com` | Ô Email hiển thị "b.lt@email.com" |
| 4 | Nhấn nút [Lưu thay đổi] | Hệ thống kiểm tra: email 'b.lt@email.com' đã tồn tại trong tblUser (ma=2). Không hợp lệ |
| 5 | Hiển thị lỗi | Ô Email viền đỏ, thông báo: "Email này đã được đăng ký bởi tài khoản khác." Form giữ nguyên, không cập nhật CSDL |

**Trạng thái CSDL sau:** Không thay đổi.

---

#### TC11: Thêm nhân viên mới

**Trạng thái CSDL trước:**

tblMembershipTier
| ma | tenHang | diemToiThieu | heSoUuDai |
|----|---------|-------------|-----------|
| 1 | Thường | 0 | 0.0 |
| 2 | Bạc | 1000 | 0.1 |
| 3 | Vàng | 5000 | 0.2 |
| 4 | Kim Cương | 20000 | 0.5 |

tblUser
| ma | hoTen | soDienThoai | email | matKhau | diemTichLuy | trangThai | tblMembershipTierMa |
|----|-------|-------------|-------|---------|-------------|-----------|---------------------|
| 1 | Nguyễn Văn A | 0912345678 | vana@email.com | $2a$10$hashAbc1234... | 1250 | Hoạt động | 2 |
| 2 | Lê Thị B | 0987654321 | b.lt@email.com | $2a$10$hashXyz5678... | 0 | Hoạt động | 1 |
| 3 | Phạm Minh C | 0909123456 | pmc@email.com | $2a$10$hashMno9012... | 5200 | Hoạt động | 3 |

tblEmployee
| ma | hoTen | soDienThoai | email | vaiTro | trangThai | tblUserMa |
|----|-------|-------------|-------|--------|-----------|-----------|
| 1 | Trần Thị F | 0977111222 | f.tt@karaoke.com | Lễ tân | Đang làm | 1 |
| 2 | Hoàng Văn G | 0966333444 | g.hv@karaoke.com | Quản lý | Đang làm | 3 |

**Kịch bản thực hiện:**

| Bước | Hành động UI | Kết quả mong đợi |
|------|-------------|------------------|
| 1 | (Đăng nhập với quyền Quản lý) Nhấn menu "Quản lý" → "Nhân viên" | Chuyển sang trang `/admin/employees`. Hiển thị bảng danh sách 2 nhân viên hiện có (Trần Thị F, Hoàng Văn G) với các cột: Mã, Họ tên, Vai trò, Trạng thái, Thao tác |
| 2 | Nhấn nút [Thêm nhân viên] | Hiển thị modal/dialog "Thêm nhân viên mới" với các ô: Họ tên, SĐT, Email, Vai trò (dropdown: Lễ tân, Phục vụ, Quản lý, Kỹ thuật), Trạng thái (dropdown: Đang làm, Tạm nghỉ) |
| 3 | Nhập Họ tên = `Lê Văn H` | Ô nhập hiển thị "Lê Văn H" |
| 4 | Nhập SĐT = `0955666777` | Ô nhập hiển thị "0955666777", viền xanh (hợp lệ, 10 số) |
| 5 | Nhập Email = `h.lv@karaoke.com` | Ô nhập hiển thị "h.lv@karaoke.com", viền xanh (hợp lệ) |
| 6 | Chọn Vai trò = `Phục vụ` từ dropdown | Dropdown hiển thị "Phục vụ" |
| 7 | Chọn Trạng thái = `Đang làm` từ dropdown | Dropdown hiển thị "Đang làm" |
| 8 | Nhấn nút [Lưu] | Hệ thống kiểm tra: SĐT '0955666777' chưa tồn tại trong tblEmployee. Email 'h.lv@karaoke.com' chưa tồn tại. Hợp lệ |
| 9 | Hệ thống tạo Employee mới | Insert tblEmployee: ma=3, hoTen="Lê Văn H", soDienThoai="0955666777", email="h.lv@karaoke.com", vaiTro="Phục vụ", trangThai="Đang làm". Đồng thời tạo tài khoản User tương ứng (ma=4) |
| 10 | Hiển thị thông báo | Toast: "Thêm nhân viên thành công!" Modal đóng, bảng danh sách cập nhật hiển thị 3 nhân viên |

**Trạng thái CSDL sau:**

tblUser (thêm 1 dòng mới)
| ma | hoTen | soDienThoai | email | matKhau | diemTichLuy | trangThai | tblMembershipTierMa |
|----|-------|-------------|-------|---------|-------------|-----------|---------------------|
| 1 | Nguyễn Văn A | 0912345678 | vana@email.com | $2a$10$hashAbc1234... | 1250 | Hoạt động | 2 |
| 2 | Lê Thị B | 0987654321 | b.lt@email.com | $2a$10$hashXyz5678... | 0 | Hoạt động | 1 |
| 3 | Phạm Minh C | 0909123456 | pmc@email.com | $2a$10$hashMno9012... | 5200 | Hoạt động | 3 |
| **4** | **Lê Văn H** | **0955666777** | **h.lv@karaoke.com** | **$2a$10$hashStu7890...** | **0** | **Hoạt động** | **1** |

tblEmployee (thêm 1 dòng mới)
| ma | hoTen | soDienThoai | email | vaiTro | trangThai | tblUserMa |
|----|-------|-------------|-------|--------|-----------|-----------|
| 1 | Trần Thị F | 0977111222 | f.tt@karaoke.com | Lễ tân | Đang làm | 1 |
| 2 | Hoàng Văn G | 0966333444 | g.hv@karaoke.com | Quản lý | Đang làm | 3 |
| **3** | **Lê Văn H** | **0955666777** | **h.lv@karaoke.com** | **Phục vụ** | **Đang làm** | **4** |
