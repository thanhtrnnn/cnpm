## 4.1. Chức năng "Đặt phòng" — Thiết kế

### Biểu đồ tuần tự

<!-- PLACEHOLDER: Chèn ảnh tuần tự Đặt phòng tại đây -->
<!-- File: output/diagrams/booking_seq_datphong.png -->

```plantuml
@startuml
left to right direction
actor "Nhân viên lễ tân" as NV
participant "ReceptionistHomePage\n<<Boundary>>" as Home
participant "SearchFreeRoomForm\n<<Boundary>>" as SearchRoom
participant "BookingController\n<<Control>>" as Ctrl
participant "SearchClientForm\n<<Boundary>>" as SearchClient
participant "ConfirmBookingModal\n<<Boundary>>" as Confirm
entity "Room\n<<Entity>>" as Room
entity "Customer\n<<Entity>>" as Cust
entity "Room_receipt\n<<Entity>>" as RR

NV -> Home: click "Dat phong"
activate Home
Home -> SearchRoom: navigate()
activate SearchRoom
Home -> NV: hien thi SearchFreeRoomForm

NV -> SearchRoom: nhap startTime, endTime, branchId
NV -> SearchRoom: click [Tim phong trong]
SearchRoom -> Ctrl: searchFreeRoom(startTime, endTime, branchId)
activate Ctrl
Ctrl -> Room: findByTimeAndBranch(startTime, endTime, branchId)
activate Room
Room --> Ctrl: List<Room>
deactivate Room
Ctrl --> SearchRoom: List<Room>
deactivate Ctrl
SearchRoom --> NV: hien thi danh sach phong trong

NV -> SearchRoom: chon phong (roomId)
SearchRoom -> SearchClient: navigate(roomId)
activate SearchClient
SearchRoom -> NV: hien thi SearchClientForm

NV -> SearchClient: nhap keyword (ten/SDT)
NV -> SearchClient: click [Tim kiem]
SearchClient -> Ctrl: searchClient(keyword)
activate Ctrl
Ctrl -> Cust: findByKeyword(keyword)
activate Cust
Cust --> Ctrl: List<Customer>
deactivate Cust
Ctrl --> SearchClient: List<Customer>
deactivate Ctrl
SearchClient --> NV: hien thi danh sach khach hang

NV -> SearchClient: chon khach hang (clientId)
SearchClient -> Confirm: navigate(roomId, clientId, timeRange)
activate Confirm
SearchClient -> NV: hien thi ConfirmBookingModal

NV -> Confirm: click [Xac nhan dat phong]
Confirm -> Ctrl: createBooking(clientId, roomId, startTime, endTime, staffId)
activate Ctrl
Ctrl -> RR: updateStatus(roomId, "Cho nhan")
activate RR
RR --> Ctrl: Room_receipt updated
deactivate RR
Ctrl -> Ctrl: saveBooking()
Ctrl --> Confirm: BookingResponse
deactivate Ctrl
Confirm --> NV: hien thi "Dat phong thanh cong!"
deactivate Confirm

NV -> Confirm: click [OK]
Confirm -> Home: navigate()
deactivate SearchRoom
deactivate SearchClient
@enduml
```

### Kịch bản phiên bản 3

**Kịch bản phiên bản 3 - Đặt phòng**

