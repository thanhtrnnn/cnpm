# Quản trị cốt lõi


MỤC LỤC



I. PHA XÁC ĐỊNH YÊU CẦU
Mô hình nghiệp vụ bằng UML
1.1. Danh sách các Actor cho module

1.2. Các Use Case cho Actor







1.3. Biểu đồ Use Case tổng quan của mô-đun 



1.4. Biểu đồ Use Case phân rã của mô-đun
Use Case 16 - Quản lý hệ thống chi nhánh

Use Case 17 - Quản lý khách hàng toàn hệ thống

Use Case 18 - Quản lý hạng hội viên

Use Case 19 - Quản lý danh mục loại phòng

Use Case 20 - Quản lý phòng hát tại chi nhánh



II. PHA PHÂN TÍCH
1. Mô hình hóa chức năng
1.1. Kịch bản “Quản lý hệ thống chi nhánh”



1.2. Kịch bản “Quản lý khách hàng toàn hệ thống”




1.3. Kịch bản “Quản lý hạng hội viên”



1.4. Kịch bản “Quản lý danh mục loại phòng”




1.5. Kịch bản “Quản lý phòng hát chi nhánh”

2. Mô hình hóa lớp
Bước 1 – Mô tả Module bằng 1 đoạn văn:
Module Quản trị cốt lõi cho phép Admin và Quản lý chi nhánh thực hiện các thao tác quản lý dữ liệu nền tảng. Admin có thể quản lý hệ thống chi nhánh: thêm, sửa, xóa chi nhánh với các thông tin như tên chi nhánh, địa chỉ, điện thoại chi nhánh. Admin quản lý khách hàng: tìm kiếm, xem lịch sử sử dụng và khóa tài khoản khách hàng trên toàn chuỗi với các thông tin tên khách hàng, số điện thoại, điểm tích lũy, trạng thái tài khoản. Admin quản lý hạng hội viên: cấu hình ngưỡng điểm, ưu đãi giảm giá và thay đổi hạng. Admin quản lý danh mục loại phòng: định nghĩa các chuẩn phòng, sức chứa và trạng thái dùng chung cho toàn chuỗi. Bên cạnh đó, Quản lý chi nhánh được cấp quyền quản lý phòng hát lẻ tại chi nhánh của mình: thêm các phòng vật lý theo loại phòng Admin đã tạo, cập nhật tên phòng và trạng thái phòng.










Bước 2 – Trích danh từ và đánh giá:


=> Các lớp thực thể: Branch, Customer, MembershipTier, RoomType, Room, Booking (Ngoại lai).

Bước 4 – Xác định quan hệ số lượng giữa các thực thể:
Một Branch có thể có nhiều Room, một Room chỉ thuộc về duy nhất một Branch ⇒ Branch và Room quan hệ 1-n.
Một MembershipTier có thể áp dụng cho nhiều Customer, một Customer tại một thời điểm chỉ thuộc về một MembershipTier duy nhất ⇒ MembershipTier và Customer quan hệ 1-n.
Một RoomType có thể được áp dụng cho nhiều Room (ở nhiều chi nhánh), một Room cụ thể chỉ được thiết lập theo một RoomType duy nhất ⇒ RoomType và Room quan hệ 1-n.
Một Customer có thể có nhiều Booking ⇒ Customer và Booking có quan hệ 1-n.
Một Room có thể có nhiều Booking ⇒ Room và Booking quan hệ 1-n.

Bước 5 – Xác định quan hệ đối tượng giữa các thực thể:
Branch có quan hệ gắn chặt (composition) với Room: phòng hát vật lý không thể tồn tại nếu chi nhánh bị giải thể/xóa bỏ.
MembershipTier có quan hệ hợp thành (aggregation) với Customer: khách hàng vẫn tồn tại và hoạt động bình thường khi hạng hội viên bị xóa bỏ hoặc thay đổi.
RoomType có quan hệ liên kết (association) với Room: phòng hát tham chiếu đến loại phòng chuẩn từ danh mục do Admin định nghĩa.
Customer và Room có quan hệ liên kết (association) với Booking: dùng để truy vấn chéo dữ liệu lịch sử.















Biểu đồ lớp thực thể pha phân tích:








3. Mô hình hóa tĩnh - Biểu đồ phân tích chức năng
3.1. Chức năng Quản lý hệ thống chi nhánh (UC16)
Phân tích chi tiết chức năng Quản lý hệ thống chi nhánh:
Admin đăng nhập vào hệ thống -> giao diện chính hiện lên -> đề xuất lớp AdminHomeView, có nút Quản lý hệ thống chi nhánh.
Admin chọn nút Quản lý hệ thống chi nhánh -> giao diện danh sách chi nhánh hiện lên -> đề xuất lớp BranchPage, hiển thị danh sách các chi nhánh kèm nút Thêm mới, ô tìm kiếm và nút Sửa, Xóa.
Khi giao diện được hiển thị, hệ thống phải tìm kiếm danh sách chi nhánh trong CSDL -> đề xuất hàm searchBranch() của lớp Branch.
Admin click nút Thêm mới -> giao diện form nhập liệu hiện lên -> đề xuất lớp BranchForm, có các ô nhập Tên chi nhánh, Địa chỉ, Số điện thoại và nút Lưu.
Sau khi Admin điền thông tin và ấn nút Lưu, hệ thống phải thực hiện lưu thông tin chi nhánh xuống CSDL -> cần chức năng addBranch() -> chức năng này là hành động của đối tượng Branch.
Tương tự, khi Admin thao tác sửa hoặc xóa chi nhánh, hệ thống đề xuất các hàm updateBranch() và deleteBranch() của lớp Branch.
Cập nhật xong, hệ thống quay về giao diện danh sách chi nhánh BranchPage để Admin tiếp tục quản lý.

