# MASTER MODULE 01 DESIGN SPECIFICATION
## Module 01: Sắp Xếp, Hai Con Trỏ & Cửa Sổ Trượt (Sorting → Two Pointers → Sliding Window)

**Tài liệu tham chiếu chuẩn:** iKHEDU Curriculum Architecture v2  
**Đối tượng:** Học sinh bắt đầu bước vào lập trình thi đấu (Tin học trẻ Bảng B, HSG THCS, Level 1)  
**Trạng thái:** 🔒 **GOLDEN SPECIFICATION — FROZEN** (Bản đặc tả hoàn chỉnh — Khóa kiến trúc 5 tầng, 3 Master Lessons & Định danh Problem độc lập)

---

## 00. Kiến Trúc Phân Cấp 5 Tầng & Định Danh Độc Lập (Identity Separation)

Toàn bộ hệ thống đào tạo iKHEDU và nền tảng Web LMS DKOJ được chuẩn hóa theo phân cấp 5 tầng và **tách biệt hoàn toàn giữa Problem Identity và Lesson Activity Placement**:

```text
PROGRAM (Chương trình đào tạo — Ví dụ: C++ Level 1 Bảng B)
   │
   ▼
MODULE / CHAPTER (Chuyên đề năng lực lớn — Ví dụ: Module 01: Sorting → Two Pointers → Sliding Window)
   │
   ▼
LESSON / BÀI HỌC (3 Master Lessons — Ví dụ: Lesson 02: Kỹ thuật Hai con trỏ đối đầu)
   │
   ▼
LESSON ACTIVITY PLACEMENT (Vị trí & Vai trò sư phạm trong bài học — Slot #1, Slot #2, Level P0..P4, Homework)
   │
   ├───────────────────────────────┐
   ▼                               ▼
PROBLEM ENTITY (Global Unique)    QUIZ ENTITY (Global Unique)
Code: CPPB-SX-01 (Mã bài toán)     ID: QUIZ-0101
```

### 🔒 Nguyên Tắc Định Danh Bất Biến (Identity Contract):
1. **`CPPB-xx-xx` / `IKH-xxxx` là Global Problem Code**: Đại diện cho thực thể bài toán duy nhất trong toàn hệ thống iKHEDU DKOJ (toàn bộ đề bài, testcases, solution, limit). `Problem.code` là trường **UNIQUE** trên cơ sở dữ liệu.
2. **`LessonActivity` là Quan Hệ Sử Dụng (Placement / Reference)**: Lesson chỉ tham chiếu tới `Problem.code`. Một bài toán `CPPB-xx-xx` có thể được tái sử dụng ở nhiều Lesson mà **không nhân bản dữ liệu bài toán**.
3. **Thứ tự (`order`) và Nấc thang (`P0..P5`, `Homework`) thuộc về Activity Placement**: Không phải là thuộc tính định danh cố định của Problem.

---

## 01. Module Contract & Scope Boundary

Module 01 là **khởi đầu của tư duy cấu trúc thuật toán**. Module này định hình DNA nhận thức xuyên suốt:

$$\text{Unordered Data} \xrightarrow[\text{Nhận diện}]{\text{Phân tích}} \text{Biến đổi Trật tự} \xrightarrow[\text{sort}]{\text{Sắp xếp}} \text{Cấu trúc Đơn điệu / Lân cận} \xrightarrow[\text{Two Pointers / Window}]{\text{Khai thác}} \text{Lời giải tối ưu } \mathcal{O}(N) / \mathcal{O}(N \log N)$$

### Bảng Giới Hạn Phạm Vi (Allowed vs. Not Yet Boundary)

| Lớp Công Cụ | Được phép sử dụng trong Module 01 (Allowed) | TUYỆT ĐỐI CHƯA ĐƯỢC DÙNG (Not Yet) | Lý do sư phạm |
|---|---|---|---|
| **Cấu trúc dữ liệu** | `vector`, Mảng tĩnh 1D/2D, `vector<vector<int>>`, `pair` / `struct` (khi thật cần thiết) | `set`, `map`, `multiset`, `priority_queue`, `deque`, Cây Fenwick / Segment Tree | Tránh quá tải cú pháp; rèn tư duy xử lý mảng và trật tự thuần thục trước khi dùng STL nâng cao (Module 04/07). |
| **Thuật toán cơ sở** | `sort`, `stable_sort`, Custom Comparator, Vòng lặp 2 con trỏ `while` / `for` | Đệ quy / Quay lui, Chia để trị, Quy hoạch động, Hash chuỗi | Rèn luyện phản xạ tuyến tính $\mathcal{O}(N)$ và $\mathcal{O}(N \log N)$ trước khi học phân rã bài toán phức tạp. |
| **Toán học & Tiền xử lý** | Đếm, tính tổng, tìm min/max, kiểm tra tính đơn điệu | Modulo nghịch đảo, Phép nhân số lớn, Bitmask nâng cao | Tập trung 100% vào trật tự dữ liệu và hai con trỏ. |

