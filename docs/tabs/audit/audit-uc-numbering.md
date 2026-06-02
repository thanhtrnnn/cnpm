# Audit UC Numbering — Đối chiếu toàn module vs XÁC ĐỊNH YÊU CẦU

**Ngày:** 2026-06-02
**Nguồn chuẩn:** `exports/xac-dinh-yeu-cau/` bảng 3.2 (UC01–UC21, bỏ UC09)
**Modules:** account · booking · services · core · hr

---

## Ma trận đối chiếu UC

| UC             | Tên UC (XÁC ĐỊNH)                       | Module phụ trách | Có trong module?                         | Có ID UC?       | Lỗi                                                                        |
| -------------- | ------------------------------------------- | ------------------ | ----------------------------------------- | ---------------- | --------------------------------------------------------------------------- |
| UC01           | Đăng nhập                                | account            | ✓                                        | ✓`UC01`       | —                                                                          |
| UC02           | Đăng ký                                  | account            | ✓                                        | ✓`UC02`       | —                                                                          |
| UC03           | Đổi mật khẩu                            | account            | ✓                                        | ✓`UC03`       | —                                                                          |
| UC04           | Quản lý thông tin cá nhân              | account            | ✓                                        | ✓`UC04`       | —                                                                          |
| UC05           | Đặt phòng                                | booking            | ✓ (tên: "Đặt phòng" + "Hủy phòng") | ✗ không có ID | Thiếu nhãn UC05                                                           |
| UC06           | Gọi món / Order                           | services           | ✓ (tên: "Quản lý order")              | ✗ không có ID | Thiếu nhãn UC06                                                           |
| UC07           | Quản lý đặt phòng (check-in)           | booking            | ✓ (tên: "Check-in")                     | ✗ không có ID | Thiếu nhãn UC07                                                           |
| UC08           | Quản lý trả phòng (check-out)           | booking            | ✓ (tên: "Check-out")                    | ✗ không có ID | Thiếu nhãn UC08                                                           |
| ~~UC09~~      | ~~(đã loại bỏ)~~                       | —                 | —                                        | —               | —                                                                          |
| UC10           | Báo cáo tình trạng hàng hóa           | services           | ✓                                        | ✗ không có ID | Thiếu nhãn UC10                                                           |
| UC11           | Quản lý nhân viên chi nhánh            | hr                 | ✓                                        | ✗ không có ID | Thiếu nhãn UC11                                                           |
| UC12           | Quản lý kho                               | services           | ✓                                        | ✗ không có ID | Thiếu nhãn UC12                                                           |
| UC13           | Báo cáo số liệu chi nhánh              | hr                 | ✓                                        | ✗ không có ID | Thiếu nhãn UC13                                                           |
| UC14           | Xem thông tin KH chi nhánh                | hr                 | ✓                                        | ✓`UC14`       | —                                                                          |
| UC15           | Quản lý menu                              | services           | ✓                                        | ✗ không có ID | Thiếu nhãn UC15                                                           |
| UC16           | Quản lý hệ thống chi nhánh             | core               | ✓                                        | ⚠ "Use Case 16" | Sai format (không phải UCxx)                                              |
| UC17           | Quản lý khách hàng toàn hệ thống     | core               | ✓                                        | ⚠ "Use Case 17" | Sai format                                                                  |
| UC18           | Quản lý hạng hội viên                  | core               | ✓                                        | ⚠ "Use Case 18" | Sai format                                                                  |
| UC19           | Quản lý phòng hát                       | core               | ⚠ chỉ có loại phòng (Admin)          | ⚠ "Use Case 19" | Thiếu luồng QL chi nhánh; sai format                                     |
| **UC20** | **Quản lý tài khoản nhân viên** | account            | ✓ (account có đúng)                   | ✓`UC20`       | **Core gán nhầm UC20 = "Quản lý phòng hát tại chi nhánh"** 🔴 |
| UC21           | Tổng hợp báo cáo toàn chuỗi           | hr                 | ✓                                        | ✓`UC21`       | —                                                                          |

---

## Lỗi nghiêm trọng theo module

### 🔴 Core — Xung đột UC20

