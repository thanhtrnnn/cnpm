# XÁC ĐỊNH YÊU CẦU

XÁC ĐỊNH YÊU CẦU
Hệ thống Quản lý Chuỗi Nhà hàng Karaoke


| Môn học: | Nhập môn Công nghệ Phần mềm |
| --- | --- |
| Nhóm: | Nhóm 7 |

# 1. Bảng thuật ngữ
Bảng thuật ngữ dưới đây định nghĩa các khái niệm nghiệp vụ chính trong hệ thống quản lý chuỗi nhà hàng karaoke, giúp toàn nhóm phát triển hiểu thống nhất các thuật ngữ sử dụng trong tài liệu.


| Thuật ngữ | Tên tiếng Anh | Định nghĩa |
| --- | --- | --- |
| 1. Nhóm thuật ngữ liên quan đến Cơ sở vật chất & Phòng hát (Facilities & Rooms) |  |  |
| Loại phòng | Room Type / Room Category | Phân loại phòng hát dựa trên tiêu chuẩn, diện tích và trang thiết bị (VD: Standard, VIP, Super VIP, Party). |
| Sức chứa | Capacity | Số lượng khách tối đa mà một phòng hát có thể phục vụ thoải mái nhất. |
| Trạng thái phòng | Room Status | Tình trạng hiện tại của phòng trên hệ thống (Trống, Đang phục vụ, Đã đặt trước, Đang dọn dẹp, Bảo trì). |
| Giá theo giờ | Hourly Rate | Mức giá áp dụng cho mỗi giờ hát. Có thể thay đổi linh hoạt theo khung giờ (ngày/đêm) hoặc ngày Lễ/Tết. |
| Thiết bị KTV | KTV Equipment | Các thiết bị đặc thù trong phòng hát (Màn hình cảm ứng chọn bài, micro, hệ thống âm thanh, đèn laser). |
| Báo cáo hỏng hóc | Report Damage | Thao tác nhân viên phục vụ ghi nhận thiết bị trong phòng bị lỗi, hỏng để báo kỹ thuật. |
| 2. Nhóm thuật ngữ liên quan đến Đặt phòng & Vận hành (Booking & Operations) |  |  |
| Đặt phòng tại quầy | Book on site / Walk-in | Khách hàng đến trực tiếp chi nhánh để yêu cầu xếp phòng hát. |
| Đặt phòng trực tuyến | Book Online | Giao dịch giữ phòng trước cho khách thông qua hệ thống web/app. |
| Tiền cọc | Deposit | Khoản tiền khách thanh toán trước để đảm bảo cho việc đặt phòng. |
| Nhận phòng / Trả phòng | Check-in / Check-out | Thao tác bắt đầu tính giờ sử dụng phòng và thao tác kết thúc tính giờ để thanh toán. |
| Hủy đặt phòng | Cancel Booking | Thao tác khách hàng hủy yêu cầu giữ phòng trước thời điểm nhận phòng. |
| 3. Nhóm thuật ngữ: Dịch vụ, Gọi món & Quản lý Kho (F&B, Order & Inventory) |  |  |
| Yêu cầu gọi món | Order / Order Note | Yêu cầu dịch vụ ăn uống từ phòng hát, được phục vụ tiếp nhận và chuyển đến bếp/bar. |
| Tồn kho | Inventory | Số lượng hàng hóa (nguyên liệu, đồ uống, vật tư) còn lại tại mỗi chi nhánh. |
| Phiếu nhập hàng | Goods Receipt | Chứng từ ghi nhận số lượng hàng hóa được nhập thêm vào kho chi nhánh. |
| Kiểm kê định kỳ | Periodic Inventory | Quá trình kiểm đếm số lượng thực tế tại kho để so sánh với số liệu trên hệ thống. |
| Đối soát kho | Reconciliation | Xử lý các chênh lệch (Handle quantity differences) khi số lượng thực tế khác với hệ thống. |
| Báo cáo thiếu hụt | Report Shortage | Cảnh báo từ nhân viên hoặc hệ thống khi một mặt hàng sắp hoặc đã hết trong kho. |
| 4. Nhóm thuật ngữ: Quản lý Hội viên (Membership Management) |  |  |
| Dịch vụ / Món ăn | Services | Các sản phẩm đồ ăn, thức uống và dịch vụ bổ sung (khăn lạnh, trái cây...) mà khách hàng có thể gọi thêm. |
| Tồn kho (Inventory) | Inventory | Số lượng hàng hóa (nguyên liệu, đồ uống, vật tư) còn lại tại mỗi chi nhánh, cần được theo dõi và bổ sung. |
| Nhân viên lễ tân | Receptionist | Nhân viên tại quầy tiếp tân, phụ trách xếp phòng, check-in/out, lập hóa đơn và thu tiền. |
| Nhân viên phục vụ | Waiter | Nhân viên phụ trách nhận order gọi món từ phòng, phục vụ đồ ăn/uống và báo cáo tình trạng hàng hóa. |
| Quản lý chi nhánh | Branch Manager | Người quản lý một chi nhánh cụ thể: điều phối nhân viên, giám sát kho và xem báo cáo hoạt động. |
| Chủ doanh nghiệp | Founder | Người sở hữu toàn bộ chuỗi karaoke, có quyền quản lý tất cả chi nhánh, nhân viên, menu, giá và xem báo cáo tổng hợp. |
| Hội viên | Member | Khách hàng đã đăng ký thẻ, được tích điểm và hưởng ưu đãi theo hạng. |
| Kiểm tra hạng thẻ | Check Membership Class | Truy xuất cấp bậc hiện tại của hội viên (Thường, Bạc, Vàng...) trên hệ thống. |
| Nâng hạng thẻ | Upgrade Membership Class | Quá trình hệ thống tự động hoặc thủ công nâng cấp bậc cho hội viên khi đủ điều kiện. |
| Quản lý thông tin | Manage Personal Info | Các thao tác cập nhật số điện thoại, mật khẩu, họ tên của người dùng. |
| 5. Nhóm thuật ngữ: Thanh toán & Báo cáo Doanh thu (Payment & Reporting) |  |  |
| Thanh toán | Payment | Chứng từ tổng hợp bao gồm tiền phòng và tiền dịch vụ/gọi món cho một lượt sử dụng. |
| Áp dụng Voucher | Apply Voucher | Thao tác nhập mã giảm giá hoặc sử dụng điểm hội viên để trừ vào tổng hóa đơn. |
| Tiêu chí thời gian | Time Criteria | Các mốc lọc dữ liệu báo cáo (Theo ngày, tuần, tháng, quý, năm). |
| So sánh hiệu suất | Compare Branches Efficiency | Báo cáo đối chiếu doanh thu, công suất hoạt động giữa các chi nhánh khác nhau trong chuỗi. |
| Tổng doanh thu | Total Revenue | Báo cáo gộp số tiền thu về của toàn bộ chuỗi karaoke do Admin quản lý. |
| 6. Nhóm thuật ngữ: Quản trị Hệ thống & Nhân sự (Admin, Branch & HR) |  |  |
| Danh mục chung | General Categories | Các dữ liệu gốc do Chủ doanh nghiệp quản lý (Menu F&B, Bảng giá phòng, Khuyến mãi). |
| Chi nhánh | Branch | Cơ sở kinh doanh karaoke thuộc chuỗi, có địa chỉ, nhân viên và phòng hát riêng. |
| Phân ca | Assign Shifts | Việc Quản lý chi nhánh sắp xếp lịch làm việc cho từng nhân viên theo ngày/tuần. |
| Theo dõi chấm công | Timekeeping Tracking | Việc quản lý ghi nhận và theo dõi thời gian làm việc thực tế của nhân viên. |
| Đánh giá nhân sự | Evaluate Employee | Quy trình nhận xét hiệu suất làm việc của nhân viên tại chi nhánh. |
| Khen thưởng / Kỷ luật | Award / Discipline | Các quyết định thưởng hoặc phạt nhân viên dựa trên đánh giá hiệu suất hoặc vi phạm. |