3.2. Chức năng Quản lý khách hàng toàn hệ thống
Phân tích chi tiết chức năng Quản lý khách hàng toàn hệ thống:
Vào hệ thống -> giao diện chính hiện lên -> đề xuất lớp AdminHomeView, có nút Quản lý khách hàng.
Admin click nút Quản lý khách hàng -> giao diện tìm kiếm khách hàng hiện lên -> đề xuất lớp CustomerPage, hiển thị ô nhập từ khóa, tiêu chí tìm kiếm, nút Tìm kiếm và bảng danh sách khách hàng.
Admin nhập từ khóa và ấn Tìm kiếm, hệ thống phải tìm kiếm khách hàng trong CSDL -> đề xuất hàm searchCustomer() của lớp Customer.
Admin click chọn một khách hàng và ấn Xem -> giao diện chi tiết khách hàng hiện lên -> đề xuất lớp CustomerDetailPanel, hiển thị thông tin cá nhân, lịch sử sử dụng, trạng thái và nút Khóa tài khoản.
Khi giao diện chi tiết hiển thị, hệ thống truy xuất thông tin chi tiết bằng hàm getCustomerDetails() của lớp Customer, đồng thời gọi hàm getBookingHistory() của lớp Booking để lấy lịch sử sử dụng.
Sau khi Admin ấn nút Khóa tài khoản -> hệ thống thực hiện cập nhật trạng thái khóa xuống CSDL -> cần chức năng lockAccount() -> chức năng này là hành động của đối tượng Customer.
Cập nhật xong, hệ thống thông báo thành công và cập nhật lại giao diện CustomerDetailPanel để Admin tiếp tục thao tác.


3.3. Chức năng Quản lý hạng hội viên
Phân tích chi tiết chức năng Quản lý hạng hội viên:
Vào hệ thống -> giao diện chính hiện lên -> đề xuất lớp AdminHomeView, có nút Quản lý hạng hội viên.
Admin click nút Quản lý hạng hội viên -> giao diện cấu hình hạng hiện lên -> đề xuất lớp MembershipTierPage, hiển thị bảng danh sách các hạng hội viên, nút Thay đổi hạng thủ công và nút Sửa.
Khi giao diện hiển thị, hệ thống phải tải danh sách hạng từ CSDL -> đề xuất hàm getAllTiers() của lớp MembershipTier.
Admin click nút Sửa trên một hạng -> giao diện form sửa hiện lên -> đề xuất lớp MembershipTierForm, hiển thị ô nhập Ngưỡng điểm, Giảm giá và nút Lưu.
Admin thay đổi thông tin và ấn nút Lưu -> hệ thống thực hiện cập nhật cấu hình hạng xuống CSDL -> cần chức năng updateTier() -> chức năng này là hành động của đối tượng MembershipTier.
Nếu Admin ấn nút Thay đổi hạng thủ công -> giao diện tìm kiếm và đổi hạng hiện lên -> đề xuất lớp ManualUpgradeModal, hiển thị ô tìm kiếm khách hàng, dropdown chọn hạng và nút Xác nhận.
Sau khi Admin ấn nút Xác nhận -> hệ thống thực hiện cập nhật hạng cho khách hàng xuống CSDL -> cần chức năng upgradeMembershipManual() -> chức năng này là hành động của đối tượng Customer.
Cập nhật xong, hệ thống quay về giao diện MembershipTierPage để Admin tiếp tục cấu hình.




3.4. Chức năng Quản lý danh mục loại phòng
Phân tích chi tiết chức năng Quản lý danh mục loại phòng:
Vào hệ thống -> giao diện chính hiện lên -> đề xuất lớp AdminHomeView, có nút Quản lý danh mục loại phòng.
Admin click nút Quản lý danh mục loại phòng -> giao diện danh mục loại phòng hiện lên -> đề xuất lớp RoomTypePage, hiển thị bảng danh sách loại phòng chuẩn và nút Thêm mới.
Khi giao diện hiển thị, hệ thống phải lấy danh sách loại phòng từ CSDL -> đề xuất hàm getAllRoomTypes() của lớp RoomType.
Admin click nút Thêm mới -> giao diện form loại phòng hiện lên -> đề xuất lớp RoomTypeForm, hiển thị ô nhập Tên loại, Sức chứa chuẩn, Giá cước chung, Trạng thái và nút Lưu.
Admin điền thông tin và ấn nút Lưu -> hệ thống thực hiện lưu loại phòng xuống CSDL toàn chuỗi -> cần chức năng addRoomType() -> chức năng này là hành động của đối tượng RoomType.
Tương tự, khi Admin thao tác sửa hoặc xóa loại phòng, hệ thống đề xuất các hàm updateRoomType() và deleteRoomType() của lớp RoomType.
Cập nhật xong, hệ thống quay về giao diện danh mục RoomTypePage để Admin tiếp tục quản lý.




3.5. Chức năng Quản lý phòng hát chi nhánh
Phân tích chi tiết chức năng Quản lý phòng hát chi nhánh:
Vào hệ thống -> giao diện chính hiện lên -> đề xuất lớp BranchManagerHomeView, có nút Quản lý phòng hát.
Quản lý chi nhánh click nút Quản lý phòng hát -> giao diện danh sách phòng hiện lên -> đề xuất lớp RoomPage, hiển thị bảng danh sách phòng thuộc chi nhánh, trạng thái và nút Thêm mới.
Khi giao diện hiển thị, hệ thống phải tìm kiếm danh sách phòng theo chi nhánh trong CSDL -> đề xuất hàm getRoomsByBranch() của lớp Room.
Quản lý chi nhánh click nút Thêm mới -> giao diện form nhập phòng hiện lên -> đề xuất lớp RoomForm, hiển thị ô nhập Tên phòng, dropdown Loại phòng, Trạng thái và nút Lưu.
Quản lý chi nhánh nhập thông tin và ấn nút Lưu -> hệ thống thực hiện kiểm tra và lưu phòng mới xuống CSDL -> cần chức năng addRoom() -> chức năng này là hành động của đối tượng Room.
Tương tự, khi Quản lý thao tác Sửa phòng, hệ thống đề xuất hàm updateRoom() của lớp Room. Khi thao tác Xóa phòng, hệ thống sẽ gọi checkActiveBooking() của lớp Booking để kiểm tra, sau đó gọi deleteRoom() của lớp Room.
Cập nhật xong, hệ thống quay về giao diện danh sách phòng RoomPage để Quản lý chi nhánh tiếp tục quản lý.


