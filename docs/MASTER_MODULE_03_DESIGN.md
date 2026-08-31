# ĐẶC TẢ THIẾT KẾ MASTER MODULE 03 (GOLDEN SPECIFICATION)
## CHUYÊN ĐỀ: SỐ HỌC, ĐỒNG DƯ THỨC & SỐ NGUYÊN LỚN (NUMBER THEORY / MODULO / BIG INTEGER)

---

## 01. Tổng Quan Kiến Trúc & Ranh Giới Công Cụ (Architecture Overview)

### Tuyên Ngôn Triết Lý Module 03:
> *"Lý thuyết số trong Competitive Programming là nghệ thuật thu hẹp không gian tìm kiếm từ $\mathcal{O}(N)$ xuống $\mathcal{O}(\sqrt{N})$ và $\mathcal{O}(\log N)$, đồng thời kiểm soát tuyệt đối tính bất biến của các phép toán trên vành đồng dư và xử lý các giá trị vượt giới hạn 64-bit mà không làm tràn số."*

$$\begin{aligned}
\text{Phân tích số học } N &\xrightarrow[\text{Thừa số nguyên tố / Sàng}]{\text{Prime Factorization}} \text{Thuật toán tối ưu } \mathcal{O}(\sqrt{N}) \text{ hoặc } \mathcal{O}(\log N) \\
\text{Tính toán lũy thừa } A^B \pmod M &\xrightarrow[\text{Chia để trị nhị phân}]{\text{Binary Exponentiation}} \text{Thời gian thực thi } \mathcal{O}(\log B) \\
\text{Số nguyên siêu lớn } 10^{1000} &\xrightarrow[\text{Mảng chữ số / String}]{\text{Big Integer Arithmetic}} \text{Đại số đa độ chính xác } \mathcal{O}(L)
\end{aligned}$$

---

### Bảng Giới Hạn Phạm Vi (Allowed vs. Not Yet Boundary)

| Lớp Công Cụ | Được Phép Sử Dụng Trong Module 03 (Allowed) | TUYỆT ĐỐI CHƯA ĐƯỢC DÙNG (Not Yet) |
|---|---|---|
| **Cấu trúc dữ liệu** | `string`, `vector<int>`, `vector<long long>`, Mảng tĩnh, Mảng chữ số | `set`, `map`, `priority_queue`, Segment Tree, Fenwick Tree |
| **Thuật toán cơ sở** | Euclid GCD/LCM, Sàng Eratosthenes, Sàng SPF, Lũy thừa nhị phân, Euclid mở rộng, Fermat nhỏ, BigInt $\mathcal{O}(L^2)$ | FFT / NTT (Nhân số lớn nhanh), Pollard's Rho, Miller-Rabin ngẫu nhiên, CRT nâng cao |
| **Toán học** | Số nguyên tố, Ước số, Đồng dư Modulo, Nghịch đảo Modulo, Lũy thừa số học | Hình học giải tích, Đại số tuyến tính ma trận nâng cao, Tích phân số |

---

## 02. Ma Trận Bài Tập Chi Tiết Module 03 (48 Problems Total)

### 10.1. Lesson 01: Ước Số, Bội Số & Số Nguyên Tố (16 bài `CPPB-NT-01` $\to$ `16`)

