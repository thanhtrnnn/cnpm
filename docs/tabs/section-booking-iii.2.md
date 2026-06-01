## Thiết kế CSDL

### Bước 1 – Tạo bảng cho mỗi lớp thực thể

| Lớp thực thể | Tên bảng |
|--------------|----------|
| Client | tblClient |
| Branch | tblBranch |
| Room | tblRoom |
| Employee | tblEmployee |
| Room_receipt | tblRoom_receipt |
| Room_receipt_detail | tblRoom_receipt_detail |
| MemberRanking | tblMemberRanking |
| Promotion | tblPromotion |

### Bước 2 – Chuyển kiểu dữ liệu

| Kiểu Java | Kiểu SQL |
|-----------|----------|
| int | integer(10) |
| String | varchar(255) |
| double | double(10) |
| Date | date |

### Bước 3 – Xử lý quan hệ cardinality

- Branch – Room (1-n): Giữ riêng, Room có FK `tblBranchMa`
- Branch – Employee (1-n): Giữ riêng, Employee có FK `tblBranchMa`
- Client – MemberRanking (n-1): Giữ riêng, Client có FK `tblMemberRankingMa`
- Room_receipt – Room_receipt_detail (1-n): Giữ riêng, Room_receipt_detail có FK `tblRoom_receiptMa`
- Room_receipt – Promotion (n-n): Tạo bảng trung gian `tblApply_promotion`
- Client – Room_receipt (1-n): Room_receipt có FK `tblClientMa`
- Room – Room_receipt (1-n): Room_receipt có FK `tblRoomMa`
- Employee – Room_receipt (1-n): Room_receipt có FK `tblEmployeeMa`

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
' === VP Base Theme v2 ===
skinparam linetype ortho
skinparam defaultFontName "Arial"
skinparam defaultFontSize 10
skinparam shadowing false
skinparam arrowColor #000000
skinparam lineColor #000000
hide circle

entity "tblBranch" {
  * ma : integer(10) <<PK>>
  --
  tenBranch : varchar(255)
  diaChi : varchar(255)
  soDienThoai : varchar(20)
}

entity "tblRoom" {
  * ma : integer(10) <<PK>>
  --
  tenRoom : varchar(255)
  loaiRoom : varchar(50)
  sucChua : integer(10)
  giaTheoGio : double(10)
  trangThai : varchar(50)
  * tblBranchMa : integer(10) <<FK>>
}

entity "tblEmployee" {
  * ma : integer(10) <<PK>>
  --
  hoTen : varchar(255)
  vaiTro : varchar(50)
  trangThai : varchar(50)
  * tblBranchMa : integer(10) <<FK>>
}

entity "tblClient" {
  * ma : integer(10) <<PK>>
  --
  hoTen : varchar(255)
  soDienThoai : varchar(20)
  email : varchar(255)
  matKhau : varchar(255)
  ngayTao : date
  diemTichLuy : integer(10)
  trangThai : varchar(50)
  * tblMemberRankingMa : integer(10) <<FK>>
}

entity "tblMemberRanking" {
  * ma : integer(10) <<PK>>
  --
  tenHang : varchar(50)
  diemToiThieu : integer(10)
  moTa : varchar(255)
  heSoUuDai : double(10)
}

entity "tblRoom_receipt" {
  * ma : integer(10) <<PK>>
  --
  ngayLap : date
  thoiGianBatDau : date
  thoiGianKetThuc : date
  tienRoom : double(10)
  tienDichVu : double(10)
  giamGia : double(10)
  tongTien : double(10)
  trangThaiThanhToan : varchar(50)
  phuongThucThanhToan : varchar(50)
  * tblClientMa : integer(10) <<FK>>
  * tblRoomMa : integer(10) <<FK>>
  * tblEmployeeMa : integer(10) <<FK>>
}

entity "tblRoom_receipt_detail" {
  * ma : integer(10) <<PK>>
  --
  tenDichVu : varchar(255)
  soLuong : integer(10)
  donGia : double(10)
  thanhTien : double(10)
  * tblRoom_receiptMa : integer(10) <<FK>>
}

entity "tblPromotion" {
  * ma : integer(10) <<PK>>
  --
  tenPromotion : varchar(255)
  loai : varchar(50)
  giaTri : double(10)
  dieuKienApDung : varchar(255)
  ngayBatDau : date
  ngayKetThuc : date
}

entity "tblApply_promotion" {
  * tblRoom_receiptMa : integer(10) <<PK,FK>>
  * tblPromotionMa : integer(10) <<PK,FK>>
}

tblBranch ||--o{ tblRoom
tblBranch ||--o{ tblEmployee
tblMemberRanking ||--o{ tblClient
tblClient ||--o{ tblRoom_receipt
tblRoom ||--o{ tblRoom_receipt
tblEmployee ||--o{ tblRoom_receipt
tblRoom_receipt ||--o{ tblRoom_receipt_detail
tblRoom_receipt ||--o{ tblApply_promotion
tblPromotion ||--o{ tblApply_promotion
@enduml
```