4. Mô hình hóa động - Biểu đồ tuần tự
4.1. Chức năng Quản lý hệ thống chi nhánh
Kịch bản chi tiết:
Chủ doanh nghiệp (Admin) click vào chức năng "Quản lý hệ thống chi nhánh" trên giao diện AdminHomeView.
Lớp AdminHomeView gọi sang lớp BranchPage.
Lớp BranchPage gọi đến lớp Branch để xử lý thông tin.
Lớp Branch gọi hàm searchBranch().
Lớp Branch trả kết quả về cho lớp BranchPage.
Lớp BranchPage hiển thị.
Chủ doanh nghiệp click nút "Thêm mới".
Lớp BranchPage gọi sang lớp BranchForm.
Lớp BranchForm hiển thị.
 Chủ doanh nghiệp nhập thông tin chi nhánh và click nút "Lưu".
 Lớp BranchForm gọi đến lớp Branch để xử lý thông tin.
 Lớp Branch gọi hàm addBranch().
 Lớp Branch trả kết quả về cho lớp BranchForm.
 Lớp BranchForm gọi lại về lớp BranchPage.
 Lớp BranchPage gọi đến lớp Branch để xử lý thông tin.
 Lớp Branch gọi hàm searchBranch().
 Lớp Branch trả kết quả về cho lớp BranchPage.
 Lớp BranchPage hiển thị.



4.2. Chức năng Quản lý khách hàng toàn hệ thống
Kịch bản chi tiết:
Chủ doanh nghiệp click vào chức năng "Quản lý khách hàng" trên giao diện AdminHomeView.
Lớp AdminHomeView gọi sang lớp CustomerPage.
Lớp CustomerPage hiển thị.
Chủ doanh nghiệp nhập thông tin từ khóa và click nút "Tìm kiếm".
Lớp CustomerPage gọi đến lớp Customer để xử lý thông tin.
Lớp Customer gọi hàm searchCustomer().
Lớp Customer trả kết quả về cho lớp CustomerPage.
Lớp CustomerPage hiển thị danh sách khách hàng tương ứng.
Chủ doanh nghiệp chọn thông tin khách hàng tương ứng và click "Xem".
 Lớp CustomerPage gọi sang lớp CustomerDetailPanel.
 Lớp CustomerDetailPanel gọi đến lớp Customer để xử lý thông tin.
 Lớp Customer gọi hàm getCustomerDetails().
 Lớp Customer trả kết quả về cho lớp CustomerDetailPanel.
 Lớp CustomerDetailPanel gọi đến lớp Booking để xử lý thông tin.
 Lớp Booking gọi hàm getBookingHistory().
 Lớp Booking trả kết quả về cho lớp CustomerDetailPanel.
 Lớp CustomerDetailPanel hiển thị.
 Chủ doanh nghiệp click nút "Khóa tài khoản".
 Lớp CustomerDetailPanel gọi đến lớp Customer để xử lý thông tin.
 Lớp Customer gọi hàm lockAccount().
 Lớp Customer trả kết quả về cho lớp CustomerDetailPanel.
 Lớp CustomerDetailPanel hiện thông báo thành công.


4.3. Chức năng Quản lý hạng hội viên
Kịch bản chi tiết:
Chủ doanh nghiệp click chức năng "Quản lý hạng hội viên" trên giao diện AdminHomeView.
Lớp AdminHomeView gọi sang lớp MembershipTierPage.
Lớp MembershipTierPage gọi đến lớp MembershipTier để xử lý thông tin.
Lớp MembershipTier gọi hàm getAllTiers().
Lớp MembershipTier trả kết quả về cho lớp MembershipTierPage.
Lớp MembershipTierPage hiển thị.
Chủ doanh nghiệp click nút "Sửa" trên một hạng.
Lớp MembershipTierPage gọi sang lớp MembershipTierForm.
Lớp MembershipTierForm hiển thị.
 Chủ doanh nghiệp nhập thông tin thay đổi và click nút "Lưu".
 Lớp MembershipTierForm gọi đến lớp MembershipTier để xử lý thông tin.
 Lớp MembershipTier gọi hàm updateTier().
 Lớp MembershipTier trả kết quả về cho lớp MembershipTierForm.
 Lớp MembershipTierForm gọi lại về lớp MembershipTierPage.
 Lớp MembershipTierPage gọi đến lớp MembershipTier để xử lý thông tin.
 Lớp MembershipTier gọi hàm getAllTiers().
 Lớp MembershipTier trả kết quả về cho lớp MembershipTierPage.
 Lớp MembershipTierPage hiển thị.

4.4. Chức năng Quản lý danh mục loại phòng
Kịch bản chi tiết:
Chủ doanh nghiệp click chức năng "Quản lý danh mục loại phòng" trên giao diện AdminHomeView.
Lớp AdminHomeView gọi sang lớp RoomTypePage.
Lớp RoomTypePage gọi đến lớp RoomType để xử lý thông tin.
Lớp RoomType gọi hàm getAllRoomTypes().
Lớp RoomType trả kết quả về cho lớp RoomTypePage.
Lớp RoomTypePage hiển thị.
Chủ doanh nghiệp click nút "Thêm mới".
Lớp RoomTypePage gọi sang lớp RoomTypeForm.
Lớp RoomTypeForm hiển thị.
 Chủ doanh nghiệp nhập thông tin loại phòng mới và click nút "Lưu".
 Lớp RoomTypeForm gọi đến lớp RoomType để xử lý thông tin.
 Lớp RoomType gọi hàm addRoomType().
 Lớp RoomType trả kết quả về cho lớp RoomTypeForm.
 Lớp RoomTypeForm gọi lại về lớp RoomTypePage.
 Lớp RoomTypePage gọi đến lớp RoomType để xử lý thông tin.
 Lớp RoomType gọi hàm getAllRoomTypes().
 Lớp RoomType trả kết quả về cho lớp RoomTypePage.
 Lớp RoomTypePage hiển thị.

