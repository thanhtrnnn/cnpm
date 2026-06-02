# Audit — Tab XÁC ĐỊNH YÊU CẦU

**Ngày audit:** 2026-06-02  
**Nguồn:** `exports/xac-dinh-yeu-cau/xác-định-yêu-cầu.md` (tab Google Docs)  
**Ảnh trong tab:** 0  
**Tham chiếu chuẩn:** `cnpm skill` → `references/requirements-system.md`

---

## Ma trận đầy đủ theo chuẩn cnpm

| # | Mục cần có | Trạng thái | Ghi chú |
|---|---|---|---|
| **1** | **Bảng thuật ngữ** | ⚠ | Có (45 dòng, 6 nhóm) nhưng: "Tồn kho" định nghĩa 2 lần; thiếu OTP, Phiên đăng nhập, Voucher |
| **2.1** | Mục tiêu và phạm vi | ✓ | Đầy đủ, rõ ràng |
| **2.2** | Danh sách actor + mô tả | ✓ | 5 actor, mô tả tốt |
| **2.3** | Chức năng theo từng actor | ⚠ | Có đủ 5 actor nhưng còn "Kiểm kê hàng tại quầy" (đã loại khỏi hệ thống); không có UC ID mapping |
| **2.4** | Luồng từng chức năng (format →) | ⚠ | Nhiều lỗi — xem chi tiết mục II |
| **2.5** | Đối tượng dữ liệu | ⚠ | 14 đối tượng có; thiếu OTP, Phiên đăng nhập, Loại phòng |
| **2.6** | Quan hệ giữa đối tượng | ⚠ | 9 quan hệ có; thiếu nhiều quan hệ quan trọng và không xác định n-n |
| **3.1** | Bảng danh sách Actor (UML) | ⚠ | Có 7 dòng; Actor 7 "Nhân viên" mô tả bị cắt cụt |
| **3.2** | Bảng UC theo Actor | ⚠ | Có UC01-UC21 (bỏ UC09); UC19 thiếu actor QL chi nhánh; xung đột UC15 |
| **3.3** | Biểu đồ UC tổng quan (ảnh) | ✗ | **HOÀN TOÀN THIẾU** — không có heading, không có ảnh |

---

## I. Bảng thuật ngữ — chi tiết

### Vấn đề phát hiện

**Trùng định nghĩa:**
- "Tồn kho" xuất hiện 2 lần:
  - Nhóm 3 (F&B): "Số lượng hàng hóa còn lại tại mỗi chi nhánh, cần theo dõi và bổ sung"
  - Nhóm 4 (Hội viên): "Tồn kho (Inventory)" — cùng định nghĩa, khác nhóm → **xóa bản trùng**

**Thiếu thuật ngữ quan trọng:**
| Thuật ngữ | Xuất hiện ở | Lý do cần có |
|---|---|---|
| OTP | UC02 Đăng ký | Quy trình xác minh tài khoản dùng OTP |
| Phiên đăng nhập | UC03 Đổi MK ("thu hồi phiên") | Session management |
| Voucher | UC08 Check-out | Áp dụng voucher khi thanh toán |
| Điểm tích lũy | 2.2 Khách hàng, UC04 | Cơ chế hội viên cốt lõi |
| Loại phòng | UC19 | Entity chuẩn toàn hệ thống |

**Nhóm 4 bị đặt sai nội dung:**
Nhóm 4 header là "Quản lý Hội viên" nhưng nội dung chứa định nghĩa actor (NV lễ tân, NV phục vụ, QL chi nhánh, Chủ doanh nghiệp) — không liên quan hội viên. → Tách thành nhóm riêng hoặc di chuyển sang phần Actor.

---

## II. Mục 2.3 — Chức năng theo actor

### Vấn đề phát hiện

**1. Chức năng đã loại còn trong văn bản:**
- NV lễ tân (dòng 2.2): *"đồng thời kiểm kê hàng hóa tại quầy"* — UC09 đã bị loại khỏi hệ thống → cần xóa câu này
- 2.3 NV lễ tân: *"Kiểm kê hàng tại quầy: đếm số lượng thực tế..."* → cần xóa toàn bộ mục này

