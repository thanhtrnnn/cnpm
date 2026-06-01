## II. PHA PHÂN TÍCH

### 1. Kịch bản chuẩn

#### UC01 – Đăng nhập

| Trường | Nội dung |
|---|---|
| **Use case** | Đăng nhập |
| **Actor** | Khách hàng, Nhân viên |
| **Tiền điều kiện** | Người dùng chưa đăng nhập. Tài khoản đã tồn tại trong hệ thống. |
| **Hậu điều kiện** | Người dùng được xác thực, chuyển hướng đến trang chủ. |
| **Kịch bản chính** | 1. Người dùng chọn chức năng "Đăng nhập".<br>2. Hệ thống hiển thị giao diện đăng nhập có ô nhập SĐT/Email, ô nhập Mật khẩu, nút Đăng nhập, liên kết "Quên mật khẩu?" và "Đăng ký".<br>3. Người dùng nhập SĐT/Email và Mật khẩu.<br>4. Người dùng nhấn nút Đăng nhập.<br>5. Hệ thống xác thực thành công, chuyển hướng đến trang chủ và hiển thị thông báo "Đăng nhập thành công". |
| **Ngoại lệ** | 4. Hệ thống thông báo "Tài khoản không tồn tại".<br>4.1 Người dùng chọn liên kết "Đăng ký" (chuyển sang UC02).<br><br>4. Hệ thống thông báo "Sai mật khẩu".<br>4.1 Người dùng nhập lại mật khẩu (quay về Bước 4). |

#### UC02 – Đăng ký

| Trường | Nội dung |
|---|---|
| **Use case** | Đăng ký |
| **Actor** | Khách hàng |
| **Tiền điều kiện** | Người dùng chưa có tài khoản. |
| **Hậu điều kiện** | Tài khoản mới được tạo, đăng nhập tự động. |
| **Kịch bản chính** | 1. Người dùng chọn liên kết "Đăng ký" từ giao diện đăng nhập.<br>2. Hệ thống hiển thị giao diện đăng ký có ô nhập Họ tên, SĐT, Email, Mật khẩu, Xác nhận mật khẩu, nút Tiếp tục.<br>3. Người dùng nhập Họ tên, SĐT, Email, Mật khẩu, Xác nhận mật khẩu.<br>4. Người dùng nhấn nút Tiếp tục.<br>5. Hệ thống kiểm tra thông tin hợp lệ, gửi mã OTP 6 chữ số đến SĐT.<br>6. Hệ thống hiển thị giao diện xác nhận OTP có ô nhập mã OTP, nút Xác nhận, nút Gửi lại mã.<br>7. Người dùng nhập mã OTP và nhấn nút Xác nhận.<br>8. Hệ thống tạo tài khoản mới, tự động đăng nhập và hiển thị thông báo "Đăng ký thành công!". |
| **Ngoại lệ** | 5. Hệ thống thông báo "SĐT hoặc Email đã được sử dụng".<br>5.1 Người dùng nhập lại thông tin khác (quay về Bước 4).<br><br>7. Hệ thống thông báo "Mã OTP không hợp lệ hoặc đã hết hạn".<br>7.1 Người dùng nhấn nút Gửi lại mã (quay về Bước 6). |

#### UC03 – Đổi mật khẩu

| Trường | Nội dung |
|---|---|
| **Use case** | Đổi mật khẩu |
| **Actor** | Khách hàng, Nhân viên (đã đăng nhập) |
| **Tiền điều kiện** | Người dùng đã đăng nhập. |
| **Hậu điều kiện** | Mật khẩu mới được lưu. Tất cả phiên đăng nhập khác bị thu hồi. |
| **Kịch bản chính** | 1. Người dùng chọn chức năng "Đổi mật khẩu".<br>2. Hệ thống hiển thị giao diện có ô nhập Mật khẩu hiện tại, Mật khẩu mới, Xác nhận mật khẩu mới, nút Lưu thay đổi.<br>3. Người dùng nhập Mật khẩu hiện tại, Mật khẩu mới, Xác nhận mật khẩu mới.<br>4. Người dùng nhấn nút Lưu thay đổi.<br>5. Hệ thống cập nhật mật khẩu, thu hồi các phiên khác, hiển thị thông báo "Đổi mật khẩu thành công. Vui lòng đăng nhập lại." và chuyển hướng về giao diện đăng nhập. |
| **Ngoại lệ** | 4. Hệ thống thông báo "Mật khẩu hiện tại không chính xác".<br>4.1 Người dùng nhập lại mật khẩu hiện tại (quay về Bước 4).<br><br>4. Hệ thống thông báo "Mật khẩu mới không hợp lệ".<br>4.1 Người dùng nhập lại mật khẩu mới (quay về Bước 4). |

