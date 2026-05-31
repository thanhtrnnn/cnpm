## Bảng thuật ngữ

| Thuật ngữ | Tên tiếng Anh | Định nghĩa |
|-----------|--------------|------------|
| Loại phòng | Room Type / Room Category | Phân loại phòng hát dựa trên tiêu chuẩn, diện tích và trang thiết bị (VD: Standard, VIP, Super VIP, Party). |
| Sức chứa | Capacity | Số lượng khách tối đa mà một phòng hát có thể phục vụ thoải mái nhất. |
| Trạng thái phòng | Room Status | Tình trạng hiện tại của phòng trên hệ thống (Trống, Đang phục vụ, Đã đặt trước, Đang dọn dẹp, Bảo trì). |
| Đặt phòng tại quầy | Book on site | Khách hàng đến trực tiếp chi nhánh để yêu cầu xếp phòng hát. |
| Đặt phòng trực tuyến | Book online | Giao dịch giữ phòng trước cho khách thông qua hệ thống web/app. |
| Tiền cọc | Deposit | Khoản tiền khách thanh toán trước để đảm bảo cho việc đặt phòng. |
| Nhận phòng/ Trả phòng | Check-in/ Check-out | Thao tác bắt đầu tính giờ sử dụng phòng và thao tác kết thúc tính giờ để thanh toán. |
| Huỷ đặt phòng | Cancel Booking | Thao tác khách hàng huỷ yêu cầu giữ phòng trước thời điểm nhận phòng. |
| Chi nhánh | Branch | Cơ sở kinh doanh karaoke thuộc chuỗi, có địa chỉ, nhân viên và phòng hát riêng. |
| Áp dụng voucher | Apply Voucher | Thao tác nhập mã giảm giá hoặc sử dụng điểm hội viên để trừ vào tổng hóa đơn. |

## Mô hình nghiệp vụ bằng ngôn ngữ tự nhiên

### 2.1. Mục tiêu mô-đun

Thực hiện chức năng quản lý đặt phòng, huỷ phòng để tham gia vào xây dựng hệ thống phần mềm quản lý tập trung cho chuỗi nhà hàng karaoke.

### 2.2. Phạm vi mô-đun

Mô-đun sẽ bao phủ toàn bộ quy trình vận hành từ khi khách hàng đặt phòng đến khi thanh toán.

### 2.3. Ai có thể sử dụng mô-đun?

Mô-đun sẽ phục vụ 2 nhóm người chính:
- **Khách hàng** là nhóm người sẽ tham gia vào các thao tác đặt phòng, huỷ phòng, thanh toán.
- **Nhân viên lễ tân** là người trực tiếp tham gia vào thao tác đặt phòng, check-in/ check-out, tổng hợp hoá đơn và thu tiền của khách.

### 2.4. Người dùng có những chức năng gì?

**Khách hàng:**
- Đặt phòng trực tuyến hoặc đặt phòng tại chi nhánh.
- Huỷ phòng trực tuyến hoặc huỷ phòng tại chi nhánh.
- Check-in/ check-out.
- Thanh toán.

**Nhân viên lễ tân:**
- Đặt phòng.
- Huỷ phòng.
- Check-in/ check-out.
- Tổng hợp hoá đơn.
- Áp dụng ưu đãi hội viên.
- Thu tiền.
- In hoá đơn.

### 2.5. Mỗi chức năng hoạt động như thế nào?

**Đặt phòng trực tuyến:** Khách hàng đăng nhập vào hệ thống web/app → Khách hàng chọn chi nhánh → Khách hàng xem danh sách phòng trống theo khung giờ mong muốn → Khách hàng chọn phòng và thời gian → Khách hàng xác nhận đặt phòng → Hệ thống ghi nhận booking với trạng thái "Chờ nhận" trên hệ thống.

**Đặt phòng tại chi nhánh:** Khách hàng đến trực tiếp chi nhánh → Lễ tân kiểm tra phòng trống → Lễ tân chọn chi nhánh → Lễ tân xem danh sách phòng trống theo khung giờ mong muốn → Lễ tân chọn phòng và thời gian → Lễ tân ghi nhận thông tin khách (hoặc tra cứu hội viên qua số điện thoại) → Lễ tân xác nhận đặt phòng với khách hàng → Lễ tân tạo booking với trạng thái "Chờ nhận" trên hệ thống.

**Check-in:** Khách hàng yêu cầu nhận phòng → Lễ tân kiểm tra thông tin khách hàng và phòng đặt → Lễ tân xác nhận đúng thông tin → Hệ thống chuyển trạng thái phòng được đặt từ "Chờ nhận" sang "Đang hoạt động".