---

## 02. Learning Outcomes (Chuẩn Đầu Ra Đo Lường Được)

* **`LO-01 (Ordering & Transformation)`**: Đứng trước một bài toán hỗn loạn, nhận diện được khi nào việc sắp xếp làm lộ ra tính chất cấu trúc có lợi (tính chất lân cận hoặc tính chất đơn điệu), chuyển hóa chính xác mọi quy tắc thứ tự thành hàm Comparator C++ chuẩn tuân thủ Strict Weak Ordering.
* **`LO-02 (Exploiting Adjacent Property)`**: Khai thác triệt để tính chất lân cận sau khi sắp xếp (các phần tử gần nhau nhất, bằng nhau, hoặc cùng nhóm sẽ nằm kề nhau) để giải quyết các bài toán khoảng cách cực tiểu, gom nhóm và đếm giá trị phân biệt trong $\mathcal{O}(N \log N)$.
* **`LO-03 (Opposite-Direction Two Pointers & Loop Invariant)`**: Thiết lập và chứng minh được **Tính chất bất biến (Loop Invariant)** của kỹ thuật hai con trỏ đối đầu ($L \leftrightarrow R$), hiểu tại sao mỗi bước dịch chuyển con trỏ loại bỏ chắc chắn các trường hợp không thể tạo nghiệm, đạt độ phức tạp tối ưu $\mathcal{O}(N)$.
* **`LO-04 (Sliding Window & Monotonic Condition)`**: Làm chủ kỹ thuật cửa sổ trượt ($L \to R$) cho cả cửa sổ cố định kích thước $K$ và cửa sổ biến thiên trên mảng không âm; nắm vững cơ chế mở rộng $R$ và co lại $L$, chứng minh mỗi phần tử chỉ vào/ra cửa sổ tối đa 1 lần.
* **`LO-05 (Boundary & Failure Analysis)`**: Nhận diện chính xác các bẫy biên (tràn số `long long`, trỏ ra ngoài mảng $0..N-1$) và chỉ ra được các phản ví dụ khi phương pháp thất bại (ví dụ: cửa sổ trượt thất bại khi mảng có số âm).

---

## 03. Prerequisites (C++ Foundation Prerequisite Layer)

Học sinh cần hoàn thành **C++ Foundation Layer** với các kỹ năng sau:
* Đọc/Ghi dữ liệu Fast I/O (`cin`, `cout`, `ios::sync_with_stdio(false)`, `cin.tie(nullptr)`).
* Kiểu dữ liệu số nguyên `int`, `long long` và quy tắc ép kiểu chống tràn số 32-bit khi nhân/cộng.
* Vòng lặp `for`, `while`, câu lệnh rẽ nhánh `if / else if / else`.
* Khai báo và duyệt mảng động `vector<int>`, `vector<vector<int>>`.
* Viết hàm, truyền tham chiếu (`&`) và tham chiếu hằng (`const &`).
* Ước lượng độ phức tạp thời gian cơ bản: $\mathcal{O}(1), \mathcal{O}(N), \mathcal{O}(N^2), \mathcal{O}(N \log N)$.

---

## 04. Theory Taxonomy (Cây Kiến Thức Lý Thuyết 3 Cụm)

