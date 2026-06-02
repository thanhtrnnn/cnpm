
HỌC VIỆN CÔNG NGHỆ BƯU CHÍNH VIỄN THÔNG
KHOA CÔNG NGHỆ THÔNG TIN 1
______________BÁO CÁO BÀI TẬP LỚN
HỌC PHẦN: NHẬP MÔN CÔNG NGHỆ PHẦN MỀM
Module: Dịch vụ & Sản phẩmGiảng viên hướng dẫn: Đỗ Thị Liên
Lớp học phần: D23CQCE01-B
Nhóm thực hiện: Nhóm 7
SV thực hiện: Nguyễn Gia Đức Trung
MSV: B23DCVT423HÀ NỘI, THÁNG 5/2026
MỤC LỤC

I. PHA XÁC ĐỊNH YÊU CẦU 
3. Mô hình nghiệp vụ bằng UML
3.1. Danh sách các Actor cho module
Actor trực tiếp: Nhân viên phục vụ (Service Staff), Nhân viên lễ tân (Receptionist), Nhân viên quản lý chi nhánh (Branch manager). Các actor này kế thừa từ actor Nhân viên (Employee).
Actor gián tiếp: Khách hàng (Client).

3.2. Các Use Case cho từng Actor

Actor | Use caseNhân viên phục vụ | Quản lý order | Báo cáo tình trạng hàng hóaNhân viên quản lý chi nhánh | Quản lý kho | Quản lý menuKhách hàng | Order
3.3. Biểu đồ UC tổng quan của module


3.4. Các biểu đồ Use Case phân rã của module
a) Use case Quản lý order


b) Báo cáo tình trạng hàng hóa


c) Quản lý menu


d) Quản lý kho


II. PHA PHÂN TÍCH
1. Mô hình hóa chức năng
1.1. Kịch bản “Tạo order”

Tên UC | Tạo orderActor | Nhân viên phục vụ, khách hàngTiền điều kiện | Khách hàng gọi điện yêu cầu orderHậu điều kiện | Đơn gọi món lưu vào CSDLKịch bản chính | (1) Khách hàng gọi điện thoại để order sản phẩm. Nhân viên phục vụ click vào chức năng tìm phòng.
(2) Hệ thống hiển thị danh sách các phòng đang hoạt động.
(3) Nhân viên nhập số phòng mà khách nói và tìm kiếm.
(4) Giao diện hiển thị phòng tương ứng.
(5) Nhân viên click vào phòng tương ứng và click tạo order.
(6) Giao diện hiện lên danh sách các sản phẩm.
(7) Nhân viên A hỏi lại khách hàng B về sản phẩm muốn order kèm số lượng.
(8) Khách hàng B trả lời sản phẩm kèm số lượng.
(9) Nhân viên A gõ tên sản phẩm vào thanh tìm kiếm và click nút tìm kiếm.
(10) Hệ thống hiển thị danh sách các sản phẩm theo từ khóa đã nhập.
(11) Nhân viên A click vào nút “Thêm” ở các sản phẩm tương ứng và click xác nhận.
(12) Hệ thống hiển thị thông báo "Tạo order thành công" trên màn hình của nhân viên A và cơ sở dữ liệu tự động trừ số lượng sản phẩm và cộng dồn tiền dịch vụ ở Hóa đơn phòng.
(13) Sau khi đơn hàng được phục vụ, nhân viên A cập nhật trạng thái đơn hàng thành “Đã phục vụ”.Ngoại lệ | (4) Phòng mà khách trả lời không có trong danh sách đang hoạt động.
(10) Sản phẩm khách yêu cầu không có trong danh sách sản phẩm.
(11) Nhân viên click nút “Thêm” nhưng tồn kho của sản phẩm không còn.
1.2. Kịch bản “Báo cáo tình trạng hàng”

Tên UC | Báo cáo tình trạng hàngActor | Nhân viên phục vụTiền điều kiện | Khách trả phòngHậu điều kiện | Báo cáo lưu vào CSDLKịch bản chính | (1) Nhân viên phục vụ A vào phòng và mở hệ thống để tiến hành kiểm tra cơ sở vật chất.
(2) Hệ thống hiển thị các phòng ở trạng thái “Chờ dọn”.
(3) Nhân viên chọn phòng tương ứng và bắt đầu tạo báo cáo tình trạng phòng.
(4) Hệ thống hiển thị giao diện danh sách các cơ sở vật chất.
(5) Nhân viên A nhập tên cơ sở vật chất và ấn tìm kiếm.
(6) Hệ thống hiện lên csvc tương ứng.
(7) Nhân viên nhập báo cáo tình trạng lên giao diện hệ thống và ấn lưu lại báo cáo.
(8) Hệ thống tự động tìm kiếm hóa đơn phòng và cộng thêm tiền vào cột damage_fee. Đồng thời, ghi nhận trừ số lượng trong Database cơ sở vật chất.
(9) Sau khi dọn xong, nhân viên cập nhật trạng thái phòng từ "Đang chờ dọn" sang "Trống".Ngoại lệ | (6) Cơ sở vật chất chưa có trong CSDL.
1.3. Kịch bản “Quản lý menu”

Tên UC | Sửa menuActor | Nhân viên quản lýTiền điều kiện | Quản lý cần sửa thông tin của sản phẩmHậu điều kiện | Thông tin sản phẩm được cập nhật vào CSDLKịch bản chính | (1) Quản lý chi nhánh truy cập vào hệ thống để sửa thông tin sản phẩm.
(2) Hệ thống hiện giao diện đăng nhập, có ô nhập tên đăng nhập, mật khẩu, và nút đăng nhập.
(3) Quản lý nhập thông tin tài khoản của mình và click đăng nhập.
(4) Hệ thống hiện giao diện chính của nhân viên quản lí, có chức năng lựa chọn: quản lí menu.
(5) Quản lý chọn chức năng quản lí menu.
(6) Hệ thống hiện giao diện danh sách các sản phẩm, có 3 chức năng lựa chọn: thêm, sửa, xóa sản phẩm.
(7) Quản lý tìm kiếm sản phẩm cần thực hiện thao tác.
(8) Hệ thống hiển thị sản phẩm tương ứng.
(9) Quản lý click vào sản phẩm và click nút sửa.
(10) Hệ thống hiển thị thông tin chi tiết của sản phẩm.
(11) Quản lý sửa giá sản phẩm và click nút cập nhật.
(12) Hệ thống thông báo thành công.
(13) Quản lý click OK.
(14) Hệ thống cập nhật thông tin về CSDL và trở về giao diện chính của quản lý.Ngoại lệ | (8) Hệ thống báo không có sản phẩm nào trong kết quả tìm kiếm.

1.4. Kịch bản “Quản lý kho”

Tên UC | Quản lý khoActor | Nhân viên quản lýTiền điều kiện | Quản lý cần kiểm tra tồn kho của các sản phẩmHậu điều kiện | Phiếu nhập sản phẩm lưu vào CSDLKịch bản chính | (1) Quản lý chi nhánh truy cập vào tác vụ Quản lý kho trên phần mềm để kiểm tra số lượng tồn kho của các sản phẩm và csvc.
(2) Hệ thống hiển thị danh sách các sản phẩm.
(3) Quản lý kiểm tra thấy một số sản phẩm thông báo đỏ vì sắp hết hàng vì vậy click vào chức năng Nhập hàng.
(4) Hệ thống hiển thị giao diện danh sách các nhà cung cấp có trong CSDL.
(5) Quản lý nhập tên nhà cung cấp muốn nhập hàng và click tìm.
(6) Hệ thống hiển thị thông tin của nhà cung cấp.
(7) Quản lý click vào nhà cung cấp muốn nhập hàng.
(8) Hệ thống hiển thị phiếu nhập hàng.
(9) Quản lý tìm kiếm sản phẩm.
(10) Hệ thống hiển thị sản phẩm.
(9) Quản lý nhập các thông tin lên phiếu và ấn xác nhận.
(10) Hệ thống thông báo tạo phiếu thành công.
(11) Quản lý click OK.
(12) Hệ thống lưu phiếu vào CSDL và cập nhật lại số lượng của từng sản phẩm.Ngoại lệ | (6) Hệ thống thông báo không có nhà cung cấp nào trong kết quả tìm kiếm.
(10) Sản phẩm không có trong CSDL.
2. Mô hình hóa lớp
Mô tả module bằng 1 đoạn văn:
“Trong module Dịch vụ và Kho, khách hàng hoặc Nhân viên phục vụ thực hiện yêu cầu gọi món bằng cách tạo Đơn hàng. Ngay lập tức, hệ thống sẽ tự động trừ số lượng tương ứng trong tồn kho hệ thống và ghi nhận chi phí dịch vụ vào hóa đơn phòng. Sau khi khách trả phòng, Nhân viên phục vụ tiến hành dọn dẹp; nếu phát hiện tài sản vỡ hỏng, nhân viên sẽ lập báo cáo tình trạng. Dựa vào báo cáo này, hệ thống tiếp tục trừ kho và có thể sinh ra phí đền bù. Khi một sản phẩm rơi xuống dưới định mức an toàn, Quản lý sẽ lập liên hệ đặt hàng với Nhà cung cấp. Khi hàng được giao đến, Quản lý tiến hành đếm số lượng và tạo phiếu nhập kho, cấu trúc dữ liệu sẽ tự động thêm số lượng của các sản phẩm tương ứng”.

Xác định lớp thực thể:
Khách hàng: không phải đổi tượng xử lý của module → loại.
Nhân viên phục vụ: đối tượng xử lý của module → 1 lớp thực thể chung: Employee.
Đơn hàng: đối tượng xử lý của module → 1 lớp thực thể: Order.
Hệ thống: danh từ chung chung → loại.
Tồn kho hệ thống: thuộc tính của Product.
Chi phí dịch vụ: thuộc tính của Room_receipt.
Hóa đơn phòng: đối tượng xử lý của module → 1 lớp thực thể: Room_receipt.
Phòng: đối tượng xử lý của module → 1 lớp thực thể: Room.
Tài sản: đối tượng xử lý của module → 1 lớp thực thể: Facility.
Báo cáo tình trạng: đối tượng xử lý của module → 1 lớp thực thể: Damage_report.
Phí đền bù: thuộc tính của Room_receipt.
Hàng hóa: đối tượng xử lý của module → 1 lớp thực thể: Product.
Quản lý chi nhánh: đối tượng xử lý của module → 1 lớp thực thể chung: Employee.
Định mức an toàn: thuộc tính của Product.
Nhà cung cấp: đối tượng xử lý của module → 1 lớp thực thể: Provider.
Phiếu nhập kho: đối tượng xử lý của module → 1 lớp thực thể: Import_receipt.

⇒ Các lớp thực thể ban đầu: Employee, Order, Room_receipt, Room, Facility, Damage_report, Product, Provider, Import_receipt.

Xác định quan hệ số lượng giữa các thực thể:
Một Room có nhiều Room_receipt, một Room_receipt chỉ thuộc về một Roon ⇒ Room và Room_receipt quan hệ 1-n.
Một Employee có thể tạo nhiều Order, một Order chỉ do một Employee tạo ⇒ Employee và Order quan hệ 1-n.
Một Employee có thể tạo nhiều Room_receipt, một Room_receipt chỉ do một Employee tạo ⇒ Employee và Room_receipt quan hệ 1-n.
Một Employee có thể tạo nhiều Damage_report, một Damage_report chỉ do một Employee tạo ⇒ Employee và Damage_report quan hệ 1-n.
Một Employee có thể tạo nhiều Import_receipt, một Import_receipt chỉ do một Employee tạo ⇒ Employee và Import_receipt quan hệ 1-n.
Một Room_receipt có thể không có Order nào, có 1 Order hoặc nhiều Order, một Order chỉ thuộc duy nhất một Room_receipt ⇒ Room_receipt và Order quan hệ 1-0..*.
Một Order có thể có nhiều Product, một Product có thể ở nhiều Order ⇒ Order và Product quan hệ n-n ⇒ Cần có lớp trung gian là Order_detail.
Một Damage_report có thể có nhiều Facility, một Facility có thể ở nhiều Damage_report ⇒ Damage_report và Facility quan hệ n-n ⇒ Cần có lớp trung gian là Damage_detail.
Một Provider có thể có nhiều Import_receipt, một Import_receipt chỉ ứng với một Provider ⇒ Provider và Import_receipt quan hệ 1-n.
Một Import_receipt có thể có nhiều Product, một Product có thể ở nhiều Import_receipt ⇒ Import_receipt và Product quan hệ n-n ⇒ Cần có lớp trung gian là Import_detail.
Một Room_receipt có thể không có, có 1 hoặc nhiều Damage_report, một Damage_report chỉ thuộc về duy nhất một Room_receipt ⇒ Room_receipt và Damage_report quan hệ 1-0..*.

