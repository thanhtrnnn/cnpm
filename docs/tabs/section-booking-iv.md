## IV. PHA CÀI ĐẶT VÀ KIỂM THỬ

### 1.1. Lập kế hoạch test

**Phạm vi test:** Module "Quản lý đặt và trả phòng" — 4 chức năng: Đặt phòng, Check-in, Check-out, Huỷ phòng.

**Loại test:** Functional testing (kiểm thử chức năng) — kiểm tra từng chức năng theo kịch bản sử dụng thực tế.

**Nguyên tắc test:**
- Test case bao gồm: CSDL trước test → Kịch bản thực hiện → Kết quả mong đợi → CSDL sau test
- CSDL mẫu dùng dữ liệu tiếng Việt, tên riêng Việt Nam
- Dữ liệu trong CSDL phải khớp với ERD (III.2) và Entity class (III.1)

### Bảng Test Case (tổng hợp)

| TT | Module | Test case | Loại |
|----|--------|-----------|------|
| TC01 | Đặt phòng | Đặt phòng thành công khi có phòng trống | Happy path |
| TC02 | Đặt phòng | Không tìm thấy phòng trống theo thời gian yêu cầu | Exception |
| TC03 | Đặt phòng | Khách hàng chưa có trong CSDL | Exception |
| TC04 | Check-in | Check-in thành công với booking trạng thái "Chờ nhận" | Happy path |
| TC05 | Check-in | Phòng đang dọn dẹp, không thể check-in | Exception |
| TC06 | Check-out | Check-out thành công, thanh toán tiền mặt | Happy path |
| TC07 | Check-out | Check-out với voucher giảm giá | Happy path |
| TC08 | Check-out | Voucher không hợp lệ | Exception |
| TC09 | Huỷ phòng | Hủy đặt phòng thành công | Happy path |
| TC10 | Huỷ phòng | Không tìm thấy booking | Exception |
| TC11 | Huỷ phòng | Booking đã quá thời gian hủy | Exception |

---

### 1.2. Các test case cho từng chức năng

---

#### TC01: Đặt phòng thành công

**Trạng thái CSDL trước khi test:**

tblBranch
| branchID | name | address |
|----------|------|---------|
| 1 | Karaoke Quận 1 | 123 Lê Lợi, Q1 |

tblRoom
| roomID | name | type | hourly_pricing | status | branchID |
|--------|------|------|----------------|--------|----------|
| 1 | P.VIP1 | Super VIP | 200000 | Trống | 1 |
| 2 | P.Std3 | Standard | 100000 | Trống | 1 |

tblCustomer
| customerID | name | phone_number | rankingID |
|------------|------|--------------|-----------|
| 1 | Nguyễn Văn An | 0912345678 | 2 |

tblEmployee
| employeeID | name | role | branchID |
|------------|------|------|----------|
| 1 | Trần Thị B | Lễ tân | 1 |

tblMemberRanking
| rankingID | name | base_score | coupon |
|-----------|------|------------|--------|
| 1 | Thường | 0 | 0 |
| 2 | Bạc | 1000 | 10 |

**Kịch bản thực hiện + Kết quả mong đợi:**

| Kịch bản | Kết quả mong đợi |
|----------|------------------|
| 1. NV click [Đặt phòng] | Hiển thị SearchFreeRoomForm |
| 2. NV nhập: ngày 30/05/2026, từ 14:00, đến 17:00, chi nhánh Quận 1 | Form hiển thị đầy đủ |
| 3. NV click [Tìm phòng trống] | Hiển thị danh sách: P.VIP1 (200.000đ/giờ), P.Std3 (100.000đ/giờ) |
| 4. NV chọn P.VIP1 | Chuyển sang SearchClientForm, hiển thị "Phòng: P.VIP1" |
| 5. NV nhập "0912345678" và click [Tìm kiếm] | Hiển thị: Nguyễn Văn An, 0912345678, Hạng Bạc |
| 6. NV chọn khách hàng | Chuyển sang ConfirmBookingModal |
| 7. NV click [Xác nhận đặt phòng] | Hiển thị "Đặt phòng thành công!" |

**Trạng thái CSDL sau khi test:**

tblRoom
| roomID | name | status |
|--------|------|--------|
| 1 | P.VIP1 | **Chờ nhận** ← thay đổi |
| 2 | P.Std3 | Trống |

tblRoom_receipt (mới tạo)
| room_receipt_ID | checkin_time | checkout_time | room_fee | service_fee | discount | status | payment_method |
|-----------------|--------------|---------------|----------|-------------|----------|--------|----------------|
| 1 | 2026-05-30 14:00 | NULL | NULL | NULL | NULL | Chờ nhận | NULL |

---

#### TC02: Không tìm thấy phòng trống theo thời gian yêu cầu

**Trạng thái CSDL trước khi test:**

tblRoom
| roomID | name | type | hourly_pricing | status | branchID |
|--------|------|------|----------------|--------|----------|
| 1 | P.VIP1 | Super VIP | 200000 | **Đang hoạt động** | 1 |
| 2 | P.Std3 | Standard | 100000 | **Chờ nhận** | 1 |