**Check-out:** Khách hàng yêu cầu trả phòng → Lễ tân chọn phòng trên hệ thống → Hệ thống tự động tính tiền phòng (giờ sử dụng × đơn giá) cộng tổng tiền order gọi món → Nếu khách là hội viên, lễ tân áp dụng ưu đãi hoặc voucher → Hệ thống hiển thị tổng tiền → Khách hàng thanh toán (tiền mặt/chuyển khoản) → Lễ tân in hóa đơn → Hệ thống đóng phòng → Hệ thống chuyển trạng thái về "Trống" → Hệ thống cộng điểm hội viên tự động.

**Huỷ phòng trực tuyến:** Khách hàng ấn nút Huỷ đặt phòng trên hệ thống → Hệ thống hỏi người dùng xác nhận chắc chắn huỷ → Hệ thống chuyển trạng thái "Chờ nhận" ở ghi nhận booking sang "Trống" → Lễ tân bấm xác nhận "Huỷ đặt phòng".

**Huỷ phòng tại chi nhánh:** Khách hàng huỷ đặt phòng trực tiếp tại chi nhánh → Lễ tân chuyển trạng thái "chờ nhận" ở ghi nhận booking sang "huỷ đặt". Lễ tân bấm xác nhận "huỷ đặt phòng" và không hoàn tiền cọc cho khách hàng.

### 2.6. Những thông tin/ đối tượng mà mô-đun cần xử lý

Mô-đun cần quản lý và xử lý các đối tượng thông tin chính sau:
- **Chi nhánh:** Mã chi nhánh, tên, địa chỉ, số điện thoại.
- **Khách hàng:** Mã khách hàng, họ tên, số điện thoại, địa chỉ, hạng hội viên (Thường, Bạc, Vàng), trạng thái tài khoản.
- **Nhân viên:** Mã nhân viên, họ tên, vai trò, chi nhánh làm việc, trạng thái (đang làm/ đã nghỉ).
- **Hạng hội viên:** Mã hạng, tên hạng, ngưỡng điểm tối thiểu, ưu đãi (% giảm giá, điểm thưởng nhận).
- **Phòng hát:** Mã phòng, tên phòng, loại phòng, sức chứa, giá theo giờ, trạng thái, thuộc chi nhánh.
- **Khuyến mãi:** Mã khuyến mãi, tên, loại (voucher/ giảm giá %), điều kiện áp dụng, thời gian hiệu lực.
- **Hoá đơn:** Mã hoá đơn, liên kết đặt phòng, tiền phòng, thời gian sử dụng thực tế, tiền dịch vụ, phụ phí, giảm giá, tổng tiền, trạng thái thanh toán, phương thức thanh toán.

### 2.7. Quan hệ giữa các đối tượng

Các đối tượng trong mô-đun có mối quan hệ chặt chẽ với nhau:
- Một chi nhánh có nhiều phòng hát.
- Một khách hàng thuộc một hạng hội viên.
- Một hạng hội viên định nghĩa ngưỡng điểm và áp dụng cho nhiều khách hàng.
- Một nhân viên thuộc một chi nhánh.
- Một hoá đơn có thể áp dụng nhiều khuyến mãi.

## Mô hình nghiệp vụ bằng UML

### 3.1. Danh sách Actor

| STT | Actor | Mô tả |
|-----|-------|-------|
| 1 | Khách hàng (gián tiếp) | Người sử dụng dịch vụ karaoke, truy cập qua web/app hoặc tới tận chi nhánh để đặt phòng; thanh toán; quản lý tài khoản cá nhân. |
| 2 | Nhân viên lễ tân (trực tiếp) | Nhân viên tại quầy, xử lý đặt phòng, check-in/ check-out, thu tiền, in hoá đơn. |

### 3.2. Các Use Case cho từng Actor

| Actor | Use Case |
|-------|----------|
| Khách hàng | UC05 - Đặt phòng |
|  | UC - Huỷ phòng |
| Nhân viên lễ tân | UC05 - Đặt phòng |
|  | UC - Huỷ phòng |
|  | UC07 - Check-in |
|  | UC08 - Check-out |

### 3.3. Biểu đồ Use Case tổng quan của mô-đun

<!-- PLACEHOLDER: UC tong quan diagram -->

### 3.4. Biểu đồ Use Case phân rã của mô-đun

<!-- PLACEHOLDER: UC phan ra diagram -->