# 2. Mô hình nghiệp vụ bằng ngôn ngữ tự nhiên
## 2.1. Mục tiêu và phạm vi hệ thống
Mục tiêu: Xây dựng hệ thống phần mềm quản lý tập trung cho chuỗi nhà hàng karaoke, cho phép quản lý đặt phòng, gọi món, thanh toán, nhân sự, kho hàng và báo cáo doanh thu trên nhiều chi nhánh.
Phạm vi: Hệ thống bao phủ toàn bộ quy trình vận hành từ khi khách hàng đặt phòng đến khi thanh toán, đồng thời hỗ trợ quản lý nội bộ (nhân sự, kho, báo cáo) cho từng chi nhánh và toàn chuỗi. Hệ thống được triển khai trên nền tảng web và ứng dụng di động, phục vụ cả người dùng bên ngoài (khách hàng) lẫn người dùng nội bộ (nhân viên, quản lý, chủ doanh nghiệp).
## 2.2. Ai có thể sử dụng phần mềm?
Hệ thống phục vụ 5 nhóm người dùng chính:
Khách hàng là nhóm người dùng bên ngoài, sử dụng web hoặc ứng dụng di động để đặt phòng trực tuyến, theo dõi lịch sử sử dụng, quản lý điểm thưởng hội viên và tương tác dịch vụ trực tiếp khi đang ở phòng hát.
Nhân viên lễ tân là người dùng nội bộ tại quầy tiếp tân của mỗi chi nhánh. Họ trực tiếp xử lý các thao tác đặt phòng walk-in, thực hiện check-in/check-out, tổng hợp hóa đơn và thu tiền của khách.
Nhân viên phục vụ là người dùng nội bộ sử dụng thiết bị tablet hoặc ứng dụng di động để tiếp nhận order gọi món từ các phòng, chuyển yêu cầu đến bếp/bar, theo dõi và cập nhật trạng thái phục vụ, đồng thời báo cáo tình trạng hàng hóa và cơ sở vật chất trong phòng.
Quản lý chi nhánh là người dùng nội bộ phụ trách điều hành toàn bộ một chi nhánh: phân ca làm việc cho nhân viên, theo dõi chấm công, đánh giá hiệu suất, quản lý kho hàng, xem thông tin khách hàng của chi nhánh và xem báo cáo doanh thu chi nhánh.
Chủ doanh nghiệp là người dùng cấp cao nhất, có quyền quản lý toàn bộ chuỗi karaoke: thêm/sửa/xóa chi nhánh, quản lý danh mục chung (menu, bảng giá phòng, chương trình khuyến mãi), quản lý toàn bộ danh sách khách hàng, cấu hình hạng hội viên, quản lý phòng hát và xem báo cáo tổng hợp toàn chuỗi.
## 2.3. Người dùng có những chức năng gì?
## Khách hàng
Đặt phòng trực tuyến hoặc trực tiếp tại chi nhánh.
Quản lý thông tin cá nhân (tên, số điện thoại, hạng hội viên).
Tương tác dịch vụ trong phòng: gọi món qua app hoặc điện thoại nội bộ, yêu cầu dịch vụ bổ sung.
Nhân viên lễ tân
Quản lý đặt phòng: xếp phòng walk-in, xác nhận check-in booking online, tra cứu và tìm kiếm booking.
Quản lý trả phòng: tính tiền phòng, tổng hợp order, áp dụng ưu đãi hội viên/voucher, thu tiền, in hóa đơn.
Nhân viên phục vụ
Quản lý order: nhận yêu cầu gọi món từ phòng (qua app hoặc điện thoại), chuyển bếp/bar, cập nhật trạng thái giao hàng, hủy hoặc thay đổi order.
Báo cáo tình trạng hàng hóa: kiểm tra cơ sở vật chất phòng sau mỗi lượt, cập nhật trạng thái phòng, báo hỏng hóc thiết bị, yêu cầu bổ sung minibar.
Quản lý chi nhánh
Quản lý nhân viên chi nhánh: phân ca làm việc, theo dõi chấm công thực tế, đánh giá hiệu suất, thực hiện khen thưởng hoặc kỷ luật.
Quản lý kho: theo dõi nhập/xuất, duyệt phiếu nhập hàng, gửi đơn mua hàng, hủy hàng, đối soát tồn kho.
Xem thông tin khách hàng của chi nhánh: tra cứu danh sách và lịch sử sử dụng của khách hàng tại chi nhánh mình.
Báo cáo số liệu: doanh thu, công suất phòng, số lượng khách, doanh số bán hàng theo ngày/tuần/tháng/quý/năm; xuất báo cáo.
Quản lý phòng hát tại chi nhánh: thêm phòng mới (áp dụng theo loại phòng chuẩn), cập nhật trạng thái (trống, bảo trì...) và xóa các phòng vật lý.
Chủ doanh nghiệp (Admin)
Quản lý hệ thống chi nhánh: thêm, cập nhật, xóa chi nhánh; xem toàn bộ danh sách chi nhánh.
Quản lý danh mục chung: menu món ăn/đồ uống, bảng giá phòng theo loại và khung giờ, chương trình khuyến mãi.
Quản lý danh mục loại phòng: định nghĩa các loại phòng chuẩn (Standard, VIP...), cấu hình mức sức chứa và bảng giá chung cho toàn hệ thống.
Quản lý khách hàng toàn hệ thống: xem/tìm kiếm khách hàng toàn chuỗi, xem lịch sử sử dụng, khóa tài khoản nếu cần.
Quản lý hạng hội viên: cấu hình điều kiện nâng hạng và ưu đãi theo hạng (rule hệ thống); thay đổi hạng thủ công cho khách hàng cụ thể khi cần.
Quản lý tài khoản nhân viên: tạo tài khoản mới, phân quyền, khóa/mở tài khoản, reset mật khẩu.
Tổng hợp báo cáo: so sánh hiệu suất chi nhánh, doanh thu toàn chuỗi, xuất file báo cáo.
## 2.4. Mỗi chức năng hoạt động như thế nào?
## UC01 – Đăng nhập
Người dùng nhập SĐT/Email và mật khẩu → Hệ thống xác thực thông tin đăng nhập → Hệ thống tạo phiên đăng nhập → Hệ thống chuyển người dùng đến trang chủ tương ứng vai trò.
Người dùng nhập sai mật khẩu → Hệ thống thông báo lỗi xác thực → Người dùng nhập lại (tối đa 5 lần).
Tài khoản bị khóa → Hệ thống hiển thị thông báo tài khoản bị khóa → Người dùng liên hệ Admin.

