## Thiết kế CSDL

### Bước 1 – Tạo bảng cho mỗi lớp thực thể

| Lớp thực thể | Tên bảng |
|--------------|----------|
| KhachHang | tblKhachHang |
| ChiNhanh | tblChiNhanh |
| Phong | tblPhong |
| NhanVien | tblNhanVien |
| HoaDon | tblHoaDon |
| ChiTietHoaDon | tblChiTietHoaDon |
| HangHoiVien | tblHangHoiVien |
| KhuyenMai | tblKhuyenMai |

### Bước 2 – Chuyển kiểu dữ liệu

| Kiểu Java | Kiểu SQL |
|-----------|----------|
| int | integer(10) |
| String | varchar(255) |
| double | double(10) |
| Date | date |

### Bước 3 – Xử lý quan hệ cardinality

- ChiNhanh – Phong (1-n): Giữ riêng, Phong có FK `tblChiNhanhMa`
- ChiNhanh – NhanVien (1-n): Giữ riêng, NhanVien có FK `tblChiNhanhMa`
- KhachHang – HangHoiVien (n-1): Giữ riêng, KhachHang có FK `tblHangHoiVienMa`
- HoaDon – ChiTietHoaDon (1-n): Giữ riêng, ChiTietHoaDon có FK `tblHoaDonMa`
- HoaDon – KhuyenMai (n-n): Tạo bảng trung gian `tblApDungKhuyenMai`
- KhachHang – HoaDon (1-n): HoaDon có FK `tblKhachHangMa`
- Phong – HoaDon (1-n): HoaDon có FK `tblPhongMa`
- NhanVien – HoaDon (1-n): HoaDon có FK `tblNhanVienMa`

### Bước 4 – Bổ sung PK/FK

- PK: thuộc tính `id` → `ma : integer(10) <<PK>>`
- FK: đặt tên `tbl[TenBangCha]Ma`

### Bước 5 – Loại bỏ thuộc tính dư thừa

- Bỏ thuộc tính kiểu đối tượng (đã chuyển thành FK)
- Bỏ thuộc tính dẫn xuất (nếu có)

### Biểu đồ ERD

<!-- PLACEHOLDER: Chèn ảnh ERD tại đây -->
<!-- File: output/diagrams/booking_erd.png -->

```plantuml
@startuml
skinparam linetype ortho
hide circle

entity "tblChiNhanh" {
  * ma : integer(10) <<PK>>
  --
  tenChiNhanh : varchar(255)
  diaChi : varchar(255)
  soDienThoai : varchar(20)
}

entity "tblPhong" {
  * ma : integer(10) <<PK>>
  --
  tenPhong : varchar(255)
  loaiPhong : varchar(50)
  sucChua : integer(10)
  giaTheoGio : double(10)
  trangThai : varchar(50)
  * tblChiNhanhMa : integer(10) <<FK>>
}

entity "tblNhanVien" {
  * ma : integer(10) <<PK>>
  --
  hoTen : varchar(255)
  vaiTro : varchar(50)
  trangThai : varchar(50)
  * tblChiNhanhMa : integer(10) <<FK>>
}

entity "tblKhachHang" {
  * ma : integer(10) <<PK>>
  --
  hoTen : varchar(255)
  soDienThoai : varchar(20)
  email : varchar(255)
  matKhau : varchar(255)
  ngayTao : date
  diemTichLuy : integer(10)
  trangThai : varchar(50)
  * tblHangHoiVienMa : integer(10) <<FK>>
}

entity "tblHangHoiVien" {
  * ma : integer(10) <<PK>>
  --
  tenHang : varchar(50)
  diemToiThieu : integer(10)
  moTa : varchar(255)
  heSoUuDai : double(10)
}

entity "tblHoaDon" {
  * ma : integer(10) <<PK>>
  --
  ngayLap : date
  thoiGianBatDau : date
  thoiGianKetThuc : date
  tienPhong : double(10)
  tienDichVu : double(10)
  giamGia : double(10)
  tongTien : double(10)
  trangThaiThanhToan : varchar(50)
  phuongThucThanhToan : varchar(50)
  * tblKhachHangMa : integer(10) <<FK>>
  * tblPhongMa : integer(10) <<FK>>
  * tblNhanVienMa : integer(10) <<FK>>
}

entity "tblChiTietHoaDon" {
  * ma : integer(10) <<PK>>
  --
  tenDichVu : varchar(255)
  soLuong : integer(10)
  donGia : double(10)
  thanhTien : double(10)
  * tblHoaDonMa : integer(10) <<FK>>
}

entity "tblKhuyenMai" {
  * ma : integer(10) <<PK>>
  --
  tenKhuyenMai : varchar(255)
  loai : varchar(50)
  giaTri : double(10)
  dieuKienApDung : varchar(255)
  ngayBatDau : date
  ngayKetThuc : date
}

entity "tblApDungKhuyenMai" {
  * tblHoaDonMa : integer(10) <<PK,FK>>
  * tblKhuyenMaiMa : integer(10) <<PK,FK>>
}

tblChiNhanh ||--o{ tblPhong
tblChiNhanh ||--o{ tblNhanVien
tblHangHoiVien ||--o{ tblKhachHang
tblKhachHang ||--o{ tblHoaDon
tblPhong ||--o{ tblHoaDon
tblNhanVien ||--o{ tblHoaDon
tblHoaDon ||--o{ tblChiTietHoaDon
tblHoaDon ||--o{ tblApDungKhuyenMai
tblKhuyenMai ||--o{ tblApDungKhuyenMai
@enduml
```
