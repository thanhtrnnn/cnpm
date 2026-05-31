## Thiết kế lớp thực thể

### Bước 1 – Bổ sung thuộc tính `id`

Thêm thuộc tính `id : int` vào các lớp không kế thừa từ lớp khác:

- KhachHang: `id : int`
- ChiNhanh: `id : int`
- Phong: `id : int`
- NhanVien: `id : int`
- HoaDon: `id : int`
- ChiTietHoaDon: `id : int`
- HangHoiVien: `id : int`
- KhuyenMai: `id : int`

### Bước 2 – Thêm kiểu dữ liệu

Chuyển tất cả thuộc tính sang kiểu ngôn ngữ lập trình (Java):

- KhachHang: `id : int`, `hoTen : String`, `soDienThoai : String`, `email : String`, `matKhau : String`, `ngayTao : Date`, `diemTichLuy : int`, `trangThai : String`
- ChiNhanh: `id : int`, `tenChiNhanh : String`, `diaChi : String`, `soDienThoai : String`
- Phong: `id : int`, `tenPhong : String`, `loaiPhong : String`, `sucChua : int`, `giaTheoGio : double`, `trangThai : String`
- NhanVien: `id : int`, `hoTen : String`, `vaiTro : String`, `trangThai : String`
- HoaDon: `id : int`, `ngayLap : Date`, `thoiGianBatDau : Date`, `thoiGianKetThuc : Date`, `tienPhong : double`, `tienDichVu : double`, `giamGia : double`, `tongTien : double`, `trangThaiThanhToan : String`, `phuongThucThanhToan : String`
- ChiTietHoaDon: `id : int`, `tenDichVu : String`, `soLuong : int`, `donGia : double`, `thanhTien : double`
- HangHoiVien: `id : int`, `tenHang : String`, `diemToiThieu : int`, `moTa : String`, `heSoUuDai : double`
- KhuyenMai: `id : int`, `tenKhuyenMai : String`, `loai : String`, `giaTri : double`, `dieuKienApDung : String`, `ngayBatDau : Date`, `ngayKetThuc : Date`

### Bước 3 – Chuyển quan hệ association thành aggregation/composition

- ChiNhanh `*--` Phong: composition (phòng không tồn tại nếu không có chi nhánh)
- ChiNhanh `o--` NhanVien: aggregation (nhân viên tồn tại độc lập)
- KhachHang `o--` HangHoiVien: aggregation (hạng hội viên là danh mục độc lập)
- HoaDon `*--` ChiTietHoaDon: composition (chi tiết không tồn tại nếu không có hóa đơn)
- Phong `o--` HoaDon: aggregation (hóa đơn tồn tại độc lập khỏi phòng)
- KhachHang `o--` HoaDon: aggregation
- NhanVien `o--` HoaDon: aggregation

### Bước 4 – Bổ sung thuộc tính kiểu đối tượng

- HoaDon: `khachHang : KhachHang`, `phong : Phong`, `nhanVien : NhanVien`
- ChiTietHoaDon: `hoaDon : HoaDon`
- Phong: `chiNhanh : ChiNhanh`
- NhanVien: `chiNhanh : ChiNhanh`
- KhachHang: `hangHoiVien : HangHoiVien`

### Biểu đồ lớp thực thể

<!-- PLACEHOLDER: Chèn ảnh sơ đồ lớp thực thể tại đây -->
<!-- File: output/diagrams/booking_entity_class.png -->

```plantuml
@startuml
skinparam classAttributeIconSize 0
skinparam classFontSize 11
hide empty members

title Thiết kế lớp thực thể - Module Đặt & trả phòng

class KhachHang {
  -id : int
  -hoTen : String
  -soDienThoai : String
  -email : String
  -matKhau : String
  -ngayTao : Date
  -diemTichLuy : int
  -trangThai : String
  -hangHoiVien : HangHoiVien
}

class ChiNhanh {
  -id : int
  -tenChiNhanh : String
  -diaChi : String
  -soDienThoai : String
}

class Phong {
  -id : int
  -tenPhong : String
  -loaiPhong : String
  -sucChua : int
  -giaTheoGio : double
  -trangThai : String
  -chiNhanh : ChiNhanh
}

class NhanVien {
  -id : int
  -hoTen : String
  -vaiTro : String
  -trangThai : String
  -chiNhanh : ChiNhanh
}

class HoaDon {
  -id : int
  -ngayLap : Date
  -thoiGianBatDau : Date
  -thoiGianKetThuc : Date
  -tienPhong : double
  -tienDichVu : double
  -giamGia : double
  -tongTien : double
  -trangThaiThanhToan : String
  -phuongThucThanhToan : String
  -khachHang : KhachHang
  -phong : Phong
  -nhanVien : NhanVien
}

class ChiTietHoaDon {
  -id : int
  -tenDichVu : String
  -soLuong : int
  -donGia : double
  -thanhTien : double
  -hoaDon : HoaDon
}

class HangHoiVien {
  -id : int
  -tenHang : String
  -diemToiThieu : int
  -moTa : String
  -heSoUuDai : double
}

class KhuyenMai {
  -id : int
  -tenKhuyenMai : String
  -loai : String
  -giaTri : double
  -dieuKienApDung : String
  -ngayBatDau : Date
  -ngayKetThuc : Date
}

ChiNhanh *-- "n" Phong
ChiNhanh o-- "n" NhanVien
KhachHang o-- "1" HangHoiVien
HoaDon *-- "n" ChiTietHoaDon
KhachHang o-- "n" HoaDon
Phong o-- "n" HoaDon
NhanVien o-- "n" HoaDon
HoaDon o-- "n" KhuyenMai
@enduml
```
