# Quản lý đặt & trả phòng




MỤC LỤC

PHA XÁC ĐỊNH YÊU CẦU
Mô hình nghiệp vụ bằng UML
1.1. Danh sách Actor
1.2. Các Use Case cho từng Actor
1.3. Biểu đồ Use Case tổng quan của mô-đun	

1.4. Biểu đồ Use Case phân rã của mô-đun
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
Lớp SearchBookingView gọi đến lớp Client (để tra cứu khách).
Lớp Client gọi hàm searchClient().
Lớp Client trả kết quả về cho SearchBookingView.
Lớp SearchBookingView gọi đến lớp Room (để tra cứu phòng).
Lớp Room gọi hàm searchBooking().
Lớp Room trả kết quả về cho SearchBookingView.
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
Lớp CheckInView gọi đến lớp Room (tìm phòng "Chờ nhận").
Lớp Room gọi hàm searchBooking().
Lớp Room trả kết quả dữ liệu về cho CheckInView.
Lớp CheckInView gọi đến lớp Client (lấy thông tin khách hàng).
Lớp Client gọi hàm searchClient().
Lớp Client trả kết quả dữ liệu về cho CheckInView.
Lớp CheckInView hiển thị danh sách chờ nhận lên màn hình cho nhân viên.
Nhân viên hỏi khách hàng thông tin (tên hoặc số điện thoại) để đối chiếu.
Khách hàng trả lời.
Nhân viên ấn chọn bản ghi tương ứng cần check-in trên danh sách.
Lớp CheckInView gọi sang lớp ConfirmCheckInView.
Lớp ConfirmCheckInView hiển thị thông tin chi tiết của phòng và khách hàng.
Nhân viên ấn nút xác nhận check-in.
Lớp ConfirmCheckInView gọi đến lớp Room để xử lý.
Lớp Room gọi hàm changeStatus() (chuyển sang "Đang hoạt động").
Lớp Room trả kết quả lưu dữ liệu về lớp ConfirmCheckInView.
Lớp ConfirmCheckInView gọi đến lớp Room_receipt để xử lý.
Lớp Room_receipt gọi hàm startTimer() (ghi nhận thời gian bắt đầu sử dụng).
Lớp Room_receipt trả kết quả lưu dữ liệu về lớp ConfirmCheckInView.
Lớp ConfirmCheckInView hiện thông báo thành công.
Nhân viên ấn nút quay lại.
Lớp ConfirmCheckInView gọi lại về lớp ReceptionistHomeView.
Lớp ReceptionistHomeView hiển thị.


