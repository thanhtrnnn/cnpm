# PHẦN I. MÔ TẢ HỆ THỐNG

Mô tả hệ thống và khảo sát hệ thống tương tự

## 1. Mô tả chung về hệ thống

### 1.1. Bài toán thực tế

Hệ thống được định hướng như một nền tảng quản lý tập trung cho chuỗi nhà hàng karaoke, với mục tiêu giảm sai sót thủ công trong quản lý phòng, gọi món, thanh toán, đồng bộ dữ liệu giữa các chi nhánh, nâng cao trải nghiệm khách hàng qua đặt phòng online và tích điểm thành viên, đồng thời hỗ trợ chủ doanh nghiệp ra quyết định bằng báo cáo doanh thu theo thời gian.

Từ góc nhìn thực tiễn, bài toán này xuất phát từ đặc thù của mô hình karaoke: một phiên phục vụ luôn đi kèm nhiều biến số vận hành cùng lúc như thời gian sử dụng phòng, trạng thái phòng, order đồ ăn thức uống, khuyến mãi khách quen, ca làm của nhân viên và tồn kho tiêu hao. Khi quy mô phát triển từ một cơ sở sang nhiều chi nhánh, các thao tác rời rạc hoặc phụ thuộc ghi chép thủ công rất dễ tạo ra sai lệch doanh thu, nhầm trạng thái phòng và chậm phản hồi cho khách.

### 1.2. Phạm vi chức năng

Hệ thống gồm sáu phân hệ cốt lõi: quản lý đặt phòng, gọi món và dịch vụ, quản lý hội viên, quản lý kho, quản lý nhân sự và báo cáo doanh thu.

Cụ thể hơn, mỗi phân hệ không chỉ là một nhóm tính năng độc lập mà còn tạo thành chuỗi nghiệp vụ xuyên suốt một phiên phục vụ:

- Quản lý đặt phòng: tiếp nhận đặt trước, bố trí phòng trực tiếp, theo dõi trạng thái phòng trống, đang dùng hoặc bảo trì.
- Gọi món và dịch vụ: nhận order từ phòng, chuyển yêu cầu tới bếp hoặc quầy bar, cập nhật trạng thái món và cộng dồn vào hóa đơn cuối.
- Quản lý hội viên: lưu thông tin khách, lịch sử sử dụng, tích điểm và áp dụng ưu đãi.
- Quản lý kho: theo dõi nhập xuất hàng hóa, cảnh báo tồn kho và kiểm soát tiêu hao giữa các điểm bán.
- Quản lý nhân sự: phân ca, chấm công, kiểm soát vai trò và trách nhiệm của từng nhóm nhân viên.
- Báo cáo doanh thu: tổng hợp doanh thu theo ngày, tháng, năm và theo chi nhánh để phục vụ điều hành.

### 1.3. Đối tượng sử dụng

Hệ thống hướng đến năm nhóm người dùng chính: khách hàng, nhân viên lễ tân, nhân viên phục vụ, quản lý chi nhánh và chủ doanh nghiệp.

Điểm đáng chú ý là cấu trúc người dùng này phản ánh đúng chuỗi giá trị vận hành của mô hình karaoke. Khách hàng cần trải nghiệm đặt chỗ và sử dụng dịch vụ thuận tiện; lễ tân cần điều phối phòng nhanh; phục vụ cần thao tác order ít sai sót; quản lý chi nhánh cần nhìn được dòng vận hành trong ngày; còn chủ doanh nghiệp cần dữ liệu tổng hợp để ra quyết định ở cấp chuỗi.

### 1.4. Kiến trúc và định hướng triển khai

Kiến trúc được triển khai theo mô hình MVC 3 tầng, gồm lớp giao diện với React.js cho web và React Native cho ứng dụng di động, lớp xử lý nghiệp vụ bằng Node.js/Express, cùng lớp dữ liệu sử dụng PostgreSQL kết hợp Redis; ngoài ra còn đặt mục tiêu cho mỗi chi nhánh có thể hoạt động offline và đồng bộ khi có mạng.

Trong vận hành karaoke, trạng thái phòng và order thay đổi liên tục theo thời gian thực; vì vậy một kiến trúc tách lớp rõ ràng giúp hệ thống dễ mở rộng khi thêm chi nhánh, còn cơ chế đồng bộ giúp giảm phụ thuộc tuyệt đối vào đường truyền. Nói cách khác, kiến trúc ở đây không chỉ để xây được phần mềm mà để giữ cho quán vẫn vận hành được khi tải tăng, ca cao điểm xảy ra hoặc mạng không ổn định.

### 1.5. Lý do lựa chọn đề tài

Lý do lựa chọn hệ thống này có thể làm rõ ở ba lớp.

Thứ nhất, đây là bài toán có độ thực tiễn cao vì nó chạm đúng các điểm nghẽn phổ biến của quán karaoke: tính tiền theo giờ phải chính xác, quản lý phòng phải trực quan, order phải chuyển nhanh, kiểm soát thất thoát phải chặt và báo cáo phải đủ nhanh để người quản lý xử lý ngay trong ngày.

