# Quản lý đặt & trả phòng

PHẠM TUẤN ANH - B23DCDT018 - D23CQCE01-B
PHA XÁC ĐỊNH YÊU CẦU
Bảng thuật ngữ
Bảng thuật ngữ dưới đây định nghĩa các khái niệm nghiệp vụ chính trong mô-đun quản lý đặt và trả phòng trong hệ thống quản lý chuỗi nhà hàng karaoke, giúp toàn nhóm hiểu thống nhất các thuật ngữ sẽ sử dụng
Mô hình nghiệp vụ bằng ngôn ngữ tự nhiên
2.1. Mục tiêu mô-đun
Thực hiện chức năng quản lý đặt phòng, huỷ phòng để tham gia vào xây dựng hệ thống phần mềm quản lý tập trung cho chuỗi nhà hàng karaoke.
2.2. Phạm vi mô-đun
Mô-đun sẽ bao phủ toàn bộ quy trình vận hành từ khi khách hàng đặt phòng đến khi thanh toán.
2.3. Ai có thể sử dụng mô-đun?
	Mô-đun sẽ phục vụ 2 nhóm người chính:
Khánh hàng là nhóm người sẽ tham gia vào các thao tác đặt phòng, huỷ phòng, thanh toán.
Nhân viên lễ tân là người trực tiếp tham gia vào tác đặt phòng, check-in/ check-out, tổng hợp hoá đơn và thu tiền của khách.
2.4. Người dùng có những chức năng gì?
	Khách hàng:
Đặt phòng trực tuyến hoặc đặt phòng tại chi nhánh.
Huỷ phòng trực tuyến hoặc huỷ phòng tại chi nhánh.
Check-in/ check-out
Thanh toán
	Nhân viên lễ tân:
Đặt phòng
Huỷ phòng
Check-in/ check-out
Tổng hợp hoá đơn
Áp dụng ưu đãi hội viên
Thu tiền
In hoá đơn
2.5. Mỗi chức năng hoạt động như thế nào?
Đặt phòng trực tuyến: Khách hàng đăng nhập vào hệ thống web/app → Khách hàng chọn chi nhánh →  Khách hàng xem danh sách phòng trống theo khung giờ mong muốn →  Khách hàng chọn phòng và thời gian → Khách hàng xác nhận đặt phòng → Hệ thống ghi nhận booking với trạng thái "Chờ nhận" trên hệ thống.
Đặt phòng tại chi nhánh: Khách hàng đến trực tiếp chi nhánh → Lễ tân kiểm tra phòng trống → Lễ tân chọn chi nhánh →  Lễ tân xem danh sách phòng trống theo khung giờ mong muốn → Lễ tân chọn phòng và thời gian → Lễ tân ghi nhận thông tin khách (hoặc tra cứu hội viên qua số điện thoại) → Lễ tân xác nhận đặt phòng với khách hàng → Lễ tân tạo booking với trạng thái “Chờ nhận” trên hệ thống.
Check-in: Khách hàng yêu cầu nhận phòng → Lễ tân kiểm tra thông tin khách hàng và phòng đặt → Lễ tân xác nhận đúng thông tin → Hệ thống chuyển trạng thái phòng được đặt từ “Chờ nhận” sang “Đang hoạt động”.
Check-out: Khách hàng yêu cầu trả phòng → Lễ tân chọn phòng trên hệ thống → Hệ thống tự động tính tiền phòng (giờ sử dụng × đơn giá) cộng tổng tiền order gọi món → Nếu khách là hội viên, lễ tân áp dụng ưu đãi hoặc voucher →  Hệ thống hiển thị tổng tiền →  Khách hàng thanh toán (tiền mặt/chuyển khoản) → Lễ tân in hóa đơn → Hệ thống đóng phòng → Hệ thống chuyển trạng thái về "Trống" → Hệ thống cộng điểm hội viên tự động.
Huỷ phòng trực tuyến: Khách hàng ấn nút Huỷ đặt phòng trên hệ thống → Hệ thống hỏi người dùng xác nhận chắc chắn huỷ → Hệ thống chuyển trạng thái “Chờ nhận” ở ghi nhận booking sang “Trống” → Lễ tân bấm xác nhận “Huỷ đặt phòng”.
Huỷ phòng tại chi nhánh: Khách hàng huỷ đặt phòng trực tiếp tại chi nhánh → Lễ tân chuyển trạng thái “chờ nhận” ở ghi nhận booking sang “huỷ đặt”. Lễ tân bấm xác nhận “huỷ đặt phòng” và không hoàn tiền cọc cho khách hàng.

