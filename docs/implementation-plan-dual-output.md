# Kế Hoạch Triển Khai: Hoàn Thiện Giáo Trình iKHEDU C++ Bảng B

> Ngày tạo: 2026-08-28  
> Cập nhật: 2026-08-28 (v2 — đồng bộ với `review-report-v2-status-dashboard.md`)  
> Trạng thái: **Chờ duyệt**  
> Chủ dự án: iKHEDU

---

## Nguyên tắc cốt lõi

### "1 Bản Thảo — 2 Đầu Ra" (Single Source, Dual Output)

Từ **1 file Markdown canonical** (`BOOK_MASTER.md`) có thể:
1. 📚 Xuất **sách in PDF/Typst** chuyên nghiệp
2. 💻 Tự động bóc tách thành **các Block trên Web LMS / DKOJ**

### Track A đi trước Track B

```text
TRACK A — CONTENT (đi trước)     TRACK B — PLATFORM (đi sau)
     │                                │
Freeze kiến trúc              Problem ID (IKH-CCbb)
     ↓                                ↓
3 loại kiến thức              Quiz schema ([x]/[ ])
     ↓                                ↓
Review khung Chương/Bài       Problem Package (De_Bai/Huong_Dan/solution/test)
     ↓                                ↓
Source (reviewed)              Lesson Package (Ly_Thuyet/Bai_Tap/code)
     ↓                                ↓
BOOK_MASTER (canonical)        PDF / LMS renderer
     ↓
QA
```

**Không lao vào tạo 252 problem packages.** Track B chỉ pilot sau khi Track A freeze.

---

## Hiện trạng (Audit 2026-08-28)

| Thành phần | Trạng thái | Evidence |
|---|:---:|---|
| Kiến trúc sách Phần I + Phần II | 🟢 Locked | `DEC-015` |
| Roadmap 21 chuyên đề | 🟢 | Roadmap image + README |
| C++ Cơ bản — Tờ ghi nhớ | 🟡 Cần review | `source/level0/` 673 dòng |
| Tư duy giải bài (DNA) | 🟢 | `DEC-016` |
| Khung từng Chương (21 chương) | 🟡 Cần review | Ch3–21 có khung source nhưng chưa review sư phạm |
| Nội dung chi tiết | 🟡 Đang phát triển | Ch1 942 dòng, Ch2 748 dòng, Ch3–21 298–530 dòng |
| BOOK_MASTER sync | 🟡 Lệch | Ch1–2 đã sync, Ch3–21 chỉ stub 18–25 dòng |
| Problem bank `problems/` | 🔴 0/252 | Chưa tạo |
| Quiz `[x]/[ ]` | 🔴 0 | Chưa có |
| Lesson packages | 🔴 1/21 | Chỉ `level1-01-sap-xep/` |
| Dual-Output automation | 🔴 | Chưa triển khai |

---

## 3 Loại Kiến Thức (thay Level 0 / Level 1 trong sách)

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

| Loại | Ví dụ | Vai trò | Vị trí trong sách |
|---|---|---|---|
| **A. C++ Cơ bản** | `cin/cout`, `int/long long`, `if/for`, `vector`, `sort` | Nhớ & tra cứu | C++ CƠ BẢN — TỜ GHI NHỚ |
| **B. Tư duy giải bài** | Đọc đề → I-P-O → Ví dụ tay → Công thức → Code → Test → Debug | Rèn xuyên suốt | DNA `DEC-016` |
| **C. Thuật toán** | Sắp xếp, Tham lam, Binary Search, DP, Graph... | Hiểu tại sao + vận dụng | Chuyên đề 01–21 |

**Cấu trúc sách:**

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

## Thứ Tự Freeze — 5 Bước

### Bước 1 — Freeze kiến trúc sách (P0)

Chốt cấu trúc tổng: Phần mở đầu → Tờ ghi nhớ → DNA → 21 Chuyên đề.
Sửa mục lục `BOOK_MASTER.md` cho khớp.

### Bước 2 — Freeze 3 loại kiến thức (P0)

Ghi `DEC-029` vào decision log. Phân biệt rõ:
- `for` là **công cụ C++** (loại A), không phải thuật toán
- `Binary Search` là **thuật toán** (loại C), không phải cú pháp
- `Input→Process→Output` là **phương pháp** (loại B)

### Bước 3 — Review C++ Tờ ghi nhớ (P0)

Câu hỏi duy nhất: *"Học sinh chưa biết gì, xem tờ này có đủ công cụ để đọc/viết code trong Chuyên đề 01 không?"*
- Thừa → bỏ
- Thiếu → bù
- Không biến 673 dòng thành 17 bài học

### Bước 4 — Review khung từng Chương (P1)

Mỗi Chương hỏi:
- Chương dạy cái gì?
- Có bao nhiêu Bài? Mỗi Bài giải quyết vấn đề gì?
- Thứ tự có hợp lý không? Bài trước chuẩn bị gì cho Bài sau?
- Prerequisite là gì?

### Bước 5 — Khi khung duyệt → mới viết chi tiết + pilot Dual-Output (P1→P2)

```text
Bài X.Y → nội dung → ví dụ → Tự kiểm tra → Bài tập → Tóm tắt
  → map sang LMS: Lesson Content + Quiz (nếu có) + Problem (nếu có)
```

Block sinh từ **loại nội dung**, không phải bài nào cũng ép đủ mọi block.

---

## Pilot Dual-Output — Chỉ 2 Bài

Sau khi Bước 4–5 duyệt xong, pilot end-to-end với **2 bài**:

```text
IKH-0101 (Sắp xếp — Dãy tăng dần)
IKH-0201 (Tham lam — Chọn hoạt động)
  ↓
Markdown [Mã bài: IKH-xxxx] + Quiz [x]/[ ] + <!-- block:... -->
  ↓
PDF (Typst/LaTeX, QR `ikh.edu.vn/p/IKH-xxxx`)
  ↓
LMS (LessonProblem / LessonQuizBlock)
  ↓
OJ (solution.cpp + test/manifest.json)
```

Chỉ sau khi pilot chạy `Author → Source → BOOK → PDF → Web → OJ` mới chốt:
- Problem package schema
- Quiz schema
- Lesson package schema
- Block markers `<!-- block:... -->`
- QR convention
- ID convention `IKH-CCbb`

Rồi mới scale: `2 → 24 → 100 → 252`.

---

## Quy Ước Mã Bài (chờ freeze sau pilot)

| Chương | Dải mã | Ví dụ |
|---|---|---|
| Chương 1 — Sắp xếp | `IKH-0101` → `IKH-0112` | `IKH-0101 - Day_so_tang_dan` |
| Chương 2 — Tham lam | `IKH-0201` → `IKH-0212` | `IKH-0201 - Chon_hoat_dong` |
| ... | ... | ... |
| Chương 21 — Fenwick Tree | `IKH-2101` → `IKH-2112` | ... |

**Quy tắc:**
- 2 chữ số đầu = số chương (01–21)
- 2 chữ số sau = thứ tự bài trong chương (01–12)
- Tổng tối đa: 21 × 12 = **252 bài tập**

---

## Problem Package — Cấu trúc (theo khuôn ebook-ikh)

```text
problems/
├── README.md                          ← Registry tổng mã bài
├── IKH-0101 - Day_so_tang_dan/
│   ├── De_Bai.md                      ← Đề bài cho học sinh
│   ├── Huong_Dan_Giang_Day.md         ← Hướng dẫn cho giáo viên
│   ├── solution.cpp                   ← Lời giải chuẩn C++
│   └── test/
│       ├── manifest.json
│       ├── test01.inp / test01.out
│       └── ...
```

## Lesson Package — Cấu trúc

```text
lessons/
├── level1-01-sap-xep/
│   ├── README.md
│   ├── Ly_Thuyet.md
│   ├── Bai_Tap.md
│   └── code_reference.cpp
```

## Quiz — Authoring Syntax

```markdown
#### Quiz trắc nghiệm

**Câu 1:** Trong Selection Sort, sau lượt thứ $i$, phần nào đã chắc chắn đúng?
- [x] A. Đoạn từ vị trí $0$ đến $i$
- [ ] B. Đoạn từ vị trí $i+1$ đến cuối
- [ ] C. Chỉ vị trí $0$
- [ ] D. Toàn bộ dãy
> *Giải thích: Mỗi lượt đưa phần tử nhỏ nhất về đúng vị trí.*
```

- **Sách in:** In A/B/C/D; đáp án ở Phụ lục cuối sách
- **Web:** Script parse `[x]/[ ]` → `LessonQuizBlock`

---

## Sync Ch3–21 — Có Điều Kiện

```text
SOURCE hiện tại (Ch3 530 dòng .. Ch21 398 dòng)
  ↓
REVIEW KHUNG (Bước 4)
  ↓
REVIEW SƯ PHẠM + PREREQUISITE
  ↓
APPROVE (ghi DEC)
  ↓
SYNC BOOK_MASTER (không copy mù)
```

---

## Cấu Trúc Thư Mục Tổng Thể (khi hoàn thiện)

```text
courses/cpp-bang-b/
├── BOOK_MASTER.md           ← Bản thảo canonical (1 source → 2 outputs)
├── README.md
├── source/                  ← Source gốc review trước khi sync
│   ├── level0/
│   └── level1/              ← 22 files (Framework + 21 chapters)
├── lessons/                 ← Lesson packages (21 folders)
│   ├── level1-01-sap-xep/
│   └── ...
└── problems/                ← Problem packages (tối đa 252 folders)
    ├── README.md            ← Registry tổng
    ├── IKH-0101 - .../
    └── ...
```

---

## Việc Cần Làm Ngay

| # | Việc | Output | Ưu tiên |
|---|---|---|---|
| 1 | Duyệt report v2 + freeze 3 loại kiến thức | `DEC-029` | P0 |
| 2 | Sửa mục lục `BOOK_MASTER.md`: Phần mở đầu + Tờ ghi nhớ tách khỏi I.1 | Commit | P0 |
| 3 | Review `source/level0/` theo câu hỏi Bước 3 | Checklist | P0 |
| 4 | Review khung Ch3–21: số Bài, thứ tự, prerequisite | Bảng review 19 dòng | P1 |
| 5 | Sau (4) → sync BOOK_MASTER có chọn lọc | BOOK_MASTER v0.2 | P1 |
| 6 | Pilot `IKH-0101` + `IKH-0201` end-to-end | 2 problem packages + 1 quiz | P2 |

**Không làm 228 problem, không automation hàng loạt ở giai đoạn này.**

---

## Câu Hỏi Cần Chốt

1. **Freeze 3 loại kiến thức** — đồng ý ghi `DEC-029` không?
2. **Thứ tự review Ch3–21** — theo thứ tự sách hay theo nhu cầu lớp học?
3. **Phần "Tự kiểm tra"** — giữ tự luận + thêm quiz, hay chuyển hết trắc nghiệm?
4. **Quy ước mã `IKH-CCbb`** — OK hay muốn dạng khác?