```text
MODULE 01 THEORY TAXONOMY (3 MASTER PILLARS)
│
├── 01. THUẬT TOÁN SẮP XẾP (SORTING ALGORITHMS)
│   ├── Khái niệm Thứ tự & Không gian tìm kiếm
│   ├── Điều kiện biến đổi: Khi nào được phép sắp xếp? (Bảo toàn vs Phá vỡ vị trí)
│   ├── sort & stable_sort trong C++
│   ├── Thứ tự mặc định: Tăng dần (Ascending) & Giảm dần (Descending)
│   ├── Custom Comparator: Sắp xếp theo trị tuyệt đối, đa tiêu chí (vector lồng nhau / vector 2 chiều)
│   ├── Comparator ghép chuỗi tạo số lớn nhất (a + b > b + a)
│   ├── Nguyên lý Strict Weak Ordering (Luật toán tử < nghiêm ngặt, bẫy <=)
│   ├── Tính chất lân cận (Adjacency): Phần tử gần nhau nhất nằm kề nhau
│   ├── Bài toán khoảng cách cực tiểu (Min Difference) trong O(N log N)
│   └── Gom cụm & Đếm số lượng giá trị phân biệt (Distinct Values)
│
├── 02. KỸ THUẬT HAI CON TRỎ (TWO POINTERS)
│   ├── Trực giác: Thu hẹp không gian tìm kiếm 2 chiều từ O(N²) về O(N)
│   ├── Khởi tạo 2 đầu (L = 0, R = N - 1) trên mảng đã có thứ tự
│   ├── Tính chất đơn điệu (Monotonicity) của tổng A[L] + A[R]
│   ├── Chứng minh Loop Invariant: Không bỏ sót bất kỳ nghiệm hợp lệ nào
│   ├── Bài toán Two Sum: Cặp số có tổng đúng bằng S
│   ├── Đếm số cặp thỏa mãn bất đẳng thức: A[L] + A[R] <= S
│   ├── Bài toán Ghép thuyền cứu hộ (Boat Capacity / Extremal Pairing)
│   └── Mở rộng: Bài toán 3-Sum (Cố định 1 phần tử + Two Pointers đưa về O(N²))
│
└── 03. KỸ THUẬT CỬA SỔ TRƯỢT (SLIDING WINDOW)
    ├── Khái niệm Đoạn con liên tiếp (Contiguous Subarray)
    ├── Cửa sổ cố định (Fixed-size Window of size K): Trượt & Cập nhật O(1)
    ├── Cửa sổ biến thiên (Variable-size Window): Cơ chế Mở rộng (Expand R) & Co lại (Shrink L)
    ├── Điều kiện áp dụng: Tính đơn điệu của hàm mục tiêu (Mảng số không âm)
    ├── Đoạn con dài nhất / ngắn nhất có tổng thỏa mãn điều kiện
    ├── Bài toán biến đổi chuỗi / đếm số lượng phần tử thỏa mãn trong cửa sổ
    └── Giới hạn & Phản ví dụ: Khi nào Sliding Window THẤT BẠI? (Mảng có số âm)
```

---

## 05. Theory Dependency Graph (DAG Lý Thuyết)

```text
                           [C++ FOUNDATION]
                        (Vector, Vòng lặp, Hàm)
                                  │
                                  ▼
                    ┌───────────────────────────┐
                    │    LESSON 01: SẮP XẾP     │
                    │ (sort, Cmp, Lân cận) │
                    └─────────────┬─────────────┘
                                  │
         ┌────────────────────────┴────────────────────────┐
         │ (Tạo tính đơn điệu trên mảng)                   │ (Cấu trúc đoạn con liên tiếp)
         ▼                                                 ▼
┌───────────────────────────────────┐             ┌───────────────────────────────────┐
│       LESSON 02: HAI CON TRỎ      │             │       LESSON 03: CỬA SỔ TRƯỢT     │
│             ĐỐI ĐẦU               │             │             CÙNG CHIỀU            │
│ (L = 0, R = N - 1: Thu hẹp O(N))  │             │ (L → R: Mở R, Co L trên mảng >= 0)│
└───────────────────────────────────┘             └───────────────────────────────────┘
```

---

## 06. Lesson Learning Loop / Universal 3-in-1 Blueprint

> **Nguyên tắc Sư phạm Bất biến:** Không lý thuyết suông, không emoji trang trí rườm rà. Mỗi bài học là một tài liệu chuẩn mực phục vụ đồng thời: Tự học online, Sách in/Handout và Giáo án đứng lớp.

Mỗi Lesson trong Module 01 vận hành theo **Vòng lặp học tập 8 bước chuẩn mực**:

```text
1. HOOK / BÀI TOÁN SỐ NHỎ (Dẫn dắt trực diện bằng ví dụ cụ thể N = 5)
       ↓
2. BẾ TẮC QUY MÔ LỚN (Chỉ ra vét cạn O(N²) bị TLE khi N = 100.000)
       ↓
3. KHÁM PHÁ QUY LUẬT & INVARIANT (Biến đổi trật tự, bảng mô phỏng tay, chứng minh toán học)
       ↓
4. CODE C++ 3 BƯỚC & BẪY LỖI (Boilerplate chuẩn thi đấu, Trace table từng dòng/biến, Bug traps)
       ↓
5. MICRO PRACTICE P0 (Thực hành ngay tại chỗ thao tác kỹ thuật)
       ↓
6. CONCEPT QUIZ (4 câu trắc nghiệm tương tác đo năng lực Transfer)
       ↓
7. PROGRESSIVE PRACTICE P1 → P3 (Chuỗi bài tập tăng dần độ khó tại lớp)
       ↓
8. MASTERY CHALLENGE P4 / HOMEWORK (Bài toán thực tế giấu nhãn + Bài tập về nhà)
```

---

## 07. Conceptual Counterexamples (Phản Ví Dụ Chứng Minh Bản Chất)

### A. Phản ví dụ Comparator (Bẫy vi phạm Strict Weak Ordering)
* **Ý tưởng sai:** Dùng dấu `<=` trong comparator: `bool cmp(int a, int b) { return a <= b; }`.
* **Hậu quả:** Khi $a = b$, `cmp(a, b)` trả về `true` và `cmp(b, a)` cũng trả về `true`. Điều này vi phạm tính bất đối xứng ($a < b \implies \text{not}(b < a)$) $\implies$ `sort` truy cập vùng nhớ ngoài biên $\implies$ **Runtime Error / Crash bộ nhớ**.
* **Quy tắc đúng:** Luôn dùng toán tử so sánh nghiêm ngặt `<`. Khi hai phần tử bằng nhau, comparator **bắt buộc phải trả về `false`**.

### B. Phản ví dụ Two Pointers Đối Đầu (Khi mảng chưa được sắp xếp)
* **Ý tưởng sai:** Áp dụng Two Pointers $L, R$ trực tiếp trên mảng hỗn loạn để tìm cặp có tổng bằng $S$.
* **Vì sao thất bại:** Nếu $A[L] + A[R] < S$, ta tăng $L$ với hy vọng tổng tăng lên; nhưng vì mảng chưa sort nên $A[L+1]$ có thể nhỏ hơn $A[L]$, dẫn đến việc bỏ sót nghiệm.
* **Quy tắc đúng:** Tính chất đơn điệu chỉ xuất hiện sau khi mảng đã được sắp xếp tăng dần.

### C. Phản ví dụ Sliding Window (Khi mảng có chứa số âm)
* **Ý tưởng sai:** Dùng Sliding Window tìm đoạn con ngắn nhất có tổng $\ge K$ trên mảng có cả số âm.
* **Phản ví dụ:** Dãy $A = [2, -5, 10, -2, 8]$, tìm đoạn con ngắn nhất có tổng $\ge 8$.
* **Vì sao thất bại:** Khi $R$ gặp số âm $-5$, tổng bị giảm; khi $L$ dịch qua số âm, tổng lại tăng. Tính chất đơn điệu bị phá vỡ hoàn toàn $\implies$ Con trỏ $L$ không thể quyết định co một chiều $\implies$ Bắt buộc phải dùng Mảng tiền tố + Binary Search / Deque.

## 10. Danh Mục 42 Bài Tập Module 01 (Problem Activity Matrix)

### 10.1. Lesson 01: Thuật Toán Sắp Xếp