#### UC04 – Quản lý thông tin cá nhân

| Trường | Nội dung |
|---|---|
| **Use case** | Quản lý thông tin cá nhân |
| **Actor** | Khách hàng (đã đăng nhập) |
| **Tiền điều kiện** | Khách hàng đã đăng nhập. |
| **Hậu điều kiện** | Thông tin cá nhân được cập nhật. |
| **Kịch bản chính** | 1. Khách hàng chọn chức năng "Hồ sơ cá nhân".<br>2. Hệ thống hiển thị trang hồ sơ cá nhân:<br><table><tr><th>Họ tên</th><th>SĐT</th><th>Email</th><th>Hạng hội viên</th><th>Điểm tích lũy</th><th>Ngày tham gia</th></tr><tr><td>Nguyễn Văn A</td><td>0912345678</td><td>nva@gmail.com</td><td>Bạc</td><td>1.250</td><td>15/03/2025</td></tr></table><br>3. Khách hàng nhấn nút Chỉnh sửa.<br>4. Hệ thống chuyển sang chế độ chỉnh sửa: Họ tên và Email cho phép sửa, SĐT bị khóa.<br>5. Khách hàng cập nhật Họ tên và Email.<br>6. Khách hàng nhấn nút Lưu thay đổi.<br>7. Hệ thống hiển thị thông báo "Cập nhật thành công!" và quay về chế độ xem. |
| **Ngoại lệ** | 6. Hệ thống thông báo "Email không hợp lệ hoặc đã được sử dụng".<br>6.1 Khách hàng nhập lại email khác (quay về Bước 6). |

#### UC20 – Quản lý tài khoản nhân viên

| Trường | Nội dung |
|---|---|
| **Use case** | Quản lý tài khoản nhân viên |
| **Actor** | Chủ Doanh nghiệp (Admin) |
| **Tiền điều kiện** | Admin đã đăng nhập với quyền quản lý nhân viên. |
| **Hậu điều kiện** | Tài khoản nhân viên được tạo/sửa/xóa. |
| **Kịch bản chính** | 1. Admin chọn chức năng "Quản lý nhân viên".<br>2. Hệ thống hiển thị danh sách nhân viên:<br><table><tr><th>Họ tên</th><th>Vai trò</th><th>Chi nhánh</th><th>Trạng thái</th></tr><tr><td>Nguyễn Minh Tuấn</td><td>Lễ tân</td><td>Karaoke Star - CN1</td><td>Đang làm</td></tr><tr><td>Trần Thị Hương</td><td>Phục vụ</td><td>Karaoke Star - CN2</td><td>Đang làm</td></tr><tr><td>Lê Văn Khánh</td><td>Quản lý</td><td>Karaoke Star - CN1</td><td>Đang làm</td></tr></table><br>3. Admin nhấn nút Thêm nhân viên.<br>4. Hệ thống hiển thị giao diện nhập Họ tên, SĐT, Vai trò, Chi nhánh.<br>5. Admin nhập thông tin và nhấn nút Lưu.<br>6. Hệ thống kiểm tra thông tin hợp lệ, tạo tài khoản nhân viên mới.<br>7. Hệ thống hiển thị thông báo "Thêm nhân viên thành công!" và cập nhật danh sách.<br>8. Admin nhấn nút Sửa trên dòng nhân viên Nguyễn Minh Tuấn.<br>9. Hệ thống hiển thị giao diện chỉnh sửa với thông tin hiện tại.<br>10. Admin cập nhật thông tin và nhấn nút Lưu.<br>11. Hệ thống hiển thị thông báo "Cập nhật thành công!".<br>12. Admin nhấn nút Xóa trên dòng nhân viên Lê Văn Khánh.<br>13. Hệ thống yêu cầu xác nhận xóa.<br>14. Admin xác nhận xóa, hệ thống hiển thị thông báo "Xóa nhân viên thành công!". |
| **Ngoại lệ** | 6. Hệ thống thông báo "SĐT đã được sử dụng".<br>6.1 Admin nhập lại SĐT khác (quay về Bước 5).<br><br>14. Hệ thống thông báo "Không thể xóa nhân viên đang xử lý order".<br>14.1 Admin hủy thao tác xóa. |

### 2. Mô hình hóa lớp

**Bước 1 – Mô tả chức năng bằng đoạn văn xuôi**