4.4. Chức năng “Check-out”
Nhân viên click chức năng "Check-out" trên giao diện ReceptionistHomeView.
Lớp ReceptionistHomeView gọi sang lớp CheckOutView.
Lớp CheckOutView gọi đến lớp Room để lấy dữ liệu 
Lớp room gọi hàm searchRoom().
Lớp room trả kết quả về lớp CheckOutView.
Lớp CheckOutView hiển thị danh sách phòng "Đang hoạt động" cho nhân viên.
Nhân viên hỏi khách hàng số phòng cần trả.
Khách hàng trả lời.
Nhân viên chọn phòng tương ứng trên danh sách.
Lớp CheckOutView gọi sang lớp InvoiceView.
Lớp InvoiceView gọi đến đối tượng Room_receipt (để tính tổng tiền).
Lớp Room_receipt gọi hàm CalculateTotalAmount().
Lớp Room_receipt trả kết quả về lớp InvoiceView.
Lớp InvoiceView gọi đến đối tượng MemberRanking (để kiểm tra hạng thành viên).
Lớp MemberRanking gọi hàm checkMember().
Lớp MemberRanking trả kết quả về lớp InvoiceView.
Lớp InvoiceView hiển thị chi tiết hóa đơn.
Nhân viên thông báo tổng tiền cho khách hàng.
Khách hàng cung cấp mã ưu đãi (nếu có).
Nhân viên nhập mã và ấn áp dụng.
Lớp InvoiceView gọi đến đối tượng Promotion.
Lớp Promotion gọi hàm applyPromotion().
Lớp Promotion trả kết quả về InvoiceView.
Lớp InvoiceView gọi lại đến lớp Room_receip (cập nhật lại tổng tiền).
Lớp Room_receipt gọi hàm CalculateTotalAmount().
Lớp Room_receipt trả kết quả về lớp InvoiceView.
Lớp InvoiceView hiển thị chi tiết hoá đơn lại lần nữa cho nhân viên lễ tân.
Nhân viên lễ tân thông báo lại tổng tiền cho khách hàng và hỏi khách hàng muốn thanh toán theo phương thức nào.
Khách hàng trả lời. 
Nhân viên chọn phương thức thanh toán và click nút xác nhận thanh toán.
Lớp InvoiceView gọi sang lớp PaymentView.
Lớp PaymentView gọi sang lớp Room_receipt (cập nhật trạng thái "Đã thanh toán").
Lớp Room_receipt  gọi hàm updateStatus().
Lớp Room_receipt trả kết quả về lớp PaymentView.
Lớp PaymentView gọi đến lớp Room (chuyển về trạng thái “Trống”).
Lớp Room gọi hàm changeStatus().
Lớp Room trả kết quả về lớp PaymentView.
Lớp PaymentView gọi đến lớp MemberRanking (cộng điểm tích luỹ).
Lớp MemberRanking gọi hàm addPoints().
Lớp MemberRanking trả kết quả về lớp PaymentView.
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
3.2.1. Chức năng Đặt phòng
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
3.2.2. Chức năng Check-in
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
3.2.3. Chức năng Check-out
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
3.2.4. Chức năng Huỷ phòng
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
4.1. Chức năng "Đặt phòng"
a) Biểu đồ tuần tự

b) Kịch bản phiên bản 3
1. Nhân viên lễ tân click chức năng "Đặt phòng" trên giao diện ReceptionistHomePage.
2. Phương thức btnDatPhongClick() của lớp ReceptionistHomePage được gọi.
3. Phương thức btnDatPhongClick() gọi phương thức navigate() của lớp SearchFreeRoomForm.
4. Lớp SearchFreeRoomForm hiển thị form tìm phòng trống cho nhân viên.
5. Nhân viên nhập thời gian bắt đầu (startTime), thời gian kết thúc (endTime) và chọn chi nhánh (branchId).
6. Nhân viên click nút [Tìm phòng trống].
7. Phương thức btnSearchClick() của lớp SearchFreeRoomForm được gọi.
8. Phương thức btnSearchClick() gọi phương thức searchFreeRoom(startTime: Date, endTime: Date, branchId: int) của lớp BookingController.
9. Phương thức searchFreeRoom() gọi phương thức findByTimeAndBranch(startTime, endTime, branchId) của lớp Entity Room.
10. Lớp Room trả kết quả danh sách phòng trống về cho phương thức searchFreeRoom().
11. Phương thức searchFreeRoom() trả kết quả về cho phương thức btnSearchClick().
12. Lớp SearchFreeRoomForm hiển thị danh sách phòng trống cho nhân viên.
13. Nhân viên ấn vào phòng trống.
14. Phương thức tblRoomsClick(selectedRow: int) của lớp SearchFreeRoomForm được gọi.
15. Phương thức tblRoomsClick() gọi phương thức navigate(roomId) của lớp SearchClientForm.
16. Lớp SearchClientForm hiển thị form tìm khách hàng cho nhân viên.
17. Nhân viên nhập thông tin khách hàng (tên hoặc số điện thoại).
18. Nhân viên click [Tìm kiếm].
19. Phương thức btnSearchClick() của lớp SearchClientForm được gọi.
20. Phương thức btnSearchClick() gọi phương thức searchClient(keyword: String) của lớp BookingController.
21. Phương thức searchClient() gọi phương thức findByKeyword(keyword) của lớp Entity Client.
22. Lớp Client trả kết quả danh sách khách hàng về cho phương thức searchClient().
23. Phương thức searchClient() trả kết quả về cho phương thức btnSearchClick().
24. Lớp SearchClientForm hiển thị danh sách khách hàng khớp.
25. Nhân viên chọn thông tin khách hàng tương ứng.
26. Phương thức tblClientsClick(selectedRow: int) của lớp SearchClientForm được gọi.
27. Phương thức tblClientsClick() gọi phương thức navigate(roomId, clientId, timeRange) của lớp ConfirmBookingModal.
28. Lớp ConfirmBookingModal hiển thị thông tin xác nhận đặt phòng.
29. Nhân viên ấn nút xác nhận.
30. Phương thức btnConfirmClick() của lớp ConfirmBookingModal được gọi.
31. Phương thức btnConfirmClick() gọi phương thức createBooking(clientId: int, roomId: int, startTime: Date, endTime: Date, staffId: int) của lớp BookingController.
32. Phương thức createBooking() gọi phương thức updateStatus(roomId, "Chờ nhận") của lớp Entity Room_receipt.
33. Lớp Room_receipt cập nhật trạng thái và trả kết quả về cho phương thức createBooking().
34. Phương thức createBooking() lưu booking vào CSDL và trả BookingResponse về cho phương thức btnConfirmClick().
35. Lớp ConfirmBookingModal hiển thị thông báo "Đặt phòng thành công!".
36. Nhân viên ấn nút OK.
37. Phương thức showMessage() của lớp ConfirmBookingModal được gọi.
38. Phương thức showMessage() gọi phương thức navigate() của lớp ReceptionistHomePage.
39. Hệ thống quay về giao diện chính ReceptionistHomePage.
4.2. Chức năng "Check-in"
a) Biểu đồ tuần tự