## UC02 – Đăng ký
Khách hàng nhập Họ tên, SĐT, Email, Mật khẩu → Hệ thống kiểm tra SĐT và Email chưa tồn tại → Hệ thống gửi mã OTP đến SĐT → Khách hàng nhập mã OTP → Hệ thống xác minh OTP hợp lệ → Hệ thống tạo tài khoản hạng "Thường" → Hệ thống tự động đăng nhập.
SĐT hoặc Email đã tồn tại → Hệ thống thông báo trùng lặp → Khách hàng dùng thông tin khác hoặc chọn Đăng nhập.
OTP sai hoặc hết hạn (5 phút) → Hệ thống thông báo lỗi OTP → Khách hàng yêu cầu gửi lại OTP.

## UC03 – Đổi mật khẩu
Người dùng nhập mật khẩu hiện tại và mật khẩu mới → Hệ thống xác minh mật khẩu hiện tại đúng → Hệ thống kiểm tra mật khẩu mới hợp lệ → Hệ thống cập nhật mật khẩu → Hệ thống thu hồi tất cả phiên đăng nhập khác.

Mật khẩu hiện tại không đúng → Hệ thống thông báo lỗi → Người dùng thử lại.
Mật khẩu mới không hợp lệ → Hệ thống hiển thị yêu cầu định dạng → Người dùng nhập lại.