4.5. Chức năng Quản lý phòng hát chi nhánh
Kịch bản chi tiết:
Quản lý chi nhánh click chức năng "Quản lý phòng hát" trên giao diện BranchManagerHomeView.
Lớp BranchManagerHomeView gọi sang lớp RoomPage.
Lớp RoomPage gọi đến lớp Room để xử lý thông tin.
Lớp Room gọi hàm getRoomsByBranch().
Lớp Room trả kết quả về cho lớp RoomPage.
Lớp RoomPage hiển thị.
Quản lý chi nhánh chọn một phòng và click nút "Xóa".
Lớp RoomPage gọi đến lớp Booking để kiểm tra thông tin.
Lớp Booking gọi hàm checkActiveBooking().
 Lớp Booking trả kết quả về cho lớp RoomPage.
 Lớp RoomPage gọi đến lớp Room để xử lý thông tin.
 Lớp Room gọi hàm deleteRoom().
 Lớp Room trả kết quả về cho lớp RoomPage.
 Lớp RoomPage gọi đến lớp Room để xử lý thông tin.
 Lớp Room gọi hàm getRoomsByBranch().
 Lớp Room trả kết quả về cho lớp RoomPage.
 Lớp RoomPage hiển thị danh sách cập nhật.





III. PHA THIẾT KẾ
1. Thiết kế lớp thực thể

2. Thiết kế CSDL

3.  Thiết kế tĩnh
3.1. Thiết kế giao diện
Chức năng Quản lý hệ thống chi nhánh
Màn hình 1: Quản lý hệ thống chi nhánh (BranchPage)
┌──────────────────────────────────────────────────────────┐
│                  QUẢN LÝ CHI NHÁNH                       │
│                                                          │
│  [ + Thêm mới chi nhánh ]                                │
│                                                          │
│ ┌────────┬──────────────────┬──────────────┬───────────┐ │
│ │ Mã CN  │ Tên chi nhánh    │ Địa chỉ      │ Thao tác  │ │
│ ├────────┼──────────────────┼──────────────┼───────────┤ │
│ │ CN01   │ Karaoke Star HN  │ 123 Nguyễn Huệ│ Sửa·Xóa  │ │
│ │ CN02   │ Karaoke Star HCM │ 456 Lê Lợi   │ Sửa·Xóa   │ │
│ │ CN03   │ Karaoke Star ĐN  │ 789 Bạch Đằng│ Sửa·Xóa   │ │
│ └────────┴──────────────────┴──────────────┴───────────┘ │
      └──────────────────────────────────────────────────────────┘
	Màn hình 2: Form thêm/sửa chi nhánh (BranchForm)
┌──────────────────────────────────────┐
                     │       THÊM CHI NHÁNH MỚI             │
│                                      │
│  Tên chi nhánh: [________________]   │
│  Địa chỉ:       [________________]   │
│  Số điện thoại: [________________]   │
│                                      │
│           [ Hủy ]  [ Lưu ]           │
└──────────────────────────────────────┘
Chức năng Quản lý khách hàng toàn hệ thống
Màn hình 3: Quản lý hệ thống chi nhánh (BranchPage)
┌──────────────────────────────────────────────────────────┐
│              QUẢN LÝ KHÁCH HÀNG TOÀN HỆ THỐNG            │
│                                                          │
│  Tiêu chí: [Tên ▼]  Từ khóa: [____________]  [ Tìm ]     |
│                                                          │
│ ┌────────┬──────────┬───────────┬──────────┬───────────┐ │
│ │ Mã KH  │ Họ tên   │ SĐT       │ Hạng     │ Thao tác  │ │
│ ├────────┼──────────┼───────────┼──────────┼───────────┤ │
│ │ KH001  │ Nguyễn A │ 090123456 │ Vàng     │ Xem·Khóa  │ │
│ │ KH045  │ Nguyễn A │ 091234567 │ Bạc      │ Xem·Khóa  │ │
│ └────────┴──────────┴───────────┴──────────┴───────────┘ │
      └──────────────────────────────────────────────────────────┘
Màn hình 4: Chi tiết khách hàng (CustomerDetailPanel)
┌──────────────────────────────────────────────────────────┐
│              CHI TIẾT KHÁCH HÀNG                         │
│                                                          │
           │  Mã KH     : KH001                  Hạng      : Vàng     │
│  Họ tên    : Nguyễn Văn An          SĐT       : 090123456│
│                                     Điểm      : 2500     │
│  Trạng thái: Hoạt động                                   │
│                                                          │
│  ── Lịch sử sử dụng ──                                   │
│  ┌──────────┬────────┬─────────┬──────────┬──────────┐  │
│  │Mã booking│ Phòng  │ Ngày    │ Giờ      │ Tổng tiền│  │
│  ├──────────┼────────┼─────────┼──────────┼──────────┤  │
│  │ BK1023   │ VIP-01 │ 10/05   │ 19-22h   │ 1.500.000│  │
│  │ BK1056   │ STD-03 │ 18/05   │ 20-23h   │ 900.000  │  │
│  └──────────┴────────┴─────────┴──────────┴──────────┘  │
│                                                          │
│  [ Đóng ]  [ Khóa tài khoản ]                            │
└──────────────────────────────────────────────────────────┘
Chức năng Quản lý hạng hội viên
Màn hình 5: Quản lý hạng hội viên (MembershipTierPage)
|──────────────────────────────────────────────────────────┐
│              QUẢN LÝ HẠNG HỘI VIÊN                       │
│                                                          │
│  [ Thay đổi hạng thủ công ]                              │
│                                                          │
│ ┌────────┬──────────┬───────────┬──────────┬──────────┐  │
│ │ Mã hạng│ Tên hạng │ Ngưỡng điểm│ Giảm giá │ Thao tác│  │
│ ├────────┼──────────┼───────────┼──────────┼──────────┤  │
│ │ HH01   │ Thường   │ 0         │ 0%       │ Sửa     │   │
│ │ HH02   │ Bạc      │ 500       │ 5%       │ Sửa     │   │
│ │ HH03   │ Vàng     │ 2000      │ 10%      │ Sửa     │   │
│ └────────┴──────────┴───────────┴──────────┴──────────┘  │
      └──────────────────────────────────────────────────────────┘