2.6. Những thông tin/ đối tượng mà mô-đun cần xử lý
Mô-đun cần quản lý và xử lý các đối tượng thông tin chính sau:
Chi nhánh: Mã chi nhánh, tên, địa chỉ, số điện thoại.
Khách hàng: Mã khách hàng, họ tên, số điện thoại, địa chỉ, hạng hội viên (Thường, Bạc, Vàng), trạng thái tài khoản.
Nhân viên: Mã nhân viên, họ tên, vai trò, chi nhánh làm việc, trạng thái (đang làm/ đã nghỉ).
Hạng hội viên: Mã hạng, tên hạng, ngưỡng điểm tối thiểu, ưu đãi (% giảm giá, điểm thưởng nhận).
Phòng hát: Mã phòng, tên phòng, loại phòng, sức chứa, giá theo giờ, trạng thái, thuộc chi nhánh.
Khuyến mãi: Mã khuyến mãi, tên, loại (voucher/ giảm giá %), điều kiện áp dụng, thời gian hiệu lực.
Hoá đơn: Mã hoá đơn, liên kết đặt phòng, tiền phòng, thời gian sử dụng thực tế, tiền dịch vụ, phụ phí, giảm giá, tổng tiền, trạng thái thanh toán, phương thức thanh toán.
2.7. Quan hệ giữa các đối tượng
	Các đối tượng trong mô-đun có mối quan hệ chặt chẽ với nhau:
Một chi nhánh có nhiều phòng hát.
Một khách hàng thuộc một hạng hội viên.
Một hạng hội viên định nghĩa ngưỡng điểm và áp dụng cho nhiều khách hàng.
Một nhân viên thuộc một chi nhánh.
Một hoá đơn có thể áp dụng nhiều khuyến mãi.
Mô hình nghiệp vụ bằng UML
3.1. Danh sách Actor
3.2. Các Use Case cho từng Actor

3.3. Biểu đồ Use Case tổng quan của mô-đun	
	
3.4. Biểu đồ Use Case phân rã của mô-đun
Use case đặt phòng

Use case huỷ phòng

Use case check-in

Use case check-out

II. PHA PHÂN TÍCH
Mô hình hóa chức năng
1.1. Kịch bản “Đặt phòng tại chi nhánh”
1.2. Kịch bản "Check-in"
1.3. Kịch bản "Check-out"
1.4. Kịch bản "Huỷ phòng"

Mô hình hóa lớp
2.1. Mô tả module
“Trong mô-đun Đặt phòng và trả phòng, khách hàng có thể đặt phòng trực tuyến hoặc đặt phòng tại chi nhánh. Nếu khách hàng đặt phòng trực tuyến, khách hàng sẽ cần chọn chi nhánh muốn đặt, sau đó hệ thống sẽ hiển thị các phòng cùng các khung giờ còn trống. Sau khi khách hàng chọn được phòng cùng với khung giờ mong muốn, khách hàng sẽ bấm xác nhận đặt phòng. Ngay lập tức, hệ thống sẽ ghi nhận booking với trạng thái “Đang chờ”. Nếu khách hàng đặt phòng tại chi nhánh, nhân viên lễ tân sẽ đưa ra các phòng cùng với các khung giờ còn trống cho khách hàng chọn. Sau khi khách hàng chọn được phòng cùng với khung giờ mong muốn. Khách hàng sẽ xác nhận đặt phòng lại với nhân viên lễ tân. Nhân viên lễ tân sẽ thao tác trên hệ thống để ghi nhận booking với trạng thái “Đang chờ”. Khi khách hàng muốn nhận phòng, khách hàng sẽ cần check-in với nhân viên lễ tân. Sau khi trải nghiệm xong, khách hàng muốn trả phòng, khách hàng tiếp tục quay trở lại chỗ nhân viên lễ tân để làm thủ tục check-out. Nhân viên lễ tân sẽ tổng hợp lại hoá đơn, trừ đi ưu đãi của hạng hội viên và các khuyến mãi khác (nếu có). Khách hàng sẽ chọn phương thức thanh toán bằng tiền mặt hoặc chuyển khoản cho lễ tân. Lễ tân sẽ in chi tiết hoá đơn đưa lại cho khách hàng. Ngay lập tức, hệ thống sẽ ghi nhận giao dịch.”
2.2. Xác định lớp thực thể
	
