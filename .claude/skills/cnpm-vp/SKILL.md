---
name: cnpm-vp
description: >
  Tạo biểu đồ trong Visual Paradigm (use case, lớp, tuần tự, giao tiếp, trạng thái, hoạt động,
  gói, thành phần, triển khai, đối tượng, ERD, flowchart, DFD, BPMN) thông qua VP MCP server,
  rồi xuất ảnh và nhúng vào tài liệu UP. Kích hoạt khi người dùng muốn: vẽ biểu đồ UML trong
  Visual Paradigm, tạo diagram trong VP, export ảnh VP, nhúng ảnh VP vào tài liệu, hoặc bất kỳ yêu cầu
  nào liên quan đến việc sử dụng Visual Paradigm kết hợp với tài liệu CNPM/UP.
  LUÔN dùng skill này khi người dùng nhắc đến "Visual Paradigm", "VP", "vẽ trong VP",
  "xuất ảnh VP", hoặc muốn diagram chuyên nghiệp thay vì PlantUML code block.
---

# CNPM-VP Skill — Visual Paradigm MCP Integration

Tạo biểu đồ trực tiếp trong Visual Paradigm qua VP MCP server, xuất ảnh, và nhúng vào
tài liệu UP. Kết hợp với skill `cnpm` để sinh nội dung tài liệu.

Danh mục đầy đủ 121 tool (tên, tham số theo thứ tự, công dụng): [`references/vp-mcp-tools.md`](references/vp-mcp-tools.md).

---

## Điều kiện tiên quyết

VP MCP server là **plugin chạy TRONG Visual Paradigm** (không cần Docker): mở VP có cài plugin
`visual-paradigm-mcp-plugin` thì server tự chạy ở `http://localhost:2026`: MCP streamable HTTP ở
`POST /mcp` (plugin >= 1.32.8; `/sse` cũ đã bỏ), gọi thẳng tool `POST /api/execute`. Cần VP đang mở và
một project đang mở.

**Bước 1 — Mở Visual Paradigm** (plugin tự khởi động server). Chưa cài hoặc vừa đổi plugin:
```bash
cd visual-paradigm-mcp-plugin && ./run install   # rồi Quit HẲN VP và mở lại (VP giữ plugin cũ trong RAM)
```
`./run docker-up` chỉ là proxy tuỳ chọn (cổng host 2027 → VP:2026), vẫn cần VP đang chạy — không dùng cho luồng này.

**Bước 2 — Đăng ký MCP server với Claude Code / Codex.** Cách gọn nhất: cài plugin `visual-paradigm`
(MCP config + skill tiếng Anh dùng chung) từ marketplace của repo plugin:
```text
Claude Code:  /plugin marketplace add thanhtrnnn/vp-mcp
              /plugin install visual-paradigm@visual-paradigm-mcp
Codex:        codex plugin marketplace add thanhtrnnn/vp-mcp
              codex plugin add visual-paradigm@visual-paradigm-mcp
```
Hoặc chỉ đăng ký server:
```bash
.claude/skills/cnpm-vp/scripts/vp-mcp-setup.sh
```
Script tạo/cập nhật `.mcp.json` ở project root với `{"type": "http", "url": "http://localhost:2026/mcp"}` và
sửa entry SSE cũ (hoặc `claude mcp add --transport http --scope user visual-paradigm http://localhost:2026/mcp`;
Codex: `codex mcp add visual-paradigm --url http://localhost:2026/mcp`). Codex đọc skill này qua
`.agents/skills/` (symlink tới `.claude/skills/`).

**Bước 3 — Xác nhận kết nối:**
```bash
.claude/skills/cnpm-vp/scripts/vp-mcp-verify.sh
```
Script kiểm tra: `POST /mcp` trả lời, MCP `initialize` (in `serverInfo.version`), số tool từ
`tools/list` (đủ 121 với plugin >= 1.32.6), `.mcp.json` đúng cấu hình.

Sau đó restart Claude Code / Codex để nhận MCP config mới. **Danh sách tool của một session chốt lúc khởi động:**
đổi plugin giữa chừng thì tool mới KHÔNG hiện — gọi qua HTTP `POST /api/execute` (cú pháp ở đầu
`references/vp-mcp-tools.md`). Trước khi vẽ: `getProjectInfo` để chắc đang mở đúng file `.vpp`.

---

## Nguyên tắc cốt lõi

1. **Skill `cnpm` sinh nội dung, skill `cnpm-vp` vẽ trong VP.** Không tự viết PlantUML khi người dùng muốn dùng VP.
2. **Thứ tự tạo diagram:** Tạo diagram → thêm elements → thêm relationships → kiểm tra (`getDiagramElements` / `getDiagramGeometry`) → export.
3. **Ảnh VP ưu tiên hơn PlantUML** khi người dùng yêu cầu hoặc khi diagram quá phức tạp cho code block.
4. **Để layout tự đặt vị trí; chỉ truyền x/y khi thật cần ghim một shape.** Plugin ≥ 1.32.5 dùng ELK (Eclipse Layout Kernel, VP đóng gói sẵn trong `lib02.jar`): sau MỖI lần gọi `add*`, mọi loại diagram trừ sequence và BPMN được xếp lại. Layout tự chia tầng, giảm giao cắt, vẽ đường vuông góc và đặt nhãn cạnh đường. Sequence và BPMN có layout riêng, vốn đã đạt.
   - Truyền `x`,`y` > 0 (hoặc gọi `setElementBounds`) sẽ **ghim** shape: đường nối đi vòng quanh nó. Ghim nhiều làm layout kém hơn, nên mặc định truyền 0.
   - `autoLayoutDiagram` bỏ ghim và xếp lại toàn bộ diagram. `rerouteConnectors` chỉ vẽ lại đường, giữ nguyên vị trí shape.
   - Quy trình: gọi `add*` (x/y = 0) → `getDiagramGeometry` kiểm theo Luật bố cục (mục 5) → `exportDiagramImage` rồi XEM ảnh.
5. **Luật bố cục (BẮT BUỘC — user yêu cầu 2026-10-14):**
   - Mọi đoạn đường nối chỉ được nằm **ngang hoặc dọc**, ở mọi loại diagram, kể cả use case và communication. Không có đoạn xiên, không gãy chéo kiểu zigzag, không đi vòng hình chữ V. Vòng tự nối vẽ hình chữ nhật.
   - **Không hình 3D.** Node, device, execution environment trong deployment là chữ nhật phẳng, giữ stereotype và tên.
   - **Không chồng/đè:**
     - shape không chồng nhau;
     - đường không xuyên qua shape không phải đầu mút của nó;
     - hai đường không chạy đè lên nhau;
     - nhãn không đè shape hoặc nhãn khác, và không bị cắt thành `...`.
   - Kiểm bằng `getDiagramGeometry`: mọi cặp điểm liên tiếp của connector phải cùng x hoặc cùng y. Vi phạm thì gọi `autoLayoutDiagram` (bỏ các ghim) thay vì tự chỉnh toạ độ từng điểm.

---

## Nguyên tắc cấu trúc (khi vẽ trong VP)

Khi tạo biểu đồ trong VP, PHẢI tuân thủ các quy tắc cấu trúc sau:

1. **BCE — phân tách bằng TÊN + BỐ CỤC, KHÔNG bằng package màu:** Class diagram tách 3 vai trò Boundary | Control/DAO | Entity qua **tên hậu tố** (Boundary = `View` (phân tích) / `Page` hoặc `Frm` (thiết kế), Control = `Controller`, DAO = `DAO`, Entity = PascalCase trơn) và **bố cục** (hàng Boundary trên cùng, Entity bên dưới). KHÔNG cần package bao quanh.
2. **Hộp lớp để TRẮNG (khớp biểu đồ mẫu):** Biểu đồ lớp tham chiếu của môn học (`exports/services/screenshots`, `exports/account/screenshots`) dùng **hộp trắng trơn — KHÔNG màu nền, KHÔNG package màu**.
   - Mặc định: gọi `addClass` **KHÔNG** truyền `packageName`/`packageColor` (để trắng).
   - Chỉ đóng package màu khi user yêu cầu tường minh.
   - Màu xanh `#7AD2FF` **chỉ** áp dụng cho actor / use case / lifeline / activation — VP MCP **tự tô** (xem mục Render). KHÔNG tô màu hộp lớp.
3. **Stereotype lớp: KHÔNG dùng trên class diagram (khớp mẫu):** Mẫu không hiển thị `<<Boundary>>`/`<<Entity>>` trên hộp lớp.
   - Mặc định: `addClass` **KHÔNG** truyền `stereotype`.
   - Ngoại lệ: sequence **lifeline** VẪN truyền `lifelineType` = `boundary`/`control`/`entity`/`actor` để VP hiển thị icon tròn-gạch đúng (đây là yêu cầu của mẫu tuần tự).