Thứ hai, hệ thống có chiều sâu nghiệp vụ hơn nhiều mô hình bán hàng thông thường. Một quán karaoke không chỉ bán hàng hóa mà đồng thời bán thời gian sử dụng dịch vụ, không gian phòng, chất lượng phục vụ và các dịch vụ gia tăng. Vì vậy đây là đề tài phù hợp để thể hiện tư duy phân tích hệ thống, mô hình hóa actor, use case và thiết kế quy trình phần mềm theo Unified Process.

Thứ ba, đề tài có giá trị mở rộng. Nếu chỉ xây cho một quán đơn lẻ, hệ thống dừng ở mức phần mềm tính tiền; nhưng khi mở rộng lên chuỗi, bài toán lập tức chuyển thành quản trị tập trung, đồng bộ dữ liệu, phân quyền đa vai trò và báo cáo đa chi nhánh. Chính yếu tố này làm cho đề tài có chiều sâu đủ lớn để làm báo cáo môn học mà vẫn giữ liên hệ sát với thực tiễn kinh doanh.

Điều quan trọng nhất là hệ thống này không nên được nhìn như một phần mềm tính tiền karaoke, mà nên được nhìn như hạ tầng vận hành số cho chuỗi karaoke. Các trang giới thiệu của KiotViet, POS365 và Sapo đều nhấn mạnh những nhu cầu rất thực như theo dõi phòng trống, tính tiền theo giờ, quản lý hàng hóa, báo cáo doanh thu, order trên nhiều thiết bị và quản lý từ xa; điều đó cho thấy thị trường đang coi quản lý karaoke là một bài toán vận hành tổng thể chứ không còn là bài toán thu ngân đơn lẻ.

## 2. Khảo sát hệ thống tương tự

### 2.1. Mục tiêu khảo sát

Mục tiêu của phần khảo sát là xác định các hệ thống gần nhất với bài toán quản lý karaoke, từ đó chỉ ra những gì thị trường đã giải quyết tốt, những khoảng trống còn tồn tại và vị trí hợp lý cho hệ thống đề xuất của nhóm.

### 2.2. Hệ thống 1: KiotViet

Trang sản phẩm cho karaoke của KiotViet cho biết hệ thống hỗ trợ quản lý phòng bàn, hiển thị chi tiết phòng trống, phòng đang order hoặc đang sử dụng, tính tiền theo giờ, quản lý hàng hóa, quản lý khách hàng, theo dõi nhân viên, kết nối máy in và két tiền, đồng thời có thể dùng trên POS, máy tính, điện thoại và máy tính bảng.

Liên hệ thực tiễn cho thấy KiotViet phù hợp với mô hình quán muốn chuẩn hóa thao tác thu ngân và vận hành cơ bản thật nhanh. Điểm mạnh của KiotViet là biến các nghiệp vụ hay bị thủ công hóa như check giờ vào ra, theo dõi trạng thái phòng và lưu lịch sử khách thành các thao tác có cấu trúc. Tuy nhiên, nội dung công bố hiện tại cho thấy trọng tâm của KiotViet vẫn nghiêng về tối ưu quản lý tại điểm bán hơn là mô tả sâu bài toán chuỗi karaoke nhiều chi nhánh với cơ chế đồng bộ nghiệp vụ phức tạp.

### 2.3. Hệ thống 2: POS365

Các trang của POS365 mô tả phần mềm karaoke theo hướng quản lý phòng, thời gian thuê, tính tiền, quản lý hàng hóa, cảnh báo tồn kho, phân quyền nhân viên, báo cáo doanh thu và quản lý từ xa. POS365 cũng tự giới thiệu là giải pháp ứng dụng điện toán đám mây cho quản lý quán karaoke.

Về mặt thực tiễn, POS365 phản ánh khá rõ nhu cầu của các quán karaoke đang muốn vận hành bài bản hơn: phải có kiểm soát tồn kho, phải có báo cáo nhanh, phải có phân quyền và phải theo dõi phòng đang trống hay đang sử dụng trên nhiều thiết bị. Điều này cho thấy khi quán vượt khỏi quy mô nhỏ, bài toán quản lý karaoke bắt đầu hội tụ với bài toán vận hành F&B và POS hiện đại. Tuy vậy, phần công bố công khai vẫn chủ yếu nhấn mạnh quản lý vận hành và báo cáo, chưa cho thấy rõ một cấu trúc dành riêng cho quản lý chuỗi karaoke theo kiến trúc tập trung như mục tiêu của đề tài.

### 2.4. Hệ thống 3: Sapo

Trang sản phẩm karaoke của Sapo cho biết hệ thống hỗ trợ theo dõi số lượng phòng bàn trống, phòng đặt trước hoặc đang sử dụng, order qua tablet và điện thoại, tự động gửi order tới quầy bar, lưu và phân loại khách hàng để triển khai tích điểm hoặc khuyến mãi, đồng thời hỗ trợ theo dõi nhân viên và phân ca làm việc.

Liên hệ thực tiễn ở đây khá rõ: Sapo tiếp cận karaoke như một biến thể của vận hành dịch vụ có bàn, có phòng, có order và có chăm sóc khách hàng. Cách tiếp cận này phù hợp với các quán karaoke đang muốn số hóa nhanh mà không cần đầu tư hệ thống quá đặc thù. Tuy nhiên, chính vì tiếp cận theo hướng nền tảng quản lý bán hàng mở rộng, Sapo phù hợp hơn với bài toán quản trị dịch vụ tại cửa hàng hơn là bài toán thiết kế một hệ thống chuyên biệt cho chuỗi karaoke với nhiều lớp điều phối dữ liệu.

