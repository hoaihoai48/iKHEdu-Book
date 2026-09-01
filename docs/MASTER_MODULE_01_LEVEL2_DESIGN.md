# MASTER MODULE 01 (LEVEL 2) DESIGN SPECIFICATION
## Module 01: Số Học Nâng Cao, Modulo & Toán Lập Trình (Number Theory & Modular Arithmetic)

> **Tài liệu tham chiếu chuẩn:** iKHEDU Curriculum Architecture v2 & `docs/MASTER_LEVEL2_PLAN.md`  
> **Đối tượng:** Học sinh THCS ôn thi HSG Tỉnh/Thành phố & Tin học trẻ Bảng B (Level 2)  
> **Trạng thái:** 🔒 **GOLDEN SPECIFICATION — LEVEL 2 MODULE 01**

---

## 00. Kiến Trúc Phân Cấp & Định Danh Problem Độc Lập

Toàn bộ hệ sinh thái học liệu Level 2 tuân thủ nghiêm ngặt mô hình 5 tầng:
$$\text{PROGRAM (C++ Level 2)} \longrightarrow \text{MODULE 01 (Số Học & Modulo)} \longrightarrow \text{LESSON (2 Master Lessons)} \longrightarrow \text{CONCEPT} \longrightarrow \text{ACTIVITY / PROBLEM (CPPB2-L01-xx, CPPB2-L02-xx)}$$

* **Problem Identity:** Mã bài toán dạng `CPPB2-L01-xx` và `CPPB2-L02-xx` là thực thể bài toán độc lập trong Problem Library toàn hệ thống.
* **Quy chuẩn Problem Package gồm 4 thành phần:**
  1. `De_Bai.md` (Statement, Time Limit $1.0\text{s}$, Memory Limit $256\text{MB}$).
  2. `Huong_Dan_Giang_Day.md` (9 phần sư phạm chuyên sâu: Mục tiêu, Phân tích đề, Socratic Questioning, Invariant, Dry Run Table, Độ phức tạp, Bug Traps, Code C++ chuẩn, Bài toán mở rộng).
  3. `solution.cpp` (Fast I/O, Safe Input, `#include <bits/stdc++.h>`, `using namespace std;`, 0 `std::`, biên dịch sạch `g++ -O3 -std=c++17`).
  4. Thư mục `test/` (Trọn bộ testcases ma trận 6 tầng kèm `manifest.json`).

---

## 01. Module Contract & Phạm Vi Kiến Thức (Scope Boundary)

Module 01 kế thừa nền tảng từ Level 1 (`#03 Số học` và `#10 Modulo`), tập trung vào **Tái kết hợp & Nâng cao kỹ thuật (Hybrid Techniques)**:

$$\text{Phép tính số học lớn / Đồng dư thức} \xrightarrow[\text{Phân tích}]{\text{Định lý số học}} \text{Euclid mở rộng / Sàng SPF / Fermat} \xrightarrow[\text{Tối ưu hóa}]{\text{Fast Power / Modular Inverse}} \text{Độ phức tạp } \mathcal{O}(\log N) \text{ / } \mathcal{O}(1) \text{ mỗi truy vấn}$$

### Bảng Giới Hạn Phạm Vi (Allowed vs. Not Yet Boundary)
| Lớp Công Cụ | Được phép sử dụng trong Module 01 (Allowed) | TUYỆT ĐỐI CHƯA DÙNG (Not Yet) |
|---|---|---|
| **Thuật toán & Kỹ thuật** | Euclid mở rộng, Sàng SPF $\mathcal{O}(\log N)$, Sàng đoạn $[L, R]$, Fast Power, Nhân Ấn Độ / `__int128_t`, Nghịch đảo Modulo Fermat/Euclid, Euler Phi $\phi(N)$ | Cây Fenwick / Segment Tree, Quy hoạch động, BFS/DFS Đồ thị, String Hashing |
| **Cấu trúc dữ liệu** | `vector<int>`, `vector<long long>`, Mảng tĩnh 1D/2D, `vector<vector<long long>>` | `set`, `map`, `priority_queue` (để dành cho Module 05) |

---

## 02. Chuẩn Đầu Ra Module 01 (Learning Outcomes)

* **`LO-01 (Advanced Number Theory & SPF)`**: Làm chủ sàng SPF (Smallest Prime Factor) để tiền xử lý $\mathcal{O}(N)$ và phân tích thừa số nguyên tố cho hàng triệu truy vấn với độ phức tạp $\mathcal{O}(\log N)$ mỗi truy vấn.
* **`LO-02 (Segmented Sieve & Range Primes)`**: Cài đặt thành thạo thuật toán Sàng đoạn trên dải $[L, R]$ với $R \le 10^{12}$ và $R - L \le 10^6$.
* **`LO-03 (Extended Euclidean & Linear Diophantine)`**: Hiểu bản chất và cài đặt thuật toán Euclid mở rộng, tìm nghiệm nguyên phương trình $Ax + By = C$ và tìm nghịch đảo modulo khi $M$ không nguyên tố.
* **`LO-04 (Modular Arithmetic & Inverse)`**: Vận dụng thành thạo nghịch đảo modulo (Fermat & Euclid) để thực hiện phép chia đồng dư $\frac{A}{B} \bmod M = (A \times B^{-1}) \bmod M$ và rút gọn biểu thức phân số lớn.
* **`LO-05 (Fast Exponentiation & Large Modulo)`**: Cài đặt lũy thừa nhị phân nhanh $\mathcal{O}(\log B)$, áp dụng nhân Ấn Độ chống tràn số và định lý Euler hạ bậc số mũ lớn $A^B \bmod M = A^{B \bmod \phi(M)} \bmod M$.

