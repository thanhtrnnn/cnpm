<!-- REVIEW FILE — XÁC ĐỊNH YÊU CẦU mục 2.4 (đã sửa theo audit)
   Heading H2 ↔ ## (HEADING_2 trong GDocs), function names = bold paragraph.
   Mỗi luồng = một chuỗi → liền mạch từ đầu đến cuối, không nhãn phụ. -->

## 2.4. Mỗi chức năng hoạt động như thế nào?

**UC01 – Đăng nhập**

Người dùng nhập SĐT/Email và mật khẩu → Hệ thống xác thực thông tin đăng nhập → Hệ thống tạo phiên đăng nhập → Hệ thống chuyển người dùng đến trang chủ tương ứng vai trò.

Người dùng nhập sai mật khẩu → Hệ thống thông báo lỗi xác thực → Người dùng nhập lại (tối đa 5 lần).

Tài khoản bị khóa → Hệ thống hiển thị thông báo tài khoản bị khóa → Người dùng liên hệ Admin.

---

**UC02 – Đăng ký**

Khách hàng nhập Họ tên, SĐT, Email, Mật khẩu → Hệ thống kiểm tra SĐT và Email chưa tồn tại → Hệ thống gửi mã OTP đến SĐT → Khách hàng nhập mã OTP → Hệ thống xác minh OTP hợp lệ → Hệ thống tạo tài khoản hạng "Thường" → Hệ thống tự động đăng nhập.

SĐT hoặc Email đã tồn tại → Hệ thống thông báo trùng lặp → Khách hàng dùng thông tin khác hoặc chọn Đăng nhập.

OTP sai hoặc hết hạn (5 phút) → Hệ thống thông báo lỗi OTP → Khách hàng yêu cầu gửi lại OTP.

---

**UC03 – Đổi mật khẩu**

Người dùng nhập mật khẩu hiện tại và mật khẩu mới → Hệ thống xác minh mật khẩu hiện tại đúng → Hệ thống kiểm tra mật khẩu mới hợp lệ → Hệ thống cập nhật mật khẩu → Hệ thống thu hồi tất cả phiên đăng nhập khác.

Mật khẩu hiện tại không đúng → Hệ thống thông báo lỗi → Người dùng thử lại.

Mật khẩu mới không hợp lệ → Hệ thống hiển thị yêu cầu định dạng → Người dùng nhập lại.

---

**UC04 – Quản lý thông tin cá nhân**

Khách hàng xem hồ sơ cá nhân (Họ tên, SĐT, Email, Hạng hội viên, Điểm tích lũy) → Khách hàng chỉnh sửa Họ tên hoặc Email → Hệ thống kiểm tra Email chưa tồn tại → Hệ thống cập nhật hồ sơ → Hệ thống hiển thị thông báo thành công.

---

**UC05 – Đặt phòng**

*Đặt phòng trực tuyến:*
Khách hàng đăng nhập → Khách hàng chọn chi nhánh và khung giờ → Hệ thống hiển thị danh sách phòng trống → Khách hàng chọn phòng và xác nhận → Hệ thống ghi nhận booking trạng thái "Chờ nhận" → Hệ thống gửi thông báo xác nhận đến khách hàng.

*Đặt phòng tại chi nhánh:*
Khách hàng đến chi nhánh → Lễ tân tra cứu phòng trống theo khung giờ → Lễ tân ghi nhận thông tin khách (hoặc tra cứu hội viên qua SĐT) → Lễ tân chọn phòng và xác nhận với khách → Hệ thống tạo booking trạng thái "Chờ nhận".

*Hủy phòng trực tuyến:*
Khách hàng chọn booking cần hủy → Khách hàng bấm Hủy đặt phòng → Hệ thống yêu cầu xác nhận → Khách hàng xác nhận → Hệ thống chuyển trạng thái booking sang "Đã hủy" → Hệ thống giải phóng slot phòng.

*Hủy phòng tại chi nhánh:*
Khách hàng yêu cầu hủy trực tiếp → Lễ tân tra cứu booking → Lễ tân xác nhận hủy trên hệ thống → Hệ thống chuyển trạng thái sang "Đã hủy" → Hệ thống ghi nhận không hoàn tiền cọc.

---

**UC06 – Gọi món / Quản lý order**

