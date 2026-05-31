## 1.1. Lập kế hoạch test

### Bảng Test Case (tổng hợp)

| TT | Module | Test case |
|----|--------|-----------|
| TC01 | Đặt phòng | Đặt phòng thành công khi có phòng trống |
| TC02 | Đặt phòng | Không tìm thấy phòng trống theo thời gian yêu cầu |
| TC03 | Đặt phòng | Khách hàng chưa có trong CSDL |
| TC04 | Check-in | Check-in thành công với booking trạng thái "Chờ nhận" |
| TC05 | Check-in | Phòng đang dọn dẹp, không thể check-in |
| TC06 | Check-out | Check-out thành công, thanh toán tiền mặt |
| TC07 | Check-out | Check-out với voucher giảm giá |
| TC08 | Check-out | Voucher không hợp lệ |
| TC09 | Huỷ phòng | Hủy đặt phòng thành công |
| TC10 | Huỷ phòng | Không tìm thấy booking |
| TC11 | Huỷ phòng | Booking đã quá thời gian hủy |

## 1.2. Các test case cho từng chức năng

### TC01: Đặt phòng thành công

**Trạng thái CSDL trước khi test:**

tblChiNhanh
| ma | tenChiNhanh | diaChi |
|----|-------------|--------|
| 1 | Karaoke Quận 1 | 123 Lê Lợi, Q1 |

tblPhong
| ma | tenPhong | loaiPhong | giaTheoGio | trangThai | tblChiNhanhMa |
|----|----------|-----------|------------|-----------|---------------|
| 1 | P.VIP1 | Super VIP | 200000 | Trống | 1 |
| 2 | P.Std3 | Standard | 100000 | Trống | 1 |

tblKhachHang
| ma | hoTen | soDienThoai | email | tblHangHoiVienMa |
|----|-------|-------------|-------|-------------------|
| 1 | Nguyễn Văn An | 0912345678 | vana@email.com | 2 |

tblNhanVien
| ma | hoTen | vaiTro | tblChiNhanhMa |
|----|-------|--------|---------------|
| 1 | Trần Thị B | Lễ tân | 1 |

**Kịch bản thực hiện + Kết quả mong đợi:**

| Kịch bản | Kết quả mong đợi |
|----------|------------------|
| 1. NV click [Đặt phòng] | Hiển thị SearchFreeRoomView |
| 2. NV nhập: ngày 30/05/2026, từ 14:00, đến 17:00, chi nhánh Quận 1 | Form hiển thị đầy đủ |
| 3. NV click [Tìm phòng trống] | Hiển thị danh sách: P.VIP1 (200.000đ/giờ), P.Std3 (100.000đ/giờ) |
| 4. NV chọn P.VIP1 | Chuyển sang SearchClientView, hiển thị "Phòng: P.VIP1" |
| 5. NV nhập "0912345678" và click [Tìm kiếm] | Hiển thị: Nguyễn Văn An, 0912345678, Hạng Bạc |
| 6. NV chọn khách hàng | Chuyển sang ConfirmBookingView |
| 7. NV click [Xác nhận đặt phòng] | Hiển thị "Đặt phòng thành công!" |

**Trạng thái CSDL sau khi test:**

tblPhong
| ma | tenPhong | trangThai |
|----|----------|-----------|
| 1 | P.VIP1 | **Chờ nhận** ← thay đổi |
| 2 | P.Std3 | Trống |

tblBooking (mới tạo)
| ma | thoiGianBatDau | thoiGianKetThuc | trangThai | tblKhachHangMa | tblPhongMa | tblNhanVienMa |
|----|----------------|-----------------|-----------|----------------|------------|---------------|
| 1 | 30/05/2026 14:00 | 30/05/2026 17:00 | Chờ nhận | 1 | 1 | 1 |

---

### TC06: Check-out thành công, thanh toán tiền mặt

**Trạng thái CSDL trước khi test:**

tblPhong
| ma | tenPhong | trangThai |
|----|----------|-----------|
| 1 | P.VIP1 | Đang hoạt động |

