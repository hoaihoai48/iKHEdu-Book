# MASTER MODULE 02 DESIGN SPECIFICATION
## Module 02: Mảng Tiền Tố, Mảng Hiệu, Tìm Kiếm Nhị Phân & Phép Toán Bit (Prefix / Difference / Binary Search / Bit)

**Tài liệu tham chiếu chuẩn:** iKHEDU Curriculum Architecture v2  
**Đối tượng:** Học sinh học lập trình thi đấu (Tin học trẻ Bảng B, HSG THCS, Level 1)  
**Trạng thái:** 🔒 **GOLDEN SPECIFICATION — FROZEN**

---

## 00. Phân Bổ Quy Mô Linh Hoạt Theo Độ Sâu Chủ Đề (Flexible Topic Sizing)

> **Nguyên tắc sư phạm cốt lõi:** Số lượng câu hỏi Concept Quiz và Bài tập thực hành **không bị đóng khung cơ học**, mà được tùy biến mở rộng theo độ bao phủ, số lượng biến thể và độ phức tạp kỹ thuật của từng bài học.

| Đơn Vị Kiến Thức Lớn (Lesson) | Mã Viết Tắt | Số Lượng Quiz | Số Lượng Bài Tập | Dải Mã Bài Tập |
|---|:---:|:---:|:---:|---|
| **Lesson 01: Mảng Tiền Tố & Mảng Hiệu** | `PT` | **12 câu** | **16 bài** | `CPPB-PT-01` $\to$ `CPPB-PT-16` |
| **Lesson 02: Thuật Toán Tìm Kiếm Nhị Phân** | `BS` | **14 câu** | **18 bài** | `CPPB-BS-01` $\to$ `CPPB-BS-18` |
| **Lesson 03: Phép Toán Bit & Mặt Nạ Bit** | `BIT` | **12 câu** | **16 bài** | `CPPB-BIT-01` $\to$ `CPPB-BIT-16` |
| **TỔNG CỘNG MODULE 02** | | **38 câu** | **50 bài** | |

---

## 01. Module Contract & Scope Boundary

Module 02 tập trung vào hai kỹ thuật nền tảng tối ưu hóa thời gian từ $\mathcal{O}(N)$ xuống $\mathcal{O}(1)$ (Tiền xử lý mảng) và từ $\mathcal{O}(N)$ xuống $\mathcal{O}(\log N)$ (Chia đôi không gian tìm kiếm), kết hợp với thao tác bit cấp độ thanh ghi CPU:

$$\begin{aligned}
\text{Truy vấn tổng đoạn liên tục} &\xrightarrow[\text{Tiền xử lý } \mathcal{O}(N)]{\text{Prefix Sum}} \text{Trả lời truy vấn } \mathcal{O}(1) \\
\text{Cập nhật cộng đoạn } [L, R] &\xrightarrow[\text{Biến đổi mảng}]{\text{Difference Array}} \text{Cập nhật } \mathcal{O}(1) \to \text{Khôi phục } \mathcal{O}(N) \\
\text{Hàm kiểm tra đơn điệu } f(x) &\xrightarrow[\text{Chia đôi không gian}]{\text{Binary Search}} \text{Tìm nghiệm tối ưu } \mathcal{O}(\log(\text{Range})) \\
\text{Quản lý tập con } 2^N &\xrightarrow[\text{Thao tác bit}]{\text{Bitwise Mask}} \text{Biểu diễn & truy vấn } \mathcal{O}(1)
\end{aligned}$$

### Bảng Giới Hạn Phạm Vi (Allowed vs. Not Yet Boundary)

| Lớp Công Cụ | Được Phép Sử Dụng Trong Module 02 (Allowed) | TUYỆT ĐỐI CHƯA ĐƯỢC DÙNG (Not Yet) |
|---|---|---|
| **Cấu trúc dữ liệu** | `vector<long long>`, `vector<vector<long long>>` (Mảng 2D), Mảng tĩnh | `set`, `map`, `priority_queue`, Segment Tree, Fenwick Tree |
| **Thuật toán cơ sở** | Prefix Sum 1D/2D, Difference Array 1D/2D, Binary Search, `lower_bound`, Bitwise | Quy hoạch động nâng cao, Đồ thị, Chia để trị nâng cao, Hashing |
| **Toán học** | Modulo cơ bản, Cộng trừ nhân số nguyên `long long`, Bitwise AND/OR/XOR | Nghịch đảo modulo, Tổ hợp nâng cao, Hình học giải tích |