## UC04 – Quản lý thông tin cá nhân
Khách hàng xem hồ sơ cá nhân (Họ tên, SĐT, Email, Hạng hội viên, Điểm tích lũy) → Khách hàng chỉnh sửa Họ tên hoặc Email → Hệ thống kiểm tra Email chưa tồn tại → Hệ thống cập nhật hồ sơ → Hệ thống hiển thị thông báo thành công.

## UC05 – Đặt phòng
Đặt phòng trực tuyến: Khách hàng đăng nhập → Khách hàng chọn chi nhánh và khung giờ → Hệ thống hiển thị danh sách phòng trống → Khách hàng chọn phòng và xác nhận → Hệ thống ghi nhận booking trạng thái "Chờ nhận" → Hệ thống gửi thông báo xác nhận đến khách hàng.

Đặt phòng tại chi nhánh: Khách hàng đến chi nhánh → Lễ tân tra cứu phòng trống theo khung giờ → Lễ tân ghi nhận thông tin khách (hoặc tra cứu hội viên qua SĐT) → Lễ tân chọn phòng và xác nhận với khách → Hệ thống tạo booking trạng thái "Chờ nhận".

Hủy phòng trực tuyến: Khách hàng chọn booking cần hủy → Khách hàng bấm Hủy đặt phòng → Hệ thống yêu cầu xác nhận → Khách hàng xác nhận → Hệ thống chuyển trạng thái booking sang "Đã hủy" → Hệ thống giải phóng slot phòng.