Xác định quan hệ đối tượng giữa các thực thể:
Damage_report là thành phần của Room_receipt.
Order là thành phần của Room_receipt.
Room_receipt là thành phần của Room.
Damage_report và Facility liên kết tạo ra Damage_detail.
Order và Product liên kết tạo ra Order_detail.
Import_receipt và Product liên kết tạo ra Import_detail.

⇒ Biểu đồ lớp thực thể pha phân tích:


3. Mô hình hóa tĩnh - Biểu đồ phân tích chức năng
3.1. Chức năng Tạo order
Phân tích chi tiết chức năng Tạo Order:
Vào hệ thống -> giao diện login hiện lên -> đề xuất lớp LoginView, có 2 ô nhập username, password và nút Login.
Nhập username/password -> hệ thống phải kiểm tra thông tin đăng nhập -> cần chức năng checkLogin() -> chức năng này là hành động của đối tượng Employee.
Login thành công, hệ thống hiện giao diện chính của nhân viên -> đề xuất lớp StaffHomeView, có nút quản lý order.
Click nút tìm phòng đang hoạt động -> đề xuất lớp SearchRoomView, hiển thị danh sách các phòng hát đang hoạt động, ô nhập số phòng và nút tìm kiếm và nút tạo order.
Nhân viên nhập tên và ấn tìm kiếm, hệ thống phải tìm kiếm phòng trong CSDL -> đề xuất hàm searchActiveRoom() của lớp Room.
Nhân viên click vào phòng tương ứng và ấn nút tạo order -> giao diện chọn sản phẩm hiện lên -> đề xuất lớp CreateOrderView, hiển thị tên phòng, danh sách các sản phẩm kèm nút thêm, ô tìm kiếm sản phẩm, nút tìm kiếm và nút lưu.
Khi nhân viên tìm kiếm sản phẩm, hệ thống phải tìm kiếm sản phẩm trong CSDL, đề xuất hàm searchProduct() của lớp Product.
Sau khi nhân viên ấn nút lưu, giao diện hiện lên thông báo tạo order thành công -> đề xuất lớp ConfirmOrderView, hiển thị thông báo và có nút xác nhận.
Nhân viên nhấn nút "Xác nhận" -> hệ thống thực hiện lưu đơn hàng xuống CSDL -> cần chức năng addOrder() -> chức năng này là hành động chính của đối tượng Order.
Sau đó, hệ thống tự động cộng dồn phí dịch vụ -> cần chức năng updateServiceFee() của đổi tượng Room_receipt.
Cập nhật xong, hệ thống quay về giao diện chi tiết phòng StaffHomeView để nhân viên tiếp tục phục vụ.


3.2. Chức năng Báo cáo tình trạng hàng hóa
Phân tích chi tiết chức năng Báo cáo tình trạng hàng hóa:
Vào hệ thống -> giao diện login hiện lên -> đề xuất lớp LoginView, có 2 ô nhập username, password và nút Login.
Nhập username/password -> hệ thống kiểm tra thông tin đăng nhập -> cần chức năng checkLogin() -> chức năng này là hành động của đối tượng Employee.
Login thành công, hệ thống hiện giao diện chính -> đề xuất lớp StaffHomeView, có nút báo cáo tình trạng hàng.
Click nút tìm phònghiển thị sơ đồ các phòng đang chờ dọn và nút tạo báo cáo.
Nhân viên tìm kiếm phòng cần dọn -> cần chức năng searchPendingRoom() của đối tượng Room.
Nhân viên click vào một phòng và ấn tạo báo cáo -> giao diện báo cáo hiện lên -> đề xuất lớp DamageReportView, có tên phòng, ô nhập tên csvc và nút lưu, danh sách các csvc và có ô để nhập số lượng hỏng, và nút lưu.
Nhân viên nhập tên csvc bị hỏng và click tìm kiếm -> hệ thống tìm kiếm trong danh mục tài sản -> cần chức năng searchFacility() -> chức năng này là hành động của đối tượng Facility.
Sau khi đã nhập các csvc bị hỏng vào báo cáo, nhân viên click nút lưu -> hệ thống hiện giao diện tạo báo cáo thành công -> đề xuất lớp ConfirmReportView, có thông báo hoàn tất và nút xác nhận.
Nhân viên click nút xác nhận, hệ thống thực hiện lưu báo cáo vào CSDL -> cần chức năng addDamageReport() của lớp DamageReport.
Sau đó hệ thống tự động cập nhật lại phí hỏng hóc -> cần chức năng updateDamageFee() của đối tượng Room_receipt.


3.3. Chức năng Quản lý menu
Phân tích chi tiết chức năng quản lý menu:
Vào hệ thống -> giao diện login hiện lên -> đề xuất lớp LoginView, có 2 ô nhập username, password và nút Login.
Nhập username/password -> hệ thống kiểm tra thông tin đăng nhập -> cần chức năng checkLogin() -> chức năng này là hành động của đối tượng Employee.
Login thành công, hệ thống hiện giao diện chính -> đề xuất lớp ManagerHomeView, có ít nhất nút ấn chức năng quản lý menu.
Nhân viên quản lý vào chức năng quản lý menu -> đề xuất lớp MenuView, hiển thị danh sách các sản phẩm, ô tìm kiếm sản phẩm và các nút tìm kiếm, thêm, sửa, xóa.
Quản lý tìm kiếm sản phẩm, hệ thống cần tìm thông tin sản phẩm -> cần chức năng searchProduct() của đối tượng Product.
Quản lý ấn vào nút sửa -> đề xuất lớp EditMenuView, hiển thị thông tin chi tiết của sản phẩm và nút xác lưu.
Quản lý thay đổi thông tin của sản phẩm và ấn nút lưu, hệ thống thực hiện lưu vào CSDL -> cần chức năng updateProduct() của lớp Product.
Sau khi hoàn tất, quay trở lại MenuView.


3.4. Chức năng Quản lý kho
Phân tích chi tiết chức năng Quản lý kho:
Vào hệ thống -> giao diện login hiện lên -> đề xuất lớp LoginView, có 2 ô nhập username, password và nút Login.
Nhập username/password -> hệ thống kiểm tra thông tin đăng nhập -> cần chức năng checkLogin() của đối tượng Employee.
Login thành công, hệ thống hiện giao diện chính của Quản lý -> đề xuất lớp ManagerHomeView, có nút chọn vào "Quản lý kho".
Click vào nút Quản lý kho, giao diện hiển thị danh sách các sản phẩm trong kho -> đề xuất lớp WarehouseManageView, có nút nhập hàng.
Click vào nút nhập hàng, giao diện hiển thị danh sách các nhà cung cấp -> đề xuất lớp SearchProviderView, có ô tìm kiếm và nút tạo phiếu nhập.
Nhập tên nhà cung cấp, hệ thống tìm kiếm thông tin tương ứng -> cần chức năng searchProvider() của đối tượng Provider.
Sau khi ấn nút tạo phiếu nhập -> đề xuất lớp ImportReceiptView, có tên nhà cung cấp, ngày nhập hàng, danh sách sản phẩm, ô tìm kiếm và nút tìm, danh sách chi tiết nhập, tổng tiền và nút xác nhận.
Lớp ImportReceiptView cần tìm sản phẩm -> cần chức năng searchProduct() của đối tượng Product.
Sau khi ấn nút xác nhận, hệ thống lưu vào CSDL và tự động cập nhật số lượng sản phẩm -> cần chức năng addImportReceipt() của đối tượng Import_receipt và updateQuantity() của đổi tượng Product.
Hoàn tất, hệ thống hiển thị thông báo "Thành công" và quay về giao diện chính của Quản lý ManagerHomeView.


4. Mô hình hóa động - Biểu đồ tuần tự
4.1. Chức năng Tạo order
Kịch bản chi tiết:
Nhân viên phục vụ nhập username/password vào giao diện đăng nhập và click nút Login.
Lớp LoginView gọi đến lớp Employee để xử lí.
Lớp Employee gọi hàm checkLogin(). Kết quả đăng nhập thành công.
Lớp Employee gửi kết quả lại cho lớp LoginView.
Lớp LoginView gọi sang lớp StaffHomeView.
Lớp StaffHomeView hiển thị cho nhân viên phục vụ.
Nhân viên click nút quản lý order.
Lớp StaffHomeView gọi sang lớp SearchRoomView.
Lớp SearchRoomView hiển thị.
Nhân viên yêu cầu khách hàng đưa thông tin về số phòng.
Khách hàng trả lời số phòng cho nhân viên.
Nhân viên nhập tên phòng và ấn tìm kiếm.
Lớp SearchRoomView gọi lớp Room.
Lớp Room gọi hàm searchActiveRoom().
Lớp Room trả lại kết quả cho lớp StaffHomeView.
Giao diện hiển thị phòng tương ứng.
Nhân viên click chọn phòng tương ứng và ấn nút tạo order để phục vụ.
Lớp StaffHomeView gọi lớp CreateOrderView.
Lớp CreateOrderView hiển thị cho nhân viên phục vụ.
Nhân viên yêu cầu khách chọn sản phẩm và số lượng.
Khách chọn sản phẩm và số lượng.
Nhân viên nhập tên sản phẩm và click tìm.
Lớp CreateOrderView gọi đến lớp Product.
Lớp Product thực hiện chức năng searchProduct().
Lớp Product trả lại kết quả cho lớp CreateOrderView.
Giao diện hiển thị các thông tin của sản phẩm.
Nhân viên ấn nút thêm.
Sau khi hoàn thành order, nhân viên click nút lưu.
Lớp CreateOrderView gọi sang lớp ConfirmOrderView.
Lớp ConfirmOrderView hiển thị giao diện cho nhân viên phục vụ.
Nhân viên ấn nút OK.
Lớp ConfirmOrderView gọi lớp Order xử lí.
Lớp Order gọi phương thức addOrder() để lưu order vào CSDL.
Lớp Order gọi sang lớp Room_receipt để xử lý.
Lớp Room_receipt gọi hàm updateServiceFee() để cập nhật phí dịch vụ vào hóa đơn phòng.
Lớp Room_receipt trả kết quả lại cho lớp ConfirmOrderView.
Lớp ConfirmOrderView gọi lại lớp StaffHomeView.
Lớp StaffHomeView hiển thị lại cho nhân viên phục vụ.
Nhân viên thông báo order thành công.



4.2. Chức năng Báo cáo tình trạng hàng
Kịch bản chi tiết:
Nhân viên phục vụ nhập username/password vào giao diện đăng nhập và click nút Login.
Lớp LoginView gọi đến lớp Employee để xử lí.
Lớp Employee gọi hàm checkLogin(). Kết quả đăng nhập thành công.
Lớp Employee gửi kết quả lại cho lớp LoginView.
Lớp LoginView gọi sang lớp StaffHomeView.
Lớp StaffHomeView hiển thị cho nhân viên phục vụ.
Nhân viên click vào chức năng báo cáo tình trạng hàng.
Lớp StaffHomeView gọi sang lớp SearchRoomView.
Lớp SearchRoomView hiển thị.
Nhân viên nhập tên phòng và click tìm kiếm.
Lớp StaffHomeView gọi lớp Room để xử lý.
Lớp Room gọi hàm searchPendingRoom().
Lớp Room trả lại kết quả cho lớp StaffHomeView.
Lớp StaffHomeView hiển thị phòng tương ứng.
Nhân viên click vào phòng ấn nút tạo báo cáo.
Lớp StaffHomeView gọi lớp DamageReportView.
Lớp DamageReportView hiển thị chi tiết phòng cho nhân viên phục vụ.
Nhân viên nhập tên tài sản bị hỏng và click tìm.
Lớp DamageReportView gọi lớp Facility xử lí.
Lớp Facility gọi phương thức searchFacility().
Kết quả được lớp Facility gửi lại cho lớp DamageReportView.
Lớp DamageReportView hiển thị kết quả cho nhân viên.
Nhân viên chọn tài sản, nhập số lượng hỏng rồi click lưu báo cáo.
Lớp DamageReportView gọi đến lớp ConfirmReportView.
Lớp ConfirmReportView hiển thị cho nhân viên.
Nhân viên click nút OK.
Lớp ConfirmReportView gọi lớp DamageReport để xử lý.
Lớp DamageReport gọi hàm addDamageReport() để lưu báo cáo vào CSDL.
Lớp DamageReport gọi lớp Room_receipt để xử lý.
Lớp Room_receipt gọi hàm updateDamageFee() để cập nhật phí phát sinh vào hóa đơn.
Lớp Room_receipt trả kết quả về cho lớp ConfirmReportView.
Lớp ConfirmReportView gọi về lớp StaffHomeView.
Lớp StaffHomeView hiển thị cho nhân viên.



