## 2.5. Biểu đồ lớp thực thể pha phân tích

### a) Chức năng "Đặt phòng"

**Boundary:** ReceptionistHomeView, SearchFreeRoomView, SearchClientView, ConfirmView
**Entity:** Phong, KhachHang, ChiNhanh

```plantuml
@startuml
skinparam classAttributeIconSize 0

class ReceptionistHomeView {
  +hienThi()
}

class SearchFreeRoomView {
  +nhapThoiGian()
  +timPhongTrong()
  +hienThiKetQua()
}

class SearchClientView {
  +nhapThongTinKH()
  +timKiemKH()
  +hienThiKH()
}

class ConfirmView {
  +hienThiXacNhan()
  +xacNhan()
}

class Phong {
  +maPhong : int
  +tenPhong : String
  +trangThai : String
  +timPhongTrong(thoiGianBD, thoiGianKT) : List
  +doiTrangThai(trangThaiMoi)
}

class KhachHang {
  +maKH : int
  +hoTen : String
  +soDienThoai : String
  +timKiemKH(keyword) : List
}

ReceptionistHomeView --> SearchFreeRoomView
SearchFreeRoomView --> SearchClientView
SearchClientView --> ConfirmView
SearchFreeRoomView --> Phong
SearchClientView --> KhachHang
@enduml
```

### b) Chức năng "Huỷ phòng"

**Boundary:** ReceptionistHomeView, SearchBookingView, ConfirmCancelView
**Entity:** Phong, KhachHang

```plantuml
@startuml
skinparam classAttributeIconSize 0

class ReceptionistHomeView {
  +hienThi()
}

class SearchBookingView {
  +nhapThongTin()
  +timBooking()
  +hienThiKetQua()
}

class ConfirmCancelView {
  +hienThiXacNhan()
  +xacNhanHuy()
}

class Phong {
  +maPhong : int
  +trangThai : String
  +doiTrangThai(trangThaiMoi)
}

class KhachHang {
  +maKH : int
  +hoTen : String
}

ReceptionistHomeView --> SearchBookingView
SearchBookingView --> ConfirmCancelView
SearchBookingView --> Phong
SearchBookingView --> KhachHang
@enduml
```

### c) Chức năng "Check-in"

**Boundary:** ReceptionistHomeView, CheckInView, ConfirmCheckInView
**Entity:** Phong, KhachHang

```plantuml
@startuml
skinparam classAttributeIconSize 0

class ReceptionistHomeView {
  +hienThi()
}

class CheckInView {
  +hienThiDanhSach()
  +chonBooking()
  +xacNhanCheckIn()
}

class ConfirmCheckInView {
  +hienThiXacNhan()
  +xacNhan()
}

class Phong {
  +maPhong : int
  +trangThai : String
  +doiTrangThai(trangThaiMoi)
  +batDauTinhGio()
}

class KhachHang {
  +maKH : int
  +hoTen : String
}

ReceptionistHomeView --> CheckInView
CheckInView --> ConfirmCheckInView
CheckInView --> Phong
CheckInView --> KhachHang
@enduml
```

### d) Chức năng "Check-out"

**Boundary:** ReceptionistHomeView, CheckOutView, InvoiceView, PaymentView
**Entity:** Phong, HoaDon, ChiTietHoaDon, KhachHang, KhuyenMai

```plantuml
@startuml
skinparam classAttributeIconSize 0

class ReceptionistHomeView {
  +hienThi()
}

class CheckOutView {
  +hienThiDanhSach()
  +chonPhong()
}

class InvoiceView {
  +tinhHoaDon()
  +hienThiHoaDon()
}

class PaymentView {
  +chonPhuongThuc()
  +xuLyThanhToan()
  +inHoaDon()
}

class Phong {
  +maPhong : int
  +trangThai : String
  +doiTrangThai(trangThaiMoi)
}

class HoaDon {
  +maHD : int
  +tongTien : double
  +trangThai : String
  +tinhTien()
}

class ChiTietHoaDon {
  +maCTHD : int
  +tenDichVu : String
  +soLuong : int
  +donGia : double
}

class KhachHang {
  +maKH : int
  +hoTen : String
  +hangHoiVien : String
}

class KhuyenMai {
  +maKM : int
  +tenKM : String
  +giaTri : double
  +apDung(hoaDon)
}

ReceptionistHomeView --> CheckOutView
CheckOutView --> InvoiceView
InvoiceView --> PaymentView
CheckOutView --> Phong
InvoiceView --> HoaDon
InvoiceView --> ChiTietHoaDon
InvoiceView --> KhachHang
PaymentView --> KhuyenMai
@enduml
```

