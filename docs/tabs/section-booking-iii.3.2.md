## 3.2. Thiết kế mô hình MVC

Mô hình MVC được thiết kế theo kiến trúc BCE (Boundary – Control – Entity) với 3 tầng:
- **Boundary (Giao diện):** React components xử lý giao diện người dùng
- **Control (Điều khiển):** Spring Boot Controllers xử lý nghiệp vụ
- **Entity (Thực thể):** JPA Entities biểu diễn dữ liệu lưu trữ

### a) Chức năng Đặt phòng

**1. Tầng giao diện (Boundary)**

| Lớp | Component | Mô tả |
|------|-----------|-------|
| **ReceptionistHomePage** | Page | Trang chính lễ tân, hiển thị danh sách booking hôm nay |
| **SearchFreeRoomForm** | Form | Tìm phòng trống theo thời gian và chi nhánh |
| **SearchClientForm** | Form | Tìm thông tin khách hàng theo tên/SĐT |
| **ConfirmBookingModal** | Modal | Xác nhận thông tin đặt phòng |

**2. Tầng điều khiển (Control)**

a) Tìm phòng trống => `searchFreeRoom()`
- Input: thời gian bắt đầu, thời gian kết thúc, mã chi nhánh
- Output: danh sách phòng trống
- Ứng viên tham số vào:
  - `searchFreeRoom(startTime: Date, endTime: Date, branchId: int)` → chọn (gom nhóm tham số)
  - `searchFreeRoom(startTime: Date, endTime: Date, branchId: int, roomType: String)` → chọn (thêm filter loại phòng)
- Ứng viên tham số ra:
  - `searchFreeRoom(): void` → loại (cần trả về danh sách)
  - `searchFreeRoom(): List<Phong>` → chọn (trả về danh sách phòng)

b) Tìm khách hàng => `searchClient()`
- Input: tên hoặc số điện thoại
- Output: danh sách khách hàng khớp
- Ứng viên tham số vào:
  - `searchClient(keyword: String)` → chọn (tìm theo cả tên và SĐT)
- Ứng viên tham số ra:
  - `searchClient(): List<KhachHang>` → chọn

c) Tạo booking => `createBooking()`
- Input: mã khách hàng, mã phòng, thời gian bắt đầu, thời gian kết thúc, mã nhân viên
- Output: đối tượng booking vừa tạo
- Ứng viên tham số vào:
  - `createBooking(clientId: int, roomId: int, startTime: Date, endTime: Date, staffId: int)` → chọn
- Ứng viên tham số ra:
  - `createBooking(): BookingResponse` → chọn (trả về thông tin booking)

d) Thay đổi trạng thái phòng => `updateRoomStatus()`
- Input: mã phòng, trạng thái mới
- Output: đối tượng phòng đã cập nhật
- Ứng viên tham số vào:
  - `updateRoomStatus(roomId: int, status: String)` → chọn
- Ứng viên tham số ra:
  - `updateRoomStatus(): Phong` → chọn

**3. Tầng thực thể (Entity)**

| Entity | Thuộc tính chính | Quan hệ |
|--------|-----------------|---------|
| **Phong** | id, tenPhong, loaiPhong, sucChua, giaTheoGio, trangThai | ManyToOne→ChiNhanh |
| **KhachHang** | id, hoTen, soDienThoai, email, diemTichLuy | ManyToOne→HangHoiVien |
| **ChiNhanh** | id, tenChiNhanh, diaChi | — |

### b) Chức năng Check-in

**1. Tầng giao diện (Boundary)**

| Lớp | Component | Mô tả |
|------|-----------|-------|
| **CheckInPage** | Page | Hiển thị danh sách booking "Chờ nhận", nút xác nhận check-in |

**2. Tầng điều khiển (Control)**

a) Lấy danh sách booking chờ => `getPendingBookings()`
- Input: mã chi nhánh, ngày
- Output: danh sách booking trạng thái "Chờ nhận"
- Ứng viên tham số vào:
  - `getPendingBookings(branchId: int, date: Date)` → chọn
