**## 4.1. Chức năng “Đặt phòng”

* Nhân viên click chức năng đặt phòng trên giao diện ReceptionistHomeView.
* Lớp  ReceptionistHomeView gọi sang lớp SearchFreeRoomView.
* Lớp SearchFreeRoomView hiển thị cho nhân viên.
* Nhân viên hỏi khách hàng thời gian đặt phòng.
* Khách hàng trả lời.
* Nhân viên nhập thời gian đặt phòng mong muốn của khách vào ô thời gian và ấn nút tìm kiếm.
* Lớp searchFreeRoomView gọi đến lớp Room để xử lý thông tin.
* Lớp Room gọi hàm searchFreeRoom().
* Lớp Room trả kết quả về cho searchFreeRoomView.
* Lớp searchFreeRoomView hiển thị danh sách các phòng trống cho nhân viên.
* Nhân viên ấn vào phòng trống.
* Lớp searchFreeRoomView gọi sang lớp searchClientView.
* Lớp searchClientView hiển thị.
* Nhân viên hỏi khách hàng về thông tin khách hàng.
* Khách hàng trả lời.
* Nhân viên nhập thông tin khách hàng và ấn nút tìm kiếm.
* Lớp searchClientView gọi đến lớp Client.
* Lớp Client gọi hàm searchClient().
* Lớp Client trả kết quả về cho lớp searchClientView.
* Lớp searchClientView hiển thị thông tin khách hàng tương ứng.
* Nhân viên chọn thông tin khách hàng tương ứng.
* Lớp searchClientView gọi sang lớp ConfirmView.
* Lớp ConfirmView hiển thị.
* Nhân viên ấn confirm.
* Lớp ConfirmView gọi đến lớp Room để xử lý.
* Lớp Room gọi hàm changeStatus().
* Lớp Room trả kết quả về lớp ConfirmView.
* Lớp ConfirmView hiện thông báo.
* Nhân viên ấn OK.
* Lớp ConfirmView gọi lại về lớp ReceptionistHomeView.
* Lớp ReceptionistHomeView hiển thị.

**	**	![]()

## 4.2. Chức năng “Huỷ phòng”

* Nhân viên click chức năng quản lý đặt phòng trên giao diện ReceptionistHomeView.
* Lớp ReceptionistHomeView gọi sang lớp SearchBookingView.
* Lớp SearchBookingView hiển thị cho nhân viên.
* Nhân viên hỏi khách hàng thông tin tra cứu (họ tên, số điện thoại hoặc mã phòng đã đặt).
* Khách hàng trả lời.
* Nhân viên nhập thông tin và ấn nút tìm kiếm.
* Lớp SearchBookingView gọi đến lớp Client (để tra cứu khách) và lớp Room (để tra cứu phòng).
* Lớp Client gọi hàm searchClient() và lớp Room gọi hàm searchBooking().
* Lớp Client và lớp Room trả kết quả về cho SearchBookingView.
* Lớp SearchBookingView hiển thị danh sách các booking tương ứng.
* Nhân viên ấn chọn bản ghi booking cần hủy.
* Lớp SearchBookingView gọi sang lớp ConfirmCancelView.
* Lớp ConfirmCancelView hiển thị thông tin đặt phòng.
* Nhân viên ấn xác nhận hủy.
* Lớp ConfirmCancelView gọi đến lớp Room để xử lý.
* Lớp Room gọi hàm changeStatus() (để cập nhật trạng thái về "Trống").
* Lớp Room trả kết quả về lớp ConfirmCancelView.
* Lớp ConfirmCancelView hiện thông báo thành công.
* Nhân viên ấn nút quay lại.
* Lớp ConfirmCancelView gọi lại về lớp ReceptionistHomeView.
* Lớp ReceptionistHomeView hiển thị.

## 4.3. Chức năng “Check-in”

* Nhân viên click chức năng "Check-in" trên giao diện ReceptionistHomeView.
* Lớp ReceptionistHomeView gọi sang lớp CheckInView.
* Lớp CheckInView gọi đến lớp Room (để lấy dữ liệu) và hiển thị danh sách phòng "Chờ nhận" cho nhân viên.
* Nhân viên hỏi khách hàng thông tin (tên hoặc mã đặt phòng) để đối chiếu.
* Khách hàng trả lời.
* Nhân viên ấn chọn booking tương ứng cần check-in trên danh sách.
* Lớp CheckInView gọi sang lớp ConfirmCheckInView.
* Lớp ConfirmCheckInView hiển thị thông tin chi tiết của phòng và khách hàng.
* Nhân viên ấn nút xác nhận check-in.
* Lớp ConfirmCheckInView gọi đến lớp Room và lớp Room_receipt để xử lý.
* Lớp Room gọi hàm changeStatus() (chuyển sang Đang hoạt động).
* Lớp Room_receipt gọi hàm startTimer() (ghi nhận thời gian bắt đầu).
* Lớp Room và Room_receipt trả kết quả lưu dữ liệu về lớp ConfirmCheckInView.
* Lớp ConfirmCheckInView hiện thông báo thành công.
* Nhân viên ấn nút quay lại.
* Lớp ConfirmCheckInView gọi lại về lớp ReceptionistHomeView.
* Lớp ReceptionistHomeView hiển thị.

## 4.4. Chức năng “Check-out”

* Nhân viên click chức năng "Check-out" trên giao diện ReceptionistHomeView.
* Lớp ReceptionistHomeView gọi sang lớp CheckOutView.
* Lớp CheckOutView gọi đến lớp Room để lấy dữ liệu và hiển thị danh sách phòng "Đang hoạt động" cho nhân viên.
* Nhân viên hỏi khách hàng số phòng cần trả.
* Khách hàng trả lời.
* Nhân viên chọn phòng tương ứng trên danh sách.
* Lớp CheckOutView gọi sang lớp InvoiceView.
* Lớp InvoiceView gọi hàm CalculateTotalAmount() của đối tượng Room_receipt (để tính tổng tiền).
* Lớp InvoiceView gọi hàm checkMember() của đối tượng MemberRanking (để kiểm tra hạng thành viên).
* Lớp Room_receipt và MemberRanking trả kết quả về InvoiceView.
* Lớp InvoiceView hiển thị chi tiết hóa đơn.
* Nhân viên thông báo tổng tiền cho khách hàng.
* Khách hàng cung cấp mã ưu đãi (nếu có).
* Nhân viên nhập mã và ấn áp dụng.
* Lớp InvoiceView gọi hàm applyPromotion() của đối tượng Promotion.
* Lớp Promotion trả kết quả về InvoiceView, giao diện cập nhật lại tổng tiền.
* Khách hàng đưa tiền mặt cho nhân viên.
* Nhân viên chọn phương thức thanh toán và click nút xác nhận thanh toán.
* Lớp InvoiceView gọi sang lớp PaymentView.
* Lớp PaymentView gọi hàm updateStatus() của lớp Room_receipt (cập nhật trạng thái "Đã thanh toán").
* Lớp PaymentView gọi hàm changeStatus() của lớp Room (chuyển về trạng thái "Trống").
* Lớp PaymentView gọi hàm addPoints() của lớp MemberRanking (cộng điểm tích lũy).
* Các đối tượng thực thể trả kết quả lưu trữ về lớp PaymentView.
* Lớp PaymentView hiển thị thông báo thanh toán thành công.
* Nhân viên click nút in hóa đơn (để đưa cho khách hàng) và ấn hoàn tất.
* Lớp PaymentView gọi lại về lớp ReceptionistHomeView.
* Lớp ReceptionistHomeView hiển thị.

**
