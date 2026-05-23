<!-- Pha II – Analysis, Section 4 -->

## II.4. Biểu đồ tuần tự phân tích

Vẽ **đầy đủ cho MỌI UC** trong module — không bỏ sót UC nào. Mỗi UC một biểu đồ riêng.
Luồng chuẩn: `Actor → Boundary → [Control] → Entity`.
Thông điệp **PHẢI bằng tiếng Việt tự nhiên**, đánh số thứ tự liên tục trong mỗi biểu đồ.
Phải thể hiện cả nhánh `alt` cho các kịch bản ngoại lệ đã viết ở II.1.

```plantuml
@startuml
title [Tên UC] – Tuần tự Phân tích

actor "Tên Actor" as Actor
participant "GDChinh\n<<Boundary>>" as B0
participant "GDTimX\n<<Boundary>>" as B1
participant "TenThucThe\n<<Entity>>" as E

Actor -> B0 : 1: sử dụng dịch vụ
activate B0
B0 -> B1 : 2: ký hợp đồng
activate B1
Actor -> B1 : 3: nhập từ khóa + tìm
B1 -> E : 4: gọi
activate E
E -> E : 5: timX()
E --> B1 : 6: trả về danh sách
deactivate E
B1 --> Actor : 7: hiển thị
Actor -> B1 : 8: chọn kết quả
deactivate B1

alt Ngoại lệ: không tìm thấy kết quả
  E --> B1 : trả về rỗng
  B1 --> Actor : thông báo không tìm thấy
end
@enduml
```
