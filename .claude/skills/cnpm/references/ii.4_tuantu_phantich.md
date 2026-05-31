<!-- Pha II – Analysis, Section 4 -->

## II.4. Biểu đồ tuần tự phân tích

Vẽ **đầy đủ cho MỌI UC** trong module — không bỏ sót UC nào. Mỗi UC một biểu đồ riêng.
Luồng chuẩn: `Actor → Boundary → [Control] → Entity`.
Thông điệp **PHẢI bằng tiếng Việt tự nhiên**, đánh số thứ tự liên tục trong mỗi biểu đồ.
Phải thể hiện cả nhánh `alt` cho các kịch bản ngoại lệ đã viết ở II.1.

### Diễn giải tuần tự (Kịch bản phiên bản 2) — BẮT BUỘC

Bên cạnh biểu đồ PlantUML, PHẢI viết thêm **block diễn giải tuần tự** dưới dạng danh sách đánh số, theo format "Kịch bản phiên bản 2". Block này mô tả chi tiết từng bước tương tác giữa Actor, Boundary và Entity bằng tiếng Việt tự nhiên.

**Format:**

```
**Kịch bản phiên bản 2 – UC [Tên UC]**

1. [Actor] [hành động] để [mục đích].
2. [Actor] chọn chức năng [tên chức năng] trên giao diện [BoundaryName].
3. Lớp [BoundaryName] gọi lớp [NextBoundary].
4. Lớp [NextBoundary] hiển thị giao diện cho [Actor].
5. [Actor] hỏi [thông tin] từ [đối tượng].
6. [đối tượng] trả lời [thông tin].
7. [Actor] nhập [thông tin] và nhấn nút [hành động].
8. Lớp [Boundary] gọi lớp [Entity] để xử lý.
9. Lớp [Entity] gọi phương thức [simpleMethodName].
10. Lớp [Entity] trả kết quả về cho lớp [Boundary].
11. Lớp [Boundary] hiển thị kết quả cho [Actor].
...

**Ngoại lệ: [tên ngoại lệ]**
- Lớp [Entity] trả về [danh sách rỗng / kết quả thất bại].
- Lớp [Boundary] hiển thị [thông báo lỗi / nút thay thế].
```

**Quy tắc:**
- Mỗi bước là một câu hoàn chỉnh bằng tiếng Việt
- Tên class giữ nguyên tiếng Việt, hậu tố `View` (LoginView, StaffHomeView, SearchRoomView, DamageReportView, ConfirmReportView...)
- Tên hàm trong mô tả và biểu đồ PHẢI dùng tiếng Anh đơn giản (searchFreeRoom, checkLogin, addBooking...) — KHÔNG dùng tên tiếng Việt, KHÔNG có tham số/kiểu dữ liệu
- Mô tả cả Actor ↔ Boundary interaction (hỏi khách, nhập thông tin, nhấn nút)
- Mỗi nhánh ngoại lệ từ II.1 → một block "Ngoại lệ" riêng ở cuối
- Số bước phải khớp chính xác với các mũi tên trong biểu đồ PlantUML

```plantuml
@startuml
' --- Layout & Spacing Skinparams ---
skinparam shadowing false
skinparam SequenceMessageAlign left

skinparam SequenceLifeLineBackgroundColor #7AD2FF
skinparam SequenceLifeLineBorderColor #000000

<style>
sequenceDiagram {
  Shadowing 0
  RoundCorner 0
  FontName "Arial"
  FontSize 10
  FontColor #000000

  participant {
    BackgroundColor #7AD2FF
    LineColor #000000
    LineThickness 1
  }

  actor {
    BackgroundColor transparent
    LineColor #000000
  }
  boundary {
    BackgroundColor #7AD2FF
    LineColor #000000
  }
  control {
    BackgroundColor #7AD2FF
    LineColor #000000
  }
  entity {
    BackgroundColor #7AD2FF
    LineColor #000000
  }

  lifeline {
    LineColor #000000
    LineStyle 5-5
  }

  arrow {
    LineColor #000000
    LineThickness 1
    FontSize 10
  }
}
</style>

title [Tên UC] – Tuần tự Phân tích

actor "Tên Actor" as Actor
boundary LoginView
boundary SearchRoomView
entity TenThucThe

Actor -> LoginView : 1: click chức năng X
activate LoginView
LoginView -> SearchRoomView : 2: mở giao diện tìm X
activate SearchRoomView
Actor -> SearchRoomView : 3: nhập từ khóa + nhấn Tìm
SearchRoomView -> TenThucThe : 4: gọi searchX()
activate TenThucThe
TenThucThe -> TenThucThe : 5: searchX()
TenThucThe --> SearchRoomView : 6: trả về danh sách
deactivate TenThucThe
SearchRoomView --> Actor : 7: hiển thị kết quả
deactivate SearchRoomView
deactivate LoginView

alt Ngoại lệ: không tìm thấy kết quả
  TenThucThe --> SearchRoomView : trả về rỗng
  SearchRoomView --> Actor : thông báo không tìm thấy
end
@enduml
```
