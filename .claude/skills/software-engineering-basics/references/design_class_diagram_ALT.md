4. Thiết kế tĩnh: Định nghĩa các thuộc tính, phương thức cho các lớp
và vẽ sơ đồ lớp chi tiết theo mô hình MVC thuần
4.1. Định nghĩa các thuộc tính, phương thức cho các lớp
4.1.1. Các lớp biên (Boundary)
a. Lớp ManagerHomeView
 Thuộc tính:
btnManageShowtime (Thẻ <a>): Click để điều hướng sang trang xem danh
sách suất chiếu
 Phương thức:
doGet(): Tiếp nhận yêu cầu (get) truy cập từ trình duyệt, sau đó điều hướng
sang trang manager-home.jsp để hiển thị giao diện màn hình chính cho Người
quản lý.
b. Lớp ListShowtimeView
 Thuộc tính:
txtSearchMovie (Thẻ <input>): Nhập từ khóa tên phim cần tìm.
txtSearchDate (Thẻ <input>): Nhập ngày chiếu cần tìm.
btnSearchShowtime (Thẻ <button type="submit">): Click để gửi yêu cầu
tìm kiếm.
listShowtime (Thẻ <table>): Hiển thị bảng danh sách suất chiếu.
btnAddShowtime (Thẻ <a>): Click để điều hướng sang trang thêm suất chiếu.
btnUpdateShowtime (Thẻ <a>): Click để điều hướng sang trang cập nhật suất
chiếu.
btnDeleteShowtime (Thẻ <a>): Click để điều hướng sang trang xóa suất
chiếu.
 Phương thức:
doGet(): Tiếp nhận yêu cầu (get), gọi DAO lấy dữ liệu danh sách hoặc tìm
kiếm, sau đó điều hướng sang trang list_showtime.jsp để hiển thị kết quả
c. Lớp AddShowtimeView
 Thuộc tính:
cbxMovie (Thẻ <select>): Chọn bộ phim trong rạp.
cbxRoom (Thẻ <select>): Chọn phòng chiếu trong rạp.
txtDate (Thẻ <input>): Nhập ngày chiếu.
txtBasePrice (Thẻ <input>): Nhập giá vé cơ bản.
txtStatus (Thẻ <input>): Nhập trạng thái suất chiếu.
txtStartTime (Thẻ <input>): Nhập thời gian bắt đầu.
txtEndTime (Thẻ <input>): Nhập thời gian kết thúc.
29
 Phương thức:
doGet(): Tiếp nhận yêu cầu (get), gọi DAO lấy danh sách phim và phòng chiếu
để đổ vào các ô chọn, sau đó điều hướng sang trang add_showtime.jsp để hiển
thị form.
doPost(): Tiếp nhận dữ liệu từ form (post), kiểm tra tính hợp lệ và check trùng
lịch, gọi DAO để lưu suất chiếu mới vào cơ sở dữ liệu và trả về thông báo kết
quả.
d. Lớp UpdateShowtimeView
 Thuộc tính:
cbxMovie (Thẻ <select>): Chọn lại bộ phim.
cbxRoom (Thẻ <select>): Chọn lại phòng chiếu.
txtDate (Thẻ <input>): Nhập ngày chiếu cập nhật.
txtBasePrice (Thẻ <input>): Nhập giá vé cơ bản cập nhật.
txtStatus (Thẻ <input>): Nhập trạng thái suất chiếu cập nhật.
txtStartTime (Thẻ <input>): Nhập thời gian bắt đầu cập nhật.
txtEndTime (Thẻ <input>): Nhập thời gian kết thúc cập nhật.
Phương thức:
doGet(): Tiếp nhận yêu cầu (get) chứa ID suất chiếu, gọi DAO lấy thông tin
suất chiếu hiện tại và danh sách phim/phòng để điền sẵn dữ liệu, sau đó điều
hướng sang trang update_showtime.jsp.
doPost(): Tiếp nhận dữ liệu chỉnh sửa từ form (post), kiểm tra tính hợp lệ và
check trùng lịch, gọi DAO để cập nhật thông tin suất chiếu vào cơ sở dữ liệu và
hiển thị thông báo kết quả.
e. Lớp DeleteShowtimeView
 Thuộc tính:
btnYes (Thẻ <button type="submit">): Click để xác nhận đồng ý xóa suất
chiếu.
btnNo (Thẻ <a>): Click để hủy thao tác xóa và quay lại trang danh sách.
 Phương thức:
doGet(): Tiếp nhận yêu cầu (get) chứa ID suất chiếu, sau đó điều hướng sang
trang delete_showtime.jsp để hiển thị giao diện xác nhận xóa.
doPost(): Tiếp nhận quyết định xác nhận từ form (post), gọi DAO để thực thi
xóa suất chiếu khỏi cơ sở dữ liệu và hiển thị thông báo kết quả.
4.1.2. Các lớp điều khiển (Control)
a. Lớp ShowtimeDAO
 Thuộc tính: 
30
dbCon (Connection): Đối tượng dùng để duy trì kết nối với cơ sở dữ liệu
thông qua JDBC.
 Phương thức:
getAllShowtime(): Truy vấn và trả về danh sách toàn bộ các suất chiếu có
trong cơ sở dữ liệu.
getShowtimeById(): Truy vấn và trả về thông tin chi tiết của một suất chiếu cụ
thể dựa theo ID.
addShowtime(): Thực thi câu lệnh SQL (INSERT) để lưu một suất chiếu mới
vào cơ sở dữ liệu.
updateShowtime(): Thực thi câu lệnh SQL (UPDATE) để lưu các thay đổi của
một suất chiếu.
deleteShowtime(): Thực thi câu lệnh SQL (DELETE) để xóa một suất chiếu
khỏi cơ sở dữ liệu theo ID.
searchShowtime(): Truy vấn và trả về danh sách các suất chiếu được lọc theo
từ khóa (tên phim, ngày chiếu).
hasConflict(): Kiểm tra logic nghiệp vụ xem thời gian của suất chiếu chuẩn bị
thêm/sửa có bị trùng lặp với các suất chiếu khác trong cùng một phòng hay
không.
b. Lớp MovieDAO
 Thuộc tính:
dbCon (Connection): Đối tượng kết nối với cơ sở dữ liệu.
 Phương thức:
getAllMovie(): Truy vấn và trả về danh sách toàn bộ các bộ phim (dùng để đổ
dữ liệu vào dropdown list khi thêm, sửa suất chiếu).
c. Lớp RoomDAO
 Thuộc tính:
dbCon (Connection): Đối tượng kết nối với cơ sở dữ liệu.
 Phương thức:
getAllRoom(): Truy vấn và trả về danh sách toàn bộ phòng chiếu (dùng để đổ
dữ liệu vào dropdown list khi thêm,sửa suất chiếu).
4.1.3. Các lớp thực thể (Entity)
a. Lớp Showtime
 Thuộc tính:
showtimeID (UUID): Mã định danh duy nhất của suất chiếu.
movie (Movie): Đối tượng bộ phim được chiếu.
room (Room): Đối tượng phòng chiếu. 
31
startTime (datetime): Thời gian bắt đầu chiếu.
endTime (datetime): Thời gian kết thúc chiếu.
basePrice (float): Giá vé cơ bản của suất chiếu.
status (string): Trạng thái hiện tại (Ví dụ: Sắp chiếu, đã kết thúc...).
bookings (Booking[]): Danh sách các lượt đặt vé thuộc suất chiếu này.
tickets (Ticket[]): Danh sách các vé cụ thể được phát hành cho suất chiếu.
 Phương thức:
Showtime(): Hàm khởi tạo (constructor).
get(), set(): Các hàm để lấy và cập nhật giá trị cho từng thuộc tính.
b. Lớp Movie
 Thuộc tính:
movieID (UUID): Mã định danh duy nhất của bộ phim.
title (string): Tên bộ phim.
director (string): Tên đạo diễn.
duration (int): Thời lượng phim (tính bằng phút).
releaseDate (date): Ngày phát hành/khởi chiếu.
ageRating (string): Phân loại độ tuổi (VD: P, T13, T18...).
description (string): Mô tả, tóm tắt nội dung phim.
showtimes (Showtime[]): Danh sách các suất chiếu của bộ phim này.
movieGenres (MovieGenre[]): Danh sách các thể loại mà bộ phim thuộc về.
 Phương thức:
Movie(): Hàm khởi tạo (constructor).
get(), set(): Các hàm để lấy và cập nhật giá trị cho từng thuộc tính.
c. Lớp Room
 Thuộc tính:
roomID (int): Mã phòng chiếu.
name (string): Tên phòng chiếu (VD: Phòng 1, Phòng 2).
type (string): Định dạng phòng (VD: 2D, 3D, IMAX).
totalRows (int): Tổng số hàng ghế trong phòng.
totalCols (int): Tổng số cột ghế trong phòng.
seats (Seat[]): Danh sách các ghế ngồi có trong phòng chiếu này.
 Phương thức:
Room(): Hàm khởi tạo (constructor)
get(), set(): Các hàm để lấy và cập nhật giá trị cho từng thuộc tính.