4.3. Chức năng Quản lý menu
Kịch bản chi tiết:
Nhân viên quản lý nhập username/password vào giao diện đăng nhập và click nút Login.
Lớp LoginView gọi đến lớp Employee để xử lí.
Lớp Employee gọi hàm kiểm tra đăng nhập. Kết quả đăng nhập thành công.
Lớp Employee gửi kết quả lại cho lớp LoginView.
Lớp LoginView gọi sang lớp ManagerHomeView.
Lớp ManagerHomeView hiển thị cho nhân viên quản lý.
Quản lý click vào chức năng quản lý menu.
Lớp ManagerHomeView gọi đến lớp MenuView.
Lớp MenuView hiển thị.
Quản lý nhập tên sản phẩm muốn sửa và click tìm.
Lớp MenuView gọi đến lớp Product để xử lý.
Lớp Product gọi hàm searchProduct().
Lớp Product trả lại kết quả cho lớp MenuView.
Lớp MenuView hiển thị sản phẩm tương ứng cho quản lý.
Quản lý ấn vào sản phẩm và ấn nút sửa.
Lớp MenuView gọi sang lớp EditMenuView.
Lớp EditmenuView hiển thị.
Nhân viên thực hiện sửa thông tin của sản phẩm và ấn lưu.
Lớp EditMenuView gọi đến lớp Product để lưu thông tin vào CSDL.
Lớp Product gọi hàm updateProduct().
Lớp Product trả lại kết quả cho lớp EditMenuView.
Lớp EditMenuView gọi lớp MenuView.
Lớp MenuView hiển thị.



4.4. Chức năng Quản lý kho
Kịch bản chi tiết:
Nhân viên quản lí nhập username/password vào giao diện đăng nhập và click nút Login.
Lớp LoginView gọi đến lớp Employee để xử lí.
Lớp Employee gọi hàm kiểm tra đăng nhập. Kết quả đăng nhập thành công.
Lớp Employee gửi kết quả lại cho lớp LoginView.
Lớp LoginView gọi sang lớp ManagerHomeView.
Lớp ManagerHomeView hiển thị cho nhân viên quản lí.
Quản lý click vào chức năng quản lí kho.
Lớp ManagerHomeView gọi sang lớp WarehouseManageView.
Lớp WarehouseManageView hiển thị.
Quản lý chọn chức năng nhập hàng.
Lớp WarehouseManageView gọi sang lớp SearchProviderView.
Lớp SearchProviderView hiển thị.
Quản lý nhập tên nhà cung cấp và click tìm.
Lớp SearchProviderView gọi lớp Provider để xử lý.
Lớp Provider gọi hàm searchProvider().
Lớp Provider trả lại kết quả cho lớp SearchProviderView.
Lớp SearchProviderView hiển thị nhà cung cấp tương ứng.
Quản lý chọn nhà cung cấp và click nút tạo phiếu nhập.
Lớp SearchProviderView gọi sang lớp ImportReceiptView.
Lớp InportReceiptView hiển thị.
Quản lý nhập tên sản phẩm và click tìm.
Lớp ImportReceiptView gọi lớp Product.
Lớp Product gọi hàm searchProduct.
Lớp Product trả lại kết quả cho lớp ImportReceiptView.
Lớp ImportReceiptView hiển thị.
Quản lý click lưu.
Lớp ImportReceiptView gọi lớp Import_receipt để xử lý.
Lớp Import_receipt gọi hàm addImportReceipt().
Sau khi bản ghi mới được thêm, lớp Import_receipt gọi tới lớp Product để cập nhật số lượng sản phẩm.
Lớp Product gọi hàm updateQuantity().
Lớp Product trả lại kết quả cho lớp ImportReceiptView.
Lớp ImportReceiptView hiển thị thành công.
Quản lý click OK.
Lớp ImportReceiptView gọi lại lớp ManagerHomeView.
Lớp ManagerHomeView hiển thị lại cho nhân viên quản lí.



III. PHA THIẾT KẾ
1. Thiết kế lớp thực thể

2. Thiết kế CSDL


3.  Thiết kế tĩnh
3.1. Thiết kế giao diện
a) Chức năng Tạo order
Giao diện đăng nhập:


Giao diện chính của phục vụ:


Giao diện tìm phòng:


Giao diện tạo order:


Giao diện xác nhận order:


b) Chức năng báo cáo tình trạng hàng
Giao diện đăng nhập:

Giao diện chính của phục vụ:


Giao diện tìm phòng:


Giao diện báo cáo hư hỏng:


Giao diện xác nhận báo cáo:


c) Chức năng Quản lý order
Giao diện đăng nhập:


Giao diện chính của nhân viên quản lý:


Giao diện menu:


Giao diện sửa thông tin:


d) Chức năng quản lý kho
Giao diện đăng nhập:


Giao diện chính của nhân viên quản lý


Giao diện quản lý kho:


Giao diện phiếu nhập:


3.2. Thiết kế mô hình MVC
Mô hình MVC được thiết kế theo kiến trúc BCE (Boundary – Control – Entity) với 3 tầng:
Boundary (Giao diện): React components xử lý giao diện người dùng
Control (Điều khiển): Spring Boot Controllers xử lý nghiệp vụ
Entity (Thực thể): JPA Entities biểu diễn dữ liệu lưu trữ

a) Chức năng Tạo order
Tầng giao diện (Boundary): 

Lớp | Các thành phần | Chi tiết thành phần | Chức năngLoginPage | Thuộc tính | - txtUsername : TextBox | Ô nhập liệu để nhân viên điền tên tài khoản. |  | - txtPassword : TextBox | Ô nhập liệu để nhân viên điền mật khẩu. |  | - btnLogin : Button | Nút nhấn xác nhận đăng nhập. | Phương thức | + btnLoginClick() : void | Hàm bắt sự kiện khi người dùng click vào nút btnLogin. |  | + showMessage(msg : String) : void | Hàm hiển thị thông báo lỗi khi sai tài khoản hoặc mật khẩuStaffHomePage | Thuộc tính | - btnManageOrder : Button | Nút ấn chức năng quản lý order | Phương thức | + StaffHomePage() : void | Hàm khởi tạoSearchRoomPage | Thuộc tính | - tblActiveRooms : Table | Bảng hiển thị danh sách các phòng hiện đang ở trạng thái đang hoạt động. |  | - txtRoomName : TextBox | Ô nhập liệu để nhân viên gõ tên phòng cần tìm kiếm |  | - btnSearchRoom : Button | Nút kích hoạt lệnh tìm kiếm phòng. |  | - btnCreateOrder : Button | Nút nhấn để mở giao diện chọn món | Phương thức | + formLoad() : void | Hàm tự động chạy khi giao diện vừa được mở lên. Làm nhiệm vụ gọi Controller đi lấy danh sách toàn bộ phòng trống mặc định để chuẩn bị hiển thị. |  | + btnSearchRoomClick() : void | Hàm bắt sự kiện tìm kiếm khi nhấn nút btnSearchRoom. |  | + displayActiveRooms(rooms : List<Room>) : void | Hàm nhận dữ liệu danh sách phòng từ Controller và thực hiện render lên bảng tblActiveRooms. |  | + tblEmptyRoomsClick(selectedRow : int) : void | Hàm bắt sự kiện click chuột vào một dòng trên bảng tblEmptyRooms để hệ thống lưu lại trạng thái phòng đang được chọn. |  | + btnCreateOrderClick() : void | Hàm bắt sự kiện chuyển trang. Nếu nhân viên đã chọn 1 phòng, hàm này gọi Controller để mở giao diện CreateOrderView. |  | + showMessage(msg : String) : void | Hàm hiển thị cảnh báo (ví dụ: "Vui lòng chọn một phòng trước khi tạo order!"). |  | + SearchRoomPage() : void | Hàm khởi tạoCreateOrderPage | Thuộc tính | - lblRoomName : Label | Nhãn văn bản hiển thị tên của phòng |  | - txtProductName : TextBox | Ô nhập liệu để gõ tên sản phẩm. |  | - btnSearchProduct : Button | Nút tìm kiếm sản phẩm trong menu. |  | - tblProducts : Table | Bảng hiển thị danh sách các sản phẩm. |  | - tblOrderDetails : Table | Bảng hiển thị danh sách các sản phẩm trong giỏ hàng hiện tại. |  | - btnSaveOrder : Button | Nút chốt đơn hàng. | Phương thức | + formLoad() : void | Hàm tự động chạy khi cửa sổ này mở lên, gọi Controller lấy danh sách thực đơn mặc định để đổ vào bảng tblProducts. |  | + btnSearchProductClick() : void | Hàm bắt sự kiện click nút tìm món. |  | + btnAddClick() : void | Hàm bắt sự kiện click nút thêm. |  | + btnSaveOrderClick() : void | Hàm bắt sự kiện nhấn nút Lưu. |  | + displayProducts(products : List<Product>) : void | Hàm nhận danh sách sản phẩm từ Controller và hiển thị lên bảng thực đơn tblProducts. |  | + displayOrderCart(orderDetails : List<OrderDetail>) : void | Hàm nhận danh sách giỏ hàng hiện tại (sau mỗi lần thêm/bớt món) từ Controller và làm mới lại dữ liệu hiển thị trên bảng tblOrderDetails. |  | + showMessage(msg : String) : void | Hàm hiển thị các thông báo từ hệ thống (ví dụ: "Kho đã hết mặt hàng này" hoặc "Lỗi lưu dữ liệu"). |  | + CreateOrderPage() : void | Hàm khởi tạoConfirmOrderPage | Thuộc tính | - lblMessage : Label | Nhãn hiển thị nội dung thông báo thành công. |  | - btnConfirm : Button | Nút xác nhận (OK) để đóng cửa sổ. | Phương thức | + btnConfirmClick() : void | Hàm bắt sự kiện khi click nút Xác nhận. |  | + ConfirmOrderPage() : void | Hàm khởi tạo

Tầng điều khiển (Control):

Lớp | Phương thức | Chức năngLoginController | + checkLogin(username : String, password : String) : boolean | Nhận tham số từ ô text của View, kiểm tra DB và trả về kết quả.RoomController | + getActiveRooms() : List<Room> | Được gọi bởi formLoad() của SearchRoomPage để lấy danh sách toàn bộ phòng đang hoạt động lên màn hình. | + searchRoomByName(roomName : String) : List<Room> | Được gọi bởi btnSearchRoomClick() khi nhân viên gõ tên phòng và tìm kiếm.ProductController | + getAllProducts() : List<Product> | Được gọi bởi formLoad() của CreateOrderPage để hiển thị menu mặc định. | + searchProductByName(productName : String) : List<Product> | Hàm được gọi khi bấm nút btnSearchProductClick().OrderController | + saveOrder(order : Order) : boolean | Hàm nhận đối tượng Order (bên trong chứa sẵn danh sách các OrderDetail) để thực thi câu lệnh INSERT xuống cơ sở dữ liệu. Nếu thành công, trả về true để View biết và mở màn hình ConfirmOrderPage.

Tầng thực thể (Entity): Employee, Room, Order, Order_detail, Product, Room_receipt.

b) Chức năng báo cáo tình trạng hàng
Tầng giao diện:

Lớp | Các thành phần | Chi tiết thành phần | Chức năngStaffHomePage | Thuộc tính | - btnReportDamage : Button | Nút bấm báo cáo tài sản hỏng. | Phương thức | + btnReportDamageClick() : void | Hàm bắt sự kiện khi click vào nút btnReportDamage. |  | + StaffHomePage() : void | Hàm khởi tạoSearchRoomPage | Thuộc tính | - txtRoomName : TextBox | Ô nhập liệu để nhân viên gõ tên/số phòng cần tìm kiếm. |  | - btnSearchRoom : Button | Nút nhấn kích hoạt chức năng tìm kiếm phòng. |  | - tblPendingRooms : Table | Bảng hiển thị danh sách các phòng đang chờ thanh toán để nhân viên vào kiểm tra tài sản. |  | - btnCreateDamageReport : Button | Nút nhấn để chuyển sang bước lập báo cáo. | Phương thức | + formLoad() : void | Tự động gọi RoomController lấy danh sách các phòng trạng thái Pending. |  | + btnSearchRoomClick() : void | Gửi từ khóa từ ô txtSearchRoom sang Controller để lọc danh sách phòng. |  | + tblPendingRoomsClick(roomId : int) : void | Lưu lại trạng thái/ID của phòng mà nhân viên vừa click chọn trên bảng. |  | + btnCreateDamageReportClick() : void | Kiểm tra xem nhân viên đã chọn phòng chưa, nếu rồi thì mở giao diện DamageReportView và truyền ID phòng đó sang. |  | + displayPendingRooms(rooms : List<Room>) : void | Nhận danh sách phòng từ Controller và đổ dữ liệu lên bảng tblPendingRooms. |  | + showMessage(msg : String) : void | Hiển thị popup cảnh báo (VD: "Vui lòng chọn phòng trước"). |  | + SearchRoomPage() : void | Hàm khởi tạo.DamageReportPage | Thuộc tính | - lblRoomName : Label | Hiển thị dòng chữ thông báo phòng đang được lập báo cáo. |  | - txtFacilityName : TextBox | Ô nhập tên csvc để tìm kiếm nhanh. |  | - btnSearchFacility : Button | Nút nhấn để tìm kiếm tài sản trong kho. |  | - tblFacilities : Table | Bảng danh sách csvc. |  | - tblDamageDetails : Table | Bảng hiển thị danh sách các tài sản đã bị khách làm hỏng, kèm cột cho phép nhập số lượng hỏng. |  | - btnSaveReport : Button | Nút chốt lại danh sách đồ hỏng và gửi dữ liệu đi lưu. | Phương thức | + formLoad() : void | Gọi FacilityController lấy danh mục tài sản mặc định đưa lên bảng tblFacilities. |  | + btnSearchFacilityClick() : void | Hàm bắt sự kiện ấn nút tìm. |  | + tblFacilitiesClick(FacilityId : int) : void | Chức năng thêm một tài sản từ bảng danh mục sang bảng chi tiết đồ hỏng tblDamageDetails khi nhân viên click chọn. |  | + btnSaveReportClick() : void | Hàm bắt sự kiện ấn nút lưu. |  | + displayFacilities(facilities : List<Facility>) : void | Đổ dữ liệu danh mục tài sản lên bảng. |  | + displayDamageCart(details : List<Damage_detail>) : void | Cập nhật liên tục bảng chi tiết đồ hỏng mỗi khi nhân viên thêm món đồ hoặc thay đổi số lượng. |  | + showMessage(msg : String) : void | Hiện thông báo lỗi hoặc xác nhận. |  | + DamageReportPage() : void | Hàm khởi tạo.ConfirmReportPage | Thuộc tính | - lblMessage : Label | Dòng chữ thông báo kết quả |  | - btnConfirm : Button | Nút OK để xác nhận đã đọc thông báo. | Phương thức | + btnConfirmClick() : void | Hàm bắt sự kiện click nút OK. |  | + ConfirmReportPage() : void | Hàm khởi tạo.
Tầng điều khiển:

Lớp | Phương thức | Chức năngRoomController | + searchPendingRoom(keyword : String) : List<Room> | Tiếp nhận từ khóa từ giao diện, truy vấn CSDL để tìm các phòng đang chờ thanh toán khớp với tên, trả về danh sách cho View hiển thị.FacilityController | + searchFacility(keyword : String) : List<Facility> | Truy vấn cơ sở dữ liệu bảng Tài sản để lấy ra danh mục các trang thiết bị có tên khớp với từ khóa tìm kiếm. | + getAllFacility() : List<Facility> | Được gọi bởi formLoad() của DamageReportPage để hiển thị danh sách tài sản.DamageReportController | + saveDamageReport(report : DamageReport) : boolean | Nhận đối tượng báo cáo từ View, kiểm tra tính hợp lệ của dữ liệu, sau đó gọi xuống tầng Entity để tiến hành lưu dữ liệu vào các bảng DamageReport và Damage_detail. | + updateReceipt(receiptId : int, totalFine : float) : boolean | Sau khi hàm saveDamageReport chạy thành công, hàm này sẽ lấy tổng số tiền phạt của báo cáo đó và gọi sang Entity Room_receipt để cộng dồn tiền đền bù vào hóa đơn của phòng.

Tầng thực thể: Employee, Facility, Damage_report, Room, Damage_detail, Room_receipt.

c) Chức năng quản lý menu
Tầng giao diện:

Lớp | Thành phần | Chi tiết thành phần | Chức năngManagerHomePage | Thuộc tính | - btnManageMenu : Button | Nút nhấn để mở phân hệ quản lý thực đơn. | Phương thức | + btnManageMenuClick() : void | Sự kiện click nút, điều hướng hệ thống mở giao diện MenuView. |  | + ManagerHomePage() : void | Hàm khởi tạo.MenuPage | Thuộc tính | - txtProductName : TextBox | Ô nhập tên sản phẩm để tìm kiếm. |  | - btnSearchProduct : Button | Nút kích hoạt lệnh tìm kiếm. |  | - tblProducts : Table | Bảng hiển thị danh sách sản phẩm. |  | - btnAdd : Button | Nút mở giao diện thêm sản phẩm mới. |  | - btnEdit : Button | Nút mở giao diện sửa thông tin sản phẩm (chỉ bấm được khi đã chọn 1 dòng trên bảng). |  | - btnDelete : Button | Nút xóa sản phẩm đã chọn khỏi cơ sở dữ liệu. | Phương thức | + formLoad() : void | Gọi Controller lấy toàn bộ danh sách sản phẩm khi vừa mở trang. |  | + btnSearchClick() : void | Truyền từ khóa tìm kiếm sang Controller để lọc danh sách. |  | + tblProductsClick(productId : int) : void | Lấy ID của sản phẩm đang được click chọn trên bảng để chuẩn bị cho thao tác Sửa hoặc Xóa. |  | + btnAddClick() : void | Mở giao diện thêm sản phẩm (với trường hợp thêm sản phẩm) |  | + btnEditClick() : void | Mở giao diện EditMenuView ở trạng thái "Cập nhật" (đẩy thông tin của sản phẩm vừa chọn sang để điền sẵn vào các ô). |  | + btnDeleteClick() : void | Gọi Controller thực thi lệnh xóa sản phẩm đang chọn, sau đó làm mới lại bảng. |  | + displayProducts(products : List<Product>) : void | Đổ dữ liệu danh sách sản phẩm lên bảng tblProducts. |  | + showMessage(msg : String) : void | Hiển thị thông báo (VD: "Xóa thành công" hoặc "Vui lòng chọn sản phẩm cần sửa"). |  | + MenuPage() : void | Hàm khởi tạo.EditMenuPage | Thuộc tính | - lblId : Label | Hiển thị Id của sản phẩm (không thể sửa) |  | - txtCategory : TextBox | Ô nhập/chọn danh mục (VD: Đồ ăn, Đồ uống). |  | - txtName : TextBox | Ô nhập tên sản phẩm. |  | - txtUnit : TextBox | Ô nhập đơn vị tính. |  | - txtPrice : TextBox | Ô nhập giá bán. |  | - txtCurrentStock : TextBox | Ô nhập số lượng tồn kho hiện tại. |  | - txtSafetyStock : TextBox | Ô nhập số lượng tồn kho an toàn. |  | - btnSave : Button | Nút lưu thông tin. | Phương thức | + formLoad(productId : int) : void | Truyền vào Id của sản phẩm để lấy thông tin sản phẩm tương ứng. |  | + btnSaveClick() : void | Thu thập dữ liệu từ tất cả các ô TextBox, đóng gói thành một đối tượng Product, và gọi Controller để lưu trữ. |  | + showMessage(msg : String) : void | Thông báo kết quả lưu ("Thành công" hoặc "Lỗi dữ liệu"). |  | + EditMenuPage() : void | Hàm khởi tạo.

Tầng điều khiển:

Lớp | Phương thức | Chức năngProductController | + getAllProducts() : List<Product> | Truy vấn CSDL trả về toàn bộ thực đơn. | + searchProduct(keyword : String) : List<Product> | Lọc sản phẩm theo tên hoặc danh mục. | + getProductById(id : int) : Product | Lấy chi tiết 1 sản phẩm để hiển thị lên form EditMenuView. | + updateProduct(product : Product) : boolean | Hàm cập nhật thông tin sản phẩm | + addProduct(product : Product) : boolean | Hàm thêm sản phẩm | + deleteProduct(id : int) : boolean | Xóa sản phẩm khỏi hệ thống.
Tầng thực thể: Employee, Product.

d) Chức năng quản lý kho
Tầng giao diện:

Lớp | Thành phần | Chi tiết thành phần | Chức năngManagerHomePage | Thuộc tính | - btnManageWarehouse : Button | Nút nhấn để mở phân hệ quản lý kho. | Phương thức | + btnManageWarehouseClick() : void | Sự kiện click để hệ thống mở giao diện WarehouseManageView. |  | + ManagerHomePage() : void | Hàm khởi tạo.WarehouseManagePage | Thuộc tính | - tblProducts : Table | Bảng hiển thị danh sách sản phẩm. |  | - btnImport : Button | Nút kích hoạt quy trình nhập hàng mới. | Phương thức | + formLoad() : void | Lấy danh sách tồn kho từ CSDL đổ lên bảng. |  | + btnImportClick() : void | Mở giao diện SearchProviderView để bắt đầu quy trình chọn nhà cung cấp. |  | + displayProducts(products : List<Product>) : void | Hàm render dữ liệu lên bảng. |  | + WarehouseManagePage() : void | Hàm khởi tạo.SearchProviderPage | Thuộc tính | - txtProviderName : TextBox | Ô nhập từ khóa tìm kiếm nhà cung cấp. |  | - btnSearch : Button | Nút tìm kiếm. |  | - tblProviders : Table | Bảng danh sách các nhà cung cấp thỏa mãn từ khóa. |  | - btnCreateImportReceipt : Button | Nút xác nhận chọn nhà cung cấp và chuyển sang bước tạo phiếu nhập. | Phương thức | + formLoad() : void | Load danh sách nhà cung cấp mặc định. |  | + btnSearchClick() : void | Gọi Controller để lọc nhà cung cấp. |  | + tblProvidersClick(providerId : int) : void | Lưu lại ID của nhà cung cấp vừa được chọn trên bảng. |  | + btnCreateImportReceiptClick() : void | Mở giao diện ImportReceiptView và truyền thông tin nhà cung cấp sang. |  | + displayProviders(providers : List<Provider>) : void | Đổ dữ liệu lên bảng. |  | + SearchProviderPage() : void | Hàm khởi tạo.ImportReceiptPage | Thuộc tính | - lblProviderName : Label | Hiển thị tên nhà cung cấp đang chọn. |  | - dtpImportDate : DatePicker | Bộ chọn ngày nhập hàng (mặc định là ngày hôm nay). |  | - txtProductName : TextBox | Ô tìm kiếm mặt hàng |  | - btnSearch : Button | Nút tìm kiếm mặt hàng. |  | - tblProducts : Table | Bảng danh mục sản phẩm |  | - txtQuantity : TextBox | Ô nhập số lượng nhập |  | - txtUnitCost : TextBox | Ô nhập giá nhập. |  | - btnAdd : Button | Nút thêm mặt hàng vào phiếu nhập |  | - tblImportDetails : Table | Bảng giỏ hàng phiếu nhập |  | - lblTotalCost : Label | Hiển thị tổng tiền của phiếu nhập. |  | - btnSave : Button | Nút chốt phiếu nhập. | Phương thức | + formLoad() : void | Load danh mục sản phẩm lên bảng trên. |  | + btnSearchClick() : void | Lọc sản phẩm theo tên. |  | + btnAddClick() : void | Lấy số lượng và giá nhập, tính thành tiền và đẩy xuống bảng tblImportDetails. |  | + btnSaveClick() : void | Đóng gói dữ liệu thành phiếu nhập và gọi Controller. |  | + displayProducts(products : List<Product>) : void | Vẽ dữ liệu bảng Product. |  | + displayImportDetails(details : List<Import_detail>) : void | Vẽ dữ liệu bảng ImportDetails. |  | + updateTotalCost() : void | Hàm tự động tính toán tổng các dòng line_total và cập nhật lên lblTotalCost. |  | + showMessage(msg : String) : void | Hiện thông báo. |  | + ImportReceiptPage() : void | Hàm khởi tạo.
Tầng điều khiển:

Lớp | Phương thức | Chức năngProviderController | + searchProvider(keyword : String) : List<Provider> | Tìm kiếm thông tin nhà cung cấp trong CSDL | + getAllProviders() : List<Provider> | Truy vấn CSDL trả về toàn bộ nhà cung cấp.ProductController | + searchProduct(keyword : String) : List<Product> | Nhận yêu cầu từ btnSearchClick của form nhập kho để gọi xuống Entity Product | + getAllProducts() : List<Product> | Truy vấn CSDL trả về toàn bộ sản phẩm.ImportController | + saveImportReceipt(receipt : Import_receipt) : boolean | Lưu phiếu nhập kho. | + updateProductStock(productId : int, addedQuantity : int) : boolean | Hàm nhận trách nhiệm gọi xuống Entity Product để cộng dồn tồn kho sau khi lưu phiếu nhập thành công.
Tầng thực thể: Employee, Provider, Import_receipt, Product, Import_detail.


3.3. Sơ đồ lớp thiết kế
a) Chức năng tạo order


b) Chức năng báo cáo tình trạng hàng hóa


c) Chức năng quản lý menu


d) Chức năng quản lý kho


4. Thiết kế động
4.1. Chức năng quản lý order
Nhân viên nhập username, password trên giao diện LoginPage và nhấn nút Login.
Giao diện LoginPage gọi phương thức btnLoginClick().
LoginPage gửi thông tin đăng nhập sang lớp LoginController thông qua hàm checkLogin(username, password).
LoginController gọi thực thể Employee để truy vấn cơ sở dữ liệu và xác thực.
Thực thể Employee trả kết quả xác thực về cho LoginController.
LoginController trả kết quả đăng nhập thành công lại cho LoginPage.
Hệ thống điều hướng, LoginPage gọi lớp StaffHomePage.
StaffHomePage hiển thị giao diện trang chủ cho nhân viên.
Nhân viên click nút "Quản lý order" trên màn hình.
StaffHomePage gọi hàm btnManageOrderClick().
StaffHomePage gọi lớp SearchRoomPage.
Lớp SearchRoomPage tự gọi hàm formLoad() của chính nó ngay khi vừa được tạo.
SearchRoomPage gọi sang lớp RoomController thông qua hàm getActiveRooms().
RoomController gọi thực thể Room truy vấn cơ sở dữ liệu để lấy danh sách các phòng đang hoạt động.
Thực thể Room trả kết quả danh sách phòng về cho RoomController.
RoomController trả danh sách phòng về cho giao diện SearchRoomPage.
SearchRoomPage tự gọi hàm nội bộ displayActiveRooms(rooms) để hiển thị danh sách phòng lên bảng.
Khách hàng đọc số phòng, nhân viên nhập tên phòng vào ô tìm kiếm và ấn nút Tìm kiếm.
SearchRoomPage gọi hàm btnSearchRoomClick(), đẩy thông tin sang hàm searchRoomByName(roomName) của RoomController.
RoomController gọi thực thể Room lọc dữ liệu và trả kết quả về để giao diện cập nhật lại bảng.
Nhân viên click chọn đúng phòng tương ứng trên bảng, sự kiện tblRoomClick(roomId) kích hoạt để hệ thống ghi nhớ ID phòng được chọn.
Nhân viên ấn nút "Tạo Order" để phục vụ phòng đó.
SearchRoomPage gọi lớp CreateOrderPage.
Lớp CreateOrderView tự gọi hàm formLoad() của chính nó.
CreateOrderPage gọi sang lớp ProductController thông qua hàm getAllProducts().
ProductController gọi thực thể Product lấy toàn bộ danh sách thực đơn từ cơ sở dữ liệu.
Thực thể Product trả kết quả về cho ProductController, sau đó Controller đẩy dữ liệu về cho CreateOrderPage.
CreateOrderPage tự gọi hàm displayProducts(products) hiển thị toàn bộ thực đơn lên bảng.
Khách chọn món, nhân viên nhập tên sản phẩm và click nút Tìm kiếm.
CreateOrderPage gọi hàm btnSearchProductClick(), đẩy từ khóa sang ProductController.searchProductByName(productName).
ProductController gọi thực thể Product lọc danh sách và trả kết quả về cho CreateOrderPage hiển thị.
Nhân viên ấn nút Thêm.
CreateOrderPage gọi hàm btnAddClick().
Hệ thống xử lý đưa món vào giỏ hàng nội bộ, sau đó CreateOrderPage tự gọi hàm displayOrderCart(orderDetails) để hiển thị món đó lên bảng giỏ hàng. (Bước 29 đến 34 lặp lại cho đến khi khách gọi xong món).
Sau khi hoàn thành việc chọn đồ, nhân viên click nút Lưu.
CreateOrderPage gọi hàm btnSaveClick(), đóng gói toàn bộ dữ liệu giỏ hàng thành đối tượng Order và gửi sang lớp OrderController thông qua hàm saveOrder(order).
OrderController gọi xuống thực thể Order thực thi phương thức addOrder() để lưu đơn hàng vào cơ sở dữ liệu.
Sau khi lưu Order thành công, OrderController tiếp tục tự gọi hàm updateReceipt(receiptId, totalOrderAmount) của chính nó.
Trong hàm này, OrderController gọi sang thực thể Room_receipt thông qua phương thức updateServiceFee(receiptId, feeAmount).
Thực thể Room_receipt thực thi câu lệnh UPDATE cơ sở dữ liệu để cộng dồn tiền phí dịch vụ và trả kết quả thành công về cho OrderController.
OrderController trả kết quả xử lý toàn bộ giao dịch thành công về cho CreateOrderPage.
Nhận được phản hồi, CreateOrderPage gọi lớp ConfirmOrderPage.
ConfirmOrderView hiển thị thông báo order thành công cho nhân viên.
Nhân viên thông báo lại cho khách và ấn nút Xác nhận.
ConfirmOrderView gọi hàm btnConfirmClick(), popup đóng lại và hệ thống quay trở về màn hình StaffHomeView.



4.2. Chức năng báo cáo tình trạng hàng hóa
Nhân viên nhập username, password trên giao diện LoginPage và nhấn nút Login.
Giao diện LoginPage tự gọi hàm btnLoginClick() của chính nó.
LoginPage gửi thông tin đăng nhập sang lớp LoginController thông qua hàm checkLogin(username, password).
LoginController gọi thực thể Employee để truy vấn cơ sở dữ liệu và xác thực.
Thực thể Employee trả kết quả xác thực về cho LoginController.
LoginController trả kết quả đăng nhập thành công lại cho LoginPage.
Hệ thống điều hướng, LoginPage gọi lớp StaffHomePage.
StaffHomePage hiển thị giao diện trang chủ cho nhân viên.
Nhân viên click nút "Báo cáo hư hỏng" trên màn hình.
StaffHomePage tự gọi hàm btnReportDamageClick().
StaffHomePage gọi lớp SearchRoomPage.
Lớp SearchRoomPage tự gọi hàm formLoad() của chính nó ngay khi vừa được tạo.
SearchRoomPage gọi sang lớp RoomController thông qua hàm searchPendingRooms(keyword).
RoomController gọi thực thể Room truy vấn cơ sở dữ liệu để lấy danh sách phòng.
Thực thể Room trả kết quả danh sách phòng về cho RoomController.
RoomController trả danh sách phòng về cho giao diện SearchRoomPage.
SearchRoomPage tự gọi hàm nội bộ displayPendingRooms(rooms) để đổ danh sách phòng lên bảng.
Nhân viên nhập tên/số phòng vào ô tìm kiếm và ấn nút Tìm kiếm.
SearchRoomPage tự gọi hàm btnSearchRoomClick(), sau đó đẩy từ khóa sang RoomController.searchPendingRooms(keyword) để lọc dữ liệu.
RoomController gọi thực thể Room lọc lại và trả danh sách mới về cho giao diện cập nhật bảng.
Nhân viên click chọn đúng phòng cần lập biên bản trên bảng, SearchRoomPage tự gọi tblPendingRoomsClick(roomId) để lưu lại ID phòng.
Nhân viên ấn nút Tạo báo cáo hư hỏng. SearchRoomPage tự gọi btnCreateDamageReportClick().
SearchRoomPage gọi lớp DamageReportPage.
Lớp DamageReportPage tự gọi hàm formLoad() của chính nó.
DamageReportPage gọi sang lớp FacilityController thông qua hàm searchFacility(keyword).
FacilityController gọi thực thể Facility lấy toàn bộ danh mục tài sản/thiết bị từ cơ sở dữ liệu.
Thực thể Facility trả kết quả về cho FacilityController, sau đó Controller đẩy dữ liệu về cho DamageReportPage.
DamageReportPage tự gọi hàm displayFacilities(facilities) hiển thị danh mục thiết bị lên bảng.
Nhân viên nhập tên thiết bị hỏng (ví dụ: "Cốc") và click nút Tìm kiếm.
DamageReportPage tự gọi hàm btnSearchFacilityClick(), đẩy từ khóa sang FacilityController.searchFacility(keyword) để lọc thiết bị.
Nhân viên click chọn thiết bị bị hỏng trên bảng. DamageReportPage tự gọi tblFacilitiesClick(facilityId).
Nhân viên nhập số lượng hỏng, hệ thống lưu vào danh sách nội bộ và DamageReportPage tự gọi displayDamageDetail(details) để hiển thị thiết bị đó lên bảng chi tiết (giỏ đồ hỏng). (Bước 29 đến 32 lặp lại cho đến khi nhập đủ các đồ bị hỏng).
Sau khi hoàn thành việc nhập biên bản, nhân viên click nút Lưu.
DamageReportPage tự gọi hàm btnSaveReportClick(), đóng gói dữ liệu thành đối tượng DamageReport và gửi sang lớp DamageReportController thông qua hàm saveDamageReport(report).
DamageReportController gọi xuống thực thể Damage_report để lưu thông tin biên bản vào CSDL.
Sau khi lưu biên bản thành công, DamageReportController tiếp tục tự gọi hàm updateReceipt(receiptId, totalFine) của chính nó.
Trong hàm này, DamageReportController gọi sang thực thể Room_receipt thông qua phương thức updateDamageFee(receiptId, fineAmount).
Thực thể Room_receipt thực thi câu lệnh UPDATE cơ sở dữ liệu để cộng dồn tiền đền bù vào hóa đơn của phòng và trả kết quả thành công về cho DamageReportController.
DamageReportController trả kết quả xử lý toàn bộ giao dịch thành công về cho DamageReportPage.
Nhận được phản hồi, DamageReportPage gọi lớp ConfirmReportPage.
ConfirmReportPage hiển thị thông báo báo cáo thành công cho nhân viên.
Nhân viên ấn nút Xác nhận.
ConfirmReportPage tự gọi hàm btnConfirmClick().
Lớp ConfirmReportPage gọi về lớp StaffHomePage.