Hủy phòng tại chi nhánh: Khách hàng yêu cầu hủy trực tiếp → Lễ tân tra cứu booking → Lễ tân xác nhận hủy trên hệ thống → Hệ thống chuyển trạng thái sang "Đã hủy" → Hệ thống ghi nhận không hoàn tiền cọc.
## UC06 – Gọi món / Quản lý order
Tạo order: Khách hàng yêu cầu gọi món → Nhân viên phục vụ mở hệ thống, chọn phòng tương ứng → Nhân viên thêm các món vào order → Nhân viên gửi order → Hệ thống ghi nhận order và thông báo đến bếp/bar.

Cập nhật hoặc hủy order (trước khi bếp xử lý): Nhân viên chọn order cần thay đổi → Nhân viên sửa số lượng hoặc hủy món → Hệ thống cập nhật order → Hệ thống thông báo lại bếp/bar.

Giao món và ghi nhận: Nhân viên mang đồ đến phòng → Nhân viên cập nhật trạng thái order sang "Đã giao" → Hệ thống tự động ghi chi tiết order vào hóa đơn phòng.

## UC07 – Quản lý đặt phòng (check-in)
Khách hàng đến nhận phòng → Lễ tân tra cứu booking theo tên/SĐT → Lễ tân xác nhận đúng thông tin khách và phòng → Hệ thống chuyển trạng thái booking từ "Chờ nhận" sang "Đang hoạt động" → Hệ thống ghi nhận thời gian check-in thực tế.

## UC08 – Quản lý trả phòng (check-out)
Khách hàng yêu cầu trả phòng → Lễ tân chọn phòng trên hệ thống → Hệ thống tính tiền phòng (giờ thực tế × đơn giá) cộng tổng tiền order → Lễ tân áp dụng ưu đãi hoặc voucher nếu khách là hội viên → Hệ thống hiển thị tổng tiền → Khách hàng thanh toán (tiền mặt / chuyển khoản) → Lễ tân in hóa đơn → Hệ thống đóng phòng, chuyển trạng thái về "Trống" → Hệ thống cộng điểm hội viên tự động.

## UC10 – Báo cáo tình trạng hàng hóa
Sau mỗi lượt phục vụ, nhân viên phục vụ chọn phòng vừa phục vụ trên hệ thống → Nhân viên kiểm tra cơ sở vật chất trong phòng → Nhân viên cập nhật trạng thái phòng → Nếu phát hiện thiết bị hỏng, nhân viên tạo phiếu báo hỏng hóc → Nếu minibar cần bổ sung, nhân viên gửi yêu cầu bổ sung → Hệ thống ghi nhận và thông báo đến Quản lý chi nhánh.

## UC11 – Quản lý nhân viên chi nhánh
Quản lý chi nhánh xem danh sách nhân viên của chi nhánh → Quản lý phân ca làm việc cho nhân viên theo ngày/tuần → Hệ thống ghi nhận lịch ca và chấm công thực tế → Quản lý đánh giá hiệu suất định kỳ → Quản lý thực hiện khen thưởng hoặc kỷ luật → Hệ thống lưu kết quả phân ca, đánh giá và quyết định.