Chức năng Quản lý danh mục loại phòng
Màn hình 6: Danh mục loại phòng (RoomTypePage)
┌──────────────────────────────────────────────────────────┐
│              QUẢN LÝ DANH MỤC LOẠI PHÒNG                 │
│                                                          │
│  [ + Thêm loại phòng mới ]                               │
│                                                          │
│ ┌────────┬──────────┬───────────┬──────────┬─────────┐   │
│ │ Mã loại│ Tên loại │ Sức chứa  │ Giá chung│ Thao tác│   │
│ ├────────┼──────────┼───────────┼──────────┼─────────┤   │
│ │ LP01   │ Standard │ 10 người  │ 150.000đ │ Sửa·Xóa │   │
│ │ LP02   │ VIP      │ 15 người  │ 250.000đ │ Sửa·Xóa │   │
│ │ LP03   │ Super VIP│ 20 người  │ 300.000đ │ Sửa·Xóa │   │
│ └────────┴──────────┴───────────┴──────────┴─────────┘   │
      └──────────────────────────────────────────────────────────┘

Chức năng Quản lý phòng hát chi nhánh
Màn hình 7: Quản lý phòng hát chi nhánh (RoomPage)

┌──────────────────────────────────────────────────────────┐
│              QUẢN LÝ PHÒNG HÁT CHI NHÁNH                 │
│                                                          │
│  [ + Thêm phòng mới ]                                    │
│                                                          │
│ ┌────────┬──────────┬───────────┬──────────┬──────────┐  │
│ │Mã phòng│ Tên phòng│ Loại      │Trạng thái│ Thao tác │  │
│ ├────────┼──────────┼───────────┼──────────┼──────────┤  │
│ │ P001   │ VIP-01   │ Super VIP │ Trống    │ Sửa·Xóa  │  │
│ │ P002   │ STD-01   │ Standard  │ Đang pv  │ Sửa·Xóa  │  │
│ └────────┴──────────┴───────────┴──────────┴──────────┘  │
      └──────────────────────────────────────────────────────────┘

3.2. Thiết kế mô hình MVC
Mô hình MVC được thiết kế theo kiến trúc BCE (Boundary – Control – Entity) với 3 tầng:
Boundary (Giao diện): React components xử lý giao diện người dùng
Control (Điều khiển): Spring Boot Controllers xử lý nghiệp vụ
Entity (Thực thể): JPA Entities biểu diễn dữ liệu lưu trữ

Chức năng Quản lý hệ thống chi nhánh
Tầng giao diện (Boundary): 



Tầng điều khiển (Control): 

Tầng thực thể (Entity): Branch

Chức năng Quản lý khách hàng toàn hệ thống
Tầng giao diện (Boundary): 

Tầng điều khiển (Control)

Tầng thực thể (Entity): Customer


Chức năng Quản lý hạng hội viên
Tầng giao diện (Boundary): 


Tầng điều khiển (Control)


Tầng thực thể (Entity): MembershipTier, Customer.

Chức năng Quản lý danh mục loại phòng
Tầng giao diện (Boundary): 

Tầng điều khiển (Control): 

Tầng thực thể (Entity): RoomType.

Chức năng Quản lý phòng hát chi nhánh
Tầng giao diện (Boundary):

Tầng điều khiển (Control):

Tầng điều khiển (Control): Room, RoomType.
3.3. Sơ đồ lớp thiết kế:
Chức năng Quản lý hệ thống chi nhánh

Chức năng Quản lý khách hàng toàn hệ thống


Chức năng Quản lý hạng hội viên












Chức năng Quản lý danh mục loại phòng




Chức năng Quản lý phòng hát chi nhánh




4.  Thiết kế động
4.1. Chức năng quản lý hệ thống chi nhánh	
1. Chủ doanh nghiệp nhấn "Quản lý hệ thống chi nhánh" trên giao diện AdminHomeView.
2. Giao diện AdminHomeView gọi phương thức btnManageBranchClick().
3. AdminHomeView gọi điều hướng (navigate) mở lớp BranchPage.
4. Lớp BranchPage tự gọi hàm formLoad() của chính nó ngay khi vừa được tạo.
5. BranchPage gọi sang lớp BranchController thông qua hàm searchBranches("").
6. BranchController tự gọi hàm validateRequest() để kiểm tra tính hợp lệ của yêu cầu.
7. BranchController gọi thực thể Branch qua phương thức findByKeyword("") để truy vấn danh sách.
8. Thực thể Branch trả kết quả danh sách chi nhánh về cho BranchController.
9. BranchController map dữ liệu entity sang định dạng DTO (mapToDTO).
10. BranchController trả danh sách (BranchResponse) về cho giao diện BranchPage.
11. BranchPage tự gọi hàm nội bộ displayDSBranch(branches) để xử lý đổ dữ liệu.
12. BranchPage hiển thị danh sách chi nhánh lên bảng cho Chủ doanh nghiệp.
13. Chủ doanh nghiệp quan sát và nhấn nút "Thêm mới".
14. BranchPage gọi hàm btnAddBranchClick().
15. BranchPage gọi hàm openModal() để mở lớp BranchForm.
16. Lớp BranchForm tự gọi hàm formLoad(null) để chuẩn bị form.
17. BranchForm tự gọi hàm resetFields() để làm sạch các trường dữ liệu.
18. BranchForm hiển thị form trống lên màn hình cho Chủ doanh nghiệp.
19. Chủ doanh nghiệp nhập thông tin Tên chi nhánh.
20. Chủ doanh nghiệp nhập thông tin Địa chỉ.
21. Chủ doanh nghiệp nhập thông tin Số điện thoại.
22. Chủ doanh nghiệp ấn nút Lưu.
23. BranchForm gọi hàm btnSaveClick().
24. BranchForm tự gọi hàm validateInput() để kiểm tra dữ liệu đầu vào phía client.
25. BranchForm đóng gói dữ liệu và gửi sang lớp BranchController thông qua hàm saveBranch(branchDTO).
26. BranchController tự gọi hàm validateData() để kiểm tra logic phía server.
27. BranchController gọi xuống thực thể Branch thực thi phương thức save() để thêm vào cơ sở dữ liệu.
28. Thực thể Branch trả kết quả thêm thành công về cho BranchController.
29. BranchController trả kết quả xử lý (success status) về cho BranchForm.
30. BranchForm tự gọi hàm showMessage("Thêm thành công").
31. Chủ doanh nghiệp nhấn OK trên thông báo.
32. BranchForm đóng lại (close) và trả quyền điều khiển về BranchPage.
33. BranchPage tự động gọi lại formLoad() để làm mới dữ liệu.
34. BranchPage gọi lại hàm searchBranches("") của Controller.
35. Controller trả danh sách mới về cho BranchPage.
36. BranchPage gọi lại displayDSBranch() để cập nhật giao diện.