### 2.5. Bài tổng hợp thị trường dùng để đối chiếu

Bài tổng hợp của POS365 liệt kê nhiều phần mềm quản lý karaoke như POS365, KiotViet, Vietbill, OXU và Sapo, đồng thời mô tả một số tính năng phổ biến như quản lý phòng đặt trước, thống kê phòng trống, tính tiền phụ thu, tính tiền theo block và hỗ trợ nhiều thiết bị.

Dù đây là nguồn mang tính marketing, nó vẫn có giá trị tham khảo vì cho thấy cách thị trường Việt Nam đang đóng gói nhu cầu quản lý karaoke thành một cụm tính năng tương đối ổn định. Cụm tính năng đó gồm ba lớp rõ rệt: vận hành phòng, xử lý order và thanh toán, theo dõi khách hàng và báo cáo.

### 2.6. So sánh đối chiếu

Từ đây, ta có thể đúc kết được ba điều:

Thứ nhất là thị trường đã chuẩn hóa khá rõ bộ tính năng tối thiểu cho phần mềm karaoke. Dù là KiotViet, POS365 hay Sapo, các trang giới thiệu đều xoay quanh bốn việc cốt lõi: nhìn được trạng thái phòng, tính tiền theo giờ, xử lý order trên nhiều thiết bị và theo dõi khách hàng hoặc doanh thu.

Thứ hai là phần lớn giải pháp đang tiếp cận karaoke từ góc độ phần mềm quản lý bán hàng hoặc POS mở rộng. Điều đó giúp triển khai nhanh, nhưng cũng tạo ra khoảng trống cho một hệ thống được thiết kế từ đầu cho mô hình chuỗi karaoke, nơi đồng bộ dữ liệu, phân quyền nhiều lớp và báo cáo liên chi nhánh là yêu cầu trung tâm chứ không phải tính năng mở rộng.

Thứ ba là bài toán thực tế của karaoke không dừng ở thanh toán. Nếu chỉ giải quyết thu ngân, thị trường đã có nhiều lựa chọn. Giá trị khác biệt chỉ xuất hiện khi hệ thống gắn được đặt phòng, vận hành phòng, phục vụ, kho, hội viên và báo cáo vào một dòng dữ liệu thống nhất. Đây chính là chỗ đề tài của nhóm có thể đứng riêng so với các phần mềm thiên về POS thuần túy.

## 3. Tiểu kết

Hệ thống được lựa chọn trong đề tài là Hệ thống Quản lý Tập trung Chuỗi Nhà hàng Karaoke. Đây không chỉ là một phần mềm tính tiền hay quản lý phòng hát, mà là một nền tảng hỗ trợ vận hành toàn bộ chuỗi nghiệp vụ của mô hình karaoke, bao gồm đặt phòng, phục vụ, gọi món, quản lý hội viên, quản lý kho, quản lý nhân sự và báo cáo doanh thu.

Việc lựa chọn đề tài này xuất phát từ nhu cầu thực tế của ngành karaoke hiện nay. Các giải pháp đang được thị trường cung cấp như KiotViet, POS365 và Sapo đều tập trung giải quyết những vấn đề rất cụ thể như theo dõi trạng thái phòng, tính tiền theo giờ, order trên nhiều thiết bị, quản lý khách hàng và theo dõi doanh thu từ xa, cho thấy hoạt động karaoke đã và đang được số hóa theo hướng ngày càng bài bản hơn.

Tuy vậy, phần lớn các hệ thống thương mại hiện có được tiếp cận theo hướng phần mềm bán hàng hoặc POS mở rộng cho karaoke. Trong khi đó, hệ thống của đề tài hướng đến bài toán rộng hơn là quản lý tập trung cho mô hình chuỗi, nơi dữ liệu phải được đồng bộ giữa nhiều vai trò người dùng và nhiều chi nhánh.

## 4. Nguồn tham khảo

Kioviet:
- https://www.kiotviet.vn/phan-mem-tinh-tien-quan-karaoke/
- https://www.kiotviet.vn

POS365:
- https://www.pos365.vn/nganh-nghe/phan-mem-quan-ly-quan-karaoke
- https://www.pos365.vn/quan-ly-quan-karaoke-6405.html
- https://www.pos365.vn/huong-dan-nghiep-vu-chinh-quan-ly-quan-karaoke-4066.html

Sapo:
- https://www.sapo.vn/phan-mem-quan-ly-quan-karaoke.html
- https://www.sapo.vn


# PHẦN II. XÁC ĐỊNH YÊU CẦU

Hệ thống Quản lý Chuỗi Nhà hàng Karaoke

## 1. Bảng thuật ngữ

Bảng thuật ngữ dưới đây định nghĩa các khái niệm nghiệp vụ chính trong hệ thống quản lý chuỗi nhà hàng karaoke, giúp toàn nhóm phát triển hiểu thống nhất các thuật ngữ sử dụng trong tài liệu.