---

## 2.6. Biểu đồ tuần tự pha phân tích

### 4.1. Chức năng "Đặt phòng"

```plantuml
@startuml
actor "Nhan vien le tan" as NV
participant "ReceptionistHomeView" as Home
participant "SearchFreeRoomView" as SearchRoom
participant "SearchClientView" as SearchClient
participant "ConfirmView" as Confirm
entity "Phong" as Phong
entity "KhachHang" as KH

NV -> Home: click "Dat phong"
Home -> SearchRoom: hienThi()
NV -> SearchRoom: nhapThoiGian(batDau, ketThuc)
NV -> SearchRoom: timPhongTrong()
SearchRoom -> Phong: timPhongTrong(batDau, ketThuc)
Phong --> SearchRoom: danhSachPhong
SearchRoom --> NV: hienThiKetQua(danhSachPhong)
NV -> SearchRoom: chonPhong(maPhong)
SearchRoom -> SearchClient: hienThi()
NV -> SearchClient: nhapThongTinKH(hoTen, sdt)
NV -> SearchClient: timKiemKH(keyword)
SearchClient -> KH: timKiemKH(keyword)
KH --> SearchClient: danhSachKH
SearchClient --> NV: hienThiKH(danhSachKH)
NV -> SearchClient: chonKH(maKH)
SearchClient -> Confirm: hienThiXacNhan(maPhong, maKH)
NV -> Confirm: xacNhan()
Confirm -> Phong: doiTrangThai("Cho nhan")
Phong --> Confirm: thanhCong
Confirm --> NV: hienThi("Dat phong thanh cong")
NV -> Confirm: clickOK()
Confirm -> Home: hienThi()
@enduml
```

**Kịch bản phiên bản 2 - Đặt phòng tại chi nhánh**

1. Nhân viên lễ tân click chức năng "Đặt phòng" trên giao diện ReceptionistHomeView.
2. Lớp ReceptionistHomeView gọi sang lớp SearchFreeRoomView.
3. Lớp SearchFreeRoomView hiển thị cho nhân viên.
4. Nhân viên hỏi khách hàng thời gian đặt phòng.
5. Khách hàng trả lời.
6. Nhân viên nhập thời gian đặt phòng mong muốn của khách vào ô thời gian và ấn nút tìm kiếm.
7. Lớp SearchFreeRoomView gọi đến lớp Phong để xử lý thông tin.
8. Lớp Phong gọi hàm timPhongTrong().
9. Lớp Phong trả kết quả về cho SearchFreeRoomView.
10. Lớp SearchFreeRoomView hiển thị danh sách các phòng trống cho nhân viên.
11. Nhân viên ấn vào phòng trống.
12. Lớp SearchFreeRoomView gọi sang lớp SearchClientView.
13. Lớp SearchClientView hiển thị.
14. Nhân viên hỏi khách hàng về thông tin khách hàng.
15. Khách hàng trả lời.
16. Nhân viên nhập thông tin khách hàng và ấn nút tìm kiếm.
17. Lớp SearchClientView gọi đến lớp KhachHang.
18. Lớp KhachHang gọi hàm timKiemKH().
19. Lớp KhachHang trả kết quả về cho lớp SearchClientView.
20. Lớp SearchClientView hiển thị thông tin khách hàng tương ứng.
21. Nhân viên chọn thông tin khách hàng tương ứng.
22. Lớp SearchClientView gọi sang lớp ConfirmView.
23. Lớp ConfirmView hiển thị.
24. Nhân viên ấn xác nhận.
25. Lớp ConfirmView gọi đến lớp Phong để xử lý.
26. Lớp Phong gọi hàm doiTrangThai("Cho nhan").
27. Lớp Phong trả kết quả về lớp ConfirmView.
28. Lớp ConfirmView hiện thông báo.
29. Nhân viên ấn OK.
30. Lớp ConfirmView gọi lại về lớp ReceptionistHomeView.
31. Lớp ReceptionistHomeView hiển thị.