---

## 02. Ma Trận Bài Tập Chi Tiết Module 02 (50 Problems Total)

### 10.1. Lesson 01: Mảng Tiền Tố & Mảng Hiệu (16 bài `CPPB-PT-01` $\to$ `16`)

| STT | Mã Bài | Tên Bài Toán | Cấp Độ | Ràng Buộc Dữ Liệu | Mục Tiêu Rèn Luyện |
|:---:|:---:|---|:---:|---|---|
| 01 | `CPPB-PT-01` | **Truy Vấn Tổng Đoạn Con 1D** | `P0` | $N, Q \le 10^5$ | Prefix sum cơ bản $P[R] - P[L-1]$ |
| 02 | `CPPB-PT-02` | **Đếm Số Lượng Số Chẵn Trong Đoạn** | `P1` | $N, Q \le 10^5$ | Tiền tố trên mảng điều kiện logic |
| 03 | `CPPB-PT-03` | **Tìm Vị Trí Cân Bằng Của Mảng** | `P1` | $N \le 2 \cdot 10^5$ | Tổng trái bằng tổng phải |
| 04 | `CPPB-PT-04` | **Đoạn Con Có Tổng Bằng 0** | `P2` | $N \le 10^5$ | Nhận diện $P[i] == P[j]$ |
| 05 | `CPPB-PT-05` | **Cập Nhật Cộng Đoạn Tuyến Tính (Mảng Hiệu)** | `P2` | $N, Q \le 2 \cdot 10^5$ | Difference Array 1D cơ bản |
| 06 | `CPPB-PT-06` | **Trồng Cây Phủ Đoạn Tối Ưu** | `P3` | $N \le 10^5, Q \le 10^5$ | Mảng hiệu kết hợp quét mảng |
| 07 | `CPPB-PT-07` | **Truy Vấn Tổng Hình Chữ Nhật 2D** | `P1` | $N, M \le 1000, Q \le 10^5$ | Prefix sum 2D nguyên bản |
| 08 | `CPPB-PT-08` | **Tìm Hình Vuông $K \times K$ Có Tổng Lớn Nhất** | `P2` | $N, M \le 1000, K \le \min(N,M)$ | Quét cửa sổ 2D kết hợp Prefix 2D |
| 09 | `CPPB-PT-09` | **Cập Nhật Cộng Hình Chữ Nhật (Mảng Hiệu 2D)** | `P3` | $N, M \le 1000, Q \le 10^5$ | Difference Array 2D (4 góc) |
| 10 | `CPPB-PT-10` | **Đoạn Con Có Tổng Chia Hết Cho K** | `P3` | $N \le 2 \cdot 10^5, K \le 10^5$ | Mảng tiền tố kết hợp đồng dư |
| 11 | `CPPB-PT-11` | **Mảng Tiền Tố XOR Đoạn Con** | `P3` | $N, Q \le 2 \cdot 10^5$ | Tính chất $A \oplus A = 0$ trên Prefix XOR |
| 12 | `CPPB-PT-12` | **Đoạn Con Cân Bằng Số Lượng 0 và 1** | `P4` | $N \le 2 \cdot 10^5$ | Biến đổi $0 \to -1$ đưa về bài toán tổng 0 |
| 13 | `CPPB-PT-13` | **Truy Vấn Ma Trận Đa Vùng Cực Đại** | `P4` | $N, M \le 1500, Q \le 10^5$ | Tối ưu hóa bộ nhớ và truy vấn 2D |
| 14 | `CPPB-PT-14` | **Phân Phối Tài Nguyên Không Gian Tuyến Tính** | `P5` | $N, Q \le 2 \cdot 10^5$ | Mảng hiệu 2 tầng (Arithmetic Progression Update) |
| 15 | `CPPB-PT-15` | **Tìm Ma Trận Con Có Tổng Lớn Nhất (Max Submatrix)** | `P4` | $N, M \le 400$ | Nén 2D về 1D + Thuật toán Kadane kết hợp Prefix Sum |
| 16 | `CPPB-PT-16` | **Cân Bằng Tiền Tố Đa Chiều** | `P5` | $N \le 10^5$ | Cân bằng 3 trạng thái đồng thời |

---

### 10.2. Lesson 02: Thuật Toán Tìm Kiếm Nhị Phân (18 bài `CPPB-BS-01` $\to$ `18`)

