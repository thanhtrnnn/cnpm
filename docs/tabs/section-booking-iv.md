## IV. PHA CÀI ĐẶT VÀ KIỂM THỬ

### 1.1. Lập kế hoạch test

**Phạm vi test:** Module "Quản lý đặt và trả phòng" — 4 chức năng: Đặt phòng, Check-in, Check-out, Huỷ phòng.

**Loại test:** Functional testing (kiểm thử chức năng) — kiểm tra từng chức năng theo kịch bản sử dụng thực tế.

**Nguyên tắc test:**
- Test case bao gồm: CSDL trước test → Kịch bản thực hiện → Kết quả mong đợi → CSDL sau test
- CSDL mẫu dùng dữ liệu tiếng Việt, tên riêng Việt Nam
- Dữ liệu trong CSDL phải khớp với ERD (III.2) và Entity class (III.1)
- Kết quả mong đợi PHẢI liệt kê TOÀN BỘ UI elements khi sang giao diện mới

| STT | Chức năng | Trường hợp cần test |
|-----|-----------|---------------------|
| 1 | Đặt phòng | Đặt phòng thành công khi có phòng trống |
| 2 | Đặt phòng | Không tìm thấy phòng trống theo thời gian yêu cầu |
| 3 | Đặt phòng | Khách hàng chưa có trong CSDL |
| 4 | Đặt phòng | Đặt phòng trực tuyến thành công |
| 5 | Check-in | Check-in thành công với booking trạng thái "Chờ nhận" |
| 6 | Check-in | Phòng đang dọn dẹp, không thể check-in |
| 7 | Check-in | Check-in phòng Super VIP |
| 8 | Check-out | Check-out thành công, thanh toán tiền mặt |
| 9 | Check-out | Check-out với voucher giảm giá |
| 10 | Check-out | Check-out với hội viên Vàng |
| 11 | Check-out | Voucher không hợp lệ |
| 12 | Check-out | Check-out chuyển khoản |
| 13 | Huỷ phòng | Hủy đặt phòng thành công |
| 14 | Huỷ phòng | Không tìm thấy booking |
| 15 | Huỷ phòng | Booking đã quá thời gian hủy |

---

### 1.2. Các test case cho từng chức năng

#### a) Chức năng "Đặt phòng"

**TC01: Đặt phòng thành công**

CSDL trước khi test:
```
tblBranch:
| branchID | name               | address                    |
|----------|--------------------|-----------------------------|
| 1        | Karaoke Quận 1     | 123 Lê Lợi, Q1, TP.HCM    |
| 2        | Karaoke Quận 3     | 456 Nguyễn Đình Chiểu, Q3  |

tblRoom:
| roomID | name   | type      | hourly_pricing | status | branchID |
|--------|--------|-----------|----------------|--------|----------|
| 1      | P.VIP1 | VIP       | 150000         | Trống  | 1        |
| 2      | P.Std3 | Standard  | 80000          | Trống  | 1        |
| 3      | P.SVIP1| Super VIP | 250000         | Trống  | 1        |
| 4      | P.VIP2 | VIP       | 150000         | Trống  | 2        |

tblClient:
| clientID | name           | phone_number | account_status | rankingID |
|----------|----------------|--------------|----------------|-----------|
| 1        | Nguyễn Văn An  | 0912345678   | active         | 2         |
| 2        | Trần Thị Bình  | 0987654321   | active         | 1         |
| 3        | Lê Minh Châu    | 0901122334   | active         | 3         |

tblEmployee:
| employeeID | name           | role    | branchID |
|------------|----------------|---------|----------|
| 1          | Phạm Thị Dung  | Lễ tân  | 1        |
| 2          | Hoàng Văn Em   | Lễ tân  | 2        |

tblMemberRanking:
| rankingID | name   | base_score | coupon |
|-----------|--------|------------|--------|
| 1         | Thường | 0          | 0      |
| 2         | Bạc    | 1000       | 10     |
| 3         | Vàng   | 5000       | 15     |
```

CSDL sau khi test:
```
tblRoom:
| roomID | name   | status   |
|--------|--------|----------|
| 1      | P.VIP1 | Chờ nhận |

tblRoom_receipt:
| room_receipt_ID | checkin_time        | checkout_time | room_fee | service_fee | discount | status   | payment_method | clientID | employeeID | roomID |
|-----------------|---------------------|---------------|----------|-------------|----------|----------|----------------|----------|------------|--------|
| 1               | 2026-06-01 14:00:00 | NULL          | NULL     | NULL        | NULL     | Chờ nhận | NULL           | 1        | 1          | 1      |
```

| Các bước thực hiện | Kết quả mong đợi |
|---------------------|------------------|
| 1. NV Phạm Thị Dung click [Đặt phòng] trên ReceptionistHomePage | Hiển thị SearchFreeRoomForm: ô chọn ngày, ô nhập giờ bắt đầu, ô nhập giờ kết thúc, dropdown chi nhánh, nút [Tìm phòng trống] |
| 2. NV nhập: ngày 01/06/2026, từ 14:00, đến 17:00, chi nhánh "Karaoke Quận 1" | Form hiển thị đầy đủ các trường đã nhập |
| 3. NV click [Tìm phòng trống] | Hiển thị danh sách phòng trống: P.VIP1 (150.000đ/giờ), P.Std3 (80.000đ/giờ), P.SVIP1 (250.000đ/giờ) |
| 4. NV chọn P.VIP1 | Chuyển sang SearchClientForm: ô nhập tìm kiếm, nút [Tìm kiếm], label "Phòng: P.VIP1" |
| 5. NV nhập "0912345678" và click [Tìm kiếm] | Hiển thị: Nguyễn Văn An, SĐT 0912345678, Hạng Bạc, nút [Chọn] |
| 6. NV click [Chọn] khách hàng | Chuyển sang ConfirmBookingModal: thông tin phòng (P.VIP1, 14:00-17:00), thông tin khách (Nguyễn Văn An), tổng tiền dự kiến, nút [Xác nhận đặt phòng], nút [Hủy] |
| 7. NV click [Xác nhận đặt phòng] | Hiển thị thông báo "Đặt phòng thành công!", nút [OK] |

---

**TC02: Không tìm thấy phòng trống theo thời gian yêu cầu**

CSDL trước khi test:
```
tblRoom:
| roomID | name   | type      | hourly_pricing | status         | branchID |
|--------|--------|-----------|----------------|----------------|----------|
| 1      | P.VIP1 | VIP       | 150000         | Đang hoạt động | 1        |
| 2      | P.Std3 | Standard  | 80000          | Chờ nhận       | 1        |
| 3      | P.SVIP1| Super VIP | 250000         | Đang dọn dẹp   | 1        |
```

CSDL sau khi test: Không thay đổi.

| Các bước thực hiện | Kết quả mong đợi |
|---------------------|------------------|
| 1. NV click [Đặt phòng] | Hiển thị SearchFreeRoomForm: ô chọn ngày, ô nhập giờ bắt đầu, ô nhập giờ kết thúc, dropdown chi nhánh, nút [Tìm phòng trống] |
| 2. NV nhập: ngày 01/06/2026, từ 14:00, đến 17:00 | Form hiển thị đầy đủ |
| 3. NV click [Tìm phòng trống] | Hiển thị thông báo "Không có phòng trống trong khung giờ này." Danh sách kết quả trống |

---

**TC03: Khách hàng chưa có trong CSDL**

CSDL trước khi test:
```
tblRoom:
| roomID | name   | status | branchID |
|--------|--------|--------|----------|
| 1      | P.VIP1 | Trống  | 1        |

tblClient:
| clientID | name           | phone_number | account_status | rankingID |
|----------|----------------|--------------|----------------|-----------|
| 1        | Nguyễn Văn An  | 0912345678   | active         | 2         |
```

CSDL sau khi test:
```
tblClient:
| clientID | name           | phone_number | account_status | rankingID |
|----------|----------------|--------------|----------------|-----------|
| 4        | Phạm Văn Phúc  | 0999999999   | active         | 1         |
```

| Các bước thực hiện | Kết quả mong đợi |
|---------------------|------------------|
| 1. NV chọn P.VIP1 | Chuyển sang SearchClientForm: ô nhập tìm kiếm, nút [Tìm kiếm] |
| 2. NV nhập "0999999999" và click [Tìm kiếm] | Hiển thị thông báo "Không tìm thấy khách hàng." Nút [Đăng ký nhanh] xuất hiện |
| 3. NV click [Đăng ký nhanh] | Hiển thị form đăng ký nhanh: ô nhập họ tên, ô nhập SĐT, nút [Xác nhận], nút [Hủy] |
| 4. NV nhập: "Phạm Văn Phúc", "0999999999" | Form hiển thị đầy đủ |
| 5. NV click [Xác nhận] | Tạo khách hàng mới, quay về SearchClientForm với khách vừa tạo |

---

**TC04: Đặt phòng trực tuyến thành công**

CSDL trước khi test:
```
tblRoom:
| roomID | name   | type | hourly_pricing | status | branchID |
|--------|--------|------|----------------|--------|----------|
| 5      | P.VIP3 | VIP  | 150000         | Trống  | 2        |

tblClient:
| clientID | name          | phone_number | account_status | rankingID |
|----------|---------------|--------------|----------------|-----------|
| 5        | Vũ Thị Giang  | 0911223344   | active         | 1         |
```

CSDL sau khi test:
```
tblRoom:
| roomID | name   | status   |
|--------|--------|----------|
| 5      | P.VIP3 | Chờ nhận |

tblRoom_receipt:
| room_receipt_ID | checkin_time        | checkout_time | status   | clientID | roomID |
|-----------------|---------------------|---------------|----------|----------|--------|
| 5               | 2026-06-02 19:00:00 | NULL          | Chờ nhận | 5        | 5      |
```

| Các bước thực hiện | Kết quả mong đợi |
|---------------------|------------------|
| 1. KH truy cập web/app | Hiển thị trang chủ: danh sách chi nhánh, nút [Đặt phòng] |
| 2. KH chọn chi nhánh "Karaoke Quận 3" | Hiển thị danh sách phòng: P.VIP3 (150.000đ/giờ), trạng thái Trống |
| 3. KH nhập thời gian: 02/06/2026, 19:00-22:00 | Form hiển thị đầy đủ |
| 4. KH click [Tìm phòng trống] | Hiển thị: P.VIP3 (150.000đ/giờ) |
| 5. KH chọn P.VIP3 | Hiển thị thông tin phòng và thời gian, nút [Xác nhận đặt phòng] |
| 6. KH xác nhận đặt phòng | Hiển thị thông báo "Đặt phòng thành công! Mã booking: BK005" |

---

#### b) Chức năng "Check-in"

**TC05: Check-in thành công**

CSDL trước khi test:
```
tblRoom:
| roomID | name   | status   | branchID |
|--------|--------|----------|----------|
| 1      | P.VIP1 | Chờ nhận | 1        |

tblRoom_receipt:
| room_receipt_ID | checkin_time        | status   | roomID | clientID | employeeID |
|-----------------|---------------------|----------|--------|----------|------------|
| 1               | 2026-06-01 14:00:00 | Chờ nhận | 1      | 1        | 1          |

tblClient:
| clientID | name           | phone_number | rankingID |
|----------|----------------|--------------|-----------|
| 1        | Nguyễn Văn An  | 0912345678   | 2         |
```

CSDL sau khi test:
```
tblRoom:
| roomID | name   | status         |
|--------|--------|----------------|
| 1      | P.VIP1 | Đang hoạt động |

tblRoom_receipt:
| room_receipt_ID | checkin_time        | status         |
|-----------------|---------------------|----------------|
| 1               | 2026-06-01 14:05:00 | Đang hoạt động |
```

| Các bước thực hiện | Kết quả mong đợi |
|---------------------|------------------|
| 1. NV click [Check-in] trên ReceptionistHomePage | Hiển thị CheckInPage: danh sách booking "Chờ nhận", cột: tên phòng, tên khách, giờ đặt, nút [Xác nhận Check-in] |
| 2. Danh sách booking hiển thị | Hàng: P.VIP1, Nguyễn Văn An, 14:00 |
| 3. NV chọn booking P.VIP1 | Hiển thị ConfirmCheckInView: thông tin phòng (P.VIP1, VIP, 150.000đ/giờ), thông tin khách (Nguyễn Văn An, 0912345678, Hạng Bạc), nút [Xác nhận Check-in], nút [Quay lại] |
| 4. NV click [Xác nhận Check-in] | Hiển thị thông báo "Check-in thành công! Phòng P.VIP1 đã sẵn sàng." |

---

**TC06: Phòng đang dọn dẹp, không thể check-in**

CSDL trước khi test:
```
tblRoom:
| roomID | name   | status        |
|--------|--------|---------------|
| 1      | P.VIP1 | Đang dọn dẹp  |

tblRoom_receipt:
| room_receipt_ID | checkin_time        | status   | roomID |
|-----------------|---------------------|----------|--------|
| 1               | 2026-06-01 14:00:00 | Chờ nhận | 1      |
```

CSDL sau khi test: Không thay đổi.

| Các bước thực hiện | Kết quả mong đợi |
|---------------------|------------------|
| 1. NV click [Check-in] | Hiển thị CheckInPage: danh sách booking "Chờ nhận" |
| 2. Danh sách booking hiển thị | P.VIP1 không xuất hiện trong danh sách "Chờ nhận" vì trạng thái phòng là "Đang dọn dẹp" |
| 3. NV tìm booking của P.VIP1 | Không tìm thấy hoặc hiển thị thông báo "Phòng đang dọn dẹp, vui lòng chờ." |

---

**TC07: Check-in phòng Super VIP**

CSDL trước khi test:
```
tblRoom:
| roomID | name    | type       | hourly_pricing | status   | branchID |
|--------|---------|------------|----------------|----------|----------|
| 3      | P.SVIP1 | Super VIP  | 250000         | Chờ nhận | 1        |

tblRoom_receipt:
| room_receipt_ID | checkin_time        | status   | roomID | clientID |
|-----------------|---------------------|----------|--------|----------|
| 2               | 2026-06-01 20:00:00 | Chờ nhận | 3      | 3        |

tblClient:
| clientID | name          | phone_number | rankingID |
|----------|---------------|--------------|-----------|
| 3        | Lê Minh Châu   | 0901122334   | 3         |
```

CSDL sau khi test:
```
tblRoom:
| roomID | name    | status         |
|--------|---------|----------------|
| 3      | P.SVIP1 | Đang hoạt động |

tblRoom_receipt:
| room_receipt_ID | checkin_time        | status         |
|-----------------|---------------------|----------------|
| 2               | 2026-06-01 20:05:00 | Đang hoạt động |
```

| Các bước thực hiện | Kết quả mong đợi |
|---------------------|------------------|
| 1. NV click [Check-in] | Hiển thị CheckInPage: danh sách booking "Chờ nhận" |
| 2. Danh sách booking hiển thị | Hàng: P.SVIP1, Lê Minh Châu, 20:00 |
| 3. NV chọn booking P.SVIP1 | Hiển thị ConfirmCheckInView: Phòng Super VIP, Giá 250.000đ/giờ, Khách: Lê Minh Châu (Hạng Vàng), nút [Xác nhận Check-in] |
| 4. NV click [Xác nhận Check-in] | Hiển thị thông báo "Check-in thành công! Phòng P.SVIP1 đã sẵn sàng." |

---

#### c) Chức năng "Check-out"

**TC08: Check-out thành công, thanh toán tiền mặt**

CSDL trước khi test:
```
tblRoom:
| roomID | name   | status         | branchID |
|--------|--------|----------------|----------|
| 1      | P.VIP1 | Đang hoạt động | 1        |

tblRoom_receipt:
| room_receipt_ID | checkin_time        | checkout_time | room_fee | service_fee | discount | status         | payment_method | clientID | employeeID | roomID |
|-----------------|---------------------|---------------|----------|-------------|----------|----------------|----------------|----------|------------|--------|
| 1               | 2026-06-01 14:05:00 | NULL          | NULL     | NULL        | NULL     | Đang hoạt động | NULL           | 1        | 1          | 1      |

tblRoom_receipt_detail:
| room_receipt_detail_ID | service_name     | quantity | base_price | room_receipt_ID |
|------------------------|------------------|----------|------------|-----------------|
| 1                      | Lon bia Heineken | 3        | 45000      | 1               |
| 2                      | Đĩa trái cây     | 1        | 120000     | 1               |
| 3                      | Khoai tây chiên   | 2        | 65000      | 1               |

tblClient:
| clientID | name           | rankingID |
|----------|----------------|-----------|
| 1        | Nguyễn Văn An  | 2         |

tblMemberRanking:
| rankingID | name | coupon |
|-----------|------|--------|
| 2         | Bạc  | 10     |
```

CSDL sau khi test:
```
tblRoom:
| roomID | name   | status |
|--------|--------|--------|
| 1      | P.VIP1 | Trống  |

tblRoom_receipt:
| room_receipt_ID | room_fee | service_fee | discount | status         | payment_method |
|-----------------|----------|-------------|----------|----------------|----------------|
| 1               | 450000   | 340000      | 79000    | Đã thanh toán  | Tiền mặt       |
```

*(Điểm tích lũy được cộng: 711.000 / 10.000 = 71 điểm)*

| Các bước thực hiện | Kết quả mong đợi |
|---------------------|------------------|
| 1. NV click [Check-out] trên ReceptionistHomePage | Hiển thị CheckOutPage: danh sách phòng "Đang hoạt động", cột: tên phòng, khách, giờ check-in, nút [Chọn] |
| 2. Danh sách hiển thị | Hàng: P.VIP1, Nguyễn Văn An, 14:05 |
| 3. NV chọn P.VIP1 | Chuyển sang InvoicePanel: chi tiết hóa đơn (tiền phòng, dịch vụ, thời gian), ô nhập mã voucher, nút [Áp dụng], dropdown phương thức thanh toán, nút [Xác nhận thanh toán], nút [In hoá đơn] |
| 4. Hệ thống tính tiền | Hiển thị: Tiền phòng 450.000đ (3h × 150.000đ), Dịch vụ 340.000đ, Tổng 790.000đ, Giảm 10% (Hạng Bạc) = -79.000đ, Tổng thanh toán: 711.000đ |
| 5. NV chọn "Tiền mặt" từ dropdown | Dropdown hiển thị: Tiền mặt, Chuyển khoản |
| 6. NV click [Xác nhận thanh toán] | Hiển thị thông báo "Check-out thành công! Tổng: 711.000đ" |
| 7. NV click [In hoá đơn] | Hoá đơn được in, quay về ReceptionistHomePage |

---

**TC09: Check-out với voucher giảm giá**

