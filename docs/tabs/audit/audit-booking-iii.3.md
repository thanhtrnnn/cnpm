# Plan: Fix III.3 (Thiết kế tĩnh) — Module Đặt & trả phòng

## Mục tiêu
Đối chiếu III.1 (Entity class) + III.2 (ERD) với III.3.2 (MVC class) để tìm và sửa sai lệch.

---

## 1. So sánh Entity classes: III.1 vs III.3.2

### 1.1. KhachHang

| Thuộc tính | III.1 | III.3.2 | Status |
|------------|-------|---------|--------|
| id : int | ✓ | ✓ | OK |
| hoTen : String | ✓ | ✓ | OK |
| soDienThoai : String | ✓ | ✓ | OK |
| email : String | ✓ | ✓ | OK |
| matKhau : String | ✓ | ❌ MISSING | **CẦN THÊM** |
| ngayTao : Date | ✓ | ❌ MISSING | **CẦN THÊM** |
| diemTichLuy : int | ✓ | ✓ | OK |
| trangThai : String | ✓ | ❌ MISSING | **CẦN THÊM** |
| hangHoiVien : HangHoiVien | ✓ | ❌ (FK in ERD) | OK (FK) |

### 1.2. HoaDon

| Thuộc tính | III.1 | III.3.2 | Status |
|------------|-------|---------|--------|
| id : int | ✓ | ✓ | OK |
| ngayLap : Date | ✓ | ✓ | OK |
| thoiGianBatDau : Date | ✓ | ❌ MISSING | **CẦN THÊM** |
| thoiGianKetThuc : Date | ✓ | ❌ MISSING | **CẦN THÊM** |
| tienPhong : double | ✓ | ✓ | OK |
| tienDichVu : double | ✓ | ✓ | OK |
| giamGia : double | ✓ | ✓ | OK |
| tongTien : double | ✓ | ✓ | OK |
| trangThaiThanhToan : String | ✓ | ✓ | OK |
| phuongThucThanhToan : String | ✓ | ❌ MISSING | **CẦN THÊM** |
| khachHang : KhachHang | ✓ | ❌ MISSING | **CẦN THÊM** |
| phong : Phong | ✓ | ❌ MISSING | **CẦN THÊM** |
| nhanVien : NhanVien | ✓ | ❌ MISSING | **CẦN THÊM** |

### 1.3. KhuyenMai

| Thuộc tính | III.1 | III.3.2 | Status |
|------------|-------|---------|--------|
| id : int | ✓ | ✓ | OK |
| tenKhuyenMai : String | ✓ | ✓ | OK |
| loai : String | ✓ | ✓ | OK |
| giaTri : double | ✓ | ✓ | OK |
| dieuKienApDung : String | ✓ | ❌ MISSING | **CẦN THÊM** |
| ngayBatDau : Date | ✓ | ❌ MISSING | **CẦN THÊM** |
| ngayKetThuc : Date | ✓ | ❌ MISSING | **CẦN THÊM** |

### 1.4. ChiNhanh

| Thuộc tính | III.1 | III.3.2 | Status |
|------------|-------|---------|--------|
| id : int | ✓ | ✓ | OK |
| tenChiNhanh : String | ✓ | ✓ | OK |
| diaChi : String | ✓ | ✓ | OK |
| soDienThoai : String | ✓ | ❌ MISSING | **CẦN THÊM** |

### 1.5. HangHoiVien

| Thuộc tính | III.1 | III.3.2 | Status |
|------------|-------|---------|--------|
| id : int | ✓ | ✓ | OK |
| tenHang : String | ✓ | ✓ | OK |
| diemToiThieu : int | ✓ | ✓ | OK |
| moTa : String | ✓ | ❌ MISSING | **CẦN THÊM** |
| heSoUuDai : double | ✓ | ✓ | OK |

### 1.6. NhanVien

