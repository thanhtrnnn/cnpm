<!-- Pha II – Analysis, Section 4 -->

## II.4. Biểu đồ tuần tự phân tích

Vẽ **đầy đủ cho MỌI UC** trong module — không bỏ sót UC nào. Mỗi UC một biểu đồ riêng.
Luồng chuẩn: `Actor → Boundary → [Control] → Entity`.
Arrow labels trong `@startuml` **PHẢI tiếng Anh ngắn gọn** (`click btnSearch`, `display results`, `enter keyword`). Kịch bản phiên bản 2 text bên ngoài PlantUML giữ tiếng Việt.
**Biểu đồ chỉ thể hiện luồng chính. Không dùng `alt`.** Ngoại lệ → viết block text riêng sau biểu đồ.

### Diễn giải tuần tự (Kịch bản phiên bản 2) — BẮT BUỘC

Bên cạnh biểu đồ PlantUML, PHẢI viết thêm **block diễn giải tuần tự** dạng **danh sách bullet (gạch đầu dòng)**, theo format "Kịch bản phiên bản 2". Block này mô tả chi tiết từng bước tương tác giữa Actor, Boundary và Entity bằng tiếng Việt tự nhiên.

**Format:**

```
**Kịch bản phiên bản 2 – UC [Tên UC]**

- [Actor] [hành động] để [mục đích].
- [Actor] chọn chức năng [tên chức năng] trên giao diện [BoundaryName].
- Lớp [BoundaryName] gọi lớp [NextBoundary].
- Lớp [NextBoundary] hiển thị giao diện cho [Actor].
- [Actor] hỏi [thông tin] từ [đối tượng].
- [đối tượng] trả lời [thông tin].
- [Actor] nhập [thông tin] và nhấn nút [hành động].
- Lớp [Boundary] gọi lớp [Entity] để xử lý.
- Lớp [Entity] gọi phương thức [simpleMethodName].
- Lớp [Entity] trả kết quả về cho lớp [Boundary].
- Lớp [Boundary] hiển thị kết quả cho [Actor].
...

**Ngoại lệ: [tên ngoại lệ]**
- Lớp [Entity] trả về [danh sách rỗng / kết quả thất bại].
- Lớp [Boundary] hiển thị [thông báo lỗi / nút thay thế].
```

**Quy tắc:**
- Kịch bản phiên bản 2 dùng **bullet** (gạch đầu dòng `- `), không đánh số
- Mỗi bước là một câu hoàn chỉnh bằng tiếng Việt
- Tên class giữ nguyên tiếng Anh, hậu tố `View` (LoginView, SearchRoomView, SearchXView, CreateXView...)
- Tên hàm trong mô tả PHẢI dùng tiếng Anh đơn giản (searchFreeRoom, checkLogin, addBooking...) — KHÔNG dùng tên tiếng Việt, KHÔNG có tham số/kiểu dữ liệu
- Mô tả cả Actor ↔ Boundary interaction (hỏi khách, nhập thông tin, nhấn nút)
- Mỗi nhánh ngoại lệ từ II.1 → một block "Ngoại lệ" riêng ở cuối (text only, không PlantUML)
- Số bước trong kịch bản phải khớp chính xác với số mũi tên trong biểu đồ PlantUML (kể cả return `-->`)

```plantuml
@startuml
' --- Main flow only — no alt blocks ---
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

title [UC Name] – Analysis Sequence ([N] steps)

actor "Actor Name" as Actor
boundary LoginView
boundary SearchRoomView
entity TenThucThe

Actor -> LoginView : 1: select function X
activate LoginView
LoginView -> SearchRoomView : 2: open search screen
activate SearchRoomView
Actor -> SearchRoomView : 3: enter keyword + click Search
SearchRoomView -> TenThucThe : 4: searchX()
activate TenThucThe
TenThucThe -> TenThucThe : 5: searchX()
TenThucThe --> SearchRoomView : 6: return results
deactivate TenThucThe
SearchRoomView --> Actor : 7: display results
deactivate SearchRoomView
deactivate LoginView
@enduml
```

**Ngoại lệ: searchX() không tìm thấy kết quả**
- Lớp `TenThucThe` trả về danh sách rỗng cho `SearchRoomView`.
- `SearchRoomView` hiển thị thông báo "Không tìm thấy kết quả".
- Actor nhập lại từ khóa khác (quay về bước 3).
