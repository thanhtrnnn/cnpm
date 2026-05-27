## III.2. Thiết kế mô hình MVC

Mô hình MVC được thiết kế theo kiến trúc **BCE (Boundary – Control – Entity)** với 3 tầng:
- **Boundary (Giao diện):** React components xử lý giao diện người dùng
- **Control (DAO):** Spring Boot Controllers + JPA Repositories xử lý nghiệp vụ và truy cập dữ liệu
- **Entity (Thực thể):** JPA Entities biểu diễn dữ liệu lưu trữ

---

### a) Chức năng Tạo order

**1. Tầng giao diện (Boundary)**

| Lớp | Component | Mô tả |
|------|-----------|-------|
| `OrderPage` | Page | Trang chính tạo order, chọn phòng và sản phẩm |
| `RoomSelector` | Panel | Chọn phòng đang hoạt động từ danh sách |
| `ProductSearchForm` | Form | Tìm kiếm sản phẩm theo tên |
| `ProductTable` | Table | Hiển thị danh sách sản phẩm với nút "Thêm" |
| `OrderCartPanel` | Panel | Giỏ hàng hiện tại, tổng tiền, nút xác nhận |
| `ConfirmOrderModal` | Modal | Xác nhận tạo order |

**2. Tầng điều khiển (Control/DAO)**

Xác định chữ ký hàm cho từng phương thức:

**a) Tạo order mới**

Tạo order => `createOrder()`
- Input: mã phòng, danh sách sản phẩm (tên + số lượng)
- Output: đối tượng Order vừa tạo
- Ứng viên tham số vào:
  - `createOrder(roomId: String, items: List<OrderItemRequest>)` → chọn (hướng đối tượng, gom nhóm dữ liệu)
  - `createOrder(roomId: String, productId: String, quantity: int)` → loại (gọi nhiều lần nếu nhiều sản phẩm)
- Ứng viên tham số ra:
  - `createOrder(): void` → loại (cần trả về order vừa tạo)
  - `createOrder(): OrderResponse` → chọn (trả về thông tin order)

**b) Tìm danh sách order theo trạng thái**

Tìm danh sách order => `getOrders()`
- Input: trạng thái order
- Output: danh sách order
- Ứng viên tham số vào:
  - `getOrders(status: OrderStatus)` → chọn (lọc theo trạng thái)
- Ứng viên tham số ra:
  - `getOrders(): List<OrderResponse>` → chọn (trả về danh sách)

**c) Tìm sản phẩm theo danh mục**

Tìm sản phẩm theo danh mục => `getByCategory()`
- Input: tên danh mục
- Output: danh sách sản phẩm
- Ứng viên tham số vào:
  - `getByCategory(category: String)` → chọn
- Ứng viên tham số ra:
  - `getByCategory(): List<MenuItem>` → chọn

**d) Tìm sản phẩm theo mã**

Tìm sản phẩm theo mã => `getById()`
- Input: mã sản phẩm
- Output: đối tượng sản phẩm
- Ứng viên tham số vào:
  - `getById(id: String)` → chọn
- Ứng viên tham số ra:
  - `getById(): MenuItem` → chọn

**3. Tầng thực thể (Entity)**

| Entity | Thuộc tính chính | Quan hệ |
|--------|-----------------|---------|
| `ServiceOrder` | id, orderedAt, status | ManyToOne→Room, OneToMany→ServiceOrderItem |
| `ServiceOrderItem` | quantity, unitPrice | ManyToOne→ServiceOrder, ManyToOne→MenuItem |
| `MenuItem` | id, name, category, price, stock, image, active | — |
| `Room` | id, name, branch | — |

**4. Sơ đồ lớp thiết kế**