4.2. Chức năng Quản lý khách hàng toàn hệ thống
1. Chủ doanh nghiệp nhấn nút "Quản lý khách hàng" trên giao diện AdminHomeView.
2. AdminHomeView gọi phương thức btnManageCustomerClick().
3. AdminHomeView gọi điều hướng (navigate) mở lớp CustomerPage.
4. Lớp CustomerPage tự gọi hàm formLoad().
5. CustomerPage gọi hàm searchCustomers("") của CustomerController để lấy dữ liệu mặc định.
6. CustomerController trả danh sách khách hàng ban đầu về.
7. CustomerPage tự gọi hàm displayCustomers() để đổ dữ liệu lên bảng.
8. CustomerPage hiển thị giao diện danh sách cho Chủ doanh nghiệp.
9. Chủ doanh nghiệp nhập từ khóa (Tên hoặc SĐT) vào ô tìm kiếm.
10. Chủ doanh nghiệp nhấn nút "Tìm kiếm".
11. CustomerPage gọi sự kiện btnSearchClick().
12. CustomerPage đẩy từ khóa sang hàm searchCustomers(keyword) của CustomerController.
13. CustomerController tự gọi hàm validateKeyword() để kiểm tra dữ liệu đầu vào.
14. CustomerController gọi thực thể Customer (findByKeyword) để lọc dữ liệu.
15. Thực thể Customer trả kết quả danh sách về cho CustomerController.
16. CustomerController trả SearchResponse về cho CustomerPage.
17. CustomerPage tự gọi hàm displayCustomers(customers) để cập nhật bảng kết quả.
18. Giao diện hiển thị danh sách khách hàng vừa lọc cho Chủ doanh nghiệp.
19. Chủ doanh nghiệp click chọn đúng khách hàng tương ứng trên bảng.
20. CustomerPage bắt sự kiện tblCustomersClick(customerId).
21. CustomerPage gọi mở lớp CustomerDetailPanel thông qua hàm openPanel(customerId).
22. Lớp CustomerDetailPanel tự gọi hàm formLoad(customerId).
23. CustomerDetailPanel gọi CustomerController thông qua hàm getCustomerById(customerId).
24. CustomerController gọi thực thể Customer (findById).
25. Thực thể Customer trả thông tin chi tiết về.
26. CustomerController trả CustomerDTO về cho Panel.
27. CustomerDetailPanel tự gọi displayCustomerInfo() để vẽ giao diện thông tin cá nhân.
28. CustomerDetailPanel tiếp tục tự gọi displayBookingHistory() để vẽ lịch sử đặt phòng.
29. Màn hình chi tiết khách hàng hoàn chỉnh được hiển thị.
30. Chủ doanh nghiệp kiểm tra và nhấn nút "Khóa tài khoản".
31. CustomerDetailPanel gọi hàm btnLockAccountClick().
32. CustomerDetailPanel gửi yêu cầu khóa sang CustomerController thông qua hàm lockAccount(id).
33. CustomerController gọi xuống thực thể Customer thực thi lệnh updateStatus("Đã khóa").
34. Thực thể Customer trả kết quả thành công (true) về.
35. CustomerController trả kết quả về cho CustomerDetailPanel.
36. CustomerDetailPanel hiển thị thông báo "Khóa thành công".
37. Chủ doanh nghiệp nhấn nút OK để đóng thông báo.
38. CustomerDetailPanel tự gọi lại formLoad(customerId) để cập nhật giao diện chi tiết.



4.3. Chức năng Quản lý hạng hội viên
1. Chủ doanh nghiệp nhấn nút "Quản lý hạng hội viên" trên AdminHomeView.
2. AdminHomeView gọi phương thức btnManageTierClick().
3. AdminHomeView gọi navigate mở lớp MembershipTierPage.
4. Lớp MembershipTierPage tự gọi hàm formLoad().
5. MembershipTierPage gọi hàm getAllTiers() của MembershipTierController.
6. MembershipTierController gọi thực thể MembershipTier (findAll).
7. Thực thể MembershipTier trả danh sách về cho Controller.
8. MembershipTierController trả TierResponse về cho MembershipTierPage.
9. MembershipTierPage tự gọi displayTiers(tiers) để hiển thị lên bảng.
10. Giao diện danh sách hạng hội viên được hiển thị.
11. Chủ doanh nghiệp chọn một dòng hạng mục.
12. Chủ doanh nghiệp ấn nút "Đổi hạng thủ công".
13. MembershipTierPage gọi hiển thị lớp ManualUpgradeModal qua hàm openModal().
14. Lớp ManualUpgradeModal tự gọi formLoad().
15. Giao diện form đổi hạng hiển thị cho Chủ doanh nghiệp.
16. Chủ doanh nghiệp nhập mã khách hàng (customerId).
17. Chủ doanh nghiệp nhấn nút "Kiểm tra".
18. ManualUpgradeModal gọi CustomerController qua hàm getCustomerById(customerId).
19. CustomerController gọi thực thể Customer (findById).
20. Thực thể Customer trả thông tin khách về.
21. CustomerController trả CustomerInfo hợp lệ về cho Modal.
22. ManualUpgradeModal tự gọi displayCustomerInfo() để hiện tên và hạng cũ.
23. Chủ doanh nghiệp chọn hạng mới từ ComboBox.
24. Chủ doanh nghiệp ấn "Xác nhận".
25. ManualUpgradeModal gọi hàm btnConfirmClick().
26. ManualUpgradeModal tự gọi validateSelection() kiểm tra logic.
27. ManualUpgradeModal gửi yêu cầu đổi hạng sang MembershipTierController thông qua hàm manualUpgrade(customerId, tierId).
28. MembershipTierController tự gọi validateLogic() để xác thực quy tắc nâng hạng.
29. MembershipTierController gọi thực thể Customer cập nhật FK (updateTierId).
30. Thực thể Customer trả kết quả cập nhật thành công.
31. MembershipTierController trả kết quả xử lý (upgradeStatus) về cho Modal.
32. ManualUpgradeModal gọi showMessage("Đổi hạng thành công").
33. Chủ doanh nghiệp nhấn OK để đóng thông báo.
34. ManualUpgradeModal tự gọi close() đóng popup và trở về Page.
35. MembershipTierPage gọi lại formLoad() để làm mới cấu hình hiển thị nếu cần.