<!-- TABLE: bảng thuật ngữ — dán bảng từ Google Docs vào đây -->

## 2. Mô hình nghiệp vụ bằng ngôn ngữ tự nhiên

### 2.1. Mục tiêu và phạm vi hệ thống

**Mục tiêu:** Xây dựng hệ thống phần mềm quản lý tập trung cho chuỗi nhà hàng karaoke, cho phép quản lý đặt phòng, gọi món, thanh toán, nhân sự, kho hàng và báo cáo doanh thu trên nhiều chi nhánh.

**Phạm vi:** Hệ thống bao phủ toàn bộ quy trình vận hành từ khi khách hàng đặt phòng đến khi thanh toán, đồng thời hỗ trợ quản lý nội bộ (nhân sự, kho, báo cáo) cho từng chi nhánh và toàn chuỗi. Hệ thống được triển khai trên nền tảng web và ứng dụng di động, phục vụ cả người dùng bên ngoài (khách hàng) lẫn người dùng nội bộ (nhân viên, quản lý, chủ doanh nghiệp).

### 2.2. Ai có thể sử dụng phần mềm?

Hệ thống phục vụ 5 nhóm người dùng chính:

**Khách hàng** là nhóm người dùng bên ngoài, sử dụng web hoặc ứng dụng di động để đặt phòng trực tuyến, theo dõi lịch sử sử dụng, quản lý điểm thưởng hội viên và tương tác dịch vụ trực tiếp khi đang ở phòng hát.

**Nhân viên lễ tân** là người dùng nội bộ tại quầy tiếp tân của mỗi chi nhánh. Họ trực tiếp xử lý các thao tác đặt phòng walk-in, thực hiện check-in/check-out, tổng hợp hóa đơn và thu tiền của khách, đồng thời kiểm kê hàng hóa tại quầy.

**Nhân viên phục vụ** là người dùng nội bộ sử dụng thiết bị tablet hoặc ứng dụng di động để tiếp nhận order gọi món từ các phòng, chuyển yêu cầu đến bếp/bar, theo dõi và cập nhật trạng thái phục vụ, đồng thời báo cáo tình trạng hàng hóa và cơ sở vật chất trong phòng.

**Quản lý chi nhánh** là người dùng nội bộ phụ trách điều hành toàn bộ một chi nhánh: phân ca làm việc cho nhân viên, theo dõi chấm công, đánh giá hiệu suất, quản lý kho hàng, xem thông tin khách hàng của chi nhánh và xem báo cáo doanh thu chi nhánh.

**Chủ doanh nghiệp** là người dùng cấp cao nhất, có quyền quản lý toàn bộ chuỗi karaoke: thêm/sửa/xóa chi nhánh, quản lý danh mục chung (menu, bảng giá phòng, chương trình khuyến mãi), quản lý toàn bộ danh sách khách hàng, cấu hình hạng hội viên, quản lý phòng hát và xem báo cáo tổng hợp toàn chuỗi.

### 2.3. Người dùng có những chức năng gì?

**Khách hàng**

- Đặt phòng trực tuyến hoặc trực tiếp tại chi nhánh.
- Quản lý thông tin cá nhân (tên, số điện thoại, hạng hội viên).
- Tương tác dịch vụ trong phòng: gọi món qua app hoặc điện thoại nội bộ, yêu cầu dịch vụ bổ sung.

**Nhân viên lễ tân**

- Quản lý đặt phòng: xếp phòng walk-in, xác nhận check-in booking online, tra cứu và tìm kiếm booking.
- Quản lý trả phòng: tính tiền phòng, tổng hợp order, áp dụng ưu đãi hội viên/voucher, thu tiền, in hóa đơn.
- Kiểm kê hàng tại quầy: đếm số lượng thực tế, tạo phiếu kiểm kê, báo cáo chênh lệch tồn kho.

**Nhân viên phục vụ**

- Quản lý order: nhận yêu cầu gọi món từ phòng (qua app hoặc điện thoại), chuyển bếp/bar, cập nhật trạng thái giao hàng, hủy hoặc thay đổi order.
- Báo cáo tình trạng hàng hóa: kiểm tra cơ sở vật chất phòng sau mỗi lượt, cập nhật trạng thái phòng, báo hỏng hóc thiết bị, yêu cầu bổ sung minibar.

**Quản lý chi nhánh**

- Quản lý nhân viên chi nhánh: phân ca làm việc, theo dõi chấm công thực tế, đánh giá hiệu suất, thực hiện khen thưởng hoặc kỷ luật.
- Quản lý kho: theo dõi nhập/xuất, duyệt phiếu nhập hàng, gửi đơn mua hàng, hủy hàng, đối soát tồn kho.
- Xem thông tin khách hàng của chi nhánh: tra cứu danh sách và lịch sử sử dụng của khách hàng tại chi nhánh mình.
- Báo cáo số liệu: doanh thu, công suất phòng, số lượng khách, doanh số bán hàng theo ngày/tuần/tháng/quý/năm; xuất báo cáo.
- Quản lý phòng hát tại chi nhánh: thêm phòng mới (áp dụng theo loại phòng chuẩn), cập nhật trạng thái (trống, bảo trì...) và xóa các phòng vật lý.

**Chủ doanh nghiệp (Admin)**

