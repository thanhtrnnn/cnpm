# Danh mục VP MCP tools (117 tools)

Nguồn: các method `@Tool(name=…)` trong `visual-paradigm-mcp-plugin/src/main/java/com/brunnen/vp/mcp/tools/*.java` (plugin `serverInfo.version` 1.32.3.25). Tên tool và thứ tự tham số lấy từ Java, không từ trí nhớ; khi plugin đổi, sinh lại danh mục từ nguồn.

**Quy ước gọi:**

- MCP gọi theo TÊN tham số. Schema của plugin coi MỌI tham số là bắt buộc: tham số không dùng truyền `""` (String), `0` (int), `false` (bool); đừng truyền null.
- `x`,`y` (int): > 0 = đặt góc trên-trái tại toạ độ diagram; 0 = tool tự đặt. `width`,`height`: > 0 = đặt cỡ; 0 = fit/mặc định.
- Tool trả về CHUỖI, không ném lỗi: lỗi/từ chối là chuỗi (`Error …`, `… not found`, `… already exists`, `Unknown …`). Luôn đọc kết quả mỗi lần gọi.
- Tên diagram: rỗng hoặc trùng diagram đã có thì `create*` từ chối. Gọi sai loại diagram thì báo `Diagram 'X' is a StateDiagram, …`.
- Cột "Tham số": kiểu `int`/`bool` ghi sau dấu hai chấm, còn lại là String.
- Gọi qua HTTP khi session Claude chưa thấy tool mới: `curl -s -X POST http://localhost:2026/api/execute -H 'Content-Type: application/json' -d '{"toolName":"listDiagrams","arguments":{"type":""}}'` → `{"result":"…"}` hoặc `{"error":"…"}`.

## Project (5)

Làm việc với file `.vpp` đang mở trong VP. `getProjectInfo` dùng làm chốt chặn trước khi sửa (đúng file chưa).

| Tool | Tham số (theo thứ tự) | Công dụng |
|------|-----------------------|-----------|
| `getProjectInfo` | (không có) | Tên + đường dẫn file project đang mở. |
| `saveProject` | (không có) | Lưu project vào file hiện tại. |
| `saveProjectAs` | filePath | Lưu sang `.vpp` mới (thư mục cha phải có; KHÔNG ghi đè file có sẵn); file mới thành project đang mở. |
| `openProject` | filePath | Mở `.vpp` khác, thay project đang mở (lưu trước; hộp thoại lưu của VP có thể chặn). |
| `newProject` | (không có) | Đóng project hiện tại, tạo project trống (thay đổi chưa lưu bị bỏ). |

## Dùng cho mọi loại diagram (11)

`x`,`y` > 0 mới có tác dụng; `width/height <= 0` = fit theo nội dung.