4.4. Chức năng Quản lý danh mục loại phòng
1. Chủ doanh nghiệp nhấn "Quản lý danh mục loại phòng" trên AdminHomeView.
2. AdminHomeView gọi phương thức btnManageRoomTypeClick().
3. AdminHomeView navigate mở lớp RoomTypePage.
4. Lớp RoomTypePage tự gọi hàm formLoad().
5. RoomTypePage gọi hàm getAllRoomTypes() của RoomTypeController.
6. RoomTypeController gọi thực thể RoomType (findAll).
7. Thực thể RoomType trả kết quả danh sách về.
8. RoomTypeController trả kết quả về cho RoomTypePage.
9. RoomTypePage tự gọi hàm displayRoomTypes(types) để xử lý giao diện.
10. RoomTypePage hiển thị danh mục loại phòng lên bảng.
11. Chủ doanh nghiệp ấn nút "Thêm danh mục mới".
12. RoomTypePage gọi openModal() mở lớp RoomTypeForm.
13. Lớp RoomTypeForm tự gọi hàm formLoad(null).
14. Lớp RoomTypeForm tự gọi resetFields() xóa trắng dữ liệu.
15. Màn hình form trống hiện lên cho Chủ doanh nghiệp.
16. Chủ doanh nghiệp nhập Tên loại phòng.
17. Chủ doanh nghiệp nhập Sức chứa.
18. Chủ doanh nghiệp nhập Giá cơ sở.
19. Chủ doanh nghiệp ấn Lưu.
20. RoomTypeForm gọi hàm btnSaveClick().
21. RoomTypeForm tự gọi validateInput() để kiểm tra kiểu dữ liệu đầu vào.
22. RoomTypeForm gọi hàm saveRoomType(roomTypeDTO) của RoomTypeController.
23. RoomTypeController gọi validateData() kiểm tra quy tắc nghiệp vụ.
24. RoomTypeController gọi thực thể RoomType (save).
25. Thực thể RoomType trả lại đối tượng vừa lưu thành công.
26. RoomTypeController trả success status về cho RoomTypeForm.
27. RoomTypeForm gọi showMessage("Thêm thành công").
28. Chủ doanh nghiệp nhấn OK.
29. RoomTypeForm gọi hàm close() để tự đóng cửa sổ.
30. RoomTypePage gọi lại formLoad() để làm mới dữ liệu.
31. RoomTypePage gọi lại getAllRoomTypes().
32. Controller trả danh sách mới về cho Page.
33. RoomTypePage gọi displayRoomTypes() để cập nhật bảng.







4.5. Chức năng Quản lý phòng hát chi nhánh
1. Quản lý chi nhánh nhấn nút "Quản lý phòng hát" trên BranchManagerHomeView.
2. BranchManagerHomeView gọi phương thức btnManageRoomClick().
3. BranchManagerHomeView navigate gọi hiển thị lớp RoomPage.
4. Lớp RoomPage tự gọi hàm formLoad().
5. RoomPage gọi hàm getRoomsByBranch(branchId) của RoomController.
6. RoomController gọi thực thể Room (findByBranch) lấy danh sách phòng thuộc chi nhánh.
7. Thực thể Room trả kết quả danh sách về cho Controller.
8. RoomController trả RoomResponse về cho RoomPage.
9. RoomPage tự gọi displayRooms(rooms) hiển thị lên bảng.
10. Giao diện phòng hát được hiển thị cho Quản lý chi nhánh.
11. Quản lý chi nhánh ấn nút "Thêm phòng mới".
12. RoomPage gọi openModal() để hiển thị lớp RoomForm.
13. Lớp RoomForm tự gọi hàm formLoad(null).
14. Bên trong formLoad, RoomForm lập tức gọi hàm getAllRoomTypes() của RoomTypeController.
15. RoomTypeController gọi thực thể RoomType (findAll) để lấy tất cả các danh mục.
16. Thực thể RoomType trả kết quả danh sách về.
17. RoomTypeController trả danh sách cấu hình loại phòng về cho RoomForm.
18. RoomForm tự gọi renderComboBox() để nạp dữ liệu loại phòng vào thẻ Dropdown (ComboBox).
19. Form nhập liệu hoàn thiện được hiển thị cho người dùng.
20. Quản lý chi nhánh nhập Tên phòng.
21. Quản lý chi nhánh chọn Trạng thái phòng từ danh sách có sẵn.
22. Quản lý chi nhánh chọn Loại phòng từ ComboBox.
23. Quản lý chi nhánh nhấn nút Lưu.
24. RoomForm gọi hàm btnSaveClick().
25. RoomForm tự gọi hàm validateInput() kiểm tra dữ liệu client.
26. RoomForm gửi dữ liệu thông qua hàm saveRoom(roomDTO) của RoomController.
27. RoomController gọi validateData() kiểm tra xem tên phòng có bị trùng trong chi nhánh không.
28. RoomController gọi thực thể Room lưu thông tin (save).
29. Thực thể Room trả kết quả lưu thành công vào CSDL.
30. RoomController trả kết quả saveStatus về cho RoomForm.
31. RoomForm gọi showMessage("Thêm thành công").
32. Quản lý chi nhánh nhấn OK.
33. RoomForm tự gọi hàm close() để đóng popup.
34. Lớp RoomPage gọi lại formLoad() và cập nhật lại bảng giao diện hiện tại.



