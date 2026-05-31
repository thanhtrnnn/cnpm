<!-- Pha III – Design, Section 4 -->

## III.4. Biểu đồ tuần tự thiết kế

**Input:** Biểu đồ tuần tự phân tích (II.4) + Sơ đồ lớp thiết kế (III.3.2).

Nâng cấp từ II.4:
- Thêm lớp **Controller** vào luồng (giữa Boundary và Entity) — KHÔNG dùng DAO.
- Thay **toàn bộ** thông điệp tiếng Việt thành **tên hàm tiếng Anh chính xác** (khớp với chữ ký đã định nghĩa ở III.3.2).
- Bắt sự kiện giao diện:
  - **JFrame:** `actionPerformed(e: ActionEvent)`
  - **React:** `btnTênClick()`, `formLoad()`, `showMessage()`
- Đánh số thứ tự liên tục.

### Diễn giải tuần tự (Kịch bản phiên bản 3) — BẮT BUỘC

Bên cạnh biểu đồ PlantUML, PHẢI viết thêm **block diễn giải tuần tự** dưới dạng danh sách đánh số, theo format "Kịch bản phiên bản 3". Block này mô tả chi tiết từng bước tương tác giữa Actor, Boundary, DAO và Entity, có sử dụng tên hàm Java + kiểu dữ liệu.

**Format:**

```
**Kịch bản phiên bản 3 – UC [Tên UC]**

1. [Actor] [hành động] trên giao diện [TênView].
2. Lớp [TênView] gọi phương thức [btnTênClick()].
3. Phương thức [btnTênClick()] gọi lớp [EntityController].
4. Lớp [EntityController] gọi phương thức [methodName(param)] của lớp [Entity].
5. Lớp [Entity] thực thi [methodName()].
6. Lớp [Entity] trả kết quả về cho lớp [EntityController].
7. Lớp [EntityController] trả kết quả về cho lớp [TênView].
8. Lớp [TênView] hiển thị kết quả cho [Actor].
...
N. Phương thức [btnTênClick()] gọi phương thức [methodName] của lớp [EntityController].
N+1. Phương thức [methodName] thực thi.
N+2. Phương thức [methodName] gọi lớp [Entity] để đóng gói kết quả.
N+3. Lớp [Entity] đóng gói từng đối tượng [Entity].
N+4. Lớp [Entity] trả về đối tượng cho phương thức [methodName].
N+5. Phương thức [methodName] trả về kết quả cho phương thức [btnTênClick()].
...

**Ngoại lệ: [tên ngoại lệ]**
- Phương thức [methodName] trả về [giá trị rỗng/false].
- Phương thức actionPerformed hiển thị thông báo [thông báo lỗi].
```

**Quy tắc:**
- Mỗi bước là một câu hoàn chỉnh bằng tiếng Việt
- Tên phương thức/class giữ nguyên tiếng Anh (khớp với III.3.2)
- Tham số kiểu ghi rõ: `searchFreeRoom(checkin: Date, checkout: Date)`
- Mô tả cả Actor ↔ Boundary interaction (hỏi khách, nhập thông tin, nhấn nút)
- Mỗi nhánh ngoại lệ từ II.1 → một block "Ngoại lệ" riêng ở cuối

**Variant JFrame:**

```plantuml
@startuml
title [Tên UC] – Tuần tự Thiết kế (JFrame)

actor "Tên Actor" as Actor
participant "GDChinhFrm\n<<Boundary>>" as B0
participant "GDTimXFrm\n<<Boundary>>" as B1
participant "TenEntityDAO\n<<DAO>>" as DAO
participant "TenEntity\n<<Entity>>" as E

Actor -> B0 : 1: sd dịch vụ trả góp
activate B0
B0 -> B1 : 2: actionPerformed(e : ActionEvent)
activate B1
B0 -> B1 : 3: TimXFrm(nv : NhanVien)
B1 --> B0 : 4: hiển thị
Actor -> B1 : 5: nhập từ khóa + nhấn Tìm
B1 -> B1 : 6: actionPerformed(e : ActionEvent)
B1 -> DAO : 7: gọi
activate DAO
DAO -> E : 8: timX(ten : String) : List<TenEntity>
activate E
E --> DAO : 9: List<TenEntity>
deactivate E
DAO --> B1 : 10: trả về
deactivate DAO
B1 --> Actor : 11: hiển thị danh sách

alt timX() trả về rỗng
  DAO --> B1 : List rỗng
  B1 --> Actor : thông báo không tìm thấy
end
@enduml
```

**Variant React MVC:**

**Lưu ý:** Tên participant dùng hậu tố `View` (LoginView, SearchRoomView, CreateOrderView...) theo quy ước ở III.3.2.

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

title [Tên UC] – Tuần tự Thiết kế (React MVC)

actor "Tên Actor" as Actor
boundary SearchRoomView
boundary CreateOrderView
control OrderController
entity Room
entity Order

Actor -> SearchRoomView : 1: nhập từ khóa + click Tìm
activate SearchRoomView
SearchRoomView -> SearchRoomView : 2: btnSearchRoomClick()
SearchRoomView -> OrderController : 3: fetch /api/searchRoom
activate OrderController
OrderController -> Room : 4: searchRoomByName(roomName : String) : List<Room>
activate Room
Room --> OrderController : 5: List<Room>
deactivate Room
OrderController --> SearchRoomView : 6: JSON response
deactivate OrderController
SearchRoomView --> Actor : 7: displayActiveRooms(rooms)
deactivate SearchRoomView

Actor -> CreateOrderView : 8: chọn phòng + click Tạo order
activate CreateOrderView
CreateOrderView -> CreateOrderView : 9: formLoad()
CreateOrderView -> OrderController : 10: fetch /api/saveOrder
activate OrderController
OrderController -> Order : 11: saveOrder(order : Order) : boolean
activate Order
Order --> OrderController : 12: true
deactivate Order
OrderController --> CreateOrderView : 13: JSON response
deactivate OrderController
CreateOrderView --> Actor : 14: showMessage("Tạo order thành công")
deactivate CreateOrderView

alt saveOrder() trả về false
  Order --> OrderController : false
  OrderController --> CreateOrderView : error
  CreateOrderView --> Actor : showMessage("Tạo order thất bại")
end
@enduml
```