b) Kịch bản phiên bản 3
1. Nhân viên lễ tân click chức năng "Check-in" trên giao diện ReceptionistHomePage.
2. Phương thức btnCheckInClick() của lớp ReceptionistHomePage được gọi.
3. Phương thức btnCheckInClick() gọi phương thức navigate() của lớp CheckInPage.
4. Phương thức formLoad() của lớp CheckInPage được gọi.
5. Phương thức formLoad() gọi phương thức getPendingBookings(branchId: int, date: Date) của lớp BookingController.
6. Phương thức getPendingBookings() gọi phương thức findByStatus("Chờ nhận") của lớp Entity Room.
7. Lớp Room trả kết quả danh sách booking về cho phương thức getPendingBookings().
8. Phương thức getPendingBookings() trả kết quả về cho phương thức formLoad().
9. Lớp CheckInPage hiển thị danh sách booking "Chờ nhận" hôm nay cho nhân viên.
10. Nhân viên ấn chọn booking tương ứng cần check-in trên danh sách.
11. Phương thức tblPendingBookingsClick(selectedRow: int) của lớp CheckInPage được gọi.
12. Phương thức tblPendingBookingsClick() gọi phương thức navigate(bookingId) của lớp ConfirmCheckInView.
13. Lớp ConfirmCheckInView hiển thị thông tin chi tiết của phòng và khách hàng.
14. Nhân viên ấn nút xác nhận check-in.
15. Phương thức btnCheckInClick() của lớp ConfirmCheckInView được gọi.
16. Phương thức btnCheckInClick() gọi phương thức checkIn(bookingId: int) của lớp BookingController.
17. Phương thức checkIn() gọi phương thức updateStatus(roomId, "Đang hoạt động") của lớp Entity Room.
18. Lớp Room cập nhật trạng thái và trả kết quả về cho phương thức checkIn().
19. Phương thức checkIn() gọi phương thức setStartTime(now) của lớp Entity Room_receipt.
20. Lớp Room_receipt ghi nhận thời gian bắt đầu và trả kết quả về cho phương thức checkIn().
21. Phương thức checkIn() trả BookingResponse về cho phương thức btnCheckInClick().
22. Lớp ConfirmCheckInView hiển thị thông báo "Check-in thành công! Phòng [tên phòng] đã sẵn sàng."
23. Nhân viên ấn nút quay lại.
24. Phương thức showMessage() của lớp ConfirmCheckInView được gọi.
25. Phương thức showMessage() gọi phương thức navigate() của lớp ReceptionistHomePage.
26. Hệ thống quay về giao diện chính ReceptionistHomePage.
4.3. Chức năng "Check-out"
a) Biểu đồ tuần tự