Hệ thống cho phép khách hàng đăng ký tài khoản hội viên mới bằng cách cung cấp họ tên, số điện thoại, email và mật khẩu; sau đó xác minh số điện thoại qua mã OTP trước khi hoàn tất đăng ký. Mỗi tài khoản gắn liền với một hạng hội viên (Thường, Bạc, Vàng, Kim Cương) dựa trên điểm tích lũy. Người dùng sau khi đăng nhập có thể xem và cập nhật thông tin cá nhân như họ tên và email, hoặc thực hiện đổi mật khẩu bằng cách xác minh mật khẩu cũ rồi nhập mật khẩu mới. Hệ thống ghi nhận các phiên đăng nhập để phục vụ bảo mật và thu hồi phiên khi đổi mật khẩu. Ngoài ra, chủ doanh nghiệp có quyền quản lý tài khoản nhân viên: tạo, chỉnh sửa và xóa tài khoản nhân viên trong hệ thống.

**Bước 2 + 3 – Trích danh từ và đánh giá**

▪ Hệ thống → loại: quá chung, không phải thực thể nghiệp vụ
▪ Khách hàng → lớp User: fullName, phoneNumber, email, password, loyaltyPoints, createdAt
▪ Tài khoản → thuộc về User (gộp vào User, tránh tách thừa)
▪ Họ tên → thuộc tính fullName của User
▪ Số điện thoại → thuộc tính phoneNumber của User (dùng làm username đăng nhập)
▪ Email → thuộc tính email của User
▪ Mật khẩu → thuộc tính password của User (lưu dạng mã hóa)
▪ Ngày tham gia → thuộc tính createdAt của User
▪ Hạng hội viên → lớp MembershipTier: tierName, minPoints, description, discountRate
▪ Điểm tích lũy → thuộc tính loyaltyPoints của User
▪ Mã OTP → lớp OTP: otpCode, type, expiresAt, verified
▪ Phiên đăng nhập → lớp LoginSession: sessionToken, loginTime, expiresAt, device
▪ Lịch sử → loại: quá chung → cụ thể là LoginSession đã đủ
▪ Danh sách → loại: không phải thực thể
▪ Giao diện → loại: là Boundary, không phải Entity
▪ Nhân viên → lớp Employee: fullName, role, branch, status
▪ Chủ doanh nghiệp → loại: actor, không phải thực thể dữ liệu

**Bước 4 – Xác định quan hệ số lượng**

▪ 1 User có 1 MembershipTier → User – MembershipTier: n – 1
(nhiều người dùng có thể có cùng hạng)
▪ 1 User có nhiều OTP → User – OTP: 1 – n
(mỗi lần đăng ký/đổi SĐT tạo 1 OTP mới)
▪ 1 User có nhiều LoginSession → User – LoginSession: 1 – n
(người dùng có thể đăng nhập trên nhiều thiết bị)
▪ Employee là lớp độc lập, không có quan hệ với User
(branch là thuộc tính text, không cần tách riêng vì Chi nhánh thuộc module khác)

**Bước 5 – Bổ sung quan hệ**

User gắn composition với OTP: một OTP không tồn tại độc lập nếu không có User tương ứng (khi xóa User thì xóa theo tất cả OTP). Tương tự, LoginSession không tồn tại độc lập khỏi User. Quan hệ với MembershipTier là aggregation: MembershipTier là dữ liệu danh mục tồn tại độc lập với User. Employee là lớp riêng biệt, không kế thừa từ User.

**Biểu đồ thực thể Module Tài khoản & Thành viên:**

<!-- PLACEHOLDER: account_entity_analysis -->

```plantuml
@startuml
skinparam classBackgroundColor #7AD2FF
skinparam classBorderColor #000000
skinparam classFontColor #000000
skinparam linetype ortho
title Biểu đồ thực thể – Module Tài khoản & Thành viên

class User {
  -fullName
  -phoneNumber
  -email
  -password
  -loyaltyPoints
  -createdAt
}
class Employee {
  -fullName
  -role
  -branch
  -status
}
class MembershipTier {
  -tierName
  -minPoints
  -description
  -discountRate
}
class OTP {
  -otpCode
  -type
  -expiresAt
  -verified
}
class LoginSession {
  -sessionToken
  -loginTime
  -expiresAt
  -device
}

User "n" o-- "1" MembershipTier : aggregation
User "1" *-- "n" OTP : composition
User "1" *-- "n" LoginSession : composition
@enduml
```

### 3. Biểu đồ lớp phân tích

**Phân tích chi tiết chức năng "Đăng nhập":**

Người dùng truy cập trang đăng nhập -> đề xuất lớp **LoginView**, có ô nhập SĐT, ô nhập mật khẩu, nút Đăng nhập.

