# MASTER CURRICULUM & IMPLEMENTATION PLAN — LEVEL 2 (BẢNG B)
## Khóa Học C++ Bảng B — Level 2: Nâng Cao Tư Duy & Cấu Trúc Dữ Liệu Chuyên Sâu

> **Tài liệu tham chiếu chuẩn:** iKHEDU Curriculum Architecture v2 & Lộ trình [Lo_trinh_hoc_tap_bangB_level2.jpg](file:///Users/vu/Developer/ikhEdu_lessons/Lo_trinh_hoc_tap_bangB_level2.jpg)  
> **Trạng thái:** 🔒 **OFFICIAL BLUEPRINT — FROZEN & APPROVED**

---

## 1. BẢN CHẤT CỦA LEVEL 2 & NGUYÊN TẮC KẾ THỪA TÁI KẾT HỢP

### 1.1. Bản Chất Cốt Lõi
Học sinh học Level 2 **đã có nền tảng C++ và các kỹ thuật thuật toán cơ bản trước khi học Level 2**. Do đó:
* **Không dạy lại lý thuyết vỡ lòng / cú pháp sơ cấp**: Học sinh đã nắm vững các cú pháp, thao tác mảng, hàm, đệ quy cơ bản và các thuật toán nền tảng.
* **Trọng tâm Level 2 là TÁI KẾT HỢP & NÂNG CAO TƯ DUY (Hybrid Techniques)**:
  * Kết hợp **Số học + Modulo + Toán học trong lập trình** (`#03 + #10`).
  * Kết hợp **Tìm kiếm nhị phân + Mảng tiền tố** (`#05 + #06`).
  * Kết hợp **Hai con trỏ + Đếm phân phối / Bảng tần suất** (`#07 + #04`).
  * Kết hợp **Đệ quy + Chia để trị + Kỹ thuật gặp nhau ở giữa MITM** (`#09`).
  * Nâng cấp **Phép toán trên bit sang Bitmask nâng cao & Duyệt Submask** (`#20`).
  * Làm chủ các chủ đề chuyên sâu: **Tham lam (`#02`)**, **Quy hoạch động (`#13`)**, **Monotonic Stack/Deque (`#15`)**, **Thư viện C++ STL (`#12`)**, **Tổ hợp (`#11`)**, **Lý thuyết đồ thị (`#14`)**, **Segment Tree / Fenwick Tree (`#21 + #16`)**, **Digit DP (`#17`)**, **String Hashing (`#08 + #18`)**, **Số nguyên lớn BigInt (`#19`)**.

### 1.2. Phân Tầng Nội Dung Kiến Thức (Taxonomy)
Nhằm giữ đúng tinh thần lộ trình hình ảnh gốc nhưng vẫn đảm bảo chiều sâu thi đấu:
* **Core (Bắt buộc)**: Các kiến thức, thuật toán và kỹ thuật xuất hiện trực tiếp trên lộ trình ảnh Level 2.
* **Extension (Mở rộng tự nhiên)**: Các kỹ thuật phân rã trực tiếp từ Core nhằm giải quyết trọn vẹn bài toán (ví dụ: Sàng SPF, 2D Difference Array, Submask Iteration).
* **Challenge (Nâng cao / HSG)**: Các biến thể và bài toán thử thách dành cho học sinh giỏi (ví dụ: Diophantine, 0-1 BFS, Stars & Bars, BigInt Division).

---

## 2. NGUYÊN TẮC THIẾT KẾ LINH HOẠT THEO NỘI DUNG (CONTENT-DRIVEN SIZING)

Không áp đặt bất kỳ định mức hay quota số lượng cứng nhắc nào cho các Lesson. Số lượng Quiz, Bài tập và Hình ảnh trực quan được quyết định hoàn toàn dựa trên **độ rộng kiến thức, mức độ trừu tượng và số dạng bài biến thể thực tế** của từng Lesson:

| Thành phần | Quy tắc định lượng & Quản lý |
|---|---|
| **Visual Plan (Hình ảnh trực quan)** | Bắt buộc cho các kiến thức có tính cấu trúc, trạng thái, phân nhánh, phạm vi hoặc biến đổi theo bước (Graph, Tree, DP, Window, Bitmask...). Số lượng linh hoạt theo độ trừu tượng. |
| **Quiz mỗi Lesson** | Tùy biến theo độ rộng, số ý chính và số bẫy biên/tính chất của Lesson. |
| **Bài tập mỗi Lesson** | Tùy biến theo số kỹ thuật, số nấc thang phân tầng (P0 $\to$ P5) và độ phủ dạng bài thi HSG. |
| **Lesson trọng điểm (DP, Graph, Segment Tree, String/BigInt)** | Tự động mở rộng số lượng quiz, bài tập và sơ đồ minh họa để bao quát toàn bộ biến thể. |
| **Lesson tinh gọn** | Giữ dung lượng vừa vặn, không ép bài tập hay sơ đồ nhân tạo. |
| **Quiz cuối Module & Final Exam** | Xây dựng theo mục tiêu tổng hợp kiến thức của từng Module và toàn khóa. |
| **Tổng số toàn khóa** | **TBD (Sẽ chốt chính xác sau khi hoàn thiện biên soạn toàn bộ từng Lesson)**. |

---

## 3. QUY CHUẨN VISUAL PLAN (HÌNH ẢNH & SƠ ĐỒ TRỰC QUAN)

> 💡 **Nguyên tắc vàng:** *Các kiến thức có tính cấu trúc, trạng thái, phân nhánh, phạm vi hoặc biến đổi theo bước bắt buộc phải có hình ảnh/sơ đồ trực quan đi kèm khi cần thiết.*

Mỗi Lesson trong quá trình biên soạn sẽ bao gồm một **Visual Plan**, quản lý các hình ảnh/sơ đồ với cấu trúc:
* **Ý tưởng minh họa:** Bản chất trực giác của thuật toán / cấu trúc dữ liệu.
* **Vị trí nhúng trong bài:** Đặt đúng ngữ cảnh lý thuyết hoặc dry-run mẫu.
* **Tên file quy chuẩn:** `cppb2_lxx_visual_01_tên_hình.png/svg`.
* **Trạng thái:** `TBD / Draft / Approved`.

### Ma Trận Minh Họa Trực Quan Tham Chiếu Cho 15 Lessons:
| Nhóm chủ đề | Hình ảnh / Sơ đồ trực quan phù hợp |
|---|---|
| **Số học & Modulo** | Vòng tròn số dư đồng dư thức, Trục số modulo, Sơ đồ thuật toán Euclid thu hẹp |
| **Binary Search** | Mô phỏng không gian tìm kiếm $[L, R]$ và mảng bị thu hẹp qua từng bước `mid` |
| **Prefix Sum & Difference** | So sánh mảng gốc vs mảng tiền tố 1D/2D, Vùng chữ nhật bao phủ $2D$ |
| **Two Pointers & Sliding Window** | Chuyển động hai con trỏ đối đầu / cùng chiều, Khung cửa sổ trượt co giãn trên mảng |
| **Recursion & Divide & Conquer** | Cây gọi hàm đệ quy (Call Stack), Sơ đồ 3 bước `Divide → Solve → Combine` |
| **Meet-In-The-Middle** | Tập $N$ phần tử chia đôi thành 2 nửa $N/2$, hai không gian trạng thái gộp lại |
| **Bitwise & Bitmask** | Bảng bit nhị phân biểu diễn tập hợp con, Mô phỏng phép dịch bit và Submask |
| **Greedy** | Trục thời gian các khoảng hoạt động (Intervals) và quy luật chọn tối ưu |
| **Dynamic Programming** | Bảng quy hoạch động (DP Table), Lưới trạng thái và các mũi tên chuyển trạng thái |
| **Stack, Queue & Deque** | Cơ chế LIFO/FIFO, Monotonic Stack đẩy/bật phần tử, Cửa sổ trượt Deque 2 đầu |
| **Graph Theory** | Đồ thị đỉnh/cạnh, Cây duyệt BFS theo lớp / DFS theo nhánh sâu, Ma trận lưới Flood Fill |
| **Segment Tree & Fenwick** | Cây phân đoạn nhị phân quản lý đoạn $[L, R]$, Cây Fenwick với các bước nhảy bit `lowbit` |
| **Digit DP** | Cây phân nhánh lựa chọn từng chữ số $0..9$ và cơ chế rẽ nhánh cờ biên `tight` |
| **String Hashing** | Mã băm tiền tố $H[i]$ và cơ chế tính hash đoạn con $S[L..R]$ qua lũy thừa cơ số |
| **Big Integer** | Mô phỏng đặt tính dọc phép cộng, trừ, nhân nhiều chữ số có nhớ |

---

## 4. KHUNG CẤU TRÚC 6 MODULES / 15 LESSONS

```text
1 KHÓA HỌC LEVEL 2 (cpp-bang-b-level2)
└── 6 Module / Chương
    └── 15 Lesson (Large Conceptual Units)
        ├── 1. Mục tiêu học tập (Learning Outcomes)
        ├── 2. Nội dung chính (Core / Extension / Challenge)
        ├── 3. Visual Plan (Sơ đồ & Hình ảnh trực quan)
        ├── 4. Ví dụ minh họa (Dry Run Table & C++ Sample)
        ├── 5. Concept Quiz (Linh hoạt theo nội dung)
        └── 6. Bài tập phân tầng (Linh hoạt theo độ phủ P0 → P5)
```

```text
LEVEL 2 — BẢNG B (C++ OLYMPIAD ADVANCED & HYBRID PROBLEM SOLVING)
│
├── 📘 Module 01: Số Học và Modulo [#03 + #10]
│   ├── Lesson 01 (CPPB2-L01): Số Học Cơ Bản & Chuyên Sâu (Ước bội, GCD/LCM, Euclid, Số nguyên tố, Thừa số nguyên tố)
│   └── Lesson 02 (CPPB2-L02): Modulo và Fast Power (Đồng dư, Lũy thừa nhanh, Chia modulo, Inverse modulo)
│
├── 📘 Module 02: Kỹ Thuật Tìm Kiếm và Xử Lý Mảng [#05 + #06 & #07 + #04]
│   ├── Lesson 03 (CPPB2-L03): Binary Search và Prefix Sum (BS trên mảng, Lower/Upper bound, BS on answer, Prefix sum)
│   └── Lesson 04 (CPPB2-L04): Two Pointers và Counting (Hai con trỏ, Sliding window, Bảng tần suất, Đếm cặp)
│
├── 📘 Module 03: Đệ Quy, Chia Để Trị và Bitwise [#09 & #20]
│   ├── Lesson 05 (CPPB2-L05): Recursion, Divide & Conquer và MITM (Đệ quy, Chia để trị, Merge sort, Meet-in-the-middle)
│   └── Lesson 06 (CPPB2-L06): Bitwise và Bitmask (Phép toán bit, Bật/tắt bit, Biểu diễn tập hợp, Duyệt tập con)
│
├── 📘 Module 04: Greedy và Quy Hoạch Động Cơ Bản [#02 & #13]
│   ├── Lesson 07 (CPPB2-L07): Greedy (Lựa chọn tối ưu, Sắp xếp + Greedy, Activity selection, Phản ví dụ)
│   └── Lesson 08 (CPPB2-L08): Dynamic Programming Cơ Bản (Trạng thái, Chuyển trạng thái, Fibonacci, Knapsack, LIS, LCS)
│
├── 📘 Module 05: Cấu Trúc Dữ Liệu Cơ Bản và C++ Library [#15, #12 & #11]
│   ├── Lesson 09 (CPPB2-L09): Stack, Queue và Deque (LIFO, FIFO, Monotonic stack, Monotonic queue, Sliding window deque)
│   ├── Lesson 10 (CPPB2-L10): Thư Viện C++ (vector, set, multiset, map, unordered_map, iterator, độ phức tạp)
│   └── Lesson 11 (CPPB2-L11): Các Bài Toán Tổ Hợp (Quy tắc đếm, Hoán vị, Chỉnh hợp, Tổ hợp nCr, Tam giác Pascal)
│
└── 📘 Module 06: Đồ Thị, Cấu Trúc Nâng Cao, Chuỗi và Số Lớn [#14, #21+#16, #17, #08+#18, #19]
    ├── Lesson 12 (CPPB2-L12): Graph Theory (Biểu diễn đồ thị, BFS, DFS, Liên thông, Chu trình, Grid graph)
    ├── Lesson 13 (CPPB2-L13): Fenwick Tree và Segment Tree (Truy vấn đoạn, Cập nhật điểm, BIT, Segment tree)
    ├── Lesson 14 (CPPB2-L14): Digit DP (Trạng thái chữ số, Giới hạn tight, Tổng chữ số, Đếm số trên đoạn [L, R])
    └── Lesson 15 (CPPB2-L15): String, String Hashing và Big Integer (Xử lý xâu, Palindrome, Rolling hash, BigInt +, -, *, /)
```

---

## 5. CHI TIẾT NỘI DUNG TỪNG LESSON (Ý CHÍNH — VISUAL — VÍ DỤ — QUIZ — BÀI TẬP)

### 📘 MODULE 01 — SỐ HỌC VÀ MODULO

#### Lesson 01: Số Học Cơ Bản & Chuyên Sâu (`CPPB2-L01`)
* **Mục tiêu:** Nắm vững cấu trúc ước/bội, nguyên tố và tối ưu hóa phân tích thừa số.
* **Nội dung chính:**
  * **Core**: Chia hết, ước và bội; GCD và LCM; Thuật toán Euclid; Số nguyên tố và kiểm tra nguyên tố; Phân tích thừa số nguyên tố.
  * **Extension**: Sàng nguyên tố Eratosthenes, Sàng đoạn $[L, R]$, Sàng SPF (Smallest Prime Factor) phân tích thừa số nhanh $\mathcal{O}(\log N)$.
  * **Challenge**: Thuật toán Euclid mở rộng, Phương trình Diophantine $Ax + By = C$, Hàm phi Euler $\phi(N)$.
* **Visual Plan:** Sơ đồ thu hẹp Euclid; Trục số sàng nguyên tố đoạn $[L, R]$; Cây phân tích thừa số SPF.
* **Ví dụ:** Tìm GCD/LCM; Kiểm tra nguyên tố & Phân tích thừa số nguyên tố qua SPF; Sàng đoạn trên dải lớn.
* **Quiz:** TBD (Xác định theo số lượng ý chính và bẫy biên).
* **Bài tập phân tầng:** TBD (Xác định theo độ phủ các dạng bài từ P0 $\to$ P5).

#### Lesson 02: Modulo và Fast Power (`CPPB2-L02`)
* **Mục tiêu:** Làm chủ tính toán đồng dư, lũy thừa nhanh và nghịch đảo modulo.
* **Nội dung chính:**
  * **Core**: Phép cộng, trừ, nhân modulo; Đồng dư; Chia modulo; Inverse modulo; Lũy thừa nhanh (Fast Power); Xử lý số lớn trong phép tính modulo.
  * **Extension**: Phép nhân Ấn Độ chống tràn số; Nghịch đảo modulo Fermat ($A^{M-2} \bmod M$) và Euclid mở rộng; Rút gọn phân số lớn theo modulo.
  * **Challenge**: Khi $\gcd(A,M)=1$, lũy thừa với số mũ cực lớn có thể rút gọn qua Euler ($A^B \bmod M = A^{B \bmod \phi(M)} \bmod M$). Nếu $\gcd(A,M)\ne1$, không được áp dụng công thức này máy móc và phải dùng cách xử lý khác; Tiền xử lý nghịch đảo tuyến tính $\mathcal{O}(N)$.
* **Visual Plan:** Vòng tròn đồng dư thức modulo $M$; Cây phân rã lũy thừa nhị phân $A^B$.
* **Ví dụ:** Tính $A^B \bmod M$; Tính nghịch đảo modulo; Tính giá trị biểu thức phân số lớn theo modulo; So sánh lũy thừa tuyến tính vs Fast Power.
* **Quiz:** TBD (Xác định theo nội dung).
* **Bài tập phân tầng:** TBD (Xác định theo độ phủ kiến thức).

---

### 📘 MODULE 02 — KỸ THUẬT TÌM KIẾM VÀ XỬ LÝ MẢNG

#### Lesson 03: Binary Search và Prefix Sum (`CPPB2-L03`)
* **Mục tiêu:** Làm chủ chặt nhị phân kết quả và tiền xử lý tổng/hiệu đa chiều.
* **Nội dung chính:**
  * **Core**: Tư tưởng chia đôi; Tìm kiếm trên dãy đã sắp xếp; Lower Bound và Upper Bound; Binary Search trên đáp án; Mảng tiền tố; Truy vấn tổng trên đoạn.
  * **Extension**: Binary Search on Answer với hàm `check(mid)`; Mảng tiền tố 2D (2D Prefix Sum); Mảng hiệu 1D & 2D (Difference Array).
  * **Challenge**: Kết hợp Binary Search on Answer với 2D Prefix Sum / Difference Array.
* **Visual Plan:** Mô phỏng thu hẹp khoảng $[L, R]$ qua các bước; Sơ đồ diện tích bao phủ 2D Prefix Sum & 2D Difference.
* **Ví dụ:** Tìm giá trị / vị trí đầu tiên/cuối cùng; Tìm đáp án nhỏ nhất thỏa điều kiện; Tính tổng nhiều đoạn / hình chữ nhật bằng Prefix Sum.
* **Quiz:** TBD (Xác định theo nội dung).
* **Bài tập phân tầng:** TBD (Xác định theo độ phủ kiến thức).

#### Lesson 04: Two Pointers và Counting (`CPPB2-L04`)
* **Mục tiêu:** Tối ưu hóa không gian tìm kiếm đa biến qua con trỏ và cửa sổ trượt.
* **Nội dung chính:**
  * **Core**: Hai con trỏ cùng chiều; Hai con trỏ ngược chiều; Sliding Window; Frequency Counting; Đếm cặp; Đếm phần tử phân biệt.
  * **Extension**: Cửa sổ trượt co giãn duy trì bảng tần suất; Đếm đoạn con qua $\text{Count}(Exact\_K) = \text{AtMost}(K) - \text{AtMost}(K - 1)$.
  * **Challenge**: Khử chiều tìm kiếm 3-Sum, 4-Sum, đếm số tam giác bằng hai con trỏ.
* **Visual Plan:** Chuyển động hai con trỏ đối đầu trên mảng; Khung cửa sổ trượt co giãn $L \to R$ duy trì mảng đếm.
* **Ví dụ:** Tìm hai phần tử có tổng bằng $K$; Tìm đoạn con ngắn nhất/dài nhất thỏa điều kiện; Đếm số cặp bằng bảng tần suất.
* **Quiz:** TBD (Xác định theo nội dung).
* **Bài tập phân tầng:** TBD (Xác định theo độ phủ kiến thức).

---

### 📘 MODULE 03 — ĐỆ QUY, CHIA ĐỂ TRỊ VÀ BITWISE

#### Lesson 05: Recursion, Divide & Conquer và MITM (`CPPB2-L05`)
* **Mục tiêu:** Phân rã bài toán phức tạp và vượt ngưỡng vét cạn $2^N$ với Meet-In-The-Middle.
* **Nội dung chính:**
  * **Core**: Điều kiện dừng; Lời gọi đệ quy; Cây gọi hàm; Chia bài toán thành các bài toán con; Divide, Solve, Combine; Meet-in-the-Middle; Kết hợp MITM với tìm kiếm.
  * **Extension**: Merge Sort đếm cặp nghịch thế $\mathcal{O}(N \log N)$; Chia đôi tập dữ liệu $N \le 40$ thành $N/2$ sinh trạng thái độc lập.
  * **Challenge**: MITM kết hợp Two Pointers, bài toán 4-Sum trên 4 mảng độc lập.
* **Visual Plan:** Cây đệ quy gọi hàm; Sơ đồ Divide-Solve-Combine của Merge Sort; Sơ đồ chia đôi tập hợp Meet-In-The-Middle.
* **Ví dụ:** Tính lũy thừa bằng đệ quy; Merge Sort; Đếm nghịch thế bằng Chia để trị; Chia tập phần tử thành hai nửa để tìm tổng (Subset Sum MITM).
* **Quiz:** TBD (Xác định theo nội dung).
* **Bài tập phân tầng:** TBD (Xác định theo độ phủ kiến thức).

#### Lesson 06: Bitwise và Bitmask (`CPPB2-L06`)
* **Mục tiêu:** Tối ưu hóa biểu diễn tập hợp và vét cạn cấu hình qua phép toán bit.
* **Nội dung chính:**
  * **Core**: Các phép toán `&`, `|`, `^`, `~`; Phép dịch bit `<<`, `>>`; Kiểm tra, bật, tắt và đảo bit; Đếm số bit 1; Biểu diễn tập hợp bằng Bitmask; Duyệt các tập con.
  * **Extension**: Các hàm tối ưu `__builtin_popcountll`, `__builtin_ctzll`; Phép lấy bit thấp nhất `lowbit(x) = x & (-x)`.
  * **Challenge**: Kỹ thuật duyệt tất cả Submask của một Mask trong $\mathcal{O}(3^N)$: `for (int s = mask; s > 0; s = (s - 1) & mask)`.
* **Visual Plan:** Bảng biểu diễn nhị phân tập hợp $\{0, 1, ..., N-1\}$; Minh họa phép toán giao/hợp bit và cây duyệt Submask.
* **Ví dụ:** Kiểm tra số lũy thừa của 2; Tìm phần tử xuất hiện 1 lần bằng XOR; Bật/tắt bit; Duyệt toàn bộ tập con của một tập nhỏ.
* **Quiz:** TBD (Xác định theo nội dung).
* **Bài tập phân tầng:** TBD (Xác định theo độ phủ kiến thức).

---

### 📘 MODULE 04 — GREEDY VÀ QUY HOẠCH ĐỘNG CƠ BẢN

#### Lesson 07: Greedy (`CPPB2-L07`)
* **Mục tiêu:** Nắm vững tư duy lựa chọn tối ưu cục bộ và phương pháp chứng minh đúng đắn.
* **Nội dung chính:**
  * **Core**: Lựa chọn cục bộ và mục tiêu toàn cục; Quy luật chọn tối ưu; Sắp xếp kết hợp Greedy; Activity Selection; Khi nào Greedy đúng; Phản ví dụ khi Greedy thất bại.
  * **Extension**: Phương pháp chứng minh bằng đổi chỗ (Exchange Argument); Xếp lịch công việc (Interval Scheduling); Đổi tiền xu; Nối dây chi phí nhỏ nhất.
  * **Challenge**: Fractional Knapsack, Greedy kết hợp Heap/Priority Queue.
* **Visual Plan:** Trục thời gian xếp các đoạn hoạt động không giao nhau; Sơ đồ đổi chỗ chứng minh Exchange Argument.
* **Ví dụ:** Chọn nhiều hoạt động không giao nhau; Xếp lịch; Đổi tiền; Chọn vật phẩm hoặc công việc theo tiêu chí tối ưu.
* **Quiz:** TBD (Xác định theo nội dung).
* **Bài tập phân tầng:** TBD (Xác định theo độ phủ kiến thức).

#### Lesson 08: Dynamic Programming Cơ Bản (`CPPB2-L08`)
* **Mục tiêu:** Xây dựng mô hình trạng thái, bảng quy hoạch động và kỹ thuật truy vết cấu hình.
* **Nội dung chính:**
  * **Core**: Khái niệm trạng thái; Công thức chuyển; Giá trị khởi tạo; Thứ tự tính; Fibonacci; Xâu con chung; Xếp tiền; Truy hồi và lưu kết quả.
  * **Extension**: LIS tối ưu $\mathcal{O}(N \log N)$; 0/1 Knapsack tối ưu mảng 1D; LCS; Palindrome DP; Kỹ thuật truy vết tìm cấu hình tối ưu.
  * **Challenge**: Knapsack đổi trục trạng thái (Value-based DP), Unbounded Knapsack, Edit Distance.
* **Visual Plan:** Bảng DP lưới 2D và các mũi tên chuyển trạng thái; Sơ đồ mảng múp đơn điệu trong LIS $\mathcal{O}(N \log N)$.
* **Ví dụ:** Fibonacci; Coin Change; Longest Common Subsequence cơ bản; LIS $\mathcal{O}(N \log N)$; Truy vết nghiệm tối ưu.
* **Quiz:** TBD (Xác định theo nội dung).
* **Bài tập phân tầng:** TBD (Xác định theo độ phủ kiến thức).

---

### 📘 MODULE 05 — CẤU TRÚC DỮ LIỆU CƠ BẢN VÀ C++ LIBRARY

#### Lesson 09: Stack, Queue và Deque (`CPPB2-L09`)
* **Mục tiêu:** Khai thác cấu trúc đơn điệu giải quyết các bài toán biên lân cận và cửa sổ trượt.
* **Nội dung chính:**
  * **Core**: Nguyên tắc LIFO của Stack; Nguyên tắc FIFO của Queue; Deque và thao tác ở hai đầu; Monotonic Stack; Monotonic Queue; Sliding Window bằng Deque.
  * **Extension**: Next Greater Element (NGE), Previous Smaller Element (PSE); Kiểm tra dãy ngoặc; Đánh giá biểu thức RPN.
  * **Challenge**: Hình chữ nhật lớn nhất trên Histogram $\mathcal{O}(N)$, Trapping Rain Water.
* **Visual Plan:** Mô phỏng vào/ra LIFO/FIFO; Quá trình đẩy/bật phần tử trong Monotonic Stack; Cửa sổ trượt Deque 2 đầu.
* **Ví dụ:** Kiểm tra dãy ngoặc; Next Greater Element; Previous Smaller Element; Sliding Window Maximum.
* **Quiz:** TBD (Xác định theo nội dung).
* **Bài tập phân tầng:** TBD (Xác định theo độ phủ kiến thức).

#### Lesson 10: Thư Viện C++ (`CPPB2-L10`)
* **Mục tiêu:** Sử dụng thành thạo các cấu trúc dữ liệu chuẩn STL và đánh giá chính xác độ phức tạp.
* **Nội dung chính:**
  * **Core**: `vector`; `set` và `multiset`; `map`; `unordered_map`; Iterator; Tìm kiếm và sắp xếp bằng STL; Chọn container phù hợp; Độ phức tạp của các thao tác.
  * **Extension**: `priority_queue` (Max-heap/Min-heap); Iterator arithmetic (`auto it`, `prev`, `next`); Red-Black Tree vs Hash Table (xử lý Hash Collision).
  * **Challenge**: Kết hợp nhiều container quản lý dữ liệu động đa tiêu chí, tìm trung vị động bằng 2 Heap.
* **Visual Plan:** So sánh cấu trúc Red-Black Tree (cân bằng) vs Hash Table (buckets); Sơ đồ 2 Heap duy trì trung vị.
* **Ví dụ:** Đếm tần suất bằng `map`; Loại phần tử trùng bằng `set`; Tra cứu nhanh bằng `unordered_map`; Kết hợp container với sắp xếp.
* **Quiz:** TBD (Xác định theo nội dung).
* **Bài tập phân tầng:** TBD (Xác định theo độ phủ kiến thức).

#### Lesson 11: Các Bài Toán Tổ Hợp (`CPPB2-L11`)
* **Mục tiêu:** Nắm vững các quy tắc đếm, tam giác Pascal và tiền xử lý tổ hợp modulo.
* **Nội dung chính:**
  * **Core**: Quy tắc cộng và quy tắc nhân; Hoán vị; Chỉnh hợp; Tổ hợp `C(n,k)`; Tam giác Pascal; Tính tổ hợp bằng quy hoạch động; Tổ hợp theo modulo.
  * **Extension**: Tiền xử lý mảng giai thừa và nghịch đảo modulo tính $C_n^k \bmod (10^9+7)$ trong $\mathcal{O}(1)$; Nguyên lý bù trừ (PIE).
  * **Challenge**: Bài toán chia kẹo Euler (Stars and Bars), Số Catalan.
* **Visual Plan:** Tam giác Pascal và đường đi cộng dồn; Sơ đồ vách ngăn bài toán chia kẹo (Stars & Bars); Biểu đồ Venn nguyên lý bù trừ.
* **Ví dụ:** Tính số cách chọn $K$ phần tử; Tính $C(n,k)$ bằng Pascal; Đếm đường đi trên lưới; Bài toán chia kẹo.
* **Quiz:** TBD (Xác định theo nội dung).
* **Bài tập phân tầng:** TBD (Xác định theo độ phủ kiến thức).

---

### 📘 MODULE 06 — ĐỒ THỊ, CẤU TRÚC NÂNG CAO, CHUỖI VÀ SỐ LỚN

#### Lesson 12: Graph Theory (`CPPB2-L12`)
* **Mục tiêu:** Làm chủ biểu diễn đồ thị, các thuật toán duyệt BFS/DFS và bài toán loang trên lưới ma trận.
* **Nội dung chính:**
  * **Core**: Biểu diễn đồ thị; Danh sách kề; BFS; DFS; Thành phần liên thông; Phát hiện chu trình; Đồ thị trên lưới.
  * **Extension**: Tìm đường đi ngắn nhất không trọng số và truy vết đường đi bằng BFS; Flood Fill trên ma trận; Kiểm tra đồ thị 2 phía (2-Coloring).
  * **Challenge**: Multi-source BFS (lan tỏa dịch bệnh/cháy rừng), 0-1 BFS với `deque`.
* **Visual Plan:** Đồ thị và danh sách kề tương ứng; Sơ đồ lan tỏa lớp của BFS vs nhánh sâu của DFS; Lưới ma trận Flood Fill 4 hướng.
* **Ví dụ:** Duyệt toàn bộ đồ thị; Đếm thành phần liên thông; Tìm đường đi ngắn nhất không trọng số; Flood Fill trên ma trận.
* **Quiz:** TBD (Xác định theo nội dung).
* **Bài tập phân tầng:** TBD (Xác định theo độ phủ kiến thức).

#### Lesson 13: Fenwick Tree và Segment Tree (`CPPB2-L13`)
* **Mục tiêu:** Giải quyết bài toán truy vấn đoạn và cập nhật điểm động trong thời gian $\mathcal{O}(\log N)$.
* **Nội dung chính:**
  * **Core**: Truy vấn đoạn; Cập nhật điểm; Prefix Query; Fenwick Tree; Segment Tree; Build, Query và Update; So sánh Fenwick Tree với Segment Tree.
  * **Extension**: Cây Fenwick (BIT) tính tổng đoạn & đếm nghịch thế $\mathcal{O}(N \log N)$; Cây phân đoạn (Segment Tree) tìm Min/Max đoạn có cập nhật điểm.
  * **Challenge**: Nén tọa độ kết hợp Fenwick/Segment Tree.
* **Visual Plan:** Cây nhị phân Segment Tree quản lý đoạn $[L, R]$; Cấu trúc cây bước nhảy bit Fenwick Tree (`i & (-i)`).
* **Ví dụ:** Tổng đoạn có cập nhật; Đếm nghịch thế bằng Fenwick Tree; Truy vấn min/max bằng Segment Tree; Chọn cấu trúc dữ liệu theo loại truy vấn.
* **Quiz:** TBD (Xác định theo nội dung).
* **Bài tập phân tầng:** TBD (Xác định theo độ phủ kiến thức).

#### Lesson 14: Digit DP (`CPPB2-L14`)
* **Mục tiêu:** Thiết kế mô hình quy hoạch động chữ số đếm cấu hình trên đoạn số $[L, R]$ cực lớn.
* **Nội dung chính:**
  * **Core**: Trạng thái theo vị trí chữ số; Giới hạn `tight`; Tổng chữ số; Điều kiện chia hết; Số 0 ở đầu; Đếm số trong đoạn $[L, R]$.
  * **Extension**: Chuyển bài toán $[L, R] \to F(R) - F(L-1)$; Thiết kế hàm đệ quy nhớ `dp(idx, tight, leading_zero, sum, rem)`.
  * **Challenge**: Digit DP kết hợp điều kiện không chứa chữ số cấm / chữ số lặp lại.
* **Visual Plan:** Cây rẽ nhánh lựa chọn chữ số $0..9$; Sơ đồ biểu diễn ý nghĩa cờ biên `tight = 1` vs `tight = 0`.
* **Ví dụ:** Đếm số có tổng chữ số bằng $S$; Đếm số chia hết cho $K$; Đếm số không chứa một chữ số; Đếm số thỏa điều kiện trong $[L, R]$.
* **Quiz:** TBD (Xác định theo nội dung).
* **Bài tập phân tầng:** TBD (Xác định theo độ phủ kiến thức).

#### Lesson 15: String, String Hashing và Big Integer (`CPPB2-L15`)
* **Mục tiêu:** Nắm vững so khớp chuỗi $\mathcal{O}(1)$ bằng mã băm đa thức và xử lý số học chính xác không giới hạn chữ số.
* **Nội dung chính (Phân rã 3 cụm chuyên sâu):**
  * **15.1 — Xử lý xâu cơ bản & Đối xứng (Palindrome)**:
    * *Core*: Cắt ghép, so sánh xâu, kiểm tra tính đối xứng của chuỗi.
  * **15.2 — Kỹ thuật Băm chuỗi (String Hashing)**:
    * *Core*: Khái niệm băm xâu; Polynomial Rolling Hash; Hash đoạn con $S[L..R]$ trong $\mathcal{O}(1)$; So sánh nhiều đoạn xâu và khớp mẫu chuỗi.
    * *Extension*: Double Hashing chống xung đột testcase; Ứng dụng Hash kiểm tra Palindrome nhanh.
  * **15.3 — Xử lý Số nguyên lớn (Big Integer)**:
    * *Core*: Biểu diễn số nguyên lớn bằng `string` / `vector<int>`; Các phép toán Cộng, Trừ (không âm), Nhân số lớn với số nhỏ, Nhân hai số lớn $\mathcal{O}(N \times M)$.
    * *Challenge*: Phép trừ số lớn tổng quát có dấu; Phép chia số lớn cho số nhỏ; Phép chia lấy dư; Thuật toán tìm GCD hai số nguyên lớn.
* **Visual Plan:** Trục tiền tố băm chuỗi và công thức trích xuất hash $S[L..R]$; Đặt tính dọc phép cộng/nhân số lớn nhiều chữ số.
* **Ví dụ:** Kiểm tra Palindrome; So sánh hai đoạn con bằng Rolling Hash; Khớp mẫu chuỗi nhanh; Cộng, trừ và nhân hai số có nhiều chữ số.
* **Quiz:** TBD (Xác định theo nội dung 3 phần).
* **Bài tập phân tầng:** TBD (Xác định theo độ phủ kiến thức String + Hashing + BigInt).

---

## 6. TỔNG KẾT KHUNG QUẢN TRỊ KHÓA HỌC

```text
1 KHÓA HỌC LEVEL 2 (cpp-bang-b-level2)
└── 6 Module / Chương
    ├── Module 01: Số học và Modulo (2 lessons)
    ├── Module 02: Kỹ thuật tìm kiếm và xử lý mảng (2 lessons)
    ├── Module 03: Đệ quy, Chia để trị và Bitwise (2 lessons)
    ├── Module 04: Greedy và Quy hoạch động cơ bản (2 lessons)
    ├── Module 05: Cấu trúc dữ liệu cơ bản và C++ Library (3 lessons)
    └── Module 06: Đồ thị, cấu trúc nâng cao, chuỗi và số lớn (4 lessons)
```

| Thành phần | Quy tắc quản lý |
|---|:---:|
| **Khóa học** | **1** (`courses/cpp-bang-b-level2/`) |
| **Module / Chương** | **6** |
| **Lesson (Large Conceptual Unit)** | **15** |
| **Visual Plan** | **Bắt buộc** theo từng Lesson (Linh hoạt theo độ trừu tượng) |
| **Quiz mỗi Lesson** | **Linh hoạt** (Xác định theo nội dung thực tế) |
| **Bài tập mỗi Lesson** | **Linh hoạt** (Xác định theo độ phủ biến thể P0 $\to$ P5) |
| **Quiz cuối Module** | **Linh hoạt** (Theo mục tiêu đánh giá từng Module) |
| **Final Exam** | **Linh hoạt** (Đề thi tổng hợp bao quát) |
| **Tổng số Quiz & Problem toàn khóa** | **TBD** (Tổng kết chính xác sau khi hoàn thiện toàn bộ Lesson) |

---

## 7. QUY CHUẨN KỸ THUẬT BẮT BUỘC

1. **C++ Boilerplate Chuẩn Thi Đấu**:
   * Header duy nhất: `#include <bits/stdc++.h>` và `using namespace std;`.
   * Fast I/O: `ios::sync_with_stdio(false); cin.tie(nullptr);`.
   * Safe Input: `if (!(cin >> n >> ...)) return 0;`.
   * **Tuyệt đối 0 `std::`** và không include header riêng lẻ.
2. **Quy Chuẩn Problem Package Gồm 4 Thành Phần**:
   * `De_Bai.md` (giới hạn thời gian $1.0\text{s}$, bộ nhớ $256\text{MB}$).
   * `Huong_Dan_Giang_Day.md` (đủ 9 phần sư phạm chuyên sâu).
   * `solution.cpp` (biên dịch sạch `g++ -O3 -std=c++17`, Fast I/O, Safe Input).
   * Thư mục `test/` (20 testcases ma trận 6 tầng kèm `manifest.json`).
3. **Quy Chuẩn Trình Bày**:
   * Markdown Table + KaTeX formula chuẩn, **tuyệt đối không dùng ASCII Art vẽ khung**.
   * Callout tiếng Việt nhẹ nhàng: `> ⚠️ **Lưu ý:**` hoặc `> 💡 **Mẹo nhớ:**`.
