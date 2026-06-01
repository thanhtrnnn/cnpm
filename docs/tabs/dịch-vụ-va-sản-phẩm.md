# Dịch vụ & Sản phẩm

I. PHA XÁC ĐỊNH YÊU CẦU
1. Bảng thuật ngữ


2. Mô hình nghiệp vụ bằng ngôn ngữ tự nhiên
2.1. Mục tiêu
Module thực hiện việc quản lý về dịch vụ và order, cho phép nhân viên phục vụ quản lý order và báo cáo tình trạng hàng hóa, nhân viên quản lý có thể quản lý các đầu mục sản phẩm.

2.2. Phạm vi
Các nhân viên được sử dụng phần mềm: Nhân viên quản lý và nhân viên phục vụ. Khách hàng là đối tượng gián tiếp sử dụng phần mềm.
Nhân viên phục vụ có chức năng:
Quản lý order
Báo cáo tình trạng hàng hóa
Nhân viên quản lý có chức năng:
Quản lý các đầu mục sản phẩm (menu)
Quản lý kho

2.3. Process model cho mỗi chức năng
Quản lý order: Nhân viên phục vụ đăng nhập vào hệ thống → xem danh sách các phòng đang hoạt động và chọn chức năng tạo order → Chọn các sản phẩm theo yêu cầu của khách hàng, xác nhận tạo order → Hệ thống ghi nhận order vào CSDL.
Báo cáo tình trạng hàng hóa: Nhân viên phục vụ đăng nhập vào hệ thống → xem danh sách các phòng chờ dọn và chọn chức năng báo cáo (nếu phát hiện hỏng hóc) → chọn cơ sở vật chất và số lượng hỏng, ấn xác nhận → hệ thống lưu báo cáo về CSDL, tự động cộng dồn tiền chi phí phát sinh vào hóa đơn phòng và trừ số lượng của cơ sở vật chất tương ứng.
Quản lý menu: Nhân viên quản lý đăng nhập vào hệ thống → xem danh sách các sản phẩm → thực hiện thao tác thêm/sửa/xóa sản phẩm → hệ thống cập nhật lại thông tin lên CSDL.
Quản lý kho: Nhân viên quản lý đăng nhập vào hệ thống → xem danh sách các sản phẩm và cơ sở vật chất → nếu số lượng sắp hết thực hiện tạo phiếu nhập hàng → ấn lưu, hệ thống lưu thông tin về CSDL.

2.4. Thông tin các đối tượng cần xử lý
Nhân viên: họ tên, ngày sinh, số điện thoại, vai trò, tên đăng nhập, mật khẩu, trạng thái.
Phòng: tên, loại, giá, sức chứa, trạng thái.
Hóa đơn phòng: thời gian checkin, thời gian checkout, tiền phòng, tiền dịch vụ, tiền phát sinh, tổng tiền, trạng thái.
Cơ sở vật chất: tên, đơn vị, giá, tồn kho.
Báo cáo hỏng hóc: thời gian, tổng tiền phạt.
Order: thời gian order, tổng tiền, trạng thái.
Provider: tên, số điện thoại, địa chỉ.
Phiếu nhập hàng: thời gian nhập, tổng tiền.
Sản phẩm: tên, loại, đơn vị, giá, tồn kho hiện tại, tồn kho an toàn.

2.5. Quan hệ giữa các đối tượng
Một nhân viên phục vụ có thể tạo nhiều order.
Một nhân viên phục vụ có thể tạo nhiều báo cáo.
Một nhân viên quản lý có thể tạo nhiều phiếu nhập hàng.
Một phiếu nhập hàng có thể có nhiều sản phẩm và một sản phẩm có thể có ở nhiều phiếu nhập hàng khác nhau.
Một order có thể có nhiều sản phẩm và một sản phẩm có thể ở nhiều order khác nhau.
Một báo cáo có thể có nhiều cơ sở vật chất và một cơ sở vật chất có thể ở nhiều báo cáo khác nhau.
Một nhà cung cấp có thể có nhiều phiếu nhập hàng.
Một phòng có thể có nhiều hóa đơn.
Một hóa đơn phòng có thể bao gồm chi phí từ nhiều order và nhiều báo cáo hỏng hóc.

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
Sau khi ấn nút tạo phiếu nhập -> đề xuất lớp ImportReceiptView, có các ô nhập thông tin của phiếu và nút xác nhận.
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
Quản lý nhập các thông tin cho phiếu nhập hàng và click lưu.
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


Tầng thực thể: Employee, Product






3.3. Sơ đồ lớp thiết kế
a) Chức năng tạo order


b) Chức năng báo cáo tình trạng hàng hóa


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