**Core gán "Use Case 20" = "Quản lý phòng hát tại chi nhánh"**
Nhưng UC20 trong XÁC ĐỊNH YÊU CẦU = **"Quản lý tài khoản nhân viên"** (Admin).

Nguyên nhân: core tự tách UC19 thành 2:

- Use Case 19 = Quản lý danh mục **loại** phòng (Admin)
- Use Case 20 = Quản lý phòng **vật lý** tại chi nhánh (QL chi nhánh)

→ Làm xung đột với UC20 đã gán cho account.

**Cách sửa:** Gộp "Quản lý phòng hát tại chi nhánh" vào UC19 (hai luồng theo actor). Xóa nhãn "Use Case 20" trong core.

---

### 🟡 HR — Chức năng lạc module (Pha III)

HR module nhét 2 chức năng thuộc **services** vào trong Pha III thiết kế:

- `c) Chức năng Quản lý order` — xuất hiện ở mục Thiết kế giao diện
- `c) Chức năng Quản lý menu` — xuất hiện ở mục MVC class

Hậu quả: `Xem thông tin khách hàng chi nhánh` (UC14) **bị mất** khỏi một số phần trong Pha III của HR.

**Cách sửa:** Thay 2 mục lạc bằng `c) Xem thông tin khách hàng chi nhánh (UC14)` đúng vị trí.

---

### ⚠️ Booking — Không có UC ID nào

Toàn bộ tab booking **không dùng mã UC**. Chức năng gọi theo tên tự nhiên:

- "Đặt phòng" → nên là UC05
- "Hủy phòng" → nên là UC05 (luồng hủy) hoặc UC riêng
- "Check-in" → nên là UC07
- "Check-out" → nên là UC08

---

### ⚠️ Services — Không có UC ID nào

Toàn bộ tab services **không dùng mã UC**:

- "Quản lý order" → UC06
- "Báo cáo tình trạng hàng hóa" → UC10
- "Quản lý menu" → UC15
- "Quản lý kho" → UC12

---

### ⚠️ Core — Sai format ID

Core dùng **"Use Case 16"** thay vì **"UC16"** — không khớp format chuẩn của account và XÁC ĐỊNH YÊU CẦU.

---

## Tổng kết phân bổ UC theo module

| Module             | UC phụ trách           | Có ID đúng     | Ghi chú                                         |
| ------------------ | ------------------------ | ----------------- | ------------------------------------------------ |
| **account**  | UC01 UC02 UC03 UC04 UC20 | ✓ tất cả       | Chuẩn nhất                                     |
| **booking**  | UC05 UC07 UC08           | ✗ không có ID  | Cần gán UC ID                                  |
| **services** | UC06 UC10 UC12 UC15      | ✗ không có ID  | Cần gán UC ID                                  |
| **core**     | UC16 UC17 UC18 UC19      | ⚠ sai format     | Sửa "Use Case N" → "UCN"; sửa UC20 xung đột |
| **hr**       | UC11 UC13 UC14 UC21      | ⚠ chỉ UC14+UC21 | Gán UC11, UC13; dọn 2 chức năng lạc         |

---

## Danh sách sửa theo thứ tự ưu tiên

| # | Module   | Việc cần làm                                                                                   | Mức độ |
| - | -------- | ------------------------------------------------------------------------------------------------- | --------- |
| 1 | core     | Đổi "Use Case 20 – Quản lý phòng hát tại chi nhánh" → gộp vào UC19                    | 🔴        |
| 2 | hr       | Thay `c) Quản lý order` + `c) Quản lý menu` → `c) Xem thông tin KH chi nhánh (UC14)` | 🔴        |
| 3 | core     | Đổi format "Use Case 16/17/18/19" → "UC16/UC17/UC18/UC19" xuyên suốt                         | 🟡        |
| 4 | booking  | Thêm nhãn UC05/UC07/UC08 vào heading mỗi chức năng                                          | 🟡        |
| 5 | services | Thêm nhãn UC06/UC10/UC12/UC15 vào heading mỗi chức năng                                     | 🟡        |
| 6 | hr       | Thêm nhãn UC11/UC13 vào 2 chức năng còn thiếu ID                                           | 🟡        |
| 7 | core     | UC19 bổ sung luồng QL chi nhánh (quản lý phòng vật lý)                                    | 🟡        |