Người dùng nhập SĐT, mật khẩu và nhấn nút Đăng nhập -> hệ thống cần xác thực tài khoản -> cần chức năng `checkLogin()` của đối tượng **User**.

Nếu tài khoản không tồn tại -> hệ thống hiển thị thông báo lỗi.
Nếu mật khẩu sai -> hệ thống hiển thị thông báo lỗi.

Hoàn tất, hệ thống tạo phiên đăng nhập và chuyển hướng trang chủ.

**Boundary:** LoginView
**Entity:** User

**Phân tích chi tiết chức năng "Đăng ký":**

Người dùng truy cập trang đăng ký -> đề xuất lớp **RegisterView**, có ô nhập Họ tên, SĐT, Email, Mật khẩu, Xác nhận MK, nút Tiếp tục.

Người dùng nhập thông tin và nhấn nút Tiếp tục -> hệ thống cần tạo tài khoản mới -> cần chức năng `register()` của đối tượng **User**.

Hệ thống gửi OTP đến SĐT -> đề xuất lớp **OTPVerifyView**, có ô nhập OTP, nút Xác nhận.

Người dùng nhập OTP và nhấn nút Xác nhận -> hệ thống cần xác minh OTP -> cần chức năng `verifyOTP()` của đối tượng **OTP**.

Hoàn tất, hệ thống tạo tài khoản mới và tự động đăng nhập.

**Boundary:** RegisterView, OTPVerifyView
**Entity:** User, OTP

**Phân tích chi tiết chức năng "Đổi mật khẩu":**

Người dùng truy cập trang bảo mật -> đề xuất lớp **ChangePasswordView**, có ô nhập MK hiện tại, MK mới, Xác nhận MK mới, nút Lưu.

Người dùng nhập MK hiện tại, MK mới và nhấn nút Lưu -> hệ thống cần đổi mật khẩu -> cần chức năng `changePassword()` của đối tượng **User**.

Nếu MK hiện tại sai -> hệ thống hiển thị thông báo lỗi.
Nếu MK mới không hợp lệ -> hệ thống hiển thị thông báo lỗi.

Hoàn tất, hệ thống cập nhật mật khẩu mới và thu hồi tất cả phiên đăng nhập khác.

**Boundary:** ChangePasswordView
**Entity:** User

**Phân tích chi tiết chức năng "Quản lý thông tin cá nhân":**

Người dùng nhấn vào ảnh đại diện -> đề xuất lớp **ProfileView**, có hiển thị Họ tên, SĐT, Email, Hạng hội viên, Điểm tích lũy, nút Chỉnh sửa.

Hệ thống cần lấy thông tin hồ sơ -> cần chức năng `getProfile()` của đối tượng **User**.

Người dùng nhấn Chỉnh sửa, sửa thông tin và nhấn Lưu -> hệ thống cần cập nhật hồ sơ -> cần chức năng `updateProfile()` của đối tượng **User**.

Nếu email không hợp lệ hoặc đã được dùng -> hệ thống hiển thị thông báo lỗi.

Hoàn tất, hệ thống cập nhật hồ sơ vào CSDL.

**Boundary:** ProfileView
**Entity:** User

**Phân tích chi tiết chức năng "Quản lý nhân viên":**

Admin truy cập trang quản lý nhân viên -> đề xuất lớp **StaffManageView**, có bảng danh sách nhân viên, nút Thêm, Sửa, Xóa.

Hệ thống cần tải danh sách nhân viên -> cần chức năng `getAllStaff()` của đối tượng **Employee**.

Admin nhấn Thêm, nhập thông tin và nhấn Lưu -> hệ thống cần tạo nhân viên mới -> cần chức năng `addStaff()` của đối tượng **Employee**.

Admin nhấn Sửa trên một dòng, cập nhật và nhấn Lưu -> hệ thống cần cập nhật nhân viên -> cần chức năng `updateStaff()` của đối tượng **Employee**.

Admin nhấn Xóa trên một dòng, xác nhận -> hệ thống cần xóa nhân viên -> cần chức năng `deleteStaff()` của đối tượng **Employee**.

Nếu nhân viên đang xử lý order -> hệ thống hiển thị thông báo lỗi.

Hoàn tất, hệ thống cập nhật danh sách nhân viên.

**Boundary:** StaffManageView
**Entity:** Employee

**Sơ đồ lớp phân tích – Module Tài khoản & Thành viên:**

<!-- PLACEHOLDER: account_class_analysis -->