| STT | Mã Bài | Tên Bài Toán | Cấp Độ | Ràng Buộc Dữ Liệu | Mục Tiêu Rèn Luyện & Dạng Thuật Toán |
|:---:|:---:|---|:---:|---|---|
| 01 | `CPPB-NT-01` | **Ước Chung Lớn Nhất & Bội Chung Nhỏ Nhất** | `P0` | $A, B \le 10^{18}$ | Thuật toán Euclid tối ưu và công thức $LCM = \frac{A}{\gcd(A, B)} \times B$ |
| 02 | `CPPB-NT-02` | **Kiểm Tra Số Nguyên Tố Cơ Bản** | `P0` | $N \le 10^{12}$ | Kiểm tra nguyên tố trong $\mathcal{O}(\sqrt{N})$ với bước nhảy 6k $\pm$ 1 |
| 03 | `CPPB-NT-03` | **Phân Tích Thừa Số Nguyên Tố** | `P1` | $N \le 10^{14}$ | Phân tích $N = p_1^{a_1} p_2^{a_2} \dots p_k^{a_k}$ trong $\mathcal{O}(\sqrt{N})$ |
| 04 | `CPPB-NT-04` | **Đếm Số Lượng & Tính Tổng Các Ước** | `P1` | $N \le 10^{14}$ | Ứng dụng công thức nhân tính $\sigma_0(N)$ và $\sigma_1(N)$ |
| 05 | `CPPB-NT-05` | **Số Chính Phương & Số Lập Phương** | `P1` | $N \le 10^{18}$ | Nhận diện số có số lượng ước lẻ bằng chặt nhị phân số nguyên |
| 06 | `CPPB-NT-06` | **Sàng Nguyên Tố Eratosthenes Kinh Điển** | `P2` | $N \le 10^7$ | Cài đặt sàng nguyên tố với mảng `vector<bool>` tối ưu bộ nhớ |
| 07 | `CPPB-NT-07` | **Đếm Số Nguyên Tố Trong Đoạn [L, R]** | `P2` | $R \le 10^7, Q \le 10^5$ | Tiền xử lý Sàng Eratosthenes kết hợp Mảng Tiền Tố |
| 08 | `CPPB-NT-08` | **Sàng Ước Nguyên Tố Nhỏ Nhất (SPF)** | `P2` | $N \le 10^6, Q \le 10^5$ | Phân tích thừa số nguyên tố cực nhanh trong $\mathcal{O}(\log N)$ mỗi truy vấn |
| 09 | `CPPB-NT-09` | **Sàng Phân Đoạn (Segmented Sieve)** | `P3` | $R - L \le 10^6, R \le 10^{12}$ | Sàng nguyên tố trên khoảng lớn bằng các số nguyên tố $\le \sqrt{R}$ |
| 10 | `CPPB-NT-10` | **Cặp Số Nguyên Tố Sinh Đôi (Twin Primes)** | `P3` | $N \le 10^7$ | Tìm các cặp số nguyên tố $(p, p+2)$ bằng Sàng Eratosthenes |
| 11 | `CPPB-NT-11` | **Số Hoàn Hảo & Định Lý Euclid-Euler** | `P3` | $N \le 10^{18}$ | Kiểm tra số hoàn hảo dạng $2^{p-1}(2^p - 1)$ với $2^p - 1$ là số nguyên tố Mersenne |
| 12 | `CPPB-NT-12` | **Số Có Đúng 3 Ước Số** | `P3` | $N \le 10^{12}$ | Nhận diện số có dạng $p^2$ với $p$ là số nguyên tố |
| 13 | `CPPB-NT-13` | **Số Gần Nguyên Tố (Almost Prime)** | `P4` | $N \le 10^7$ | Sàng đếm số lượng ước nguyên tố phân biệt của mọi số $\le N$ |
| 14 | `CPPB-NT-14` | **Phân Tích Giai Thừa Ra Thừa Số (Legendre)** | `P4` | $N \le 10^6, P \le 10^6$ | Công thức Legendre $E_p(N!) = \sum \lfloor \frac{N}{p^k} \rfloor$ tìm số mũ của $p$ |
| 15 | `CPPB-NT-15` | **Đếm Số Số Không Tận Cùng Của N!** | `P4` | $N \le 10^{18}$ | Ứng dụng công thức Legendre đếm số mũ của 5 trong $N!$ |
| 16 | `CPPB-NT-16` | **Số Học Cực Hạn: Cặp Nguyên Tố Cùng Nhau Cực Đại** | `P5` | $N \le 10^6$ | Ứng dụng hàm Phi Euler $\phi(N)$ và sàng số học đa năng |

