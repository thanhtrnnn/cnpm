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
| **Room** | roomID, name, type, capacity, hourly_pricing, branchID, status | ManyToOne→Branch |
| **Customer** | customerID, name, phone_number, account_status, rankingID | ManyToOne→MemberRanking |
| **Branch** | branchID, name, address, phone_number | — |

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
| **Room** | roomID, name, status | ManyToOne→Branch |
| **Customer** | customerID, name, phone_number | — |

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
| **Room_receipt** | room_receipt_ID, room_fee, service_fee, discount, status, payment_method | ManyToOne→Customer, ManyToOne→Room |
| **Room_receipt_detail** | room_receipt_detail_ID, service_name, base_price, quantity, duration, total | ManyToOne→Room_receipt |
| **Promotion** | promotionID, name, type, redeem, valid_until | — |

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
| **Room** | roomID, name, status | — |
| **Customer** | customerID, name, phone_number | — |

### Sơ đồ lớp thiết kế

<!-- PLACEHOLDER: Chèn ảnh sơ đồ lớp thiết kế MVC tại đây -->
<!-- File: output/diagrams/booking_mvc_class.png -->

```plantuml
@startuml
' === VP Base Theme v2 ===
left to right direction
skinparam linetype ortho
skinparam defaultFontName "Arial"
skinparam defaultFontSize 10
skinparam shadowing false
skinparam arrowColor #000000
skinparam lineColor #000000
hide circle

skinparam class {
  BackgroundColor #FFFFFF
  BorderColor #000000
  FontColor #000000
  FontSize 11
  AttributeFontSize 9
  AttributeIconSize 0
  BorderThickness 1
}

skinparam package {
  BackgroundColor #FFFFFF
  BorderColor #000000
}

skinparam packageStyle rectangle
skinparam packageMaxWidth 800
hide empty members

package "<<Boundary>>" #E3F2FD {
  together {
    class ReceptionistHomePage {
      -btnDatPhong : Button
      -btnCheckIn : Button
      -btnCheckOut : Button
      -tblBookings : Table
      +formLoad() : void
      +btnDatPhongClick() : void
      +btnCheckInClick() : void
      +btnCheckOutClick() : void
      +displayBookings(bookings : List) : void
    }
    class SearchFreeRoomForm {
      -txtStartTime : TextBox
      -txtEndTime : TextBox
      -cmbBranch : Select
      -cmbRoomType : Select
      -btnSearch : Button
      -tblRooms : Table
      +formLoad() : void
      +btnSearchClick() : void
      +displayRooms(rooms : List) : void
      +tblRoomsClick(selectedRow : int) : void
    }
    class SearchClientForm {
      -txtHoTen : TextBox
      -txtSDT : TextBox
      -btnSearch : Button
      -tblClients : Table
      +formLoad(roomId : int) : void
      +btnSearchClick() : void
      +displayClients(clients : List) : void
      +tblClientsClick(selectedRow : int) : void
    }
    class ConfirmBookingModal {
      -lblKhachHang : Label
      -lblPhong : Label
      -lblThoiGian : Label
      -lblTongTien : Label
      -btnConfirm : Button
      -btnCancel : Button
      +formLoad(booking : BookingResponse) : void
      +btnConfirmClick() : void
      +btnCancelClick() : void
      +showMessage(msg : String) : void
    }
  }
  together {
    class CheckInPage {
      -tblPendingBookings : Table
      -btnCheckIn : Button
      +formLoad() : void
      +btnCheckInClick() : void
      +displayPendingBookings(bookings : List) : void
      +showMessage(msg : String) : void
    }
    class CheckOutPage {
      -tblActiveRooms : Table
      -btnCheckOut : Button
      +formLoad() : void
      +btnCheckOutClick() : void
      +displayActiveRooms(rooms : List) : void
    }
    class InvoicePanel {
      -lblTienPhong : Label
      -lblTienDichVu : Label
      -lblGiamGia : Label
      -lblTongTien : Label
      -txtVoucher : TextBox
      -cmbPhuongThuc : Select
      -btnThanhToan : Button
      -btnInHoaDon : Button
      +formLoad(invoice : Room_receipt) : void
      +btnThanhToanClick() : void
      +btnInHoaDonClick() : void
      +showMessage(msg : String) : void
    }
    class CancelBookingPage {
      -txtKeyword : TextBox
      -btnSearch : Button
      -tblBookings : Table
      -btnCancel : Button
      +formLoad() : void
      +btnSearchClick() : void
      +btnCancelClick() : void
      +displayBookings(bookings : List) : void
      +showMessage(msg : String) : void
    }
  }
}

package "<<Control>>" #E8F5E9 {
  class RoomController {
    +getAll() : List<Room>
    +getById(id : int) : Room
    +searchFreeRoom(startTime : Date, endTime : Date, branchId : int) : List<Room>
    +updateStatus(roomId : int, status : String) : Room
    +getActiveRooms(branchId : int) : List<Room>
    +getPendingBookings(branchId : int, date : Date) : List<BookingResponse>
  }
  class ClientController {
    +getAll() : List<Customer>
    +getById(id : int) : Customer
    +search(keyword : String) : List<Customer>
  }
  class BookingController {
    +createBooking(clientId : int, roomId : int, startTime : Date, endTime : Date, staffId : int) : BookingResponse
    +checkIn(bookingId : int) : BookingResponse
    +cancelBooking(bookingId : int) : BookingResponse
    +searchBooking(keyword : String) : List<BookingResponse>
  }
  class InvoiceController {
    +calculateInvoice(bookingId : int) : Room_receipt
    +confirmPayment(invoiceId : int, paymentMethod : String, voucherCode : String) : Room_receipt
    +getById(id : int) : Room_receipt
  }
}

package "<<Entity>>" #FFF3E0 {
  class Room {
    -roomID: int
    -name: String
    -type: String
    -capacity: int
    -hourly_pricing: float
    -branchID: String
    -status: String
  }
  class Customer {
    -customerID: int
    -rankingID: int
    -name: String
    -phone_number: String
    -account_status: String
  }
  class Room_receipt {
    -room_receipt_ID: int
    -room_fee: float
    -checkin_time: datetime
    -checkout_time: datetime
    -service_fee: float
    -damage_fee: float
    -discount: float
    -status: String
    -payment_method: String
  }
  class Room_receipt_detail {
    -room_receipt_detail_ID: int
    -room_receipt_ID: int
    -roomID: int
    -service_name: String
    -base_price: float
    -quantity: int
    -duration: float
    -total: float
  }
  class Promotion {
    -promotionID: int
    -name: String
    -type: String
    -redeem: String
    -valid_until: datetime
  }
  class Branch {
    -branchID: int
    -name: String
    -address: String
    -phone_number: String
  }
  class MemberRanking {
    -rankingID: int
    -name: String
    -base_score: bigint
    -coupon: int
  }
}

' Boundary -> Control
ReceptionistHomePage --> RoomController
SearchFreeRoomForm --> RoomController
SearchClientForm --> ClientController
ConfirmBookingModal --> BookingController
CheckInPage --> BookingController
CheckOutPage --> RoomController
InvoicePanel --> InvoiceController
CancelBookingPage --> BookingController

' Control -> Entity
RoomController --> Room
ClientController --> Customer
BookingController --> Room_receipt
BookingController --> Room
InvoiceController --> Room_receipt
InvoiceController --> Room_receipt_detail

' Entity relationships
Branch *-- "n" Room
MemberRanking o-- "1" Customer
Room_receipt *-- "n" Room_receipt_detail
Customer o-- "n" Room_receipt
Room o-- "n" Room_receipt
@enduml
```
