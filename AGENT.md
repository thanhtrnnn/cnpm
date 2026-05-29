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

## Quy tắc formatting Notion

1. **Backtick:** Luôn dùng backtick cho tên biến, tên hàm, tên lớp, tên công nghệ
   - VD: `DAO`, `Entity`, `Boundary`, `CSDL`, `findById()`, `RoomDAO`
   - KHÔNG dùng backtick cho từ tiếng Việt thông thường
2. **Bold:** Dùng `**text**` cho tiêu đề con, tên class, tên chức năng
   - VD: `**OrderController**`, `**1. Tầng giao diện (Boundary)**`
3. **Bảng:** Tối đa 4 cột. Nếu bước chứa bảng → tối đa 2 cột
4. **Callout pairs:** "Mục tiêu" + "Đầu vào" luôn đặt trong 2 columns
5. **PlantUML:** Dùng code block `plantuml`, KHÔNG dùng `javascript`
   - Class diagram: 1 sơ đồ đồng nhất cho toàn module (không tách theo chức năng)

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

## Google Docs Update Strategy

Chiến lược cập nhật Google Docs (áp dụng cho mọi tab):

### Quy trình 5 bước
1. **Map** — Đọc và dump toàn bộ heading structure (HEADING_1/2/3 + indices)
2. **Identify** — Xác định vị trí update chính xác (start/end indices)
3. **Test** — Insert thử nội dung nhỏ, verify formatting TRƯỚC KHI insert toàn bộ
4. **Execute** — Update theo batch nhỏ (mỗi chức năng 1 batch), verify sau mỗi batch
5. **Commit** — Git commit khi hoàn thành

### Lưu ý kỹ thuật
- Google Docs indices thay đổi SAU MỖI batchUpdate → phải re-read trước mỗi operation
- `tabId` cần thiết cho mọi location objects trong requests (cả read và write)
- Heading style inheritance: phải explicit reset `namedStyleType: 'NORMAL_TEXT'` cho mọi paragraph
- Inline formatting offsets: phải track offset mapping giữa original và cleaned text

### Insert markdown vào Google Docs (đã verify)

**Chiến lược 3 phase (đã hoạt động):**
1. **Phase 1:** Parse markdown → insert text (bao gồm table rows dưới dạng pipe-separated)
2. **Phase 2:** Re-read → classify → apply formatting (heading, bold, bullet, inline code)
3. **Phase 3:** Re-read → find table regions → replace bottom-to-top với native tables
4. **Phase 4:** Insert PlantUML image qua public URL

**Markdown conversion rules:**
- `### text` → text sạch + HEADING_3 (classify: `a) ` → HEADING_3, `1. ` → HEADING_4)
- `| col1 | col2 |` → pipe-separated text → sau đó replace bằng native table
- `**bold**` → text sạch + bold style
- `` `code` `` → text sạch + Courier New font
- `- item` → text sạch + bullet style
- `---` → skip
- PlantUML blocks → insert image qua public URL

**Native table insertion (bottom-to-top):**
- Parse markdown → extract table data (rows × cols, cell content)
- Insert all text first, apply formatting
- Find table regions: consecutive paragraphs with ` | ` separators
- Process bottom-to-top: delete text → `insertTable` → re-read → populate cells
- Cell paragraphs nested trong `table.tableRows[i].tableCells[j].content`
- Bottom-to-top tránh index shifting (content above giữ nguyên)

**Rate limiting:**
- Google Docs API: 60 write requests/minute/user
- Dùng batch requests (20 operations/batch) + delay 3s giữa mỗi batch
- Retry 3 lần với exponential backoff khi gặp 429

**PlantUML images:**
- `insertInlineImage` với public PlantUML URL → **đã hoạt động** (test với service account)
- URL format: `https://www.plantuml.com/plantuml/png/{encoded}`
- Encode: custom deflate + base64 alphabet (xem `encode_plantuml()`)
- Nếu URL fails → fallback: render PNG thủ công từ `plantuml_renderer.py`