## UC12 – Quản lý kho
Quản lý chi nhánh theo dõi tồn kho trên hệ thống → Khi hàng sắp hết, hệ thống cảnh báo tự động → Quản lý duyệt phiếu nhập hàng hoặc gửi đơn mua hàng → Hàng về, nhân viên kiểm nhận và tạo phiếu nhập → Hệ thống cập nhật số lượng tồn kho → Khi phục vụ order, hệ thống tự động trừ tồn kho tương ứng.

## UC13 – Báo cáo số liệu chi nhánh
Quản lý chi nhánh chọn chức năng báo cáo → Quản lý chọn kỳ báo cáo (ngày/tuần/tháng/quý/năm) → Hệ thống tổng hợp doanh thu, công suất phòng, lượng khách và doanh số bán hàng → Hệ thống hiển thị số liệu dạng bảng và biểu đồ → Quản lý xuất báo cáo ra file Excel/PDF.

## UC14 – Xem thông tin khách hàng chi nhánh
Quản lý chi nhánh nhập từ khóa tìm kiếm (tên hoặc SĐT) → Hệ thống truy vấn danh sách khách hàng của chi nhánh → Hệ thống hiển thị danh sách kết quả → Quản lý chọn một khách hàng → Hệ thống hiển thị lịch sử sử dụng và điểm tích lũy.

## UC15 – Quản lý menu
Xem và lọc menu: Quản lý chi nhánh chọn chức năng quản lý menu → Hệ thống hiển thị danh sách món ăn/đồ uống → Quản lý lọc theo danh mục → Hệ thống hiển thị danh sách đã lọc.

Thêm hoặc sửa món: Quản lý chọn Thêm mới hoặc Sửa → Hệ thống hiển thị form (Tên món, Loại, Đơn giá, Mô tả, Trạng thái) → Quản lý nhập thông tin → Hệ thống kiểm tra dữ liệu hợp lệ → Hệ thống lưu và làm mới danh sách.

Ẩn hoặc xóa món: Quản lý chọn món cần xóa hoặc ẩn → Hệ thống hiển thị xác nhận → Quản lý xác nhận → Hệ thống cập nhật trạng thái "Ngừng kinh doanh" hoặc xóa khỏi danh mục.

## UC16 – Quản lý hệ thống chi nhánh
Admin chọn chức năng quản lý chi nhánh → Hệ thống hiển thị danh sách chi nhánh → Admin chọn Thêm mới, Sửa hoặc Xóa → Hệ thống hiển thị form nhập liệu (Thêm/Sửa) hoặc popup xác nhận (Xóa) → Admin nhập thông tin hoặc xác nhận → Hệ thống kiểm tra ràng buộc (không xóa chi nhánh đang hoạt động) → Hệ thống cập nhật CSDL và làm mới danh sách.

## UC17 – Quản lý khách hàng toàn hệ thống
Admin nhập từ khóa và tìm kiếm → Hệ thống hiển thị danh sách kết quả toàn chuỗi → Admin chọn Xem chi tiết hoặc Khóa tài khoản → Hệ thống truy xuất lịch sử đặt phòng (nếu xem) hoặc yêu cầu xác nhận (nếu khóa) → Admin thực hiện thao tác → Hệ thống cập nhật trạng thái tài khoản.

## UC18 – Quản lý hạng hội viên
Admin xem danh sách cấu hình các hạng (Thường/Bạc/Vàng) → Admin chọn Sửa cấu hình ngưỡng điểm/ưu đãi hoặc Thay đổi hạng thủ công cho khách hàng → Hệ thống hiển thị form tương ứng → Admin thay đổi thông số hoặc chọn khách hàng và hạng mới → Admin xác nhận → Hệ thống kiểm tra tính hợp lệ → Hệ thống cập nhật CSDL.

## UC19 – Quản lý phòng hát
Quản lý danh mục loại phòng (Admin): Admin chọn chức năng quản lý loại phòng → Hệ thống hiển thị danh mục loại phòng chuẩn → Admin chọn Thêm mới, Sửa hoặc Xóa → Hệ thống hiển thị form (Tên loại, Sức chứa, Giá chung) hoặc xác nhận xóa → Admin nhập thông tin hoặc xác nhận → Hệ thống kiểm tra ràng buộc (không xóa loại đang được chi nhánh sử dụng) → Hệ thống cập nhật tiêu chuẩn phòng toàn hệ thống.