```plantuml
@startuml
left to right direction
skinparam linetype ortho
skinparam packageStyle rectangle
skinparam packageMaxWidth 800
title Biểu đồ lớp phân tích – Module Tài khoản & Thành viên

skinparam classBackgroundColor #7AD2FF
skinparam classBorderColor #000000
skinparam classFontColor #000000
skinparam packageBackgroundColor #DDEEFF
skinparam packageBorderColor #000000

package "Boundary" #DDEEFF {
  together {
    class LoginView {
      -txtPhoneNumber
      -txtPassword
      -btnLogin
      -lnkForgotPassword
      -lnkRegister
    }
    class RegisterView {
      -txtFullName
      -txtPhoneNumber
      -txtEmail
      -txtPassword
      -txtConfirmPassword
      -btnContinue
    }
    class OTPVerifyView {
      -txtOTP
      -btnConfirm
      -btnResendOTP
    }
    class ChangePasswordView {
      -txtCurrentPassword
      -txtNewPassword
      -txtConfirmNewPassword
      -btnSave
    }
    class ProfileView {
      -lblFullName
      -lblPhoneNumber
      -lblEmail
      -lblMembershipTier
      -lblLoyaltyPoints
      -btnEdit
    }
    class StaffManageView {
      -tblStaffList
      -btnAdd
      -btnEdit
      -btnDelete
    }
  }
}

package "Entity" #FFF3CD {
  together {
    class User {
      -fullName
      -phoneNumber
      -email
      -password
      -loyaltyPoints
      -createdAt
      +checkLogin()
      +register()
      +changePassword()
      +getProfile()
      +updateProfile()
    }
    class Employee {
      -fullName
      -role
      -branch
      -status
      +getAllStaff()
      +addStaff()
      +updateStaff()
      +deleteStaff()
    }
    class MembershipTier {
      -tierName
      -minPoints
      -description
      -discountRate
    }
    class OTP {
      -otpCode
      -type
      -expiresAt
      -verified
      +verifyOTP()
      +sendOTP()
    }
    class LoginSession {
      -sessionToken
      -loginTime
      -expiresAt
      -device
    }
  }
}

' Boundary -> Entity
LoginView --> User
RegisterView --> User
RegisterView --> OTP
OTPVerifyView --> OTP
OTPVerifyView --> User
ChangePasswordView --> User
ProfileView --> User
StaffManageView --> Employee

' Entity relationships
User "n" o-- "1" MembershipTier
User "1" *-- "n" OTP
User "1" *-- "n" LoginSession
@enduml
```

### 4. Biểu đồ tuần tự phân tích

#### UC01 – Đăng nhập (5 bước)

```plantuml
@startuml
skinparam shadowing false
skinparam SequenceMessageAlign left
skinparam SequenceLifeLineBackgroundColor #7AD2FF
skinparam SequenceLifeLineBorderColor #000000
skinparam sequenceParticipantBackgroundColor #7AD2FF
skinparam sequenceParticipantBorderColor #000000
skinparam sequenceParticipantFontColor #000000
skinparam sequenceArrowColor #000000
skinparam sequenceArrowFontColor #000000

<style>
sequenceDiagram {
  Shadowing 0
  RoundCorner 0
  FontName "Arial"
  FontSize 10
  FontColor #000000
  participant { BackgroundColor #7AD2FF LineColor #000000 LineThickness 1 }
  actor { BackgroundColor transparent LineColor #000000 }
  boundary { BackgroundColor #7AD2FF LineColor #000000 }
  control { BackgroundColor #7AD2FF LineColor #000000 }
  entity { BackgroundColor #7AD2FF LineColor #000000 }
  lifeline { LineColor #000000 LineStyle 5-5 }
  arrow { LineColor #000000 LineThickness 1 FontSize 10 }
}
</style>
title Đăng nhập – Tuần tự Phân tích (5 bước)

actor "Người dùng" as Actor
boundary LoginView as B1
entity User as E1

Actor -> B1 : 1: chọn chức năng Đăng nhập
activate B1
B1 --> Actor : 2: hiển thị giao diện đăng nhập
Actor -> B1 : 3: nhập SĐT/Email + Mật khẩu, nhấn Đăng nhập
B1 -> E1 : 4: gọi checkLogin(phoneNumber, password)
activate E1
E1 --> B1 : trả kết quả xác thực
deactivate E1
B1 --> Actor : 5: chuyển hướng trang chủ, "Đăng nhập thành công"
deactivate B1
@enduml
```

<!-- PLACEHOLDER: account_seq_login_analysis -->

**Kịch bản phiên bản 2 – UC01 Đăng nhập (5 bước)**

