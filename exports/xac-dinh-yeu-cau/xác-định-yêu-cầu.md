# XÁC ĐỊNH YÊU CẦU

XÁC ĐỊNH YÊU CẦU
Hệ thống Quản lý Chuỗi Nhà hàng Karaoke

1. Bảng thuật ngữ
Bảng thuật ngữ dưới đây định nghĩa các khái niệm nghiệp vụ chính trong hệ thống quản lý chuỗi nhà hàng karaoke, giúp toàn nhóm phát triển hiểu thống nhất các thuật ngữ sử dụng trong tài liệu.


2. Mô hình nghiệp vụ bằng ngôn ngữ tự nhiên
2.1. Mục tiêu và phạm vi hệ thống
Mục tiêu: Xây dựng hệ thống phần mềm quản lý tập trung cho chuỗi nhà hàng karaoke, cho phép quản lý đặt phòng, gọi món, thanh toán, nhân sự, kho hàng và báo cáo doanh thu trên nhiều chi nhánh.
Phạm vi: Hệ thống bao phủ toàn bộ quy trình vận hành từ khi khách hàng đặt phòng đến khi thanh toán, đồng thời hỗ trợ quản lý nội bộ (nhân sự, kho, báo cáo) cho từng chi nhánh và toàn chuỗi. Hệ thống được triển khai trên nền tảng web và ứng dụng di động, phục vụ cả người dùng bên ngoài (khách hàng) lẫn người dùng nội bộ (nhân viên, quản lý, chủ doanh nghiệp).
2.2. Ai có thể sử dụng phần mềm?
Hệ thống phục vụ 5 nhóm người dùng chính:
Khách hàng là nhóm người dùng bên ngoài, sử dụng web hoặc ứng dụng di động để đặt phòng trực tuyến, theo dõi lịch sử sử dụng, quản lý điểm thưởng hội viên và tương tác dịch vụ trực tiếp khi đang ở phòng hát.
Nhân viên lễ tân là người dùng nội bộ tại quầy tiếp tân của mỗi chi nhánh. Họ trực tiếp xử lý các thao tác đặt phòng walk-in, thực hiện check-in/check-out, tổng hợp hóa đơn và thu tiền của khách, đồng thời kiểm kê hàng hóa tại quầy.
Nhân viên phục vụ là người dùng nội bộ sử dụng thiết bị tablet hoặc ứng dụng di động để tiếp nhận order gọi món từ các phòng, chuyển yêu cầu đến bếp/bar, theo dõi và cập nhật trạng thái phục vụ, đồng thời báo cáo tình trạng hàng hóa và cơ sở vật chất trong phòng.
Quản lý chi nhánh là người dùng nội bộ phụ trách điều hành toàn bộ một chi nhánh: phân ca làm việc cho nhân viên, theo dõi chấm công, đánh giá hiệu suất, quản lý kho hàng, xem thông tin khách hàng của chi nhánh và xem báo cáo doanh thu chi nhánh.
Chủ doanh nghiệp là người dùng cấp cao nhất, có quyền quản lý toàn bộ chuỗi karaoke: thêm/sửa/xóa chi nhánh, quản lý danh mục chung (menu, bảng giá phòng, chương trình khuyến mãi), quản lý toàn bộ danh sách khách hàng, cấu hình hạng hội viên, quản lý phòng hát và xem báo cáo tổng hợp toàn chuỗi.
2.3. Người dùng có những chức năng gì?
Khách hàng
Đặt phòng trực tuyến hoặc trực tiếp tại chi nhánh.
Quản lý thông tin cá nhân (tên, số điện thoại, hạng hội viên).
Tương tác dịch vụ trong phòng: gọi món qua app hoặc điện thoại nội bộ, yêu cầu dịch vụ bổ sung.
Nhân viên lễ tân
Quản lý đặt phòng: xếp phòng walk-in, xác nhận check-in booking online, tra cứu và tìm kiếm booking.
Quản lý trả phòng: tính tiền phòng, tổng hợp order, áp dụng ưu đãi hội viên/voucher, thu tiền, in hóa đơn.
Kiểm kê hàng tại quầy: đếm số lượng thực tế, tạo phiếu kiểm kê, báo cáo chênh lệch tồn kho.
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
2.4. Mỗi chức năng hoạt động như thế nào?
Đăng nhập
Người dùng cung cấp SĐT/Email và mật khẩu → Hệ thống xác thực thông tin đăng nhập → Hệ thống tạo phiên đăng nhập và chuyển người dùng đến trang chủ tương ứng vai trò.
Đăng ký
Khách hàng cung cấp Họ tên, SĐT, Email, Mật khẩu → Hệ thống kiểm tra SĐT và email chưa tồn tại → Hệ thống gửi mã OTP đến SĐT để xác minh → Khách hàng cung cấp mã OTP → Hệ thống tạo tài khoản hạng "Thường" và tự động đăng nhập.
Đổi mật khẩu
Người dùng cung cấp mật khẩu hiện tại và mật khẩu mới → Hệ thống xác minh mật khẩu hiện tại → Hệ thống kiểm tra mật khẩu mới hợp lệ → Hệ thống cập nhật mật khẩu và thu hồi tất cả phiên đăng nhập khác.

