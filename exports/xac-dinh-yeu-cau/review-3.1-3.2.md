<!-- REVIEW FILE — XÁC ĐỊNH YÊU CẦU mục 3.1 + 3.2 (đề xuất viết lại)
   Thay thế 2 bảng hiện có trong tab Google Docs.
   Các thay đổi ghi chú cuối file. -->

## 3. Mô hình nghiệp vụ bằng UML

### 3.1. Danh sách Actor

| STT | Actor | Mô tả |
|---|---|---|
| 1 | Khách hàng | Người sử dụng dịch vụ karaoke, truy cập qua web/app để đặt phòng và quản lý tài khoản cá nhân. |
| 2 | Nhân viên lễ tân | Nhân viên tại quầy, xử lý đặt phòng, check-in/check-out và thanh toán. |
| 3 | Nhân viên phục vụ | Nhân viên nhận order gọi món, phục vụ đồ ăn/uống và báo cáo tình trạng hàng hóa trong phòng. |
| 4 | Quản lý chi nhánh | Quản lý một chi nhánh: nhân sự, kho hàng, menu, phòng hát và xem báo cáo hoạt động. |
| 5 | Chủ doanh nghiệp | Chủ sở hữu toàn chuỗi, quản lý chi nhánh, danh mục, khách hàng, hạng hội viên và xem báo cáo tổng hợp. |
| 6 | Thành viên | Actor trừu tượng, là cha của tất cả actor cụ thể trong hệ thống. |
| 7 | Nhân viên | Actor trừu tượng, là cha của NV lễ tân và NV phục vụ. |

---

### 3.2. Các Use Case cho từng Actor

| Actor | Use Case |
|---|---|
| Thành viên (tổng quát) | UC01 – Đăng nhập |
| | UC03 – Đổi mật khẩu |
| Khách hàng | UC02 – Đăng ký |
| | UC04 – Quản lý thông tin cá nhân |
| | UC05 – Đặt phòng |
| | UC06 – Gọi món / Quản lý order |
| NV lễ tân | UC05 – Đặt phòng |
| | UC07 – Quản lý đặt phòng (check-in) |
| | UC08 – Quản lý trả phòng (check-out) |
| NV phục vụ | UC06 – Gọi món / Quản lý order |
| | UC10 – Báo cáo tình trạng hàng hóa |
| Quản lý chi nhánh | UC11 – Quản lý nhân viên chi nhánh |
| | UC12 – Quản lý kho |
| | UC13 – Báo cáo số liệu chi nhánh |
| | UC14 – Xem thông tin khách hàng chi nhánh |
| | UC15 – Quản lý menu |
| | UC19 – Quản lý phòng hát |
| Chủ doanh nghiệp | UC16 – Quản lý hệ thống chi nhánh |
| | UC17 – Quản lý khách hàng toàn hệ thống |
| | UC18 – Quản lý hạng hội viên |
| | UC19 – Quản lý phòng hát |
| | UC20 – Quản lý tài khoản nhân viên |
| | UC21 – Tổng hợp báo cáo toàn chuỗi |

---

<!-- ============================================================
     THAY ĐỔI SO VỚI BẢN GỐC
     ============================================================
     3.1 — Actor table:
     ✅ Actor 2 (NV lễ tân): xóa "kiểm kê hàng hóa tại quầy" — UC09 đã loại.
     ✅ Actor 4 (QL chi nhánh): bổ sung "menu, phòng hát" vào mô tả.
     ✅ Actor 7 (Nhân viên): hoàn thiện mô tả bị cắt cụt:
        "Actor trừu tượng, là cha của NV lễ tân và NV phục vụ."

     3.2 — UC table:
     ✅ UC02 – Đăng ký: chuyển từ "Thành viên" → "Khách hàng"
        (Nhân viên không tự đăng ký tài khoản — chỉ Khách hàng mới dùng UC02).
     ✅ UC06: thống nhất tên thành "UC06 – Gọi món / Quản lý order"
        (bản gốc: "UC06 – Order" ở Khách hàng vs "UC06 – Quản lý order" ở NV phục vụ).
     ✅ UC15: sửa dấu gạch ngang "UC15 - " → "UC15 – " (em dash, nhất quán với các UC khác).
     ✅ UC19 – Quản lý phòng hát: thêm actor Quản lý chi nhánh
        (QL chi nhánh quản lý phòng vật lý tại chi nhánh; Admin quản lý danh mục loại phòng).
     ⚠️  KHÔNG thay đổi thứ tự UC hay thêm cột "Module" — giữ cấu trúc bảng 2 cột như bản gốc.
     ============================================================ -->