1. Người dùng chọn chức năng Đăng nhập.
2. Lớp LoginView hiển thị giao diện đăng nhập.
3. Người dùng nhập SĐT/Email và Mật khẩu, nhấn nút Đăng nhập.
4. Lớp LoginView gọi hàm `checkLogin()` của đối tượng User để xác thực.
5. Lớp LoginView chuyển hướng trang chủ, hiển thị "Đăng nhập thành công".

#### UC02 – Đăng ký (8 bước)

```plantuml
@startuml
skinparam shadowing false
skinparam SequenceMessageAlign left
skinparam SequenceLifeLineBackgroundColor #7AD2FF
skinparam SequenceLifeLineBorderColor #000000
skinparam sequenceParticipantBackgroundColor #7AD2FF
skinparam sequenceParticipantBorderColor #000000
skinparam sequenceParticipantFontColor #000000
skinparam sequenceArrowColor #000000
skinparam sequenceArrowFontColor #000000

<style>
sequenceDiagram {
  Shadowing 0
  RoundCorner 0
  FontName "Arial"
  FontSize 10
  FontColor #000000
  participant { BackgroundColor #7AD2FF LineColor #000000 LineThickness 1 }
  actor { BackgroundColor transparent LineColor #000000 }
  boundary { BackgroundColor #7AD2FF LineColor #000000 }
  control { BackgroundColor #7AD2FF LineColor #000000 }
  entity { BackgroundColor #7AD2FF LineColor #000000 }
  lifeline { LineColor #000000 LineStyle 5-5 }
  arrow { LineColor #000000 LineThickness 1 FontSize 10 }
}
</style>
title Đăng ký – Tuần tự Phân tích (8 bước)

actor "Khách hàng" as Actor
boundary RegisterView as B1
boundary OTPVerifyView as B2
entity User as E1
entity OTP as E2

Actor -> B1 : 1: chọn liên kết Đăng ký
activate B1
B1 --> Actor : 2: hiển thị giao diện đăng ký
Actor -> B1 : 3: nhập Họ tên, SĐT, Email, Mật khẩu, nhấn Tiếp tục
B1 -> E1 : 4: gọi register(fullName, phoneNumber, email, password)
activate E1
E1 -> E2 : gọi sendOTP(phoneNumber, REGISTER)
activate E2
E2 --> E1 : OTP đã gửi
deactivate E2
E1 --> B1 : trả kết quả
deactivate E1
B1 --> Actor : 5: kiểm tra hợp lệ, gửi mã OTP
B1 --> Actor : 6: hiển thị giao diện xác nhận OTP
Actor -> B2 : 7: nhập mã OTP, nhấn Xác nhận
activate B2
B2 -> E2 : gọi verifyOTP(otpCode)
activate E2
E2 --> B2 : xác minh thành công
deactivate E2
B2 -> E1 : gọi saveUser()
activate E1
E1 --> B2 : tạo tài khoản thành công
deactivate E1
B2 --> Actor : 8: "Đăng ký thành công!", tự động đăng nhập
deactivate B2
deactivate B1
@enduml
```

<!-- PLACEHOLDER: account_seq_register_analysis -->

**Kịch bản phiên bản 2 – UC02 Đăng ký (8 bước)**

1. Khách hàng chọn liên kết Đăng ký từ giao diện đăng nhập.
2. Lớp RegisterView hiển thị giao diện đăng ký.
3. Khách hàng nhập Họ tên, SĐT, Email, Mật khẩu, Xác nhận mật khẩu, nhấn Tiếp tục.
4. Lớp RegisterView gọi hàm `register()` của đối tượng User.
5. Lớp User kiểm tra thông tin hợp lệ, gọi hàm `sendOTP()` của đối tượng OTP.
6. Lớp RegisterView hiển thị giao diện xác nhận OTP.
7. Khách hàng nhập mã OTP, nhấn Xác nhận. Lớp OTPVerifyView gọi hàm `verifyOTP()` của đối tượng OTP.
8. Lớp OTPVerifyView gọi hàm `saveUser()` của đối tượng User, hiển thị "Đăng ký thành công!".

#### UC03 – Đổi mật khẩu (5 bước)