| Tool | Tham số (theo thứ tự) | Công dụng |
|------|-----------------------|-----------|
| `listDiagrams` | type | Liệt kê diagram, lọc theo loại: UseCase, Class, Sequence, Communication, State, Activity, Component, Deployment, Package, Object, ER, BPMN, Flowchart, DFD (`""` = tất cả); khớp chính xác loại. |
| `getDiagramElements` | diagramName | Mọi shape + connector: tên, loại, chi tiết, vị trí; connector in dạng `Type <<stereotype>> name: from -> to [guard]`. |
| `getDiagramGeometry` | diagramName | Dump hình học: bounds mọi shape (lồng nhau thụt vào), điểm của connector, bounds của caption — kiểm bố cục không cần ảnh. |
| `getElementCounts` | diagramName | Đếm phần tử theo loại. |
| `autoLayoutDiagram` | diagramName | Auto layout. KHÔNG đáng tin cho hầu hết loại; sequence = no-op có chủ đích (xem SKILL.md). |
| `removeDiagramElement` | diagramName, elementName | Gỡ shape/connector khỏi diagram theo tên model; chỉ gỡ VIEW (kèm connector và shape lồng bên trong), model còn trong project — trừ lifeline/link/message (chỉ tồn tại trên diagram). |
| `addNote` | diagramName, text, attachedTo, x:int, y:int | Thêm ghi chú (hộp góc gấp) vào bất kỳ diagram; `attachedTo` = tên shape để nối đường đứt (`""` = tự do). |
| `setElementBounds` | diagramName, elementName, x:int, y:int, width:int, height:int | Di chuyển/đổi cỡ shape. Container (package, node, component, lane…) kéo theo shape lồng bên trong và không bao giờ nhỏ hơn nội dung; lifeline kéo theo message + thanh kích hoạt; control node, pseudo-state, symbol BPMN/flowchart/DFD giữ cỡ ký hiệu. |
| `rerouteConnectors` | diagramName | Neo lại mọi connector vào tâm shape (thẳng tâm–tâm hoặc routing riêng của họ diagram); chạy sau khi dời shape, và mở diagram trong VP trước. |
| `layoutConnectorLabels` | diagramName, coordinateMode | Đặt nhãn association: multiplicity cạnh hai đầu, tên giữa đường, ẩn role. `coordinateMode` = `absolute` \| `relative`. |
| `exportDiagramImage` | diagramName, filePath | Mở diagram và ghi ảnh `.png/.jpg/.jpeg` ra đường dẫn TUYỆT ĐỐI. (Skill này giữ quy ước xuất ảnh thủ công — xem mục "Xuất ảnh" trong SKILL.md; tool nêu ở đây cho đủ danh mục.) |

## Use Case (6)

Tên actor/use case trùng tên đã có trong project = CÙNG phần tử (dùng lại, vẽ view mới).

| Tool | Tham số (theo thứ tự) | Công dụng |
|------|-----------------------|-----------|
| `createUseCaseDiagram` | diagramName | Tạo diagram UC (ẩn ngăn "extension points"). |
| `addActor` | actorName, diagramName, x:int, y:int | Thêm actor; x/y > 0 đặt tay (vd actor cha trừu tượng phía trên con), mặc định xuống cột trái. |
| `addUseCase` | useCaseName, diagramName, x:int, y:int | Thêm use case; mặc định xuống cột UC (cách nhau 60px). |
| `addRelationship` | diagramName, sourceName, targetName, relationshipType | `relationshipType` = Include \| Extend \| Generalization \| Association. Include: source = UC gốc, target = UC được include. Extend: source = UC mở rộng (tuỳ chọn), target = UC gốc (mũi tên chạm UC gốc). Generalization: source = con, target = cha (tam giác ở cha). Trùng cặp thì báo, không vẽ lại. |
| `addSystemBoundary` | diagramName, systemName | Khung hệ thống/module bao mọi UC (actor bị đẩy ra ngoài); gọi sau khi UC đã vào chỗ cuối; gọi lại = đổi tên + co giãn khung. |
| `generateUseCaseReport` | diagramName | Báo cáo phân tích UC. |

## Class (21, chưa tính Project và nhóm chung)

Tên lớp là khoá tra cứu. `addClass` dùng lại lớp cùng tên (root, hoặc trong `modelPackage`) thay vì tạo `Class2`. `extendsClass`/`implementsInterfaces` phải ĐÃ có trên diagram.