4. **Phân biệt ngôn ngữ theo pha (NGHIÊM NGẶT — khớp cnpm):**
   - **Arrow label trong biểu đồ VP (@message):** TOÀN BỘ tiếng Anh ngắn gọn trong cả hai pha (`enter keyword + click Search`, `checkLogin()`, `display results`). KHÔNG dùng tiếng Việt trong message VP.
   - **Pha Thiết kế:** Arrow = tên hàm tiếng Anh đầy đủ + kiểu dữ liệu (`searchFreeRoom(checkin: Date, checkout: Date): List<Room>`).
   - **Kịch bản phiên bản 2/3 (text bên ngoài biểu đồ):** Giữ tiếng Việt tự nhiên.
   - **Tên class/bảng DB:** BẮT BUỘC tiếng Anh PascalCase (`Client`, `Employee`, `tblClient`). Tên Việt chỉ trong văn xuôi.
   - **Tên method:** Luôn tiếng Anh mọi pha (`checkLogin`, `searchFreeRoom`).
   - **Các loại diagram khác** (state, activity, communication, package…): nhãn theo cùng quy tắc (tiếng Anh ngắn). Chỉ khi user chọn profile giáo trình BG CNPM 2020 mới dùng tiếng Việt KHÔNG DẤU (`Hien thi GD chinh SV`, `goi`, `tra ve`); định danh luôn không dấu, không khoảng trắng.
5. **UC Decomposition:** Include → Extend → Generalization. UC chính ở giữa, UC con tỏa ra.
6. **Bố cục:** layout tự xếp (xem Nguyên tắc cốt lõi 4–5).
   - Class: tầng theo chiều quan hệ, giống sách: JSP/Boundary trên → DAO giữa → Entity dưới. Lớp cha/interface nằm trên lớp con.
   - UC: actor là một cột bên trái, UC nằm trong system boundary.
   - Muốn chỉnh thì dùng `setElementBounds` / `moveCommunicationLifeline` (sẽ ghim shape), rồi kiểm lại bằng `getDiagramGeometry`.
7. **Sequence participant order:** Actor → Boundary → [Control] → DAO → Entity
8. **Công nghệ giao diện:** Phải thống nhất JFrame (Java Swing) hoặc HTML (React) từ đầu. Ảnh hưởng đến Boundary class attributes.

### Chọn công nghệ giao diện

Hỏi người dùng ngay từ đầu:
- **JFrame (Java Swing):** Boundary = JFrame, attributes = JTextField/JButton/JTable, event = `actionPerformed(e: ActionEvent)`. Tên class: `[EnglishName]Frm` (VD: `LoginFrm`, `SearchRoomFrm`, `EditRoomFrm`). **KHÔNG dùng** tiền tố `GD` hay tên tiếng Việt.
- **HTML (React):** Boundary = Component, attributes = State/JSX, event = `handleSubmit/onClick`. Tên class: tiếng Anh + hậu tố loại component:

| Hậu tố | Loại component | Ví dụ |
|--------|---------------|-------|
| `Page` | Trang gắn URL/Router | `RoomPage`, `OrderPage` |
| `Card` | Ô thông tin nhỏ trong danh sách | `RoomCard`, `ProductCard` |
| `Panel` | Vùng nội dung lớn trên trang | `SessionDetailPanel` |
| `Modal` | Hộp thoại bật lên | `ExtendTimeModal` |
| `Form` | Vùng nhập liệu | `OrderForm`, `AddClientForm` |
| `Table` | Bảng dữ liệu | `RoomListTable` |

### Tiền tố thuộc tính Boundary (Thiết kế — khớp cnpm)

Boundary class trong pha **thiết kế** dùng tiền tố chuẩn sau (khớp với `cnpm/references/iii.3.2_sodo_lop_thietke.md`):

**JFrame:**

| Tiền tố | Kiểu VP | Ví dụ |
|---------|---------|-------|
| `txt` | JTextField | `txtUsername`, `txtRoomName` |
| `btn` | JButton | `btnLogin`, `btnSearch` |
| `tbl` | JTable | `tblResults` |
| `lbl` | JLabel | `lblMessage` |

**React:**

| Tiền tố | Kiểu | Ví dụ |
|---------|------|-------|
| `txt` | TextBox | `txtUsername`, `txtRoomName` |
| `btn` | Button | `btnLogin`, `btnSearch` |
| `tbl` | Table | `tblActiveRooms` |
| `lbl` | Label | `lblRoomName` |

### Tiền tố thuộc tính Boundary (Phân tích — khớp mẫu image_08)

Boundary class pha **phân tích** dùng tiền tố **camelCase tiếng Anh, KHÔNG kiểu dữ liệu, KHÔNG dấu gạch dưới** (xác nhận từ `exports/services/screenshots/image_08.png`):

| Tiền tố | Ý nghĩa | Ví dụ từ mẫu |
|---------|---------|--------------|
| `in` | Ô nhập liệu | `-inUsername`, `-inPassword`, `-inRoomName`, `-inProductName` |
| `out` | Chỉ hiển thị | `-outRoomName`, `-outProductList`, `-outSuccess` |
| `sub` | Nút hành động | `-subLogin`, `-subSearchRoom`, `-subCreateOrder`, `-subAdd`, `-subSave`, `-subConfirm` |
| `outsub` | Bảng/danh sách click được | `-outsubRoomList` |

- Giáo trình (tr.76–78) còn có `inout` (vừa nhập vừa hiển thị, `-inoutDSNganh`) và nút `-subQuaylai` trên mỗi màn hình con — không có trong image_08, chỉ dùng khi đề/mẫu yêu cầu.
- Boundary phân tích **chỉ có attributes, KHÔNG có method**.
- Entity phân tích: attributes `-` (không kiểu) **VÀ** method `+methodName()` (có `()`, không tham số): `+checkLogin()`, `+searchActiveRoom()`, `+addOrder()`. Gọi `addOperation(..., visibility="public")`.

---

## Render: màu sắc tự động (khớp biểu đồ mẫu)

VP MCP **tự tô màu xanh `#7AD2FF`** cho actor / use case / lifeline / activation bar (biểu đồ UC + tuần tự) — không cần gọi tool tô màu. Hộp lớp (class) và bảng (ERD) giữ **trắng** mặc định. Các loại khác (state, activity, component…) giữ mặc định của VP CE (xanh nhạt/cam nhạt của VP là chấp nhận được); màu không mang ý nghĩa, chỉ cần nhất quán trong một diagram. Đây là quy ước render khớp với biểu đồ mẫu của môn học và theme PlantUML của skill `cnpm`.

## Danh sách MCP Tools (121 tools)

Tên, tham số theo thứ tự và công dụng từng tool: [`references/vp-mcp-tools.md`](references/vp-mcp-tools.md). Nhóm: Project (5) · Mọi diagram (12: `listDiagrams`, `getDiagramElements`, `getDiagramGeometry`, `getElementCounts`, `autoLayoutDiagram`, `removeDiagramElement`, `addNote`, `setElementBounds`, `rerouteConnectors`, `layoutConnectorLabels`, `renameElement`, `exportDiagramImage`) · Use Case (6) · Class (23) · ERD (11) · Sequence (7) · State (5) · Activity (7) · Communication (5) · Component (8) · Deployment (7) · Package/Object (8) · Flowchart/DFD (8) · BPMN (9).

**Quy ước gọi:** MCP gọi theo TÊN tham số và schema coi MỌI tham số là bắt buộc → tham số không dùng truyền `""` / `0` / `false` (x, y = 0 → tool tự đặt). Tool trả về CHUỖI: lỗi và từ chối cũng là chuỗi (`Error …`, `… not found`, `… already exists`) — luôn đọc kết quả. Tên là handle (action, state, shape, event, lifeline…) phải unique trên diagram. Ví dụ bên dưới viết dạng positional cho gọn; `d` = tên diagram.

### Chọn loại biểu đồ (theo giáo trình BG CNPM 2020 + lab PTTK)

- **Dùng:** use case (tổng quan có khung hệ thống + chi tiết từng module), class (thực thể, BCE phân tích hộp trơn, thiết kế), sequence, ERD (Hình 4.2).
- **Communication:** phân tích, vẽ TRƯỚC từ kịch bản v2 rồi đổi thành sequence. **State:** "biểu đồ trạng thái của module" = luồng màn hình; vòng đời Order là UML hợp lệ (mục 6.8) nhưng KHÔNG phải state của module. **Activity:** thiết kế "Xử lí tại gd/do" (sách), swimlane theo vai trò (lab PTTK). **Package:** view/dao/model (Hình 4.15), khung View/Controller/DAO/Model (PTTK). **DFD:** chỉ lab PTTK (Gane-Sarson).
- **Component** (chỉ ký hiệu Bảng 1.8; mẫu A06 3 tầng) và **Deployment** (tr.113 chỉ mô tả bước; mẫu "MVC trên J2EE"): có nguồn nhưng không có ví dụ trong sách.
- **Object** (không nguồn nào có ký hiệu/ví dụ → UML chuẩn), **Flowchart**, **BPMN** (không dùng; activity thay vai trò flowchart): chỉ vẽ khi user yêu cầu.
- Nhãn trong ví dụ các mục dưới (`Bat dau`, `Hien thi GD…`, `goi`) viết theo giáo trình để dễ đối chiếu; theo quy tắc 4, mặc định dùng tiếng Anh tương ứng (`Start`/`End`, `Show main screen`, `call`/`return`/`display`) — chỉ giữ tiếng Việt không dấu khi user chọn profile giáo trình.

---

## Quy trình tạo diagram theo loại

### Use Case Diagram