```plantuml
@startuml
skinparam shadowing false
skinparam SequenceMessageAlign left
skinparam SequenceLifeLineBackgroundColor #7AD2FF
skinparam SequenceLifeLineBorderColor #000000
skinparam sequenceParticipantBackgroundColor #7AD2FF
skinparam sequenceParticipantBorderColor #000000
skinparam sequenceParticipantFontColor #000000
skinparam sequenceArrowColor #000000
skinparam sequenceArrowFontColor #000000

<style>
sequenceDiagram {
  Shadowing 0
  RoundCorner 0
  FontName "Arial"
  FontSize 10
  FontColor #000000
  participant { BackgroundColor #7AD2FF LineColor #000000 LineThickness 1 }
  actor { BackgroundColor transparent LineColor #000000 }
  boundary { BackgroundColor #7AD2FF LineColor #000000 }
  control { BackgroundColor #7AD2FF LineColor #000000 }
  entity { BackgroundColor #7AD2FF LineColor #000000 }
  lifeline { LineColor #000000 LineStyle 5-5 }
  arrow { LineColor #000000 LineThickness 1 FontSize 10 }
}
</style>
title Đổi mật khẩu – Tuần tự Phân tích (5 bước)

actor "Người dùng" as Actor
boundary ChangePasswordView as B1
entity User as E1

Actor -> B1 : 1: chọn chức năng Đổi mật khẩu
activate B1
B1 --> Actor : 2: hiển thị giao diện đổi mật khẩu
Actor -> B1 : 3: nhập MK hiện tại, MK mới, Xác nhận MK mới, nhấn Lưu
B1 -> E1 : 4: gọi changePassword(currentPassword, newPassword)
activate E1
E1 --> B1 : đổi mật khẩu thành công
deactivate E1
B1 --> Actor : 5: "Đổi mật khẩu thành công", chuyển hướng về đăng nhập
deactivate B1
@enduml
```

<!-- PLACEHOLDER: account_seq_changepw_analysis -->

**Kịch bản phiên bản 2 – UC03 Đổi mật khẩu (5 bước)**

1. Người dùng chọn chức năng Đổi mật khẩu.
2. Lớp ChangePasswordView hiển thị giao diện đổi mật khẩu.
3. Người dùng nhập Mật khẩu hiện tại, Mật khẩu mới, Xác nhận mật khẩu mới, nhấn Lưu.
4. Lớp ChangePasswordView gọi hàm `changePassword()` của đối tượng User.
5. Lớp ChangePasswordView hiển thị "Đổi mật khẩu thành công", chuyển hướng về đăng nhập.

#### UC04 – Quản lý thông tin cá nhân (7 bước)

```plantuml
@startuml
skinparam shadowing false
skinparam SequenceMessageAlign left
skinparam SequenceLifeLineBackgroundColor #7AD2FF
skinparam SequenceLifeLineBorderColor #000000
skinparam sequenceParticipantBackgroundColor #7AD2FF
skinparam sequenceParticipantBorderColor #000000
skinparam sequenceParticipantFontColor #000000
skinparam sequenceArrowColor #000000
skinparam sequenceArrowFontColor #000000

<style>
sequenceDiagram {
  Shadowing 0
  RoundCorner 0
  FontName "Arial"
  FontSize 10
  FontColor #000000
  participant { BackgroundColor #7AD2FF LineColor #000000 LineThickness 1 }
  actor { BackgroundColor transparent LineColor #000000 }
  boundary { BackgroundColor #7AD2FF LineColor #000000 }
  control { BackgroundColor #7AD2FF LineColor #000000 }
  entity { BackgroundColor #7AD2FF LineColor #000000 }
  lifeline { LineColor #000000 LineStyle 5-5 }
  arrow { LineColor #000000 LineThickness 1 FontSize 10 }
}
</style>
title Quản lý TTCN – Tuần tự Phân tích (7 bước)

actor "Khách hàng" as Actor
boundary ProfileView as B1
entity User as E1

Actor -> B1 : 1: chọn chức năng Hồ sơ cá nhân
activate B1
B1 -> E1 : 2: gọi getProfile(userId)
activate E1
E1 --> B1 : trả về thông tin User
deactivate E1
B1 --> Actor : 3: hiển thị trang hồ sơ cá nhân
Actor -> B1 : 4: nhấn nút Chỉnh sửa
B1 --> Actor : 5: chuyển sang chế độ chỉnh sửa
Actor -> B1 : 6: cập nhật Họ tên, Email, nhấn Lưu
B1 -> E1 : 7: gọi updateProfile(userId, fullName, email)
activate E1
E1 --> B1 : cập nhật thành công
deactivate E1
B1 --> Actor : "Cập nhật thành công!", quay về chế độ xem
deactivate B1
@enduml
```

<!-- PLACEHOLDER: account_seq_profile_analysis -->

**Kịch bản phiên bản 2 – UC04 Quản lý thông tin cá nhân (7 bước)**