- Quản lý hệ thống chi nhánh: thêm, cập nhật, xóa chi nhánh; xem toàn bộ danh sách chi nhánh.
- Quản lý danh mục chung: menu món ăn/đồ uống, bảng giá phòng theo loại và khung giờ, chương trình khuyến mãi.
- Quản lý danh mục loại phòng: định nghĩa các loại phòng chuẩn (Standard, VIP...), cấu hình mức sức chứa và bảng giá chung cho toàn hệ thống.
- Quản lý khách hàng toàn hệ thống: xem/tìm kiếm khách hàng toàn chuỗi, xem lịch sử sử dụng, khóa tài khoản nếu cần.
- Quản lý hạng hội viên: cấu hình điều kiện nâng hạng và ưu đãi theo hạng (rule hệ thống); thay đổi hạng thủ công cho khách hàng cụ thể khi cần.
- Quản lý tài khoản nhân viên: tạo tài khoản mới, phân quyền, khóa/mở tài khoản, reset mật khẩu.
- Tổng hợp báo cáo: so sánh hiệu suất chi nhánh, doanh thu toàn chuỗi, xuất file báo cáo.

### 2.4. Mỗi chức năng hoạt động như thế nào?

**UC01 – Đăng nhập**

Người dùng nhập SĐT/Email và mật khẩu → Hệ thống xác thực thông tin đăng nhập → Hệ thống tạo phiên đăng nhập → Hệ thống chuyển người dùng đến trang chủ tương ứng vai trò.

Người dùng nhập sai mật khẩu → Hệ thống thông báo lỗi xác thực → Người dùng nhập lại (tối đa 5 lần).

Tài khoản bị khóa → Hệ thống hiển thị thông báo tài khoản bị khóa → Người dùng liên hệ Admin.

---

**UC02 – Đăng ký**

Khách hàng nhập Họ tên, SĐT, Email, Mật khẩu → Hệ thống kiểm tra SĐT và Email chưa tồn tại → Hệ thống gửi mã OTP đến SĐT → Khách hàng nhập mã OTP → Hệ thống xác minh OTP hợp lệ → Hệ thống tạo tài khoản hạng "Thường" → Hệ thống tự động đăng nhập.

SĐT hoặc Email đã tồn tại → Hệ thống thông báo trùng lặp → Khách hàng dùng thông tin khác hoặc chọn Đăng nhập.

OTP sai hoặc hết hạn (5 phút) → Hệ thống thông báo lỗi OTP → Khách hàng yêu cầu gửi lại OTP.

---

**UC03 – Đổi mật khẩu**

Người dùng nhập mật khẩu hiện tại và mật khẩu mới → Hệ thống xác minh mật khẩu hiện tại đúng → Hệ thống kiểm tra mật khẩu mới hợp lệ → Hệ thống cập nhật mật khẩu → Hệ thống thu hồi tất cả phiên đăng nhập khác.

Mật khẩu hiện tại không đúng → Hệ thống thông báo lỗi → Người dùng thử lại.

Mật khẩu mới không hợp lệ → Hệ thống hiển thị yêu cầu định dạng → Người dùng nhập lại.

---

**UC04 – Quản lý thông tin cá nhân**

Khách hàng xem hồ sơ cá nhân (Họ tên, SĐT, Email, Hạng hội viên, Điểm tích lũy) → Khách hàng chỉnh sửa Họ tên hoặc Email → Hệ thống kiểm tra Email chưa tồn tại → Hệ thống cập nhật hồ sơ → Hệ thống hiển thị thông báo thành công.

---

**UC05 – Đặt phòng**

*Đặt phòng trực tuyến:*
Khách hàng đăng nhập → Khách hàng chọn chi nhánh và khung giờ → Hệ thống hiển thị danh sách phòng trống → Khách hàng chọn phòng và xác nhận → Hệ thống ghi nhận booking trạng thái "Chờ nhận" → Hệ thống gửi thông báo xác nhận đến khách hàng.

*Đặt phòng tại chi nhánh:*
Khách hàng đến chi nhánh → Lễ tân tra cứu phòng trống theo khung giờ → Lễ tân ghi nhận thông tin khách (hoặc tra cứu hội viên qua SĐT) → Lễ tân chọn phòng và xác nhận với khách → Hệ thống tạo booking trạng thái "Chờ nhận".

*Hủy phòng trực tuyến:*
Khách hàng chọn booking cần hủy → Khách hàng bấm Hủy đặt phòng → Hệ thống yêu cầu xác nhận → Khách hàng xác nhận → Hệ thống chuyển trạng thái booking sang "Đã hủy" → Hệ thống giải phóng slot phòng.

*Hủy phòng tại chi nhánh:*
Khách hàng yêu cầu hủy trực tiếp → Lễ tân tra cứu booking → Lễ tân xác nhận hủy trên hệ thống → Hệ thống chuyển trạng thái sang "Đã hủy" → Hệ thống ghi nhận không hoàn tiền cọc.

---

**UC06 – Gọi món / Quản lý order**

*Tạo order:*
Khách hàng yêu cầu gọi món → Nhân viên phục vụ mở hệ thống, chọn phòng tương ứng → Nhân viên thêm các món vào order → Nhân viên gửi order → Hệ thống ghi nhận order và thông báo đến bếp/bar.