```
0. listDiagrams("UseCase") → xác nhận tên diagram chưa tồn tại (unique; tool từ chối tên trùng/rỗng)
1. createUseCaseDiagram(diagramName)
2. addActor(actorName, diagramName, x, y)      — cho mỗi actor (x=y=0 → cột trái; actor cha trừu tượng đặt x/y phía trên các actor con)
3. addUseCase(useCaseName, diagramName, x, y)  — cho mỗi UC (bao gồm UC con generalization), cách nhau 60px
4. addRelationship(diagramName, source, target, type)   — Association (actor–UC), Include, Extend, Generalization
5. getDiagramGeometry(diagramName)             — kiểm Luật bố cục (đường chỉ ngang/dọc, không chồng/đè); vi phạm thì autoLayoutDiagram (Nguyên tắc 4–5)
6. addSystemBoundary(diagramName, systemName)  — SAU khi UC đã vào chỗ cuối; bao UC trong hộp module (tên module, VD "Dịch vụ và kho hàng"); actor nằm ngoài; gọi lại = đổi tên/co giãn khung
7. generateUseCaseReport(diagramName)          — kiểm tra element counts
```

> Biểu đồ UC tổng quan của mẫu (image_02) có **khung hệ thống** bao quanh toàn bộ use case, gắn nhãn tên module, với actor ở ngoài hai bên. `addSystemBoundary` tạo đúng khung này — gọi **sau** khi UC đã được đặt/dàn xong để khung ôm trọn UC.

**Chiều của relationship (cái gì là source/target):**
- **Association** (actor ↔ UC): đường liền, KHÔNG mũi tên. Mọi actor phải nối tới ít nhất 1 UC.
- **Include:** source = UC chính, target = UC được include (mũi tên đứt chạm UC được include, nhãn «include»).
- **Extend:** source = UC mở rộng (tuỳ chọn), target = UC chính (mũi tên đứt chạm UC chính, nhãn «extend»; ngăn "extension points" đã được ẩn).
- **Generalization:** source = con, target = cha (tam giác rỗng ở cha) — dùng cho cả actor lẫn UC.
- Cặp đã có quan hệ cùng loại thì bị báo trùng, không vẽ lại. Actor/UC trùng tên đã có trong project = CÙNG phần tử (view mới).

**Thứ tự thêm relationships:** Include → Extend → Generalization (rồi Association actor–UC).

**Quy tắc ký hiệu giáo trình phải giữ (tr.62–67, Hình 3.1–3.4):**
- Diagram chi tiết module: UC chính + **mỗi màn hình actor dùng = 1 UC con** (không phải nút bấm); màn hình bắt buộc → «include», màn hình xem sâu tuỳ chọn → **chuỗi «extend»** (mỗi UC extend UC liền trước).
- Có UC đăng nhập riêng cho actor ("SV dang nhap") là con (Generalization) của "Dang nhap", và UC chính «include» nó; actor cụ thể là con của actor cha ("Thanh vien") — actor cha vẽ phía trên.
- Tên UC = **cụm động từ hành động của actor** (không phải danh từ, không phải hành động của hệ thống); mọi UC phải với tới được từ một actor (UC mồ côi là lỗi).
- Soi ảnh: nhãn «extend» có hiện không, có mũi tên thừa trên đường actor–UC không, include/extend có đúng chiều không.

**Layout:** UC chính ở giữa, UC include tỏa phải, UC extend tỏa dưới phải, UC generalization tỏa dưới. Tránh xếp dọc — luôn dàn ngang. (Layout ELK tự xếp: actor là một cột bên trái, UC trong boundary theo tầng của include/extend. Mọi đường đều ngang/dọc, kể cả đường actor–UC. Chỉ ghim bằng `x`/`y` khi thật cần.)

**Ví dụ: Module Quản lý Khách hàng**
```
createUseCaseDiagram("UC - QuanLyKhachHang")
addActor("NhanVien", "UC - QuanLyKhachHang", 0, 0)
addUseCase("Tim kiem khach hang", "UC - QuanLyKhachHang", 0, 0)
addUseCase("Them moi khach hang", "UC - QuanLyKhachHang", 0, 0)
addUseCase("Xac minh CCCD", "UC - QuanLyKhachHang", 0, 0)
addUseCase("Tim theo ten", "UC - QuanLyKhachHang", 0, 0)
addUseCase("Tim theo ma", "UC - QuanLyKhachHang", 0, 0)
addRelationship("UC - QuanLyKhachHang", "NhanVien", "Tim kiem khach hang", "Association")
addRelationship("UC - QuanLyKhachHang", "Tim kiem khach hang", "Xac minh CCCD", "Include")
addRelationship("UC - QuanLyKhachHang", "Tim theo ten", "Tim kiem khach hang", "Generalization")
addRelationship("UC - QuanLyKhachHang", "Tim theo ma", "Tim kiem khach hang", "Generalization")
getDiagramGeometry("UC - QuanLyKhachHang")
addSystemBoundary("UC - QuanLyKhachHang", "Quan ly khach hang")
```

### Class Diagram

**Quy tắc BCE (BẮT BUỘC):** Class diagram PHẢI phân rõ 3 nhóm class:
- **Boundary** (hàng trên): Giao diện — JFrame (Swing) hoặc Component (React)
  - **JFrame:** tên class = `[EnglishName]Frm`
  - **React:** tên class = tiếng Anh + hậu tố (`Page`, `Card`, `Panel`, `Modal`, `Form`, `Table`) — xem bảng ở mục "Chọn công nghệ giao diện"
- **DAO/Control** (hàng giữa): Abstract DAO + DAO con kế thừa
- **Entity** (hàng dưới): Lớp thực thể từ phân tích

**Auto-placement theo tên** (khi không truyền x/y): tên kết thúc `View`/`Form`/`Screen` hoặc bắt đầu `Frm`/`Page` → hàng trên; kết thúc `DAO`/`Repository`/`Mapper` → hàng giữa; **còn lại — kể cả `XxxFrm`, `XxxPage`, `XxxController` — rơi xuống hàng dưới cùng với Entity**. Vì vậy với Boundary kiểu `Frm`/`Page` và `Controller` hãy truyền `x`,`y` (hoặc `setElementBounds`). Mỗi hàng tối đa khoảng 3 lớp rồi xuống dòng; hộp tự fit khi thêm member và đẩy các hộp lân cận ra.

**Mẫu Abstract DAO (Pha Thiết kế — BẮT BUỘC):**
Class diagram thiết kế PHẢI có class AbstractDAO (hộp trắng, đúng quy tắc 2–3: không package màu, không stereotype):
```
1. addClass(d, "AbstractDAO", isAbstract=true, x=…, y=…)
2. addAttribute("AbstractDAO", "conn", "Connection", "#", d)          // protected
3. addOperation("AbstractDAO", "AbstractDAO", "void", "", "public", false, d)  // constructor
4. addClass(d, "BookDAO", extendsClass="AbstractDAO", x=…, y=…)       // cha PHẢI đã có trên diagram; hoặc addGeneralization(d, "BookDAO", "AbstractDAO")
```

**Package/màu:** theo quy tắc 2, KHÔNG dùng package màu (`packageName`/`packageColor`/`addPackage`/`setClassColor`) trừ khi user yêu cầu tường minh. Khi cần khung layer thật (biến thể PTTK bên dưới) dùng `addPackageShape` + `moveIntoPackage`.

**Thứ tự tạo class diagram:**
```
0. listDiagrams("Class") → xác nhận tên diagram chưa tồn tại (unique)
   ⚠️  addAttribute/addOperation tra class theo TOÀN PROJECT — nếu tên class trùng giữa
   các module/diagram sẽ thêm nhầm. Đặt tên class UNIQUE toàn project (vd thêm module
   prefix: "BorrowBook_Reader") hoặc hoàn thành diagram này trước khi tạo diagram khác.
   Truyền thêm `diagramName` cho addAttribute/addOperation để chỉ dùng class hiện trên diagram đó.
1. createClassDiagram(diagramName)
2. addClass — Boundary classes (mỗi giao diện = 1 class), có x/y
3. addClass — Abstract DAO class
4. addClass — DAO classes (extendsClass="AbstractDAO")
5. addClass — Entity classes (từ phân tích thực thể — khớp 1:1 với II.2)
6. addAttribute — cho mỗi class (Boundary: UI components; Entity: private fields)
7. addOperation — cho mỗi class (Boundary: actionPerformed; DAO: CRUD methods), params = "name: Type, …"
8. addRelationships — theo thứ tự (sau khi thêm ĐỦ classes):
   a. addGeneralization — DAO extends Abstract DAO
   b. addComposition — Entity lifetime-dependent (ReaderCard◆Reader, SlipDetail◆BorrowSlip)
   c. addAggregation — Entity independent (BookTitle◇SlipDetail)
   d. addDependency — Boundary --> DAO
   e. addAssociation — Entity ↔ Entity (structural links)
9. getDiagramGeometry(diagramName) → kiểm tra hàng/cột, không hộp chồng nhau; setElementBounds chỉnh; rerouteConnectors; layoutConnectorLabels
10. getRelationshipDetails(diagramName) → JSON audit (thuộc tính, phương thức, multiplicity, chiều quan hệ)
```

**Bảng hướng dẫn chọn relationship (chiều: from → to):**