| STT | Mã Bài | Tên Bài Toán | Cấp Độ | Ràng Buộc Dữ Liệu | Mục Tiêu Rèn Luyện |
|:---:|:---:|---|:---:|---|---|
| 01 | `CPPB-SX-01` | **Xếp Hàng Điểm Danh** | `P0` | $N \le 1000, A_i \le 10^6$ | Cú pháp `sort` cơ bản |
| 02 | `CPPB-SX-02` | **Khoảng Cách Nhỏ Nhất** | `P1` | $N \le 10^5, A_i \le 10^9$ | Sắp xếp duyệt cặp kề |
| 03 | `CPPB-SX-03` | **Sắp Xếp Theo Trị Tuyệt Đối** | `P1` | $N \le 10^5, \vert A_i \vert \le 10^9$ | Custom comparator cơ bản |
| 04 | `CPPB-SX-04` | **Đếm Giá Trị Phân Biệt** | `P2` | $N \le 2 \cdot 10^5, \vert A_i \vert \le 10^9$ | Gom nhóm sau sắp xếp |
| 05 | `CPPB-SX-05` | **Hai Trạm Kiểm Soát Gần Nhau Nhất** | `P2` | $N \le 10^5, X_i \le 10^{12}$ | Xử lý dữ liệu lớn `long long` |
| 06 | `CPPB-SX-06` | **Khoảng Trống Lớn Nhất Trên Trục Tọa Độ** | `P3` | $N \le 10^5, \vert A_i \vert \le 10^{18}$ | Khai thác trật tự tuyến tính |
| 07 | `CPPB-SX-07` | **Sắp Xếp Theo Tổng Chữ Số** | `P1` | $N \le 10^5, A_i \le 10^9$ | Hàm biến đổi phụ trong comparator |
| 08 | `CPPB-SX-08` | **Gom Cụm Chênh Lệch Không Quá K** | `P2` | $N \le 2 \cdot 10^5, A_i \le 10^9$ | Tham lam tuyến tính trên mảng sắp xếp |
| 09 | `CPPB-SX-09` | **Tìm Phần Tử Xuất Hiện Nhiều Nhất** | `P2` | $N \le 2 \cdot 10^5, \vert A_i \vert \le 10^9$ | Đếm tần suất khối liên tiếp |
| 10 | `CPPB-SX-10` | **Sắp Xếp Lưu Vị Trí Ban Đầu** | `P3` | $N \le 10^5, \vert A_i \vert \le 10^9$ | Theo dõi chỉ số gốc (Index Tracking) |
| 11 | `CPPB-SX-11` | **Ghép Chuỗi Tạo Số Lớn Nhất** | `P3` | $N \le 10^4$ | So sánh chuỗi bắc cầu ($a+b > b+a$) |
| 12 | `CPPB-SX-12` | **Bảng Điểm Học Sinh Đa Trường** | `P4` | $N \le 10^5$ | Sắp xếp đa khóa ưu tiên |
| 13 | `CPPB-SX-13` | **Bảng Xếp Hạng Giải Đấu Thể Thao** | `P4` | $N \le 10^5$ | Sắp xếp tổ hợp 4 tiêu chí |
| 14 | `CPPB-SX-14` | **Sắp Xếp Đoạn Thẳng Không Giao Lỗi** | `P5` | $N \le 2 \cdot 10^5$ | Strict Weak Ordering & `stable_sort` |

---

### 10.2. Lesson 02: Kỹ Thuật Hai Con Trỏ