```plantuml
@startuml
title Biểu đồ lớp thiết kế – Tạo order (React)

package "Boundary" #DDEEFF {
  class OrderPage <<Component>> {
    +handleCreateOrder() : void
  }

  class RoomSelector <<Component>> {
    -selectedRoom : Room (state)
    +handleSelectRoom(room) : void
    +render() : JSX
  }

  class ProductSearchForm <<Component>> {
    -keyword : string (state)
    +handleSubmit() : void
    +handleChange(e) : void
  }

  class ProductTable <<Component>> {
    -products : Array (state)
    +handleAddToCart(product) : void
    +render() : JSX
  }

  class OrderCartPanel <<Component>> {
    -cartItems : Array (state)
    -totalPrice : number (state)
    +handleConfirm() : void
    +handleRemoveItem(id) : void
  }

  class ConfirmOrderModal <<Component>> {
    +handleConfirm() : void
    +handleCancel() : void
  }
}

package "Control" #D4EDDA {
  class OrderController {
    +createOrder(request) : OrderResponse
    +getOrders(status) : List<OrderResponse>
  }

  class MenuItemController {
    +getByCategory(category) : List<MenuItem>
    +getById(id) : MenuItem
  }

  class ServiceOrderRepository {
    +save(order) : ServiceOrder
    +findByRoomId(roomId) : ServiceOrder
  }

  class MenuItemRepository {
    +findById(id) : Optional<MenuItem>
    +findByCategoryIgnoreCase(category) : List<MenuItem>
  }
}

package "Entity" #FFF3CD {
  class ServiceOrder {
    -id : String
    -orderedAt : LocalDateTime
    -status : OrderStatus
  }

  class ServiceOrderItem {
    -id : Long
    -quantity : int
    -unitPrice : BigDecimal
  }

  class MenuItem {
    -id : String
    -name : String
    -category : String
    -price : BigDecimal
    -stock : int
  }

  class Room {
    -id : String
    -name : String
  }
}

OrderPage --> RoomSelector
OrderPage --> ProductSearchForm
OrderPage --> ProductTable
OrderPage --> OrderCartPanel
OrderCartPanel --> ConfirmOrderModal

RoomSelector --> OrderController
ProductSearchForm --> MenuItemController
ProductTable --> MenuItemController
OrderCartPanel --> OrderController

OrderController --> ServiceOrderRepository
MenuItemController --> MenuItemRepository

ServiceOrderRepository --> ServiceOrder
MenuItemRepository --> MenuItem

ServiceOrder "1" --> "*" ServiceOrderItem
ServiceOrderItem "*" --> "1" MenuItem
ServiceOrder "*" --> "1" Room
@enduml
```

---

### b) Chức năng Báo cáo tình trạng hàng

**1. Tầng giao diện (Boundary)**

| Lớp | Component | Mô tả |
|------|-----------|-------|
| `OrderManagement` | Page | Trang quản lý order, hiển thị danh sách theo trạng thái |
| `StatusFilterTabs` | Panel | Tab lọc theo trạng thái (PENDING, PREPARING, SERVED, CANCELLED) |
| `OrderCard` | Card | Thông tin đơn hàng (phòng, sản phẩm, trạng thái) |
| `StatusUpdateModal` | Modal | Cập nhật trạng thái đơn hàng |

**2. Tầng điều khiển (Control/DAO)**

**a) Tìm danh sách order theo trạng thái**

Tìm danh sách order => `getOrders()`
- Input: trạng thái order
- Output: danh sách order
- Ứng viên tham số vào:
  - `getOrders(status: OrderStatus)` → chọn
- Ứng viên tham số ra:
  - `getOrders(): List<OrderResponse>` → chọn

**b) Cập nhật trạng thái order**

Cập nhật trạng thái order => `updateStatus()`
- Input: mã order, trạng thái mới
- Output: đối tượng order đã cập nhật
- Ứng viên tham số vào:
  - `updateStatus(id: String, status: OrderStatus)` → chọn
- Ứng viên tham số ra:
  - `updateStatus(): void` → loại (cần xác nhận thành công)
  - `updateStatus(): OrderResponse` → chọn (trả về order đã cập nhật)

**3. Tầng thực thể (Entity)**

| Entity | Thuộc tính chính | Quan hệ |
|--------|-----------------|---------|
| `ServiceOrder` | id, orderedAt, status | ManyToOne→Room, OneToMany→ServiceOrderItem |
| `OrderStatus` | PENDING, PREPARING, SERVED, CANCELLED | enum |

**4. Sơ đồ lớp thiết kế**

