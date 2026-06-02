# Dịch vụ & Sản phẩm



MỤC LỤC

I. PHA XÁC ĐỊNH YÊU CẦU 
3. Mô hình nghiệp vụ bằng UML
3.1. Danh sách các Actor cho module
Actor trực tiếp: Nhân viên phục vụ (Service Staff), Nhân viên lễ tân (Receptionist), Nhân viên quản lý chi nhánh (Branch manager). Các actor này kế thừa từ actor Nhân viên (Employee).
Actor gián tiếp: Khách hàng (Client).

3.2. Các Use Case cho từng Actor


3.3. Biểu đồ UC tổng quan của module


3.4. Các biểu đồ Use Case phân rã của module
a) Use case Quản lý order


b) Báo cáo tình trạng hàng hóa


c) Quản lý menu


d) Quản lý kho


II. PHA PHÂN TÍCH
1. Mô hình hóa chức năng
1.1. Kịch bản “Tạo order”


1.2. Kịch bản “Báo cáo tình trạng hàng”


1.3. Kịch bản “Quản lý menu”



1.4. Kịch bản “Quản lý kho”


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



Tầng điều khiển (Control):



Tầng thực thể (Entity): Employee, Room, Order, Order_detail, Product, Room_receipt.

b) Chức năng báo cáo tình trạng hàng
Tầng giao diện:


Tầng điều khiển:



Tầng thực thể: Employee, Facility, Damage_report, Room, Damage_detail, Room_receipt.

c) Chức năng quản lý menu
Tầng giao diện:



Tầng điều khiển:


Tầng thực thể: Employee, Product.

d) Chức năng quản lý kho
Tầng giao diện:


Tầng điều khiển:


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


2. Các test case cho từng chức năng
a) Chức năng tạo order
- Test case 1: Không tìm thấy phòng trong CSDL:CSDL trước khi test:
tblEmployee:


tblRoom:


tblProduct:


tblRoomReceipt:


tblOrder:


tblOrderDetail:




CSDL sau khi test: không có gì thay đổi.

- Test case 2: có phòng nhưng không tìm thấy sản phẩm.
CSDL trước khi test:
tblEmployee:


tblRoom:


tblProduct:


tblRoomReceipt:


tblOrder:


tblOrderDetail:




CSDL sau khi test: không có gì thay đổi.

- Test case 3: Tìm thấy phòng và sản phẩm trong CSDL:
CSDL trước khi test:
tblEmployee:


tblRoom:


tblProduct:


tblRoomReceipt:


tblOrder:


tblOrderDetail:





CSDL sau khi test:
tblProduct:


tblRoomReceipt:


tblOrder:


tblOrderDetail:



- Test case 4: ấn nút thêm khi đã quá số lượng tồn kho của sản phẩm
CSDL trước khi test:
tblEmployee:


tblRoom:


tblProduct:


tblRoomReceipt:


tblOrder:


tblOrderDetail:




CSDL sau khi test: không có gì thay đổi.

b) Chức năng Báo cáo tình trạng hàng
- Test case 1: cơ sở vật chất chưa có trong CSDL
CSDL trước khi test:
tblEmployee:


tblRoom:


tblFacility:


tblRoomReceipt:


tblDamageReport:


tblDamageDetail:




CSDL sau khi test: không có gì thay đổi.

- Test case 2: cơ sở vật chất có trong CSDL:
CSDL trước khi test:
tblEmployee:


tblRoom:


tblFacility:


tblRoomReceipt:


tblDamageReport:


tblDamageDetail:




CSDL sau khi test:
tblFacility:



tblRoomReceipt:


tblDamageReport:


tblDamageDetail:



c) Chức năng quản lý menu
- Test case 1: sản phẩm chưa có trong CSDL
CSDL trước khi test:
tblEmployee:


tblProduct:




CSDL sau khi test: không có gì thay đổi.

- Test case 2: có sản phẩm trong CSDL:
CSDL trước khi test:
tblProduct:




CSDL sau khi test: chỉ có tblProduct thay đổi
tblProduct:


d) Chức năng quản lý kho
- Test case 1: không có tên nhà cung cấp trong CSDL
CSDL trước khi test:
tblEmployee:


tblProvider:




CSDL sau khi test: không có gì thay đổi

- Test case 2: đã có tên nhà cung cấp trong CSDL
CSDL trước khi test:
tblEmployee:


tblProvider:


tblImportReceipt:


tblImportDetail:




CSDL sau khi test:
tblImportReceipt:


tblImportDetail:



