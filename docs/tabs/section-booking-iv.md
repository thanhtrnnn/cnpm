## IV. PHA CÀI ĐẶT VÀ KIỂM THỬ

### 1.1. Lập kế hoạch test

**Phạm vi test:** Module "Quản lý đặt và trả phòng" — 4 chức năng: Đặt phòng, Check-in, Check-out, Huỷ phòng.

**Loại test:** Functional testing (kiểm thử chức năng) — kiểm tra từng chức năng theo kịch bản sử dụng thực tế.

**Nguyên tắc test:**
- Test case bao gồm: CSDL trước test → Kịch bản thực hiện → Kết quả mong đợi → CSDL sau test
- CSDL mẫu dùng dữ liệu tiếng Việt, tên riêng Việt Nam
- Dữ liệu trong CSDL phải khớp với ERD (III.2) và Entity class (III.1)
- Mô phỏng tình huống thực tế tại chuỗi nhà hàng karaoke

### Bảng Test Case (tổng hợp)

| TT | Module | Test case | Loại |
|----|--------|-----------|------|
| TC01 | Đặt phòng | Đặt phòng thành công khi có phòng trống | Happy path |
| TC02 | Đặt phòng | Không tìm thấy phòng trống theo thời gian yêu cầu | Exception |
| TC03 | Đặt phòng | Khách hàng chưa có trong CSDL | Exception |
| TC04 | Đặt phòng | Đặt phòng trực tuyến thành công | Happy path |
| TC05 | Check-in | Check-in thành công với booking trạng thái "Chờ nhận" | Happy path |
| TC06 | Check-in | Phòng đang dọn dẹp, không thể check-in | Exception |
| TC07 | Check-in | Check-in phòng Super VIP | Happy path |
| TC08 | Check-out | Check-out thành công, thanh toán tiền mặt | Happy path |
| TC09 | Check-out | Check-out với voucher giảm giá | Happy path |
| TC10 | Check-out | Check-out với hội viên Vàng | Happy path |
| TC11 | Check-out | Voucher không hợp lệ | Exception |
| TC12 | Check-out | Check-out chuyển khoản | Happy path |
| TC13 | Huỷ phòng | Hủy đặt phòng thành công | Happy path |
| TC14 | Huỷ phòng | Không tìm thấy booking | Exception |
| TC15 | Huỷ phòng | Booking đã quá thời gian hủy | Exception |

---

### 1.2. Các test case cho từng chức năng

---

#### TC01: Đặt phòng thành công

**Trạng thái CSDL trước khi test:**

tblBranch
| branchID | name | address |
|----------|------|---------|
| 1 | Karaoke Quận 1 | 123 Lê Lợi, Q1 |
| 2 | Karaoke Quận 3 | 456 Nguyễn Đình Chiểu, Q3 |

tblRoom
| roomID | name | type | hourly_pricing | status | branchID |
|--------|------|------|----------------|--------|----------|
| 1 | P.VIP1 | VIP | 150000 | Trống | 1 |
| 2 | P.Std3 | Standard | 80000 | Trống | 1 |
| 3 | P.SVIP1 | Super VIP | 250000 | Trống | 1 |
| 4 | P.VIP2 | VIP | 150000 | Trống | 2 |

tblClient
| clientID | name | phone_number | rankingID |
|----------|------|--------------|-----------|
| 1 | Nguyễn Văn An | 0912345678 | 2 |
| 2 | Trần Thị Bình | 0987654321 | 1 |
| 3 | Lê Minh Châu | 0901122334 | 3 |

tblEmployee
| employeeID | name | role | branchID |
|------------|------|------|----------|
| 1 | Phạm Thị Dung | Lễ tân | 1 |
| 2 | Hoàng Văn Em | Lễ tân | 2 |

tblMemberRanking
| rankingID | name | base_score | coupon |
|-----------|------|------------|--------|
| 1 | Thường | 0 | 0 |
| 2 | Bạc | 1000 | 10 |
| 3 | Vàng | 5000 | 15 |

**Kịch bản thực hiện + Kết quả mong đợi:**

| Kịch bản | Kết quả mong đợi |
|----------|------------------|
| 1. NV Phạm Thị Dung click [Đặt phòng] | Hiển thị SearchFreeRoomForm |
| 2. NV nhập: ngày 01/06/2026, từ 14:00, đến 17:00, chi nhánh Quận 1 | Form hiển thị đầy đủ |
| 3. NV click [Tìm phòng trống] | Hiển thị: P.VIP1 (150.000đ), P.Std3 (80.000đ), P.SVIP1 (250.000đ) |
| 4. NV chọn P.VIP1 | Chuyển sang SearchClientForm, hiển thị "Phòng: P.VIP1" |
| 5. NV nhập "0912345678" và click [Tìm kiếm] | Hiển thị: Nguyễn Văn An, 0912345678, Hạng Bạc |
| 6. NV chọn khách hàng | Chuyển sang ConfirmBookingModal |
| 7. NV click [Xác nhận đặt phòng] | Hiển thị "Đặt phòng thành công!" |

**Trạng thái CSDL sau khi test:**

tblRoom
| roomID | name | status |
|--------|------|--------|
| 1 | P.VIP1 | **Chờ nhận** ← thay đổi |

tblRoom_receipt (mới tạo)
| room_receipt_ID | checkin_time | checkout_time | room_fee | service_fee | discount | status | payment_method |
|-----------------|--------------|---------------|----------|-------------|----------|--------|----------------|
| 1 | 2026-06-01 14:00 | NULL | NULL | NULL | NULL | Chờ nhận | NULL |

---

#### TC02: Không tìm thấy phòng trống theo thời gian yêu cầu

**Trạng thái CSDL trước khi test:**

tblRoom
| roomID | name | type | hourly_pricing | status | branchID |
|--------|------|------|----------------|--------|----------|
| 1 | P.VIP1 | VIP | 150000 | **Đang hoạt động** | 1 |
| 2 | P.Std3 | Standard | 80000 | **Chờ nhận** | 1 |
| 3 | P.SVIP1 | Super VIP | 250000 | **Đang dọn dẹp** | 1 |

**Kịch bản thực hiện + Kết quả mong đợi:**

| Kịch bản | Kết quả mong đợi |
|----------|------------------|
| 1. NV click [Đặt phòng] | Hiển thị SearchFreeRoomForm |
| 2. NV nhập: ngày 01/06/2026, từ 14:00, đến 17:00 | Form hiển thị đầy đủ |
| 3. NV click [Tìm phòng trống] | Hiển thị thông báo: "Không có phòng trống trong khung giờ này." |
| 4. Danh sách kết quả trống | Không hiển thị phòng nào |

**Trạng thái CSDL sau khi test:** Không thay đổi.

---

#### TC03: Khách hàng chưa có trong CSDL

**Trạng thái CSDL trước khi test:**

tblRoom
| roomID | name | status | branchID |
|--------|------|--------|----------|
| 1 | P.VIP1 | Trống | 1 |

tblClient (không có SĐT "0999999999")
| clientID | name | phone_number |
|----------|------|--------------|
| (không có) |

**Kịch bản thực hiện + Kết quả mong đợi:**

| Kịch bản | Kết quả mong đợi |
|----------|------------------|
| 1. NV chọn P.VIP1 | Chuyển sang SearchClientForm |
| 2. NV nhập "0999999999" và click [Tìm kiếm] | Hiển thị: "Không tìm thấy khách hàng." |
| 3. SearchClientForm hiển thị nút [Đăng ký nhanh] | Nút [Đăng ký nhanh] xuất hiện |
| 4. NV click [Đăng ký nhanh] | Hiển thị form đăng ký nhanh: họ tên, SĐT |
| 5. NV nhập: "Phạm Văn Phúc", "0999999999" | Form hiển thị đầy đủ |
| 6. NV click [Xác nhận] | Tạo khách hàng mới, tiếp tục đặt phòng |

**Trạng thái CSDL sau khi test:**

tblClient (mới tạo)
| clientID | name | phone_number | rankingID |
|----------|------|--------------|-----------|
| 4 | Phạm Văn Phúc | 0999999999 | 1 |

---

#### TC04: Đặt phòng trực tuyến thành công

**Trạng thái CSDL trước khi test:**

tblRoom
| roomID | name | type | hourly_pricing | status | branchID |
|--------|------|------|----------------|--------|----------|
| 5 | P.VIP3 | VIP | 150000 | Trống | 2 |

tblClient
| clientID | name | phone_number | rankingID |
|----------|------|--------------|-----------|
| 5 | Vũ Thị Giang | 0911223344 | 1 |

**Kịch bản thực hiện + Kết quả mong đợi:**

| Kịch bản | Kết quả mong đợi |
|----------|------------------|
| 1. KH truy cập web/app | Hiển thị trang chủ |
| 2. KH chọn chi nhánh "Karaoke Quận 3" | Hiển thị danh sách phòng |
| 3. KH nhập thời gian: 02/06/2026, 19:00-22:00 | Form hiển thị đầy đủ |
| 4. KH click [Tìm phòng trống] | Hiển thị: P.VIP3 (150.000đ/giờ) |
| 5. KH chọn P.VIP3 | Hiển thị thông tin phòng và thời gian |
| 6. KH xác nhận đặt phòng | Hiển thị "Đặt phòng thành công! Mã booking: BK005" |

**Trạng thái CSDL sau khi test:**

tblRoom
| roomID | name | status |
|--------|------|--------|
| 5 | P.VIP3 | **Chờ nhận** ← thay đổi |

---

#### TC05: Check-in thành công

**Trạng thái CSDL trước khi test:**

tblRoom
| roomID | name | status | branchID |
|--------|------|--------|----------|
| 1 | P.VIP1 | Chờ nhận | 1 |

tblRoom_receipt
| room_receipt_ID | checkin_time | status | roomID |
|-----------------|--------------|--------|--------|
| 1 | 2026-06-01 14:00 | Chờ nhận | 1 |

tblClient
| clientID | name | phone_number | rankingID |
|----------|------|--------------|-----------|
| 1 | Nguyễn Văn An | 0912345678 | 2 |

**Kịch bản thực hiện + Kết quả mong đợi:**

| Kịch bản | Kết quả mong đợi |
|----------|------------------|
| 1. NV click [Check-in] | Hiển thị CheckInPage |
| 2. Hiển thị danh sách booking "Chờ nhận" | P.VIP1, Nguyễn Văn An, 14:00 |
| 3. NV chọn booking cần check-in | Hiển thị chi tiết phòng và khách hàng |
| 4. NV click [Xác nhận Check-in] | Hiển thị "Check-in thành công! Phòng P.VIP1 đã sẵn sàng." |

**Trạng thái CSDL sau khi test:**

tblRoom
| roomID | name | status |
|--------|------|--------|
| 1 | P.VIP1 | **Đang hoạt động** ← thay đổi |

tblRoom_receipt
| room_receipt_ID | checkin_time | status |
|-----------------|--------------|--------|
| 1 | 2026-06-01 14:05 | **Đang hoạt động** ← thay đổi |

---

#### TC06: Phòng đang dọn dẹp, không thể check-in

**Trạng thái CSDL trước khi test:**

tblRoom
| roomID | name | status |
|--------|------|--------|
| 1 | P.VIP1 | **Đang dọn dẹp** |

tblRoom_receipt
| room_receipt_ID | checkin_time | status | roomID |
|-----------------|--------------|--------|--------|
| 1 | 2026-06-01 14:00 | Chờ nhận | 1 |

**Kịch bản thực hiện + Kết quả mong đợi:**

| Kịch bản | Kết quả mong đợi |
|----------|------------------|
| 1. NV click [Check-in] | Hiển thị CheckInPage |
| 2. Danh sách booking hiển thị | Không có P.VIP1 trong danh sách "Chờ nhận" |
| 3. NV tìm booking của P.VIP1 | Không tìm thấy hoặc hiển thị lỗi |
| 4. NV liên hệ quản lý dọn dẹp | Chờ phòng sẵn sàng |

**Trạng thái CSDL sau khi test:** Không thay đổi.

---

#### TC07: Check-in phòng Super VIP

**Trạng thái CSDL trước khi test:**

tblRoom
| roomID | name | type | hourly_pricing | status | branchID |
|--------|------|------|----------------|--------|----------|
| 3 | P.SVIP1 | Super VIP | 250000 | Chờ nhận | 1 |

tblRoom_receipt
| room_receipt_ID | checkin_time | status | roomID |
|-----------------|--------------|--------|--------|
| 2 | 2026-06-01 20:00 | Chờ nhận | 3 |

tblClient
| clientID | name | phone_number | rankingID |
|----------|------|--------------|-----------|
| 3 | Lê Minh Châu | 0901122334 | 3 |

**Kịch bản thực hiện + Kết quả mong đợi:**

| Kịch bản | Kết quả mong đợi |
|----------|------------------|
| 1. NV click [Check-in] | Hiển thị CheckInPage |
| 2. Hiển thị danh sách booking "Chờ nhận" | P.SVIP1, Lê Minh Châu, 20:00 |
| 3. NV chọn booking | Hiển thị chi tiết: Phòng Super VIP, Giá 250.000đ/giờ |
| 4. NV click [Xác nhận Check-in] | Hiển thị "Check-in thành công! Phòng P.SVIP1 đã sẵn sàng." |

**Trạng thái CSDL sau khi test:**

tblRoom
| roomID | name | status |
|--------|------|--------|
| 3 | P.SVIP1 | **Đang hoạt động** ← thay đổi |

---

#### TC08: Check-out thành công, thanh toán tiền mặt

**Trạng thái CSDL trước khi test:**

tblRoom
| roomID | name | status |
|--------|------|--------|
| 1 | P.VIP1 | Đang hoạt động |

tblRoom_receipt
| room_receipt_ID | checkin_time | status | room_fee | service_fee |
|-----------------|--------------|--------|----------|-------------|
| 1 | 2026-06-01 14:05 | Đang hoạt động | NULL | NULL |

tblRoom_receipt_detail
| room_receipt_detail_ID | service_name | quantity | base_price | room_receipt_ID |
|------------------------|-------------|----------|------------|-----------------|
| 1 | Lon bia Heineken | 3 | 45000 | 1 |
| 2 | Đĩa trái cây | 1 | 120000 | 1 |
| 3 | Khoai tây chiên | 2 | 65000 | 1 |

tblClient
| clientID | name | rankingID |
|----------|------|-----------|
| 1 | Nguyễn Văn An | 2 |

tblMemberRanking
| rankingID | name | coupon |
|-----------|------|--------|
| 2 | Bạc | 10 |

**Kịch bản thực hiện + Kết quả mong đợi:**

| Kịch bản | Kết quả mong đợi |
|----------|------------------|
| 1. NV click [Check-out] | Hiển thị danh sách phòng "Đang hoạt động": P.VIP1 |
| 2. NV chọn P.VIP1 | Chuyển sang InvoicePanel |
| 3. Hệ thống tính tiền | Hiển thị: Tiền phòng 450.000đ (3h × 150.000đ), Dịch vụ 340.000đ, Tổng 790.000đ, Giảm 10% = -79.000đ, Tổng: 711.000đ |
| 4. NV chọn "Tiền mặt" | Form chọn thanh toán |
| 5. NV click [Xác nhận thanh toán] | Hiển thị "Check-out thành công! Tổng: 711.000đ" |
| 6. NV click [In hoá đơn] | Hoá đơn được in |

**Trạng thái CSDL sau khi test:**

tblRoom
| roomID | name | status |
|--------|------|--------|
| 1 | P.VIP1 | **Trống** ← thay đổi |

tblRoom_receipt
| room_receipt_ID | room_fee | service_fee | discount | status | payment_method |
|-----------------|----------|-------------|----------|--------|----------------|
| 1 | 450000 | 340000 | 79000 | **Đã thanh toán** | **Tiền mặt** |

*(Điểm tích lũy được cộng: 711000/10000 = 71 điểm)*

---

#### TC09: Check-out với voucher giảm giá

**Trạng thái CSDL trước khi test:**

tblRoom
| roomID | name | status |
|--------|------|--------|
| 3 | P.SVIP1 | Đang hoạt động |

tblRoom_receipt
| room_receipt_ID | checkin_time | status |
|-----------------|--------------|--------|
| 2 | 2026-06-01 20:00 | Đang hoạt động |

tblPromotion
| promotionID | name | type | redeem | valid_until |
|-------------|------|------|--------|-------------|
| 1 | GIẢM 50K | Voucher | VOUCHER50K | 2026-12-31 |
| 2 | GIẢM 10% | Voucher | VOUCHER10 | 2026-12-31 |

**Kịch bản thực hiện + Kết quả mong đợi:**

| Kịch bản | Kết quả mong đợi |
|----------|------------------|
| 1. NV chọn P.SVIP1 | Chuyển sang InvoicePanel |
| 2. NV nhập "VOUCHER50K" và click [Áp dụng] | Tổng tiền giảm 50.000đ |
| 3. NV click [Xác nhận thanh toán] | Hiển thị "Check-out thành công!" |

**Trạng thái CSDL sau khi test:**

tblRoom_receipt
| room_receipt_ID | discount | status |
|-----------------|----------|--------|
| 2 | 50000 | Đã thanh toán |

tblApply_promotion (mới tạo)
| apply_promotion_ID | room_receipt_ID | promotionID | discount |
|--------------------|-----------------|-------------|----------|
| 1 | 2 | 1 | 50000 |

---

#### TC10: Check-out với hội viên Vàng

**Trạng thái CSDL trước khi test:**

tblRoom
| roomID | name | status |
|--------|------|--------|
| 1 | P.VIP1 | Đang hoạt động |

tblRoom_receipt
| room_receipt_ID | checkin_time | status |
|-----------------|--------------|--------|
| 3 | 2026-06-01 18:00 | Đang hoạt động |

tblClient
| clientID | name | rankingID |
|----------|------|-----------|
| 3 | Lê Minh Châu | 3 |

tblMemberRanking
| rankingID | name | coupon |
|-----------|------|--------|
| 3 | Vàng | 15 |

**Kịch bản thực hiện + Kết quả mong đợi:**

| Kịch bản | Kết quả mong đợi |
|----------|------------------|
| 1. NV chọn P.VIP1 | Chuyển sang InvoicePanel |
| 2. Hệ thống kiểm tra hạng hội viên | Hiển thị: Lê Minh Châu - Hạng Vàng (giảm 15%) |
| 3. Tổng tiền trước giảm: 450.000đ | Hiển thị giảm 15% = -67.500đ |
| 4. NV click [Xác nhận thanh toán] | Hiển thị "Check-out thành công! Tổng: 382.500đ" |

**Trạng thái CSDL sau khi test:**

tblRoom_receipt
| room_receipt_ID | discount | status |
|-----------------|----------|--------|
| 3 | 67500 | Đã thanh toán |

---

#### TC11: Voucher không hợp lệ

**Trạng thái CSDL trước khi test:**

tblRoom
| roomID | name | status |
|--------|------|--------|
| 1 | P.VIP1 | Đang hoạt động |

tblRoom_receipt
| room_receipt_ID | status |
|-----------------|--------|
| 1 | Đang hoạt động |

**Kịch bản thực hiện + Kết quả mong đợi:**

| Kịch bản | Kết quả mong đợi |
|----------|------------------|
| 1. NV chọn P.VIP1 | Chuyển sang InvoicePanel |
| 2. NV nhập "VOUCHER_SAİ" và click [Áp dụng] | Hiển thị: "Mã voucher không hợp lệ hoặc đã hết hạn." |
| 3. Tổng tiền không thay đổi | Tổng tiền giữ nguyên |

**Trạng thái CSDL sau khi test:** Không thay đổi.

---

#### TC12: Check-out chuyển khoản

**Trạng thái CSDL trước khi test:**

tblRoom
| roomID | name | status |
|--------|------|--------|
| 4 | P.VIP2 | Đang hoạt động |

tblRoom_receipt
| room_receipt_ID | checkin_time | status |
|-----------------|--------------|--------|
| 4 | 2026-06-01 19:00 | Đang hoạt động |

tblClient
| clientID | name | rankingID |
|----------|------|-----------|
| 2 | Trần Thị Bình | 1 |

**Kịch bản thực hiện + Kết quả mong đợi:**

| Kịch bản | Kết quả mong đợi |
|----------|------------------|
| 1. NV chọn P.VIP2 | Chuyển sang InvoicePanel |
| 2. NV chọn "Chuyển khoản" | Hiển thị mã QR chuyển khoản |
| 3. KH quét QR và chuyển khoản thành công | Hệ thống xác nhận thanh toán |
| 4. NV click [Xác nhận thanh toán] | Hiển thị "Check-out thành công!" |

**Trạng thái CSDL sau khi test:**

tblRoom_receipt
| room_receipt_ID | status | payment_method |
|-----------------|--------|----------------|
| 4 | **Đã thanh toán** | **Chuyển khoản** |

---

#### TC13: Hủy đặt phòng thành công

**Trạng thái CSDL trước khi test:**

tblRoom
| roomID | name | status |
|--------|------|--------|
| 1 | P.VIP1 | Chờ nhận |

tblRoom_receipt
| room_receipt_ID | status | roomID |
|-----------------|--------|--------|
| 1 | Chờ nhận | 1 |

tblClient
| clientID | name | phone_number |
|----------|------|--------------|
| 1 | Nguyễn Văn An | 0912345678 |

**Kịch bản thực hiện + Kết quả mong đợi:**

| Kịch bản | Kết quả mong đợi |
|----------|------------------|
| 1. NV click [Quản lý đặt phòng] | Hiển thị danh sách booking "Chờ nhận" |
| 2. NV nhập "0912345678" và tìm | Hiển thị: P.VIP1, Nguyễn Văn An, 14:00 |
| 3. NV chọn booking | Hiển thị chi tiết + nút [Hủy đặt phòng] |
| 4. NV click [Hủy đặt phòng] | Hiển thị "Bạn có chắc chắn muốn hủy booking này?" |
| 5. NV click [Đồng ý] | Hiển thị "Hủy đặt phòng thành công." |

**Trạng thái CSDL sau khi test:**

tblRoom
| roomID | name | status |
|--------|------|--------|
| 1 | P.VIP1 | **Trống** ← thay đổi |

tblRoom_receipt
| room_receipt_ID | status |
|-----------------|--------|
| 1 | **Đã hủy** ← thay đổi |

---

#### TC14: Không tìm thấy booking

**Trạng thái CSDL trước khi test:**

tblRoom_receipt (không có booking với SĐT "0900000000")
| room_receipt_ID | status | roomID |
|-----------------|--------|--------|
| (không có) |

**Kịch bản thực hiện + Kết quả mong đợi:**

| Kịch bản | Kết quả mong đợi |
|----------|------------------|
| 1. NV click [Quản lý đặt phòng] | Hiển thị CancelBookingPage |
| 2. NV nhập "0900000000" và click [Tìm kiếm] | Hiển thị: "Không tìm thấy booking phù hợp." |
| 3. Danh sách kết quả trống | Không hiển thị booking nào |

**Trạng thái CSDL sau khi test:** Không thay đổi.

---

#### TC15: Booking đã quá thời gian hủy

**Trạng thái CSDL trước khi test:**

tblRoom
| roomID | name | status |
|--------|------|--------|
| 1 | P.VIP1 | Đang hoạt động |

tblRoom_receipt
| room_receipt_ID | checkin_time | status | roomID |
|-----------------|--------------|--------|--------|
| 1 | 2026-06-01 13:00 | Đang hoạt động | 1 |

**Kịch bản thực hiện + Kết quả mong đợi:**

| Kịch bản | Kết quả mong đợi |
|----------|------------------|
| 1. NV tìm booking cần hủy | Hiển thị booking P.VIP1 |
| 2. NV click [Hủy đặt phòng] | Hiển thị: "Booking đã quá thời gian hủy, không thể hủy." |
| 3. Không thể hủy booking | Booking vẫn ở trạng thái "Đang hoạt động" |

**Trạng thái CSDL sau khi test:** Không thay đổi.

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