| Quan hệ | Ký hiệu | Tool (chiều) | Khi nào dùng |
|---------|---------|--------------|---------------|
| Generalization | Tam giác rỗng ở CHA | `addGeneralization(from=con, to=cha)` | DAO kế thừa AbstractDAO; UC con kế thừa UC cha |
| Composition (◆) | Hình thoi đặc ở TOÀN THỂ | `addComposition(from=toàn thể, to=bộ phận, fromMult, toMult)` | Lifetime dependent — ReaderCard-Reader, SlipDetail-BorrowSlip |
| Aggregation (◇) | Hình thoi rỗng ở TOÀN THỂ | `addAggregation(from=toàn thể, to=bộ phận, …)` | Independent, shared — BookTitle-SlipDetail |
| Association | Đường liền | `addAssociation(from, to, fromMult, toMult, name)` | General structural link giữa entities |
| Dependency | Đường chấm, mũi tên mở | `addDependency(from=phụ thuộc, to=được dùng)` | Boundary "sử dụng" DAO |
| Realization | Đường chấm, tam giác rỗng ở interface | `addRealization(from=cài đặt, to=interface)` | `XxxDAOImpl` implements `XxxDAO` |
| Usage `<<use>>` | Đường chấm + nhãn «use» | `addUsage(from, to)` (lớp hoặc package) | Biến thể PTTK |

Multiplicity hợp lệ: số, `*`, `n`, `m`, hoặc khoảng `0..1`, `1..*`, `2..n` (sai thì tool từ chối). Chỉnh sau khi vẽ: `setAssociationProperties` (tên, multiplicity, role — `-` xoá role, navigable true/false/unspecified), `removeRelationship`. Soi ảnh theo **mũi tên/hình thoi thật**, không theo thứ tự tham số.

**Biến thể thiết kế PTTK (chỉ khi user chọn, thay AbstractDAO bằng interface + Impl):** 4 bước, mỗi bước 1 diagram — B1 thêm get/set/update/delete có kiểu; B2 association → `addUsage` «use» khi A có method nhận B; B3 `addInterface("XxxDAO")` + `addClass("XxxDAOImpl")` + `addRealization(from=Impl, to=Interface)`, entity chỉ còn `getId/setId`; B4 `addPackageShape` View/Controller/DAO/Model (Model có sub-package) + `moveIntoPackage`, tên `XxxView`/`XxxController`, «use» chỉ chỉ xuống từng tầng một. Data model PTTK (lớp `<<ORM Persistable>>`, multiplicity hai đầu, quan hệ đặt tên bằng động từ, kế thừa → association "is a"): `addStereotypeToClasses(d, "*", "ORM Persistable")` (+ `robustnessIcon="false"` để B/C/E giữ hộp), `setAssociationProperties(role "-")` để xoá role tự sinh.

**Ví dụ: Biểu đồ lớp Module Mượn Sách (JFrame) — hộp trắng** (dạng giả: `name=value` là tham số có tên, bỏ qua = `""`/`0`/`false`; `D` = `"Class - BorrowBook"`)
```
createClassDiagram(D)
addClass(D, "BorrowBookFrm", x=60, y=40)              // Boundary: tên XxxFrm không tự lên hàng trên → truyền x,y
addAttribute("BorrowBookFrm", "txtReaderId", "JTextField", "private", D)   // + btnSearch: JButton, tblResults: JTable
addOperation("BorrowBookFrm", "actionPerformed", "void", "e: ActionEvent", "public", false, D)
addClass(D, "AbstractDAO", isAbstract=true)
addAttribute("AbstractDAO", "conn", "Connection", "#", D)
addOperation("AbstractDAO", "AbstractDAO", "void", "", "public", false, D)
addClass(D, "ReaderDAO", extendsClass="AbstractDAO")   // + BorrowSlipDAO
addOperation("ReaderDAO", "findById", "Reader", "id: String", "public", false, D)
addClass(D, "Reader")                                  // + ReaderCard, BorrowSlip, BorrowSlipDetail, BookTitle
addAttribute("Reader", "id", "String", "private", D)   // + name, borrowDate…
addComposition(D, "Reader", "ReaderCard", "1", "1")    // from = toàn thể
addComposition(D, "Reader", "BorrowSlip", "1", "n")
addComposition(D, "BorrowSlip", "BorrowSlipDetail", "1", "n")
addAggregation(D, "BookTitle", "BorrowSlipDetail", "1", "n")
addDependency(D, "BorrowBookFrm", "ReaderDAO")         // + BorrowSlipDAO
getDiagramGeometry(D)
```

### ERD

**Quy tắc đặt tên ERD (BẮT BUỘC):**

| Quy tắc | Mẫu | Ví dụ |
|---------|-----|-------|
| Tên bảng | `tbl` + TênEntity | `tblSach`, `tblNhanVien` |
| Cột PK | `ma` hoặc `id` | `ma : integer(10) <<PK>>` |
| Cột FK | `tbl` + TênBangCha + `ma` | `tblNhanVienma : integer(10) <<FK>>` |
| Quan hệ FK | Parent `1` to Child `n` | `tblNhanVien \|\|--o{ tblSach` |

**Ánh xạ kiểu dữ liệu:**

| Java Type | SQL Type |
|-----------|----------|
| String | varchar(255) |
| int | integer(10) |
| double | double(10) |
| Date | date |

Tên bảng/cột là SQL identifier (chữ, số, `_`; không dấu, không khoảng trắng). Bảng cùng tên trong project là CÙNG bảng (vẽ lại view với các cột đã có). Mỗi hàng 4 bảng.

```
1. createErd(diagramName)
2. addTable(diagramName, tableName)                               — cho mỗi bảng (dùng `tbl` + tên entity)
3. addColumn(diagramName, tableName, columnName, columnType, length, scale, isPrimaryKey, isNullable, isUnique)  — cho mỗi cột (diagramName ĐỨNG ĐẦU)
4. addForeignKey(diagramName, childTable, parentTable, fromColumn, toColumn, fkName)   — cho mỗi FK; fromColumn có sẵn ở bảng con sẽ thành cột FK
5. addTableRelationship(diagramName, parentTable, childTable, type, fromMult, toMult)  — thay cho bước 4 khi cần identifying/multiplicity
6. generateDdl(diagramName)                                        — optional, sinh DDL
```

⚠️ **Hai tool FK ngược chiều nhau:** `addForeignKey(fromTable = bảng CON, toTable = bảng CHA)` còn `addTableRelationship(fromTable = bảng CHA, toTable = bảng CON)`. Cả hai đều sinh quan hệ + cột FK ở bảng con → dùng **một** cho mỗi cặp bảng (cặp đã có quan hệ bị từ chối). `type`: `identifying` (FK nằm trong PK, vd bảng con của kế thừa) | `nonIdentifying` hoặc `""`; multiplicity phía cha `1`/`0..1`, phía con `0..1`/`0..*`/`1`/`1..*`.

**Sửa mà không dựng lại:** `renameColumn`, `removeColumn` (cột FK phải `removeForeignKey` trước; cột FK vẫn còn ở bảng con sau khi gỡ FK), `removeTable` (xoá khỏi project, mọi diagram mất bảng; bảng đang có FK bị từ chối). `removeDiagramElement` chỉ gỡ view.

**Quy tắc giáo trình (tr.94–95):** mỗi entity 1 bảng; n–n tách bằng bảng trung gian; FK nằm ở bảng phía "nhiều" (chân quạ ở đó); không cột dẫn xuất (tổng, trung bình) và không bảng thống kê; PK `id`, FK theo bảng bên trên (VD `tblClientid`); kiểu `integer(10)`, `varchar(255)`, `date`, `float(10)`.

**Ví dụ:**
```
createErd("ERD - ClientManagement")
addTable("ERD - ClientManagement", "tblClient")
addColumn("ERD - ClientManagement", "tblClient", "id", "integer", 10, 0, true, false, false)
addColumn("ERD - ClientManagement", "tblClient", "name", "varchar", 255, 0, false, false, false)
addColumn("ERD - ClientManagement", "tblClient", "idCard", "varchar", 20, 0, false, false, true)
addTable("ERD - ClientManagement", "tblContract")
addColumn("ERD - ClientManagement", "tblContract", "id", "integer", 10, 0, true, false, false)
addColumn("ERD - ClientManagement", "tblContract", "signDate", "date", 0, 0, false, false, false)
addColumn("ERD - ClientManagement", "tblContract", "tblClientid", "integer", 10, 0, false, false, false)
addForeignKey("ERD - ClientManagement", "tblContract", "tblClient", "tblClientid", "id", "FK_Client_Contract")
generateDdl("ERD - ClientManagement")
```

### Sequence Diagram

**Thứ tự participant (BẮT BUỘC):**
```
Actor → [TênView] (Boundary) → [EntityController] (Control) → [Entity] (Entity)
```

**Alias lifeline: ĐỂ TRỐNG (`alias=""`) — BẮT BUỘC:**

KHÔNG đặt alias kiểu `B0`/`E1`. Lý do:
1. **Nhãn lifeline = `lifelineName` = tên class** (`LoginView`, `Employee`) → khớp biểu đồ mẫu (mẫu hiển thị tên class, KHÔNG hiển thị `B0`).
2. **Tránh lỗi mất mũi tên:** khi đặt alias, VP `getName()` trả về alias; nếu `addMessage` tham chiếu lifeline bằng `lifelineName` (cách tự nhiên) sẽ **không tìm thấy lifeline → biểu đồ rỗng mũi tên**. (Plugin đã vá lookup đa-trường, nhưng để trống alias là an toàn nhất + nhãn đúng mẫu.)