=> Các lớp thực thể: Khách hàng (KhachHang), Chi nhánh (ChiNhanh), Phòng (Phong), Nhân viên (NhanVien), Hoá đơn (HoaDon) Chi tiết hoá đơn (ChiTietHoaDon), Hạng hội viên (HangHoiVien), Khuyến mãi (KhuyenMai).
2.3. Xác định lực lượng quan giữa các thực thể
Một chi nhánh có thể có nhiều phòng => ChiNhanh và Phong có quan hệ 1-n
Một chi nhánh có thể có nhiều nhân viên => ChiNhanh và NhanVien có quan hệ 1-n
Nhiều khách hàng có thể thuộc một hạng hội viên => KhachHang và HangHoiVien có quan hệ n-1.
Một khách hàng có thể có nhiều khuyến mãi => KhachHang và KhuyenMai có quan hệ 1-n.
Khách hàng có thể có nhiều hoá đơn => KhachHang và HoaDon có quan hệ 1-n.
Một phòng có thể xuất hiện nhiều hoá đơn => Phong và HoaDon có quan hệ 1-n.
Một khách hàng có thẻ đặt nhiều phòng => KhachHang và Phong có quan hệ 1-n.
Nhân viên có thể có nhiều hoá đơn => NhanVien và HoaDon có quan hệ 1-n.
Một hoá đơn có nhiều khuyến mãi, một khuyến mãi có thẻ áp dụng cho nhiều hoá đơn => HoaDon và KhuyenMai có quan hệ n-n.
Một hoá đơn có nhiều chi tiết hoá đơn => HoaDon và ChiTietHoaDon có quan hệ 1-n.
2.4. Xác định quan hệ đối tượng giữa các thực thể
Khách hàng sở hữu hoá đơn (Association)
Chi nhánh có nhiều phòng (Composition)
Chi nhánh quản lý nhân viên (Aggregation)
Một phòng có thể xuất hiện ở nhiều hoá đơn theo thời gian (Composition)
Một nhân viên xử lý nhiều hoá đơn (Association)
Hạng hội viên phân loại khách hàng (Aggregation)
HoaDon và KhuyenMai liên kết tạo ra ApDungKhuyenMai
ChiTietHoaDon là các thành phần cấu tạo nên HoaDon (Composition)
2.5. Biểu đồ lớp thực thể pha phân tích
	
Mô hình hóa tĩnh - Biểu đồ phân tích chức năng
3.1. Chức năng “Đặt phòng”
	Phân tích chi tiết chức năng “Đặt phòng” diễn ra như sau:
Sau khi đăng nhập thành công, hiển thị giao diện chính của nhân viên lễ tân → Đề xuất lớp ReceptionistHomeView, có nút đặt phòng.
Khi ấn nút đặt phòng, hiển thị giao diện tìm phòng trống → Đề xuất lớp SearchFreeRoomView, có các ô nhập thời gian check-in, nút tìm, danh sách kết quả.
Nhân viên nhập thời gian check-in, và ấn nút tìm kiếm → Hệ thống cần tìm phòng trống theo thời gian yêu cầu → Cần chức năng searchFreeRoom() của đối tượng Room.
Khi nhân viên ấn vào phòng trống, hệ thống hiện lên giao diện nhập thông tin khách hàng → Đề xuất lớp SearchClientView, có ô nhập tên, ô nhập số điện thoại, nút tìm kiếm.
Khi nhân viên ấn tìm kiếm → Hệ thống cần tìm thông tin khách hàng tương ứng trong cơ sở dữ liệu → Cần chức năng searchClient() của đối tượng Client.
Khi nhân viên ấn vào dòng chứa thông tin khách hàng tương ứng, giao diện hiển thị xác nhận thông tin đặt phòng → Đề xuất lớp ConfirmView, có phần hiển thị thông tin đặt phòng, và nút xác nhận.
Nhân viên ấn nút xác nhận → Hệ thống chuyển trạng thái phòng thành “Chờ nhận” → Cần chức năng changeStatus() của đối tượng Room.
Hệ thống lưu xong báo lại lớp ConfirmView, lớp ConfirmView báo thành công cho nhân viên → Nhân viên ấn nút OK → Hệ thống quay về lớp ReceptionistHomeView.

	 	 	
3.2. Chức năng “Huỷ phòng”
	Phân tích chi tiết chức năng “Hủy phòng” diễn ra như sau:
Từ giao diện chính của nhân viên lễ tân, nhân viên ấn chọn chức năng quản lý đặt phòng → Đề xuất lớp ReceptionistHomeView, có nút quản lý đặt phòng.
Hệ thống hiển thị giao diện tra cứu đặt phòng → Đề xuất lớp SearchBookingView, có các ô nhập thông tin tìm kiếm (tên khách hàng, số điện thoại, tên phòng), nút tìm kiếm và danh sách kết quả.
Nhân viên nhập thông tin cần tra cứu và ấn nút tìm kiếm → Hệ thống truy xuất thông tin khách hàng và thông tin phòng tương ứng trong cơ sở dữ liệu → Cần chức năng searchClient() của đối tượng Client và chức năng searchBooking() của đối tượng Room.
Khi nhân viên ấn chọn đúng thông tin phòng cần hủy đặt, hệ thống hiển thị giao diện yêu cầu xác nhận → Đề xuất lớp ConfirmCancelView, có phần hiển thị thông tin chi tiết đặt phòng, thông tin phòng và nút xác nhận hủy.
Nhân viên ấn xác nhận hủy phòng → Hệ thống cập nhật trạng thái phòng về mức “Trống” → Cần chức năng changeStatus() của đối tượng Room.
Hệ thống lưu xong báo lại cho lớp ConfirmCancelView, lớp ConfirmCancelView hiển thị thông báo thành công cho nhân viên → Nhân viên ấn nút quay lại (Back) → Hệ thống quay về lớp ReceptionistHomeView.