| STT | Mã Bài | Tên Bài Toán | Cấp Độ | Ràng Buộc Dữ Liệu | Mục Tiêu Rèn Luyện |
|:---:|:---:|---|:---:|---|---|
| 01 | `CPPB-BS-01` | **Tìm Kiếm Phần Tử Trên Mảng Đã Sắp Xếp** | `P0` | $N, Q \le 10^5$ | Cài đặt Binary Search cơ bản |
| 02 | `CPPB-BS-02` | **Tìm Vị Trí Xuất Hiện Đầu Tiên & Cuối Cùng** | `P1` | $N, Q \le 10^5$ | Bản chất `lower_bound` / `upper_bound` |
| 03 | `CPPB-BS-03` | **Đếm Số Phần Tử Trong Đoạn $[L, R]$** | `P1` | $N, Q \le 10^5$ | Hiệu hai con trỏ nhị phân `upper - lower` |
| 04 | `CPPB-BS-04` | **Tìm Căn Bậc Hai Số Nguyên Lớn** | `P2` | $N \le 10^{18}$ | Binary Search trên tập số nguyên 64-bit |
| 05 | `CPPB-BS-05` | **Tìm Phần Tử Nhỏ Nhất Lớn Hơn X** | `P2` | $N, Q \le 10^5$ | Chặn trên nghiêm ngặt |
| 06 | `CPPB-BS-06` | **Chia Kẹo Cho Học Sinh Đạt Chuẩn** | `P3` | $N \le 10^5, K \le 10^{14}$ | Chặt nhị phân kết quả (Check chia đều) |
| 07 | `CPPB-BS-07` | **Cắt Gỗ Xây Dựng (Woodcutting / EKO)** | `P2` | $N \le 10^5, M \le 10^{14}$ | Bài toán kinh điển tìm độ cao máy cắt |
| 08 | `CPPB-BS-08` | **Đặt Trạm Phát Sóng Cách Nhau Xa Nhất (Aggressive Cows)** | `P3` | $N \le 10^5, C \le N$ | Tối đại hóa khoảng cách nhỏ nhất |
| 09 | `CPPB-BS-09` | **Chia Mảng Thành K Đoạn Có Tổng Max Nhỏ Nhất** | `P3` | $N \le 10^5, K \le N$ | Tối thiểu hóa tổng đoạn con lớn nhất |
| 10 | `CPPB-BS-10` | **Vận Chuyển Hàng Hóa Qua Phà Trong D Ngày** | `P3` | $N \le 10^5, D \le 10^5$ | Chặt nhị phân tải trọng thuyền |
| 11 | `CPPB-BS-11` | **Tìm Nghiệm Thực Của Phương Trình Đơn Điệu** | `P4` | Sai số $10^{-7}$ | Chặt nhị phân số thực với số lần lặp cố định |
| 12 | `CPPB-BS-12` | **Phần Tử Thứ K Của Hai Mảng Đã Sắp Xếp** | `P4` | $N, M \le 10^5$ | Chặt nhị phân số lượng phần tử $\le X$ |
| 13 | `CPPB-BS-13` | **Tìm Đoạn Con Có Trung Bình Lớn Nhất Độ Dài $\ge K$** | `P5` | $N \le 10^5, K \le N$ | Chặt nhị phân trung bình + Mảng tiền tố |
| 14 | `CPPB-BS-14` | **Tối Ưu Hóa Tuyến Đường Vận Tải Đa Điểm** | `P5` | $N \le 2 \cdot 10^5$ | Chặt nhị phân kết hợp cấu trúc đơn điệu |
| 15 | `CPPB-BS-15` | **Tìm Kiếm Trên Mảng Sắp Xếp Bị Xoay Vòng (Rotated Array)** | `P3` | $N \le 10^5$ | Phân đoạn đơn điệu trong mảng xoay |
| 16 | `CPPB-BS-16` | **Tìm Kiếm Trên Ma Trận 2D Đã Sắp Xếp (Matrix Search)** | `P2` | $N, M \le 1000$ | Chuyển tọa độ $1D \leftrightarrow 2D$ trong nhị phân |
| 17 | `CPPB-BS-17` | **Tìm Đỉnh Của Dãy Núi (Peak in Mountain Array)** | `P3` | $N \le 10^5$ | Chặt nhị phân theo đạo hàm / độ dốc |
| 18 | `CPPB-BS-18` | **Trung Vị Của Hai Mảng Đã Sắp Xếp (Median of Two Sorted)** | `P5` | $N, M \le 10^5$ | Phân chia vách ngăn nhị phân tối ưu $\mathcal{O}(\log(\min(N, M)))$ |