→ Gọi `addLifeline(..., alias="")` và trong mọi `addMessage`/`addReturnMessage` tham chiếu lifeline bằng **đúng `lifelineName`** (VD `"LoginView"`, `"Employee"`).

**Lifeline type (BẮT BUỘC):**
Mỗi lifeline PHẢI có `lifelineType` = `actor`/`boundary`/`control`/`entity` (KHÔNG dùng `participant`) để VP hiển thị icon đúng:
- `actor` — **hộp** (giới hạn đã chứng minh: lifeline tạo bằng API không vẽ được hình que, vì hình que không neo được message; user tự đổi tay nếu cần)
- `boundary` — circle + line
- `control` — arrow
- `entity` — circle on base line

**`lifelineType` KHÔNG đổi được sau khi đã có message** (không có tool) → sai kiểu thì tạo lại diagram.

**Số thứ tự thông điệp (BẮT BUỘC):**
Tất cả messages PHẢI được đánh số tuần tự:
- Dùng tham số `sequenceNumber` trên `addMessage` và `addReturnMessage` (`""` = số cấp 1 kế tiếp)
- Bắt đầu từ `1`, tăng dần cho mỗi message
- Return message dùng số thứ tự **tiếp theo** (số đã dùng bị tool từ chối — không dùng lại số của call)
- Combined fragment: message bên trong tiếp tục đánh số
- KHÔNG gõ `N:` trong nhãn (VP tự in số trước nhãn → nếu gõ sẽ thành `1: 1: call`)

Ví dụ: 1, 2, 3, 4, 5, 6 — nếu dùng opt/loop (luồng chính): sub-message = 5.1, 5.2 (không dùng alt)