**Kịch bản thực hiện + Kết quả mong đợi:**

| Kịch bản | Kết quả mong đợi |
|----------|------------------|
| 1. NV click [Đặt phòng] | Hiển thị SearchFreeRoomForm |
| 2. NV nhập: ngày 30/05/2026, từ 14:00, đến 17:00 | Form hiển thị đầy đủ |
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

tblCustomer
| customerID | name | phone_number |
|------------|------|--------------|
| (không có SĐT "0999999999") |

**Kịch bản thực hiện + Kết quả mong đợi:**

| Kịch bản | Kết quả mong đợi |
|----------|------------------|
| 1. NV chọn P.VIP1 | Chuyển sang SearchClientForm |
| 2. NV nhập "0999999999" và click [Tìm kiếm] | Hiển thị: "Không tìm thấy khách hàng." |
| 3. SearchClientForm hiển thị nút [Đăng ký nhanh] | Nút [Đăng ký nhanh] xuất hiện |
| 4. NV click [Đăng ký nhanh] | Hiển thị form đăng ký nhanh: họ tên, SĐT |
| 5. NV nhập thông tin mới và xác nhận | Tạo khách hàng mới, tiếp tục đặt phòng |

**Trạng thái CSDL sau khi test:**

tblCustomer (mới tạo)
| customerID | name | phone_number | rankingID |
|------------|------|--------------|-----------|
| 1 | [Tên mới] | 0999999999 | 1 |

---

#### TC04: Check-in thành công

**Trạng thái CSDL trước khi test:**

tblRoom
| roomID | name | status | branchID |
|--------|------|--------|----------|
| 1 | P.VIP1 | Chờ nhận | 1 |

tblRoom_receipt
| room_receipt_ID | checkin_time | status | roomID |
|-----------------|--------------|--------|--------|
| 1 | 2026-05-30 14:00 | Chờ nhận | 1 |

**Kịch bản thực hiện + Kết quả mong đợi:**

| Kịch bản | Kết quả mong đợi |
|----------|------------------|
| 1. NV click [Check-in] | Hiển thị CheckInPage |
| 2. Hiển thị danh sách booking "Chờ nhận" | P.VIP1, Nguyễn Văn An, 14:00 |
| 3. NV chọn booking cần check-in | Hiển thị chi tiết phòng và khách hàng |
| 4. NV click [Xác nhận Check-in] | Hiển thị "Check-in thành công!" |

**Trạng thái CSDL sau khi test:**

tblRoom
| roomID | name | status |
|--------|------|--------|
| 1 | P.VIP1 | **Đang hoạt động** ← thay đổi |

tblRoom_receipt
| room_receipt_ID | checkin_time | status |
|-----------------|--------------|--------|
| 1 | 2026-05-30 14:05 | **Đang hoạt động** ← thay đổi |

---

#### TC05: Phòng đang dọn dẹp, không thể check-in

**Trạng thái CSDL trước khi test:**

tblRoom
| roomID | name | status |
|--------|------|--------|
| 1 | P.VIP1 | **Đang dọn dẹp** |

**Kịch bản thực hiện + Kết quả mong đợi:**

| Kịch bản | Kết quả mong đợi |
|----------|------------------|
| 1. NV click [Check-in] | Hiển thị CheckInPage |
| 2. Danh sách booking hiển thị | Không có P.VIP1 trong danh sách "Chờ nhận" |
| 3. NV tìm booking của P.VIP1 | Không tìm thấy hoặc hiển thị lỗi |

**Trạng thái CSDL sau khi test:** Không thay đổi.

---

#### TC06: Check-out thành công, thanh toán tiền mặt

**Trạng thái CSDL trước khi test:**

tblRoom
| roomID | name | status |
|--------|------|--------|
| 1 | P.VIP1 | Đang hoạt động |

tblRoom_receipt
| room_receipt_ID | checkin_time | status | room_fee | service_fee |
|-----------------|--------------|--------|----------|-------------|
| 1 | 2026-05-30 14:05 | Đang hoạt động | NULL | NULL |

tblRoom_receipt_detail
| room_receipt_detail_ID | service_name | quantity | base_price | room_receipt_ID |
|------------------------|-------------|----------|------------|-----------------|
| 1 | Lon bia Heineken | 2 | 50000 | 1 |
| 2 | Dĩa trái cây | 1 | 150000 | 1 |

tblCustomer
| customerID | name | rankingID |
|------------|------|-----------|
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
| 3. Hệ thống tính tiền | Hiển thị: Tiền phòng 534.000đ (2h40p × 200.000đ), Dịch vụ 250.000đ, Giảm 10% = -78.400đ, Tổng: 705.600đ |
| 4. NV chọn "Tiền mặt" | Form chọn thanh toán |
| 5. NV click [Xác nhận thanh toán] | Hiển thị "Check-out thành công! Tổng: 705.600đ" |
| 6. NV click [In hóa đơn] | Hóa đơn được in |