*Cập nhật hoặc hủy order (trước khi bếp xử lý):*
Nhân viên chọn order cần thay đổi → Nhân viên sửa số lượng hoặc hủy món → Hệ thống cập nhật order → Hệ thống thông báo lại bếp/bar.

*Giao món và ghi nhận:*
Nhân viên mang đồ đến phòng → Nhân viên cập nhật trạng thái order sang "Đã giao" → Hệ thống tự động ghi chi tiết order vào hóa đơn phòng.

---

**UC07 – Quản lý đặt phòng (check-in)**

Khách hàng đến nhận phòng → Lễ tân tra cứu booking theo tên/SĐT → Lễ tân xác nhận đúng thông tin khách và phòng → Hệ thống chuyển trạng thái booking từ "Chờ nhận" sang "Đang hoạt động" → Hệ thống ghi nhận thời gian check-in thực tế.

---

**UC08 – Quản lý trả phòng (check-out)**

Khách hàng yêu cầu trả phòng → Lễ tân chọn phòng trên hệ thống → Hệ thống tính tiền phòng (giờ thực tế × đơn giá) cộng tổng tiền order → Lễ tân áp dụng ưu đãi hoặc voucher nếu khách là hội viên → Hệ thống hiển thị tổng tiền → Khách hàng thanh toán (tiền mặt / chuyển khoản) → Lễ tân in hóa đơn → Hệ thống đóng phòng, chuyển trạng thái về "Trống" → Hệ thống cộng điểm hội viên tự động.

---

**UC10 – Báo cáo tình trạng hàng hóa**

Sau mỗi lượt phục vụ, nhân viên phục vụ chọn phòng vừa phục vụ trên hệ thống → Nhân viên kiểm tra cơ sở vật chất trong phòng → Nhân viên cập nhật trạng thái phòng → Nếu phát hiện thiết bị hỏng, nhân viên tạo phiếu báo hỏng hóc → Nếu minibar cần bổ sung, nhân viên gửi yêu cầu bổ sung → Hệ thống ghi nhận và thông báo đến Quản lý chi nhánh.

---

**UC11 – Quản lý nhân viên chi nhánh**

Quản lý chi nhánh xem danh sách nhân viên của chi nhánh → Quản lý phân ca làm việc cho nhân viên theo ngày/tuần → Hệ thống ghi nhận lịch ca và chấm công thực tế → Quản lý đánh giá hiệu suất định kỳ → Quản lý thực hiện khen thưởng hoặc kỷ luật → Hệ thống lưu kết quả phân ca, đánh giá và quyết định.

---

**UC12 – Quản lý kho**

Quản lý chi nhánh theo dõi tồn kho trên hệ thống → Khi hàng sắp hết, hệ thống cảnh báo tự động → Quản lý duyệt phiếu nhập hàng hoặc gửi đơn mua hàng → Hàng về, nhân viên kiểm nhận và tạo phiếu nhập → Hệ thống cập nhật số lượng tồn kho → Khi phục vụ order, hệ thống tự động trừ tồn kho tương ứng.

---

**UC13 – Báo cáo số liệu chi nhánh**

Quản lý chi nhánh chọn chức năng báo cáo → Quản lý chọn kỳ báo cáo (ngày/tuần/tháng/quý/năm) → Hệ thống tổng hợp doanh thu, công suất phòng, lượng khách và doanh số bán hàng → Hệ thống hiển thị số liệu dạng bảng và biểu đồ → Quản lý xuất báo cáo ra file Excel/PDF.

---

**UC14 – Xem thông tin khách hàng chi nhánh**

Quản lý chi nhánh nhập từ khóa tìm kiếm (tên hoặc SĐT) → Hệ thống truy vấn danh sách khách hàng của chi nhánh → Hệ thống hiển thị danh sách kết quả → Quản lý chọn một khách hàng → Hệ thống hiển thị lịch sử sử dụng và điểm tích lũy.

---

**UC15 – Quản lý menu**

*Xem và lọc menu:*
Quản lý chi nhánh chọn chức năng quản lý menu → Hệ thống hiển thị danh sách món ăn/đồ uống → Quản lý lọc theo danh mục → Hệ thống hiển thị danh sách đã lọc.

*Thêm hoặc sửa món:*
Quản lý chọn Thêm mới hoặc Sửa → Hệ thống hiển thị form (Tên món, Loại, Đơn giá, Mô tả, Trạng thái) → Quản lý nhập thông tin → Hệ thống kiểm tra dữ liệu hợp lệ → Hệ thống lưu và làm mới danh sách.

*Ẩn hoặc xóa món:*
Quản lý chọn món cần xóa hoặc ẩn → Hệ thống hiển thị xác nhận → Quản lý xác nhận → Hệ thống cập nhật trạng thái "Ngừng kinh doanh" hoặc xóa khỏi danh mục.

---

**UC16 – Quản lý hệ thống chi nhánh**

Admin chọn chức năng quản lý chi nhánh → Hệ thống hiển thị danh sách chi nhánh → Admin chọn Thêm mới, Sửa hoặc Xóa → Hệ thống hiển thị form nhập liệu (Thêm/Sửa) hoặc popup xác nhận (Xóa) → Admin nhập thông tin hoặc xác nhận → Hệ thống kiểm tra ràng buộc (không xóa chi nhánh đang hoạt động) → Hệ thống cập nhật CSDL và làm mới danh sách.

