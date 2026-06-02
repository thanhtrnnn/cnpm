# MÔ TẢ HỆ THỐNG

Mô tả hệ thống và khảo sát hệ thống tương tự
# 1. Mô tả chung về hệ thống
## 1.1. Bài toán thực tế
Hệ thống được định hướng như một nền tảng quản lý tập trung cho chuỗi nhà hàng karaoke, với mục tiêu giảm sai sót thủ công trong quản lý phòng, gọi món, thanh toán, đồng bộ dữ liệu giữa các chi nhánh, nâng cao trải nghiệm khách hàng qua đặt phòng online và tích điểm thành viên, đồng thời hỗ trợ chủ doanh nghiệp ra quyết định bằng báo cáo doanh thu theo thời gian.
Từ góc nhìn thực tiễn, bài toán này xuất phát từ đặc thù của mô hình karaoke: một phiên phục vụ luôn đi kèm nhiều biến số vận hành cùng lúc như thời gian sử dụng phòng, trạng thái phòng, order đồ ăn thức uống, khuyến mãi khách quen, ca làm của nhân viên và tồn kho tiêu hao. Khi quy mô phát triển từ một cơ sở sang nhiều chi nhánh, các thao tác rời rạc hoặc phụ thuộc ghi chép thủ công rất dễ tạo ra sai lệch doanh thu, nhầm trạng thái phòng và chậm phản hồi cho khách.
## 1.2. Phạm vi chức năng
Hệ thống gồm sáu phân hệ cốt lõi: quản lý đặt phòng, gọi món và dịch vụ, quản lý hội viên, quản lý kho, quản lý nhân sự và báo cáo doanh thu.
Cụ thể hơn, mỗi phân hệ không chỉ là một nhóm tính năng độc lập mà còn tạo thành chuỗi nghiệp vụ xuyên suốt một phiên phục vụ:
Quản lý đặt phòng: tiếp nhận đặt trước, bố trí phòng trực tiếp, theo dõi trạng thái phòng trống, đang dùng hoặc bảo trì.
Gọi món và dịch vụ: nhận order từ phòng, chuyển yêu cầu tới bếp hoặc quầy bar, cập nhật trạng thái món và cộng dồn vào hóa đơn cuối.
Quản lý hội viên: lưu thông tin khách, lịch sử sử dụng, tích điểm và áp dụng ưu đãi.
Quản lý kho: theo dõi nhập xuất hàng hóa, cảnh báo tồn kho và kiểm soát tiêu hao giữa các điểm bán.
Quản lý nhân sự: phân ca, chấm công, kiểm soát vai trò và trách nhiệm của từng nhóm nhân viên.
Báo cáo doanh thu: tổng hợp doanh thu theo ngày, tháng, năm và theo chi nhánh để phục vụ điều hành.
## 1.3. Đối tượng sử dụng
Hệ thống hướng đến năm nhóm người dùng chính: khách hàng, nhân viên lễ tân, nhân viên phục vụ, quản lý chi nhánh và chủ doanh nghiệp.
Điểm đáng chú ý là cấu trúc người dùng này phản ánh đúng chuỗi giá trị vận hành của mô hình karaoke. Khách hàng cần trải nghiệm đặt chỗ và sử dụng dịch vụ thuận tiện; lễ tân cần điều phối phòng nhanh; phục vụ cần thao tác order ít sai sót; quản lý chi nhánh cần nhìn được dòng vận hành trong ngày; còn chủ doanh nghiệp cần dữ liệu tổng hợp để ra quyết định ở cấp chuỗi.
## 1.4. Kiến trúc và định hướng triển khai
Kiến trúc được triển khai theo mô hình MVC 3 tầng, gồm lớp giao diện với React.js cho web và React Native cho ứng dụng di động, lớp xử lý nghiệp vụ bằng Node.js/Express, cùng lớp dữ liệu sử dụng PostgreSQL kết hợp Redis; ngoài ra còn đặt mục tiêu cho mỗi chi nhánh có thể hoạt động offline và đồng bộ khi có mạng.
Trong vận hành karaoke, trạng thái phòng và order thay đổi liên tục theo thời gian thực; vì vậy một kiến trúc tách lớp rõ ràng giúp hệ thống dễ mở rộng khi thêm chi nhánh, còn cơ chế đồng bộ giúp giảm phụ thuộc tuyệt đối vào đường truyền. Nói cách khác, kiến trúc ở đây không chỉ để xây được phần mềm mà để giữ cho quán vẫn vận hành được khi tải tăng, ca cao điểm xảy ra hoặc mạng không ổn định.
## 1.5. Lý do lựa chọn đề tài
Lý do lựa chọn hệ thống này có thể làm rõ ở ba lớp.
Thứ nhất, đây là bài toán có độ thực tiễn cao vì nó chạm đúng các điểm nghẽn phổ biến của quán karaoke: tính tiền theo giờ phải chính xác, quản lý phòng phải trực quan, order phải chuyển nhanh, kiểm soát thất thoát phải chặt và báo cáo phải đủ nhanh để người quản lý xử lý ngay trong ngày.
Thứ hai, hệ thống có chiều sâu nghiệp vụ hơn nhiều mô hình bán hàng thông thường. Một quán karaoke không chỉ bán hàng hóa mà đồng thời bán thời gian sử dụng dịch vụ, không gian phòng, chất lượng phục vụ và các dịch vụ gia tăng. Vì vậy đây là đề tài phù hợp để thể hiện tư duy phân tích hệ thống, mô hình hóa actor, use case và thiết kế quy trình phần mềm theo Unified Process.
Thứ ba, đề tài có giá trị mở rộng. Nếu chỉ xây cho một quán đơn lẻ, hệ thống dừng ở mức phần mềm tính tiền; nhưng khi mở rộng lên chuỗi, bài toán lập tức chuyển thành quản trị tập trung, đồng bộ dữ liệu, phân quyền đa vai trò và báo cáo đa chi nhánh. Chính yếu tố này làm cho đề tài có chiều sâu đủ lớn để làm báo cáo môn học mà vẫn giữ liên hệ sát với thực tiễn kinh doanh.
Điều quan trọng nhất là hệ thống này không nên được nhìn như một phần mềm tính tiền karaoke, mà nên được nhìn như hạ tầng vận hành số cho chuỗi karaoke. Các trang giới thiệu của KiotViet, POS365 và Sapo đều nhấn mạnh những nhu cầu rất thực như theo dõi phòng trống, tính tiền theo giờ, quản lý hàng hóa, báo cáo doanh thu, order trên nhiều thiết bị và quản lý từ xa; điều đó cho thấy thị trường đang coi quản lý karaoke là một bài toán vận hành tổng thể chứ không còn là bài toán thu ngân đơn lẻ.
# 2. Khảo sát hệ thống tương tự
## 2.1. Mục tiêu khảo sát
Mục tiêu của phần khảo sát là xác định các hệ thống gần nhất với bài toán quản lý karaoke, từ đó chỉ ra những gì thị trường đã giải quyết tốt, những khoảng trống còn tồn tại và vị trí hợp lý cho hệ thống đề xuất của nhóm.
## 2.2. Hệ thống 1: KiotViet
Trang sản phẩm cho karaoke của KiotViet cho biết hệ thống hỗ trợ quản lý phòng bàn, hiển thị chi tiết phòng trống, phòng đang order hoặc đang sử dụng, tính tiền theo giờ, quản lý hàng hóa, quản lý khách hàng, theo dõi nhân viên, kết nối máy in và két tiền, đồng thời có thể dùng trên POS, máy tính, điện thoại và máy tính bảng.
Liên hệ thực tiễn cho thấy KiotViet phù hợp với mô hình quán muốn chuẩn hóa thao tác thu ngân và vận hành cơ bản thật nhanh. Điểm mạnh của KiotViet là biến các nghiệp vụ hay bị thủ công hóa như check giờ vào ra, theo dõi trạng thái phòng và lưu lịch sử khách thành các thao tác có cấu trúc. Tuy nhiên, nội dung công bố hiện tại cho thấy trọng tâm của KiotViet vẫn nghiêng về tối ưu quản lý tại điểm bán hơn là mô tả sâu bài toán chuỗi karaoke nhiều chi nhánh với cơ chế đồng bộ nghiệp vụ phức tạp.
## 2.3. Hệ thống 2: POS365
Các trang của POS365 mô tả phần mềm karaoke theo hướng quản lý phòng, thời gian thuê, tính tiền, quản lý hàng hóa, cảnh báo tồn kho, phân quyền nhân viên, báo cáo doanh thu và quản lý từ xa. POS365 cũng tự giới thiệu là giải pháp ứng dụng điện toán đám mây cho quản lý quán karaoke.
Về mặt thực tiễn, POS365 phản ánh khá rõ nhu cầu của các quán karaoke đang muốn vận hành bài bản hơn: phải có kiểm soát tồn kho, phải có báo cáo nhanh, phải có phân quyền và phải theo dõi phòng đang trống hay đang sử dụng trên nhiều thiết bị. Điều này cho thấy khi quán vượt khỏi quy mô nhỏ, bài toán quản lý karaoke bắt đầu hội tụ với bài toán vận hành F&B và POS hiện đại. Tuy vậy, phần công bố công khai vẫn chủ yếu nhấn mạnh quản lý vận hành và báo cáo, chưa cho thấy rõ một cấu trúc dành riêng cho quản lý chuỗi karaoke theo kiến trúc tập trung như mục tiêu của đề tài.
## 2.4. Hệ thống 3: Sapo
Trang sản phẩm karaoke của Sapo cho biết hệ thống hỗ trợ theo dõi số lượng phòng bàn trống, phòng đặt trước hoặc đang sử dụng, order qua tablet và điện thoại, tự động gửi order tới quầy bar, lưu và phân loại khách hàng để triển khai tích điểm hoặc khuyến mãi, đồng thời hỗ trợ theo dõi nhân viên và phân ca làm việc.
Liên hệ thực tiễn ở đây khá rõ: Sapo tiếp cận karaoke như một biến thể của vận hành dịch vụ có bàn, có phòng, có order và có chăm sóc khách hàng. Cách tiếp cận này phù hợp với các quán karaoke đang muốn số hóa nhanh mà không cần đầu tư hệ thống quá đặc thù. Tuy nhiên, chính vì tiếp cận theo hướng nền tảng quản lý bán hàng mở rộng, Sapo phù hợp hơn với bài toán quản trị dịch vụ tại cửa hàng hơn là bài toán thiết kế một hệ thống chuyên biệt cho chuỗi karaoke với nhiều lớp điều phối dữ liệu.
## 2.5. Bài tổng hợp thị trường dùng để đối chiếu
Bài tổng hợp của POS365 liệt kê nhiều phần mềm quản lý karaoke như POS365, KiotViet, Vietbill, OXU và Sapo, đồng thời mô tả một số tính năng phổ biến như quản lý phòng đặt trước, thống kê phòng trống, tính tiền phụ thu, tính tiền theo block và hỗ trợ nhiều thiết bị. <tham khảo tổng hợp>
Dù đây là nguồn mang tính marketing, nó vẫn có giá trị tham khảo vì cho thấy cách thị trường Việt Nam đang đóng gói nhu cầu quản lý karaoke thành một cụm tính năng tương đối ổn định. Cụm tính năng đó gồm ba lớp rõ rệt: vận hành phòng, xử lý order và thanh toán, theo dõi khách hàng và báo cáo.
## 2.6. So sánh đối chiếu

| Tiêu chí | Hệ thống đề xuất của nhóm | KiotViet | POS365 | Sapo |
| --- | --- | --- | --- | --- |
| Trục bài toán | Quản lý tập trung chuỗi karaoke nhiều vai trò người dùng. | Tối ưu quản lý và tính tiền karaoke tại điểm bán. | Quản lý karaoke theo hướng POS, cloud, hàng hóa và báo cáo. | Quản lý karaoke như một bài toán dịch vụ có phòng, order và khách hàng. |
| Quản lý phòng | Có đặt phòng, trạng thái phòng, | Có hiển thị phòng trống, đang order, đang sử dụng. | Có quản lý thời gian thuê và tình trạng phòng. | Có theo dõi phòng trống, phòng đặt trước, phòng đang sử dụng. |
| Order và phục vụ | Có order từ phòng, gửi bếp/bar, đồng bộ hóa đơn. | Có quản lý phòng và tính tiền; nội dung công bố ít nhấn mạnh luồng phục vụ theo vai trò. | Có quản lý hàng hóa, thao tác trên nhiều thiết bị, phục vụ vận hành quán. | Có order qua tablet/điện thoại và gửi order tới quầy bar. |
| Hội viên/khách hàng | Có tích điểm, ưu đãi, lịch sử sử dụng. | Có lưu và phân nhóm thông tin khách hàng, lịch sử giao dịch. | Có quản lý khách hàng trong hệ thống POS karaoke. | Có lưu, phân loại khách hàng và thiết lập tích điểm hoặc khuyến mãi. |
| Quản lý kho | Có nhập/xuất, cảnh báo tồn kho, đồng bộ chi nhánh. | Có quản lý hàng hóa. | Có quản lý hàng hóa, cảnh báo tồn kho, thiết lập định mức tối thiểu. | Chưa thấy công bố chuyên sâu bằng POS365, nhưng gắn với quản lý vận hành tại quán. |
| Báo cáo điều hành | Có báo cáo đa chi nhánh theo ngày/tháng/năm. | Có theo dõi doanh thu, tăng trưởng và quản lý từ xa. | Có báo cáo nhanh, chính xác và quản lý từ xa. | Có theo dõi báo cáo doanh thu, lãi lỗ chi tiết. |
| Phạm vi phù hợp | Chuỗi karaoke cần quản trị tập trung và mở rộng dài hạn. | Quán muốn chuẩn hóa vận hành nhanh với chi phí dễ tiếp cận. | Quán hoặc chuỗi cần mô hình POS quản trị bài bản hơn. | Quán muốn số hóa nhanh trên nền tảng quản lý bán hàng dịch vụ. |