CSDL trước khi test:
```
tblRoom:
| roomID | name    | status         | branchID |
|--------|---------|----------------|----------|
| 3      | P.SVIP1 | Đang hoạt động | 1        |

tblRoom_receipt:
| room_receipt_ID | checkin_time        | status         | roomID | clientID |
|-----------------|---------------------|----------------|--------|----------|
| 2               | 2026-06-01 20:05:00 | Đang hoạt động | 3      | 3        |

tblPromotion:
| promotionID | name     | type    | redeem      | discount_type | discount_value | valid_until |
|-------------|----------|---------|-------------|---------------|----------------|-------------|
| 1           | GIẢM 50K | Voucher | VOUCHER50K  | fixed         | 50000          | 2026-12-31  |
```

CSDL sau khi test:
```
tblRoom:
| roomID | name    | status |
|--------|---------|--------|
| 3      | P.SVIP1 | Trống  |

tblRoom_receipt:
| room_receipt_ID | discount | status         | payment_method |
|-----------------|----------|----------------|----------------|
| 2               | 50000    | Đã thanh toán  | Tiền mặt       |

tblApply_promotion:
| apply_promotion_ID | room_receipt_ID | promotionID | discount |
|--------------------|-----------------|-------------|----------|
| 1                  | 2               | 1           | 50000    |
```

| Các bước thực hiện | Kết quả mong đợi |
|---------------------|------------------|
| 1. NV chọn P.SVIP1 từ danh sách CheckOutPage | Chuyển sang InvoicePanel: chi tiết hóa đơn, ô nhập mã voucher, nút [Áp dụng], dropdown phương thức, nút [Xác nhận thanh toán] |
| 2. NV nhập "VOUCHER50K" và click [Áp dụng] | Hiển thị thông báo "Áp dụng voucher thành công!", tổng tiền giảm 50.000đ |
| 3. Tổng tiền cập nhật | Hiển thị: Tổng trước giảm, Giảm 50.000đ, Tổng thanh toán mới |
| 4. NV click [Xác nhận thanh toán] | Hiển thị thông báo "Check-out thành công!" |

---

**TC10: Check-out với hội viên Vàng**

CSDL trước khi test:
```
tblRoom:
| roomID | name   | status         | branchID |
|--------|--------|----------------|----------|
| 1      | P.VIP1 | Đang hoạt động | 1        |

tblRoom_receipt:
| room_receipt_ID | checkin_time        | status         | roomID | clientID |
|-----------------|---------------------|----------------|--------|----------|
| 3               | 2026-06-01 18:00:00 | Đang hoạt động | 1      | 3        |

tblClient:
| clientID | name          | rankingID |
|----------|---------------|-----------|
| 3        | Lê Minh Châu   | 3         |

tblMemberRanking:
| rankingID | name | base_score | coupon |
|-----------|------|------------|--------|
| 3         | Vàng | 5000       | 15     |
```

CSDL sau khi test:
```
tblRoom:
| roomID | name   | status |
|--------|--------|--------|
| 1      | P.VIP1 | Trống  |

tblRoom_receipt:
| room_receipt_ID | room_fee | discount | status         | payment_method |
|-----------------|----------|----------|----------------|----------------|
| 3               | 450000   | 67500    | Đã thanh toán  | Tiền mặt       |
```

| Các bước thực hiện | Kết quả mong đợi |
|---------------------|------------------|
| 1. NV chọn P.VIP1 từ danh sách CheckOutPage | Chuyển sang InvoicePanel: chi tiết hóa đơn |
| 2. Hệ thống kiểm tra hạng hội viên | Hiển thị: Lê Minh Châu - Hạng Vàng (giảm 15%) |
| 3. Tổng tiền trước giảm: 450.000đ | Hiển thị giảm 15% = -67.500đ, Tổng thanh toán: 382.500đ |
| 4. NV click [Xác nhận thanh toán] | Hiển thị thông báo "Check-out thành công! Tổng: 382.500đ" |

---

**TC11: Voucher không hợp lệ**