3.3. Chức năng “Check-in”
Phân tích chi tiết chức năng “Check-in” diễn ra như sau:
Nhân viên lễ tân click chức năng “Check-in” trên giao diện ReceptionistHomeView → Đề xuất lớp CheckInView, hiển thị danh sách các phòng đang ở trạng thái “Chờ nhận”. Để có danh sách này, hệ thống cần truy xuất dữ liệu thông qua hàm searchBooking() của đối tượng Room và thông tin khách hàng từ đối tượng Client.
Nhân viên chọn phòng cần check-in → Hệ thống hiển thị thông tin chi tiết → Đề xuất lớp ConfirmCheckInView, có phần hiển thị thông tin xác nhận đặt phòng, thông tin phòng và nút xác nhận check-in.
Nhân viên ấn nút xác nhận → Hệ thống chuyển trạng thái phòng từ “Chờ nhận” sang “Đang hoạt động” → Cần chức năng changeStatus() của đối tượng Room.
Đồng thời, hệ thống tạo hóa đơn và ghi nhận thời gian bắt đầu sử dụng → Cần chức năng startTimer() của đối tượng Room_receipt.
Hệ thống lưu xong báo lại cho lớp ConfirmCheckInView, lớp ConfirmCheckInView báo thành công cho nhân viên → Nhân viên ấn nút quay lại → Hệ thống quay về lớp ReceptionistHomeView.

3.4. Chức năng “Check-out”
Phân tích chi tiết chức năng “Check-out” diễn ra như sau:
Nhân viên lễ tân click chức năng “Check-out” trên giao diện chính ReceptionistHomeView → Đề xuất lớp CheckOutView, hiển thị danh sách các phòng đang hoạt động (dữ liệu truy xuất từ đối tượng Room).
Nhân viên chọn phòng cần check-out → Hệ thống tính toán tổng tiền → Cần chức năng CalculateTotalAmount() của đối tượng Room_receipt (kết hợp dữ liệu từ Room_receipt_detail).
Hệ thống chuyển sang giao diện hóa đơn → Đề xuất lớp InvoiceView, hiển thị chi tiết tiền phòng, dịch vụ, thời gian sử dụng và tổng tiền.
Hệ thống kiểm tra hạng thành viên của khách hàng → Cần chức năng checkMember() của đối tượng MemberRanking (thông qua liên kết với Client).
Nếu khách hàng có mã ưu đãi, nhân viên nhập mã và ấn áp dụng → Cần chức năng applyPromotion() của đối tượng Promotion.
Nhân viên xác nhận số tiền cuối cùng và chọn phương thức thanh toán → Chuyển sang giao diện thanh toán → Đề xuất lớp PaymentView để xử lý và in hóa đơn.
Thanh toán hoàn tất, hệ thống cập nhật trạng thái hóa đơn thành "Đã thanh toán" → Cần chức năng updateStatus() của đối tượng Room_receipt.
Hệ thống cập nhật trạng thái phòng về “Trống” → Cần chức năng changeStatus() của đối tượng Room.
Đồng thời, hệ thống cộng điểm tích lũy cho khách hàng (nếu là hội viên) → Cần chức năng addPoints() của đối tượng MemberRanking.
Hệ thống thông báo thành công, nhân viên ấn hoàn tất → Quay trở về ReceptionistHomeView.

Mô hình hóa động - Biểu đồ tuần tự
4.1. Chức năng “Đặt phòng”
Nhân viên click chức năng đặt phòng trên giao diện ReceptionistHomeView.
Lớp  ReceptionistHomeView gọi sang lớp SearchFreeRoomView.
Lớp SearchFreeRoomView hiển thị cho nhân viên.
Nhân viên hỏi khách hàng thời gian đặt phòng.
Khách hàng trả lời.
Nhân viên nhập thời gian đặt phòng mong muốn của khách vào ô thời gian và ấn nút tìm kiếm.
Lớp searchFreeRoomView gọi đến lớp Room để xử lý thông tin.
Lớp Room gọi hàm searchFreeRoom().
Lớp Room trả kết quả về cho searchFreeRoomView.
Lớp searchFreeRoomView hiển thị danh sách các phòng trống cho nhân viên.
Nhân viên ấn vào phòng trống.
Lớp searchFreeRoomView gọi sang lớp searchClientView.
Lớp searchClientView hiển thị.
Nhân viên hỏi khách hàng về thông tin khách hàng.
Khách hàng trả lời.
Nhân viên nhập thông tin khách hàng và ấn nút tìm kiếm.
Lớp searchClientView gọi đến lớp Client.
Lớp Client gọi hàm searchClient().
Lớp Client trả kết quả về cho lớp searchClientView.
Lớp searchClientView hiển thị thông tin khách hàng tương ứng.
Nhân viên chọn thông tin khách hàng tương ứng.
Lớp searchClientView gọi sang lớp ConfirmView.
Lớp ConfirmView hiển thị.
Nhân viên ấn confirm.
Lớp ConfirmView gọi đến lớp Room để xử lý.
Lớp Room gọi hàm changeStatus().
Lớp Room trả kết quả về lớp ConfirmView.
Lớp ConfirmView hiện thông báo.
Nhân viên ấn OK.
Lớp ConfirmView gọi lại về lớp ReceptionistHomeView.
Lớp ReceptionistHomeView hiển thị.
		
