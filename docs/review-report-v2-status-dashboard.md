# Report v2 — Dashboard Trạng Thái & Định Hướng Freeze

> Ngày: 2026-08-28
> Cơ sở: `docs/implementation-plan-dual-output.md:1` + audit source `2026-08-28`
> Vai trò: **Báo cáo trạng thái kỹ thuật** — không phải bản đồ quyết định nội dung chi tiết
> Trạng thái: `draft` — chờ chủ dự án duyệt freeze

## 0. Tóm tắt điều hành

Kiến trúc sách đã Locked (`DEC-015` tại `docs/book-architecture-verdict.md:5` — 9/10). Source content đã đi trước BOOK_MASTER. Dual-Output (Problem/Quiz/LMS/automation) chưa triển khai. **Không dùng con số 28–32% để quyết định việc tiếp theo** — đó là % hoàn thành *plan engineering*, không phải % giá trị sư phạm.

Thứ tự đúng giai đoạn này:

```text
Freeze kiến trúc -> Review 3 loại kiến thức -> Review khung từng Chương/Bài -> Duyệt -> mới viết chi tiết -> pilot Dual-Output 2 bài -> freeze schema -> scale
```

Track A (Content) đi trước Track B (Platform) một nhịp.

---

## 1. Dashboard 2 trục (thay % đơn)

| Thành phần | Trạng thái | Evidence |
|---|:---:|---|
| Kiến trúc sách `BOOK_MASTER.md:15` Phần I (I.1–I.6) + Phần II (Chương 1–21) | 🟢 Locked | `DEC-015` tại `.agent/context/decision-log.md:24` |
| Roadmap 21 chuyên đề | 🟢 | `Lo_trinh_hoc_tap_bangB_level1.jpg` + `courses/cpp-bang-b/README.md:47` |
| C++ Cơ bản — Tờ ghi nhớ | 🟡 Review | `source/level0/IKHEDU_Level0_Foundation.md:1` 673 dòng — cần kiểm tra đủ/thừa |
| Tư duy giải bài (DNA xuyên suốt) | 🟢 | `DEC-016` tại `decision-log.md:25` + `BOOK_MASTER.md:116` |
| Khung từng Chương (21 chương) | 🟡 Cần review | `source/level1/IKHEDU_Chapter03_NumberTheory_Source.md:1` .. `IKHEDU_Chapter21_FenwickTree_Source.md:1` đã có khung nhưng chưa review sư phạm |
| Khung từng Bài trong Chương | 🟡 Cần freeze | Ch1 `BOOK_MASTER.md:290` 7 Bài deep, Ch2 `BOOK_MASTER.md:1206` 6 Bài deep, Ch3–21 chỉ stub `BOOK_MASTER.md:1921` 18–25 dòng |
| Nội dung chi tiết | 🟡 Đang phát triển | 22 source files = 12,207 dòng (Ch1 942, Ch2 748, Ch3 530, Ch4–21 298–480) |
| BOOK_MASTER sync | 🟡 Lệch | Source deep nhưng BOOK chưa sync 19 chương |
| Problem bank `problems/` | 🔴 | `0/252` — `ls problems: No such file` (audit 2026-08-28) |
| Quiz `[x]/[ ]` | 🔴 | `grep -c Quiz =0`, `grep -c \[x\] =0` toàn workspace |
| Lesson package `lessons/` | 🔴 | `1/21` — chỉ `lessons/level1-01-sap-xep/:1` |
| Dual-Output automation (`<!-- block:... -->`, PDF/LMS) | 🔴 | Chưa triển khai |

---

## 2. Audit hiện trạng (fact)

```text
BOOK_MASTER.md: 2394 dòng (canonical)
source/level1/: 22 files / 12,207 dòng (bao gồm Framework 483 dòng)
source/level0/: 673 dòng
lessons/: 1 package (Ly_Thuyet 539 dòng + Bai_Tap 537 dòng + code_reference.cpp:1)
problems/: 0
IKH-xxxx: 0 (grep toàn workspace)
Quiz trắc nghiệm: 0
```

