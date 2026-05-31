## 1.2. Kịch bản "Check-in"

| Use case | Check-in |
|----------|----------|
| Actor | Nhân viên lễ tân |
| Tiền điều kiện | Nhân viên đã đăng nhập vào hệ thống. Phòng ở trạng thái "Chờ nhận" (đã được đặt trước đó). |
| Hậu điều kiện | Phòng chuyển trạng thái từ "Chờ nhận" sang "Đang hoạt động". Thời gian bắt đầu sử dụng được ghi nhận vào hệ thống. |
| Kịch bản chính | 1. Nhân viên lễ tân chọn chức năng "Check-in" trên giao diện chính.<br>2. Hệ thống hiển thị danh sách các booking có trạng thái "Chờ nhận" hôm nay, gồm: mã booking, tên khách hàng, số điện thoại, phòng, giờ đặt.<br>3. Nhân viên chọn booking cần check-in.<br>4. Hệ thống hiển thị thông tin chi tiết: tên khách, SĐT, phòng, giờ đặt, giờ dự kiến check-in.<br>5. Nhân viên xác nhận thông tin với khách hàng tại quầy.<br>6. Nhân viên nhấn nút [Xác nhận Check-in].<br>7. Hệ thống cập nhật trạng thái phòng từ "Chờ nhận" sang "Đang hoạt động".<br>8. Hệ thống ghi nhận thời gian bắt đầu sử dụng thực tế.<br>9. Hệ thống hiển thị thông báo "Check-in thành công! Phòng [tên phòng] đã sẵn sàng." |
| Ngoại lệ | 3a. Khách hàng không đến đúng giờ đặt:<br>3a.1 Nhân viên chọn hủy booking hoặc gia hạn thời gian chờ.<br>3a.2 Nếu hủy, hệ thống chuyển trạng thái booking sang "Đã hủy", phòng về "Trống".<br><br>6a. Phòng đang được dọn dẹp:<br>6a.1 Hệ thống hiển thị thông báo "Phòng đang dọn dẹp, vui lòng chờ.".<br>6a.2 Nhân viên chờ hoặc chuyển khách sang phòng khác.<br><br>6b. Thông tin booking không khớp:<br>6b.1 Nhân viên yêu cầu khách hàng cung cấp lại thông tin xác minh.<br>6b.2 Nếu không khớp, nhân viên liên hệ quản lý. |

## 1.3. Kịch bản "Check-out"

| Use case | Check-out |
|----------|----------|
| Actor | Nhân viên lễ tân |
| Tiền điều kiện | Nhân viên đã đăng nhập vào hệ thống. Phòng ở trạng thái "Đang hoạt động" (đã check-in trước đó). |
| Hậu điều kiện | Phòng chuyển trạng thái từ "Đang hoạt động" sang "Trống". Hóa đơn được tạo và thanh toán hoàn tất. Điểm tích lũy được cộng vào tài khoản hội viên (nếu có). |
| Kịch bản chính | 1. Nhân viên lễ tân chọn chức năng "Check-out" trên giao diện chính.<br>2. Hệ thống hiển thị danh sách các phòng đang ở trạng thái "Đang hoạt động", gồm: mã phòng, tên khách, giờ bắt đầu, thời gian sử dụng.<br>3. Nhân viên chọn phòng cần check-out.<br>4. Hệ thống hiển thị thông tin tổng hợp: thời gian sử dụng phòng, tiền phòng (giờ × đơn giá), tổng tiền order dịch vụ, tổng tiền trước giảm giá.<br>5. Nếu khách là hội viên, hệ thống tự động áp dụng ưu đãi hạng hội viên (% giảm giá).<br>6. Nhân viên nhập mã voucher (nếu có) và nhấn [Áp dụng].<br>7. Hệ thống hiển thị tổng tiền cần thanh toán sau giảm giá.<br>8. Khách hàng chọn phương thức thanh toán (tiền mặt / chuyển khoản).<br>9. Nhân viên chọn phương thức thanh toán và nhấn [Xác nhận thanh toán].<br>10. Hệ thống tạo hóa đơn, cập nhật trạng thái thanh toán "Đã thanh toán".<br>11. Hệ thống chuyển trạng thái phòng về "Trống".<br>12. Nếu khách là hội viên, hệ thống cộng điểm tích lũy tự động.<br>13. Hệ thống hiển thị thông báo "Check-out thành công! Tổng tiền: [X]đ." và nút [In hóa đơn]. |
| Ngoại lệ | 3a. Phòng có order dịch vụ chưa được xác nhận:<br>3a.1 Hệ thống cảnh báo "Có [N] order chưa xác nhận.".<br>3a.2 Nhân viên xác nhận hoặc hủy các order trước khi tiếp tục.<br><br>5a. Khách hàng không phải hội viên:<br>5a.1 Hệ thống bỏ qua bước áp dụng ưu đãi hạng.<br><br>8a. Khách hàng khiếu nại hóa đơn:<br>8a.1 Nhân viên chỉnh sửa hóa đơn (thêm/bớt mục) trước khi xác nhận.<br>8a.2 Nếu cần, nhân viên liên hệ quản lý để xử lý.<br><br>9a. Thanh toán chuyển khoản thất bại:<br>9a.1 Hệ thống hiển thị lỗi, yêu cầu chọn lại phương thức.<br>9a.2 Nhân viên xác nhận với khách và thử lại. |