Quản lý phòng vật lý tại chi nhánh (Quản lý chi nhánh): Quản lý chọn chức năng quản lý phòng của chi nhánh → Hệ thống hiển thị danh sách phòng thuộc chi nhánh → Quản lý chọn Thêm mới, Sửa hoặc Xóa → Hệ thống hiển thị form (Tên phòng, Loại phòng) hoặc xác nhận xóa → Quản lý nhập thông tin hoặc xác nhận → Hệ thống kiểm tra ràng buộc (không xóa phòng đang có lịch đặt) → Hệ thống cập nhật CSDL chi nhánh.

## UC20 – Quản lý tài khoản nhân viên
Chủ doanh nghiệp xem danh sách tài khoản nhân viên → Chủ doanh nghiệp tạo tài khoản mới (Họ tên, SĐT, Vai trò, Chi nhánh) → Hệ thống tạo tài khoản và mã hóa mật khẩu mặc định → Chủ doanh nghiệp gán phân quyền phù hợp với vai trò → Khi cần, Chủ doanh nghiệp khóa, mở hoặc reset mật khẩu tài khoản → Hệ thống cập nhật trạng thái tài khoản.

## UC21 – Tổng hợp báo cáo toàn chuỗi
Chủ doanh nghiệp chọn khoảng thời gian và các chi nhánh cần xem → Hệ thống tổng hợp số liệu toàn chuỗi → Hệ thống hiển thị biểu đồ so sánh hiệu suất giữa các chi nhánh và tổng doanh thu → Chủ doanh nghiệp xuất file báo cáo (Excel/PDF).

## 2.5. Những thông tin/đối tượng mà hệ thống cần xử lý
Hệ thống cần quản lý và xử lý các đối tượng thông tin chính sau:
Chi nhánh: Mã chi nhánh, tên, địa chỉ, số điện thoại.
Khách hàng: Mã khách hàng, họ tên, số điện thoại, địa chỉ, hạng hội viên (Thường/Bạc/Vàng), trạng thái tài khoản.
Hạng hội viên: Mã hạng, tên hạng, ngưỡng điểm tối thiểu, ưu đãi (% giảm giá, điểm thưởng nhân).
Nhân viên: Mã nhân viên, họ tên, vai trò, chi nhánh làm việc, trạng thái (đang làm/nghỉ).
Tài khoản: Mã tài khoản, tên đăng nhập, mật khẩu mã hóa, phân quyền, trạng thái hoạt động.
Phòng hát: Mã phòng, tên phòng, loại phòng, sức chứa, giá theo giờ, trạng thái, thuộc chi nhánh.
Dịch vụ/Món ăn: Mã dịch vụ, tên, loại (đồ ăn/đồ uống/dịch vụ bổ sung), đơn giá, mô tả, trạng thái kinh doanh.
Đặt phòng: Mã booking, khách hàng, phòng, nhân viên lễ tân xử lý, thời gian bắt đầu/kết thúc dự kiến và thực tế, trạng thái (Chờ nhận/Đang sử dụng/Hoàn thành/Đã hủy).
Hóa đơn: Mã hóa đơn, liên kết đặt phòng, tiền phòng, thời gian sử dụng thực tế, tiền dịch vụ, phụ phí, giảm giá, tổng tiền, trạng thái thanh toán, phương thức thanh toán.
Chi tiết gọi món: Mã chi tiết, liên kết hóa đơn, dịch vụ/món ăn, số lượng, nhân viên phục vụ, thời gian gọi, trạng thái (Chờ/Đang chuẩn bị/Đã giao/Đã hủy).
Tồn kho: Mã tồn kho, chi nhánh, dịch vụ/hàng hóa, số lượng tồn, ngưỡng cảnh báo thấp.
Phiếu nhập hàng: Mã phiếu, chi nhánh, danh sách hàng nhập, số lượng, ngày nhập, người duyệt, trạng thái.
Ca làm việc: Mã ca, nhân viên, ngày làm việc, giờ bắt đầu/kết thúc, trạng thái chấm công.
Khuyến mãi: Mã khuyến mãi, tên, loại (voucher/giảm giá %), điều kiện áp dụng, thời hạn hiệu lực.
## 2.6. Quan hệ giữa các đối tượng
Các đối tượng trong hệ thống có mối quan hệ chặt chẽ với nhau:
Một Chi nhánh có nhiều Phòng hát, nhiều Nhân viên và nhiều bản ghi Tồn kho.
Một Khách hàng thuộc một Hạng hội viên (Thường/Bạc/Vàng) và có thể có một Tài khoản đăng nhập.
Một Hạng hội viên định nghĩa ngưỡng điểm và áp dụng cho nhiều Khách hàng.
Một Nhân viên thuộc một Chi nhánh, có thể có một Tài khoản và có nhiều bản ghi Ca làm việc.
Một Đặt phòng liên kết với một Phòng hát, một Khách hàng (có thể null nếu walk-in chưa đăng ký) và một Nhân viên lễ tân xử lý.
Một Đặt phòng tạo ra đúng một Hóa đơn.
Một Hóa đơn chứa nhiều Chi tiết gọi món. Một Hóa đơn có thể áp dụng một Khuyến mãi.
Mỗi Chi tiết gọi món tham chiếu đến một Dịch vụ/Món ăn và một Nhân viên phục vụ.
Tồn kho theo dõi số lượng của mỗi Dịch vụ/Hàng hóa tại mỗi Chi nhánh.
Một Phiếu nhập hàng thuộc một Chi nhánh và ghi nhận nhiều mặt hàng được nhập.