Quản lý tài khoản cá nhân
Khách hàng xem thông tin hồ sơ cá nhân (Họ tên, SĐT, Email, Hạng hội viên, Điểm tích lũy) → Khách hàng cập nhật Họ tên và Email → Hệ thống cập nhật hồ sơ.
Quản lý tài khoản nhân viên
Admin xem danh sách nhân viên → Admin thêm nhân viên mới (Họ tên, SĐT, Vai trò) → Hệ thống tạo tài khoản nhân viên → Admin sửa thông tin nhân viên → Hệ thống cập nhật → Admin xóa nhân viên → Hệ thống chuyển trạng thái "Đã nghỉ".
Đặt phòng trực tuyến
Khách hàng đăng nhập vào hệ thống web/app → Khách hàng chọn chi nhánh →  Khách hàng xem danh sách phòng trống theo khung giờ mong muốn →  Khách hàng chọn phòng và thời gian → Khách hàng xác nhận đặt phòng → Hệ thống ghi nhận booking với trạng thái "Chờ nhận" trên hệ thống.
Đặt phòng tại chi nhánh
Khách hàng đến trực tiếp chi nhánh → Lễ tân kiểm tra phòng trống → Lễ tân chọn chi nhánh →  Lễ tân xem danh sách phòng trống theo khung giờ mong muốn → Lễ tân chọn phòng và thời gian → Lễ tân ghi nhận thông tin khách (hoặc tra cứu hội viên qua số điện thoại) → Lễ tân xác nhận đặt phòng với khách hàng → Lễ tân tạo booking với trạng thái “Chờ nhận” trên hệ thống.
Check-in
Khách hàng yêu cầu nhận phòng → Lễ tân kiểm tra thông tin khách hàng và phòng đặt → Lễ tân xác nhận đúng thông tin → Hệ thống chuyển trạng thái phòng được đặt từ “Chờ nhận” sang “Đang hoạt động”.
Check-out
Khách hàng yêu cầu trả phòng → Lễ tân chọn phòng trên hệ thống → Hệ thống tự động tính tiền phòng (giờ sử dụng × đơn giá) cộng tổng tiền order gọi món → Nếu khách là hội viên, lễ tân áp dụng ưu đãi hoặc voucher →  Hệ thống hiển thị tổng tiền →  Khách hàng thanh toán (tiền mặt/chuyển khoản) → Lễ tân in hóa đơn → Hệ thống đóng phòng → Hệ thống chuyển trạng thái về "Trống" → Hệ thống cộng điểm hội viên tự động.
Huỷ phòng trực tuyến
Khách hàng ấn nút Huỷ đặt phòng trên hệ thống → Hệ thống hỏi người dùng xác nhận chắc chắn huỷ → Hệ thống chuyển trạng thái “Chờ nhận” ở ghi nhận booking sang “Trống” → Lễ tân bấm xác nhận “Huỷ đặt phòng”.
Huỷ phòng tại chi nhánh
Khách hàng huỷ đặt phòng trực tiếp tại chi nhánh → Lễ tân chuyển trạng thái “chờ nhận” ở ghi nhận booking sang “huỷ đặt”. Lễ tân bấm xác nhận “huỷ đặt phòng” và không hoàn tiền cọc cho khách hàng.
Gọi món / Tương tác dịch vụ
Khách yêu cầu gọi món qua app hoặc điện thoại nội bộ. Nhân viên phục vụ mở hệ thống trên tablet, chọn phòng tương ứng, thêm các món vào order, gửi order. Hệ thống thông báo đến bếp/bar để chuẩn bị. Nhân viên phục vụ mang đồ đến phòng và cập nhật trạng thái đã giao.
Quản lý order
Nhân viên phục vụ nhận order từ phòng, chuyển đến bếp/bar. Trước khi bếp xử lý, nhân viên có thể hủy hoặc thay đổi order. Sau khi giao, nhân viên cập nhật trạng thái và hệ thống tự động ghi vào hóa đơn của phòng.
Trả phòng & Thanh toán
Khách yêu cầu trả phòng, lễ tân chọn phòng trên hệ thống. Hệ thống tự động tính tiền phòng (giờ sử dụng × đơn giá) cộng tổng tiền order gọi món. Nếu khách là hội viên, lễ tân áp dụng ưu đãi hoặc voucher. Hệ thống hiển thị tổng tiền, khách thanh toán (tiền mặt/chuyển khoản), lễ tân in hóa đơn. Hệ thống đóng phòng, chuyển trạng thái về "Trống" và cộng điểm hội viên tự động.
Báo cáo tình trạng hàng hóa
Sau mỗi lượt phục vụ, nhân viên phục vụ kiểm tra cơ sở vật chất và cập nhật trạng thái phòng. Nếu phát hiện thiết bị hỏng, nhân viên báo hỏng hóc để kỹ thuật xử lý. Nếu minibar cần bổ sung, nhân viên gửi yêu cầu bổ sung qua hệ thống.
Kiểm kê hàng tại quầy
Nhân viên lễ tân đếm số lượng thực tế các mặt hàng tại quầy, tạo phiếu kiểm kê và lưu vào hệ thống. Nếu phát hiện chênh lệch so với tồn kho hệ thống, nhân viên báo cáo chênh lệch để quản lý xử lý đối soát.
Quản lý kho
Quản lý chi nhánh theo dõi tồn kho trên hệ thống. Khi hàng sắp hết, hệ thống cảnh báo. Quản lý duyệt phiếu nhập hàng hoặc gửi đơn mua hàng. Sau khi hàng về, nhân viên kiểm nhận và tạo phiếu nhập, cập nhật số lượng tồn kho. Khi giao hàng cho phòng, hệ thống tự động trừ tồn kho tương ứng.
Quản lý nhân viên chi nhánh
Quản lý chi nhánh đăng nhập vào hệ thống → Quản lý chi nhánh xem danh sách nhân viên của chi nhánh → Quản lý chi nhánh phân ca làm việc cho nhân viên theo ngày/tuần → Hệ thống ghi nhận chấm công thực tế của nhân viên → Quản lý chi nhánh đánh giá hiệu suất định kỳ → Quản lý chi nhánh thực hiện khen thưởng hoặc kỷ luật dựa trên kết quả đánh giá → Hệ thống lưu lại kết quả phân ca, đánh giá và quyết định.
Báo cáo số liệu chi nhánh
Quản lý chi nhánh chọn chức năng báo cáo → Quản lý chi nhánh chọn kỳ báo cáo (ngày/tuần/tháng/quý/năm) → Hệ thống tổng hợp doanh thu, công suất phòng, lượng khách và doanh số bán hàng trong kỳ → Hệ thống hiển thị số liệu dưới dạng bảng và biểu đồ → Quản lý chi nhánh xuất báo cáo ra file Excel/PDF.
Xem thông tin khách hàng chi nhánh:
Quản lý chi nhánh chọn chức năng xem thông tin khách hàng → Quản lý chi nhánh nhập từ khóa tìm kiếm theo tên hoặc số điện thoại → Hệ thống truy vấn danh sách khách hàng của chi nhánh → Hệ thống hiển thị danh sách khách hàng → Quản lý chi nhánh chọn một khách hàng → Hệ thống hiển thị lịch sử sử dụng và điểm tích lũy của khách hàng.
Quản lý hệ thống chi nhánh
Admin chọn chức năng quản lý chi nhánh → Hệ thống hiển thị danh sách chi nhánh → Admin chọn Thêm mới, Sửa hoặc Xóa → Hệ thống hiển thị form nhập liệu (với Thêm/Sửa) hoặc popup xác nhận (với Xóa) → Admin nhập thông tin hoặc bấm xác nhận → Hệ thống kiểm tra dữ liệu hợp lệ và các ràng buộc (không xóa chi nhánh đang hoạt động) → Hệ thống cập nhật CSDL và làm mới danh sách.
Quản lý khách hàng toàn hệ thống
Admin chọn chức năng quản lý khách hàng → Hệ thống hiển thị giao diện tìm kiếm → Admin nhập từ khóa và tìm kiếm → Hệ thống hiển thị danh sách kết quả → Admin chọn Xem chi tiết hoặc Khóa tài khoản → Hệ thống truy xuất và hiển thị lịch sử đặt phòng (nếu xem) hoặc yêu cầu xác nhận (nếu khóa) → Admin thao tác tương ứng → Hệ thống cập nhật trạng thái tài khoản nếu khóa.
Quản lý hạng hội viên
Admin chọn chức năng quản lý hạng hội viên → Hệ thống hiển thị danh sách cấu hình các hạng → Admin chọn Sửa cấu hình hoặc Thay đổi hạng thủ công cho khách hàng → Hệ thống hiển thị form tương ứng → Admin thay đổi thông số ngưỡng điểm/giảm giá hoặc chọn khách hàng và hạng mới → Admin xác nhận lưu → Hệ thống kiểm tra tính hợp lệ → Hệ thống cập nhật dữ liệu vào CSDL.
Quản lý danh mục loại phòng
Admin chọn chức năng quản lý loại phòng → Hệ thống hiển thị danh mục các loại phòng chuẩn → Admin chọn Thêm mới, Sửa hoặc Xóa loại phòng → Hệ thống hiển thị form cấu hình (Tên loại, Sức chứa chuẩn, Giá chung) hoặc popup xác nhận (nếu Xóa) → Admin nhập thông tin hoặc xác nhận → Hệ thống kiểm tra ràng buộc (không xóa loại phòng đang có chi nhánh sử dụng) → Hệ thống cập nhật bảng giá và tiêu chuẩn phòng xuống toàn bộ hệ thống.
Quản lý phòng hát tại chi nhánh
Quản lý chi nhánh chọn chức năng quản lý phòng hát → Hệ thống hiển thị danh sách phòng thuộc chi nhánh mình quản lý → Quản lý chọn Thêm mới, Sửa hoặc Xóa phòng → Hệ thống hiển thị form nhập liệu hoặc popup xác nhận → Quản lý nhập thông tin (Tên phòng, chọn chuẩn Loại phòng) hoặc xác nhận → Hệ thống kiểm tra dữ liệu và ràng buộc (không xóa phòng đang có lịch đặt) → Hệ thống cập nhật CSDL và làm mới danh sách phòng của chi nhánh.
Quản lý tài khoản nhân viên
Chủ doanh nghiệp chọn chức năng quản lý tài khoản nhân viên → Chủ doanh nghiệp tạo tài khoản mới cho nhân viên → Chủ doanh nghiệp gán phân quyền phù hợp với vai trò → Hệ thống mã hóa mật khẩu và lưu tài khoản → Chủ doanh nghiệp khóa, mở hoặc reset mật khẩu tài khoản khi cần → Hệ thống cập nhật trạng thái tài khoản.
 Tổng hợp báo cáo
Chủ doanh nghiệp chọn chức năng tổng hợp báo cáo → Chủ doanh nghiệp chọn khoảng thời gian và các chi nhánh → Hệ thống tổng hợp số liệu của toàn chuỗi → Hệ thống hiển thị biểu đồ so sánh hiệu suất giữa các chi nhánh và tổng doanh thu → Chủ doanh nghiệp xuất file báo cáo.
2.5. Những thông tin/đối tượng mà hệ thống cần xử lý
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
2.6. Quan hệ giữa các đối tượng
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

3. Mô hình nghiệp vụ bằng UML
3.1. Danh sách Actor
3.2. Các Use Case cho từng Actor