IV. PHA CÀI ĐẶT VÀ KIỂM THỬ
1. Lập kế hoạch test
Phạm vi test: Module "Quản trị cốt lõi" - 5 chức năng: 
Quản lý chi nhánh (UC16)
Quản lý khách hàng toàn hệ thống (UC17) 
Quản lý hạng hội viên (UC18)
Quản lý danh mục loại phòng (UC19)
Quản lý phòng hát chi nhánh (UC20).
Loại test: Functional testing (kiểm thử chức năng) - kiểm tra từng chức năng theo kịch bản sử dụng thực tế (black-box testing).
Nguyên tắc test:
Mỗi test case bao gồm: CSDL trước test → Kịch bản thực hiện (từng bước) → Kết quả mong đợi → CSDL sau test.
CSDL mẫu dùng dữ liệu tiếng Việt, tên riêng Việt Nam.
Test case bao gồm cả trường hợp thành công và trường hợp thất bại.

2. Trạng thái CSDL mẫu trước khi test toàn bộ
Trước khi thực hiện các test case, CSDL cần được thiết lập ở trạng thái ban đầu như sau:

tblBranch:

tblMembershipTier:

tblCustomer:

tblRoomType:






tblRoom:

3. Các test case cho từng chức năng
3.1.  Chức năng "Quản lý hệ thống chi nhánh" (UC16)
TC01: Thêm chi nhánh mới thành công (tên chưa tồn tại)
Bước thực hiện:


CSDL trước khi test:
tblBranch:

CSDL sau khi test:
tblBranch:





TC02: Thêm chi nhánh mới thất bại (tên đã tồn tại)
Bước thực hiện:


CSDL trước khi test:
tblBranch:



CSDL sau khi test:
Không thay đổi.



TC03: Sửa thông tin chi nhánh thành công
Bước thực hiện:






CSDL trước khi test: 
tblBranch:

CSDL sau khi test: 
tblBranch:

TC04: Xóa chi nhánh không có phòng hoạt động → thành công
Bước thực hiện:

CSDL trước khi test:
 tblBranch:

tblRoom: (không có phòng thuộc chi nhánh 3)



CSDL sau khi test: 
tblBranch:

tblRoom: không thay đổi.

TC05: Xóa chi nhánh có phòng đang hoạt động → thất bại
Bước thực hiện:





CSDL trước khi test: 
tblBranch:

tblRoom:

CSDL sau khi test: Không thay đổi.


3.2.  Chức năng "Quản lý khách hàng toàn hệ thống" (UC17)
TC06: Tìm kiếm khách hàng theo tên → tìm thấy kết quả
Bước thực hiện:

CSDL trước khi test: 
tblCustomer:

CSDL sau khi test: Không thay đổi (chỉ truy vấn, không ghi).


TC07: Tìm kiếm khách hàng → không tìm thấy
Bước thực hiện:

CSDL trước khi test: 
tblCustomer: 

CSDL sau khi test: Không thay đổi.
TC08: Xem lịch sử sử dụng của khách hàng
Bước thực hiện:

CSDL trước khi test: 
tblCustomer: 


CSDL sau khi test: Không thay đổi (chỉ truy vấn).

TC09: Khóa tài khoản khách hàng thành công
Bước thực hiện:

CSDL trước khi test:
tblCustomer:

CSDL sau khi test: 
tblCustomer:


3.3 Chức năng "Quản lý hạng hội viên" (UC18)
TC10: Xem cấu hình hạng hội viên
Bước thực hiện:

CSDL trước khi test: tblMembershipTier:


CSDL sau khi test: Không thay đổi (chỉ truy vấn).



TC11: Sửa ngưỡng điểm hạng Bạc thành công
Bước thực hiện:

CSDL trước khi test: tblMembershipTier:

CSDL sau khi test: tblMembershipTier:




TC12: Thay đổi hạng thủ công cho khách hàng thành công

Bước thực hiện:


CSDL trước khi test: tblCustomer:


CSDL sau khi test: tblCustomer:



3.4. Chức năng "Quản lý danh mục loại phòng" (UC19)
TC13: Thêm loại phòng mới thành công
Bước thực hiện:

CSDL trước khi test: tblRoomType:


CSDL sau khi test: tblRoomType:






TC14: Thêm loại phòng mới thất bại (tên trùng)
Bước thực hiện:

CSDL trước khi test: tblRoomType: (giống TC13)

CSDL sau khi test: Không thay đổi.


TC15: Sửa thông tin loại phòng thành công
Bước thực hiện:

CSDL trước khi test: tblRoomType:


CSDL sau khi test: tblRoomType:


TC16: Xóa loại phòng không có phòng vật lý sử dụng → thành công
Bước thực hiện:

CSDL trước khi test: tblRoomType:


tblRoom: (không có phòng nào dùng loại Super VIP)


CSDL sau khi test: tblRoomType:


tblRoom: không thay đổi.


TC17: Xóa loại phòng đang được sử dụng → thất bại
Bước thực hiện:

CSDL trước khi test: tblRoomType:


tblRoom:


CSDL sau khi test: Không thay đổi.


3.5 Chức năng "Quản lý phòng hát chi nhánh" (UC20)
TC18: Thêm phòng mới tại chi nhánh thành công
Bước thực hiện:

CSDL trước khi test: tblRoom:


CSDL sau khi test: tblRoom:


TC19: Thêm phòng mới thất bại (tên trùng trong chi nhánh)
Bước thực hiện:

CSDL trước khi test: tblRoom:


CSDL sau khi test: Không thay đổi.

TC20: Sửa trạng thái phòng thành công
Bước thực hiện:

CSDL trước khi test: tblRoom:


CSDL sau khi test: tblRoom:




TC21: Xóa phòng không có đặt phòng hoạt động → thành công
Bước thực hiện:

CSDL trước khi test: tblRoom:


CSDL sau khi test: tblRoom:






TC22: Xóa phòng có đặt phòng đang hoạt động → thất bại
Bước thực hiện:

CSDL trước khi test: tblRoom:


CSDL sau khi test: Không thay đổi.


4. Tóm tắt kết quả test

Tỷ lệ đạt: 22/22 = 100%
Kết luận: Tất cả các test case đều đạt yêu cầu. Module "Quản trị cốt lõi" hoạt động đúng theo thiết kế, bao gồm đầy đủ 5 chức năng: quản lý chi nhánh, quản lý khách hàng, quản lý hạng hội viên, quản lý danh mục loại phòng và quản lý phòng hát chi nhánh. Các trường hợp thành công và thất bại đều được xử lý đúng theo kịch bản và ràng buộc nghiệp vụ.