1. Nhân viên lễ tân click chức năng "Đặt phòng" trên giao diện ReceptionistHomePage.
2. Phương thức btnDatPhongClick() của lớp ReceptionistHomePage được gọi.
3. Phương thức btnDatPhongClick() gọi phương thức navigate() của lớp SearchFreeRoomForm.
4. Lớp SearchFreeRoomForm hiển thị form tìm phòng trống cho nhân viên.
5. Nhân viên hỏi khách hàng thời gian đặt phòng.
6. Khách hàng trả lời.
7. Nhân viên nhập thời gian bắt đầu (startTime), thời gian kết thúc (endTime) và chọn chi nhánh (branchId).
8. Nhân viên click nút [Tìm phòng trống].
9. Phương thức btnSearchClick() của lớp SearchFreeRoomForm được gọi.
10. Phương thức btnSearchClick() gọi phương thức searchFreeRoom(startTime: Date, endTime: Date, branchId: int) của lớp BookingController.
11. Phương thức searchFreeRoom() gọi phương thức findByTimeAndBranch(startTime, endTime, branchId) của lớp Entity Room.
12. Lớp Room trả kết quả danh sách phòng trống về cho phương thức searchFreeRoom().
13. Phương thức searchFreeRoom() trả kết quả về cho phương thức btnSearchClick().
14. Lớp SearchFreeRoomForm hiển thị danh sách phòng trống cho nhân viên.
15. Nhân viên ấn vào phòng trống.
16. Phương thức tblRoomsClick(selectedRow: int) của lớp SearchFreeRoomForm được gọi.
17. Phương thức tblRoomsClick() gọi phương thức navigate(roomId) của lớp SearchClientForm.
18. Lớp SearchClientForm hiển thị form tìm khách hàng cho nhân viên.
19. Nhân viên hỏi khách hàng về thông tin khách hàng.
20. Khách hàng trả lời.
21. Nhân viên nhập thông tin khách hàng (tên hoặc số điện thoại) và click [Tìm kiếm].
22. Phương thức btnSearchClick() của lớp SearchClientForm được gọi.
23. Phương thức btnSearchClick() gọi phương thức searchClient(keyword: String) của lớp BookingController.
24. Phương thức searchClient() gọi phương thức findByKeyword(keyword) của lớp Entity Customer.
25. Lớp Customer trả kết quả danh sách khách hàng về cho phương thức searchClient().
26. Phương thức searchClient() trả kết quả về cho phương thức btnSearchClick().
27. Lớp SearchClientForm hiển thị danh sách khách hàng khớp.
28. Nhân viên chọn thông tin khách hàng tương ứng.
29. Phương thức tblClientsClick(selectedRow: int) của lớp SearchClientForm được gọi.
30. Phương thức tblClientsClick() gọi phương thức navigate(roomId, clientId, timeRange) của lớp ConfirmBookingModal.
31. Lớp ConfirmBookingModal hiển thị thông tin xác nhận đặt phòng.
32. Nhân viên ấn nút xác nhận.
33. Phương thức btnConfirmClick() của lớp ConfirmBookingModal được gọi.
34. Phương thức btnConfirmClick() gọi phương thức createBooking(clientId: int, roomId: int, startTime: Date, endTime: Date, staffId: int) của lớp BookingController.
35. Phương thức createBooking() gọi phương thức updateStatus(roomId, "Chờ nhận") của lớp Entity Room_receipt.
36. Lớp Room_receipt cập nhật trạng thái và trả kết quả về cho phương thức createBooking().
37. Phương thức createBooking() lưu booking vào CSDL và trả BookingResponse về cho phương thức btnConfirmClick().
38. Lớp ConfirmBookingModal hiển thị thông báo "Đặt phòng thành công!".
39. Nhân viên ấn nút OK.
40. Phương thức showMessage() của lớp ConfirmBookingModal được gọi.
41. Phương thức showMessage() gọi phương thức navigate() của lớp ReceptionistHomePage.
42. Hệ thống quay về giao diện chính ReceptionistHomePage.

**Ngoại lệ:**
- **Phòng trống không tìm thấy:** Phương thức searchFreeRoom() trả về danh sách rỗng. Lớp SearchFreeRoomForm hiển thị "Không có phòng trống trong khung giờ này."
- **Khách hàng chưa có trong CSDL:** Lớp SearchClientForm hiển thị nút [Đăng ký nhanh]. Nhân viên nhập thông tin mới, hệ thống tạo khách hàng mới trước khi tiếp tục.
17. Phương thức createBooking(clientId: int, roomId: int, startTime: Date, endTime: Date, staffId: int) của lớp BookingController được gọi.
18. BookingController cập nhật trạng thái phòng thành "Chờ nhận" và lưu booking vào CSDL.
19. ConfirmBookingModal hiển thị thông báo "Đặt phòng thành công!".
20. Nhân viên click [OK], hệ thống quay về ReceptionistHomePage.

**Ngoại lệ:**
- **Phòng trống không tìm thấy:** BookingController trả về danh sách rỗng. SearchFreeRoomForm hiển thị "Không có phòng trống trong khung giờ này."
- **Khách hàng chưa có trong CSDL:** SearchClientForm hiển thị nút [Đăng ký nhanh]. Nhân viên nhập thông tin mới, hệ thống tạo khách hàng mới trước khi tiếp tục.

