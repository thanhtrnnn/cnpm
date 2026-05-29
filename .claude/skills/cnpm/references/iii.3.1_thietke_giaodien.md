<!-- Pha III – Design, Section 3.1 -->

## III.3.1. Thiết kế giao diện

Vẽ wireframe ASCII cho **từng màn hình** của module. Thể hiện đầy đủ: tiêu đề, các ô nhập liệu, bảng kết quả, các nút bấm.

**Header bảng PHẢI dùng thuộc tính thật của Entity (BẮT BUỘC):**
Tên cột trong bảng wireframe PHẢI là tên thuộc tính (attribute) của Entity class, KHÔNG phải tên hiển thị giao diện. VD: dùng `ma`, `ten`, `ngayMuon` — KHÔNG dùng "Mã sách", "Tên sách", "Ngày mượn".

Ví dụ:
```
┌──────────────────────────────────────────┐
│           Tên màn hình                   │
│                                          │
│  Nhãn 1:  [________________________]     │
│  Nhãn 2:  [________________________]     │
│                              [ Tìm ]     │
│ ┌──────┬────────┬──────────┬───────┐     │
│ │ ma   │ ten    │ ngayTao   │  ...  │     │
│ │      │ click  │          │       │     │
│ │      │        │          │       │     │
│ └──────┴────────┴──────────┴───────┘     │
│  [ Hủy ]                  [ Tiếp tục ]   │
└──────────────────────────────────────────┘
```