CSDL trước khi test:
```
tblRoom:
| roomID | name   | status         | branchID |
|--------|--------|----------------|----------|
| 1      | P.VIP1 | Đang hoạt động | 1        |

tblRoom_receipt:
| room_receipt_ID | checkin_time        | status         | roomID |
|-----------------|---------------------|----------------|--------|
| 1               | 2026-06-01 14:05:00 | Đang hoạt động | 1      |
```

CSDL sau khi test: Không thay đổi.

| Các bước thực hiện | Kết quả mong đợi |
|---------------------|------------------|
| 1. NV chọn P.VIP1 | Chuyển sang InvoicePanel: chi tiết hóa đơn, ô nhập mã voucher |
| 2. NV nhập "VOUCHER_SAI" và click [Áp dụng] | Hiển thị thông báo lỗi "Mã voucher không hợp lệ hoặc đã hết hạn." |
| 3. Tổng tiền không thay đổi | Tổng tiền giữ nguyên, không áp dụng giảm giá |

---

**TC12: Check-out chuyển khoản**

CSDL trước khi test:
```
tblRoom:
| roomID | name   | status         | branchID |
|--------|--------|----------------|----------|
| 4      | P.VIP2 | Đang hoạt động | 2        |

tblRoom_receipt:
| room_receipt_ID | checkin_time        | status         | roomID | clientID | employeeID |
|-----------------|---------------------|----------------|--------|----------|------------|
| 4               | 2026-06-01 19:00:00 | Đang hoạt động | 4      | 2        | 2          |

tblClient:
| clientID | name           | rankingID |
|----------|----------------|-----------|
| 2        | Trần Thị Bình   | 1         |
```

CSDL sau khi test:
```
tblRoom:
| roomID | name   | status |
|--------|--------|--------|
| 4      | P.VIP2 | Trống  |

tblRoom_receipt:
| room_receipt_ID | status         | payment_method |
|-----------------|----------------|----------------|
| 4               | Đã thanh toán  | Chuyển khoản   |
```

| Các bước thực hiện | Kết quả mong đợi |
|---------------------|------------------|
| 1. NV chọn P.VIP2 từ danh sách CheckOutPage | Chuyển sang InvoicePanel: chi tiết hóa đơn, dropdown phương thức thanh toán |
| 2. NV chọn "Chuyển khoản" từ dropdown | Hiển thị mã QR chuyển khoản, thông tin tài khoản ngân hàng |
| 3. KH quét QR và chuyển khoản thành công | Hệ thống xác nhận thanh toán, hiển thị thông báo "Đã nhận thanh toán" |
| 4. NV click [Xác nhận thanh toán] | Hiển thị thông báo "Check-out thành công!" |

---

#### d) Chức năng "Huỷ phòng"

**TC13: Hủy đặt phòng thành công**

CSDL trước khi test:
```
tblRoom:
| roomID | name   | status   | branchID |
|--------|--------|----------|----------|
| 1      | P.VIP1 | Chờ nhận | 1        |

tblRoom_receipt:
| room_receipt_ID | checkin_time        | status   | roomID | clientID | employeeID |
|-----------------|---------------------|----------|--------|----------|------------|
| 1               | 2026-06-01 14:00:00 | Chờ nhận | 1      | 1        | 1          |

tblClient:
| clientID | name           | phone_number | rankingID |
|----------|----------------|--------------|-----------|
| 1        | Nguyễn Văn An  | 0912345678   | 2         |
```

CSDL sau khi test:
```
tblRoom:
| roomID | name   | status |
|--------|--------|--------|
| 1      | P.VIP1 | Trống  |

tblRoom_receipt:
| room_receipt_ID | status  |
|-----------------|---------|
| 1               | Đã hủy  |
```