b) Kịch bản phiên bản 3
1. Nhân viên lễ tân click chức năng "Check-out" trên giao diện ReceptionistHomePage.
2. Phương thức btnCheckOutClick() của lớp ReceptionistHomePage được gọi.
3. Phương thức btnCheckOutClick() gọi phương thức navigate() của lớp CheckOutPage.
4. Phương thức formLoad() của lớp CheckOutPage được gọi.
5. Phương thức formLoad() gọi phương thức getActiveRooms(branchId: int) của lớp BookingController.
6. Phương thức getActiveRooms() gọi phương thức findByStatus("Đang hoạt động") của lớp Entity Room.
7. Lớp Room trả kết quả danh sách phòng về cho phương thức getActiveRooms().
8. Phương thức getActiveRooms() trả kết quả về cho phương thức formLoad().
9. Lớp CheckOutPage hiển thị danh sách phòng đang sử dụng cho nhân viên.
10. Nhân viên chọn phòng tương ứng trên danh sách.
11. Phương thức tblActiveRoomsClick(selectedRow: int) của lớp CheckOutPage được gọi.
12. Phương thức tblActiveRoomsClick() gọi phương thức navigate(room_receipt_ID) của lớp InvoicePanel.
13. Phương thức formLoad(invoice: Room_receipt) của lớp InvoicePanel được gọi.
14. Phương thức formLoad() gọi phương thức calculateInvoice(room_receipt_ID: int) của lớp BookingController.
15. Phương thức calculateInvoice() gọi phương thức calculateTimeFee() + calculateServiceFee() của lớp Entity Room_receipt.
16. Lớp Room_receipt trả kết quả hóa đơn về cho phương thức calculateInvoice().
17. Phương thức calculateInvoice() trả Room_receipt về cho phương thức formLoad().
18. Lớp InvoicePanel hiển thị chi tiết tiền phòng, dịch vụ, thời gian sử dụng và tổng tiền.
19. Nhân viên thông báo tổng tiền cho khách hàng.
20. Khách hàng cung cấp mã ưu đãi (nếu có).
21. Nhân viên nhập mã và ấn áp dụng.
22. Phương thức btnApply() của lớp InvoicePanel được gọi.
23. Phương thức btnApply() gọi phương thức applyPromotion(room_receipt_ID: int) của lớp BookingController.
24. Phương thức applyPromotion() gọi phương thức applyVoucher() của lớp Entity Promotion.
25. Lớp Promotion trả kết quả giảm giá về cho phương thức applyPromotion().
26. Phương thức applyPromotion() trả kết quả về cho phương thức btnApply().
27. Lớp InvoicePanel cập nhật lại tổng tiền sau giảm giá.
28. Khách hàng đưa tiền mặt cho nhân viên.
29. Nhân viên chọn phương thức thanh toán và click nút xác nhận thanh toán.
30. Phương thức btnThanhToanClick() của lớp InvoicePanel được gọi.
31. Phương thức btnThanhToanClick() gọi phương thức confirmPayment(room_receipt_ID: int, paymentMethod: String, voucherCode: String) của lớp BookingController.
32. Phương thức confirmPayment() gọi phương thức updateStatus("Đã thanh toán") của lớp Entity Room_receipt.
33. Phương thức confirmPayment() gọi phương thức updateStatus("Trống") của lớp Entity Room.
34. Phương thức confirmPayment() gọi phương thức addPoints(base_score) của lớp Entity Client.
35. Các lớp Entity trả kết quả lưu trữ về cho phương thức confirmPayment().
36. Phương thức confirmPayment() trả Room_receipt về cho phương thức btnThanhToanClick().
37. Lớp InvoicePanel hiển thị thông báo "Check-out thành công! Tổng tiền: [X]đ."
38. Nhân viên click nút in hóa đơn (để đưa cho khách hàng) và ấn hoàn tất.
39. Phương thức btnInHoaDonClick() của lớp InvoicePanel được gọi.
40. Phương thức btnInHoaDonClick() gọi phương thức showMessage() của lớp InvoicePanel.
41. Phương thức showMessage() gọi phương thức navigate() của lớp ReceptionistHomePage.
42. Hệ thống quay về giao diện chính ReceptionistHomePage.
4.4. Chức năng "Huỷ phòng"
a) Biểu đồ tuần tự