4.2. Chức năng “Huỷ phòng”
Nhân viên click chức năng quản lý đặt phòng trên giao diện ReceptionistHomeView.
Lớp ReceptionistHomeView gọi sang lớp SearchBookingView.
Lớp SearchBookingView hiển thị cho nhân viên.
Nhân viên hỏi khách hàng thông tin tra cứu (họ tên, số điện thoại hoặc mã phòng đã đặt).
Khách hàng trả lời.
Nhân viên nhập thông tin và ấn nút tìm kiếm.
Lớp SearchBookingView gọi đến lớp Client (để tra cứu khách) và lớp Room (để tra cứu phòng).
Lớp Client gọi hàm searchClient() và lớp Room gọi hàm searchBooking().
Lớp Client và lớp Room trả kết quả về cho SearchBookingView.
Lớp SearchBookingView hiển thị danh sách các booking tương ứng.
Nhân viên ấn chọn bản ghi booking cần hủy.
Lớp SearchBookingView gọi sang lớp ConfirmCancelView.
Lớp ConfirmCancelView hiển thị thông tin đặt phòng.
Nhân viên ấn xác nhận hủy.
Lớp ConfirmCancelView gọi đến lớp Room để xử lý.
Lớp Room gọi hàm changeStatus() (để cập nhật trạng thái về "Trống").
Lớp Room trả kết quả về lớp ConfirmCancelView.
Lớp ConfirmCancelView hiện thông báo thành công.
Nhân viên ấn nút quay lại.
Lớp ConfirmCancelView gọi lại về lớp ReceptionistHomeView.
Lớp ReceptionistHomeView hiển thị.


4.3. Chức năng “Check-in”
Nhân viên click chức năng "Check-in" trên giao diện ReceptionistHomeView.
Lớp ReceptionistHomeView gọi sang lớp CheckInView.
Lớp CheckInView gọi đến lớp Room (tìm phòng "Chờ nhận") và lớp Client (lấy thông tin khách hàng).
Lớp Room gọi hàm searchBooking(), lớp Client gọi hàm searchClient().
Lớp Room và lớp Client trả kết quả dữ liệu về cho CheckInView.
Lớp CheckInView hiển thị danh sách chờ nhận lên màn hình cho nhân viên.
Nhân viên hỏi khách hàng thông tin (tên hoặc số điện thoại) để đối chiếu.
Khách hàng trả lời.
Nhân viên ấn chọn bản ghi tương ứng cần check-in trên danh sách.
Lớp CheckInView gọi sang lớp ConfirmCheckInView.
Lớp ConfirmCheckInView hiển thị thông tin chi tiết của phòng và khách hàng.
Nhân viên ấn nút xác nhận check-in.
Lớp ConfirmCheckInView gọi đến lớp Room và lớp Room_receipt để xử lý.
Lớp Room gọi hàm changeStatus() (chuyển sang "Đang hoạt động").
Lớp Room_receipt gọi hàm startTimer() (ghi nhận thời gian bắt đầu sử dụng).
Lớp Room và Room_receipt trả kết quả lưu dữ liệu về lớp ConfirmCheckInView.
Lớp ConfirmCheckInView hiện thông báo thành công.
Nhân viên ấn nút quay lại.
Lớp ConfirmCheckInView gọi lại về lớp ReceptionistHomeView.
Lớp ReceptionistHomeView hiển thị.