| STT | Mã Bài | Tên Bài Toán | Cấp Độ | Ràng Buộc Dữ Liệu | Mục Tiêu Rèn Luyện |
|:---:|:---:|---|:---:|---|---|
| 01 | `CPPB-HCT-01` | **Mô Phỏng Hai Con Trỏ Đối Đầu** | `P0` | $N \le 10^5, A_i \le 10^9$ | Cơ chế co hẹp $L \to \leftarrow R$ |
| 02 | `CPPB-HCT-02` | **Cặp Số Có Tổng Bằng S (Two Sum)** | `P1` | $N \le 10^5, A_i \le 10^9$ | Sắp xếp + Hai con trỏ |
| 03 | `CPPB-HCT-03` | **Đếm Cặp Có Tổng Không Quá S** | `P2` | $N \le 2 \cdot 10^5, A_i \le 10^9$ | Cộng dồn tổ hợp đoạn $(R - L)$ |
| 04 | `CPPB-HCT-04` | **Đếm Cặp Có Tổng Lớn Hơn Hoặc Bằng S** | `P2` | $N \le 2 \cdot 10^5, A_i \le 10^9$ | Biến thể chặn dưới tổ hợp |
| 05 | `CPPB-HCT-05` | **Ghép Thuyền Cứu Hộ Tối Ưu** | `P3` | $N \le 10^5, C \le 10^9$ | Tham lam ghép cực trị |
| 06 | `CPPB-HCT-06` | **Vận Chuyển Thùng Hàng Cực Đại** | `P4` | $N \le 10^5, W_i \le 10^{12}$ | Ghép cặp với dữ liệu cực lớn |
| 07 | `CPPB-HCT-07` | **Tìm Cặp Có Tổng Gần S Nhất** | `P1` | $N \le 10^5, A_i \le 10^9$ | Tối ưu sai số tuyệt đối |
| 08 | `CPPB-HCT-08` | **Tìm Cặp Có Hiệu Đúng Bằng K** | `P2` | $N \le 10^5, K \le 10^{18}$ | Hai con trỏ truy vết hiệu |
| 09 | `CPPB-HCT-09` | **Bộ Ba Số Có Tổng Bằng S (3-Sum)** | `P3` | $N \le 3000, A_i \le 10^9$ | Cố định 1 phần tử + Two Pointers |
| 10 | `CPPB-HCT-10` | **Đếm Số Tam Giác Có Thể Tạo Thành** | `P3` | $N \le 3000, A_i \le 10^9$ | Cố định cạnh lớn nhất + Two Pointers |
| 11 | `CPPB-HCT-11` | **Đếm Cặp Tổng S Trên Mảng Trùng Lặp** | `P4` | $N \le 2 \cdot 10^5$ | Xử lý tần suất giá trị trùng nhau |
| 12 | `CPPB-HCT-12` | **Ghép Cặp Trẻ Em Và Bánh Quy** | `P4` | $N, M \le 10^5$ | Hai con trỏ trên 2 mảng khác nhau |
| 13 | `CPPB-HCT-13` | **Bộ Bốn Số Có Tổng Bằng S (4-Sum)** | `P5` | $N \le 1000$ | Cố định 2 phần tử + Two Pointers |
| 14 | `CPPB-HCT-14` | **Cặp Số Tối Ưu Với Chênh Lệch Cực Hạn** | `P5` | $N, M \le 2 \cdot 10^5$ | Tìm $\min \vert A_i - B_j \vert$ tuyến tính |

---

### 10.3. Lesson 03: Kỹ Thuật Cửa Sổ Trượt

| STT | Mã Bài | Tên Bài Toán | Cấp Độ | Ràng Buộc Dữ Liệu | Mục Tiêu Rèn Luyện |
|:---:|:---:|---|:---:|---|---|
| 01 | `CPPB-CST-01` | **Tổng Cửa Sổ Cố Định K** | `P0` | $N \le 10^5, K \le N$ | Trượt cố định $\mathcal{O}(1)$ mỗi bước |
| 02 | `CPPB-CST-02` | **Giá Trị Trung Bình Lớn Nhất Của Đoạn K** | `P1` | $N \le 10^5, K \le N$ | Cửa sổ cố định với số thực |
| 03 | `CPPB-CST-03` | **Đoạn Con Ngắn Nhất Có Tổng Đạt S** | `P1` | $N \le 10^5, S \le 10^{14}$ | Cửa sổ co giãn tìm $\min$ length |
| 04 | `CPPB-CST-04` | **Đoạn Con Dài Nhất Có Tổng Không Quá S** | `P2` | $N \le 2 \cdot 10^5, S \le 10^{14}$ | Cửa sổ co giãn tìm $\max$ length |
| 05 | `CPPB-CST-05` | **Đoạn Con Chứa Tối Đa K Số 0 (Lật Bit)** | `P3` | $N \le 10^5, K \le N$ | Cửa sổ đếm trạng thái nhị phân |
| 06 | `CPPB-CST-06` | **Giám Sát Camera Giao Thông Thông Minh** | `P4` | $N \le 10^5, K \le N$ | Tối ưu hóa cửa sổ thực tế |
| 07 | `CPPB-CST-07` | **Tìm Min Trong Mọi Cửa Sổ Độ Dài K** | `P1` | $N \le 10^4, K \le N$ | Kiểm tra cửa sổ liên tiếp |
| 08 | `CPPB-CST-08` | **Đếm Số Lượng Đoạn Con Có Tổng Không Quá S** | `P2` | $N \le 2 \cdot 10^5, S \le 10^{14}$ | Cộng dồn $(R - L + 1)$ đoạn con |
| 09 | `CPPB-CST-09` | **Đếm Số Lượng Đoạn Con Có Tổng Đúng Bằng S** | `P2` | $N \le 2 \cdot 10^5, A_i > 0$ | Đếm đoạn trên mảng đơn điệu |
| 10 | `CPPB-CST-10` | **Đoạn Con Dài Nhất Chứa Tối Đa K Ký Tự Khác Nhau** | `P3` | $N \le 10^5, K \le 26$ | Cửa sổ ký tự với mảng đếm tần suất |
| 11 | `CPPB-CST-11` | **Đoạn Con Ngắn Nhất Chứa Đủ Mọi Ký Tự Của Tập Hợp** | `P3` | $N \le 10^5, M \le 26$ | Bài toán Minimum Window Substring |
| 12 | `CPPB-CST-12` | **Phủ Sóng Trạm Phát Sóng Wifi Đô Thị** | `P4` | $N \le 10^5, X_i \le 10^{14}$ | Hai con trỏ + Tham lam vị trí |
| 13 | `CPPB-CST-13` | **Đoạn Con Có Độ Chênh Lệch Max - Min Không Quá K** | `P4` | $N \le 5000$ | Khống chế biên độ trong cửa sổ |
| 14 | `CPPB-CST-14` | **Tối Ưu Cửa Sổ Trượt Tuyến Tính Khi N = 2.10⁵** | `P5` | $N \le 2 \cdot 10^5$ | Kỹ thuật hiệu $F(B) - F(A - 1)$ |