**Drift chính:**

```text
Ch1: source deep (942) -> BOOK deep (đã sync) ✓
Ch2: source deep (748) -> BOOK deep (đã sync) ✓
Ch3: source deep (530) -> BOOK stub (25 dòng) ✗
Ch4–21: source 298–480 dòng (đã có LO + 5 bài + 12 bài tập A/B/C) -> BOOK stub 18–23 dòng ✗
```

Drift này là việc cần xử lý, nhưng **không sửa bằng copy mù**.

---

## 3. Ba loại kiến thức — cần freeze (thay Level 0/1 trong sách)

> `level0/level1` chỉ giữ trong repo để quản trị. Trong sách in, không dùng `Level 0/Level 1` (`DEC-015`).

```text
              iKH C++ BẢNG B
                   │
     ┌─────────────┼─────────────┐
     ↓             ↓             ↓
 C++ Cơ bản    Tư duy giải    Thuật toán
 CẦN NHỚ      bài CẦN HÌNH   CẦN HIỂU
  Tra cứu      THÀNH xuyên    Chuyên đề
               suốt
```

| Loại | Ví dụ | Vai trò sư phạm | Vị trí trong sách |
|---|---|---|---|
| **A. C++ Cơ bản** | `#include`, `using namespace std`, `main`, `cin/cout`, `int/long long/double/char/string/bool`, `if/else`, `for/while`, `array/vector`, `function`, `sort`, `min/max` | Nhớ & tra cứu | `C++ CƠ BẢN — TỜ GHI NHỚ` (không phải Chương 0 với Bài 0.1..0.n) |
| **B. Tư duy giải bài** | `Đọc đề -> Input/Output -> Process -> Ví dụ tay -> Công thức -> Code -> Test nhỏ/biên -> Debug`, `độ phức tạp` | Rèn xuyên suốt mọi Chương | DNA `DEC-016` tại `BOOK_MASTER.md:116` |
| **C. Thuật toán** | `Sắp xếp`, `Tham lam`, `Số học`, `Đếm tần suất`, `Binary Search`, `Prefix Sum`, `Two Pointers`, `DP`, `Graph`... | Hiểu tại sao dùng + vận dụng | `Chuyên đề 01..21` — mỗi Chuyên đề = Chương với n Bài |

**Nguyên tắc:**

*   `for` là **công cụ C++** (loại A), không phải thuật toán.
*   `Binary Search` là **thuật toán** (loại C), không phải cú pháp.
*   `Input->Process->Output` là **phương pháp** (loại B), không phải cú pháp.

**`Làm quen với lập trình`** (lập trình là gì, chương trình là gì) không phải kiến thức ngang hàng `if/for/array/sort`. Để làm **Phần mở đầu rất ngắn** trước Tờ ghi nhớ:

```text
PHẦN MỞ ĐẦU (Làm quen — 2–3 trang)
  ↓
C++ CƠ BẢN — TỜ GHI NHỚ (tra cứu)
  ↓
CÁCH GIẢI BÀI (DNA)
  ↓
CHUYÊN ĐỀ 01 — SẮP XẾP [Bài 1.1 .. 1.n]
CHUYÊN ĐỀ 02 — THAM LAM [Bài 2.1 .. 2.n]
...
CHUYÊN ĐỀ 21 — FENWICK TREE
```

---

## 4. Hai track — Track A đi trước một nhịp

```text
              iKH C++ BẢNG B
                   │
     ┌─────────────┴─────────────┐
     │                           │
TRACK A — CONTENT           TRACK B — PLATFORM
     │                           │
Cấu trúc giáo trình         Problem ID (IKH-CCbb)
     ↓                           ↓
C++ Tờ ghi nhớ / ref        Quiz schema ([x]/[ ])
     ↓                           ↓
Curriculum 21 chương        Problem Package (De_Bai/Huong_Dan/solution/test)
     ↓                           ↓
Review từng Chương          Lesson Package (Ly_Thuyet/Bai_Tap/code)
     ↓                           ↓
Source (reviewed)           PDF / LMS renderer
     ↓
BOOK_MASTER (canonical)
     ↓
QA
```