## 1.4. Kịch bản "Huỷ phòng"

| Use case | Huỷ phòng |
|----------|----------|
| Actor | Nhân viên lễ tân, khách hàng |
| Tiền điều kiện | Booking ở trạng thái "Chờ nhận" (chưa check-in). |
| Hậu điều kiện | Booking chuyển trạng thái sang "Đã hủy". Phòng về trạng thái "Trống". Tiền cọc (nếu có) được xử lý theo chính sách hoàn tiền. |
| Kịch bản chính | 1. Khách hàng liên hệ lễ tân (trực tiếp hoặc qua hotline) yêu cầu hủy phòng.<br>2. Nhân viên lễ tân chọn chức năng "Quản lý đặt phòng" trên giao diện.<br>3. Hệ thống hiển thị danh sách booking trạng thái "Chờ nhận".<br>4. Nhân viên tìm booking của khách hàng theo tên, SĐT, hoặc mã booking.<br>5. Nhân viên chọn booking cần hủy.<br>6. Hệ thống hiển thị thông tin chi tiết: tên khách, phòng, giờ đặt, tiền cọc (nếu có).<br>7. Nhân viên nhấn nút [Hủy đặt phòng].<br>8. Hệ thống hiển thị xác nhận "Bạn có chắc chắn muốn hủy booking này?".<br>9. Nhân viên xác nhận [Đồng ý].<br>10. Hệ thống cập nhật trạng thái booking sang "Đã hủy".<br>11. Hệ thống chuyển trạng thái phòng về "Trống".<br>12. Hệ thống hiển thị thông báo "Hủy đặt phòng thành công." |
| Ngoại lệ | 4a. Không tìm thấy booking:<br>4a.1 Nhân viên yêu cầu khách hàng cung cấp lại thông tin.<br>4a.2 Nếu vẫn không tìm thấy, thông báo "Không tìm thấy booking phù hợp.".<br><br>7a. Booking đã quá thời gian cho phép hủy:<br>7a.1 Hệ thống hiển thị "Booking đã quá thời gian hủy, không thể hủy.".<br>7a.2 Nhân viên thông báo cho khách hàng.<br><br>9a. Khách hàng yêu cầu hoàn tiền cọc:<br>9a.1 Nhân viên kiểm tra chính sách hoàn tiền.<br>9a.2 Nếu đủ điều kiện, nhân viên xử lý hoàn tiền thủ công (ngoài hệ thống). |
