---
name: audit
description: >
  Audit chất lượng & tính đầy đủ của tài liệu UP từng module dựa trên nội dung
  ĐÃ TẢI VỀ từ Google Docs (thư mục docs/tabs/exports/). Kích hoạt khi người dùng
  muốn: kiểm tra/audit tài liệu module, rà soát tính đầy đủ theo rubric UP, đối
  chiếu nhất quán giữa các pha (analysis ↔ design), kiểm tra nhất quán entity/bảng
  giữa các module, hoặc so sánh độ hoàn thiện giữa các module. Luôn dùng skill này
  khi người dùng nói "audit", "kiểm tra tài liệu", "rà soát module", "so sánh module".
---

# Audit Skill — Rà soát tài liệu UP theo rubric

Audit tài liệu UP của từng module dựa trên **nội dung tải về từ Google Docs**, không phải bản nháp local. Sinh báo cáo `docs/tabs/audit/audit-all-modules.md`.

---

## Nguồn dữ liệu (BẮT BUỘC)

Audit dựa trên `docs/tabs/exports/<module>/`:

```
docs/tabs/exports/
├── account/   { account.md  + screenshots/image_NN.png }
├── booking/   { booking.md  + screenshots/ }
├── services/  { services.md + screenshots/ }
└── core/      { core.md     + screenshots/ }
```

- `<module>.md` = text tab Google Docs (đã tải qua `gdocs tab-read`)
- `screenshots/` = ảnh nhúng trong tab (use-case, BCE, sequence, ERD, MVC...)

**Lý do:** bản trên Google Docs mới là sản phẩm cuối. Bản nháp local trong `account/`, `booking/`, `services/` có thể lệch (thiếu/thừa pha) so với Google Docs.

---

## Workflow khi được gọi

1. **Refresh exports nếu cần.** Nếu user yêu cầu audit dữ liệu mới nhất, tải lại từng tab:
   ```bash
   python3 .claude/skills/gdocs/scripts/cli.py tab-read <doc_id> "<Tên tab>" --output docs/tabs/exports/<module>
   ```
   Sau đó đổi tên file text về `<module>.md` cho nhất quán.
   Doc ID: `1H0pFNhmbX9yDMObxERGsZ0RqKjpX9Je6N60n4tYrB6s`. Tên tab: "Tài khoản & Thành viên" (account), "Quản lý đặt & trả phòng" (booking), "Dịch vụ & Sản phẩm" (services), "Quản trị cốt lõi" (core).
2. **Đọc** từng `exports/<module>/<module>.md`.
3. **Đếm ảnh** trong `exports/<module>/screenshots/`.
4. **Chạy 3 nhóm kiểm tra** A (đầy đủ nội dung), B (nhất quán liên pha), C (nhất quán liên module) cho mỗi module được yêu cầu.
5. **Ghi báo cáo** `docs/tabs/audit/audit-all-modules.md` theo format ở mục Output.
6. Với mỗi mục FAIL/PARTIAL, ghi gợi ý sửa ngắn gọn.

**Tham số gọi:** `all` (mặc định) hoặc danh sách module: `account booking services core`.

---

## A. Rubric đầy đủ nội dung (mỗi module)

Đánh dấu mỗi mục: ✓ (đủ) / ⚠ (một phần) / ✗ (thiếu).

| #   | Pha | Cần có                                              | Cách phát hiện trong text/ảnh export                                  |
| --- | --- | --------------------------------------------------- | --------------------------------------------------------------------- |
| R01 | I   | Bảng danh sách UC (ID, tên, actor, mô tả)           | có dòng bảng chứa `UC0`                                                |
| R02 | I   | Bảng danh sách Actor (tên + vai trò)                | heading `Actor`/`Tác nhân` + bảng theo sau                            |
| R03 | I   | Bảng quan hệ Include/Extend                         | cột chứa `Include` hoặc `Extend`                                       |
| R04 | I   | Ảnh biểu đồ UC tổng quan                            | có ≥1 ảnh ngữ cảnh pha I                                               |
| R05 | I   | Ảnh UC chi tiết (1 ảnh/UC)                           | số ảnh UC ≥ số UC ở R01                                                |
| R06 | II  | Bảng kịch bản chuẩn mỗi UC (Bước/Hành động/Kết quả) | có cột `Bước`, số mục ≥ số UC                                          |
| R07 | II  | Kịch bản ngoại lệ mỗi UC                            | heading `ngoại lệ`/`Kịch bản ngoại lệ`                                |
| R08 | II  | Mô hình hóa lớp 5 bước (văn xuôi + bảng trích danh từ) | có `Bước 1`…`Bước 5`                                               |
| R09 | II  | Ảnh sơ đồ lớp phân tích (BCE)                        | ảnh ngữ cảnh class/bce pha II                                         |
| R10 | II  | Ảnh sequence phân tích mỗi UC                        | số ảnh seq pha II ≥ số UC                                              |
| R11 | III | Thiết kế lớp thực thể 4 bước                        | có `Bước 1`…`Bước 4` trong mục thiết kế                              |
| R12 | III | Ảnh ERD                                             | heading `ERD` + ảnh                                                    |
| R13 | III | Wireframe mỗi UC (≥1 màn hình/UC)                   | số heading `Màn hình`/`Wireframe` ≥ số UC                             |
| R14 | III | Ảnh sơ đồ lớp thiết kế (MVC)                         | heading `Biểu đồ lớp`/`MVC` + ảnh                                     |
| R15 | III | Bảng chữ ký hàm (method, input, output, HTTP)       | bảng có cột `HTTP`/`Phương thức`/`Method`                            |
| R16 | III | Ảnh sequence thiết kế mỗi UC                        | số ảnh seq pha III ≥ số UC                                            |
| R17 | IV  | Bảng kế hoạch test (TC ID, module, kịch bản)        | có dòng bảng chứa `TC0`                                                |
| R18 | IV  | Mỗi TC có CSDL trước VÀ sau                          | trong mỗi mục TC có cả `trước` và `sau`                              |
| R19 | IV  | Mỗi TC có bảng kịch bản UI từng bước                | mỗi mục TC có bảng cột `Bước`                                          |
| R20 | IV  | Phủ: mỗi UC có ≥1 TC thành công + ≥1 TC thất bại    | đối chiếu tên TC với danh sách UC                                     |
| R21 | IV  | Edge case: khóa/trùng/không hợp lệ                  | tên TC có `khóa`/`đã tồn tại`/`trùng`/`không hợp lệ`                 |