1. Khách hàng chọn chức năng Hồ sơ cá nhân.
2. Lớp ProfileView gọi hàm `getProfile()` của đối tượng User.
3. Lớp ProfileView hiển thị trang hồ sơ cá nhân.
4. Khách hàng nhấn nút Chỉnh sửa.
5. Lớp ProfileView chuyển sang chế độ chỉnh sửa.
6. Khách hàng cập nhật Họ tên, Email, nhấn Lưu. Lớp ProfileView gọi hàm `updateProfile()` của đối tượng User.
7. Lớp ProfileView hiển thị "Cập nhật thành công!", quay về chế độ xem.

#### UC20 – Quản lý tài khoản nhân viên (14 bước)

```plantuml
@startuml
skinparam shadowing false
skinparam SequenceMessageAlign left
skinparam SequenceLifeLineBackgroundColor #7AD2FF
skinparam SequenceLifeLineBorderColor #000000
skinparam sequenceParticipantBackgroundColor #7AD2FF
skinparam sequenceParticipantBorderColor #000000
skinparam sequenceParticipantFontColor #000000
skinparam sequenceArrowColor #000000
skinparam sequenceArrowFontColor #000000

<style>
sequenceDiagram {
  Shadowing 0
  RoundCorner 0
  FontName "Arial"
  FontSize 10
  FontColor #000000
  participant { BackgroundColor #7AD2FF LineColor #000000 LineThickness 1 }
  actor { BackgroundColor transparent LineColor #000000 }
  boundary { BackgroundColor #7AD2FF LineColor #000000 }
  control { BackgroundColor #7AD2FF LineColor #000000 }
  entity { BackgroundColor #7AD2FF LineColor #000000 }
  lifeline { LineColor #000000 LineStyle 5-5 }
  arrow { LineColor #000000 LineThickness 1 FontSize 10 }
}
</style>
title Quản lý nhân viên – Tuần tự Phân tích (14 bước)

actor "Admin" as Actor
boundary StaffManageView as B1
entity Employee as E1

Actor -> B1 : 1: chọn chức năng Quản lý nhân viên
activate B1
B1 -> E1 : 2: gọi getAllStaff()
activate E1
E1 --> B1 : trả về danh sách Employee
deactivate E1
B1 --> Actor : 3: hiển thị danh sách nhân viên
Actor -> B1 : 4: nhấn nút Thêm nhân viên
B1 --> Actor : 5: hiển thị giao diện nhập thông tin
Actor -> B1 : 6: nhập Họ tên, SĐT, Vai trò, Chi nhánh, nhấn Lưu
B1 -> E1 : 7: gọi addStaff(fullName, role)
activate E1
E1 --> B1 : tạo thành công
deactivate E1
B1 --> Actor : 8: "Thêm nhân viên thành công!"
Actor -> B1 : 9: nhấn nút Sửa trên dòng Nguyễn Minh Tuấn
B1 --> Actor : 10: hiển thị giao diện chỉnh sửa
Actor -> B1 : 11: cập nhật thông tin, nhấn Lưu
B1 -> E1 : 12: gọi updateStaff(id, data)
activate E1
E1 --> B1 : cập nhật thành công
deactivate E1
B1 --> Actor : "Cập nhật thành công!"
Actor -> B1 : 13: nhấn nút Xóa trên dòng Lê Văn Khánh
B1 --> Actor : 14: yêu cầu xác nhận xóa, "Xóa nhân viên thành công!"
deactivate B1
@enduml
```

<!-- PLACEHOLDER: account_seq_staff_analysis -->

**Kịch bản phiên bản 2 – UC20 Quản lý tài khoản nhân viên (14 bước)**

1. Admin chọn chức năng Quản lý nhân viên.
2. Lớp StaffManageView gọi hàm `getAllStaff()` của đối tượng Employee.
3. Lớp StaffManageView hiển thị danh sách nhân viên.
4. Admin nhấn nút Thêm nhân viên.
5. Lớp StaffManageView hiển thị giao diện nhập thông tin.
6. Admin nhập Họ tên, SĐT, Vai trò, Chi nhánh, nhấn Lưu.
7. Lớp StaffManageView gọi hàm `addStaff()` của đối tượng Employee.
8. Lớp StaffManageView hiển thị "Thêm nhân viên thành công!".
9. Admin nhấn nút Sửa trên dòng Nguyễn Minh Tuấn.
10. Lớp StaffManageView hiển thị giao diện chỉnh sửa.
11. Admin cập nhật thông tin, nhấn Lưu.
12. Lớp StaffManageView gọi hàm `updateStaff()` của đối tượng Employee.
13. Admin nhấn nút Xóa trên dòng Lê Văn Khánh.
14. Lớp StaffManageView yêu cầu xác nhận, hiển thị "Xóa nhân viên thành công!".