---

### 10.2. Lesson 02: Đồng Dư Modulo, Lũy Thừa Nhị Phân & Nghịch Đảo Modulo (16 bài `CPPB-MOD-01` $\to$ `16`)

> **Phân tầng lộ trình:** 
> * **Core Foundations (`CPPB-MOD-01` $\to$ `09`):** Nhóm kiến thức bắt buộc cho học sinh Bảng B.
> * **Advanced Challenge (`CPPB-MOD-10` $\to$ `16`):** Nhóm chuyên đề mở rộng nâng cao.

| STT | Mã Bài | Tên Bài Toán | Cấp Độ | Phân Loại | Ràng Buộc Dữ Liệu | Mục Tiêu Rèn Luyện & Dạng Thuật Toán |
|:---:|:---:|---|:---:|:---:|---|---|
| 01 | `CPPB-MOD-01` | **Phép Tính Đồng Dư Cơ Bản (+, -, \*)** | `P0` | **Core** | $A, B \le 10^{18}, M = 10^9+7$ | Quy tắc cộng trừ nhân đồng dư và xử lý số âm `(a % m + m) % m` |
| 02 | `CPPB-MOD-02` | **Lũy Thừa Nhị Phân Cơ Bản ($A^B \pmod M$)** | `P0` | **Core** | $A, B \le 10^{18}, M \le 10^9+7$ | Lũy thừa nhị phân lặp $\mathcal{O}(\log B)$ |
| 03 | `CPPB-MOD-03` | **Lũy Thừa Chuỗi Số Lớn ($A^B \pmod M$ với $B$ là chuỗi)** | `P1` | **Core** | $A \le 10^9, |B| \le 10^5, M = 10^9+7$ | Định lý Fermat nhỏ và rút gọn số mũ $B \pmod{M - 1}$ ($\gcd(A, M) = 1$) |
| 04 | `CPPB-MOD-04` | **Nhân Ấn Độ Chống Tràn Số ($A \times B \pmod M$)** | `P1` | **Core** | $A, B, M \le 10^{18}$ | Nhân nhân đôi nhị phân $\mathcal{O}(\log B)$ hoặc dùng `__int128` |
| 05 | `CPPB-MOD-05` | **Tính Tổng Cấp Số Nhân Đồng Dư** | `P2` | **Core** | $A, N \le 10^{18}, M = 10^9+7$ | Chia để trị tính $S = 1 + A + A^2 + \dots + A^N \pmod M$ |
| 06 | `CPPB-MOD-06` | **Nghịch Đảo Modulo Bằng Định Lý Fermat Nhỏ** | `P2` | **Core** | $A \le 10^9, M = 10^9+7$ (Nguyên tố) | Tính $A^{-1} \equiv A^{M-2} \pmod M$ |
| 07 | `CPPB-MOD-07` | **Nghịch Đảo Modulo Bằng Thuật Toán Euclid Mở Rộng** | `P2` | **Core** | $A, M \le 10^9, \gcd(A, M) = 1$ | Giải phương trình Diophantine $Ax + My = 1$ |
| 08 | `CPPB-MOD-08` | **Phép Chia Đồng Dư $\frac{A}{B} \pmod M$** | `P2` | **Core** | $A, B \le 10^{18}, M = 10^9+7$ | Thực hiện $A \times B^{-1} \pmod M$ |
| 09 | `CPPB-MOD-09` | **Tính Số Tổ Hợp $C(N, K) \pmod M$** | `P3` | **Core** | $N, K \le 10^6, M = 10^9+7$ | Tiền xử lý Giai thừa và Nghịch đảo Giai thừa trong $\mathcal{O}(N)$ |
| 10 | `CPPB-MOD-10` | **Tính Số Chỉnh Hợp $A(N, K) \pmod M$** | `P3` | *Advanced* | $N, K \le 10^6, M = 10^9+7$ | Công thức $A(N, K) = \frac{N!}{(N-K)!} \pmod M$ |
| 11 | `CPPB-MOD-11` | **Dãy Fibonacci Đồng Dư Lớn** | `P3` | *Advanced* | $N \le 10^{18}, M = 10^9+7$ | Nhân ma trận nhị phân $\mathcal{O}(\log N)$ tính $F_N \pmod M$ |
| 12 | `CPPB-MOD-12` | **Số Catalan Đồng Dư $C_N \pmod M$** | `P3` | *Advanced* | $N \le 10^6, M = 10^9+7$ | Công thức $C_N = \frac{1}{N+1} C(2N, N) \pmod M$ |
| 13 | `CPPB-MOD-13` | **Lũy Thừa Tầng (Tower of Powers)** | `P4` | *Advanced* | $A, B, C \le 10^9, M = 10^9+7$ | Tính $A^{B^C} \pmod M$ bằng định lý Euler / Fermat nhỏ |
| 14 | `CPPB-MOD-14` | **Nghịch Đảo Tuyến Tính $1 \dots N$ Trong $\mathcal{O}(N)$** | `P4` | *Advanced* | $N \le 10^7, M = 10^9+7$ | Công thức hồi quy $inv[i] = -(M / i) \times inv[M \% i] \pmod M$ |
| 15 | `CPPB-MOD-15` | **Giải Phương Trình Đồng Dư Tuyến Tính $Ax \equiv B \pmod M$** | `P4` | *Advanced* | $A, B, M \le 10^9$ | Thuật toán Euclid mở rộng tổng quát tìm nghiệm nhỏ nhất |
| 16 | `CPPB-MOD-16` | **Đồng Dư Cực Hạn: Căn Bậc Hai Modulo (Tonelli-Shanks)** | `P5` | *Advanced* | $A, P \le 10^9, P \text{ nguyên tố}$ | Giải phương trình $x^2 \equiv A \pmod P$ |