---

## 4.2. Chức năng "Check-in" — Thiết kế

### Biểu đồ tuần tự

<!-- PLACEHOLDER: Chèn ảnh tuần tự Check-in tại đây -->
<!-- File: output/diagrams/booking_seq_checkin.png -->

```plantuml
@startuml
actor "Nhân viên lễ tân" as NV
participant "CheckInPage\n<<Boundary>>" as CheckIn
participant "BookingController\n<<Control>>" as Ctrl
entity "Room\n<<Entity>>" as Room
entity "Room_receipt\n<<Entity>>" as RR

NV -> CheckIn: click "Check-in"
activate CheckIn
CheckIn -> Ctrl: getPendingBookings(branchId, today)
activate Ctrl
Ctrl -> Ctrl: findByStatus("Cho nhan")
Ctrl --> CheckIn: List<BookingResponse>
deactivate Ctrl
CheckIn --> NV: hien thi danh sach booking cho

NV -> CheckIn: chon booking can check-in
NV -> CheckIn: click [Xac nhan Check-in]
CheckIn -> Ctrl: checkIn(bookingId)
activate Ctrl
Ctrl -> Room: updateStatus(roomId, "Dang hoat dong")
activate Room
Room --> Ctrl: Room updated
deactivate Room
Ctrl -> RR: setStartTime(now)
Ctrl --> CheckIn: BookingResponse
deactivate Ctrl
CheckIn --> NV: "Check-in thanh cong!"
deactivate CheckIn
@enduml
```

### Kịch bản phiên bản 3

**Kịch bản phiên bản 3 - Check-in**

1. Nhân viên lễ tân click chức năng "Check-in" trên giao diện ReceptionistHomePage.
2. Phương thức btnCheckInClick() của lớp ReceptionistHomePage được gọi.
3. Phương thức btnCheckInClick() gọi phương thức navigate() của lớp CheckInPage.
4. Lớp CheckInPage hiển thị danh sách booking chờ nhận phòng.
5. Phương thức formLoad() của lớp CheckInPage được gọi.
6. Phương thức formLoad() gọi phương thức getPendingBookings(branchId: int, date: Date) của lớp BookingController.
7. Phương thức getPendingBookings() gọi phương thức findByStatus("Chờ nhận") của lớp Entity Room.
8. Lớp Room trả kết quả danh sách booking về cho phương thức getPendingBookings().
9. Phương thức getPendingBookings() trả kết quả về cho phương thức formLoad().
10. Lớp CheckInPage hiển thị danh sách booking "Chờ nhận" hôm nay cho nhân viên.
11. Nhân viên hỏi khách hàng thông tin (tên hoặc mã đặt phòng) để đối chiếu.
12. Khách hàng trả lời.
13. Nhân viên ấn chọn booking tương ứng cần check-in trên danh sách.
14. Phương thức tblPendingBookingsClick(selectedRow: int) của lớp CheckInPage được gọi.
15. Phương thức tblPendingBookingsClick() gọi phương thức navigate(bookingId) của lớp ConfirmCheckInView.
16. Lớp ConfirmCheckInView hiển thị thông tin chi tiết của phòng và khách hàng.
17. Nhân viên ấn nút xác nhận check-in.
18. Phương thức btnCheckInClick() của lớp ConfirmCheckInView được gọi.
19. Phương thức btnCheckInClick() gọi phương thức checkIn(bookingId: int) của lớp BookingController.
20. Phương thức checkIn() gọi phương thức updateStatus(roomId, "Đang hoạt động") của lớp Entity Room.
21. Lớp Room cập nhật trạng thái và trả kết quả về cho phương thức checkIn().
22. Phương thức checkIn() gọi phương thức setStartTime(now) của lớp Entity Room_receipt.
23. Lớp Room_receipt ghi nhận thời gian bắt đầu và trả kết quả về cho phương thức checkIn().
24. Phương thức checkIn() trả BookingResponse về cho phương thức btnCheckInClick().
25. Lớp ConfirmCheckInView hiển thị thông báo "Check-in thành công! Phòng [tên phòng] đã sẵn sàng."
26. Nhân viên ấn nút quay lại.
27. Phương thức showMessage() của lớp ConfirmCheckInView được gọi.
28. Phương thức showMessage() gọi phương thức navigate() của lớp ReceptionistHomePage.
29. Hệ thống quay về giao diện chính ReceptionistHomePage.

**Ngoại lệ:**
- **Phòng đang dọn dẹp:** Phương thức checkIn() kiểm tra trạng thái phòng, trả về lỗi. Lớp ConfirmCheckInView hiển thị "Phòng đang dọn dẹp, vui lòng chờ."
- **Khách hàng không đến:** Nhân viên chọn hủy booking thay vì check-in. Phương thức cancelBooking() của BookingController được gọi, chuyển trạng thái booking sang "Đã hủy".

---

## 4.3. Chức năng "Check-out" — Thiết kế

### Biểu đồ tuần tự

<!-- PLACEHOLDER: Chèn ảnh tuần tự Check-out tại đây -->
<!-- File: output/diagrams/booking_seq_checkout.png -->

```plantuml
@startuml
actor "Nhân viên lễ tân" as NV
participant "CheckOutPage\n<<Boundary>>" as CheckOut
participant "InvoicePanel\n<<Boundary>>" as Invoice
participant "BookingController\n<<Control>>" as Ctrl
entity "HoaDon\n<<Entity>>" as HD
entity "Phong\n<<Entity>>" as Phong

NV -> CheckOut: click "Check-out"
activate CheckOut
CheckOut -> Ctrl: getActiveRooms(branchId)
activate Ctrl
Ctrl -> Phong: findByStatus("Đang hoạt động")
activate Phong
Phong --> Ctrl: List<Phong>
deactivate Phong
Ctrl --> CheckOut: List<Phong>
deactivate Ctrl
CheckOut --> NV: hiển thị danh sách phòng đang hoạt động

NV -> CheckOut: chọn phòng cần check-out
CheckOut -> Invoice: navigate(bookingId)
activate Invoice
CheckOut -> NV: hiển thị InvoicePanel

Invoice -> Ctrl: calculateInvoice(bookingId)
activate Ctrl
Ctrl -> HD: calculateTimeFee() + calculateServiceFee()
activate HD
HD --> Ctrl: HoaDon
deactivate HD
Ctrl --> Invoice: HoaDon
deactivate Ctrl
Invoice --> NV: hiển thị chi tiết hóa đơn

NV -> Invoice: nhập mã voucher (nếu có)
NV -> Invoice: chọn phương thức thanh toán
NV -> Invoice: click [Xác nhận thanh toán]
Invoice -> Ctrl: confirmPayment(invoiceId, paymentMethod, voucherCode)
activate Ctrl
Ctrl -> HD: updateStatus("Đã thanh toán")
Ctrl -> Phong: updateStatus("Trống")
Ctrl -> Ctrl: addPoints(clientId, points)
Ctrl --> Invoice: HoaDon updated
deactivate Ctrl
Invoice --> NV: "Check-out thành công! Tổng tiền: Xđ"
deactivate Invoice

NV -> Invoice: click [In hóa đơn]
Invoice -> NV: hiển thị hóa đơn in
deactivate CheckOut
@enduml
```

### Kịch bản phiên bản 3

**Kịch bản phiên bản 3 - Check-out**

