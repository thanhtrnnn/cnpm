## 4.1. Chức năng "Đặt phòng" — Thiết kế

### Biểu đồ tuần tự

<!-- PLACEHOLDER: Chèn ảnh tuần tự Đặt phòng tại đây -->
<!-- File: output/diagrams/booking_seq_datphong.png -->

```plantuml
@startuml
skinparam shadowing false
skinparam SequenceMessageAlign left
skinparam SequenceArrowThickness 2
skinparam SequenceLifeLineBackgroundColor #7AD2FF
skinparam ParticipantBackgroundColor #7AD2FF
skinparam ParticipantBorderColor black
skinparam BoundaryBackgroundColor #7AD2FF
skinparam BoundaryBorderColor black
skinparam ControlBackgroundColor #7AD2FF
skinparam ControlBorderColor black
skinparam EntityBackgroundColor #7AD2FF
skinparam EntityBorderColor black

title Dat phong – Tuần tự Thiết kế (React MVC)

actor "Nhan vien le tan" as NV
boundary "ReceptionistHomePage" as Home
boundary "SearchFreeRoomForm" as SRF
control "BookingController" as Ctrl
boundary "SearchClientForm" as SCF
boundary "ConfirmBookingModal" as CBM
entity "Room" as Room
entity "Client" as Cust
entity "Room_receipt" as RR

NV -> Home : 1: click "Dat phong"
activate Home
Home -> Home : 2: btnDatPhongClick()
Home -> SRF : 3: navigate()
activate SRF
SRF --> NV : 4: hien thi SearchFreeRoomForm
deactivate SRF

NV -> SRF : 5: nhap startTime, endTime, branchId
activate SRF
NV -> SRF : 6: click [Tim phong trong]
SRF -> SRF : 7: btnSearchClick()
SRF -> Ctrl : 8: searchFreeRoom(startTime, endTime, branchId)
activate Ctrl
Ctrl -> Room : 9: findByTimeAndBranch(startTime, endTime, branchId)
activate Room
Room --> Ctrl : 10: List<Room>
deactivate Room
Ctrl --> SRF : 11: List<Room>
deactivate Ctrl
SRF --> NV : 12: hien thi danh sach phong trong
deactivate SRF

NV -> SRF : 13: chon phong (roomId)
activate SRF
SRF -> SRF : 14: tblRoomsClick(selectedRow)
SRF -> SCF : 15: navigate(roomId)
activate SCF
SCF --> NV : 16: hien thi SearchClientForm
deactivate SCF

NV -> SCF : 17: nhap keyword (ten/SDT)
activate SCF
NV -> SCF : 18: click [Tim kiem]
SCF -> SCF : 19: btnSearchClick()
SCF -> Ctrl : 20: searchClient(keyword)
activate Ctrl
Ctrl -> Cust : 21: findByKeyword(keyword)
activate Cust
Cust --> Ctrl : 22: List<Client>
deactivate Cust
Ctrl --> SCF : 23: List<Client>
deactivate Ctrl
SCF --> NV : 24: hien thi danh sach khach hang
deactivate SCF

NV -> SCF : 25: chon khach hang (clientId)
activate SCF
SCF -> SCF : 26: tblClientsClick(selectedRow)
SCF -> CBM : 27: navigate(roomId, clientId, timeRange)
activate CBM
CBM --> NV : 28: hien thi ConfirmBookingModal
deactivate CBM

NV -> CBM : 29: click [Xac nhan dat phong]
activate CBM
CBM -> CBM : 30: btnConfirmClick()
CBM -> Ctrl : 31: createBooking(clientId, roomId, startTime, endTime, staffId)
activate Ctrl
Ctrl -> RR : 32: updateStatus(roomId, "Cho nhan")
activate RR
RR --> Ctrl : 33: Room_receipt updated
deactivate RR
Ctrl -> Ctrl : 34: saveBooking()
Ctrl --> CBM : 35: BookingResponse
deactivate Ctrl
CBM --> NV : 36: showMessage("Dat phong thanh cong!")
deactivate CBM

NV -> CBM : 37: click [OK]
activate CBM
CBM -> CBM : 38: showMessage()
CBM -> Home : 39: navigate()
deactivate CBM
deactivate Home
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
24. Phương thức searchClient() gọi phương thức findByKeyword(keyword) của lớp Entity Client.
25. Lớp Client trả kết quả danh sách khách hàng về cho phương thức searchClient().
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
skinparam shadowing false
skinparam SequenceMessageAlign left
skinparam SequenceArrowThickness 2
skinparam SequenceLifeLineBackgroundColor #7AD2FF
skinparam ParticipantBackgroundColor #7AD2FF
skinparam ParticipantBorderColor black
skinparam BoundaryBackgroundColor #7AD2FF
skinparam BoundaryBorderColor black
skinparam ControlBackgroundColor #7AD2FF
skinparam ControlBorderColor black
skinparam EntityBackgroundColor #7AD2FF
skinparam EntityBorderColor black

title Check-in – Tuần tự Thiết kế (React MVC)

actor "Nhan vien le tan" as NV
boundary "ReceptionistHomePage" as Home
boundary "CheckInPage" as CIP
control "BookingController" as Ctrl
entity "Room" as Room
entity "Room_receipt" as RR

NV -> Home : 1: click "Check-in"
activate Home
Home -> Home : 2: btnCheckInClick()
Home -> CIP : 3: navigate()
activate CIP
CIP -> CIP : 4: formLoad()
CIP -> Ctrl : 5: getPendingBookings(branchId, today)
activate Ctrl
Ctrl -> Room : 6: findByStatus("Cho nhan")
activate Room
Room --> Ctrl : 7: List<Room>
deactivate Room
Ctrl --> CIP : 8: List<BookingResponse>
deactivate Ctrl
CIP --> NV : 9: hien thi danh sach booking cho
deactivate CIP

NV -> CIP : 10: chon booking can check-in
activate CIP
NV -> CIP : 11: click [Xac nhan Check-in]
CIP -> CIP : 12: tblPendingBookingsClick(selectedRow)
CIP -> Ctrl : 13: checkIn(bookingId)
activate Ctrl
Ctrl -> Room : 14: updateStatus(roomId, "Dang hoat dong")
activate Room
Room --> Ctrl : 15: Room updated
deactivate Room
Ctrl -> RR : 16: setStartTime(now)
activate RR
RR --> Ctrl : 17: Room_receipt updated
deactivate RR
Ctrl --> CIP : 18: BookingResponse
deactivate Ctrl
CIP --> NV : 19: showMessage("Check-in thanh cong!")
deactivate CIP

NV -> CIP : 20: click [OK]
activate CIP
CIP -> CIP : 21: showMessage()
CIP -> Home : 22: navigate()
deactivate CIP
deactivate Home
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
skinparam shadowing false
skinparam SequenceMessageAlign left
skinparam SequenceArrowThickness 2
skinparam SequenceLifeLineBackgroundColor #7AD2FF
skinparam ParticipantBackgroundColor #7AD2FF
skinparam ParticipantBorderColor black
skinparam BoundaryBackgroundColor #7AD2FF
skinparam BoundaryBorderColor black
skinparam ControlBackgroundColor #7AD2FF
skinparam ControlBorderColor black
skinparam EntityBackgroundColor #7AD2FF
skinparam EntityBorderColor black

title Check-out – Tuần tự Thiết kế (React MVC)

actor "Nhan vien le tan" as NV
boundary "ReceptionistHomePage" as Home
boundary "CheckOutPage" as COP
boundary "InvoicePanel" as IP
control "BookingController" as Ctrl
entity "Room" as Room
entity "Room_receipt" as RR
entity "Client" as Cust
entity "Promotion" as Promo

NV -> Home : 1: click "Check-out"
activate Home
Home -> Home : 2: btnCheckOutClick()
Home -> COP : 3: navigate()
activate COP
COP -> COP : 4: formLoad()
COP -> Ctrl : 5: getActiveRooms(branchId)
activate Ctrl
Ctrl -> Room : 6: findByStatus("Dang hoat dong")
activate Room
Room --> Ctrl : 7: List<Room>
deactivate Room
Ctrl --> COP : 8: List<Room>
deactivate Ctrl
COP --> NV : 9: hien thi danh sach phong dang hoat dong
deactivate COP

NV -> COP : 10: chon phong can check-out
activate COP
COP -> COP : 11: tblActiveRoomsClick(selectedRow)
COP -> IP : 12: navigate(room_receipt_ID)
activate IP
IP -> IP : 13: formLoad(invoice)
IP -> Ctrl : 14: calculateInvoice(room_receipt_ID)
activate Ctrl
Ctrl -> RR : 15: calculateTimeFee() + calculateServiceFee()
activate RR
RR --> Ctrl : 16: Room_receipt
deactivate RR
Ctrl --> IP : 17: Room_receipt
deactivate Ctrl
IP --> NV : 18: hien thi chi tiet hoa don
deactivate IP

NV -> IP : 19: nhap ma voucher (neu co)
activate IP
NV -> IP : 20: click [Ap dung]
IP -> IP : 21: btnApply()
IP -> Ctrl : 22: applyPromotion(room_receipt_ID)
activate Ctrl
Ctrl -> Promo : 23: applyVoucher()
activate Promo
Promo --> Ctrl : 24: discount
deactivate Promo
Ctrl --> IP : 25: discount
deactivate Ctrl
IP --> NV : 26: cap nhat tong tien sau giam gia
deactivate IP

NV -> IP : 27: chon phuong thuc thanh toan
activate IP
NV -> IP : 28: click [Xac nhan thanh toan]
IP -> IP : 29: btnThanhToanClick()
IP -> Ctrl : 30: confirmPayment(room_receipt_ID, paymentMethod, voucherCode)
activate Ctrl
Ctrl -> RR : 31: updateStatus("Da thanh toan")
activate RR
RR --> Ctrl : 32: Room_receipt updated
deactivate RR
Ctrl -> Room : 33: updateStatus("Trong")
activate Room
Room --> Ctrl : 34: Room updated
deactivate Room
Ctrl -> Cust : 35: addPoints(base_score)
activate Cust
Cust --> Ctrl : 36: Client updated
deactivate Cust
Ctrl --> IP : 37: Room_receipt
deactivate Ctrl
IP --> NV : 38: showMessage("Check-out thanh cong!")
deactivate IP

NV -> IP : 39: click [In hoa don]
activate IP
IP -> IP : 40: btnInHoaDonClick()
IP -> IP : 41: showMessage()
IP -> Home : 42: navigate()
deactivate IP
deactivate Home
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
38. Phương thức confirmPayment() gọi phương thức addPoints(base_score) của lớp Entity Client.
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
skinparam shadowing false
skinparam SequenceMessageAlign left
skinparam SequenceArrowThickness 2
skinparam SequenceLifeLineBackgroundColor #7AD2FF
skinparam ParticipantBackgroundColor #7AD2FF
skinparam ParticipantBorderColor black
skinparam BoundaryBackgroundColor #7AD2FF
skinparam BoundaryBorderColor black
skinparam ControlBackgroundColor #7AD2FF
skinparam ControlBorderColor black
skinparam EntityBackgroundColor #7AD2FF
skinparam EntityBorderColor black

title Huy phong – Tuần tự Thiết kế (React MVC)

actor "Nhan vien le tan" as NV
boundary "ReceptionistHomePage" as Home
boundary "CancelBookingPage" as CBP
control "BookingController" as Ctrl
entity "Room" as Room

NV -> Home : 1: click "Quan ly dat phong"
activate Home
Home -> Home : 2: btnBookingManagementClick()
Home -> CBP : 3: navigate()
activate CBP
CBP --> NV : 4: hien thi form tim kiem booking
deactivate CBP

NV -> CBP : 5: nhap keyword (ten, SDT, ma booking)
activate CBP
NV -> CBP : 6: click [Tim kiem]
CBP -> CBP : 7: btnSearchClick()
CBP -> Ctrl : 8: searchBooking(keyword)
activate Ctrl
Ctrl -> Room : 9: findByKeyword(keyword)
activate Room
Room --> Ctrl : 10: List<Room>
deactivate Room
Ctrl --> CBP : 11: List<BookingResponse>
deactivate Ctrl
CBP --> NV : 12: hien thi danh sach booking
deactivate CBP

NV -> CBP : 13: chon booking can huy
activate CBP
CBP -> CBP : 14: tblBookingsClick(selectedRow)
CBP --> NV : 15: hien thi chi tiet booking + nut [Huy]
deactivate CBP

NV -> CBP : 16: click [Huy dat phong]
activate CBP
CBP --> NV : 17: hien thi xac nhan "Ban co chac chan?"
deactivate CBP

NV -> CBP : 18: click [Dong y]
activate CBP
CBP -> CBP : 19: btnCancelClick()
CBP -> Ctrl : 20: cancelBooking(bookingId)
activate Ctrl
Ctrl -> Room : 21: updateStatus(roomId, "Trong")
activate Room
Room --> Ctrl : 22: Room updated
deactivate Room
Ctrl -> Ctrl : 23: updateBookingStatus("Da huy")
Ctrl --> CBP : 24: BookingResponse
deactivate Ctrl
CBP --> NV : 25: showMessage("Huy dat phong thanh cong!")
deactivate CBP

NV -> CBP : 26: click [Quay lai]
activate CBP
CBP -> CBP : 27: showMessage()
CBP -> Home : 28: navigate()
deactivate CBP
deactivate Home
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