**Ngôn ngữ theo pha (khớp cnpm #8):**
- **Arrow label trong VP (addMessage/addReturnMessage):** TOÀN BỘ tiếng Anh trong cả 2 pha (`enter keyword + click Search`, `checkLogin()`, `display results`, `List<Room>`).
- **Phân tích:** Dùng từ khoá: `click btnX` (Actor→Boundary), `call` (Boundary/Control kích hoạt lớp kế), `return` (phản hồi), `display` (Boundary→Actor hiển thị).
- **`methodName()` là SELF-MESSAGE trên Entity (khớp mẫu image_12):** Khi Boundary/Control gọi nghiệp vụ của Entity, vẽ **3 bước**:
  1. Boundary/Control → Entity: `call`
  2. Entity → **chính Entity** (self): `methodName()` — VD `checkLogin()`, `searchActiveRoom()`, `addOrder()`
  3. Entity → Boundary/Control: `return`

  Trong VP MCP: bước 2 gọi `addMessage(diagram, "Entity", "Entity", "methodName()", n, "sync")` (from == to → VP vẽ mũi tên tự gọi).
- **Tương tác Actor↔Actor:** mẫu có `ask X` / `reply X` giữa hai actor (VD Service Staff hỏi Client) — dùng câu tiếng Anh ngắn.
- **Thiết kế:** `methodName()` self-message mang tham số + kiểu (`searchRoomByName(roomName: String): List<Room>`); event Boundary self-call `btnSearchRoomClick()` / `actionPerformed(e: ActionEvent)`.
- **Tên method luôn tiếng Anh** mọi pha (checkLogin, searchProduct, addOrder...).
- **Kịch bản text (v2/v3 bên ngoài biểu đồ):** Giữ tiếng Việt.

**Diễn giải tuần tự (BẮT BUỘC alongside diagram):**

Bên cạnh biểu đồ sequence diagram, PHẢI viết thêm block diễn giải tuần tự dưới dạng danh sách đánh số:
- **Phân tích → Kịch bản phiên bản 2:** Danh sách bước bằng tiếng Việt tự nhiên, mô tả Actor ↔ Boundary ↔ Entity. Xem `cnpm/references/ii.4_tuantu_phantich.md` để biết format chi tiết.
- **Thiết kế → Kịch bản phiên bản 3:** Danh sách bước có tên hàm Java + kiểu dữ liệu, mô tả Actor ↔ Boundary ↔ Control ↔ Entity. Xem `cnpm/references/iii.4_tuantu_thietke.md` để biết format chi tiết.

Block diễn giải giúp người đọc hiểu luồng xử lý mà không cần đọc biểu đồ UML. Luôn đặt ngay sau biểu đồ, trong callout `📖` màu green.

```
0. listDiagrams("Sequence") → xác nhận tên diagram chưa tồn tại (unique)
1. createSequenceDiagram(diagramName)
2. addLifeline(diagramName, lifelineName, className, lifelineType, alias="") — theo thứ tự: Actor, Boundary, [Control], DAO, Entity
3. addActivation — tuỳ chọn (message tự tạo thanh kích hoạt, tool gộp thành thanh liền mỗi lifeline)
4. addMessage — sync message (thứ tự tăng dần, tiếng Anh). Gọi nghiệp vụ Entity = 3 bước: `call` → `methodName()` self-message (from==to là Entity) → `return`
5. addReturnMessage — return / display (mỗi `call` cần 1 `return`)
6. addCombinedFragment — CHỈ khi cần loop/opt (xem dưới); thêm SAU các message nó bao
7. getDiagramElements(diagramName) → xác nhận participants đúng thứ tự, message count đúng
   (autoLayoutDiagram là no-op trên sequence — không cần gọi; muốn dời lifeline dùng setElementBounds, message đi theo)
```

**Lưu ý Combined Fragment (khớp cnpm #10):**
Biểu đồ sequence **chỉ vẽ luồng chính** — không dùng `alt` để mô tả ngoại lệ. Ngoại lệ → viết block text "Ngoại lệ" sau biểu đồ.
Tool `addCombinedFragment(diagramName, operator, guard, coveredLifelines, fromSeq, toSeq, operandStarts)` vẫn sẵn có (operators: `alt`, `opt`, `loop`, `break`, `par`) — chỉ dùng khi user yêu cầu tường minh hoặc cần `loop`/`opt` cho luồng chính. Khung bao các message có số cấp 1 từ `fromSeq` đến `toSeq` (gồm 4.1, 4.2…).
- `opt` = bước tùy chọn trong luồng chính
- `loop` = lặp lại trong luồng chính (giáo trình chỉ dùng `loop`, guard dạng `[lap den khi het mon dang ki]`)

**Ví dụ: Sequence Diagram "Tạo order" (Phân tích)**
```
createSequenceDiagram("SD - TaoOrder_PhanTich")
// alias="" → nhãn lifeline = lifelineName (khớp mẫu); tham chiếu lifeline bằng lifelineName
addLifeline("SD - TaoOrder_PhanTich", "Actor", "ServiceStaff", "actor", "")
addLifeline("SD - TaoOrder_PhanTich", "LoginView", "LoginView", "boundary", "")
addLifeline("SD - TaoOrder_PhanTich", "SearchRoomView", "SearchRoomView", "boundary", "")
addLifeline("SD - TaoOrder_PhanTich", "Employee", "Employee", "entity", "")
addLifeline("SD - TaoOrder_PhanTich", "Room", "Room", "entity", "")
addActivation("SD - TaoOrder_PhanTich", "LoginView")
// --- Đăng nhập: Boundary call Entity → Entity self-method() → return ---
addMessage("SD - TaoOrder_PhanTich", "Actor", "LoginView", "Login", "1", "sync")
addMessage("SD - TaoOrder_PhanTich", "LoginView", "Employee", "call", "2", "sync")
addMessage("SD - TaoOrder_PhanTich", "Employee", "Employee", "checkLogin()", "3", "sync")   // self-message
addReturnMessage("SD - TaoOrder_PhanTich", "Employee", "LoginView", "return", "4")
addMessage("SD - TaoOrder_PhanTich", "LoginView", "SearchRoomView", "call", "5", "sync")
addReturnMessage("SD - TaoOrder_PhanTich", "SearchRoomView", "Actor", "display", "6")
// --- Tìm phòng: cùng mẫu call → searchActiveRoom() self → return → display ---
addMessage("SD - TaoOrder_PhanTich", "Actor", "SearchRoomView", "enter room name and click search", "7", "sync")
addMessage("SD - TaoOrder_PhanTich", "SearchRoomView", "Room", "call", "8", "sync")
addMessage("SD - TaoOrder_PhanTich", "Room", "Room", "searchActiveRoom()", "9", "sync")       // self-message
addReturnMessage("SD - TaoOrder_PhanTich", "Room", "SearchRoomView", "return", "10")
addReturnMessage("SD - TaoOrder_PhanTich", "SearchRoomView", "Actor", "display", "11")
getDiagramElements("SD - TaoOrder_PhanTich")
// Ngoại lệ (text block bên ngoài biểu đồ):
// - searchActiveRoom() trả về rỗng → SearchRoomView hiển thị "No rooms found"
```

Soi ảnh: call nét liền đầu đặc, return nét đứt đầu hở; không mũi tên nào lơ lửng/dạt về x=0; luồng nào cũng kết thúc bằng `display` về Actor; không số bị nhân đôi (`1: 1:`); `create` hạ đầu lifeline xuống mũi tên; nhãn rộng hơn mũi tên sẽ đẩy lifeline bên phải ra.

### State Machine Diagram

Giáo trình: **"biểu đồ trạng thái của module" = LUỒNG MÀN HÌNH** (Hình 3.9/3.11/3.13): state = `Hien thi GD xxx`, transition = thao tác của user dạng guard (`[chon chuc nang dang ki]`, `[chon quay lai]`), initial `Bat dau`, final `Ket thuc`, bố cục trên → dưới, transition "quay lại" chạy ngược lên song song với transition tiến. Vòng đời đối tượng (Order: Pending → Approved → …, mục 6.8 tài liệu) là UML hợp lệ nhưng **SAI khi đề hỏi state của module**.

```
1. createStateDiagram(d)
2. addInitialState(d, "Bat dau", x, y)     — VP LUÔN in tên dưới hình tròn, không giấu được → đặt tên đẹp ("Bat dau"/"Start")
3. addState(d, stateName, entryAction, doActivity, exitAction, x, y)   — entry/do/exit chỉ cho vòng đời; luồng màn hình để ""
4. addFinalState(d, "Ket thuc", x, y)
5. addTransition(d, fromState, toState, label)   — label = `event [guard] / effect`; fromState==toState = self-loop
```
- Đúng 1 initial, ≥ 1 final, mọi state tới được, mọi transition có nhãn; tên state là handle (unique).
- **Nhãn dài đè lên hộp:** truyền x/y để state cách nhau ~300px thay vì dựa auto-placement (lưới 3 cột, state mới nhảy xuống dưới nguồn của transition đến).
- Không hỗ trợ composite state, choice, history, internal transition → dùng state phẳng.

### Activity Diagram

Hai biến thể — chọn theo profile (hỏi user/đề):
- **Sách — thiết kế "Xử lí tại gdXxx.jsp / doXxx.jsp"** (Hình 4.9/4.11/4.13): khung bo tròn theo trang; mỗi action = **một phương thức đã thiết kế**; mỗi lần gọi DAO là hộp `XxxDAO: method()` **ngoài khung**, nối action bằng **mũi tên hai đầu**; rẽ nhánh = **guard trên cạnh rời action**, KHÔNG diamond/swimlane.
- **Lab PTTK — swimlane theo vai trò:** diamond có câu hỏi + guard Yes/No (hoặc `[else]`), fork/join cân, nhiều final được.

```
Sách:
1. createActivityDiagram(d); addActivityControlNode(d, "initial", "Bat dau", "", x, y)
2. addActivityAction(d, "Nhan thong tin SV", "", x, y)        — tên unique (là handle); hộp DAO: addActivityAction(d, "SinhvienDAO: getNganh()", "", x, y)
3. addActivityFlow(d, from, to, guard, twoWay)               — action ↔ hộp DAO: twoWay=true; nhánh: guard "click dang ki"
4. addActivityControlNode(d, "final", "Ket thuc", "", x, y)
5. addActivityFrame(d, "Xu li tai gdDangki.jsp", "nodeA,nodeB,…", 0,0,0,0)   — SAU khi node + flow xong; không đưa hộp DAO vào nodeNames

PTTK:
1. createActivityDiagram(d)
2. addActivityPartition(d, "Customer", …) rồi "System", …    — lane xếp ngang theo thứ tự thêm; thêm lane TRƯỚC node
3. addActivityControlNode(d, kind, nodeName, partitionName, x, y)   — initial | final | flowFinal | decision | merge | fork | join
4. addActivityAction(d, name, partitionName, x, y); addActivityObjectNode(d, "Order", "created", partitionName, x, y)   — hiện [created]
5. addActivityFlow(d, from, to, guard, false)                — flow tới/từ object node tự thành object flow
```
- Đúng 1 initial, ≥ 1 final; mọi action có vào/ra; **mọi cạnh rời decision có guard**; fork/join cân; node nằm trọn trong 1 lane/khung; không flow đứt giữa chừng. Lane = vai trò (không phải màn hình), bước nội bộ hệ thống không nằm lane actor; hộp DAO phải có trong class diagram thiết kế.
- Không hỗ trợ send-signal/accept-event action, pin. Guard trong layout explicit chật có thể chạm đường (tool in WARNING).

### Communication Diagram

Giáo trình (phân tích, Hình 3.10/3.12/3.14): vẽ **TRƯỚC** từ kịch bản v2, sau đó đổi thành sequence; object + link = đúng các lớp + quan hệ của class diagram phân tích; **KHÔNG DAO, KHÔNG control**. Actor (hình người) giữa trên, hàng boundary nối chuỗi bằng link, entity hàng dưới ngay dưới boundary dùng nó.

```
1. createCommunicationDiagram(d)
2. addCommunicationLifeline(d, "ServiceStaff", "", true, x, y, "")          — actor hình người
   addCommunicationLifeline(d, "LoginView", "", false, x, y, "boundary")    — icon boundary (GDxxx của sách); entity: lifelineType "entity"
   (đối tượng ẩn danh `:Room` = lifelineName "" + classifierName "Room")
3. addCommunicationLink(d, a, b)                                           — MỘT link/cặp, KHÔNG mũi tên; cùng tên 2 đầu = self link
4. addCommunicationMessage(d, from, to, sequenceNumber, messageText)        — số TRƯỚC, nội dung SAU (ngược addMessage của sequence)
   · "" = số cấp 1 kế tiếp; không gõ "N:" trong nhãn; hỗ trợ "1.2", "2a", "1.1*"
   · entity method = self: addCommunicationMessage(d, "Room", "Room", "4", "searchActiveRoom()")
   · hai chiều trên CÙNG link = hai mũi tên cạnh nhau, đừng tạo link thứ hai
5. moveCommunicationLifeline(d, name, x, y)                                — chỉ khi cần ghim lifeline theo bố cục sách (layout ELK tự xếp; link luôn ngang/dọc)
```
- Soi: link không mũi tên, mũi tên message nằm cạnh link, số liên tục và khớp kịch bản v2, nhãn không đè nhau, mọi object có trong class diagram phân tích. Từ khoá nhãn: `click btnX`, `call`, `return`, `display`.

### Component Diagram

Giáo trình chỉ nêu ký hiệu (Bảng 1.8); mẫu A06: **khung layer** ("Presentation Layer", "Application Layer", "Data Layer") chứa component, dependency `<<use>>` nét đứt **chỉ chỉ xuống một tầng** (không Presentation → Data).

```
1. createComponentDiagram(d)
2. addComponentPackage(d, "Presentation Layer", "", x, y, width, height); addComponentPackage(d, "Application Layer", …)   — mỗi tầng, trên → dưới
3. addComponent(d, "OrderForm", "", "", x, y, "Presentation Layer"); addComponent(d, "OrderService", "", "", x, y, "Application Layer")   — (stereotype "", parentComponent "", packageName = tên khung)
4. addPort(d, "OrderService", "pOrder")                                    — nếu cần
5. addComponentInterface(d, "IOrderService", x, y)                         — hộp <<interface>>, KHÔNG lollipop
   addProvidedInterface(d, "OrderService", "IOrderService")                — realization nét đứt, tam giác rỗng ở interface
   addRequiredInterface(d, "OrderForm", "IOrderService")                   — <<use>> nét đứt
6. addComponentDependency(d, "OrderForm", "OrderService", "use")
```
- `<<component>>` do VP tự in — đừng truyền làm stereotype; không vẽ nội dung lớp bên trong component; `componentName` của provided/required có thể là tên port.

### Deployment Diagram

Mẫu "MVC trên J2EE": «device» Client PC ⊃ Browser «executionEnvironment»; «device» Web Server ⊃ Tomcat ⊃ `app.war` ⊃ View / Controller / Model; «device» DB Server ⊃ MySQL ⊃ database; link `1: HTTP/HTTPS` (client–web), `2: JDBC/TCP 3306` (web–DB).

```
1. createDeploymentDiagram(d)
2. addDeploymentNode(d, "Client PC", "device", "", x, y, w, h); addDeploymentNode(d, "Browser", "executionEnvironment", "Client PC", 0,0,0,0)   — cha trước, con sau (parentNode); tương tự "Web Server" ⊃ "Tomcat", "DB Server" ⊃ "MySQL"
3. addDeploymentArtifact(d, "app.war", "Tomcat", x, y)
4. addDeploymentComponent(d, "View", "app.war", 0, 0); "Controller"; "Model"   — một hàng trong artifact, cách 90px
5. addDeploymentDependency(d, "View", "Controller", "submit")                  — nét đứt; Controller → Model tương tự
6. addCommunicationPath(d, "Client PC", "Web Server", "1: HTTP/HTTPS"); addCommunicationPath(d, "Web Server", "DB Server", "2: JDBC/TCP 3306")
7. addDeployDependency(d, artifact, node)                                      — chỉ cho artifact đứng riêng
```
- Node = hộp 3-D (không vẽ class thành node); mọi link có nhãn giao thức, đánh số theo thời gian; DB không nằm trên client; artifact phải nằm trong node.

### Package Diagram

Sách (Hình 4.15): 3 package xếp **dọc** `view` (trên), `dao`, `model` (dưới), nối bằng **đường liền không mũi tên, không «import»**; `view` chứa 1 sub-package theo actor trên một hàng (`thanhvien`, `sinhvien`, `giangvien`, `quanli`); tên chữ thường. PTTK: khung View/Controller/DAO/Model, «use» chỉ xuống từng tầng, không View → DAO/Model.

```
1. createPackageDiagram(d)
2. addPackageElement(d, "view", "", x, y, width, height); addPackageElement(d, "sinhvien", "view", 0,0,0,0)…   — thêm CON của một package trước package cấp cao kế tiếp (khung tự đặt không chồng)
   addPackageElement(d, "dao", …); addPackageElement(d, "model", …)
3. addClassInPackage(d, "dao", "SinhvienDAO")               — hộp lớp chỉ tên, lớp thuộc package đó trong model
4. addPackageDependency(d, "view", "dao", "line")           — sách: "line"; PTTK: "use" (còn import | access | merge)
```
- Lỗi hay bị trừ điểm: `view` phẳng (khi theo sách), thiếu tầng, đảo chiều tầng, class sai tầng, phụ thuộc đi lên/nhảy tầng.

### Object Diagram

Không nguồn nào có ký hiệu hay ví dụ → áp UML: ô `obj : Class` gạch chân (`: Class` nếu ẩn danh), slot `thuoctinh = gia tri` (không kiểu, không ngăn operation), link khớp association của class diagram, không multiplicity.
```
1. createObjectDiagram(d)
2. addObject(d, "sv1", "Sinhvien", "ten=Lan;ngaysinh=2000-01-01", x, y, "")   — objectName "" = ẩn danh; attr phải có sẵn trong lớp (hoặc lớp cha); modelPackage chọn lớp khi nhiều package có lớp cùng tên
3. addObjectLink(d, "sv1", "dk1", "dang ki")
```

### Flowchart và DFD

**Flowchart** (không dùng trong giáo trình; chỉ khi user yêu cầu — oval terminator, chữ nhật process, diamond decision có `Yes`/`No`, hình bình hành I/O, trên → dưới):
`createFlowchart(d)` → `addFlowchartShape(d, name, kind, x, y)` (kind: terminator|process|decision|inputOutput|document|predefinedProcess|database|manualInput|connector) → `addFlowchartFlow(d, from, to, label)`.

**DFD (lab PTTK, Gane-Sarson):** external entity = hộp vàng ký hiệu a/b/c, process = hộp bo tròn có số, data store = hộp hở có ô "D", flow = mũi tên nhãn **danh từ**.
```
1. createDataFlowDiagram(d, "ganeSarson")
2. addDfdExternalEntity(d, "Customer", "", x, y)    — entityId "" = tiếp a, b, c
3. addDfdProcess(d, "Place order", "1", x, y)       — processId "" = tiếp số (1.0 → 2.0)
4. addDfdDataStore(d, "Orders", "1", x, y)          — chỉ truyền số hoặc "D1" (VP tự in chữ D)
5. addDfdDataFlow(d, from, to, "order details")     — tham chiếu theo tên hoặc ID
```
- Mọi flow chạm một process (entity↔store, store↔store, entity↔entity bị từ chối); mỗi process ≥ 1 vào + ≥ 1 ra; process = cụm động từ, flow = danh từ; **level 0 (context) đúng 1 process**; ghi mức (0, 1, 2) vào tên diagram.

### BPMN Diagram

Giáo trình không dùng — chỉ khi user yêu cầu (BPMN 2.0: start = vòng mảnh, end = vòng đậm, task bo tròn, gateway thoi X/+, sequence flow liền, message flow đứt giữa các pool).
```
1. createBpmnDiagram(d); addBpmnPool(d, "Customer", x, y, width, height)   — pool hộp đen cao 40–60
2. addBpmnLane(d, pool, lane)                       — thêm HẾT lane của pool TRƯỚC khi đặt phần tử
3. addBpmnEvent(d, "Order received", lane, "start", "", x, y); addBpmnTask(d, "Check stock", lane, "user", x, y)
   addBpmnGateway(d, "In stock?", lane, "exclusive", x, y); addBpmnDataObject(d, "Invoice", lane, x, y)
4. addBpmnSequenceFlow(d, from, to, condition)      — CÙNG pool; nhãn nhánh "Yes"/"[in stock]"; với data object = data association
   addBpmnMessageFlow(d, from, to, label)           — KHÁC pool (start chỉ nhận, end chỉ gửi)
```
- Tên phần tử là handle (unique). Chưa hỗ trợ boundary event, text annotation, call activity, loop marker.

---

## Xuất ảnh và nhúng vào tài liệu

### Cách xuất ảnh từ VP

**Cách 0 — Tự động qua MCP (mặc định):** `exportDiagramImage(diagramName, filePath)` ghi PNG trực tiếp (đường dẫn tuyệt đối, đuôi `.png`). Sau khi xuất, **mở PNG ra xem** (Read) để kiểm tra nhãn, mũi tên, chồng lấn trước khi nhúng. Ảnh xuất từ bản VP evaluation có watermark — đó là chuyện bản quyền, không xử lý trong skill.

Cách thủ công (khi cần chỉnh tay trong VP rồi mới xuất):

**Cách 1 — Export từ VP application:**
1. Mở diagram trong Visual Paradigm
2. Menu: Diagram → Export as Image → PNG/SVG
3. Lưu vào thư mục `docs/images/`
4. Nhúng vào markdown: `![Tên biểu đồ](images/ten-file.png)`

**Cách 2 — VP Command Line (nếu có):**
```bash
# Export diagram as PNG via VP CLI (nếu cài đặt)
vpcmd -export diagram "Diagram Name" -format png -output docs/images/
```

**Cách 3 — Generate Report thay thế:**
Nếu không cần ảnh, dùng `generateXxxReport` để lấy text report nhúng vào tài liệu.

**Chất lượng ảnh:** chân trang "Powered By Visual Paradigm Community Edition" là chấp nhận được; watermark chéo "Enterprise [evaluation copy]" thì KHÔNG (cần bản "copy sạch"). Không hộp bị cắt ở mép ảnh.

### Nhúng ảnh vào tài liệu Notion

Sau khi có file ảnh, dùng Notion API để upload và nhúng:

```markdown
![Biểu đồ lớp – Module KH](images/class-quanlykhachhang.png)
```

Hoặc nếu ảnh đã upload lên hosting khác:
```markdown
![Biểu đồ lớp – Module KH](https://url-to-image.png)
```

---

## Quy trình tổng hợp: cnpm + cnpm-vp

Khi người dùng muốn tài liệu UP với biểu đồ VP:

```
1. Dùng skill cnpm → BƯỚC 0 PLAN (hỏi cả công nghệ giao diện + có dùng VP không)
2. Dùng skill cnpm → sinh nội dung các mục (text + bảng)
3. Dùng skill cnpm-vp → tạo diagram trong VP theo nội dung đã sinh
4. Dùng skill cnpm-vp → export ảnh từ VP
5. Dùng skill notion-format → nhúng ảnh vào tài liệu Notion
```

**Khi nào dùng VP thay vì PlantUML:**
- Diagram phức tạp (nhiều class, nhiều relationship)
- Cần diagram chuyên nghiệp cho báo cáo/presentation
- Người dùng yêu cầu
- Diagram cần chỉnh sửa trực quan (drag & drop)

**Khi nào giữ PlantUML:**
- Diagram đơn giản
- Chỉ cần text-based documentation
- Không có VP MCP server đang chạy
- Người dùng không yêu cầu VP

---

## Kiểm tra cấu trúc sau khi vẽ (Verification)

Sau khi tạo xong diagram, **BẮT BUỘC** chạy verification trước khi export. Mọi loại: `getDiagramElements` (cấu trúc) + `getDiagramGeometry` (bounds lồng nhau, điểm connector, bounds nhãn).

**Soi ảnh/hình học trước tiên (lỗi hay gặp của VP MCP):** nhãn «extend» mất / ngăn "extension points"; mũi tên thừa trên đường actor–UC; mũi tên sequence dạt về x=0; số message nhân đôi (`1: 1:`); đầu connector neo ở góc trên-trái (mở diagram trong VP rồi `rerouteConnectors`); role name tự sinh trên quan hệ ORM; nhãn «use» nằm đè lên hộp; connector xuyên qua hộp thứ ba; hộp chồng nhau hoặc bị cắt ở mép; tên mặc định (`Class`, `UseCase`, `Lifeline`, `State`). Chiều quan hệ VP lưu có thể ngược tên tham số (Generalization lưu cha→con, Realization interface→impl): luôn kiểm bằng **mũi tên trong ảnh**.

### Class Diagram verification
```
1. getDiagramElements(diagramName) → kiểm tra cấu trúc:
   - Có đủ 3 nhóm: Boundary, DAO (thiết kế), Entity classes
   - Phân tích BCE: Mỗi Boundary class có attributes với prefix in/out/sub/outsub
     (VD: -inKeyword, -outClientList, -subSearch) — KHÔNG dùng txt/btn ở pha phân tích
   - Thiết kế JFrame: attributes = JTextField/JButton/JTable
   - Thiết kế React: attributes = State/JSX (VD: roomList, selectedRoom)
   - Mỗi Entity class có private attributes với kiểu dữ liệu VÀ methods có ()
   - Mỗi DAO class extends AbstractDAO
   - Relationships: >= 1 Generalization (DAO→AbstractDAO), N Dependencies (Boundary→DAO)
2. getDiagramGeometry(diagramName) → kiểm tra bố cục x/y:
   - Layout tốt: theo tầng — Boundary/JSP (y nhỏ nhất) < DAO < Entity; mọi connector chỉ có đoạn ngang/dọc; hộp không chồng; nhãn multiplicity/role cạnh đường
   - Layout xấu: đoạn xiên, hộp chồng, đường xuyên hộp hoặc đè nhau → autoLayoutDiagram (bỏ các ghim x/y) rồi kiểm lại
3. getRelationshipDetails(diagramName) → chiều quan hệ, multiplicity, aggregation kind (kim cương ở toàn thể)
```

### Sequence Diagram verification
```
1. getDiagramElements(diagramName) → kiểm tra cấu trúc:
   - Lifelines đúng thứ tự: Actor → Boundary → [Control] → DAO → Entity
   - Số lifeline khớp với số participant đã lên kế hoạch
   - Số message = số bước trong kịch bản (v2 hoặc v3)
   - Mỗi sync message có ít nhất 1 return message
   - Arrow labels đúng quy ước:
     · Actor→Boundary: "click btnX" hoặc "input X + click btnY"
     · Boundary/Controller kích hoạt: "call"
     · Entity/DAO method call: "methodName()" (phân tích không tham số; thiết kế có param:Type)
     · Phản hồi: "return"
     · Hiển thị kết quả: "display" hoặc "showMessage(\"msg\")"
   - KHÔNG có combined fragment alt (ngoại lệ → viết text block bên ngoài biểu đồ)
2. getDiagramGeometry(diagramName) → mọi connector có 2 điểm, đầu mút nằm trên lifeline (không x=0)
```

### UC Diagram verification
```
1. getDiagramElements(diagramName) → kiểm tra cấu trúc:
   - Số actor đúng dự kiến (thường 1 actor chính + 1 guest nếu có phân quyền)
   - Số UC đúng dự kiến (= số chức năng trong module, gồm UC con generalization)
   - Có đủ relationship types: Association (actor–UC), Include (<<include>>), Extend (<<extend>>), Generalization
2. getDiagramGeometry(diagramName) → kiểm tra bố cục:
   - Actor nằm ngoài cụm UC: x của actor nhỏ hơn x nhỏ nhất của tất cả UC (actor bên trái)
   - UC spread theo chiều dọc (y positions đa dạng, khoảng cách >= 60px) — tránh chồng
   - Nếu có nhiều actor: actor thứ 2 nằm bên phải (x lớn hơn x lớn nhất của UC)
   - Khung hệ thống ôm hết UC, actor nằm ngoài khung
```

### ERD verification
```
1. getDiagramElements(diagramName) → kiểm tra cấu trúc:
   - Số bảng đúng dự kiến (mỗi entity chính = 1 bảng)
   - Mỗi bảng có primary key column (isPrimary=true hoặc PK stereotype)
   - FK columns tồn tại ở bảng phía N của quan hệ 1:N
   - Số relationship đúng dự kiến (mỗi cặp bảng liên quan có 1 relationship)
   - Multiplicities đúng nghiệp vụ: "1..*" / "0..*" / "1" đặt đúng chiều
   - Không còn n–n giữa hai bảng; không cột dẫn xuất
2. getDiagramGeometry(diagramName) → kiểm tra bố cục:
   - Bảng trung tâm (nhiều FK nhất) nằm gần trung tâm sơ đồ
   - Các bảng liên quan spread xung quanh, x và y positions đa dạng
```

### Các loại khác
Kiểm theo gạch đầu dòng quy tắc ở cuối mỗi mục loại diagram phía trên (state, activity, communication, component, deployment, package, DFD…), cộng với `getDiagramGeometry` (không hộp chồng, connector chạm viền shape).

### Report verification
```
generateUseCaseReport / generateClassReport / generateSequenceReport / generateErdReport
→ trả về element counts — so sánh với expected counts từ plan:
   UC: actor count, use case count, relationship count
   Class: class count per package, attribute count, method count, relationship count
   Sequence: lifeline count, message count
   ERD: table count, column count, relationship count
```
Các loại không có report: dùng `getElementCounts(diagramName)` so với plan.

---

## Giới hạn đã chứng minh (đừng thử lại)

Đã thử nhiều cách với VP 18.1 (CE) và plugin 1.32.3–1.32.6; đây là giới hạn của VP/API, không phải lỗi gọi tool:

- **Component interface dạng lollipop:** VP không vẽ shape lollipop khi tạo bằng API (thử theo model, shape type, cỡ 24–60px, mở lại diagram: không vẽ gì). Interface luôn là hộp `<<interface>>`; không có assembly/delegation connector.
- **Sequence actor dạng hình que:** lifeline actor tạo bằng API luôn có đầu hộp; hình que không neo được message (message trôi về x=0). Chấp nhận hộp (UML hợp lệ), hoặc user đổi tay.
- **Sequence `lifelineType` không đổi được** sau khi đã có message → tạo lại diagram.
- **Destroy (`messageType="destroy"`):** lifeline chỉ kết thúc tại mũi tên — VP không vẽ dấu X cho lifeline tạo bằng API (`setStopped` + mở lại diagram cũng không đổi).
- **Guard của operand combined fragment:** VP tự vẽ ở góc trên-trái của operand, có thể chạm thanh lifeline đầu tiên — không có caption để dời.
- **Pseudo-state (initial/final):** VP luôn in tên model dưới hình; không giấu được (đặt tên đẹp).
- **Chưa có tool/không hỗ trợ:** BPMN boundary event, text annotation, call activity, loop marker; UML composite state / choice / history / internal transition; activity send-signal/accept-event action và pin; sequence found/lost message; `removeRelationship` không liệt kê Usage.
- **Giới hạn layout còn lại (plugin 1.32.6+):**
  - Deployment lồng nhiều tầng (máy → server → artifact) ra dải ngang dài khoảng 5:1, vì ELK không xếp chồng tầng ngoài khi giữ các host lồng trên một hàng.
  - Communication có nhiều shape ghim sát nhau thì nhãn message còn có thể chật.
  - Ký hiệu database của flowchart là hình trụ phẳng của VP (không bóng, không gradient), API không đổi được.
  - Một mẩu 2–3px còn sót ở cuối thanh kích hoạt sequence.
- **`removeDiagramElement` chỉ gỡ view** (model còn trong project, trừ lifeline/link/message); `removeTable`/`removeColumn` xoá thật khỏi project.
- **Hộp thoại modal của VP** (hỏi lưu, hỏi xoá khỏi repository) chặn `openProject` và việc thoát VP; plugin tự trả lời các hộp xoá, còn hộp lưu thì phải tự xử lý.

---

## Constraints

- VP MCP server phải chạy trên `localhost:2026` (hoặc URL tùy chỉnh)
- Tên diagram trong VP phải unique — nếu trùng sẽ lỗi (tool `create*` từ chối tên trùng/rỗng trước khi tạo)
- Tham số rỗng: truyền `""` (empty string), KHÔNG truyền null; int không dùng = `0`, boolean không dùng = `false` (schema coi mọi tham số là bắt buộc)
- Tên element trong VP KHÔNG được chứa ký tự đặc biệt (dùng tiếng Việt không dấu nếu cần)
- `addColumn`: `length` và `scale` là integer, không phải string
- `addMessage`: `messageType` nhận `"sync"`/`"synch"`, `"async"`/`"asynch"`, `"create"`, `"destroy"`
- `addCombinedFragment`: `operator` chỉ nhận `"alt"`, `"opt"`, `"loop"`, `"break"`, `"par"`
- Relationship trong class diagram: thêm **sau khi** đã add tất cả classes và attributes (`extendsClass`/`implementsInterfaces` của `addClass` cần lớp cha ĐÃ có trên diagram)
- Sequence diagram: add lifelines **trước**, messages **sau**, combined fragment sau cùng
- **Class naming → ClassXXX:** Nếu cùng tên class ở nhiều diagram → VP sinh `ClassXXX`. Dùng tên unique (suffix số: `LecturerHomeFrm2`). Không có tool rename — phải sửa tay trong VP GUI.
- **`addAttribute`/`addOperation` first-match:** Match class đầu tiên có tên đó trong toàn project. Dùng tên unique → không bao giờ nhầm.
- **Sequential DAO addition:** Thêm DAO abstract vào diagram đầu tiên, rồi các diagram sau TUẦN TỰ (không song song).
- **`autoLayoutDiagram` recreates packages:** KHÔNG gọi sau khi remove package.
- **`addDependency` invisible:** `getDiagramElements` không liệt kê Dependency. Verify phải mở VP GUI.
- **Export ảnh:** ~~Không có tool export~~ — từ plugin 1.27.9 đã có `exportDiagramImage(diagramName, filePath)`; export tay chỉ khi cần chỉnh hình trong VP trước.
- *Cập nhật theo plugin 1.32 (các quy ước trên giữ nguyên):* `addClass` nay dùng lại lớp cùng tên (root hoặc trong `modelPackage`) thay vì sinh `Class2`, và `addAttribute`/`addOperation` nhận `diagramName` để chỉ tra lớp hiện trên diagram đó — nhưng lớp dùng lại chia sẻ thuộc tính giữa các diagram, nên quy ước tên unique vẫn là cách an toàn. `getDiagramElements` nay in mọi connector (kể cả Dependency/Usage) dạng `Type <<stereotype>> name: from -> to`; vẫn nên mở VP xem hình để chắc.