*Tạo order:*
Khách hàng yêu cầu gọi món → Nhân viên phục vụ mở hệ thống, chọn phòng tương ứng → Nhân viên thêm các món vào order → Nhân viên gửi order → Hệ thống ghi nhận order và thông báo đến bếp/bar.

*Cập nhật hoặc hủy order (trước khi bếp xử lý):*
Nhân viên chọn order cần thay đổi → Nhân viên sửa số lượng hoặc hủy món → Hệ thống cập nhật order → Hệ thống thông báo lại bếp/bar.

*Giao món và ghi nhận:*
Nhân viên mang đồ đến phòng → Nhân viên cập nhật trạng thái order sang "Đã giao" → Hệ thống tự động ghi chi tiết order vào hóa đơn phòng.

---

**UC07 – Quản lý đặt phòng (check-in)**

Khách hàng đến nhận phòng → Lễ tân tra cứu booking theo tên/SĐT → Lễ tân xác nhận đúng thông tin khách và phòng → Hệ thống chuyển trạng thái booking từ "Chờ nhận" sang "Đang hoạt động" → Hệ thống ghi nhận thời gian check-in thực tế.

---

**UC08 – Quản lý trả phòng (check-out)**

Khách hàng yêu cầu trả phòng → Lễ tân chọn phòng trên hệ thống → Hệ thống tính tiền phòng (giờ thực tế × đơn giá) cộng tổng tiền order → Lễ tân áp dụng ưu đãi hoặc voucher nếu khách là hội viên → Hệ thống hiển thị tổng tiền → Khách hàng thanh toán (tiền mặt / chuyển khoản) → Lễ tân in hóa đơn → Hệ thống đóng phòng, chuyển trạng thái về "Trống" → Hệ thống cộng điểm hội viên tự động.

---

**UC10 – Báo cáo tình trạng hàng hóa**

Sau mỗi lượt phục vụ, nhân viên phục vụ chọn phòng vừa phục vụ trên hệ thống → Nhân viên kiểm tra cơ sở vật chất trong phòng → Nhân viên cập nhật trạng thái phòng → Nếu phát hiện thiết bị hỏng, nhân viên tạo phiếu báo hỏng hóc → Nếu minibar cần bổ sung, nhân viên gửi yêu cầu bổ sung → Hệ thống ghi nhận và thông báo đến Quản lý chi nhánh.

---

**UC11 – Quản lý nhân viên chi nhánh**

Quản lý chi nhánh xem danh sách nhân viên của chi nhánh → Quản lý phân ca làm việc cho nhân viên theo ngày/tuần → Hệ thống ghi nhận lịch ca và chấm công thực tế → Quản lý đánh giá hiệu suất định kỳ → Quản lý thực hiện khen thưởng hoặc kỷ luật → Hệ thống lưu kết quả phân ca, đánh giá và quyết định.

---

**UC12 – Quản lý kho**

Quản lý chi nhánh theo dõi tồn kho trên hệ thống → Khi hàng sắp hết, hệ thống cảnh báo tự động → Quản lý duyệt phiếu nhập hàng hoặc gửi đơn mua hàng → Hàng về, nhân viên kiểm nhận và tạo phiếu nhập → Hệ thống cập nhật số lượng tồn kho → Khi phục vụ order, hệ thống tự động trừ tồn kho tương ứng.

---

**UC13 – Báo cáo số liệu chi nhánh**

Quản lý chi nhánh chọn chức năng báo cáo → Quản lý chọn kỳ báo cáo (ngày/tuần/tháng/quý/năm) → Hệ thống tổng hợp doanh thu, công suất phòng, lượng khách và doanh số bán hàng → Hệ thống hiển thị số liệu dạng bảng và biểu đồ → Quản lý xuất báo cáo ra file Excel/PDF.

---

**UC14 – Xem thông tin khách hàng chi nhánh**

Quản lý chi nhánh nhập từ khóa tìm kiếm (tên hoặc SĐT) → Hệ thống truy vấn danh sách khách hàng của chi nhánh → Hệ thống hiển thị danh sách kết quả → Quản lý chọn một khách hàng → Hệ thống hiển thị lịch sử sử dụng và điểm tích lũy.

---

**UC15 – Quản lý menu**

*Xem và lọc menu:*
Quản lý chi nhánh chọn chức năng quản lý menu → Hệ thống hiển thị danh sách món ăn/đồ uống → Quản lý lọc theo danh mục → Hệ thống hiển thị danh sách đã lọc.

