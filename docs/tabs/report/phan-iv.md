# PHẦN IV. THIẾT KẾ VÀ CÀI ĐẶT

## 1. Kiến trúc hệ thống

Hệ thống được triển khai theo mô hình MVC 3 tầng kết hợp kiến trúc BCE (Boundary – Control – Entity):

| Tầng | Công nghệ | Vai trò |
|---|---|---|
| Boundary (Giao diện) | React.js (web), React Native (mobile) | Hiển thị UI, nhận input người dùng |
| Control (Điều khiển) | Node.js / Express (hoặc Spring Boot) | Xử lý nghiệp vụ, điều phối luồng |
| Entity (Dữ liệu) | PostgreSQL + Redis | Lưu trữ bền vững + cache phiên |

Mỗi module ánh xạ thành một nhóm Controller độc lập. Boundary (React component) gọi REST API của Control; Control truy vấn Entity qua ORM. Redis lưu session token và cache trạng thái phòng theo thời gian thực.

**Mục tiêu kiến trúc:** Mỗi chi nhánh có thể hoạt động offline và đồng bộ dữ liệu khi có mạng — giảm phụ thuộc đường truyền trong ca cao điểm.

## 2. Entity model toàn hệ thống

Bảng chuẩn hóa tên entity và bảng CSDL xuyên 5 module:

| Khái niệm nghiệp vụ | Tên class chuẩn | Bảng CSDL | Module sở hữu |
|---|---|---|---|
| Khách hàng | Client | tblUser (role=CLIENT) | Account |
| Nhân viên | Employee | tblUser (role=EMPLOYEE) | Account |
| Hạng hội viên | MembershipTier | tblMembershipTier | Account |
| Chi nhánh | Branch | tblBranch | Core |
| Loại phòng | RoomType | tblRoomType | Core |
| Phòng hát | Room | tblRoom | Core / Booking |
| Đặt phòng / Hóa đơn | Room_receipt | tblRoom_receipt | Booking |
| Chi tiết hóa đơn | Room_receipt_detail | tblRoom_receipt_detail | Booking |
| Khuyến mãi | Promotion | tblPromotion | Booking |
| Sản phẩm / Dịch vụ | Product | tblProduct | Services |
| Đơn hàng | Order | tblOrder | Services |
| Chi tiết đơn hàng | Order_detail | tblOrderDetail | Services |
| Báo cáo hư hỏng | Damage_report | tblDamageReport | Services |
| Tài sản cơ sở vật chất | Facility | tblFacility | Services |
| Nhà cung cấp | Provider | tblProvider | Services |
| Phiếu nhập kho | Import_receipt | tblImportReceipt | Services |
| Ca làm việc | Shift | tblShift | HR |
| Chấm công | Timekeeping | tblTimekeeping | HR |
| Đánh giá nhân viên | Evaluation | tblEvaluation | HR |

**Lưu ý chuẩn hóa cần thực hiện:**
- Booking `MemberRanking` → đổi thành `MembershipTier` (nhất quán với Account/Core)
- Core `Customer` + HR `KhachHang` → đổi thành `Client` (nhất quán với Account/Booking)
- HR entity tiếng Việt (`CaLamViec`, `ChamCong`) → đổi sang `Shift`, `Timekeeping`

## 3. Giao diện liên module

Các lời gọi xuyên module đã được xác định trong quá trình phân tích:

| Module gọi | Module nhận | Phương thức / Dữ liệu | Mục đích |
|---|---|---|---|
| Booking | Account | Client.findById() | Tra cứu khách hàng khi đặt phòng |
| Booking | Core | Room.updateStatus() | Cập nhật trạng thái phòng |
| Services | Booking | Room_receipt.updateServiceFee() | Cộng dồn phí dịch vụ vào hóa đơn |
| Services | Booking | Room_receipt.updateDamageFee() | Cộng phí đền bù hư hỏng |
| Core | Booking | Booking.checkActiveBooking() | Kiểm tra trước khi xóa phòng |
| HR | Account | Employee.findByBranch() | Lấy danh sách nhân viên chi nhánh |
| HR | Booking | Room_receipt.tongHopDoanhThu() | Tổng hợp doanh thu cho báo cáo |

## 4. Cài đặt hệ thống

### Tech stack

| Layer | Công nghệ | Phiên bản |
|---|---|---|
| Frontend Web | React.js | 18.x |
| Frontend Mobile | React Native | 0.73.x |
| Backend API | Node.js + Express (hoặc Spring Boot) | Node 20 LTS |
| Database chính | PostgreSQL | 15.x |
| Cache / Session | Redis | 7.x |
| ORM | Prisma (hoặc JPA/Hibernate) | — |
| Authentication | JWT + BCrypt | — |

### API endpoints chính

| Module | Method | Endpoint | Mô tả |
|---|---|---|---|
| Account | POST | /api/auth/login | Đăng nhập |
| Account | POST | /api/auth/register | Đăng ký |
| Account | PUT | /api/auth/change-password | Đổi mật khẩu |
| Account | GET/PUT | /api/users/profile | Xem / cập nhật hồ sơ |
| Account | GET/POST/PUT/DELETE | /api/staff | Quản lý tài khoản nhân viên |
| Booking | GET/POST | /api/bookings | Đặt phòng |
| Booking | POST | /api/bookings/:id/checkin | Check-in |
| Booking | POST | /api/bookings/:id/checkout | Check-out + thanh toán |
| Booking | DELETE | /api/bookings/:id | Hủy đặt phòng |
| Services | GET/POST | /api/orders | Tạo / xem order |
| Services | POST | /api/damage-reports | Báo cáo hư hỏng |
| Services | GET/PUT | /api/products | Quản lý menu |
| Services | GET/POST | /api/providers | Nhà cung cấp |
| Services | POST | /api/import-receipts | Phiếu nhập kho |
| Core | GET/POST/PUT/DELETE | /api/branches | Quản lý chi nhánh |
| Core | GET | /api/customers | Khách hàng toàn hệ thống |
| Core | GET/PUT | /api/membership-tiers | Hạng hội viên |
| Core | GET/POST/PUT/DELETE | /api/room-types | Loại phòng |
| Core | GET/POST/PUT/DELETE | /api/rooms | Phòng hát |
| HR | GET/POST | /api/shifts | Ca làm việc |
| HR | POST | /api/evaluations | Đánh giá nhân viên |
| HR | GET | /api/reports/branch | Báo cáo chi nhánh |
| HR | GET | /api/reports/chain | Báo cáo toàn chuỗi |

### Hướng dẫn triển khai

**Yêu cầu môi trường:**
- Node.js 20 LTS hoặc Java 17+ (tùy backend)
- PostgreSQL 15, Redis 7
- Port mặc định: Backend 8080, Frontend 3000

**Các bước cài đặt:**

1. Cài đặt dependencies: `npm install` (frontend) / `mvn install` (backend)
2. Cấu hình biến môi trường: `.env` (DB_URL, REDIS_URL, JWT_SECRET)
3. Khởi tạo CSDL: chạy migration script hoặc `npm run migrate`
4. Seed dữ liệu mẫu: `npm run seed` (hạng hội viên, loại phòng mặc định)
5. Khởi chạy: `npm run start` (frontend), `npm run dev` (backend)

**Cấu hình multi-tenant (nhiều chi nhánh):** Mỗi yêu cầu API đính kèm `branchId` trong JWT payload; middleware tự động lọc dữ liệu theo chi nhánh.