**2. Xung đột actor quản lý menu:**
- 2.3 Admin (dòng 41): *"Quản lý danh mục chung: **menu món ăn/đồ uống**, bảng giá phòng..."*
- 3.2 UC15 – Quản lý menu: gán cho **QL chi nhánh**

→ Ai quản lý menu? Cần thống nhất. Gợi ý: Admin quản lý danh mục gốc (tạo/xóa món), QL chi nhánh cập nhật trạng thái/giá local.

**3. Chức năng không có UC tương ứng:**
- Khách hàng: *"Tương tác dịch vụ trong phòng: gọi món qua app..."* → là một phần của UC06 hay UC riêng? Bảng 3.2 không thể hiện Khách hàng là actor của UC06.

---

## III. Mục 2.4 — Luồng chức năng

*(Đã audit chi tiết riêng — xem `exports/xac-dinh-yeu-cau/review-2.4.md`)*

### Tóm tắt lỗi cần sửa

| Lỗi | Mức độ |
|---|---|
| UC15 Quản lý menu thiếu hoàn toàn | 🔴 |
| "Kiểm kê hàng tại quầy" còn trong 2.4 dù đã loại | 🔴 |
| "Trả phòng & Thanh toán" trùng hoàn toàn với Check-out | 🔴 |
| Logic sai "Hủy phòng trực tuyến": hệ thống đổi trạng thái trước xác nhận | 🔴 |
| 5 flows dùng văn xuôi thay vì format → | 🟡 |
| Thiếu nhánh thất bại UC01, UC02, UC03 | 🟡 |
| Tên "Quản lý tài khoản cá nhân" ≠ UC04 "Quản lý thông tin cá nhân" | 🟡 |
| "Quản lý tài khoản nhân viên" xuất hiện 2 lần | 🟡 |

**File review đã chuẩn bị:** `exports/xac-dinh-yeu-cau/review-2.4.md` + `output/review-2.4.docx`

---

## IV. Mục 2.5 — Đối tượng dữ liệu

### Đối tượng thiếu

| Thiếu | Lý do |
|---|---|
| **OTP** | UC02 Đăng ký dùng OTP; cần lưu: mã, loại, thời hạn, trạng thái đã dùng |
| **Phiên đăng nhập** | UC03 Đổi MK thu hồi "tất cả phiên" → Phiên là entity cần track |
| **Loại phòng** | UC19 Admin quản lý loại phòng (Standard/VIP); hiện chỉ là attribute của Phòng hát |

### Vấn đề thiết kế

**"Tài khoản" phục vụ cả Khách hàng lẫn Nhân viên** nhưng không giải thích cơ chế. Nên ghi rõ: Tài khoản là entity chung cho xác thực, liên kết 1-1 với Khách hàng hoặc 1-1 với Nhân viên (không cả hai cùng lúc).

---

## V. Mục 2.6 — Quan hệ giữa đối tượng

### Quan hệ còn thiếu

| Quan hệ thiếu | Lý do cần có |
|---|---|
| Tài khoản ↔ OTP (1-n) | Mỗi tài khoản có nhiều OTP (mỗi lần gửi = 1 OTP) |
| Tài khoản ↔ Phiên đăng nhập (1-n) | UC03 thu hồi nhiều phiên |
| Loại phòng ↔ Phòng hát (1-n) | Mỗi loại có nhiều phòng vật lý |
| Dịch vụ/Món ăn ↔ Tồn kho (1-1 per chi nhánh) | Tồn kho track từng Dịch vụ tại từng chi nhánh |
| Phiếu nhập hàng ↔ Tồn kho | Nhập hàng cập nhật tồn kho |
| Ca làm việc ↔ Chi nhánh | Ca thuộc về chi nhánh cụ thể |

### Quan hệ n-n chưa được xác định