**Không lao vào tạo 228 problem package vì audit báo 0/228.** Con số đó đúng nhưng chưa cấp bách. Track B chỉ pilot sau khi Track A freeze.

---

## 5. Thứ tự freeze 5 bước (giai đoạn hiện tại)

### Bước 1 — Freeze kiến trúc sách

```text
Phần mở đầu
C++ Cơ bản — Tờ ghi nhớ
Cách giải bài (DNA)
Chuyên đề 01 [Bài 1.1 .. 1.n]
Chuyên đề 02 [Bài 2.1 .. 2.n]
...
Chuyên đề 21
```

Không mở rộng thêm Chương trước khi review xong. Mỗi Chương phải nhìn thấy **danh sách Bài**.

### Bước 2 — Freeze vai trò 3 loại kiến thức (mục 3)

Ghi vào `decision-log.md` thay cho `Level 0/Level 1` trong văn phong sách.

### Bước 3 — Review C++ Tờ ghi nhớ

Câu hỏi duy nhất: *“Học sinh chưa biết gì, sau khi xem tờ này có đủ công cụ để đọc/viết code trong Chuyên đề 01 không?”* Thừa -> bỏ, thiếu -> bù. Không biến 673 dòng thành 17 bài học.

### Bước 4 — Review khung từng Chương (chưa viết chi tiết)

Mỗi Chương hỏi:

```text
Chương dạy cái gì?
Có bao nhiêu Bài? Mỗi Bài giải quyết vấn đề gì?
Thứ tự có hợp lý không? Bài trước chuẩn bị gì cho Bài sau?
Prerequisite là gì? (ví dụ Ch2 Tham lam cần Sorting `BOOK_MASTER.md:1213`)
```

### Bước 5 — Khi khung duyệt -> mới viết chi tiết

```text
Bài 1.1 -> nội dung -> ví dụ -> Tự kiểm tra -> Bài tập -> Tóm tắt -> mới map sang LMS:
1 Bài -> Lesson Content + Quiz (nếu có) + Problem (nếu có) + Resource (nếu có)
```

Block sinh từ **loại nội dung**, không phải bài nào cũng ép đủ mọi block (ý kiến ChatGPT mục 7).

---

## 6. Dual-Output — chỉ pilot, chưa scale

Sau khi Bước 5 có 1–2 Bài được duyệt, mới pilot:

```text
IKH-0101 (Sắp xếp — Dãy tăng dần, Bài 1.7.1 BOOK_MASTER.md:956)
IKH-0201 (Tham lam — Chọn hoạt động, Bài 2.6.5 BOOK_MASTER.md:1725)
  ↓
Markdown [Mã bài: IKH-xxxx] + Quiz [x]/[ ] + <!-- block:... -->
  ↓
PDF (Typst/LaTeX, QR `ikh.edu.vn/p/IKH-xxxx`)
  ↓
LMS (LessonProblem / LessonQuizBlock)
  ↓
OJ (solution.cpp + test/manifest.json)
```

`[x]/[ ]` chỉ là **authoring syntax** tại `docs/implementation-plan-dual-output.md:70`:

```markdown
#### Quiz trắc nghiệm
**Câu 1:** ...
- [x] B. Đoạn 0..i
- [ ] A. ...
> *Giải thích: ...*
```

Backend parse thành `Question{stem, options, correct, explanation}` rồi render 2 đầu ra. Không để `[x]` thành DB schema trá hình.

Chỉ sau khi pilot chạy end-to-end `Author -> Source -> BOOK -> PDF -> Web -> OJ` mới chốt:

```text
Problem package schema (references/problem-package-template.md:1)
Quiz schema
Lesson package schema (references/lesson-package-template.md:1)
Block markers <!-- block:lesson-content/quiz/problem -->
QR convention
ID convention IKH-CCbb (docs/implementation-plan-dual-output.md:28)
```

Rồi mới scale `2 -> 24 -> 100 -> 252`.

---