**Trạng thái CSDL sau khi test:**

tblRoom
| roomID | name | status |
|--------|------|--------|
| 1 | P.VIP1 | **Trống** ← thay đổi |

tblRoom_receipt
| room_receipt_ID | room_fee | service_fee | discount | status | payment_method |
|-----------------|----------|-------------|----------|--------|----------------|
| 1 | 534000 | 250000 | 78400 | **Đã thanh toán** | **Tiền mặt** |

tblCustomer
| customerID | name |
|------------|------|
| 1 | Nguyễn Văn An |

*(Điểm tích lũy được cộng sau khi check-out: 705600/10000 = 71 điểm)*

---

#### TC07: Check-out với voucher giảm giá

**Trạng thái CSDL trước khi test:**

tblRoom
| roomID | name | status |
|--------|------|--------|
| 1 | P.VIP1 | Đang hoạt động |

tblRoom_receipt
| room_receipt_ID | checkin_time | status |
|-----------------|--------------|--------|
| 1 | 2026-05-30 14:00 | Đang hoạt động |

tblPromotion
| promotionID | name | type | redeem | valid_until |
|-------------|------|------|--------|-------------|
| 1 | GIẢM 50K | Voucher | VOUCHER50K | 2026-12-31 |

**Kịch bản thực hiện + Kết quả mong đợi:**

| Kịch bản | Kết quả mong đợi |
|----------|------------------|
| 1. NV chọn P.VIP1 | Chuyển sang InvoicePanel |
| 2. NV nhập "VOUCHER50K" và click [Áp dụng] | Tổng tiền giảm 50.000đ |
| 3. NV click [Xác nhận thanh toán] | Hiển thị "Check-out thành công!" |

**Trạng thái CSDL sau khi test:**

tblRoom_receipt
| room_receipt_ID | discount | status |
|-----------------|----------|--------|
| 1 | 50000 | Đã thanh toán |

tblApply_promotion (mới tạo)
| apply_promotion_ID | room_receipt_ID | promotionID | discount |
|--------------------|-----------------|-------------|----------|
| 1 | 1 | 1 | 50000 |

---

#### TC08: Voucher không hợp lệ

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

#### TC09: Hủy đặt phòng thành công

**Trạng thái CSDL trước khi test:**

tblRoom
| roomID | name | status |
|--------|------|--------|
| 1 | P.VIP1 | Chờ nhận |

tblRoom_receipt
| room_receipt_ID | status | roomID |
|-----------------|--------|--------|
| 1 | Chờ nhận | 1 |

**Kịch bản thực hiện + Kết quả mong đợi:**

| Kịch bản | Kết quả mong đợi |
|----------|------------------|
| 1. NV click [Quản lý đặt phòng] | Hiển thị danh sách booking "Chờ nhận" |
| 2. NV nhập "0912345678" và tìm | Hiển thị: P.VIP1, Nguyễn Văn An, 14:00 |
| 3. NV chọn booking | Hiển thị chi tiết + nút [Hủy đặt phòng] |
| 4. NV click [Hủy đặt phòng] | Hiển thị "Bạn có chắc chắn?" |
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

#### TC10: Không tìm thấy booking

**Trạng thái CSDL trước khi test:**

tblRoom_receipt
| room_receipt_ID | status | roomID |
|-----------------|--------|--------|
| (không có booking với SĐT "0900000000") |

**Kịch bản thực hiện + Kết quả mong đợi:**

| Kịch bản | Kết quả mong đợi |
|----------|------------------|
| 1. NV click [Quản lý đặt phòng] | Hiển thị CancelBookingPage |
| 2. NV nhập "0900000000" và click [Tìm kiếm] | Hiển thị: "Không tìm thấy booking phù hợp." |
| 3. Danh sách kết quả trống | Không hiển thị booking nào |

**Trạng thái CSDL sau khi test:** Không thay đổi.

---

#### TC11: Booking đã quá thời gian hủy

**Trạng thái CSDL trước khi test:**

tblRoom
| roomID | name | status |
|--------|------|--------|
| 1 | P.VIP1 | Đang hoạt động |

tblRoom_receipt
| room_receipt_ID | checkin_time | status | roomID |
|-----------------|--------------|--------|--------|
| 1 | 2026-05-30 13:00 | Đang hoạt động | 1 |

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
| TC04 | Check-in thành công | ✅ Đạt |
| TC05 | Phòng đang dọn dẹp | ✅ Đạt |
| TC06 | Check-out thành công | ✅ Đạt |
| TC07 | Check-out với voucher | ✅ Đạt |
| TC08 | Voucher không hợp lệ | ✅ Đạt |
| TC09 | Hủy đặt phòng thành công | ✅ Đạt |
| TC10 | Không tìm thấy booking | ✅ Đạt |
| TC11 | Booking quá thời gian hủy | ✅ Đạt |

**Tỷ lệ đạt:** 11/11 = 100%

**Kết luận:** Tất cả các test case đều đạt yêu cầu. Module "Quản lý đặt và trả phòng" hoạt động đúng theo thiết kế.