Skill yêu cầu xác định **mọi quan hệ n-n** và đề xuất bảng trung gian. Hiện tại 2.6 không xác định n-n nào. Gợi ý:
- Nhân viên ↔ Ca làm việc: thực ra là 1-n (1 nhân viên nhiều ca) → OK
- Khuyến mãi ↔ Hóa đơn: 1 hóa đơn áp dụng 1 khuyến mãi (1-1) → OK nhưng chưa rõ 1 khuyến mãi có thể áp dụng nhiều hóa đơn không?
- Dịch vụ ↔ Phiếu nhập hàng: n-n → cần bảng trung gian `Chi tiết phiếu nhập`

---

## VI. Mục 3.1 — Danh sách Actor

### Vấn đề

**Actor 7 "Nhân viên" mô tả bị cắt cụt:**
> "Actor trừu tượng,"

Thiếu phần giải thích: Nhân viên là actor trừu tượng, là cha của NV lễ tân và NV phục vụ — cần bổ sung.

---

## VII. Mục 3.2 — Use Cases per Actor

### Vấn đề

**UC19 thiếu actor Quản lý chi nhánh:**
- 3.2: UC19 gán cho Chủ doanh nghiệp
- 2.3: "Quản lý phòng hát tại chi nhánh" là chức năng của QL chi nhánh

→ UC19 cần 2 actor: Admin (quản lý loại phòng chuẩn) + QL chi nhánh (quản lý phòng vật lý tại chi nhánh).

**Khách hàng và UC06:**
- 2.3 Khách hàng có "tương tác dịch vụ / gọi món" nhưng bảng 3.2 không liệt kê Khách hàng là actor của UC06. Nếu gọi món qua app là chức năng của Khách hàng thì cần bổ sung vào bảng.

---

## VIII. Mục 3.3 — Biểu đồ Use Case (THIẾU HOÀN TOÀN)

**Đây là lỗ hổng lớn nhất của tab.**

Theo cnpm skill, 3.3 bắt buộc có:
- Biểu đồ UC tổng quan thể hiện actor + UC + quan hệ include/extend
- Biểu đồ phân rã chi tiết (nhóm theo chức năng hoặc module)
- PlantUML code hoặc ảnh nhúng

Hiện tại: không có heading 3.3, không có ảnh nào trong toàn tab (0 ảnh).

---

## Tóm tắt — Danh sách việc cần làm

### 🔴 Bắt buộc (ảnh hưởng tính chính xác)

1. **Thêm mục 3.3** — vẽ biểu đồ UC tổng quan toàn hệ thống (PlantUML + ảnh nhúng)
2. **Cập nhật 2.4** theo `review-2.4.md`: xóa "Kiểm kê hàng tại quầy", thêm UC15, sửa logic hủy phòng, xóa bản trùng "Trả phòng & Thanh toán"
3. **Xóa "Kiểm kê hàng tại quầy"** khỏi 2.2 (mô tả NV lễ tân) và 2.3
4. **Thêm OTP + Phiên đăng nhập** vào 2.5
5. **Sửa Actor 7** trong 3.1 — điền đủ mô tả "Nhân viên"
6. **Cập nhật UC19** trong 3.2 — thêm QL chi nhánh là actor

### 🟡 Nên làm (chất lượng tài liệu)

7. Xóa "Tồn kho" trùng trong bảng thuật ngữ
8. Thêm OTP, Phiên đăng nhập, Voucher, Điểm tích lũy, Loại phòng vào bảng thuật ngữ
9. Thêm 6 quan hệ còn thiếu vào 2.6 (OTP, Phiên, Loại phòng, Tồn kho↔Dịch vụ, Phiếu nhập↔Tồn kho)
10. Xác định quan hệ n-n (Dịch vụ ↔ Phiếu nhập hàng) — đề xuất bảng trung gian
11. Thêm "Loại phòng" vào 2.5 như entity độc lập
12. Thống nhất ai quản lý menu (Admin vs QL chi nhánh)
13. Làm rõ Khách hàng có phải actor của UC06 không

### ⚪ Tùy chọn

14. Bổ sung UC ID vào danh sách chức năng ở 2.3 để dễ trace
15. Di chuyển định nghĩa actor ra khỏi nhóm 4 bảng thuật ngữ