---

## 11. Mastery Exit Criteria (Tiêu Chí Hoàn Thành Module 01)

Học sinh được công nhận **Mastery Module 01** khi vượt qua bài kiểm tra đánh giá năng lực và đạt trọn bộ tiêu chí:

- [ ] **1. Nhận diện trật tự:** Tự giải thích được khi nào cần sắp xếp để tạo ra tính chất lân cận hoặc tính đơn điệu.
- [ ] **2. Cài đặt Comparator:** Tự viết được Custom Comparator (đa tiêu chí, ghép chuỗi) tuân thủ đúng Strict Weak Ordering, không bị crash bộ nhớ.
- [ ] **3. Tính chất lân cận:** Khai thác thành thạo để tìm khoảng cách nhỏ nhất và đếm giá trị phân biệt trong $\mathcal{O}(N \log N)$.
- [ ] **4. Chứng minh Two Pointers:** Trình bày được Loop Invariant của kỹ thuật $L \leftrightarrow R$ (tại sao không bỏ sót nghiệm).
- [ ] **5. Cơ chế Sliding Window:** Cài đặt thành thạo kỹ thuật mở rộng $R$ và co lại $L$, giải thích được tại sao đạt $\mathcal{O}(N)$.
- [ ] **6. Phản ví dụ:** Chỉ ra được lý do tại sao Sliding Window thất bại khi mảng có số âm và comparator lỗi khi dùng `<=`.
- [ ] **7. Tối ưu thời gian:** Đạt điểm tối đa $100\%$ các bài toán có giới hạn $N = 2 \times 10^5$ trong thời gian $1.0\text{s}$.
- [ ] **8. Xử lý biên:** Tự phòng tránh và xử lý triệt để các lỗi tràn số $10^{18}$ (`long long`) và lỗi biên mảng $0..N-1$.

---

## 12. Dual-Output Mapping (Quy Chuẩn Đồng Bộ Sách In & Web DKOJ)

* **Đầu ra Sách in (Print PDF / Typst)**:
  * Mỗi Lesson trình bày theo Universal Blueprint 8 bước: Bối cảnh $\to$ Bế tắc $N=100.000 \to$ Quy luật & Invariant $\to$ Code C++ 3 bước $\to$ Trace Table $\to$ Bẫy lỗi $\to$ Phản ví dụ $\to$ Bài tập $P0 \to P4$ & Homework.
  * Dưới mỗi đề bài in kèm **Mã QR và Global Problem Code `IKH-xxxx`**.
* **Đầu ra Web LMS (DKOJ Platform)**:
  * Khối `LessonContent`: Chứa toàn bộ nội dung bài giảng dẫn dắt chuẩn Markdown & KaTeX (không chứa text quiz/đề bài trùng lặp).
  * Khối `LessonQuizBlock`: Tự động trích xuất các câu hỏi kiểm tra khái niệm P0 để tạo tương tác phản hồi tức thì.
  * Khối `LessonProblem`: Tự động liên kết các `LessonActivity` tới Global Problem tương ứng trong Problem Bank với 20 testcases chuẩn $100\%$ AC.