- Ứng viên tham số ra:
  - `getPendingBookings(): List<BookingResponse>` → chọn

b) Xác nhận check-in => `checkIn()`
- Input: mã booking
- Output: booking đã cập nhật
- Ứng viên tham số vào:
  - `checkIn(bookingId: int)` → chọn
- Ứng viên tham số ra:
  - `checkIn(): BookingResponse` → chọn

**3. Tầng thực thể (Entity)**

| Entity | Thuộc tính chính | Quan hệ |
|--------|-----------------|---------|
| **Phong** | id, tenPhong, trangThai | ManyToOne→ChiNhanh |
| **KhachHang** | id, hoTen, soDienThoai | — |

### c) Chức năng Check-out

**1. Tầng giao diện (Boundary)**

| Lớp | Component | Mô tả |
|------|-----------|-------|
| **CheckOutPage** | Page | Hiển thị danh sách phòng đang hoạt động, tổng hợp hóa đơn |
| **InvoicePanel** | Panel | Hiển thị chi tiết hóa đơn, áp dụng voucher, chọn thanh toán |

**2. Tầng điều khiển (Control)**

a) Lấy danh sách phòng đang hoạt động => `getActiveRooms()`
- Input: mã chi nhánh
- Output: danh sách phòng trạng thái "Đang hoạt động"
- Ứng viên tham số vào:
  - `getActiveRooms(branchId: int)` → chọn
- Ứng viên tham số ra:
  - `getActiveRooms(): List<Phong>` → chọn

b) Tính tiền hóa đơn => `calculateInvoice()`
- Input: mã booking
- Output: chi tiết hóa đơn (tiền phòng, tiền dịch vụ, giảm giá, tổng)
- Ứng viên tham số vào:
  - `calculateInvoice(bookingId: int)` → chọn
- Ứng viên tham số ra:
  - `calculateInvoice(): HoaDon` → chọn

c) Xác nhận thanh toán => `confirmPayment()`
- Input: mã hóa đơn, phương thức thanh toán, mã voucher (nếu có)
- Output: hóa đơn đã thanh toán
- Ứng viên tham số vào:
  - `confirmPayment(invoiceId: int, paymentMethod: String, voucherCode: String)` → chọn
- Ứng viên tham số ra:
  - `confirmPayment(): HoaDon` → chọn

**3. Tầng thực thể (Entity)**

| Entity | Thuộc tính chính | Quan hệ |
|--------|-----------------|---------|
| **HoaDon** | id, ngayLap, tienPhong, tienDichVu, giamGia, tongTien | ManyToOne→KhachHang, ManyToOne→Phong |
| **ChiTietHoaDon** | id, tenDichVu, soLuong, donGia, thanhTien | ManyToOne→HoaDon |
| **KhuyenMai** | id, tenKhuyenMai, loai, giaTri | — |

### d) Chức năng Huỷ phòng

**1. Tầng giao diện (Boundary)**

| Lớp | Component | Mô tả |
|------|-----------|-------|
| **CancelBookingPage** | Page | Tìm và hủy booking trạng thái "Chờ nhận" |

**2. Tầng điều khiển (Control)**

a) Tìm booking => `searchBooking()`
- Input: tên khách, SĐT, hoặc mã booking
- Output: danh sách booking khớp
- Ứng viên tham số vào:
  - `searchBooking(keyword: String)` → chọn
- Ứng viên tham số ra:
  - `searchBooking(): List<BookingResponse>` → chọn

b) Hủy booking => `cancelBooking()`
- Input: mã booking
- Output: booking đã hủy
- Ứng viên tham số vào:
  - `cancelBooking(bookingId: int)` → chọn
- Ứng viên tham số ra:
  - `cancelBooking(): BookingResponse` → chọn

**3. Tầng thực thể (Entity)**

| Entity | Thuộc tính chính | Quan hệ |
|--------|-----------------|---------|
| **Phong** | id, tenPhong, trangThai | — |
| **KhachHang** | id, hoTen, soDienThoai | — |

### Sơ đồ lớp thiết kế

<!-- PLACEHOLDER: Chèn ảnh sơ đồ lớp thiết kế MVC tại đây -->
<!-- File: output/diagrams/booking_mvc_class.png -->