tblBooking
| ma | thoiGianBatDau | thoiGianKetThuc | trangThai | tblKhachHangMa | tblPhongMa |
|----|----------------|-----------------|-----------|----------------|------------|
| 1 | 30/05/2026 14:05 | null | Đang hoạt động | 1 | 1 |

tblChiTietHoaDon
| ma | tenDichVu | soLuong | donGia | tblHoaDonMa |
|----|-----------|---------|--------|-------------|
| 1 | Lon bia Heineken | 2 | 50000 | null |
| 2 | Dĩa trái cây | 1 | 150000 | null |

tblKhachHang
| ma | hoTen | diemTichLuy | tblHangHoiVienMa |
|----|-------|-------------|-------------------|
| 1 | Nguyễn Văn An | 1250 | 2 |

tblHangHoiVien
| ma | tenHang | heSoUuDai |
|----|---------|-----------|
| 2 | Bạc | 0.1 |

**Kịch bản thực hiện + Kết quả mong đợi:**

| Kịch bản | Kết quả mong đợi |
|----------|------------------|
| 1. NV click [Check-out] | Hiển thị danh sách phòng "Đang hoạt động": P.VIP1 |
| 2. NV chọn P.VIP1 | Chuyển sang InvoicePanel |
| 3. Hệ thống tính tiền | Hiển thị: Tiền phòng 534.000đ (2h40p × 200.000đ), Dịch vụ 250.000đ, Giảm 10% = -78.400đ, Tổng: 705.600đ |
| 4. NV chọn "Tiền mặt" | Form chọn thanh toán |
| 5. NV click [Xác nhận thanh toán] | Hiển thị "Check-out thành công! Tổng: 705.600đ" |

**Trạng thái CSDL sau khi test:**

tblPhong
| ma | tenPhong | trangThai |
|----|----------|-----------|
| 1 | P.VIP1 | **Trống** ← thay đổi |

tblHoaDon (mới tạo)
| ma | ngayLap | tienPhong | tienDichVu | giamGia | tongTien | trangThaiThanhToan | phuongThucThanhToan | tblKhachHangMa |
|----|---------|-----------|------------|---------|----------|--------------------|--------------------|----------------|
| 1 | 30/05/2026 | 534000 | 250000 | 78400 | 705600 | Đã thanh toán | Tiền mặt | 1 |

tblKhachHang
| ma | hoTen | diemTichLuy |
|----|-------|-------------|
| 1 | Nguyễn Văn An | **1321** ← cộng 71 điểm (705600/10000) |

---

### TC09: Hủy đặt phòng thành công

**Trạng thái CSDL trước khi test:**

tblPhong
| ma | tenPhong | trangThai |
|----|----------|-----------|
| 1 | P.VIP1 | Chờ nhận |

tblBooking
| ma | thoiGianBatDau | trangThai | tblKhachHangMa | tblPhongMa |
|----|----------------|-----------|----------------|------------|
| 1 | 30/05/2026 14:00 | Chờ nhận | 1 | 1 |

**Kịch bản thực hiện + Kết quả mong đợi:**

| Kịch bản | Kết quả mong đợi |
|----------|------------------|
| 1. NV click [Quản lý đặt phòng] | Hiển thị danh sách booking "Chờ nhận" |
| 2. NV nhập "0912345678" và tìm | Hiển thị: BK001, Nguyễn Văn An, P.VIP1, 14:00 |
| 3. NV chọn booking | Hiển thị chi tiết + nút [Hủy đặt phòng] |
| 4. NV click [Hủy đặt phòng] | Hiển thị "Bạn có chắc chắn?" |
| 5. NV click [Đồng ý] | Hiển thị "Hủy đặt phòng thành công." |

**Trạng thái CSDL sau khi test:**

tblPhong
| ma | tenPhong | trangThai |
|----|----------|-----------|
| 1 | P.VIP1 | **Trống** ← thay đổi |

tblBooking
| ma | trangThai |
|----|-----------|
| 1 | **Đã hủy** ← thay đổi |