**Ngoại lệ:**
- Phòng trống không tìm thấy: SearchFreeRoomView hiển thị "Không có phòng trống trong khung giờ này."
- Khách hàng chưa có trong CSDL: SearchClientView hiển thị nút [Đăng ký nhanh]. Nhân viên nhập thông tin mới, hệ thống tạo khách hàng mới trước khi tiếp tục.

---

### 4.2. Chức năng "Huỷ phòng"

```plantuml
@startuml
actor "Nhan vien le tan" as NV
participant "ReceptionistHomeView" as Home
participant "SearchBookingView" as SearchBooking
participant "ConfirmCancelView" as Confirm
entity "Phong" as Phong

NV -> Home: click "Quan ly dat phong"
Home -> SearchBooking: hienThi()
NV -> SearchBooking: nhapThongTin(keyword)
NV -> SearchBooking: timBooking()
SearchBooking -> Phong: timBooking(keyword)
Phong --> SearchBooking: danhSachBooking
SearchBooking --> NV: hienThiKetQua(danhSachBooking)
NV -> SearchBooking: chonBooking(maBooking)
SearchBooking -> Confirm: hienThiXacNhan(maBooking)
NV -> Confirm: xacNhanHuy()
Confirm -> Phong: doiTrangThai("Da huy")
Phong --> Confirm: thanhCong
Confirm --> NV: hienThi("Huy dat phong thanh cong")
NV -> Confirm: clickOK()
Confirm -> Home: hienThi()
@enduml
```

**Kịch bản phiên bản 2 - Huỷ phòng**

1. Nhân viên lễ tân click chức năng "Quản lý đặt phòng" trên giao diện ReceptionistHomeView.
2. Lớp ReceptionistHomeView gọi sang lớp SearchBookingView.
3. Lớp SearchBookingView hiển thị.
4. Nhân viên nhập thông tin tìm kiếm (tên khách, SĐT, hoặc mã booking).
5. Nhân viên ấn nút tìm kiếm.
6. Lớp SearchBookingView gọi đến lớp Phong.
7. Lớp Phong gọi hàm timBooking(keyword).
8. Lớp Phong trả kết quả về cho SearchBookingView.
9. Lớp SearchBookingView hiển thị danh sách booking tìm thấy.
10. Nhân viên chọn booking cần hủy.
11. Lớp SearchBookingView gọi sang lớp ConfirmCancelView.
12. Lớp ConfirmCancelView hiển thị xác nhận.
13. Nhân viên ấn [Đồng ý].
14. Lớp ConfirmCancelView gọi đến lớp Phong.
15. Lớp Phong gọi hàm doiTrangThai("Da huy").
16. Lớp Phong trả kết quả về.
17. Lớp ConfirmCancelView hiện thông báo thành công.
18. Nhân viên ấn OK.
19. Lớp ConfirmCancelView gọi về ReceptionistHomeView.

**Ngoại lệ:**
- Không tìm thấy booking: SearchBookingView hiển thị "Không tìm thấy booking phù hợp."
- Booking đã quá thời gian hủy: ConfirmCancelView hiển thị "Booking đã quá thời gian hủy."

---

### 4.3. Chức năng "Check-in"

```plantuml
@startuml
actor "Nhan vien le tan" as NV
participant "ReceptionistHomeView" as Home
participant "CheckInView" as CheckIn
participant "ConfirmCheckInView" as Confirm
entity "Phong" as Phong

NV -> Home: click "Check-in"
Home -> CheckIn: hienThiDanhSach()
CheckIn -> Phong: layDanhSachBooking("Cho nhan")
Phong --> CheckIn: danhSachBooking
CheckIn --> NV: hienThiDanhSach(danhSachBooking)
NV -> CheckIn: chonBooking(maBooking)
CheckIn -> Confirm: hienThiXacNhan(maBooking)
NV -> Confirm: xacNhan()
Confirm -> Phong: doiTrangThai("Dang hoat dong")
Phong -> Phong: batDauTinhGio()
Phong --> Confirm: thanhCong
Confirm --> NV: hienThi("Check-in thanh cong")
NV -> Confirm: clickOK()
Confirm -> Home: hienThi()
@enduml
```

**Kịch bản phiên bản 2 - Check-in**

