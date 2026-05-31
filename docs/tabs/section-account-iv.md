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