4.4. Chức năng “Check-out”
Nhân viên click chức năng "Check-out" trên giao diện ReceptionistHomeView.
Lớp ReceptionistHomeView gọi sang lớp CheckOutView.
Lớp CheckOutView gọi đến lớp Room để lấy dữ liệu và hiển thị danh sách phòng "Đang hoạt động" cho nhân viên.
Nhân viên hỏi khách hàng số phòng cần trả.
Khách hàng trả lời.
Nhân viên chọn phòng tương ứng trên danh sách.
Lớp CheckOutView gọi sang lớp InvoiceView.
Lớp InvoiceView gọi hàm CalculateTotalAmount() của đối tượng Room_receipt (để tính tổng tiền).
Lớp InvoiceView gọi hàm checkMember() của đối tượng MemberRanking (để kiểm tra hạng thành viên).
Lớp Room_receipt và MemberRanking trả kết quả về InvoiceView.
Lớp InvoiceView hiển thị chi tiết hóa đơn.
Nhân viên thông báo tổng tiền cho khách hàng.
Khách hàng cung cấp mã ưu đãi (nếu có).
Nhân viên nhập mã và ấn áp dụng.
Lớp InvoiceView gọi hàm applyPromotion() của đối tượng Promotion.
Lớp Promotion trả kết quả về InvoiceView, giao diện cập nhật lại tổng tiền.
Khách hàng đưa tiền mặt cho nhân viên.
Nhân viên chọn phương thức thanh toán và click nút xác nhận thanh toán.
Lớp InvoiceView gọi sang lớp PaymentView.
Lớp PaymentView gọi hàm updateStatus() của lớp Room_receipt (cập nhật trạng thái "Đã thanh toán").
Lớp PaymentView gọi hàm changeStatus() của lớp Room (chuyển về trạng thái "Trống").
Lớp PaymentView gọi hàm addPoints() của lớp MemberRanking (cộng điểm tích lũy).
Các đối tượng thực thể trả kết quả lưu trữ về lớp PaymentView.
Lớp PaymentView hiển thị thông báo thanh toán thành công.
Nhân viên click nút in hóa đơn (để đưa cho khách hàng) và ấn hoàn tất.
Lớp PaymentView gọi lại về lớp ReceptionistHomeView.
Lớp ReceptionistHomeView hiển thị.

III. PHA THIẾT KẾ
Thiết kế lớp thực thể

Thiết kế CSDL