```plantuml
@startuml
left to right direction
skinparam linetype ortho
skinparam packageStyle rectangle
skinparam packageMaxWidth 800
skinparam classAttributeIconSize 0
skinparam classFontSize 11
skinparam packageFontSize 13
hide empty members

package "<<Boundary>>" #E3F2FD {
  class ReceptionistHomePage {
    +render()
  }
  class SearchFreeRoomForm {
    -startTime: Date
    -endTime: Date
    -branchId: int
    -roomType: String
    -results: List<Phong>
    +render()
  }
  class SearchClientForm {
    -keyword: String
    -selectedRoom: Phong
    -results: List<KhachHang>
    +render()
  }
  class ConfirmBookingModal {
    -booking: BookingResponse
    -room: Phong
    -customer: KhachHang
    -total: double
    +render()
  }
  class CheckInPage {
    -pendingBookings: List<BookingResponse>
    -selectedBooking: BookingResponse
    +render()
  }
  class CheckOutPage {
    -activeRooms: List<Phong>
    -invoice: HoaDon
    -paymentMethod: String
    +render()
  }
  class InvoicePanel {
    -invoice: HoaDon
    -discount: double
    -voucherCode: String
    +render()
  }
  class CancelBookingPage {
    -keyword: String
    -bookingList: List<BookingResponse>
    +render()
  }
}

package "<<Control>>" #E8F5E9 {
  class BookingController {
    +searchFreeRoom(startTime, endTime, branchId): List<Phong>
    +searchClient(keyword): List<KhachHang>
    +createBooking(clientId, roomId, startTime, endTime, staffId): BookingResponse
    +updateRoomStatus(roomId, status): Phong
    +getPendingBookings(branchId, date): List<BookingResponse>
    +checkIn(bookingId): BookingResponse
    +getActiveRooms(branchId): List<Phong>
    +calculateInvoice(bookingId): HoaDon
    +confirmPayment(invoiceId, paymentMethod, voucherCode): HoaDon
    +searchBooking(keyword): List<BookingResponse>
    +cancelBooking(bookingId): BookingResponse
  }
}

package "<<Entity>>" #FFF3E0 {
  class Phong {
    -id: int
    -tenPhong: String
    -loaiPhong: String
    -sucChua: int
    -giaTheoGio: double
    -trangThai: String
  }
  class KhachHang {
    -id: int
    -hoTen: String
    -soDienThoai: String
    -email: String
    -diemTichLuy: int
  }
  class HoaDon {
    -id: int
    -ngayLap: Date
    -tienPhong: double
    -tienDichVu: double
    -giamGia: double
    -tongTien: double
    -trangThaiThanhToan: String
  }
  class ChiTietHoaDon {
    -id: int
    -tenDichVu: String
    -soLuong: int
    -donGia: double
    -thanhTien: double
  }
  class KhuyenMai {
    -id: int
    -tenKhuyenMai: String
    -loai: String
    -giaTri: double
  }
  class ChiNhanh {
    -id: int
    -tenChiNhanh: String
    -diaChi: String
  }
  class HangHoiVien {
    -id: int
    -tenHang: String
    -diemToiThieu: int
    -heSoUuDai: double
  }
}

' Boundary -> Control
ReceptionistHomePage --> BookingController
SearchFreeRoomForm --> BookingController
SearchClientForm --> BookingController
ConfirmBookingModal --> BookingController
CheckInPage --> BookingController
CheckOutPage --> BookingController
InvoicePanel --> BookingController
CancelBookingPage --> BookingController

' Control -> Entity
BookingController --> Phong
BookingController --> KhachHang
BookingController --> HoaDon
BookingController --> ChiTietHoaDon
BookingController --> KhuyenMai
BookingController --> ChiNhanh

' Entity relationships
ChiNhanh *-- "n" Phong
KhachHang o-- "1" HangHoiVien
HoaDon *-- "n" ChiTietHoaDon
KhachHang o-- "n" HoaDon
Phong o-- "n" HoaDon
@enduml
```
