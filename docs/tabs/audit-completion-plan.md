# Audit & Completion Plan — Module "Tài khoản & Thành viên" & "Quản lý đặt & trả phòng"

Generated: 2026-05-30

---

## Tab: Tài khoản & Thành viên (t.e7vhkfc8t70g)

### Current state
- 24 headings, 7 tables, 42 paragraphs, 0 bullets, 21 code runs
- Heading style: NUMBERED (1-10), NOT phased (I/II/III/IV) ← sai format so với chuẩn UP
- Missing formatting: no bullets, no bold paragraphs, no inline code in non-heading text

### Required 11 items (from cnpm skill)

| # | Required | Status | Action |
|---|----------|--------|--------|
| I.1 | UC chi tiết + mô tả UC | ✅ DONE | 4 UC (UC01-UC04) với bảng mô tả |
| II.1 | Kịch bản chuẩn + ngoại lệ | ❌ MISSING | Cần viết bảng kịch bản cho UC01-UC04 |
| II.2 | Trích xuất lớp thực thể | ✅ DONE | Bước 1-5 + bảng danh từ/thực thể |
| II.3 | Sơ đồ lớp phân tích (BCE) | ⚠️ VERIFY | Có heading "Biểu đồ thực thể (PlantUML)" — cần verify |
| II.4 | Biểu đồ tuần tự phân tích | ❌ EMPTY | Heading có, nội dung không |
| III.1 | Thiết kế lớp thực thể | ❌ EMPTY | Heading có, nội dung không |
| III.2 | ERD + thiết kế CSDL | ❌ EMPTY | Heading có, nội dung không |
| III.3.1 | Wireframe ASCII | ❌ EMPTY | Heading có, nội dung không |
| III.3.2 | Sơ đồ lớp thiết kế (MVC) | ❌ EMPTY | Heading có, nội dung không |
| III.4 | Biểu đồ tuần tự thiết kế | ❌ EMPTY | Heading có, nội dung không |
| IV | Test Plan + Test Case | ❌ EMPTY | Heading có, nội dung không |

**Summary: 2/11 done, 1 to verify, 8 to write**

### Heading structure issue
Current: `1.`, `2.`, `3.`, ..., `10.` (numbered)
Required: `I.`, `II.`, `III.`, `IV.` with sub-headings (phased, same as "Quản lý đặt & trả phòng")

---

## Tab: Quản lý đặt & trả phòng (t.13baw92fsltt)

### Current state
- 50 headings, 7 tables, 100 paragraphs, 98 bullets, 0 code runs
- Heading style: PHASED (I/II/III/IV) ← correct format
- Has bullets, bold formatting ← better quality

### Required 11 items

| # | Required | Status | Action |
|---|----------|--------|--------|
| I.1 | UC chi tiết + mô tả UC | ✅ DONE | Bảng thuật ngữ, Actor, UC (Đặt/Huỷ/Check-in/Check-out) |
| II.1 | Kịch bản chuẩn + ngoại lệ | ✅ DONE | 4 kịch bản với bảng Use Case |
| II.2 | Trích xuất lớp thực thể | ✅ DONE | 2.1-2.4 + bảng 17x5 danh từ/thực thể |
| II.3 | Sơ đồ lớp phân tích (BCE) | ⚠️ VERIFY | heading "2.5" — cần verify có PlantUML |
| II.4 | Biểu đồ tuần tự phân tích | ✅ DONE | 4.1-4.4 (Đặt/Huỷ/Check-in/Check-out) |
| III.1 | Thiết kế lớp thực thể | ❌ EMPTY | Heading có, nội dung không |
| III.2 | ERD + thiết kế CSDL | ❌ EMPTY | Heading có, nội dung không |
| III.3.1 | Wireframe ASCII | ❌ EMPTY | Heading có, nội dung không |
| III.3.2 | Sơ đồ lớp thiết kế (MVC) | ❌ EMPTY | Heading có, nội dung không |
| III.4 | Biểu đồ tuần tự thiết kế | ❌ EMPTY | Heading có, nội dung không |
| IV | Test Plan + Test Case | ❌ EMPTY | Heading có, nội dung không |

**Summary: 5/11 done, 1 to verify, 5 to write**

---

## Execution Order

### Phase 1: "Quản lý đặt & trả phòng" (more complete, faster to finish)
1. Verify PlantUML diagrams (II.3)
2. Write III.1 — Thiết kế lớp thực thể (attributes, data types, PK)
3. Write III.2 — ERD + CSDL (PlantUML ERD diagram)
4. Write III.3.1 — Wireframe ASCII
5. Write III.3.2 — MVC (BCE class diagram, copy pattern from "Dịch vụ & Sản phẩm")
6. Write III.4 — Biểu đồ tuần tự thiết kế
7. Write IV — Test Plan + Test Case

### Phase 2: "Tài khoản & Thành viên" (needs more work)
1. Fix heading structure (numbered → phased)
2. Write II.1 — Kịch bản chuẩn cho UC01-UC04
3. Verify II.3 — PlantUML
4. Write II.4 — Biểu đồ tuần tự phân tích
5. Write III.1 — Thiết kế lớp thực thể
6. Write III.2 — ERD + CSDL
7. Write III.3.1 — Wireframe ASCII
8. Write III.3.2 — MVC
9. Write III.4 — Biểu đồ tuần tự thiết kế
10. Write IV — Test Plan + Test Case

---

## GDocs Formatting Reference

### "Quản lý đặt & trả phòng" (reference — has proper formatting)

| Style | lineSpacing | spaceBelow | indentFirstLine | indentStart |
|-------|-------------|------------|-----------------|-------------|
| HEADING_1 | 100 | 3pt | 18pt | 36pt |
| HEADING_2 | — | — | 18pt | 36pt |
| HEADING_3 | — | — | 36pt | 36pt |
| HEADING_4 | — | — | 54pt | 72pt |
| NORMAL_TEXT | — | — | 36pt | 36pt |

### "Tài khoản & Thành viên" (needs formatting fix)
- All styles have default/empty spacing and indentation
- Need to apply same formatting as "Quản lý đặt & trả phòng"