---

**UC17 – Quản lý khách hàng toàn hệ thống**

Admin nhập từ khóa và tìm kiếm → Hệ thống hiển thị danh sách kết quả toàn chuỗi → Admin chọn Xem chi tiết hoặc Khóa tài khoản → Hệ thống truy xuất lịch sử đặt phòng (nếu xem) hoặc yêu cầu xác nhận (nếu khóa) → Admin thực hiện thao tác → Hệ thống cập nhật trạng thái tài khoản.

---

**UC18 – Quản lý hạng hội viên**

Admin xem danh sách cấu hình các hạng (Thường/Bạc/Vàng) → Admin chọn Sửa cấu hình ngưỡng điểm/ưu đãi hoặc Thay đổi hạng thủ công cho khách hàng → Hệ thống hiển thị form tương ứng → Admin thay đổi thông số hoặc chọn khách hàng và hạng mới → Admin xác nhận → Hệ thống kiểm tra tính hợp lệ → Hệ thống cập nhật CSDL.

---

**UC19 – Quản lý phòng hát**

*Quản lý danh mục loại phòng (Admin):*
Admin chọn chức năng quản lý loại phòng → Hệ thống hiển thị danh mục loại phòng chuẩn → Admin chọn Thêm mới, Sửa hoặc Xóa → Hệ thống hiển thị form (Tên loại, Sức chứa, Giá chung) hoặc xác nhận xóa → Admin nhập thông tin hoặc xác nhận → Hệ thống kiểm tra ràng buộc (không xóa loại đang được chi nhánh sử dụng) → Hệ thống cập nhật tiêu chuẩn phòng toàn hệ thống.

*Quản lý phòng vật lý tại chi nhánh (Quản lý chi nhánh):*
Quản lý chọn chức năng quản lý phòng của chi nhánh → Hệ thống hiển thị danh sách phòng thuộc chi nhánh → Quản lý chọn Thêm mới, Sửa hoặc Xóa → Hệ thống hiển thị form (Tên phòng, Loại phòng) hoặc xác nhận xóa → Quản lý nhập thông tin hoặc xác nhận → Hệ thống kiểm tra ràng buộc (không xóa phòng đang có lịch đặt) → Hệ thống cập nhật CSDL chi nhánh.

---

**UC20 – Quản lý tài khoản nhân viên**

Chủ doanh nghiệp xem danh sách tài khoản nhân viên → Chủ doanh nghiệp tạo tài khoản mới (Họ tên, SĐT, Vai trò, Chi nhánh) → Hệ thống tạo tài khoản và mã hóa mật khẩu mặc định → Chủ doanh nghiệp gán phân quyền phù hợp với vai trò → Khi cần, Chủ doanh nghiệp khóa, mở hoặc reset mật khẩu tài khoản → Hệ thống cập nhật trạng thái tài khoản.

---

**UC21 – Tổng hợp báo cáo toàn chuỗi**

Chủ doanh nghiệp chọn khoảng thời gian và các chi nhánh cần xem → Hệ thống tổng hợp số liệu toàn chuỗi → Hệ thống hiển thị biểu đồ so sánh hiệu suất giữa các chi nhánh và tổng doanh thu → Chủ doanh nghiệp xuất file báo cáo (Excel/PDF).

### 2.5. Những thông tin/đối tượng mà hệ thống cần xử lý

Hệ thống cần quản lý và xử lý các đối tượng thông tin chính sau:

- **Chi nhánh:** Mã chi nhánh, tên, địa chỉ, số điện thoại.
- **Khách hàng:** Mã khách hàng, họ tên, số điện thoại, địa chỉ, hạng hội viên (Thường/Bạc/Vàng), trạng thái tài khoản.
- **Hạng hội viên:** Mã hạng, tên hạng, ngưỡng điểm tối thiểu, ưu đãi (% giảm giá, điểm thưởng nhân).
- **Nhân viên:** Mã nhân viên, họ tên, vai trò, chi nhánh làm việc, trạng thái (đang làm/nghỉ).
- **Tài khoản:** Mã tài khoản, tên đăng nhập, mật khẩu mã hóa, phân quyền, trạng thái hoạt động.
- **Phòng hát:** Mã phòng, tên phòng, loại phòng, sức chứa, giá theo giờ, trạng thái, thuộc chi nhánh.
- **Dịch vụ/Món ăn:** Mã dịch vụ, tên, loại (đồ ăn/đồ uống/dịch vụ bổ sung), đơn giá, mô tả, trạng thái kinh doanh.
- **Đặt phòng:** Mã booking, khách hàng, phòng, nhân viên lễ tân xử lý, thời gian bắt đầu/kết thúc dự kiến và thực tế, trạng thái (Chờ nhận/Đang sử dụng/Hoàn thành/Đã hủy).
- **Hóa đơn:** Mã hóa đơn, liên kết đặt phòng, tiền phòng, thời gian sử dụng thực tế, tiền dịch vụ, phụ phí, giảm giá, tổng tiền, trạng thái thanh toán, phương thức thanh toán.
- **Chi tiết gọi món:** Mã chi tiết, liên kết hóa đơn, dịch vụ/món ăn, số lượng, nhân viên phục vụ, thời gian gọi, trạng thái (Chờ/Đang chuẩn bị/Đã giao/Đã hủy).
- **Tồn kho:** Mã tồn kho, chi nhánh, dịch vụ/hàng hóa, số lượng tồn, ngưỡng cảnh báo thấp.
- **Phiếu nhập hàng:** Mã phiếu, chi nhánh, danh sách hàng nhập, số lượng, ngày nhập, người duyệt, trạng thái.
- **Ca làm việc:** Mã ca, nhân viên, ngày làm việc, giờ bắt đầu/kết thúc, trạng thái chấm công.
- **Khuyến mãi:** Mã khuyến mãi, tên, loại (voucher/giảm giá %), điều kiện áp dụng, thời hạn hiệu lực.

