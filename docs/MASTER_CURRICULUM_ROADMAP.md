# MASTER CURRICULUM ROADMAP — LEVEL 1 (BẢNG B)
## Khung Chương Trình Chuẩn Luyện Thi Tin Học Trẻ Bảng B & HSG THCS

**Tài liệu tham chiếu chuẩn:** iKHEDU Curriculum Architecture v2  
**Trạng thái:** 🔒 **OFFICIAL ROADMAP — FROZEN**

---

## 🏛️ Cấu Trúc 8 Master Modules

```text
LEVEL 1 — BẢNG B (C++ OLYMPIAD FOUNDATION)
│
├── Module 01: Sắp Xếp, Hai Con Trỏ & Cửa Sổ Trượt (Sorting / Two Pointers / Sliding Window)
│   ├── Lesson 01: Thuật Toán Sắp Xếp (sort, Custom Comparator, Strict Weak Ordering)
│   ├── Lesson 02: Kỹ Thuật Hai Con Trỏ (Two Sum, Đếm Cặp, Ghép Cặp Cực Trị, Khử Chiều 3-Sum)
│   └── Lesson 03: Kỹ Thuật Cửa Sổ Trượt (Cửa Sổ Cố Định K, Cửa Sổ Co Giãn, Bảng Tần Suất)
│
├── Module 02: Mảng Tiền Tố, Mảng Hiệu, Tìm Kiếm Nhị Phân & Phép Toán Bit (Prefix / Difference / Binary Search / Bit)
│   ├── Lesson 01: Mảng Tiền Tố & Mảng Hiệu (Prefix Sum 1D/2D, Difference Array 1D/2D)
│   ├── Lesson 02: Thuật Toán Tìm Kiếm Nhị Phân (Binary Search Mảng Đơn Điệu, Chặt Nhị Phân Kết Quả)
│   └── Lesson 03: Phép Toán Bit & Mặt Nạ Bit Cơ Bản (Bitwise Operations, Bật/Tắt Bit, Duyệt Tập Con 2^N)
│
├── Module 03: Số Học, Đồng Dư & Số Nguyên Lớn (Number Theory / Modulo / Big Integer)
│   ├── Lesson 01: Số Học & Ước Bội (GCD/LCM, Sàng Nguyên Tố Eratosthenes, Phân Tích Thừa Số)
│   ├── Lesson 02: Số Học Đồng Dư & Lũy Thừa Nhanh (Modulo Arithmetic, Binary Exponentiation)
│   └── Lesson 03: Xử Lý Số Nguyên Lớn (Big Integer Addition, Subtraction, Multiplication)
│
├── Module 04: Đếm Phân Phối, Bảng Tần Suất & Tổ Hợp Cơ Bản (Frequency / Counting / Combinatorics)
│   ├── Lesson 01: Đếm Phân Phối & Bảng Tần Suất (Coordinate Compression / Nén Tọa Độ)
│   ├── Lesson 02: Nguyên Lý Dirichlet & Kỹ Thuật Đếm Trực Tiếp
│   └── Lesson 03: Tổ Hợp Cơ Bản (Hoán Vị, Chỉnh Hợp, Tổ Hợp, Tam Giác Pascal)
│
├── Module 05: Xử Lý Chuỗi Ký Tự & Băm Chuỗi (String / Hashing)
│   ├── Lesson 01: Xử Lý Chuỗi Cơ Bản (Ký Tự, Bảng Chữ Cái, Substring, Palindrome)
│   ├── Lesson 02: Kỹ Thuật Băm Chuỗi Tuyến Tính (Rolling Hash / Polynomial Hashing)
│   └── Lesson 03: So Khớp Mẫu Chuỗi (Substring Search & Ứng Dụng Hashing O(1))
│
├── Module 06: Đệ Quy, Quay Lui & Quy Hoạch Động Nhập Môn (Recursion / Backtracking / DP)
│   ├── Lesson 01: Đệ Quy & Chia Để Trị (Recursion Tree, Divide & Conquer)
│   ├── Lesson 02: Thuật Toán Quay Lui (Backtracking, Liệt Kê Hoán Vị, N-Queens)
│   └── Lesson 03: Quy Hoạch Động Nhập Môn (DP 1D, Dãy Con Tăng Dài Nhất LIS, Knapsack Cơ Bản)
│
├── Module 07: Cấu Trúc Dữ Liệu STL, Ngăn Xếp & Hàng Đợi (STL / Stack / Queue)
│   ├── Lesson 01: Thư Viện Cấu Trúc Dữ Liệu STL (set, map, priority_queue)
│   ├── Lesson 02: Ngăn Xếp (Stack, Kiểm Tra Dãy Ngoặc Đúng, Monotonic Stack Cơ Bản)
│   └── Lesson 03: Hàng Đợi & Hàng Đợi Hai Đầu (Queue, Deque, Duy Trì Min/Max Cửa Sổ)
│
└── Module 08: Lý Thuyết Đồ Thị & Truy Vấn Đoạn Cơ Bản (Graph / Tree / Range Query)
    ├── Lesson 01: Biểu Diễn Đồ Thị & Duyệt Đồ Thị Cơ Bản (Adjacency List, BFS, DFS)
    ├── Lesson 02: Cây & Đồ Thị Lưới 2D (Connected Components, Flood Fill)
    └── Lesson 03: Giới Thiệu Cây Phân Đoạn (Segment Tree / Fenwick Tree Nhập Môn)
```

---

## 🎯 Quy Chuẩn Triển Khai Cho Từng Module
Mỗi Module bắt buộc triển khai đầy đủ hệ sinh thái:
1. **Master Design Specification (`docs/MASTER_MODULE_xx_DESIGN.md`):** Bản đặc tả Golden Spec.
2. **3 Master Lessons (Textbook Content):** Biên soạn văn phong giáo trình chuẩn mực, không văn phong kể chuyện bài giảng, có chứng minh quy nạp / loop invariant, mẫu code C++ 3 bước, bảng phân tích độ phức tạp, và 10 câu hỏi Concept Quiz sâu sắc.
3. **14 Problem Packages / Lesson (42 bài/Module):**
   * Định danh: `[Mã Khóa]-[Mã Bài Viết Tắt]-[Số Thứ Tự]` (Ví dụ: `CPPB-PT-01` $\to$ `CPPB-PT-14`).
   * Mỗi bài có: `De_Bai.md`, `Huong_Dan_Giang_Day.md`, `solution.cpp` (Fast I/O, Safe Input, không dùng struct/pair không cần thiết).
