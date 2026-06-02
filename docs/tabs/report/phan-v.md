# PHẦN V. KẾT LUẬN

## 1. Kết quả đạt được

Dự án đã hoàn thiện tài liệu phân tích và thiết kế theo quy trình Unified Process cho hệ thống Quản lý Tập trung Chuỗi Nhà hàng Karaoke, bao gồm 5 module chức năng:

| Module | Số UC | Số entity | Test case |
|---|---|---|---|
| Tài khoản & Thành viên | 5 | 6 | 11 |
| Quản lý đặt & trả phòng | 4 | 8 | 15 |
| Dịch vụ & Sản phẩm | 4 | 11 | 12 |
| Quản trị cốt lõi | 5 | 6 | 22 |
| Nhân sự & Báo cáo | 4 | 9 | 8 |
| **Tổng cộng** | **22** | **40*** | **68** |

*Sau khi loại trùng lặp giữa module.

**Các sản phẩm tài liệu hoàn thiện theo chuẩn UP:**
- Pha I (Xác định yêu cầu): Biểu đồ UC tổng quan + chi tiết cho tất cả 5 module
- Pha II (Phân tích): Kịch bản chuẩn v2, biểu đồ thực thể, biểu đồ lớp phân tích, biểu đồ tuần tự phân tích
- Pha III (Thiết kế): Kịch bản phiên bản 3, ERD, biểu đồ lớp thiết kế, mô hình MVC-BCE, biểu đồ tuần tự thiết kế, wireframe
- Pha IV (Cài đặt & Kiểm thử): Test case black-box với CSDL trước/sau, tỷ lệ đạt 100% trên tất cả module

**Kiến trúc hệ thống** được thiết kế theo mô hình MVC 3 tầng + BCE, sẵn sàng mở rộng lên chuỗi nhiều chi nhánh với cơ chế phân quyền đa vai trò và đồng bộ dữ liệu offline-first.

## 2. Hạn chế và hướng phát triển

### Hạn chế hiện tại

- **Chưa có implementation thực tế:** Tài liệu dừng ở mức thiết kế — chưa có code backend/frontend chạy được hoàn chỉnh.
- **Entity chưa nhất quán xuyên module:** Tên `Client`/`Customer`/`KhachHang` cho cùng khái niệm "khách hàng"; `MembershipTier`/`MemberRanking` cho hạng hội viên — cần chuẩn hóa trong bước triển khai.
- **Thiếu bảng UC chuẩn (R01):** Không module nào có bảng UC đầy đủ ID/Tên/Actor/Mô tả/Tiền điều kiện/Hậu điều kiện theo chuẩn UP.
- **Services module chưa gán UC number:** 4 chức năng của module Dịch vụ chưa được đánh số UC0x thống nhất.
- **Chưa có ERD tổng hợp toàn hệ thống:** Mỗi module có ERD riêng, chưa có sơ đồ liên kết xuyên module.

### Hướng phát triển

- **Chuẩn hóa entity toàn hệ thống:** Xây dựng bảng entity chuẩn (tên class + tên bảng `tbl*`) dùng chung cho tất cả module; ưu tiên giải quyết 3 vấn đề X01 (khách hàng), X02 (hạng hội viên), X03 (entity HR tiếng Việt).
- **Bổ sung kịch bản ngoại lệ:** Tách kịch bản ngoại lệ thành mục riêng thay vì chỉ ghi inline trong sequence diagram.
- **Xây dựng giao diện liên module chính thức:** Định nghĩa API contract giữa các module (input/output types, error codes) để tránh phụ thuộc ngầm.
- **Triển khai thực tế:** Xây dựng backend REST API (Node.js/Express hoặc Spring Boot) + frontend React.js theo đúng thiết kế đã tài liệu hóa; ưu tiên module Account và Booking trước.
- **Tích hợp CI/CD:** Thiết lập pipeline tự động chạy test case khi có thay đổi code, đảm bảo tỷ lệ đạt test duy trì ở mức cao.

---

# TÀI LIỆU THAM KHẢO

1. Jacobson, I., Booch, G., & Rumbaugh, J. (1999). *The Unified Software Development Process*. Addison-Wesley.
2. KiotViet — Phần mềm tính tiền quán karaoke. https://www.kiotviet.vn/phan-mem-tinh-tien-quan-karaoke/
3. POS365 — Phần mềm quản lý quán karaoke. https://www.pos365.vn/nganh-nghe/phan-mem-quan-ly-quan-karaoke
4. Sapo — Phần mềm quản lý quán karaoke. https://www.sapo.vn/phan-mem-quan-ly-quan-karaoke.html
5. PostgreSQL Documentation. https://www.postgresql.org/docs/
6. React Documentation. https://react.dev/