4.3. Chức năng quản lý menu
Quản lý nhập username, password trên giao diện LoginPage và nhấn nút Login.
Giao diện LoginPage tự gọi sự kiện btnLoginClick() của chính nó.
LoginPage gửi thông tin đăng nhập sang lớp LoginController thông qua hàm checkLogin(username, password).
LoginController gọi xuống thực thể Employee để truy vấn cơ sở dữ liệu và xác thực.
Thực thể Employee trả kết quả xác thực thành công về cho LoginController.
LoginController trả kết quả đăng nhập thành công lại cho giao diện LoginPage.
LoginPage gọi lớp ManagerHomePage.
ManagerHomePage hiển thị giao diện trang chủ cho Quản lý.
Quản lý click nút "Quản lý Menu" trên màn hình.
ManagerHomePage tự gọi sự kiện btnManageMenuClick().
ManagerHomePage lớp MenuPage.
Lớp MenuPage tự gọi hàm formLoad() của chính nó ngay khi vừa được tạo.
MenuPage gọi sang lớp ProductController thông qua hàm getAllProducts().
ProductController gọi thực thể Product truy vấn cơ sở dữ liệu để lấy toàn bộ danh sách sản phẩm.
Thực thể Product trả danh sách sản phẩm về cho ProductController.
ProductController trả danh sách sản phẩm về cho giao diện MenuPage.
MenuPage tự gọi hàm nội bộ displayProducts(products) để đổ dữ liệu lên bảng danh sách.
Quản lý click chọn một sản phẩm cần sửa trên bảng danh sách.
MenuPage tự gọi sự kiện tblProductsClick(productId) của chính nó để hệ thống ghi nhớ ID của sản phẩm đang được chọn.
Quản lý ấn nút "Sửa" trên màn hình.
MenuPage tự gọi hàm btnEditClick().
MenuPage gọi lớp EditMenuPage.
Lớp EditMenuPage tự gọi hàm formLoad() của chính nó.
Để lấy thông tin cũ của sản phẩm, EditMenuPage gọi sang lớp ProductController thông qua hàm getProductById(productId).
ProductController gọi thực thể Product truy vấn cơ sở dữ liệu để lấy dữ liệu chi tiết của sản phẩm đó.
Thực thể Product trả kết quả bản ghi về cho ProductController.
ProductController trả dữ liệu về cho giao diện EditMenuPage.
EditMenuPage điền thông tin cũ của sản phẩm lên các ô TextBox để Quản lý nhìn thấy.
Quản lý tiến hành gõ/chỉnh sửa thông tin mới (ví dụ: đổi giá bán, sửa số lượng tồn kho...) trên các ô nhập liệu và ấn nút "Lưu".
EditMenuPage tự gọi hàm btnSaveClick().
EditMenuPage đóng gói toàn bộ thông tin mới thành đối tượng Product và gửi sang ProductController thông qua hàm updateProduct(product).
ProductController gọi xuống thực thể Product thực thi phương thức updateProduct(product) để chạy lệnh UPDATE dưới cơ sở dữ liệu.
Thực thể Product lưu thành công và trả kết quả (true) về cho ProductController.
ProductController trả kết quả xử lý thành công về cho giao diện EditMenuPage.
EditMenuPage tự gọi hàm showMessage(msg) để hiển thị popup thông báo "Cập nhật sản phẩm thành công".
EditMenuPage gọi lại lớp MenuPage.


4.4. Chức năng quản lý kho
Quản lý nhập username, password trên giao diện LoginPage và nhấn nút Login.
Giao diện LoginPage tự gọi sự kiện btnLoginClick() của chính nó.
LoginPage gửi thông tin đăng nhập sang lớp LoginController thông qua hàm checkLogin(username, password).
LoginController gọi xuống thực thể Employee để truy vấn cơ sở dữ liệu và xác thực.
Thực thể Employee trả kết quả xác thực thành công về cho LoginController.
LoginController trả kết quả đăng nhập thành công lại cho giao diện LoginPage.
LoginPage gọi lớp ManagerHomePage.
ManagerHomePage hiển thị giao diện trang chủ cho Quản lý.
Quản lý click nút "Quản lý Kho" trên màn hình.
ManagerHomePage tự gọi sự kiện btnManageWarehouseClick().
ManagerHomePage lớp WarehouseManagePage.
Lớp WarehouseManagePage tự gọi hàm formLoad() của chính nó ngay khi vừa được tạo.
WarehouseManagePage gọi sang lớp ProductController thông qua hàm getAllProducts().
ProductController gọi thực thể Product truy vấn cơ sở dữ liệu lấy toàn bộ danh sách sản phẩm kèm số lượng tồn kho hiện tại.
Thực thể Product trả danh sách về cho ProductController.
ProductController trả danh sách về cho giao diện WarehouseManagePage.
WarehouseManagePage tự gọi hàm nội bộ displayProduct(products) để đổ dữ liệu tình trạng kho lên bảng.
Quản lý nhận thấy có hàng sắp hết, liền ấn nút "Nhập kho".
WarehouseManagePage tự gọi sự kiện btnImportClick().
WarehouseManagePage gọi lớp SearchProviderPage.
Lớp SearchProviderPage tự gọi hàm formLoad() của chính nó.
SearchProviderPage gọi sang ProviderController thông qua hàm getAllProviders().
ProviderController gọi thực thể Provider lấy danh sách nhà cung cấp từ CSDL.
Thực thể Provider trả kết quả về cho Controller, Controller đẩy về giao diện.
SearchProviderPage tự gọi hàm displayProviders(providers) để hiển thị danh sách nhà cung cấp lên bảng.
Quản lý nhập tên nhà cung cấp và ấn nút Tìm kiếm. SearchProviderPage tự gọi btnSearchClick(), đẩy sang ProviderController.searchProvider(keyword) để lọc và cập nhật lại bảng.
Quản lý click chọn đúng nhà cung cấp giao lô hàng này trên bảng.
SearchProviderPage tự gọi sự kiện tblProvidersClick(providerId) để hệ thống ghi nhớ ID nhà cung cấp.
Quản lý ấn nút "Tạo phiếu nhập". SearchProviderPage tự gọi hàm btnCreateImportReceiptClick().
SearchProviderPage gọi lớp ImportReceiptPage.
Lớp ImportReceiptPage tự gọi hàm formLoad() của chính nó.
Để hiển thị danh mục sản phẩm cho quản lý chọn nhập, ImportReceiptPage gọi sang ProductController thông qua hàm getAllProducts().
ProductController gọi thực thể Product lấy danh sách, trả về Controller, rồi trả về View.
ImportReceiptPage tự gọi hàm displayProducts(products) hiển thị các món lên bảng trên cùng.
Quản lý nhập tên món cần tìm và ấn nút Tìm kiếm. ImportReceiptPage tự gọi btnSearchClick(), đẩy qua ProductController.searchProduct(keyword) để lọc.
Quản lý điền số lượng (txtQuantity) và giá nhập (txtUnitCost) trực tiếp vào dòng sản phẩm trên bảng, sau đó ấn nút Thêm.
ImportReceiptPage tự gọi hàm btnAddClick().
Hệ thống tính toán thành tiền, đưa món hàng vào bảng chi tiết phiếu nhập bên dưới, và ImportReceiptPage tự gọi tiếp hàm updateTotalCost() để cộng dồn hiển thị tổng tiền lô hàng lên nhãn lblTotalCost. (Bước 35 đến 38 lặp lại cho đến khi nhập xong toàn bộ các mặt hàng).
Quản lý ấn nút Lưu để chốt phiếu.
ImportReceiptPage tự gọi hàm btnSaveClick().
ImportReceiptPage đóng gói toàn bộ dữ liệu phiếu nhập và danh sách hàng hóa gửi sang ImportController thông qua hàm saveImportReceipt(receipt).
ImportController gọi xuống thực thể Import_receipt để thực thi lệnh lưu lịch sử nhập hàng vào cơ sở dữ liệu.
Ngay sau khi lưu phiếu thành công, ImportController tự động gọi hàm updateProductStock(productId, addedQuantity).
ImportController gọi sang thực thể Product để chạy lệnh UPDATE, cộng dồn số lượng hàng hóa mới vào thuộc tính current_stock dưới CSDL.
Thực thể Product cập nhật kho thành công, trả kết quả về cho ImportController.
ImportController trả kết quả hoàn tất toàn bộ quy trình về cho ImportReceiptPage.
ImportReceiptPage tự gọi hàm showMessage(msg) hiển thị thông báo "Nhập kho thành công!".
Quản lý click OK.
ImportReceiptPage gọi lại lớp ManagerHomePage.



IV. PHA CÀI ĐẶT VÀ KIỂM THỬ
1. Lập kế hoạch test

STT | Chức năng | Trường hợp cần test1 | Tạo order | Không tìm thấy phòng2 |  | Không tìm thấy sản phẩm3 |  | Tìm thấy phòng và có sản phẩm trong CSDL4 |  | Tồn kho sản phẩm không còn5 | Báo cáo tình trạng hàng | Cơ sở vật chất chưa có trong CSDL6 |  | Cơ sở vật chất đã có trong CSDL7 | Quản lý menu | Sản phẩm chưa có trong CSDL8 |  | Sản phẩm đã có trong CSDL9 | Quản lý kho | Không có nhà cung cấp trong CSDL10 |  | Có nhà cung cấp trong CSDL
2. Các test case cho từng chức năng
a) Chức năng tạo order
- Test case 1: Không tìm thấy phòng trong CSDL:CSDL trước khi test:
tblEmployee:

id | full_name | dob | tel | role | username | password | status1 | Nguyễn Gia Đức Trung | 10/09/2005 | 123456 | Quản lý | manager | trung@123 | Working2 | Trần Xuân Thành | 20/08/2005 | 112233 | Phục vụ | staff | thanh@123 | Working3 | Phạm Tuấn Anh | 14/01/2005 | 224466 | Phục vụ | staff | tuan@123 | Working4 | Vũ Hùng Anh | 03/01/2005 | 445566 | Lễ tân | receptionist | hanh@123 | Working
tblRoom:

id | name | type | price | capacity | status1 | 101 | Normal | 200,000 | 20 | Active2 | 102 | VIP | 350,000 | 25 | Active3 | 103 | Normal | 200,000 | 20 | Active4 | 104 | VIP | 350,000 | 25 | Active
tblProduct:

id | name | category | unit | price | current_stock | safety_stock1 | Bia Heniken | Đồ uống | Lon | 20,000 | 10 | 502 | Nước lọc | Đồ uống | Chai | 12,000 | 50 | 303 | Bim Bim | Đồ ăn | Gói | 10,000 | 80 | 50
tblRoomReceipt:

id | checkin_time | checkout_time | room_fee | service_fee | damage_fee | total_amount | status | employee_id | room_id1 | 01/01/2020 18:00 | 01/01/2020 21:00 | 200,000 | 166,000 | 0 | 366,000 | PAID | 4 | 12 | 01/01/2020 18:00 | 03/01/2020 21:00 | 350,000 | 0 | 0 | 350,000 | PAID | 4 | 23 | 02/01/2020 19:00 | 02/01/2020 21:00 | 350,000 | 250,000 | 100,000 | 700,000 | PAID | 4 | 2
tblOrder:

id | order_time | total_amount | status | room_receipt_id | employee_id1 | 01/01/2020 18:50 | 100,000 | Served | 1 | 22 | 01/01/2020 20:14 | 66,000 | Served | 1 | 23 | 02/01/2020 19:22 | 250,000 | Served | 3 | 2
tblOrderDetail:

id | order_id | product_id | quantity | unit_price | line_total1 | 1 | 1 | 5 | 20,000 | 100,0002 | 2 | 2 | 3 | 12,000 | 36,0003 | 2 | 3 | 10 | 10,000 | 30,0004 | 3 | 1 | 10 | 20,000 | 200,0005 | 3 | 3 | 5 | 10,000 | 50,000

Các bước thực hiện | Kết quả mong đợi1. Nhân viên phục vụ (id = 2) đã đăng nhập. | Giao diện tìm phòng đang hoạt động hiện ra, có ô nhập tên phòng và nút tìm.2. Nhập 107 và click nút tìm | Kết quả hiện lên:3. Click OK | Quay về giao diện chính của nhân viên phục vụ.
CSDL sau khi test: không có gì thay đổi.

- Test case 2: có phòng nhưng không tìm thấy sản phẩm.
CSDL trước khi test:
tblEmployee:

id | full_name | dob | tel | role | username | password | status1 | Nguyễn Gia Đức Trung | 10/09/2005 | 123456 | Quản lý | manager | trung@123 | Working2 | Trần Xuân Thành | 20/08/2005 | 112233 | Phục vụ | staff | thanh@123 | Working3 | Phạm Tuấn Anh | 14/01/2005 | 224466 | Phục vụ | staff | tuan@123 | Working4 | Vũ Hùng Anh | 03/01/2005 | 445566 | Lễ tân | receptionist | hanh@123 | Working
tblRoom:

id | name | type | price | capacity | status1 | 101 | Normal | 200,000 | 20 | Active2 | 102 | VIP | 3530,000 | 25 | Active3 | 103 | Normal | 200,000 | 20 | Active4 | 104 | VIP | 350,000 | 25 | Active
tblProduct:

id | name | category | unit | price | current_stock | safety_stock1 | Bia Heniken | Đồ uống | Lon | 20,000 | 10 | 502 | Nước lọc | Đồ uống | Chai | 12,000 | 50 | 303 | Bim Bim | Đồ ăn | Gói | 10,000 | 80 | 50
tblRoomReceipt:

id | checkin_time | checkout_time | room_fee | service_fee | damage_fee | total_amount | status | employee_id | room_id1 | 01/01/2020 18:00 | 01/01/2020 21:00 | 200,000 | 166,000 | 0 | 366,000 | PAID | 4 | 12 | 01/01/2020 18:00 | 03/01/2020 21:00 | 350,000 | 0 | 0 | 350,000 | PAID | 4 | 23 | 02/01/2020 19:00 | 02/01/2020 21:00 | 350,000 | 250,000 | 100,000 | 700,000 | PAID | 4 | 2
tblOrder:

id | order_time | total_amount | status | room_receipt_id | employee_id1 | 01/01/2020 18:50 | 100,000 | Served | 1 | 22 | 01/01/2020 20:14 | 66,000 | Served | 1 | 23 | 02/01/2020 19:22 | 250,000 | Served | 3 | 2
tblOrderDetail:

id | order_id | product_id | quantity | unit_price | line_total1 | 1 | 1 | 5 | 20,000 | 100,0002 | 2 | 2 | 3 | 12,000 | 36,0003 | 2 | 3 | 10 | 10,000 | 30,0004 | 3 | 1 | 10 | 20,000 | 200,0005 | 3 | 3 | 5 | 10,000 | 50,000

Các bước thực hiện | Kết quả mong đợi1. Nhân viên phục vụ (id = 2) đăng nhập thành công | Giao diện tìm phòng đang hoạt động hiện ra, có ô nhập tên phòng và nút tìm.2. Nhập 104 và click tìm | Kết quả hiện lên:3. Click vào phòng 104 và click nút tạo order | Giao diện “Tạo order” hiển thị gồm:
- Tên phòng
- Danh sách các sản phẩm
- Nút thêm
- Ô nhập tên sản phẩm
- Nút tìm.4. Nhập “Kem” | Kết quả hiện lên:5. Click OK | Quay về giao diện tạo order
CSDL sau khi test: không có gì thay đổi.

- Test case 3: Tìm thấy phòng và sản phẩm trong CSDL:
CSDL trước khi test:
tblEmployee:

id | full_name | dob | tel | role | username | password | status1 | Nguyễn Gia Đức Trung | 10/09/2005 | 123456 | Quản lý | manager | trung@123 | Working2 | Trần Xuân Thành | 20/08/2005 | 112233 | Phục vụ | staff | thanh@123 | Working3 | Phạm Tuấn Anh | 14/01/2005 | 224466 | Phục vụ | staff | tuan@123 | Working4 | Vũ Hùng Anh | 03/01/2005 | 445566 | Phục vụ | staff | hanh@123 | Working
tblRoom:

id | name | type | price | capacity | status1 | 101 | Normal | 200,000 | 20 | Active2 | 102 | VIP | 350,000 | 25 | Active3 | 103 | Normal | 200,000 | 20 | Active4 | 104 | VIP | 350,000 | 25 | Active
tblProduct:

id | name | category | unit | price | current_stock | safety_stock1 | Bia Heniken | Đồ uống | Lon | 20,000 | 10 | 502 | Nước lọc | Đồ uống | Chai | 12,000 | 50 | 303 | Bim Bim | Đồ ăn | Gói | 10,000 | 80 | 50
tblRoomReceipt:

id | checkin_time | checkout_time | room_fee | service_fee | damage_fee | total_amount | status | employee_id | room_id1 | 01/01/2020 18:00 | 01/01/2020 21:00 | 200,000 | 166,000 | 0 | 366,000 | PAID | 4 | 12 | 01/01/2020 18:00 | 03/01/2020 21:00 | 350,000 | 0 | 0 | 350,000 | PAID | 4 | 23 | 02/01/2020 19:00 | 02/01/2020 21:00 | 350,000 | 250,000 | 100,000 | 700,000 | PAID | 4 | 2
tblOrder:

id | order_time | total_amount | status | room_receipt_id | employee_id1 | 01/01/2020 18:50 | 100,000 | Served | 1 | 22 | 01/01/2020 20:14 | 66,000 | Served | 1 | 23 | 02/01/2020 19:22 | 250,000 | Served | 3 | 2
tblOrderDetail:

id | order_id | product_id | quantity | unit_price | line_total1 | 1 | 1 | 5 | 20,000 | 100,0002 | 2 | 2 | 3 | 12,000 | 36,0003 | 2 | 3 | 10 | 10,000 | 30,0004 | 3 | 1 | 10 | 20,000 | 200,0005 | 3 | 3 | 5 | 10,000 | 50,000


Các bước thực hiện | Kết quả mong đợi1. Nhân viên phục vụ (id = 3) đăng nhập thành công | Giao diện hiện lên, bao gồm:
- Danh sách phòng đang hoạt động, 
- Có ô nhập tên phòng
- Nút tìm.2. Nhập 104 và click tìm | Kết quả hiện lên:3. Click vào phòng 104 và click nút tạo order | Giao diện hiển thị bao gồm:
- Tên phòng
- Danh sách các sản phẩm
- Nút thêm, ô nhập tên sản phẩm và nút tìm.4. Nhập “Bia Heniken”, “Bim Bim” | Kết quả hiện lên:5. Click nút “THÊM” | Kết quả hiện lên:6. Click nút gửi order | Kết quả hiện lên:7. Click nút OK | Lưu order vào CSDL và quay trở về trang chủ của nhân viên phục vụ.
CSDL sau khi test:
tblProduct:

id | name | category | unit | price | current_stock | safety_stock1 | Bia Heniken | Đồ uống | Lon | 20,000 | 5 | 502 | Nước lọc | Đồ uống | Chai | 12,000 | 50 | 303 | Bim Bim | Đồ ăn | Gói | 10,000 | 76 | 50
tblRoomReceipt:

id | checkin_time | checkout_time | room_fee | service_fee | damage_fee | total_amount | status | employee_id | room_id1 | 01/01/2020 18:00 | 01/01/2020 21:00 | 200,000 | 166,000 | 0 | 366,000 | PAID | 4 | 12 | 01/01/2020 18:00 | 03/01/2020 21:00 | 350,000 | 0 | 0 | 350,000 | PAID | 4 | 23 | 02/01/2020 19:00 | 02/01/2020 21:00 | 350,000 | 250,000 | 100,000 | 700,000 | PAID | 4 | 24 | 03/01/2020 09:00 | 03/01/2020 11:00 | 200,000 | 148,000 | 0 | 348,000 | UNPAID | 4 | 3
tblOrder:

id | order_time | total_amount | status | room_receipt_id | employee_id1 | 01/01/2020 18:50 | 100,000 | Served | 1 | 22 | 01/01/2020 20:14 | 66,000 | Served | 1 | 23 | 02/01/2020 19:22 | 250,000 | Served | 3 | 24 | 03/01/2020 09:14 | 148,000 | Preparing | 4 | 3
tblOrderDetail:

id | order_id | product_id | quantity | unit_price | line_total1 | 1 | 1 | 5 | 20,000 | 100,0002 | 2 | 2 | 3 | 12,000 | 36,0003 | 2 | 3 | 10 | 10,000 | 30,0004 | 3 | 1 | 10 | 20,000 | 200,0005 | 3 | 3 | 5 | 10,000 | 50,0006 | 4 | 1 | 5 | 20,000 | 100,0007 | 4 | 3 | 4 | 12,000 | 48,000

- Test case 4: ấn nút thêm khi đã quá số lượng tồn kho của sản phẩm
CSDL trước khi test:
tblEmployee:

id | full_name | dob | tel | role | username | password | status1 | Nguyễn Gia Đức Trung | 10/09/2005 | 123456 | Quản lý | manager | trung@123 | Working2 | Trần Xuân Thành | 20/08/2005 | 112233 | Phục vụ | staff | thanh@123 | Working3 | Phạm Tuấn Anh | 14/01/2005 | 224466 | Phục vụ | staff | tuan@123 | Working4 | Vũ Hùng Anh | 03/01/2005 | 445566 | Phục vụ | staff | hanh@123 | Working
tblRoom:

id | name | type | price | capacity | status1 | 101 | Normal | 200,000 | 20 | Active2 | 102 | VIP | 350,000 | 25 | Active3 | 103 | Normal | 200,000 | 20 | Active4 | 104 | VIP | 350,000 | 25 | Active
tblProduct:

id | name | category | unit | price | current_stock | safety_stock1 | Bia Heniken | Đồ uống | Lon | 20,000 | 10 | 502 | Nước lọc | Đồ uống | Chai | 12,000 | 50 | 303 | Bim Bim | Đồ ăn | Gói | 10,000 | 80 | 50
tblRoomReceipt:

id | checkin_time | checkout_time | room_fee | service_fee | damage_fee | total_amount | status | employee_id | room_id1 | 01/01/2020 18:00 | 01/01/2020 21:00 | 200,000 | 166,000 | 0 | 366,000 | PAID | 4 | 12 | 01/01/2020 18:00 | 03/01/2020 21:00 | 350,000 | 0 | 0 | 350,000 | PAID | 4 | 23 | 02/01/2020 19:00 | 02/01/2020 21:00 | 350,000 | 250,000 | 100,000 | 700,000 | PAID | 4 | 2
tblOrder:

id | order_time | total_amount | status | room_receipt_id | employee_id1 | 01/01/2020 18:50 | 100,000 | Served | 1 | 22 | 01/01/2020 20:14 | 66,000 | Served | 1 | 23 | 02/01/2020 19:22 | 250,000 | Served | 3 | 2
tblOrderDetail:

id | order_id | product_id | quantity | unit_price | line_total1 | 1 | 1 | 5 | 20,000 | 100,0002 | 2 | 2 | 3 | 12,000 | 36,0003 | 2 | 3 | 10 | 10,000 | 30,0004 | 3 | 1 | 10 | 20,000 | 200,0005 | 3 | 3 | 5 | 10,000 | 50,000

Các bước thực hiện | Kết quả mong đợi1. Nhân viên phục vụ (id = 3) đăng nhập thành công | Giao diện hiện lên, bao gồm:
- Danh sách phòng đang hoạt động, 
- Có ô nhập tên phòng
- Nút tìm.2. Nhập 104 và click tìm | Kết quả hiện lên:3. Click vào phòng 104 và click nút tạo order | Giao diện hiển thị bao gồm:
- Tên phòng
- Danh sách các sản phẩm
- Nút thêm, ô nhập tên sản phẩm và nút tìm.4. Nhập “Bia Heniken”, “Bim Bim” | Kết quả hiện lên:5. Click nút “THÊM” | Kết quả hiện lên:6. Tiếp tục click nút “THÊM”” hoặc click “+” | Kết quả hiện lên:7. Click OK | Quay về giao diện tạo order.
CSDL sau khi test: không có gì thay đổi.

b) Chức năng Báo cáo tình trạng hàng
- Test case 1: cơ sở vật chất chưa có trong CSDL
CSDL trước khi test:
tblEmployee:

id | full_name | dob | tel | role | username | password | status1 | Nguyễn Gia Đức Trung | 10/09/2005 | 123456 | Quản lý | manager | trung@123 | Working2 | Trần Xuân Thành | 20/08/2005 | 112233 | Phục vụ | staff | thanh@123 | Working3 | Phạm Tuấn Anh | 14/01/2005 | 224466 | Phục vụ | staff | tuan@123 | Working4 | Vũ Hùng Anh | 03/01/2005 | 445566 | Phục vụ | staff | hanh@123 | Working
tblRoom:

id | name | type | price | capacity | status1 | 101 | Normal | 200,000 | 20 | Active2 | 102 | VIP | 350,000 | 25 | Active3 | 103 | Normal | 200,000 | 20 | Active4 | 104 | VIP | 350,000 | 25 | Active
tblFacility:

id | name | unit | compensation_price | stock1 | Cốc thủy tinh | Cái | 100,000 | 402 | Đĩa thủy tinh | Cái | 200,000 | 403 | Micro | Cái | 1,500,000 | 20
tblRoomReceipt:

id | checkin_time | checkout_time | room_fee | service_fee | damage_fee | total_amount | status | employee_id | room_id1 | 01/01/2020 18:00 | 01/01/2020 21:00 | 200,000 | 166,000 | 0 | 366,000 | PAID | 4 | 12 | 01/01/2020 18:00 | 03/01/2020 21:00 | 350,000 | 0 | 0 | 350,000 | PAID | 4 | 23 | 02/01/2020 19:00 | 02/01/2020 21:00 | 350,000 | 250,000 | 100,000 | 700,000 | PAID | 4 | 2
tblDamageReport:

id | report_time | total_fine | room_receipt_id | employee_id1 | 02/01/2020 21:05 | 100,000 | 3 | 3
tblDamageDetail:

id | facility_id | room_receipt_id | quantity | unit_fine_amount | line_total1 | 1 | 3 | 1 | 100,000 | 100,000

Các bước thực hiện | Kết quả mong đợi1. Nhân viên phục vụ (id = 2) đăng nhập thành công và ấn vào chức năng báo cáo tình trạng hàng. | Giao diện hiện lên gồm:
- Các phòng đang ở trạng thái chờ dọn.
- Ô nhập tên phòng
- Nút tìm2. Nhập 104 và click tìm | Kết quả hiện lên:3. Click vào phòng 104 và click nút tạo báo cáo | Giao diện hiển thị bao gồm:
- Tên phòng
- Danh sách các cơ sở vật chất
- Ô nhập tên csvc
- Nút tìm
- Ô nhập số lượng4. Nhập “Thìa” và click tìm | Giao diện hiện lên:5. Click OK | Quay về giao diện báo cáo.
CSDL sau khi test: không có gì thay đổi.

- Test case 2: cơ sở vật chất có trong CSDL:
CSDL trước khi test:
tblEmployee:

id | full_name | dob | tel | role | username | password | status1 | Nguyễn Gia Đức Trung | 10/09/2005 | 123456 | Quản lý | manager | trung@123 | Working2 | Trần Xuân Thành | 20/08/2005 | 112233 | Phục vụ | staff | thanh@123 | Working3 | Phạm Tuấn Anh | 14/01/2005 | 224466 | Phục vụ | staff | tuan@123 | Working4 | Vũ Hùng Anh | 03/01/2005 | 445566 | Phục vụ | staff | hanh@123 | Working
tblRoom:

id | name | type | price | capacity | status1 | 101 | Normal | 200,000 | 20 | Active2 | 102 | VIP | 350,000 | 25 | Active3 | 103 | Normal | 200,000 | 20 | Active4 | 104 | VIP | 350,000 | 25 | Active
tblFacility:

id | name | unit | compensation_price | stock1 | Cốc thủy tinh | Cái | 100,000 | 402 | Đĩa thủy tinh | Cái | 200,000 | 403 | Micro | Cái | 1,500,000 | 20
tblRoomReceipt:

id | checkin_time | checkout_time | room_fee | service_fee | damage_fee | total_amount | status | employee_id | room_id1 | 01/01/2020 18:00 | 01/01/2020 21:00 | 200,000 | 166,000 | 0 | 366,000 | PAID | 4 | 12 | 01/01/2020 18:00 | 03/01/2020 21:00 | 350,000 | 0 | 0 | 350,000 | PAID | 4 | 23 | 02/01/2020 19:00 | 02/01/2020 21:00 | 350,000 | 250,000 | 100,000 | 700,000 | PAID | 4 | 2
tblDamageReport:

id | report_time | total_fine | room_receipt_id | employee_id1 | 02/01/2020 21:05 | 100,000 | 3 | 3
tblDamageDetail:

id | facility_id | room_receipt_id | quantity | unit_fine_amount | line_total1 | 1 | 3 | 1 | 100,000 | 100,000

Các bước thực hiện | Kết quả mong đợi1. Nhân viên phục vụ (id = 2) đăng nhập thành công và ấn vào chức năng báo cáo tình trạng hàng. | Giao diện hiện lên gồm:
- Các phòng đang ở trạng thái chờ dọn.
- Ô nhập tên phòng
- Nút tìm2. Nhập 104 và click tìm | Kết quả hiện lên:3. Click vào phòng 104 và click nút tạo báo cáo | Giao diện hiển thị bao gồm:
- Tên phòng
- Danh sách các cơ sở vật chất
- Ô nhập tên csvc
- Nút tìm
- Ô nhập số lượng4. Nhập “Cốc thủy tinh” và click tìm | Giao diện hiện lên:5. Nhập số lượng “2” và click lưu | Kết quả hiện lên:6. Click OK | Hệ thống tự động trừ số lượng vào bảng tblFacility và quay về giao diện chính của nhân viên phục vụ.
CSDL sau khi test:
tblFacility:

id | name | unit | compensation_price | stock1 | Cốc thủy tinh | Cái | 100,000 | 382 | Đĩa thủy tinh | Cái | 200,000 | 403 | Micro | Cái | 1,500,000 | 20

tblRoomReceipt:

id | checkin_time | checkout_time | room_fee | service_fee | damage_fee | total_amount | status | employee_id | room_id1 | 01/01/2020 18:00 | 01/01/2020 21:00 | 200,000 | 166,000 | 0 | 366,000 | PAID | 4 | 12 | 01/01/2020 18:00 | 03/01/2020 21:00 | 350,000 | 0 | 0 | 350,000 | PAID | 4 | 23 | 02/01/2020 19:00 | 02/01/2020 21:00 | 350,000 | 250,000 | 100,000 | 700,000 | PAID | 4 | 24 | 03/01/2020 09:00 | 03/01/2020 11:00 | 200,000 | 148,000 | 100,000 | 448,000 | UNPAID | 4 | 3
tblDamageReport:

id | report_time | total_fine | room_receipt_id | employee_id1 | 02/01/2020 21:05 | 100,000 | 3 | 32 | 03/01/2020 11:10 | 100,000 | 4 | 2
tblDamageDetail:

id | facility_id | room_receipt_id | quantity | unit_fine_amount | line_total1 | 1 | 3 | 1 | 100,000 | 100,0002 | 1 | 4 | 1 | 100,000 | 100,000

c) Chức năng quản lý menu
- Test case 1: sản phẩm chưa có trong CSDL
CSDL trước khi test:
tblEmployee:

id | full_name | dob | tel | role | username | password | status1 | Nguyễn Gia Đức Trung | 10/09/2005 | 123456 | Quản lý | manager | trung@123 | Working2 | Trần Xuân Thành | 20/08/2005 | 112233 | Phục vụ | staff | thanh@123 | Working3 | Phạm Tuấn Anh | 14/01/2005 | 224466 | Phục vụ | staff | tuan@123 | Working4 | Vũ Hùng Anh | 03/01/2005 | 445566 | Phục vụ | staff | hanh@123 | Working
tblProduct:

id | name | category | unit | price | current_stock | safety_stock1 | Bia Heniken | Đồ uống | Lon | 20,000 | 10 | 502 | Nước lọc | Đồ uống | Chai | 12,000 | 50 | 303 | Bim Bim | Đồ ăn | Gói | 10,000 | 80 | 50

Các bước thực hiện | Kết quả mong đợi1. Nhân viên quản lý (id = 1) đăng nhập thành công và click vào chức năng quản lý menu. | Giao diện hiển thị:
- Danh sách các sản phẩm
- Ô nhập tên sản phẩm
- Nút tìm
- Nút thêm
- Nút sửa
- Nút xóa2. Nhập “Cơm rang” và ấn tìm kiếm | Kết quả hiển thị:
CSDL sau khi test: không có gì thay đổi.

- Test case 2: có sản phẩm trong CSDL:
CSDL trước khi test:
tblProduct:

id | name | category | unit | price | current_stock | safety_stock1 | Bia Heniken | Đồ uống | Lon | 20,000 | 10 | 502 | Nước lọc | Đồ uống | Chai | 12,000 | 50 | 303 | Bim Bim | Đồ ăn | Gói | 10,000 | 80 | 50

Các bước thực hiện | Kết quả mong muốn1. Nhân viên quản lý (id = 1) đăng nhập thành công và click vào chức năng quản lý menu. | Giao diện hiển thị:
- Danh sách các sản phẩm
- Ô nhập tên sản phẩm
- Nút tìm
- Nút thêm
- Nút sửa
- Nút xóa2. Nhập “Bia Heniken” và click tìm kiếm | Giao diện hiển thị:3. Click vào chức năng “Sửa” | Giao diện hiển thị:4. Sửa giá sản phẩm thành “25,000” | Giao diện hiển thị:5. Click “Lưu” | Thông báo hiện lên “Sửa thành công”6. Click OK | Hệ thống cập nhật lại vào CSDL, về lại giao diện Menu.
CSDL sau khi test: chỉ có tblProduct thay đổi
tblProduct:

id | name | category | unit | price | current_stock | safety_stock1 | Bia Heniken | Đồ uống | Lon | 25,000 | 10 | 502 | Nước lọc | Đồ uống | Chai | 12,000 | 50 | 303 | Bim Bim | Đồ ăn | Gói | 10,000 | 80 | 50
d) Chức năng quản lý kho
- Test case 1: không có tên nhà cung cấp trong CSDL
CSDL trước khi test:
tblEmployee:

id | full_name | dob | tel | role | username | password | status1 | Nguyễn Gia Đức Trung | 10/09/2005 | 123456 | Quản lý | manager | trung@123 | Working2 | Trần Xuân Thành | 20/08/2005 | 112233 | Phục vụ | staff | thanh@123 | Working3 | Phạm Tuấn Anh | 14/01/2005 | 224466 | Phục vụ | staff | tuan@123 | Working4 | Vũ Hùng Anh | 03/01/2005 | 445566 | Phục vụ | staff | hanh@123 | Working
tblProvider:

id | name | tel | address1 | Công ty cổ phần bia-rượu-nước giải khát | 123456 | abcd2 | Công ty Cổ phần Acecook Việt Nam | 246357 | xyzt

Các bước thực hiện | Kết quả mong muốn1. Nhân viên quản lý đăng nhập thành công và click vào chức năng quản lý kho. | Giao diện hiển thị danh sách thông tin các sản phẩm và có nút nhập hàng.2. Quản lý thấy một số sản phẩm sắp hết (báo đỏ) và click vào nút nhập hàng. | Giao diện hiển thị:
- Danh sách các nhà cung cấp
- Ô nhập tên nhà cung cấp
- Nút tìm
- Nút tạo phiếu nhập hàng3. Quản lý nhập “Thực phẩm Tân Việt” | Giao diện hiển thị:
CSDL sau khi test: không có gì thay đổi

- Test case 2: đã có tên nhà cung cấp trong CSDL
CSDL trước khi test:
tblEmployee:

id | full_name | dob | tel | role | username | password | status1 | Nguyễn Gia Đức Trung | 10/09/2005 | 123456 | Quản lý | manager | trung@123 | Working2 | Trần Xuân Thành | 20/08/2005 | 112233 | Phục vụ | staff | thanh@123 | Working3 | Phạm Tuấn Anh | 14/01/2005 | 224466 | Phục vụ | staff | tuan@123 | Working4 | Vũ Hùng Anh | 03/01/2005 | 445566 | Phục vụ | staff | hanh@123 | Working
tblProvider:

id | name | tel | address1 | Công ty cổ phần bia-rượu-nước giải khát | 123456 | abcd2 | Công ty Cổ phần Acecook Việt Nam | 246357 | xyzt
tblImportReceipt:

id | import_date | total_cost | employee_id | provider_id1 | 02/01/2020 | 100,000 | 1 | 1
tblImportDetail:

id | product_id | import_receipt_id | quantity | unit_cost | line_total1 | 1 | 1 | 50 | 18,000 | 900,000

Các bước thực hiện | Kết quả mong muốn1. Nhân viên quản lý đăng nhập thành công và click vào chức năng quản lý kho. | Giao diện hiển thị danh sách thông tin các sản phẩm và có nút nhập hàng.2. Quản lý thấy một số sản phẩm sắp hết (báo đỏ) và click vào nút nhập hàng. | Giao diện hiển thị:
- Danh sách các nhà cung cấp
- Ô nhập tên nhà cung cấp
- Nút tìm
- Nút tạo phiếu nhập hàng3. Quản lý nhập “Bia-rượu-nước giải khát” | Giao diện hiển thị:4. Click vào nhà cung cấp và click nút tạo phiếu nhập hàng. | Giao diện hiển thị:5. Nhập các thông tin “Bia Heniken”, “50”, “18,000” vàclick “LƯU” | Hiển thị thông báo thành công.6. Click OK | Hệ thống lưu phiếu vào CSDL và quay lại màn hình chính của quản lý.
CSDL sau khi test:
tblImportReceipt:

id | import_date | total_cost | employee_id | provider_id1 | 02/01/2020 | 100,000 | 1 | 22 | 04/01/2020 | 900,000 | 1 | 1
tblImportDetail:

id | product_id | import_receipt_id | quantity | unit_cost | line_total1 | 3 | 1 | 10 | 10,000 | 100,0002 | 1 | 2 | 50 | 18,000 | 900,000


