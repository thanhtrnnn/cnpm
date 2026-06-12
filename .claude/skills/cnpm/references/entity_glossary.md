<!-- Entity Glossary — canonical names for cross-module consistency -->

## Bảng entity chuẩn toàn hệ thống

> Mọi module PHẢI dùng tên class + tên bảng `tbl*` trong bảng dưới đây. KHÔNG tự ý đổi tên.

| Entity chuẩn | Tên bảng DB | Tên đã dùng sai (KHÔNG dùng lại) | Module sử dụng |
|-------------|-------------|----------------------------------|----------------|
| `User` | `tblUser` | `KhachHang`, `Client`, `Customer` | account, booking, services, core |
| `Employee` | `tblEmployee` | `NhanVien` | booking, services, core |
| `Room` | `tblRoom` | `Phong` | booking, services |
| `Room_receipt` | `tblRoomReceipt` | `HoaDon`, `Invoice` | booking, services |
| `MembershipTier` | `tblMembershipTier` | `HangHoiVien`, `MemberRanking` | account, booking |
| `Order` | `tblOrder` | `DonHang` | services |
| `Product` | `tblProduct` | `SanPham`, `MenuItem` | services |
| `Facility` | `tblFacility` | `CoSoVatChat`, `Asset` | services |
| `Damage_report` | `tblDamageReport` | `BaoCaoHong` | services |
| `Provider` | `tblProvider` | `NhaCungCap` | services |
| `Import_receipt` | `tblImportReceipt` | `PhieuNhap` | services |

### Quy tắc

1. **Tên class tiếng Anh PascalCase** — `User`, `Room_receipt`, `MembershipTier`
2. **Tên bảng DB `tbl` + tên entity** — `tblUser`, `tblRoom_receipt`, `tblMembershipTier`
3. **Tên trong văn xuôi phân tích** — có thể dùng tiếng Việt (`khách hàng`, `hóa đơn`) nhưng tên class/bảng PHẢI theo bảng trên
4. **Khi thêm entity mới** — kiểm tra bảng này trước, dùng tên đã có nếu cùng khái niệm

### Đính chính cross-module

- `Room_receipt` và `Employee` NHẤT QUÁN ở cấp class/bảng — tên Việt chỉ ở văn xuôi
- `User` (account) / `Client` (booking, services) / `Customer` (core) → **dùng `User`** cho tất cả
- `MembershipTier` vs `MemberRanking` → **dùng `MembershipTier`**
