# iKHEDU C++ BẢNG B — LEVEL 2
## Nâng Cao Tư Duy, Cấu Trúc Dữ Liệu & Kỹ Thuật Lập Trình Thi Đấu

> **Trang chủ quản lý & Registry điều hướng khóa học Level 2 (Bảng B)**  
> **Tài liệu tham chiếu chuẩn:** [docs/MASTER_LEVEL2_PLAN.md](file:///Users/vu/Developer/ikhEdu_lessons/docs/MASTER_LEVEL2_PLAN.md)  
> **Trạng thái:** 🚀 `in-progress`

---

## 🏛️ Cấu Trúc 6 Master Modules Khóa Học Level 2

| Module / Chương | Tên Chuyên Đề | Số Lesson | Chủ đề tích hợp kế thừa | Trạng thái |
|---|---|:---:|---|:---:|
| **Module 01** | [Số Học và Modulo](lessons/lesson-01-so-hoc-co-ban-chuyen-sau/README.md) | 2 | `#03 Số học` + `#10 Modulo` | `draft` |
| **Module 02** | Kỹ Thuật Tìm Kiếm và Xử Lý Mảng | 2 | `#05 BS` + `#06 Prefix` & `#07 Two Pointers` + `#04 Counting` | `planned` |
| **Module 03** | Đệ Quy, Chia Để Trị và Bitwise | 2 | `#09 Đệ quy / MITM` + `#20 Phép toán bit` | `planned` |
| **Module 04** | Greedy và Quy Hoạch Động Cơ Bản | 2 | `#02 Tham lam` + `#13 Quy hoạch động` | `planned` |
| **Module 05** | Cấu Trúc Dữ Liệu Cơ Bản và C++ Library | 3 | `#15 Stack/Queue/Deque` + `#12 STL` + `#11 Tổ hợp` | `planned` |
| **Module 06** | Đồ Thị, Cấu Trúc Nâng Cao, Chuỗi và Số Lớn | 4 | `#14 Đồ thị` + `#21+#16 Tree` + `#17 Digit DP` + `#08+#18 String` + `#19 BigInt` | `planned` |

---

## 📂 Cấu Trúc Tổ Chức Thư Mục

```text
courses/cpp-bang-b-level2/
├── README.md                           # Trang chủ điều hướng khóa học
├── MASTER_ALL_LESSONS.md               # Sách giáo trình tổng hợp 15 bài học
├── build_docx.py                       # Pipeline xuất bản Word (.docx) & PDF chuẩn SGK
├── lessons/                            # 15 thư mục bài học (Lesson Packages)
│   ├── lesson-01-so-hoc-co-ban-chuyen-sau/
│   ├── lesson-02-modulo-va-fast-power/
│   └── ... (đến lesson-15)
└── problems/                           # Thư viện Problem Packages chuẩn thi đấu
    ├── cppb2_l01_01_.../
    └── ...
```

---

## 🎯 Quy Chuẩn Problem Package & Bài Học iKHEDU

Mỗi Lesson trong khóa học tuân thủ vòng lặp học tập:
$$\text{Learning Outcomes} \longrightarrow \text{Nội dung Core/Extension/Challenge} \longrightarrow \text{Visual Plan} \longrightarrow \text{Ví dụ mẫu} \longrightarrow \text{Concept Quiz} \longrightarrow \text{Bài tập phân tầng P0 } \to \text{ P5}$$

Mọi Problem Package bao gồm đầy đủ **4 thành phần**:
1. `De_Bai.md`: Statement chuẩn, giới hạn $1.0\text{s}$, $256\text{MB}$.
2. `Huong_Dan_Giang_Day.md`: 9 phần sư phạm chuyên sâu.
3. `solution.cpp`: Mã nguồn C++ chuẩn thi đấu (Fast I/O, Safe Input, 0 `std::`).
4. Thư mục `test/`: 20 testcases ma trận 6 tầng + `manifest.json`.