---

## B. Nhất quán biến đổi liên pha (mỗi module)

Xác minh sự "biến đổi" đúng từ Analysis → Design.

| #   | Kiểm tra                                                                       |
| --- | ------------------------------------------------------------------------------ |
| T01 | Tên entity ở sơ đồ lớp phân tích (II) xuất hiện đủ ở thiết kế lớp thực thể (III) |
| T02 | Tên bảng ERD (`tbl*`) ánh xạ 1:1 với entity class (quy ước `tbl`+tên class)     |
| T03 | Tên method controller ở III xuất hiện trong bảng chữ ký hàm (R15)               |
| T04 | Số lớp Boundary ở III ≥ số màn hình wireframe (mỗi màn hình có 1 Boundary)      |

Báo cáo: với mỗi T, liệt kê phần tử **không khớp** (entity/method/bảng bị lệch giữa các pha).

---

## C. Nhất quán entity/bảng liên module

Các xung đột ĐÃ BIẾT (kiểm tra lại và báo cáo chính xác trạng thái hiện tại):

| #   | Khái niệm        | account            | booking                    | services      | core             | Vấn đề                       |
| --- | ---------------- | ------------------ | -------------------------- | ------------- | ---------------- | ---------------------------- |
| X01 | Khách hàng       | `User`/tblUser     | `KhachHang`/`Client`/tblClient | `Client`  | `Customer`/tblCustomer | **4 tên cho cùng 1 entity** |
| X02 | Hạng hội viên    | `MembershipTier`   | `HangHoiVien`/`MemberRanking` | (ẩn)       | `MembershipTier` | booking lệch tên             |
| X03 | Hóa đơn/receipt  | —                  | `HoaDon`/`Room_receipt`    | `Room_receipt`| —                | 2 tên giữa các module        |
| X04 | Phòng            | —                  | `Phong`/`Room`/tblRoom     | (ẩn)          | `Room`/tblRoom   | booking dùng tên Việt ở analysis |
| X05 | Nhân viên        | `Employee`/tblEmployee | `NhanVien`             | `Employee`    | (ẩn)             | booking dùng tên Việt        |
| X06 | Gọi liên module  | —                  | —                          | —             | gọi `Booking.getBookingHistory()` | phụ thuộc liên module chưa tài liệu hóa |

Quy tắc đánh giá: tên entity/bảng cho cùng một khái niệm **nên thống nhất** xuyên suốt các module. Tên tiếng Việt trong văn xuôi phân tích chấp nhận được, nhưng tên **class và bảng** (pha III) phải đồng nhất.

---

## D. Khoảng trống đã biết (nêu rõ trong báo cáo)

Kiểm tra lại các điểm sau trên bản export (vì bản local từng lệch so với Google Docs):

| Module   | Điểm cần xác minh                                                                 |
| -------- | --------------------------------------------------------------------------------- |
| services | Mục MVC pha III: có lẫn code hệ thống thư viện (LibrarianDAO/Reader/Book) không?   |
| services | Pha IV: có test case thật chưa, hay chỉ outline?                                    |
| services | Có khai báo tên bảng `tbl*` rõ ràng chưa?                                          |
| account  | Pha III/IV đã lên Google Docs chưa? (user dán tay)                                 |
| core     | Wireframe + test phủ đủ chưa?                                                       |
| booking  | Mốc tham chiếu — đủ 4 pha, ~15 TC.                                                  |

> Lưu ý: export services có ~42 ảnh (nhiều nhất) → bản Google Docs có thể đầy đủ hơn bản nháp local rất nhiều. PHẢI audit theo export, không theo bản nháp.

---

## Output — `docs/tabs/audit/audit-all-modules.md`

Cấu trúc báo cáo:

1. **Ma trận đầy đủ** — hàng = R01–R21, cột = các module, ô = ✓/⚠/✗.
2. **Bảng biến đổi liên pha** — T01–T04 mỗi module + danh sách phần tử lệch.
3. **Bảng nhất quán liên module** — X01–X06 kèm ghi chú trạng thái thực tế.
4. **Khoảng trống & gợi ý sửa** — nhóm theo module, mỗi mục ✗/⚠ kèm 1 dòng gợi ý.
5. **So sánh độ hoàn thiện** — đối chiếu mỗi module với booking (mốc đầy đủ nhất).

Mở đầu báo cáo ghi: ngày audit (hỏi/để trống nếu không có), commit hash hiện tại, danh sách module được audit, và số ảnh mỗi module.

---

## Lưu ý

- Audit là **read-only** với `exports/` — không sửa nội dung export.
- Khi đếm "số ảnh theo ngữ cảnh pha", dựa vào thứ tự ảnh + heading lân cận trong text (ảnh `image_NN.png` xuất hiện theo thứ tự đọc của tài liệu).
- Nếu một module thiếu cả pha (VD account chưa có III/IV trên Docs), đánh ✗ toàn bộ rubric pha đó và ghi rõ "chưa đẩy lên Google Docs".