Thiết kế tĩnh
3.1. Thiết kế giao diện
Màn hình 1: ReceptionistHomePage — Giao diện chính lễ tân
+------------------------------------------------------------------+ |  [Logo]  Quan ly Karaoke ABC            [Nhan vien: Nguyen Van A]| +------------------------------------------------------------------+ |  Chi nhanh: Quan 1                    	Ngay: 30/05/2026   	| +------------------------------------------------------------------+ |                                                                  | |  +------------------+  +------------------+  +------------------+| |  |   DAT PHONG  	|  |   CHECK-IN   	|  |   CHECK-OUT  	|  | |  |   [Click de dat] |  |   [Click de C.I] |  |   [Click de C.O] |  | |  +------------------+  +------------------+  +------------------+  | |                                                                    | |  Danh sach booking hom nay:                                    	| |  +--------------------------------------------------------------+  | |  | maBK | khachHang  | phong  | gioDat	| trangThai     	|  | |  |------|------------|--------|-----------|-------------------|  | |  | BK001| Nguyen V.A | P.VIP1 | 14:00 	| Cho nhan      	|  | |  | BK002| Tran T.B   | P.Std3 | 15:00 	| Dang hoat dong	|  | |  | BK003| Le M.C 	| P.VIP2 | 16:00 	| Cho nhan      	|  | |  +--------------------------------------------------------------+  | |                                                                    | +------------------------------------------------------------------+
Màn hình 2: SearchFreeRoomForm — Tìm phòng trống
+------------------------------------------------------------------+ |  [< Quay lai]   Tim phong trong                              	| +------------------------------------------------------------------+ |                                                                    | |  Thoi gian dat:  [30/05/2026]  Tu: [14:00]  Den: [17:00]    	| |  Chi nhanh:  	[Quan 1   	v]                             	| |  Loai phong: 	[Tat ca    	v]                            	| |                     	                                           | |  [Tim phong trong]                                                 | |                                                                    | |  Ket qua: 3 phong trong                                        	| |  +--------------------------------------------------------------+  | |  | maPhong | loaiPhong  | sucChua | giaTheoGio | trangThai 	|  | |  |---------|------------|---------|------------|---------------|  | |  | P.VIP1  | Super VIP  | 15  	| 200000 	| Trong     	|  | |  | P.Std3  | Standard   | 8   	| 100000 	| Trong     	|  | |  | P.VIP2  | VIP        | 12  	| 150000 	| Trong     	|  | |  +--------------------------------------------------------------+  | |                                                                    | |  [Chon phong]                                                      | +------------------------------------------------------------------+
Màn hình 3: SearchClientForm — Tìm thông tin khách hàng
+------------------------------------------------------------------+ |  [< Quay lai]   Tim khach hang                               	| +------------------------------------------------------------------+ |                                                                    | |  Phong da chon: P.VIP1 (Super VIP, 200000/gio)               	| |  Thoi gian: 30/05/2026, 14:00 - 17:00                        	| |                                                                    | |  Thong tin khach hang:                                             | |  hoTen:    	[Nguyen Van An       	]                     	| |  soDienThoai:  [0912345678          	]                     	| |                                                                    | |  [Tim kiem]                                                        | |                                                                    | |  Ket qua:                                                          | |  +--------------------------------------------------------------+  | |  | hoTen      	| soDienThoai | hangHoiVien | diemTichLuy	|  | |  |----------------|-------------|-------------|----------------|  | |  | Nguyen Van An  | 0912345678  | Bac     	| 1250       	|  | |  +--------------------------------------------------------------+  | |                                                                    | |  Khach moi? [Dang ky nhanh]                                    	| +------------------------------------------------------------------+
Màn hình 4: ConfirmBookingModal — Xác nhận đặt phòng
+------------------------------------------------------------------+ |  [< Quay lai]   Xac nhan dat phong                            	| +------------------------------------------------------------------+ |                                                                    | |  +--------------------------------------------------------------+  | |  | THONG TIN DAT PHONG                                          |  | |  |----------------------------------------------------------------|  | |  | khachHang: 	Nguyen Van An (0912345678)                 	|  | |  | hangHoiVien:   Bac (giam 10%)                             	|  | |  | phong:     	P.VIP1 - Super VIP                         	|  | |  | chiNhanh:  	Quan 1                                          |  | |  | thoiGian:  	30/05/2026, 14:00 - 17:00 (3 gio)         	|  | |  | giaTheoGio:	200000                                     	|  | |  | duKien:    	600000                                     	|  | |  +--------------------------------------------------------------+  | |                   	                                             | |  [Xac nhan dat phong]	[Huy]                                	| +------------------------------------------------------------------+
Màn hình 5: CheckOutPage — Thanh toán check-out
+------------------------------------------------------------------+ |  [< Quay lai]   Check-out - Phong P.VIP1                      	| +------------------------------------------------------------------+ |                                                                    | |  +--------------------------------------------------------------+  | |  | HOA DON THANH TOAN                                           |  | |  |----------------------------------------------------------------|  | |  | khachHang:     Nguyen Van An (Bac - giam 10%)            	|  | |  | phong:     	P.VIP1                                     	|  | |  | thoiGian:  	14:05 - 16:45 (2h40p)                     	|  | |  |----------------------------------------------------------------|  | |  | tienPhong: 	200000 x 2.67h = 534000                   	|  | |  | tienDichVu:	2 lon bia + 1 dia trai cay = 250000       	|  | |  | tongCong:  	784000                                     	|  | |  | giamGia(10%):  -78400                                        |  | |  | THANH TOAN:	705600                                     	|  | |  +--------------------------------------------------------------+  | |                                                                    | |  maVoucher: [____________] [Ap dung]                           	| |                                                                    | |  phuongThucThanhToan: (o) Tien mat  ( ) Chuyen khoan          	| |                                                                    | |  [Xac nhan thanh toan]	[In hoa don]	[Huy]               	| +------------------------------------------------------------------+
Màn hình 6: CancelBookingPage — Quản lý đặt phòng (Huỷ)
+------------------------------------------------------------------+ |  [< Quay lai]   Quan ly dat phong                             	| +------------------------------------------------------------------+ |                                                                    | |  Tim kiem: [Ten khach / SDT / maBK___________] [Tim kiem]     	| |                                                                    | |  Ket qua:                                                          | |  +--------------------------------------------------------------+  | |  | maBK | khachHang  | phong  | gioDat	| trangThai     	|  | |  |------|------------|--------|-----------|-------------------|  | |  | BK001| Nguyen V.A | P.VIP1 | 14:00 	| Cho nhan      	|  | |  +--------------------------------------------------------------+  | |                                                                    | |  +--------------------------------------------------------------+  | |  | Chi tiet booking BK001           	                        |  | |  |----------------------------------------------------------------|  | |  | khachHang: 	Nguyen Van An (0912345678)                 	|  | |  | phong:     	P.VIP1 - Super VIP                         	|  | |  | thoiGian:  	30/05/2026, 14:00 - 17:00                 	|  | |  | tienCoc:   	200000                                     	|  | |  +--------------------------------------------------------------+  | |                                                                    | |  [Huy dat phong]          	[Quay lai]                      	| +------------------------------------------------------------------+
Màn hình 7: CheckInPage — Check-in phòng
+------------------------------------------------------------------+ |  [< Quay lai]   Check-in                                      	| +------------------------------------------------------------------+ |                                                                    | |  Danh sach booking "Cho nhan" hom nay:                         	| |  +--------------------------------------------------------------+  | |  | maBK | khachHang  | phong  | gioDat	| trangThai     	|  | |  |------|------------|--------|-----------|-------------------|  | |  | BK001| Nguyen V.A | P.VIP1 | 14:00 	| Cho nhan      	|  | |  | BK003| Le M.C 	| P.VIP2 | 16:00 	| Cho nhan      	|  | |  +--------------------------------------------------------------+  | |                                                                    | |  +--------------------------------------------------------------+  | |  | Chi tiet booking BK001                                   	|  | |  |----------------------------------------------------------------|  | |  | khachHang: 	Nguyen Van An (0912345678)                 	|  | |  | phong:     	P.VIP1 - Super VIP                         	|  | |  | gioDat:    	14:00 - 17:00                              	|  | |  +--------------------------------------------------------------+  | |                                                                    | |  [Xac nhan Check-in]       	[Huy booking]                  	| +------------------------------------------------------------------+
3.2. Thiết kế mô hình MVC
Mô hình MVC được thiết kế theo kiến trúc BCE (Boundary – Control – Entity) với 3 tầng:
 Boundary (Giao diện): React components xử lý giao diện người dùng.
