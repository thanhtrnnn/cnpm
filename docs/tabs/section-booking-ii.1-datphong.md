## 1.1. Kịch bản "Đặt phòng tại chi nhánh"

| Use case | Đặt phòng |
|----------|----------|
| Actor | Nhân viên lễ tân, khách hàng |
| Tiền điều kiện | Nhân viên đã đăng nhập vào hệ thống |
| Hậu điều kiện | Hệ thống chuyển trạng thái phòng từ "Trống" sang "Chờ nhận" |
| Kịch bản chính | 1. Nhân viên lễ tân chọn chức năng đặt phòng.<br>2. Hệ thống hiển thị yêu cầu nhập thời gian đặt phòng.<br>3. Nhân viên hỏi khách hàng về thời gian đặt phòng.<br>4. Khách hàng trả lời thời gian muốn đặt phòng.<br>5. Nhân viên nhập thời gian đặt phòng lên hệ thống.<br>6. Hệ thống hiển thị danh sách phòng trống theo thời gian vừa nhập.<br>7. Nhân viên hỏi loại phòng trống mong muốn của khách.<br>8. Khách hàng trả lời.<br>9. Nhân viên chọn phòng trống theo mong muốn của khách hàng.<br>10. Hệ thống yêu cầu nhập thông tin khách hàng.<br>11. Nhân viên hỏi thông tin khách hàng.<br>12. Khách hàng cung cấp thông tin cá nhân (họ tên, SĐT,...) cho nhân viên.<br>13. Nhân viên nhập thông tin khách hàng lên hệ thống.<br>14. Hệ thống hiển thị thông tin khách hàng tương ứng.<br>15. Nhân viên bấm vào thông tin khách hàng tương ứng.<br>16. Hệ thống hiển thị xác nhận đặt phòng.<br>17. Nhân viên bấm xác nhận.<br>18. Hệ thống chuyển trạng thái phòng từ "Trống" sang "Chờ nhận". |
| Ngoại lệ | 6. Hệ thống không hiển thị phòng trống nào theo thời gian muốn đặt phòng.<br>14. Chưa có thông tin khách hàng trong cơ sở dữ liệu.<br>8. Khách hàng không ưng phòng nào cả. |