# 3. Mô hình nghiệp vụ bằng UML
## 3.1. Danh sách Actor


| STT | Actor | Mô tả |
| --- | --- | --- |
| 1 | Khách hàng | Người sử dụng dịch vụ karaoke, truy cập qua web/app để đặt phòng và quản lý tài khoản cá nhân. |
| 2 | Nhân viên lễ tân | Nhân viên tại quầy, xử lý đặt phòng, check-in/check-out và thanh toán. |
| 3 | Nhân viên phục vụ | Nhân viên nhận order gọi món, phục vụ đồ ăn/uống và báo cáo tình trạng hàng hóa trong phòng. |
| 4 | Quản lý chi nhánh | Quản lý một chi nhánh: nhân sự, kho hàng, menu, phòng hát và xem báo cáo hoạt động. |
| 5 | Chủ doanh nghiệp | Chủ sở hữu toàn chuỗi, quản lý chi nhánh, danh mục, khách hàng, hạng hội viên và xem báo cáo tổng hợp. |
| 6 | Thành viên | Actor trừu tượng, là cha của tất cả actor cụ thể trong hệ thống. |
| 7 | Nhân viên | Actor trừu tượng, là cha của NV lễ tân và NV phục vụ. |

## 3.2. Các Use Case cho từng Actor

| Actor | Use Case |
| --- | --- |
| Thành viên (tổng quát) | UC01 – Đăng nhập |
|  | UC03 – Đổi mật khẩu |
| Khách hàng | UC02 – Đăng ký |
|  | UC04 – Quản lý thông tin cá nhân |
|  | UC05 – Đặt phòng |
|  | UC06 – Gọi món / Quản lý order |
| NV lễ tân | UC05 – Đặt phòng |
|  | UC07 – Quản lý đặt phòng (check-in) |
|  | UC08 – Quản lý trả phòng (check-out) |
| NV phục vụ | UC06 – Gọi món / Quản lý order |
|  | UC10 – Báo cáo tình trạng hàng hóa |
| Quản lý chi nhánh | UC11 – Quản lý nhân viên chi nhánh |
|  | UC12 – Quản lý kho |
|  | UC13 – Báo cáo số liệu chi nhánh |
|  | UC14 – Xem thông tin khách hàng chi nhánh |
|  | UC15 – Quản lý menu |
|  | UC19 – Quản lý phòng hát |
| Chủ doanh nghiệp | UC16 – Quản lý hệ thống chi nhánh |
|  | UC17 – Quản lý khách hàng toàn hệ thống |
|  | UC18 – Quản lý hạng hội viên |
|  | UC19 – Quản lý phòng hát |
|  | UC20 – Quản lý tài khoản nhân viên |
|  | UC21 – Tổng hợp báo cáo toàn chuỗi |

## 
### 