---

### 10.3. Lesson 03: Xử Lý Số Nguyên Lớn Big Integer (16 bài `CPPB-BIG-01` $\to$ `16`)

> **Phân tầng lộ trình:**
> * **Core Foundations (`CPPB-BIG-01` $\to$ `12`):** Nhóm kiến thức bắt buộc mô phỏng 4 phép tính, Giai thừa, Lũy thừa, Fibonacci, Tổng chữ số.
> * **Advanced Challenge (`CPPB-BIG-13` $\to$ `16`):** Nhóm chuyên đề mở rộng nâng cao (Chia 2 số lớn, Căn bậc hai, Binary GCD, Tổ hợp chính xác).

| STT | Mã Bài | Tên Bài Toán | Cấp Độ | Phân Loại | Ràng Buộc Dữ Liệu | Mục Tiêu Rèn Luyện & Dạng Thuật Toán |
|:---:|:---:|---|:---:|:---:|---|---|
| 01 | `CPPB-BIG-01` | **So Sánh Hai Số Nguyên Lớn** | `P0` | **Core** | $|A|, |B| \le 1000$ | So sánh độ dài và so sánh từ điển chuỗi số lớn |
| 02 | `CPPB-BIG-02` | **Cộng Hai Số Nguyên Lớn (BigInt + BigInt)** | `P0` | **Core** | $|A|, |B| \le 10000$ | Thuật toán cộng có nhớ trên chuỗi/mảng chữ số |
| 03 | `CPPB-BIG-03` | **Trừ Hai Số Nguyên Lớn (BigInt - BigInt)** | `P1` | **Core** | $|A|, |B| \le 10000, A \ge B$ | Thuật toán trừ có mượn trên chuỗi |
| 04 | `CPPB-BIG-04` | **Trừ Hai Số Nguyên Lớn Có Dấu (Hỗ Trợ $A < B$)** | `P1` | **Core** | $|A|, |B| \le 10000$ | Xử lý số âm khi $A < B$ và in dấu trừ |
| 05 | `CPPB-BIG-05` | **Nhân Số Nguyên Lớn Với Số Nhỏ (BigInt $\times$ int)** | `P1` | **Core** | $|A| \le 10000, B \le 10^9$ | Nhân số lớn với số nguyên 32-bit |
| 06 | `CPPB-BIG-06` | **Nhân Hai Số Nguyên Lớn (BigInt $\times$ BigInt)** | `P2` | **Core** | $|A|, |B| \le 1000$ | Thuật toán nhân tay đặt tính $\mathcal{O}(|A| \times |B|)$ |
| 07 | `CPPB-BIG-07` | **Chia Số Nguyên Lớn Cho Số Nhỏ (BigInt / int)** | `P2` | **Core** | $|A| \le 10000, B \le 10^9$ | Chia lấy thương nguyên và dồn số dư Horner |
| 08 | `CPPB-BIG-08` | **Chia Lấy Dư Số Nguyên Lớn Cho Số Nhỏ (BigInt % int)** | `P2` | **Core** | $|A| \le 10^5, B \le 10^{18}$ | Tính $A \pmod B$ bằng vòng lặp Horner $\mathcal{O}(|A|)$ |
| 09 | `CPPB-BIG-09` | **Tính Giai Thừa Số Lớn ($N!$)** | `P3` | **Core** | $N \le 1000$ | Dồn phép nhân BigInt $\times$ int liên tiếp |
| 10 | `CPPB-BIG-10` | **Lũy Thừa Số Nguyên Lớn ($A^B$)** | `P3` | **Core** | $A \le 100, B \le 1000$ | Lũy thừa nhị phân kết hợp nhân BigInt |
| 11 | `CPPB-BIG-11` | **Tính Số Fibonacci Lớn ($F_N$)** | `P3` | **Core** | $N \le 1000$ | Dồn phép cộng BigInt + BigInt quy hoạch động |
| 12 | `CPPB-BIG-12` | **Tổng Các Chữ Số Của $N!$ hoặc $2^N$** | `P3` | **Core** | $N \le 1000$ | Tính số lớn và tính tổng chữ số |
| 13 | `CPPB-BIG-13` | **Chia Hai Số Nguyên Lớn (BigInt / BigInt)** | `P4` | *Advanced* | $|A|, |B| \le 500$ | Thuật toán chia chặt nhị phân thương số hoặc Long Division |
| 14 | `CPPB-BIG-14` | **Căn Bậc Hai Số Nguyên Lớn ($\lfloor \sqrt{\text{BigInt}} \rfloor$)** | `P4` | *Advanced* | $|A| \le 500$ | Chặt nhị phân trên không gian chuỗi số lớn |
| 15 | `CPPB-BIG-15` | **Ước Chung Lớn Nhất Của Hai Số Lớn ($\gcd(\text{BigInt}, \text{BigInt})$)** | `P4` | *Advanced* | $|A|, |B| \le 500$ | Thuật toán Binary GCD (Stein's Algorithm) trên BigInt |
| 16 | `CPPB-BIG-16` | **Số Lớn Cực Hạn: Tổ Hợp $C(N, K)$ Chính Xác** | `P5` | *Advanced* | $N, K \le 100$ | Phân tích thừa số nguyên tố kết hợp nhân lũy thừa số lớn |

---

## 03. Kế Hoạch Triển Khai Tiếp Theo
1. **Biên soạn `Lesson07_Production_Content.md`** (Ước số, Bội số & Số nguyên tố).
2. **Biên soạn `Lesson08_Production_Content.md`** (Đồng dư Modulo, Lũy thừa nhị phân & Nghịch đảo Modulo).
3. **Biên soạn `Lesson09_Production_Content.md`** (Xử lý Số nguyên lớn Big Integer).
4. **Khởi tạo 48 Problem Packages** (`CPPB-NT-01..16`, `CPPB-MOD-01..16`, `CPPB-BIG-01..16`) kèm 20 testcases chuẩn/bài.
