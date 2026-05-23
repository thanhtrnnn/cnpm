<!-- Pha III – Design, Section 4 -->

## III.4. Biểu đồ tuần tự thiết kế

**Input:** Biểu đồ tuần tự phân tích (II.4) + Sơ đồ lớp thiết kế (III.3.2).

Nâng cấp từ II.4:
- Thêm lớp DAO vào luồng (giữa Boundary và Entity).
- Thay **toàn bộ** thông điệp tiếng Việt thành **tên hàm tiếng Anh chính xác** (khớp với chữ ký đã định nghĩa ở III.3.2).
- Bắt sự kiện giao diện:
  - **JFrame:** `actionPerformed(e: ActionEvent)`
  - **React:** `handleSubmit()`, `onClick()`
- Đánh số thứ tự liên tục.

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

**Variant React:**

```plantuml
@startuml
title [Tên UC] – Tuần tự Thiết kế (React)

actor "Tên Actor" as Actor
participant "PageChinh\n<<Component>>" as B0
participant "PageTimX\n<<Component>>" as B1
participant "TenEntityDAO\n<<DAO>>" as DAO
participant "TenEntity\n<<Entity>>" as E

Actor -> B0 : 1: navigate to /module
activate B0
B0 -> B1 : 2: <Route> render PageTimX
activate B1
B0 -> B1 : 3: pass props (nv : NhanVien)
B1 --> B0 : 4: render UI
Actor -> B1 : 5: nhập từ khóa + click Tìm
B1 -> B1 : 6: handleSubmit()
B1 -> DAO : 7: fetch /api/timX
activate DAO
DAO -> E : 8: timX(ten : String) : List<TenEntity>
activate E
E --> DAO : 9: List<TenEntity>
deactivate E
DAO --> B1 : 10: JSON response
deactivate DAO
B1 --> Actor : 11: render table data

alt timX() trả về rỗng
  DAO --> B1 : empty array
  B1 --> Actor : render "Không tìm thấy"
end
@enduml
```