| Các bước thực hiện | Kết quả mong đợi |
|---------------------|------------------|
| 1. NV click [Quản lý đặt phòng] trên ReceptionistHomePage | Hiển thị CancelBookingPage: ô nhập tìm kiếm, nút [Tìm kiếm], danh sách booking "Chờ nhận" |
| 2. NV nhập "0912345678" và click [Tìm kiếm] | Hiển thị danh sách: P.VIP1, Nguyễn Văn An, 14:00 |
| 3. NV chọn booking P.VIP1 | Hiển thị chi tiết booking: phòng, khách, thời gian, nút [Hủy đặt phòng], nút [Quay lại] |
| 4. NV click [Hủy đặt phòng] | Hiển thị xác nhận "Bạn có chắc chắn muốn hủy booking này?", nút [Đồng ý], nút [Hủy] |
| 5. NV click [Đồng ý] | Hiển thị thông báo "Hủy đặt phòng thành công." |

---

**TC14: Không tìm thấy booking**

CSDL trước khi test:
```
tblRoom_receipt:
| room_receipt_ID | checkin_time        | status   | roomID | clientID |
|-----------------|---------------------|----------|--------|----------|
| 1               | 2026-06-01 14:00:00 | Chờ nhận | 1      | 1        |
```

CSDL sau khi test: Không thay đổi.

| Các bước thực hiện | Kết quả mong đợi |
|---------------------|------------------|
| 1. NV click [Quản lý đặt phòng] | Hiển thị CancelBookingPage: ô nhập tìm kiếm, nút [Tìm kiếm] |
| 2. NV nhập "0900000000" và click [Tìm kiếm] | Hiển thị thông báo "Không tìm thấy booking phù hợp." Danh sách kết quả trống |
| 3. Danh sách kết quả trống | Không hiển thị booking nào |

---

**TC15: Booking đã quá thời gian hủy**

CSDL trước khi test:
```
tblRoom:
| roomID | name   | status         | branchID |
|--------|--------|----------------|----------|
| 1      | P.VIP1 | Đang hoạt động | 1        |

tblRoom_receipt:
| room_receipt_ID | checkin_time        | status         | roomID |
|-----------------|---------------------|----------------|--------|
| 1               | 2026-06-01 13:00:00 | Đang hoạt động | 1      |
```

CSDL sau khi test: Không thay đổi.

| Các bước thực hiện | Kết quả mong đợi |
|---------------------|------------------|
| 1. NV tìm booking cần hủy | Hiển thị booking P.VIP1, trạng thái "Đang hoạt động" |
| 2. NV click [Hủy đặt phòng] | Hiển thị thông báo lỗi "Booking đã quá thời gian hủy, không thể hủy." |
| 3. Không thể hủy booking | Booking vẫn ở trạng thái "Đang hoạt động", không thay đổi |

---

### 1.3. Tóm tắt kết quả test

| TT | Test case | Kết quả |
|----|-----------|---------|
| TC01 | Đặt phòng thành công | ✅ Đạt |
| TC02 | Không tìm thấy phòng trống | ✅ Đạt |
| TC03 | Khách hàng chưa có trong CSDL | ✅ Đạt |
| TC04 | Đặt phòng trực tuyến | ✅ Đạt |
| TC05 | Check-in thành công | ✅ Đạt |
| TC06 | Phòng đang dọn dẹp | ✅ Đạt |
| TC07 | Check-in phòng Super VIP | ✅ Đạt |
| TC08 | Check-out tiền mặt | ✅ Đạt |
| TC09 | Check-out voucher | ✅ Đạt |
| TC10 | Check-out hội viên Vàng | ✅ Đạt |
| TC11 | Voucher không hợp lệ | ✅ Đạt |
| TC12 | Check-out chuyển khoản | ✅ Đạt |
| TC13 | Hủy đặt phòng | ✅ Đạt |
| TC14 | Không tìm thấy booking | ✅ Đạt |
| TC15 | Booking quá thời gian hủy | ✅ Đạt |

**Tỷ lệ đạt:** 15/15 = 100%

**Kết luận:** Tất cả các test case đều đạt yêu cầu. Module "Quản lý đặt và trả phòng" hoạt động đúng theo thiết kế.