| Tool | Tham số (theo thứ tự) | Công dụng |
|------|-----------------------|-----------|
| `createClassDiagram` | diagramName | Tạo class diagram (bật auto-fit). |
| `addClass` | diagramName, className, packageName, packageColor, stereotype, isAbstract:bool, extendsClass, implementsInterfaces, x:int, y:int, modelPackage | Thêm lớp. Hộp trắng: `packageName`, `packageColor`, `stereotype` để `""`. `x/y` > 0 đặt tay, không thì ô trống đầu tiên của hàng theo tầng (tên kết thúc View\|Form\|Screen hoặc bắt đầu Frm\|Page = hàng trên; kết thúc DAO\|Repository\|Mapper = hàng giữa; còn lại, kể cả XxxFrm, XxxPage, XxxController và entity = hàng dưới), khoảng ba lớp một hàng. `modelPackage` = package model (không vẽ khung) để tách lớp cùng tên. `extendsClass` vẽ generalization. |
| `addAttribute` | className, attributeName, attributeType, visibility, diagramName | Thêm thuộc tính; `attributeType` có thể rỗng (pha phân tích); `visibility` = public\|private\|protected\|package (hoặc + - # ~). Có `diagramName` thì chỉ dùng lớp hiện trên diagram đó. |
| `addOperation` | className, operationName, returnType, params, visibility, isAbstract:bool, diagramName | Thêm phương thức; `params` = `name: Type, ...`; `visibility`, `isAbstract`; `diagramName` giới hạn tra cứu như addAttribute. |
| `addAssociation` | diagramName, fromClass, toClass, fromMultiplicity, toMultiplicity, name | Association; multiplicity chấp nhận số, `*`, `n`, `m`, `a..b`; `name` = tên quan hệ. |
| `addGeneralization` | diagramName, fromClass, toClass | `fromClass` = lớp CON, `toClass` = lớp CHA; tam giác rỗng ở lớp cha. |
| `addAggregation` | diagramName, fromClass, toClass, fromMultiplicity, toMultiplicity | Aggregation ◇; `fromClass` = TOÀN THỂ (kim cương ở đầu from), `toClass` = bộ phận. |
| `addComposition` | diagramName, fromClass, toClass, fromMultiplicity, toMultiplicity | Composition ◆; `fromClass` = TOÀN THỂ, `toClass` = bộ phận. |
| `addDependency` | diagramName, fromClass, toClass | Dependency (đường chấm, mũi tên mở): `fromClass` phụ thuộc `toClass`. |
| `addRealization` | diagramName, fromClass, toClass | Realization: `fromClass` = lớp cài đặt, `toClass` = interface (tam giác rỗng ở interface). |
| `addInterface` | diagramName, interfaceName | Thêm interface vào class diagram. |
| `addPackage` | diagramName, packageName, backgroundColor | Thêm package có màu nền (chỉ khi user yêu cầu tường minh). |
| `addPackageShape` | diagramName, packageName, parentPackage, modelPackage, x:int, y:int, width:int, height:int, backgroundColor | Vẽ khung package tại bounds cho trước; `parentPackage` lồng vào khung khác; `modelPackage` chọn package model sở hữu; `backgroundColor` = `#RRGGBB` hoặc rỗng. Dùng cho khung View/Controller/DAO/Model. |
| `moveIntoPackage` | diagramName, elementName, packageName | Đặt lớp (hoặc package) vào khung package trên cùng diagram: package thành owner trong model + container trên diagram; giữ bounds. |
| `addUsage` | diagramName, fromName, toName | Dependency `<<use>>` (đường chấm, nhãn «use») giữa hai lớp hoặc hai package. |
| `setClassColor` | diagramName, className, backgroundColor | Đặt màu nền hộp lớp (mặc định để trắng — chỉ khi user yêu cầu). |
| `generateClassReport` | diagramName | Báo cáo class diagram (lớp con đứng trước, có ký hiệu visibility, loại quan hệ + multiplicity hai đầu). |
| `addStereotypeToClasses` | diagramName, classNames, stereotype, robustnessIcon | Gán stereotype (vd `ORM Persistable`) cho danh sách lớp (phân cách dấu phẩy) hoặc `*` = mọi lớp; `robustnessIcon` true/false = vẽ boundary/control/entity dạng icon hay hộp lớp có member (`""` = giữ nguyên). |
| `removeRelationship` | diagramName, fromClass, toClass, relationshipType | Xoá quan hệ giữa hai lớp khỏi MODEL (shape + model). `relationshipType` = Generalization (from = con) \| Association \| Aggregation \| Composition \| Dependency \| Realization. Chưa liệt kê Usage. |
| `setAssociationProperties` | diagramName, fromClass, toClass, name, fromMultiplicity, toMultiplicity, fromRole, toRole, fromNavigable, toNavigable | Sửa association/aggregation/composition đã có (hai chiều): `name`, multiplicity, `fromRole`/`toRole` (`-` = xoá role), `fromNavigable`/`toNavigable` = true\|false\|unspecified. Rỗng = giữ nguyên. |
| `getRelationshipDetails` | diagramName | Dump JSON để audit: lớp (abstract, stereotype, owner, thuộc tính, phương thức, bounds) + mọi quan hệ (multiplicity, kiểu aggregation, role, navigability, điểm connector). |

## ERD (11)

Tên bảng/cột là SQL identifier (chữ, số, `_`; không dấu, không khoảng trắng). Bảng cùng tên trong project là CÙNG bảng. Bốn bảng một hàng.

| Tool | Tham số (theo thứ tự) | Công dụng |
|------|-----------------------|-----------|
| `createErd` | diagramName | Tạo ER diagram. |
| `addTable` | diagramName, tableName | Thêm bảng. |
| `addColumn` | diagramName, tableName, columnName, columnType, length:int, scale:int, isPrimaryKey:bool, isNullable:bool, isUnique:bool | Thêm cột vào bảng trên diagram. `columnType` = SQL type (`varchar`, `integer`, `date`, `decimal(10,2)`…; `nvarchar`, `datetime`, `bit`… được ánh xạ sang kiểu VP biết); kiểu ghi kèm độ dài thắng `length/scale`; `varchar` không độ dài = 255; `isUnique` = chữ "U" cạnh khoá. |
| `addForeignKey` | diagramName, fromTable, toTable, fromColumn, toColumn, relationshipName | FK: `fromTable` = bảng CON giữ `fromColumn`, `toTable` = bảng CHA (`toColumn` rỗng = khoá chính). Cột `fromColumn` có sẵn trở thành cột FK; để rỗng thì VP tự thêm cột đặt theo bảng cha. Chân quạ ở bảng con. |
| `addTableRelationship` | diagramName, fromTable, toTable, type, fromMultiplicity, toMultiplicity | Quan hệ identifying/non-identifying: `fromTable` = bảng CHA, `toTable` = bảng CON (NGƯỢC chiều addForeignKey); `type` = identifying \| nonIdentifying \| `""`; mult from = `1`\|`0..1`, mult to = `0..1`\|`0..*`\|`1`\|`1..*`. Cũng sinh cột FK ở bảng con; cặp bảng đã có quan hệ thì bị từ chối. |
| `removeColumn` | diagramName, tableName, columnName | Xoá cột khỏi project (cột FK phải gỡ FK trước). |
| `renameColumn` | diagramName, tableName, columnName, newName | Đổi tên cột. |
| `removeTable` | diagramName, tableName | Xoá bảng khỏi project (mọi diagram mất bảng); bảng đang tham gia FK bị từ chối. |
| `removeForeignKey` | diagramName, parentTable, childTable | Xoá FK giữa `parentTable` và `childTable`; cột FK vẫn còn ở bảng con. |
| `generateDdl` | diagramName | Sinh `CREATE TABLE` cho mọi bảng. |
| `generateErdReport` | diagramName | Báo cáo ERD (kết quả liệt kê cả cột sinh ra). |

## Sequence (7)

Mọi message tham chiếu lifeline bằng `lifelineName`. Số thứ tự đã dùng bị từ chối. Không viết `N:` trong nhãn (VP tự in số).

| Tool | Tham số (theo thứ tự) | Công dụng |
|------|-----------------------|-----------|
| `createSequenceDiagram` | diagramName | Tạo sequence diagram. |
| `addLifeline` | diagramName, lifelineName, className, lifelineType, alias | Thêm lifeline; `lifelineName` = nhãn đầu + handle (unique trên diagram); `className` rỗng = lấy `lifelineName`, lớp/actor có sẵn cùng tên được dùng lại (không sửa); `lifelineType` = actor\|boundary\|control\|entity (icon chỉ cho lifeline này) hoặc `""`/participant = hộp trơn; actor luôn đầu hộp; `alias` để rỗng. |
| `addActivation` | diagramName, lifelineName | Thêm thanh kích hoạt (tuỳ chọn: message tự tạo thanh, tool gộp thành thanh liền). |
| `addMessage` | diagramName, fromLifeline, toLifeline, messageName, sequenceNumber, messageType | `messageType` = synch/sync (mặc định, nét liền đầu đặc) \| asynch/async (đầu hở) \| create (đầu tiên tới lifeline, nét đứt, hạ đầu xuống mũi tên) \| destroy (cuối cùng tới lifeline; KHÔNG có dấu X). `sequenceNumber` rỗng = số cấp 1 kế tiếp; hỗ trợ `5.1`. `from == to` = self-message. Nhãn dài hơn mũi tên sẽ đẩy các lifeline bên phải ra. |
| `addReturnMessage` | diagramName, fromLifeline, toLifeline, messageName, sequenceNumber | Return (nét đứt, đầu hở); `sequenceNumber` như addMessage. |
| `addCombinedFragment` | diagramName, operator, guard, coveredLifelines, fromSeq:int, toSeq:int, operandStarts | Khung alt/opt/loop/break/par bao message `fromSeq`..`toSeq` (cấp 1, gồm cả 4.1, 4.2…; 0 = đầu/cuối). Thêm MESSAGE trước. `guard` nhiều operand ngăn bằng `\|`; `operandStarts` = số message đầu của operand 2..n (rỗng = chia đều); `coveredLifelines` rỗng = tất cả. |
| `generateSequenceReport` | diagramName | Báo cáo sequence. |

## State machine (5)

Cần plugin >= 1.28.4. Tên state là handle của `addTransition`. Nhãn/caption chỉ hiện sau `resetCaption` (tool tự làm).

| Tool | Tham số (theo thứ tự) | Công dụng |
|------|-----------------------|-----------|
| `createStateDiagram` | diagramName | Tạo state machine diagram. |
| `addState` | diagramName, stateName, entryAction, doActivity, exitAction, x:int, y:int | Thêm state; `entryAction/doActivity/exitAction` (rỗng = bỏ) hiện ngăn `entry / …`, `do / …`, `exit / …`; hộp fit theo chữ. x/y > 0 đặt tay, không thì lưới 3 cột và dời xuống dưới nguồn của transition đến đầu tiên. |
| `addInitialState` | diagramName, stateName, x:int, y:int | Initial pseudo-state (hình tròn đặc). VP LUÔN in tên model dưới hình → đặt tên đẹp (`Bat dau`/`Start`). |
| `addFinalState` | diagramName, stateName, x:int, y:int | Final state (bia). Tên in dưới hình → `Ket thuc`/`End`. |
| `addTransition` | diagramName, fromState, toState, label | Transition; `label` = `event [guard] / effect` (rỗng = không nhãn); `fromState == toState` = self-loop; cặp đi/về được bẻ để nhãn không chồng. |

## Activity (7)

`actionName`/`nodeName`/`objectName` là handle của `addActivityFlow` → unique trên diagram.

| Tool | Tham số (theo thứ tự) | Công dụng |
|------|-----------------------|-----------|
| `createActivityDiagram` | diagramName | Tạo activity diagram (shape fit theo chữ). |
| `addActivityPartition` | diagramName, partitionName, x:int, y:int, width:int, height:int | Thêm swimlane dọc; lane đầu tạo khung tại x/y (mặc định 40,40), các lane sau nối bên phải (x/y bị bỏ qua); width/height > 0 chỉnh cỡ lane (mặc định 240x480); mọi lane cùng chiều cao và tự giãn theo node. |
| `addActivityAction` | diagramName, actionName, partitionName, x:int, y:int | Thêm action (hộp bo tròn); `partitionName` = lane (`""` = không lane); x/y > 0 đặt góc trên-trái. |
| `addActivityControlNode` | diagramName, kind, nodeName, partitionName, x:int, y:int | `kind` = initial \| final \| flowFinal \| decision \| merge \| fork \| join. decision hiện câu hỏi (`nodeName`, vd `Valid?`); initial/final hiện tên (`Start`/`End`); fork/join là thanh ngang. |
| `addActivityObjectNode` | diagramName, objectName, state, partitionName, x:int, y:int | Object node, `state` hiện `[state]` dưới tên; flow tới/từ nó là object flow. |
| `addActivityFlow` | diagramName, fromNode, toNode, guard, twoWay:bool | Nối hai node theo tên; `guard` hiện `[guard]` (thường trên cạnh rời decision); `twoWay=true` = một mũi tên hai đầu (action <-> "XxxDAO: method()" của sách). Đích tự đặt được dời xuống dưới nguồn (nhánh cùng fork/decision đứng cạnh nhau). |
| `addActivityFrame` | diagramName, title, nodeNames, x:int, y:int, width:int, height:int | Khung bo tròn tiêu đề đậm (UML activity) = "Xử lí tại gdXxx.jsp"; `nodeNames` = danh sách node phân cách dấu phẩy mà khung bao (đặt SAU khi node + flow đã xong); `nodeNames` rỗng thì dùng x/y/width/height; gọi lại cùng `title` = co giãn lại. |

## Component (8)

`<<component>>` do VP tự in — đừng truyền làm stereotype. Interface là hộp `<<interface>>`, KHÔNG phải lollipop.

| Tool | Tham số (theo thứ tự) | Công dụng |
|------|-----------------------|-----------|
| `createComponentDiagram` | diagramName | Tạo component diagram. |
| `addComponent` | diagramName, componentName, stereotype, parentComponent, x:int, y:int, packageName | Thêm component; `stereotype` (rỗng/`subsystem`…, nhiều cái ngăn dấu phẩy); `parentComponent` lồng vào component khác; `packageName` đặt vào khung layer (đã tạo bằng addComponentPackage); x/y > 0 đặt tay. Component có sẵn trong project được dùng lại. |
| `addComponentInterface` | diagramName, interfaceName, x:int, y:int | Interface vẽ dạng hộp `<<interface>>`; dùng lại interface cùng tên. |
| `addProvidedInterface` | diagramName, componentName, interfaceName | Component cung cấp interface: realization nét đứt, tam giác rỗng ở hộp interface; `componentName` có thể là port. |
| `addRequiredInterface` | diagramName, componentName, interfaceName | Component cần interface: mũi tên nét đứt `<<use>>` tới hộp interface; `componentName` có thể là port. |
| `addComponentDependency` | diagramName, fromComponent, toComponent, stereotype | Dependency nét đứt giữa component/interface/port; `stereotype` (`use`, `call`…) hiện `<<stereotype>>`. |
| `addPort` | diagramName, componentName, portName | Port (ô vuông nhỏ trên viền); port xen kẽ cạnh trái/phải; component giãn khi không đủ chỗ. |
| `addComponentPackage` | diagramName, packageName, parentPackage, x:int, y:int, width:int, height:int | Khung layer ("Presentation Layer"…); `parentPackage` lồng khung; component thêm với `packageName` nằm trong và khung tự giãn; cỡ khởi đầu 200x100. |

## Deployment (7)

Tên node/artifact/component unique trên diagram.

| Tool | Tham số (theo thứ tự) | Công dụng |
|------|-----------------------|-----------|
| `createDeploymentDiagram` | diagramName | Tạo deployment diagram. |
| `addDeploymentNode` | diagramName, nodeName, kind, parentNode, x:int, y:int, width:int, height:int | `kind` = node \| device \| executionEnvironment (`""` = node); `parentNode` lồng node (vd Tomcat trong Web Server); node giãn theo nội dung; node cấp cao nằm trên hàng node. |
| `addDeploymentArtifact` | diagramName, artifactName, nodeName, x:int, y:int | Artifact (`app.war`, `schema.sql`); `nodeName` rỗng = đứng riêng (nối bằng addDeployDependency), tên node = triển khai vào node (vẽ bên trong), tên artifact = vẽ bên trong artifact đó. |
| `addDeploymentComponent` | diagramName, componentName, nodeName, x:int, y:int | Component do node hoặc artifact chứa (View/Controller/Model trong `app.war`); các component cùng host xếp một hàng, cách nhau 90px, host giãn theo. |
| `addCommunicationPath` | diagramName, fromNode, toNode, label | Đường liền giữa hai node; `label` = giao thức (`1: HTTP/HTTPS`); `<<TCP/IP>>` = hiện như stereotype. |
| `addDeployDependency` | diagramName, artifactName, nodeName | Dependency `<<deploy>>` từ artifact tới node — chỉ cho artifact đứng riêng. |
| `addDeploymentDependency` | diagramName, fromElement, toElement, label | Dependency nét đứt giữa component/artifact/node (View -> Controller nhãn `submit`); nhãn dạng `<<manifest>>` thành stereotype. |

## Package và Object (7)

Thêm con của một package trước package cấp cao kế tiếp để khung tự đặt không chồng.

| Tool | Tham số (theo thứ tự) | Công dụng |
|------|-----------------------|-----------|
| `createPackageDiagram` | diagramName | Tạo package diagram. |
| `addPackageElement` | diagramName, packageName, parentPackage, x:int, y:int, width:int, height:int | Khung package; `parentPackage` lồng (cha giãn theo); package cấp cao tự xếp 3 khung một hàng, con xếp một hàng trong cha; tối thiểu 100x50. Package cùng tên có sẵn được dùng lại. |
| `addPackageDependency` | diagramName, fromPackage, toPackage, kind | `kind` = use \| import \| access \| merge \| line (`""` = use). `line` = đường liền không mũi tên, không từ khoá (view - dao - model của sách); use = `<<use>>` nét đứt mũi tên mở. Đầu có thể là hộp lớp đang nằm trong package. |
| `addClassInPackage` | diagramName, packageName, className | Hộp lớp (chỉ tên) trong khung package; lớp thuộc package đó trong model. |
| `createObjectDiagram` | diagramName | Tạo object diagram (hiện slot). |
| `addObject` | diagramName, objectName, className, slots, x:int, y:int, modelPackage | Instance `objectName : ClassName` gạch chân; `objectName` rỗng + `className` = đối tượng ẩn danh `: ClassName` (handle = tên lớp); `slots` = `attr=value;attr2=value2`, attr phải là thuộc tính của lớp (hoặc lớp cha); không có lớp thì tạo lớp mới; `modelPackage` chọn lớp khi nhiều package có lớp cùng tên. |
| `addObjectLink` | diagramName, fromObject, toObject, label | Link (đường liền) giữa hai object, `label` rỗng = không nhãn. |

## Communication (5)

Thứ tự tham số của `addCommunicationMessage` là `sequenceNumber` rồi `messageText` (khác addMessage của sequence).

| Tool | Tham số (theo thứ tự) | Công dụng |
|------|-----------------------|-----------|
| `createCommunicationDiagram` | diagramName | Tạo communication diagram (hiện số thứ tự message, fit theo chữ). |
| `addCommunicationLifeline` | diagramName, lifelineName, classifierName, isActor:bool, x:int, y:int, lifelineType | Participant; `lifelineName` = nhãn + handle; `classifierName` kiểu `name : Classifier`; `lifelineName` rỗng + `classifierName` = đối tượng ẩn danh `:Classifier` (handle = tên classifier); `isActor=true` = hình người que; `lifelineType` = boundary\|control\|entity vẽ icon robustness (GDxxx, entity của sách), rỗng = hộp trơn; x/y > 0 đặt tay. |
| `addCommunicationLink` | diagramName, fromLifeline, toLifeline | Link (đường các message chạy trên đó); cùng tên hai đầu = self link; trùng thì báo link cũ. |
| `addCommunicationMessage` | diagramName, fromLifeline, toLifeline, sequenceNumber, messageText | Message đánh số, vẽ thành mũi tên cạnh link (tự tạo link nếu thiếu), hướng from -> to. `sequenceNumber` = biểu thức UML (`1`, `1.2`, `2a`, `1.1*`), rỗng = số cấp 1 kế tiếp. `1.2:` ở đầu `messageText` bị cắt. |
| `moveCommunicationLifeline` | diagramName, lifelineName, x:int, y:int | Dời participant tới x/y (góc trên-trái); link và mũi tên message được bố trí lại — để đạt bố cục sách: actor giữa trên, hàng boundary, entity bên dưới. |

## Flowchart và DFD (8)

DFD: flow phải chạm một process (entity/store tới entity/store bị từ chối).

| Tool | Tham số (theo thứ tự) | Công dụng |
|------|-----------------------|-----------|
| `createFlowchart` | diagramName | Tạo flowchart. |
| `addFlowchartShape` | diagramName, shapeName, kind, x:int, y:int | `kind` = terminator \| process \| decision \| inputOutput \| document \| predefinedProcess \| database \| manualInput \| connector; `shapeName` hiện trên shape + là handle (unique); tự xếp một cột trên->dưới, cách 50px. |
| `addFlowchartFlow` | diagramName, fromShape, toShape, label | Mũi tên nối hai shape; `label` (vd Yes/No). |
| `createDataFlowDiagram` | diagramName, notation | `notation` = `""`/standard \| ganeSarson \| yourdonDeMarco \| yourdonCoad; các add*Dfd* theo ký hiệu của diagram. |
| `addDfdProcess` | diagramName, processName, processId, x:int, y:int | Process; `processId` = số hiện trên process (`1`, `1.0`, `1.1`), rỗng = tiếp số của diagram; tham chiếu bằng tên hoặc ID. |
| `addDfdExternalEntity` | diagramName, entityName, entityId, x:int, y:int | External entity; `entityId` = ký hiệu a, b, c ở góc hộp (rỗng = tiếp chữ). |
| `addDfdDataStore` | diagramName, storeName, storeId, x:int, y:int | Data store; `storeId` `D1` hoặc `1` (VP tự in chữ D); rỗng = tiếp số. |
| `addDfdDataFlow` | diagramName, fromElement, toElement, label | Data flow (tham chiếu tên hoặc ID); `label` = dữ liệu di chuyển (danh từ). |

## BPMN (9)

Tên phần tử là handle của các tool flow → unique trên diagram. Chưa có: boundary event, text annotation, call activity, loop marker.

| Tool | Tham số (theo thứ tự) | Công dụng |
|------|-----------------------|-----------|
| `createBpmnDiagram` | diagramName | Tạo BPMN 2.0 diagram. |
| `addBpmnPool` | diagramName, poolName, x:int, y:int, width:int, height:int | Pool (participant) dạng dải ngang, tên bên trái; cỡ mặc định 900x160 (cao 40-60 = pool hộp đen); giãn theo lane/phần tử. |
| `addBpmnLane` | diagramName, poolName, laneName | Lane trong pool, xếp trên->dưới theo thứ tự thêm; thêm HẾT lane của pool trước khi đặt phần tử. |
| `addBpmnTask` | diagramName, taskName, laneName, kind, x:int, y:int | `kind` = task \| user \| service \| manual \| send \| receive \| script \| subprocess; `laneName` = lane (hoặc pool không lane), `""` = ngoài pool. |
| `addBpmnEvent` | diagramName, eventName, laneName, position, trigger, x:int, y:int | `position` = start \| intermediate \| end; `trigger` = none (`""`) \| message \| timer \| error \| signal \| terminate (chỉ end; end không dùng timer); tên hiện dưới vòng tròn. |
| `addBpmnGateway` | diagramName, gatewayName, laneName, kind, x:int, y:int | `kind` = exclusive (`""`) \| parallel \| inclusive \| eventBased; tên = câu hỏi hiện phía trên thoi. |
| `addBpmnDataObject` | diagramName, name, laneName, x:int, y:int | Data object (vd `Invoice`, `Order [approved]`), nối bằng addBpmnSequenceFlow thành data association. |
| `addBpmnSequenceFlow` | diagramName, fromElement, toElement, condition | Sequence flow liền trong CÙNG pool; `condition` ghi nhãn nhánh (`Yes`/`[in stock]`); tool kiểm luật BPMN (không flow ra khỏi end, vào start, xuyên pool); data object -> data association chấm. |
| `addBpmnMessageFlow` | diagramName, fromElement, toElement, label | Message flow nét đứt giữa HAI pool khác nhau (đầu là vòng tròn hở); đầu có thể là task, sub-process, event hoặc tên pool. |