Control (Điều khiển): Spring Boot Controllers xử lý nghiệp vụ.
Entity (Thực thể): JPA Entities biểu diễn dữ liệu lưu trữ.
a) Chức năng Đặt phòng
1. Tầng giao diện (Boundary)

2. Tầng điều khiển (Control)
a) Tìm phòng trống => searchFreeRoom()
 Input: thời gian bắt đầu, thời gian kết thúc, mã chi nhánh.
Output: danh sách phòng trống.
Ứng viên tham số vào:
 searchFreeRoom(startTime: Date, endTime: Date, branchId: int) → chọn (gom nhóm tham số)
 searchFreeRoom(startTime: Date, endTime: Date, branchId: int, roomType: String) → chọn (thêm filter loại phòng)
 Ứng viên tham số ra:
searchFreeRoom(): void → loại (cần trả về danh sách)
searchFreeRoom(): List<Room> → chọn (trả về danh sách phòng)
b) Tìm khách hàng => searchClient()
 Input: tên hoặc số điện thoại
Output: danh sách khách hàng khớp
Ứng viên tham số vào:
searchClient(keyword: String) → chọn (tìm theo cả tên và SĐT)
Ứng viên tham số ra:
searchClient(): List<Client> → chọn
c) Thay đổi trạng thái phòng => changeStatus()
 Input: mã phòng, trạng thái mới.
 Output: đối tượng phòng đã cập nhật.
Ứng viên tham số vào:
changeStatus(roomID: int, status: String) → chọn
 Ứng viên tham số ra:
changeStatus(): Room → chọn
3. Tầng thực thể (Entity)
b) Chức năng Check-in
1. Tầng giao diện (Boundary)
2. Tầng điều khiển (Control)
a) Lấy danh sách booking chờ => getPendingBookings()
Input: mã chi nhánh, ngày
Output: danh sách booking trạng thái "Chờ nhận"
Ứng viên tham số vào:
 getPendingBookings(branchId: int, date: Date) → chọn
 Ứng viên tham số ra:
getPendingBookings(): List<BookingResponse> → chọn
b) Xác nhận check-in => checkIn()
Input: mã booking
Output: booking đã cập nhật
Ứng viên tham số vào:
checkIn(bookingId: int) → chọn
Ứng viên tham số ra:
checkIn(): BookingResponse → chọn
3. Tầng thực thể (Entity)
c) Chức năng Check-out
1. Tầng giao diện (Boundary)
2. Tầng điều khiển (Control)
a) Lấy danh sách phòng đang hoạt động => getActiveRooms()
Input: mã chi nhánh
 Output: danh sách phòng trạng thái "Đang hoạt động"
Ứng viên tham số vào:
getActiveRooms(branchID: int) → chọn
Ứng viên tham số ra:
getActiveRooms(): List<Room> → chọn
b) Tính tiền hóa đơn => calculateInvoice()
 Input: mã booking
 Output: chi tiết hóa đơn (tiền phòng, tiền dịch vụ, giảm giá, tổng)
Ứng viên tham số vào:
calculateInvoice(bookingId: int) → chọn
Ứng viên tham số ra:
CalculateTotalAmount(): Room_receipt → chọn
c) Xác nhận thanh toán => confirmPayment()
Input: mã hóa đơn, phương thức thanh toán, mã khuyến mãi (nếu có)
Output: hóa đơn đã thanh toán
Ứng viên tham số vào:
confirmPayment(Room_receip_ID: int, payment_method: String, promotion_ID: String) → chọn
Ứng viên tham số ra:
 confirmPayment(): Room_receipt → chọn
3. Tầng thực thể (Entity)
d) Chức năng Huỷ phòng
1. Tầng giao diện (Boundary)
2. Tầng điều khiển (Control)
a) Tìm booking => searchBooking()
 Input: tên khách, SĐT, hoặc mã booking.
 Output: danh sách booking khớp.
Ứng viên tham số vào:
searchBooking(keyword: String) → chọn
Ứng viên tham số ra:
 searchBooking(): List<BookingResponse> → chọn
b) Hủy booking => cancelBooking()
Input: mã booking
Output: booking đã hủy
Ứng viên tham số vào:
cancelBooking(bookingId: int) → chọn
 Ứng viên tham số ra:
cancelBooking(): BookingResponse → chọn
3. Tầng thực thể (Entity)

3.3. Sơ đồ lớp thiết kế
	
Thiết kế động
4.1. Chức năng quản lý
IV. PHA CÀI ĐẶT VÀ KIỂM THỬ
Kiểm thử chức năng
1.1. Lập kế hoạch test
1.2. Các test case cho từng có chức năng
