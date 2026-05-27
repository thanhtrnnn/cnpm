# AGENT.md — Dự án CNPM Karaoke

## Thông tin dự án

| Thông tin | Chi tiết |
|-----------|----------|
| **Tên hệ thống** | Quản lý chuỗi nhà hàng karaoke |
| **Môn học** | Nhập môn Công nghệ Phần mềm (CNPM) |
| **Quy trình** | Unified Process (UP) |
| **Ngôn ngữ** | Tiếng Việt (trừ tên hàm/biến ở pha Thiết kế) |
| **UML Tool** | PlantUML |
| **Output format** | Google Docs (markdown text) |
| **Nhánh làm việc** | `report` |

## Cấu trúc tài liệu UP

### Phần mở đầu — Requirements toàn hệ thống
- Bảng thuật ngữ
- Mô hình nghiệp vụ bằng ngôn ngữ tự nhiên (2.1 → 2.6)
- Mô hình nghiệp vụ bằng UML (3.1 → 3.3)
- Đề xuất phân module

### Pha I — Requirements (cho mỗi module)
- I.1. Biểu đồ Use Case chi tiết của module
- I.2. Kịch bản chuẩn và ngoại lệ

### Pha II — Analysis
- II.1. Mô hình hóa chức năng
- II.2. Mô hình hóa lớp
- II.3. Sơ đồ lớp phân tích (BCE)
- II.4. Biểu đồ tuần tự phân tích

### Pha III — Design
- III.1. Thiết kế lớp thực thể
- III.2. Thiết kế CSDL (ERD)
- III.3.1. Thiết kế giao diện (Wireframe)
- III.3.2. Sơ đồ lớp thiết kế
- III.4. Biểu đồ tuần tự thiết kế

### Pha IV — Test
- IV. Cài đặt & Kiểm thử (Test Plan, Test Case)

## Quy tắc bắt buộc

1. **Hướng Use-case:** Mọi phân tích, thiết kế đều xuất phát từ Use-case
2. **BCE:** Luôn phân rã theo Boundary – Control – Entity
3. **Phân biệt ngôn ngữ theo pha:**
   - Pha Phân tích: Thông điệp sequence diagram = tiếng Việt tự nhiên
   - Pha Thiết kế: Thông điệp = tên hàm tiếng Anh đầy đủ
4. **Văn bản:** 100% tiếng Việt (trừ tên hàm/biến ở pha Thiết kế)
5. **UML:** PlantUML trong code block `plantuml`

## Actors dự kiến

| Actor | Vai trò |
|-------|---------|
| Quản lý | Quản lý chuỗi nhà hàng, xem báo cáo |
| Nhân viên phục vụ | Đặt phòng, order dịch vụ |
| Thu ngân | Thanh toán, hóa đơn |
| Admin | Quản lý tài khoản, hệ thống |
| Khách hàng (gián tiếp) | Sử dụng dịch vụ qua nhân viên |

## Workflow làm việc

1. Đọc AGENT.md trước khi bắt đầu
2. Dùng skill `cnpm` để sinh nội dung
3. Viết output dạng markdown text (tương thích Google Docs)
4. Commit sau khi hoàn thành mỗi phần

## Skills sử dụng

- **cnpm:** Sinh nội dung tài liệu UP (text + PlantUML)
- **cnpm-vp:** Vẽ biểu đồ trong Visual Paradigm (nếu cần diagram chuyên nghiệp)
- **docx:** Tạo file Word document (nếu cần export)
- **gdocs:** Đọc/ghi Google Docs qua API (đẩy nội dung UP lên Google Docs)

## Karaoke Codebase (`../karaoke`)

### Kiến trúc tổng quát
- **Frontend:** React 19 + TypeScript + Vite → `frontend/src/pages/`
- **Backend:** Java 17 + Spring Boot 4.0 → `backend/src/main/java/com/karaoke/backend/`
- **Kiến trúc:** React SPA → REST API → JPA Repository (không có Service layer riêng)

### Key Entities (tab Dịch vụ & Sản phẩm)
| Entity | Table | Mô tả |
|--------|-------|-------|
| `MenuItem` | `tblProduct` | id, name, category(String), price, stock, image, active |
| `ServiceOrder` | `tblOrder` | id, room(ManyToOne→Room), items(OneToMany), orderedAt, status(OrderStatus) |
| `ServiceOrderItem` | `tblOrderItem` | id, order(ManyToOne→ServiceOrder), menuItem(ManyToOne→MenuItem), quantity, unitPrice |
| `OrderStatus` | enum | PENDING, PREPARING, SERVED, CANCELLED |
| `Invoice` | `tblInvoice` | id, booking, roomTotal, serviceTotal, discount, grandTotal, paidAt |

### Controllers
| Controller | Route | Chức năng |
|-----------|-------|-----------|
| `MenuItemController` | `/api/menu-items` | CRUD menu (filter by category) |
| `OrderController` | `/api/orders` | create, list(filter status), updateStatus |
| `InvoiceController` | `/api/invoices` | generate (tính tổng từ ServiceOrderItems) |

### Frontend Pages (tab Dịch vụ & Sản phẩm)
| Component | File | API |
|-----------|------|-----|
| `MenuManagement` | `frontend/src/pages/MenuManagement.tsx` | `/api/menu-items` |
| `OrderPage` | `frontend/src/pages/OrderPage.tsx` | `/api/menu-items`, `/api/orders` |
| `OrderManagement` | `frontend/src/pages/OrderManagement.tsx` | `/api/orders` |
| `InventoryPage` | `frontend/src/pages/InventoryPage.tsx` | `/api/menu-items` (PUT) |

### Mối quan hệ chính
```
Room ──(1:N)──> ServiceOrder ──(1:N)──> ServiceOrderItem ──(N:1)──> MenuItem
Invoice ──(N:1)──> Booking
Invoice.serviceTotal = SUM(ServiceOrderItem.unitPrice × quantity)
```

## Google Docs Document

- **Document ID:** `1H0pFNhmbX9yDMObxERGsZ0RqKjpX9Je6N60n4tYrB6s`
- **Document tabs:** Dùng `includeTabsContent=true` để lấy tất cả tabs
- **Tab tree:**
  - [Test 3 - Software Process]
  - GUIDELINE BỐ CỤC
  - MÔ TẢ HỆ THỐNG
  - XÁC ĐỊNH YÊU CẦU
  - MODULES (5 children)
    - Tài khoản & Thành viên
    - Quản lý đặt và trả phòng
    - **Dịch vụ & Sản phẩm** ← tab chính đang làm
    - Quản trị cốt lõi
    - Nhân sự và báo cáo thống kê
  - THIẾT KẾ

## Quy trình phân tích yêu cầu

Khi nhận yêu cầu từ user:
1. Xác định scope: toàn hệ thống / module cụ thể / vài mục
2. Sinh plan → chờ user xác nhận
3. Thực hiện theo đúng scope đã xác nhận
4. Hỏi sau mỗi pha: "Bạn có muốn điều chỉnh gì không?"