---

## 03. Cấu Trúc 2 Master Lessons Module 01

### 📘 LESSON 01: SỐ HỌC CƠ BẢN & CHUYÊN SÂU (`CPPB2-L01`)
* **1. Mục tiêu học tập:** Phân tích thừa số nguyên tố $\mathcal{O}(\log N)$, sàng đoạn lớn và giải phương trình Diophantine tuyến tính.
* **2. Nội dung chính:**
  * **Core (Bắt buộc):** Chia hết, ước và bội; GCD và LCM; Thuật toán Euclid; Kiểm tra số nguyên tố $\mathcal{O}(\sqrt{N})$; Phân tích thừa số nguyên tố.
  * **Extension (Mở rộng):** Sàng Eratosthenes, Sàng đoạn $[L, R]$ ($R \le 10^{12}, R - L \le 10^6$), Sàng SPF phân tích thừa số $\mathcal{O}(\log N)$.
  * **Challenge (Nâng cao):** Thuật toán Euclid mở rộng giải $Ax + By = \gcd(A, B)$, Nghiệm phương trình Diophantine, Hàm phi Euler $\phi(N)$.
* **3. Visual Plan (Sơ đồ trực quan):**
  * `cppb2_l01_visual_01_euclid_trace.png`: Sơ đồ hình học thu hẹp diện tích của thuật toán Euclid.
  * `cppb2_l01_visual_02_spf_sieve.png`: Mô phỏng mảng `spf[i]` lưu ước số nguyên tố nhỏ nhất và chuỗi truy vết chia liên tiếp.
  * `cppb2_l01_visual_03_segmented_sieve.png`: Trục số ánh xạ đoạn $[L, R]$ về mảng cơ sở $0 \dots R-L$.
* **4. Ví dụ minh họa:**
  * *Ví dụ 1:* Cài đặt hàm `gcd(a, b)` và `extgcd(a, b, x, y)`.
  * *Ví dụ 2:* Tiền xử lý mảng `spf` và hàm phân tích `vector<pair<int, int>> factorize(int n)`.
  * *Ví dụ 3:* Cài đặt thuật toán Sàng đoạn đếm số nguyên tố trong $[L, R]$.
* **5. Concept Quiz:** 12–14 câu trắc nghiệm bản chất, bẫy tràn số và biên độ.
* **6. Bài tập phân tầng (Problem Packages):** Phân tầng P0 $\to$ P5 từ củng cố đến bài thi HSG.

---

### 📘 LESSON 02: MODULO VÀ FAST POWER (`CPPB2-L02`)
* **1. Mục tiêu học tập:** Làm chủ tính toán đồng dư thức, phép chia modulo qua nghịch đảo và lũy thừa nhanh với số mũ cực lớn.
* **2. Nội dung chính:**
  * **Core (Bắt buộc):** Các phép cộng, trừ, nhân modulo; Đồng dư; Phép chia modulo; Nghịch đảo modulo (Modular Inverse); Lũy thừa nhanh (Fast Power); Xử lý số lớn trong phép tính modulo.
  * **Extension (Mở rộng):** Phép nhân Ấn Độ / `__int128_t` chống tràn số khi $M \approx 10^{18}$; Nghịch đảo modulo bằng định lý Fermat nhỏ ($A^{M-2} \bmod M$) và Euclid mở rộng; Rút gọn phân số lớn theo modulo.
  * **Challenge (Nâng cao):** Lũy thừa với số mũ cực lớn $A^B \bmod M$ qua hạ bậc Euler $\phi(M)$; Tiền xử lý mảng nghịch đảo tuyến tính $\mathcal{O}(N)$.
* **3. Visual Plan (Sơ đồ trực quan):**
  * `cppb2_l02_visual_01_modulo_circle.png`: Vòng tròn chu kỳ đồng dư thức modulo $M$.
  * `cppb2_l02_visual_02_fast_power_tree.png`: Cây phân rã nhị phân của thuật toán Fast Power $\mathcal{O}(\log B)$.
* **4. Ví dụ minh họa:**
  * *Ví dụ 1:* Hàm lũy thừa nhị phân `power(a, b, m)`.
  * *Ví dụ 2:* Tính nghịch đảo modulo `modInverse(a, m)` bằng Fermat và Euclid mở rộng.
  * *Ví dụ 3:* Tính giá trị phân số $\frac{P}{Q} \bmod (10^9+7)$ và kiểm tra trường hợp $\gcd(Q, M) \ne 1$.
* **5. Concept Quiz:** 12–14 câu trắc nghiệm bẫy số âm trong modulo, số mũ lớn, điều kiện nghịch đảo.
* **6. Bài tập phân tầng (Problem Packages):** Phân tầng P0 $\to$ P5 bao quát trọn vẹn Fast Power, Inverse và bài toán số học tổ hợp.

---

## 04. QA Checklist & Verification Protocol

Mọi nội dung biên soạn và package bài tập trong Module 01 bắt buộc phải vượt qua QA Gate:
1. **Source & Context Integrity:** Đúng source-of-truth, không bịa số liệu, không trùng mã bài duplicate.
2. **C++ Code Standards:** Biên dịch sạch `g++ -O3 -std=c++17`, không dùng `std::`, có Fast I/O và Safe Input.
3. **Problem Package Quality:** Đầy đủ 4 thành phần (`De_Bai.md`, `Huong_Dan_Giang_Day.md` 9 phần, `solution.cpp`, `test/` với 20 testcases có `manifest.json`).