---

### 10.3. Lesson 03: Phép Toán Bit & Biểu Diễn Trạng Thái (16 bài `CPPB-BIT-01` $\to$ `16`)

| STT | Mã Bài | Tên Bài Toán | Cấp Độ | Ràng Buộc Dữ Liệu | Mục Tiêu Rèn Luyện |
|:---:|:---:|---|:---:|---|---|
| 01 | `CPPB-BIT-01` | **Bật, Tắt Và Kiểm Tra Bit Thứ K** | `P0` | $N \le 10^{18}, K \le 60$ | Thao tác `(1LL << k)`, `&`, `|`, `^` |
| 02 | `CPPB-BIT-02` | **Đếm Số Lượng Bit 1 (Popcount)** | `P1` | $N \le 10^{18}$ | `__builtin_popcountll` và thuật toán bit |
| 03 | `CPPB-BIT-03` | **Kiểm Tra Số Có Phải Lũy Thừa Của 2** | `P1` | $N \le 10^{18}$ | Kỹ thuật `n > 0 && (n & (n - 1)) == 0` |
| 04 | `CPPB-BIT-04` | **Tìm Phần Tử Xuất Hiện 1 Lần Duy Nhất** | `P2` | $N \le 2 \cdot 10^5$ | Tính chất tự triệt tiêu $A \oplus A = 0$ |
| 05 | `CPPB-BIT-05` | **Tìm Hai Số Xuất Hiện 1 Lần Duy Nhất** | `P2` | $N \le 2 \cdot 10^5$ | Phân tách nhóm bằng bit khác biệt đầu tiên |
| 06 | `CPPB-BIT-06` | **Đảo Bit Và Giá Trị Bù 1** | `P2` | $N \le 10^9$ | Phép toán NOT kết hợp mặt nạ |
| 07 | `CPPB-BIT-07` | **Duyệt Toàn Bộ $2^N$ Tập Con Bằng Mặt Nạ Bit** | `P2` | $N \le 20$ | `for (int mask = 0; mask < (1 << n); ++mask)` |
| 08 | `CPPB-BIT-08` | **Bài Toán Tổng Tập Con Bằng S (Subset Sum)** | `P3` | $N \le 20, S \le 10^9$ | Duyệt nhị phân vét cạn $2^N$ |
| 09 | `CPPB-BIT-09` | **Chia Tập Hợp Thành 2 Phần Có Tổng Chênh Lệch Nhỏ Nhất** | `P3` | $N \le 20$ | Vét cạn bitmask tối ưu hiệu |
| 10 | `CPPB-BIT-10` | **Đếm Cặp Có Tích Bit AND Bằng 0** | `P3` | $N \le 10^5, A_i < 2^{16}$ | Tần suất bit và kiểm tra tương thích |
| 11 | `CPPB-BIT-11` | **Tìm Cặp Có XOR Lớn Nhất Trong Mảng** | `P4` | $N \le 10^5, A_i \le 10^9$ | Duyệt từng bit từ cao xuống thấp (Greedy Bit) |
| 12 | `CPPB-BIT-12` | **Duyệt Tất Cả Các Tập Con Của Một Mặt Nạ Bit** | `P4` | $N \le 18$ | Kỹ thuật `submask = (submask - 1) & mask` |
| 13 | `CPPB-BIT-13` | **Tìm Dãy Con Có Tổng XOR Bằng K** | `P4` | $N \le 22$ | Vét cạn nâng cao kết hợp bit |
| 14 | `CPPB-BIT-14` | **Tối Ưu Hóa Gán Việc Cho N Người (N <= 20)** | `P5` | $N \le 20$ | Bitmask trạng thái và tối ưu hóa tổ hợp |
| 15 | `CPPB-BIT-15` | **Đếm Số Cặp Có Tổng Bằng Lũy Thừa Của 2** | `P3` | $N \le 10^5, A_i \le 10^9$ | Kết hợp bitmask và hai con trỏ / chặt nhị phân |
| 16 | `CPPB-BIT-16` | **Tập Hợp Độc Lập Về Bit Lớn Nhất** | `P4` | $N \le 24$ | Bitmask đồ thị độc lập cực đại |