1. Nhân viên lễ tân click chức năng "Check-out" trên giao diện ReceptionistHomePage.
2. Phương thức btnCheckOutClick() của lớp ReceptionistHomePage được gọi.
3. Phương thức btnCheckOutClick() gọi phương thức navigate() của lớp CheckOutPage.
4. Lớp CheckOutPage hiển thị danh sách phòng đang hoạt động.
5. Phương thức formLoad() của lớp CheckOutPage được gọi.
6. Phương thức formLoad() gọi phương thức getActiveRooms(branchId: int) của lớp BookingController.
7. Phương thức getActiveRooms() gọi phương thức findByStatus("Đang hoạt động") của lớp Entity Room.
8. Lớp Room trả kết quả danh sách phòng về cho phương thức getActiveRooms().
9. Phương thức getActiveRooms() trả kết quả về cho phương thức formLoad().
10. Lớp CheckOutPage hiển thị danh sách phòng đang sử dụng cho nhân viên.
11. Nhân viên hỏi khách hàng số phòng cần trả.
12. Khách hàng trả lời.
13. Nhân viên chọn phòng tương ứng trên danh sách.
14. Phương thức tblActiveRoomsClick(selectedRow: int) của lớp CheckOutPage được gọi.
15. Phương thức tblActiveRoomsClick() gọi phương thức navigate(room_receipt_ID) của lớp InvoicePanel.
16. Lớp InvoicePanel hiển thị chi tiết hóa đơn.
17. Phương thức formLoad(invoice: Room_receipt) của lớp InvoicePanel được gọi.
18. Phương thức formLoad() gọi phương thức calculateInvoice(room_receipt_ID: int) của lớp BookingController.
19. Phương thức calculateInvoice() gọi phương thức calculateTimeFee() + calculateServiceFee() của lớp Entity Room_receipt.
20. Lớp Room_receipt trả kết quả hóa đơn về cho phương thức calculateInvoice().
21. Phương thức calculateInvoice() trả Room_receipt về cho phương thức formLoad().
22. Lớp InvoicePanel hiển thị chi tiết tiền phòng, dịch vụ, thời gian sử dụng và tổng tiền.
23. Nhân viên thông báo tổng tiền cho khách hàng.
24. Khách hàng cung cấp mã ưu đãi (nếu có).
25. Nhân viên nhập mã và ấn áp dụng.
26. Phương thức btnApply() của lớp InvoicePanel được gọi.
27. Phương thức btnApply() gọi phương thức applyPromotion(room_receipt_ID: int) của lớp BookingController.
28. Phương thức applyPromotion() gọi phương thức applyVoucher() của lớp Entity Promotion.
29. Lớp Promotion trả kết quả giảm giá về cho phương thức applyPromotion().
30. Phương thức applyPromotion() trả kết quả về cho phương thức btnApply().
31. Lớp InvoicePanel cập nhật lại tổng tiền sau giảm giá.
32. Khách hàng đưa tiền mặt cho nhân viên.
33. Nhân viên chọn phương thức thanh toán và click nút xác nhận thanh toán.
34. Phương thức btnThanhToanClick() của lớp InvoicePanel được gọi.
35. Phương thức btnThanhToanClick() gọi phương thức confirmPayment(room_receipt_ID: int, paymentMethod: String, voucherCode: String) của lớp BookingController.
36. Phương thức confirmPayment() gọi phương thức updateStatus("Đã thanh toán") của lớp Entity Room_receipt.
37. Phương thức confirmPayment() gọi phương thức updateStatus("Trống") của lớp Entity Room.
38. Phương thức confirmPayment() gọi phương thức addPoints(base_score) của lớp Entity Customer.
39. Các lớp Entity trả kết quả lưu trữ về cho phương thức confirmPayment().
40. Phương thức confirmPayment() trả Room_receipt về cho phương thức btnThanhToanClick().
41. Lớp InvoicePanel hiển thị thông báo "Check-out thành công! Tổng tiền: [X]đ."
42. Nhân viên click nút in hóa đơn (để đưa cho khách hàng) và ấn hoàn tất.
43. Phương thức btnInHoaDonClick() của lớp InvoicePanel được gọi.
44. Phương thức btnInHoaDonClick() gọi phương thức showMessage() của lớp InvoicePanel.
45. Phương thức showMessage() gọi phương thức navigate() của lớp ReceptionistHomePage.
46. Hệ thống quay về giao diện chính ReceptionistHomePage.

**Ngoại lệ:**
- **Voucher không hợp lệ:** Phương thức applyPromotion() trả về lỗi. Lớp InvoicePanel hiển thị "Mã voucher không hợp lệ hoặc đã hết hạn."
- **Thanh toán chuyển khoản thất bại:** Phương thức confirmPayment() trả về lỗi. Lớp InvoicePanel hiển thị lỗi, yêu cầu chọn lại phương thức.

---

## 4.4. Chức năng "Huỷ phòng" — Thiết kế

### Biểu đồ tuần tự

<!-- PLACEHOLDER: Chèn ảnh tuần tự Huỷ phòng tại đây -->
<!-- File: output/diagrams/booking_seq_huyphong.png -->