b) Kịch bản phiên bản 3
1. Nhân viên lễ tân click chức năng "Quản lý đặt phòng" trên giao diện ReceptionistHomePage.
2. Phương thức btnBookingManagementClick() của lớp ReceptionistHomePage được gọi.
3. Phương thức btnBookingManagementClick() gọi phương thức navigate() của lớp CancelBookingPage.
4. Lớp CancelBookingPage hiển thị form tìm kiếm booking.
5. Nhân viên nhập thông tin tìm kiếm (họ tên, số điện thoại hoặc mã phòng đã đặt) và ấn nút tìm kiếm.
6. Phương thức btnSearchClick() của lớp CancelBookingPage được gọi.
7. Phương thức btnSearchClick() gọi phương thức searchBooking(keyword: String) của lớp BookingController.
8. Phương thức searchBooking() gọi phương thức findByKeyword(keyword) của lớp Entity Room.
9. Lớp Room trả kết quả danh sách phòng về cho phương thức searchBooking().
10. Phương thức searchBooking() gọi phương thức findByKeyword(keyword) của lớp Entity Room_receipt.
11. Lớp Room_receipt trả kết quả danh sách hóa đơn về cho phương thức searchBooking().
12. Phương thức searchBooking() tổng hợp và trả kết quả về cho phương thức btnSearchClick().
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
24. Phương thức cancelBooking() gọi phương thức updateStatus("Đã hủy") của lớp Entity Room_receipt.
25. Lớp Room_receipt cập nhật trạng thái và trả kết quả về cho phương thức cancelBooking().
26. Phương thức cancelBooking() trả BookingResponse về cho phương thức btnCancelClick().
27. Lớp CancelBookingPage hiển thị thông báo "Hủy đặt phòng thành công."
28. Nhân viên ấn nút quay lại.
29. Phương thức showMessage() của lớp CancelBookingPage được gọi.
30. Phương thức showMessage() gọi phương thức navigate() của lớp ReceptionistHomePage.
31. Hệ thống quay về giao diện chính ReceptionistHomePage.
IV. PHA CÀI ĐẶT VÀ KIỂM THỬ
1.1. Lập kế hoạch test
Phạm vi test: Module "Quản lý đặt và trả phòng" — 4 chức năng: Đặt phòng, Check-in, Check-out, Huỷ phòng.
Loại test: Functional testing (kiểm thử chức năng) — kiểm tra từng chức năng theo kịch bản sử dụng thực tế.
Nguyên tắc test:
Test case bao gồm: CSDL trước test → Kịch bản thực hiện → Kết quả mong đợi → CSDL sau test
CSDL mẫu dùng dữ liệu tiếng Việt, tên riêng Việt Nam
Dữ liệu trong CSDL phải khớp với ERD (III.2) và Entity class (III.1)
Kết quả mong đợi PHẢI liệt kê TOÀN BỘ UI elements khi sang giao diện mới
---
1.2. Các test case cho từng chức năng
a) Chức năng "Đặt phòng"
TC01: Đặt phòng thành công
CSDL trước khi test:
*tblBranch:*
*tblRoom:*
*tblClient:*
*tblEmployee:*
*tblMemberRanking:*
CSDL sau khi test:
*tblRoom:*
*tblRoom_receipt:*
---
TC02: Không tìm thấy phòng trống theo thời gian yêu cầu
CSDL trước khi test:
*tblRoom:*
CSDL sau khi test: Không thay đổi.
---
TC03: Khách hàng chưa có trong CSDL
CSDL trước khi test:
*tblRoom:*
*tblClient:*
CSDL sau khi test:
*tblClient (mới tạo):*
---
TC04: Đặt phòng trực tuyến thành công
CSDL trước khi test:
*tblRoom:*
*tblClient:*
CSDL sau khi test:
*tblRoom:*
*tblRoom_receipt:*
---
b) Chức năng "Check-in"
TC05: Check-in thành công
CSDL trước khi test:
*tblRoom:*
*tblRoom_receipt:*
*tblClient:*
CSDL sau khi test:
*tblRoom:*
*tblRoom_receipt:*
---
TC06: Phòng đang dọn dẹp, không thể check-in
CSDL trước khi test:
*tblRoom:*
*tblRoom_receipt:*
CSDL sau khi test: Không thay đổi.
---
TC07: Check-in phòng Super VIP
CSDL trước khi test:
*tblRoom:*
*tblRoom_receipt:*
*tblClient:*
CSDL sau khi test:
*tblRoom:*
*tblRoom_receipt:*
---
c) Chức năng "Check-out"
TC08: Check-out thành công, thanh toán tiền mặt
CSDL trước khi test:
*tblRoom:*
*tblRoom_receipt:*
*tblRoom_receipt_detail:*
*tblClient:*
*tblMemberRanking:*
CSDL sau khi test:
*tblRoom:*
*tblRoom_receipt:*
*(Điểm tích lũy được cộng: 711.000 / 10.000 = 71 điểm)*
---
TC09: Check-out với voucher giảm giá
CSDL trước khi test:
*tblRoom:*
*tblRoom_receipt:*
*tblPromotion:*
CSDL sau khi test:
*tblRoom:*
*tblRoom_receipt:*
*tblApply_promotion:*
---
TC10: Check-out với hội viên Vàng
CSDL trước khi test:
*tblRoom:*
*tblRoom_receipt:*
*tblClient:*
*tblMemberRanking:*
CSDL sau khi test:
*tblRoom:*
*tblRoom_receipt:*
---
TC11: Voucher không hợp lệ
CSDL trước khi test:
*tblRoom:*
*tblRoom_receipt:*
CSDL sau khi test: Không thay đổi.
---
TC12: Check-out chuyển khoản
CSDL trước khi test:
*tblRoom:*
*tblRoom_receipt:*
*tblClient:*
CSDL sau khi test:
*tblRoom:*
*tblRoom_receipt:*
---
d) Chức năng "Huỷ phòng"
TC13: Hủy đặt phòng thành công
CSDL trước khi test:
*tblRoom:*
*tblRoom_receipt:*
*tblClient:*
CSDL sau khi test:
*tblRoom:*
*tblRoom_receipt:*
---
TC14: Không tìm thấy booking
CSDL trước khi test:
*tblRoom_receipt:*
CSDL sau khi test: Không thay đổi.
---
TC15: Booking đã quá thời gian hủy
CSDL trước khi test:
*tblRoom:*
*tblRoom_receipt:*
CSDL sau khi test: Không thay đổi.
---
1.3. Tóm tắt kết quả test
Tỷ lệ đạt: 15/15 = 100%
Kết luận: Tất cả các test case đều đạt yêu cầu. Module "Quản lý đặt và trả phòng" hoạt động đúng theo thiết kế.