## 7. Sync Ch3–21 — có điều kiện

```text
SOURCE hiện tại (Ch3 530 dòng .. Ch21 398 dòng)
  ↓
REVIEW KHUNG (mục 5 Bước 4)
  ↓
REVIEW SƯ PHẠM + PREREQUISITE + BÀI TRONG CHƯƠNG
  ↓
APPROVE (ghi DEC)
  ↓
SYNC BOOK_MASTER (không copy mù)
```

Không `Source có rồi -> copy vào BOOK -> xong`.

---

## 8. Chuẩn tối thiểu cho mỗi Bài (thay template cứng)

Không ép mọi Bài có cùng số mục. Chuẩn tối thiểu:

```text
Mục tiêu | Ôn nhanh (C++ + Tư duy) | Kiến thức mới | Ví dụ (I-P-O + code) | Tự kiểm tra | Bài tập (A/B/C) | Tóm tắt
+ optional: Debug / Proof (đổi chỗ Ch2 Bài 2.4 BOOK_MASTER.md:1550) / Visualization / Complexity
```

Hiện Ch4–21 thiếu `Tự kiểm tra` so với Ch1–2 — cần bổ sung khi review, nhưng linh hoạt theo Bài.

---

## 9. Việc cần làm ngay (đề xuất cho Vũ)

| # | Việc | Output | Ưu tiên |
|---|---|---|---|
| 1 | Duyệt report v2 này + freeze mục 3 (3 loại kiến thức) | `DEC-029` | P0 |
| 2 | Sửa `BOOK_MASTER.md:15` mục lục: `Phần mở đầu` + `C++ Cơ bản — Tờ ghi nhớ` tách khỏi `I.1 Làm quen` | Commit | P0 |
| 3 | Review `source/level0/IKHEDU_Level0_Foundation.md:1` theo câu hỏi Bước 3 | Checklist | P0 |
| 4 | Review khung Ch3–21 (mỗi Chương 30 phút): số Bài, thứ tự, prerequisite | Bảng review 19 dòng | P1 |
| 5 | Chỉ sau 4 -> sync BOOK_MASTER có chọn lọc | BOOK_MASTER v0.2 | P1 |
| 6 | Pilot `IKH-0101` + `IKH-0201` end-to-end | 2 problem packages + 1 quiz | P2 (sau P1) |

Không làm `228 problem`, không automation hàng loạt ở giai đoạn này.

---

## 10. Phụ lục — Số liệu audit chi tiết

*   `courses/cpp-bang-b/BOOK_MASTER.md:1` 2394 dòng — Ch1 7 Bài deep, Ch2 6 Bài deep, Ch3–21 stub (trung bình 20 dòng, Ch18/20 chỉ 13 dòng)
*   `source/level1/IKHEDU_Chapter01_Sorting_Source.md:1` 942 dòng, `IKHEDU_Chapter02_Greedy_Source.md:1` 748 dòng — chuẩn mẫu DNA
*   `source/level1/IKHEDU_Chapter16_SegmentTree_Source.md:347` `struct Node` — cần exception hoặc sửa theo `DEC-024`
*   `source/level1/IKHEDU_Chapter04_FrequencyCount_Source.md:67` `MAX_VAL=100000` — cần cảnh báo phạm vi, phân biệt `frequency array` vs `compression/map`
*   `.agent/skills/ikhedu-authoring/references/` đã có `problem-package-template.md`, `lesson-package-template.md`, `chapter-template.md` — sẵn cho pilot

---

## 11. Kết luận

Report v2 là **dashboard kỹ thuật** để quản lý drift và track, không phải roadmap viết 252 bài. Quyết định nội dung lúc này là **kiến trúc -> 3 loại kiến thức -> khung Bài trong Chương -> prerequisite -> C++ Tờ ghi nhớ -> mới đến Dual-Output**. Nếu khung đúng, 200+ bài sau là công việc sản xuất; nếu khung sai, càng viết càng tốn công sửa.

> Đề xuất duyệt: Freeze mục 3 + mục 5 Bước 1–2 trước khi review Ch3–21.