1. Nhân viên lễ tân click chức năng "Check-in" trên giao diện chính.
2. Lớp ReceptionistHomeView gọi sang lớp CheckInView.
3. Lớp CheckInView hiển thị danh sách booking "Chờ nhận".
4. Nhân viên chọn booking cần check-in.
5. Lớp CheckInView gọi sang lớp ConfirmCheckInView.
6. Lớp ConfirmCheckInView hiển thị thông tin xác nhận.
7. Nhân viên ấn [Xác nhận Check-in].
8. Lớp ConfirmCheckInView gọi đến lớp Phong.
9. Lớp Phong gọi hàm doiTrangThai("Dang hoat dong").
10. Lớp Phong gọi hàm batDauTinhGio().
11. Lớp Phong trả kết quả về.
12. Lớp ConfirmCheckInView hiện thông báo thành công.
13. Nhân viên ấn OK.
14. Lớp ConfirmCheckInView gọi về ReceptionistHomeView.

**Ngoại lệ:**
- Phòng đang dọn dẹp: Phong trả về lỗi. CheckInView hiển thị "Phòng đang dọn dẹp, vui lòng chờ."
- Khách hàng không đến: Nhân viên chọn hủy booking thay vì check-in.

---

### 4.4. Chức năng "Check-out"

```plantuml
@startuml
actor "Nhan vien le tan" as NV
participant "ReceptionistHomeView" as Home
participant "CheckOutView" as CheckOut
participant "InvoiceView" as Invoice
participant "PaymentView" as Payment
entity "Phong" as Phong
entity "HoaDon" as HD
entity "KhachHang" as KH
entity "KhuyenMai" as KM

NV -> Home: click "Check-out"
Home -> CheckOut: hienThiDanhSach()
CheckOut -> Phong: layDanhSachPhong("Dang hoat dong")
Phong --> CheckOut: danhSachPhong
CheckOut --> NV: hienThiDanhSach(danhSachPhong)
NV -> CheckOut: chonPhong(maPhong)
CheckOut -> Invoice: tinhHoaDon(maPhong)
Invoice -> HD: tinhTien()
HD --> Invoice: hoaDon
Invoice -> KH: layThongTinKH()
KH --> Invoice: khachHang
Invoice -> KM: kiemTraUuDai(maKH)
KM --> Invoice: uuDai
Invoice --> NV: hienThiHoaDon(hoaDon, uuDai)
NV -> Invoice: chonPhuongThuc("Tien mat")
Invoice -> Payment: xuLyThanhToan(maHD, phuongThuc)
Payment -> HD: capNhatTrangThai("Da thanh toan")
Payment -> Phong: doiTrangThai("Trong")
HD --> Payment: thanhCong
Phong --> Payment: thanhCong
Payment --> NV: hienThi("Check-out thanh cong")
NV -> Payment: inHoaDon()
Payment --> NV: hoaDonIn
@enduml
```

**Kịch bản phiên bản 2 - Check-out**

1. Nhân viên lễ tân click chức năng "Check-out" trên giao diện chính.
2. Lớp ReceptionistHomeView gọi sang lớp CheckOutView.
3. Lớp CheckOutView hiển thị danh sách phòng đang hoạt động.
4. Nhân viên chọn phòng cần check-out.
5. Lớp CheckOutView gọi sang lớp InvoiceView.
6. Lớp InvoiceView gọi hàm tinhHoaDon() trên lớp HoaDon.
7. Lớp HoaDon trả kết quả hóa đơn về InvoiceView.
8. InvoiceView gọi lớp KhachHang để lấy thông tin khách.
9. InvoiceView gọi lớp KhuyenMai để kiểm tra ưu đãi.
10. InvoiceView hiển thị hóa đơn cho nhân viên.
11. Nhân viên chọn phương thức thanh toán "Tiền mặt".
12. Nhân viên ấn [Xác nhận thanh toán].
13. InvoiceView gọi lớp Payment.
14. Payment gọi hàm capNhatTrangThai("Da thanh toan") trên HoaDon.
15. Payment gọi hàm doiTrangThai("Trong") trên Phong.
16. Payment hiện thông báo thành công.
17. Nhân viên ấn [In hóa đơn].

**Ngoại lệ:**
- Voucher không hợp lệ: InvoiceView hiển thị "Mã voucher không hợp lệ hoặc đã hết hạn."
- Thanh toán chuyển khoản thất bại: PaymentView hiển thị lỗi, yêu cầu chọn lại phương thức.