*Thêm hoặc sửa món:*
Quản lý chọn Thêm mới hoặc Sửa → Hệ thống hiển thị form (Tên món, Loại, Đơn giá, Mô tả, Trạng thái) → Quản lý nhập thông tin → Hệ thống kiểm tra dữ liệu hợp lệ → Hệ thống lưu và làm mới danh sách.

*Ẩn hoặc xóa món:*
Quản lý chọn món cần xóa hoặc ẩn → Hệ thống hiển thị xác nhận → Quản lý xác nhận → Hệ thống cập nhật trạng thái "Ngừng kinh doanh" hoặc xóa khỏi danh mục.

---

**UC16 – Quản lý hệ thống chi nhánh**

Admin chọn chức năng quản lý chi nhánh → Hệ thống hiển thị danh sách chi nhánh → Admin chọn Thêm mới, Sửa hoặc Xóa → Hệ thống hiển thị form nhập liệu (Thêm/Sửa) hoặc popup xác nhận (Xóa) → Admin nhập thông tin hoặc xác nhận → Hệ thống kiểm tra ràng buộc (không xóa chi nhánh đang hoạt động) → Hệ thống cập nhật CSDL và làm mới danh sách.

---

**UC17 – Quản lý khách hàng toàn hệ thống**

Admin nhập từ khóa và tìm kiếm → Hệ thống hiển thị danh sách kết quả toàn chuỗi → Admin chọn Xem chi tiết hoặc Khóa tài khoản → Hệ thống truy xuất lịch sử đặt phòng (nếu xem) hoặc yêu cầu xác nhận (nếu khóa) → Admin thực hiện thao tác → Hệ thống cập nhật trạng thái tài khoản.

---

**UC18 – Quản lý hạng hội viên**

Admin xem danh sách cấu hình các hạng (Thường/Bạc/Vàng) → Admin chọn Sửa cấu hình ngưỡng điểm/ưu đãi hoặc Thay đổi hạng thủ công cho khách hàng → Hệ thống hiển thị form tương ứng → Admin thay đổi thông số hoặc chọn khách hàng và hạng mới → Admin xác nhận → Hệ thống kiểm tra tính hợp lệ → Hệ thống cập nhật CSDL.

---

**UC19 – Quản lý phòng hát**

*Quản lý danh mục loại phòng (Admin):*
Admin chọn chức năng quản lý loại phòng → Hệ thống hiển thị danh mục loại phòng chuẩn → Admin chọn Thêm mới, Sửa hoặc Xóa → Hệ thống hiển thị form (Tên loại, Sức chứa, Giá chung) hoặc xác nhận xóa → Admin nhập thông tin hoặc xác nhận → Hệ thống kiểm tra ràng buộc (không xóa loại đang được chi nhánh sử dụng) → Hệ thống cập nhật tiêu chuẩn phòng toàn hệ thống.

*Quản lý phòng vật lý tại chi nhánh (Quản lý chi nhánh):*
Quản lý chọn chức năng quản lý phòng của chi nhánh → Hệ thống hiển thị danh sách phòng thuộc chi nhánh → Quản lý chọn Thêm mới, Sửa hoặc Xóa → Hệ thống hiển thị form (Tên phòng, Loại phòng) hoặc xác nhận xóa → Quản lý nhập thông tin hoặc xác nhận → Hệ thống kiểm tra ràng buộc (không xóa phòng đang có lịch đặt) → Hệ thống cập nhật CSDL chi nhánh.

---

**UC20 – Quản lý tài khoản nhân viên**

Chủ doanh nghiệp xem danh sách tài khoản nhân viên → Chủ doanh nghiệp tạo tài khoản mới (Họ tên, SĐT, Vai trò, Chi nhánh) → Hệ thống tạo tài khoản và mã hóa mật khẩu mặc định → Chủ doanh nghiệp gán phân quyền phù hợp với vai trò → Khi cần, Chủ doanh nghiệp khóa, mở hoặc reset mật khẩu tài khoản → Hệ thống cập nhật trạng thái tài khoản.

---

**UC21 – Tổng hợp báo cáo toàn chuỗi**

Chủ doanh nghiệp chọn khoảng thời gian và các chi nhánh cần xem → Hệ thống tổng hợp số liệu toàn chuỗi → Hệ thống hiển thị biểu đồ so sánh hiệu suất giữa các chi nhánh và tổng doanh thu → Chủ doanh nghiệp xuất file báo cáo (Excel/PDF).