Từ đây, ta có thể đúc kết được ba điều:
Thứ nhất là thị trường đã chuẩn hóa khá rõ bộ tính năng tối thiểu cho phần mềm karaoke. Dù là KiotViet, POS365 hay Sapo, các trang giới thiệu đều xoay quanh bốn việc cốt lõi: nhìn được trạng thái phòng, tính tiền theo giờ, xử lý order trên nhiều thiết bị và theo dõi khách hàng hoặc doanh thu.
Thứ hai là phần lớn giải pháp đang tiếp cận karaoke từ góc độ phần mềm quản lý bán hàng hoặc POS mở rộng. Điều đó giúp triển khai nhanh, nhưng cũng tạo ra khoảng trống cho một hệ thống được thiết kế từ đầu cho mô hình chuỗi karaoke, nơi đồng bộ dữ liệu, phân quyền nhiều lớp và báo cáo liên chi nhánh là yêu cầu trung tâm chứ không phải tính năng mở rộng.
Thứ ba là bài toán thực tế của karaoke không dừng ở thanh toán. Nếu chỉ giải quyết thu ngân, thị trường đã có nhiều lựa chọn. Giá trị khác biệt chỉ xuất hiện khi hệ thống gắn được đặt phòng, vận hành phòng, phục vụ, kho, hội viên và báo cáo vào một dòng dữ liệu thống nhất. Đây chính là chỗ đề tài của nhóm có thể đứng riêng so với các phần mềm thiên về POS thuần túy.
# 3. Tiểu kết
Hệ thống được lựa chọn trong đề tài là Hệ thống Quản lý Tập trung Chuỗi Nhà hàng Karaoke. Đây không chỉ là một phần mềm tính tiền hay quản lý phòng hát, mà là một nền tảng hỗ trợ vận hành toàn bộ chuỗi nghiệp vụ của mô hình karaoke, bao gồm đặt phòng, phục vụ, gọi món, quản lý hội viên, quản lý kho, quản lý nhân sự và báo cáo doanh thu.
Việc lựa chọn đề tài này xuất phát từ nhu cầu thực tế của ngành karaoke hiện nay. Các giải pháp đang được thị trường cung cấp như KiotViet, POS365 và Sapo đều tập trung giải quyết những vấn đề rất cụ thể như theo dõi trạng thái phòng, tính tiền theo giờ, order trên nhiều thiết bị, quản lý khách hàng và theo dõi doanh thu từ xa, cho thấy hoạt động karaoke đã và đang được số hóa theo hướng ngày càng bài bản hơn.
Tuy vậy, phần lớn các hệ thống thương mại hiện có được tiếp cận theo hướng phần mềm bán hàng hoặc POS mở rộng cho karaoke. Trong khi đó, hệ thống của đề tài hướng đến bài toán rộng hơn là quản lý tập trung cho mô hình chuỗi, nơi dữ liệu phải được đồng bộ giữa nhiều vai trò người dùng và nhiều chi nhánh.
# 4. Nguồn tham khảo
Kioviet:
 https://www.kiotviet.vn/phan-mem-tinh-tien-quan-karaoke/
 https://www.kiotviet.vn
Pos365:
 https://www.pos365.vn/nganh-nghe/phan-mem-quan-ly-quan-karaoke
 https://www.pos365.vn/quan-ly-quan-karaoke-6405.html
https://www.pos365.vn/huong-dan-nghiep-vu-chinh-quan-ly-quan-karaoke-4066.html
Sapo:
 https://www.sapo.vn/phan-mem-quan-ly-quan-karaoke.html
https://www.sapo.vn