```plantuml
@startuml
actor "Nhân viên lễ tân" as NV
participant "CancelBookingPage\n<<Boundary>>" as Cancel
participant "BookingController\n<<Control>>" as Ctrl
entity "Phong\n<<Entity>>" as Phong

NV -> Cancel: click "Quản lý đặt phòng"
activate Cancel
Cancel -> Ctrl: searchBooking(keyword)
activate Ctrl
Ctrl -> Ctrl: findByKeyword(keyword)
Ctrl --> Cancel: List<BookingResponse>
deactivate Ctrl
Cancel --> NV: hiển thị danh sách booking

NV -> Cancel: chọn booking cần hủy
NV -> Cancel: click [Hủy đặt phòng]
Cancel -> NV: hiển thị xác nhận "Bạn có chắc chắn?"
NV -> Cancel: click [Đồng ý]
Cancel -> Ctrl: cancelBooking(bookingId)
activate Ctrl
Ctrl -> Phong: updateStatus(roomId, "Trống")
activate Phong
Phong --> Ctrl: Phong updated
deactivate Phong
Ctrl -> Ctrl: updateBookingStatus("Đã hủy")
Ctrl --> Cancel: BookingResponse
deactivate Ctrl
Cancel --> NV: "Hủy đặt phòng thành công!"
deactivate Cancel
@enduml
```

### Kịch bản phiên bản 3

**Kịch bản phiên bản 3 - Huỷ phòng**

1. Nhân viên lễ tân click chức năng "Quản lý đặt phòng" trên giao diện ReceptionistHomePage.
2. Phương thức btnBookingManagementClick() của lớp ReceptionistHomePage được gọi.
3. Phương thức btnBookingManagementClick() gọi phương thức navigate() của lớp CancelBookingPage.
4. Lớp CancelBookingPage hiển thị form tìm kiếm booking.
5. Nhân viên hỏi khách hàng thông tin tra cứu (họ tên, số điện thoại hoặc mã phòng đã đặt).
6. Khách hàng trả lời.
7. Nhân viên nhập thông tin tìm kiếm và ấn nút tìm kiếm.
8. Phương thức btnSearchClick() của lớp CancelBookingPage được gọi.
9. Phương thức btnSearchClick() gọi phương thức searchBooking(keyword: String) của lớp BookingController.
10. Phương thức searchBooking() gọi phương thức findByKeyword(keyword) của lớp Entity Room.
11. Lớp Room trả kết quả danh sách booking về cho phương thức searchBooking().
12. Phương thức searchBooking() trả kết quả về cho phương thức btnSearchClick().
13. Lớp CancelBookingPage hiển thị danh sách các booking tương ứng cho nhân viên.
14. Nhân viên ấn chọn bản ghi booking cần hủy.
15. Phương thức tblBookingsClick(selectedRow: int) của lớp CancelBookingPage được gọi.
16. Lớp CancelBookingPage hiển thị thông tin chi tiết booking và nút [Hủy đặt phòng].
17. Nhân viên click [Hủy đặt phòng].
18. Lớp CancelBookingPage hiển thị xác nhận "Bạn có chắc chắn muốn hủy booking này?".
19. Nhân viên click [Đồng ý].
20. Phương thức btnCancelClick() của lớp CancelBookingPage được gọi.
21. Phương thức btnCancelClick() gọi phương thức cancelBooking(bookingId: int) của lớp BookingController.
22. Phương thức cancelBooking() gọi phương thức updateStatus(roomId, "Trống") của lớp Entity Room.
23. Lớp Room cập nhật trạng thái và trả kết quả về cho phương thức cancelBooking().
24. Phương thức cancelBooking() cập nhật trạng thái booking sang "Đã hủy" trong CSDL.
25. Phương thức cancelBooking() trả BookingResponse về cho phương thức btnCancelClick().
26. Lớp CancelBookingPage hiển thị thông báo "Hủy đặt phòng thành công."
27. Nhân viên ấn nút quay lại.
28. Phương thức showMessage() của lớp CancelBookingPage được gọi.
29. Phương thức showMessage() gọi phương thức navigate() của lớp ReceptionistHomePage.
30. Hệ thống quay về giao diện chính ReceptionistHomePage.

**Ngoại lệ:**
- **Không tìm thấy booking:** Phương thức searchBooking() trả về danh sách rỗng. Lớp CancelBookingPage hiển thị "Không tìm thấy booking phù hợp."
- **Booking đã quá thời gian hủy:** Phương thức cancelBooking() kiểm tra thời gian, trả về lỗi. Lớp CancelBookingPage hiển thị "Booking đã quá thời gian hủy."