```plantuml
@startuml
title Biểu đồ lớp thiết kế – Báo cáo tình trạng hàng (React)

package "Boundary" #DDEEFF {
  class OrderManagement <<Component>> {
    +handleRefresh() : void
  }

  class StatusFilterTabs <<Component>> {
    -activeTab : OrderStatus (state)
    +handleTabChange(status) : void
  }

  class OrderCard <<Component>> {
    -order : OrderResponse (props)
    +handleStatusUpdate(id, status) : void
    +render() : JSX
  }

  class StatusUpdateModal <<Component>> {
    -selectedOrder : OrderResponse (state)
    +handleConfirm() : void
    +handleCancel() : void
  }
}

package "Control" #D4EDDA {
  class OrderController {
    +getOrders(status) : List<OrderResponse>
    +updateStatus(id, status) : OrderResponse
  }

  class ServiceOrderRepository {
    +findByStatus(status) : List<ServiceOrder>
    +save(order) : ServiceOrder
  }
}

package "Entity" #FFF3CD {
  class ServiceOrder {
    -id : String
    -orderedAt : LocalDateTime
    -status : OrderStatus
  }

  enum OrderStatus {
    PENDING
    PREPARING
    SERVED
    CANCELLED
  }
}

OrderManagement --> StatusFilterTabs
OrderManagement --> OrderCard
OrderCard --> StatusUpdateModal

StatusFilterTabs --> OrderController
StatusUpdateModal --> OrderController

OrderController --> ServiceOrderRepository
ServiceOrderRepository --> ServiceOrder
ServiceOrder --> OrderStatus
@enduml
```

---

### c) Chức năng Quản lý menu

**1. Tầng giao diện (Boundary)**

| Lớp | Component | Mô tả |
|------|-----------|-------|
| `MenuManagement` | Page | Trang quản lý menu (CRUD sản phẩm) |
| `CategoryFilter` | Panel | Lọc theo danh mục (Đồ uống, Đồ ăn, Trái cây) |
| `MenuItemTable` | Table | Danh sách sản phẩm với nút Sửa/Xóa |
| `MenuItemForm` | Form | Form thêm/sửa sản phẩm (tên, giá, tồn kho, hình ảnh) |

**2. Tầng điều khiển (Control/DAO)**

**a) Liệt kê tất cả sản phẩm**

Liệt kê sản phẩm => `getAll()`
- Input: danh mục (tùy chọn)
- Output: danh sách sản phẩm
- Ứng viên tham số vào:
  - `getAll()` → loại (không có tham số)
  - `getAll(category: String)` → chọn (lọc theo danh mục)
- Ứng viên tham số ra:
  - `getAll(): List<MenuItem>` → chọn

**b) Tìm sản phẩm theo mã**

Tìm sản phẩm theo mã => `getById()`
- Input: mã sản phẩm
- Output: đối tượng sản phẩm
- Ứng viên tham số vào:
  - `getById(id: String)` → chọn
- Ứng viên tham số ra:
  - `getById(): MenuItem` → chọn

**c) Thêm sản phẩm mới**

Thêm sản phẩm => `create()`
- Input: thông tin sản phẩm
- Output: sản phẩm vừa tạo
- Ứng viên tham số vào:
  - `create(item: MenuItem)` → chọn (hướng đối tượng)
- Ứng viên tham số ra:
  - `create(): MenuItem` → chọn (trả về sản phẩm vừa tạo)

**d) Cập nhật sản phẩm**

Cập nhật sản phẩm => `update()`
- Input: mã sản phẩm, thông tin mới
- Output: sản phẩm đã cập nhật
- Ứng viên tham số vào:
  - `update(id: String, item: MenuItem)` → chọn
- Ứng viên tham số ra:
  - `update(): MenuItem` → chọn

**e) Xóa sản phẩm**

Xóa sản phẩm => `delete()`
- Input: mã sản phẩm
- Output: không có
- Ứng viên tham số vào:
  - `delete(id: String)` → chọn
- Ứng viên tham số ra:
  - `delete(): void` → chọn (không cần trả về)

**3. Tầng thực thể (Entity)**

| Entity | Thuộc tính chính | Quan hệ |
|--------|-----------------|---------|
| `MenuItem` | id, name, category, price, stock, image, active | — |

**4. Sơ đồ lớp thiết kế**