| Thuộc tính | III.1 | III.3.2 | Status |
|------------|-------|---------|--------|
| id : int | ✓ | ❌ MISSING | **CẦN THÊM** |
| hoTen : String | ✓ | ❌ MISSING | **CẦN THÊM** |
| vaiTro : String | ✓ | ❌ MISSING | **CẦN THÊM** |
| trangThai : String | ✓ | ❌ MISSING | **CẦN THÊM** |
| chiNhanh : ChiNhanh | ✓ | ❌ MISSING | **CẦN THÊM** |

→ **NhanVien bị thiếu hoàn toàn trong III.3.2 Entity package!**

### 1.7. Phong, ChiTietHoaDon — OK (đầy đủ)

---

## 2. So sánh Relationships: III.1 vs III.3.2

### III.1 relationships:
```
ChiNhanh *-- "n" Phong
ChiNhanh o-- "n" NhanVien
KhachHang o-- "1" HangHoiVien
HoaDon *-- "n" ChiTietHoaDon
KhachHang o-- "n" HoaDon
Phong o-- "n" HoaDon
NhanVien o-- "n" HoaDon
HoaDon o-- "n" KhuyenMai  (n-n qua tblApDungKhuyenMai)
```

### III.3.2 relationships (hiện tại):
```
ChiNhanh *-- "n" Phong ✓
KhachHang o-- "1" HangHoiVien ✓
HoaDon *-- "n" ChiTietHoaDon ✓
KhachHang o-- "n" HoaDon ✓
Phong o-- "n" HoaDon ✓
```

### MẤU QUAN HỆ:
- ❌ `ChiNhanh o-- "n" NhanVien` — thiếu (vì thiếu NhanVien)
- ❌ `NhanVien o-- "n" HoaDon` — thiếu (vì thiếu NhanVien)
- ❌ `HoaDon o-- "n" KhuyenMai` — thiếu quan hệ n-n

---

## 3. So sánh ERD (III.2) vs III.3.2 Entity

### ERD tables:
- tblChiNhanh, tblPhong, tblNhanVien, tblKhachHang, tblHangHoiVien, tblHoaDon, tblChiTietHoaDon, tblKhuyenMai, tblApDungKhuyenMai

### III.3.2 Entity classes:
- ChiNhanh, Phong, KhachHang, HangHoiVien, HoaDon, ChiTietHoaDon, KhuyenMai

### MẤU:
- ❌ **NhanVien** — có trong ERD nhưng không có trong III.3.2 Entity
- ❌ **tblApDungKhuyenMai** — junction table trong ERD, cần thể hiện trong III.3.2

---

## 4. Tóm tắt việc cần sửa

### 4.1. Entity package — THÊM:
1. **NhanVien class** mới: id, hoTen, vaiTro, trangThai, chiNhanh
2. **KhachHang**: thêm matKhau, ngayTao, trangThai
3. **HoaDon**: thêm thoiGianBatDau, thoiGianKetThuc, phuongThucThanhToan, khachHang, phong, nhanVien
4. **KhuyenMai**: thêm dieuKienApDung, ngayBatDau, ngayKetThuc
5. **ChiNhanh**: thêm soDienThoai
6. **HangHoiVien**: thêm moTa

### 4.2. Relationships — THÊM:
1. `ChiNhanh o-- "n" NhanVien`
2. `NhanVien o-- "n" HoaDon`
3. `HoaDon o-- "n" KhuyenMai` (thể hiện junction table)

### 4.3. Control package — KIỂM TRA:
- NhanVien có cần controller riêng không? (Hiện tại không có chức năng quản lý NV trong module này)
- BookingController có cần thêm method nào cho NhanVien không?

### 4.4. Boundary package — KIỂM TRA:
- ReceptionistHomePage có cần hiển thị thông tin nhân viên không?

---

## 5. Thứ tự thực hiện

1. ✍️ Cập nhật Entity classes trong III.3.2 markdown
2. 🔄 Regenerate PlantUML diagram (booking_mvc_class.png)
3. 📄 Regenerate DOCX
4. ✅ Verify: so sánh lại với III.1 và III.2

---

**Bạn xác nhận plan này? Muốn điều chỉnh gì không?**