### 2.6. Quan hệ giữa các đối tượng

Các đối tượng trong hệ thống có mối quan hệ chặt chẽ với nhau:

- Một Chi nhánh có nhiều Phòng hát, nhiều Nhân viên và nhiều bản ghi Tồn kho.
- Một Khách hàng thuộc một Hạng hội viên (Thường/Bạc/Vàng) và có thể có một Tài khoản đăng nhập.
- Một Hạng hội viên định nghĩa ngưỡng điểm và áp dụng cho nhiều Khách hàng.
- Một Nhân viên thuộc một Chi nhánh, có thể có một Tài khoản và có nhiều bản ghi Ca làm việc.
- Một Đặt phòng liên kết với một Phòng hát, một Khách hàng (có thể null nếu walk-in chưa đăng ký) và một Nhân viên lễ tân xử lý.
- Một Đặt phòng tạo ra đúng một Hóa đơn.
- Một Hóa đơn chứa nhiều Chi tiết gọi món. Một Hóa đơn có thể áp dụng một Khuyến mãi.
- Mỗi Chi tiết gọi món tham chiếu đến một Dịch vụ/Món ăn và một Nhân viên phục vụ.
- Tồn kho theo dõi số lượng của mỗi Dịch vụ/Hàng hóa tại mỗi Chi nhánh.
- Một Phiếu nhập hàng thuộc một Chi nhánh và ghi nhận nhiều mặt hàng được nhập.

## 3. Mô hình nghiệp vụ bằng UML

### 3.1. Danh sách Actor

| STT | Actor | Mô tả |
|---|---|---|
| 1 | Khách hàng | Người sử dụng dịch vụ karaoke, truy cập qua web/app để đặt phòng và quản lý tài khoản cá nhân. |
| 2 | Nhân viên lễ tân | Nhân viên tại quầy, xử lý đặt phòng, check-in/check-out và thanh toán. |
| 3 | Nhân viên phục vụ | Nhân viên nhận order gọi món, phục vụ đồ ăn/uống và báo cáo tình trạng hàng hóa trong phòng. |
| 4 | Quản lý chi nhánh | Quản lý một chi nhánh: nhân sự, kho hàng, menu, phòng hát và xem báo cáo hoạt động. |
| 5 | Chủ doanh nghiệp | Chủ sở hữu toàn chuỗi, quản lý chi nhánh, danh mục, khách hàng, hạng hội viên và xem báo cáo tổng hợp. |
| 6 | Thành viên | Actor trừu tượng, là cha của tất cả actor cụ thể trong hệ thống. |
| 7 | Nhân viên | Actor trừu tượng, là cha của NV lễ tân và NV phục vụ. |

### 3.2. Các Use Case cho từng Actor

| Actor | Use Case |
|---|---|
| Thành viên (tổng quát) | UC01 – Đăng nhập |
| | UC03 – Đổi mật khẩu |
| Khách hàng | UC02 – Đăng ký |
| | UC04 – Quản lý thông tin cá nhân |
| | UC05 – Đặt phòng |
| | UC06 – Gọi món / Quản lý order |
| NV lễ tân | UC05 – Đặt phòng |
| | UC07 – Quản lý đặt phòng (check-in) |
| | UC08 – Quản lý trả phòng (check-out) |
| NV phục vụ | UC06 – Gọi món / Quản lý order |
| | UC10 – Báo cáo tình trạng hàng hóa |
| Quản lý chi nhánh | UC11 – Quản lý nhân viên chi nhánh |
| | UC12 – Quản lý kho |
| | UC13 – Báo cáo số liệu chi nhánh |
| | UC14 – Xem thông tin khách hàng chi nhánh |
| | UC15 – Quản lý menu |
| | UC19 – Quản lý phòng hát |
| Chủ doanh nghiệp | UC16 – Quản lý hệ thống chi nhánh |
| | UC17 – Quản lý khách hàng toàn hệ thống |
| | UC18 – Quản lý hạng hội viên |
| | UC19 – Quản lý phòng hát |
| | UC20 – Quản lý tài khoản nhân viên |
| | UC21 – Tổng hợp báo cáo toàn chuỗi |

<!-- DIAGRAM: biểu đồ UC tổng hợp toàn hệ thống — dán ảnh từ Google Docs tab XÁC ĐỊNH YÊU CẦU -->