```plantuml
@startuml
title Biểu đồ lớp thiết kế – Quản lý menu (React)

package "Boundary" #DDEEFF {
  class MenuManagement <<Component>> {
    +handleRefresh() : void
  }

  class CategoryFilter <<Component>> {
    -selectedCategory : string (state)
    +handleFilterChange(category) : void
  }

  class MenuItemTable <<Component>> {
    -items : Array (state)
    +handleEdit(id) : void
    +handleDelete(id) : void
    +render() : JSX
  }

  class MenuItemForm <<Component>> {
    -formData : MenuItem (state)
    -isEdit : boolean (state)
    +handleSubmit() : void
    +handleChange(e) : void
  }
}

package "Control" #D4EDDA {
  class MenuItemController {
    +getAll(category?) : List<MenuItem>
    +getById(id) : MenuItem
    +create(item) : MenuItem
    +update(id, item) : MenuItem
    +delete(id) : void
  }

  class MenuItemRepository {
    +save(item) : MenuItem
    +findById(id) : Optional<MenuItem>
    +deleteById(id) : void
    +findByCategoryIgnoreCase(category) : List<MenuItem>
  }
}

package "Entity" #FFF3CD {
  class MenuItem {
    -id : String
    -name : String
    -category : String
    -price : BigDecimal
    -stock : int
    -image : String
    -active : boolean
  }
}

MenuManagement --> CategoryFilter
MenuManagement --> MenuItemTable
MenuManagement --> MenuItemForm

CategoryFilter --> MenuItemController
MenuItemTable --> MenuItemController
MenuItemForm --> MenuItemController

MenuItemController --> MenuItemRepository
MenuItemRepository --> MenuItem
@enduml
```

---

### d) Chức năng Quản lý kho

**1. Tầng giao diện (Boundary)**

| Lớp | Component | Mô tả |
|------|-----------|-------|
| `InventoryPage` | Page | Trang quản lý tồn kho |
| `StockTable` | Table | Danh sách sản phẩm với số lượng tồn kho |
| `StockUpdateForm` | Form | Cập nhật số lượng tồn kho (nhập kho) |

**2. Tầng điều khiển (Control/DAO)**

**a) Liệt kê tất cả sản phẩm**

Liệt kê sản phẩm => `getAll()`
- Input: danh mục (tùy chọn)
- Output: danh sách sản phẩm
- Ứng viên tham số vào:
  - `getAll(category: String)` → chọn (lọc theo danh mục)
- Ứng viên tham số ra:
  - `getAll(): List<MenuItem>` → chọn

**b) Cập nhật tồn kho**

Cập nhật tồn kho => `update()`
- Input: mã sản phẩm, số lượng mới
- Output: sản phẩm đã cập nhật
- Ứng viên tham số vào:
  - `update(id: String, item: MenuItem)` → chọn (cập nhật toàn bộ MenuItem)
- Ứng viên tham số ra:
  - `update(): MenuItem` → chọn

**3. Tầng thực thể (Entity)**

| Entity | Thuộc tính chính | Quan hệ |
|--------|-----------------|---------|
| `MenuItem` | id, name, category, price, stock, image, active | — |

**4. Sơ đồ lớp thiết kế**

```plantuml
@startuml
title Biểu đồ lớp thiết kế – Quản lý kho (React)

package "Boundary" #DDEEFF {
  class InventoryPage <<Component>> {
    +handleRefresh() : void
  }

  class StockTable <<Component>> {
    -items : Array (state)
    +handleUpdateStock(id) : void
    +render() : JSX
  }

  class StockUpdateForm <<Component>> {
    -selectedItem : MenuItem (state)
    -newStock : number (state)
    +handleSubmit() : void
    +handleChange(e) : void
  }
}

package "Control" #D4EDDA {
  class MenuItemController {
    +getAll(category?) : List<MenuItem>
    +update(id, item) : MenuItem
  }

  class MenuItemRepository {
    +findAll() : List<MenuItem>
    +save(item) : MenuItem
  }
}

package "Entity" #FFF3CD {
  class MenuItem {
    -id : String
    -name : String
    -category : String
    -price : BigDecimal
    -stock : int
    -image : String
    -active : boolean
  }
}

InventoryPage --> StockTable
InventoryPage --> StockUpdateForm

StockTable --> MenuItemController
StockUpdateForm --> MenuItemController

MenuItemController --> MenuItemRepository
MenuItemRepository --> MenuItem
@enduml
```
