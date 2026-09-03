# Bài 02: Modulo và lũy thừa nhanh

## 1. Khái niệm & bản chất của đại số đồng dư trong lập trình thi đấu

Trong các bài toán đếm tổ hợp, xác suất và tối ưu hóa quy mô lớn, kết quả đầu ra thường tăng theo hàm số mũ hoặc giai thừa, dễ dàng vượt qua giới hạn biểu diễn của số nguyên 64-bit (`long long` $\approx 9.22 \times 10^{18}$). Để tránh việc phải xử lý số nguyên lớn (BigInt) làm chậm thời gian thực thi, các đề thi thường yêu cầu tính toán kết quả **theo modulo của một số nguyên $M$** (thông dụng nhất là số nguyên tố lớn như $10^9 + 7$ hoặc $998244353$).

Đại số đồng dư (Modular Arithmetic) cho phép ta thu gọn các số cực lớn về một không gian hữu hạn $\{0, 1, \dots, M - 1\}$ mà vẫn bảo toàn các tính chất toán học của phép cộng, trừ, nhân. Tuy nhiên, phép chia trong modulo không thể thực hiện trực tiếp mà phải thông qua khái niệm **Nghịch đảo modulo (Modular Inverse)**.

---

## 2. Các quy tắc tính toán đồng dư cơ bản & bẫy lỗi tử huyệt

### 2.1. Bốn phép toán đồng dư cơ sở

Với mọi $A, B \in \mathbb{Z}$ và số chia modulo $M$:
1. **Phép cộng:** $(A + B) \bmod M = ((A \bmod M) + (B \bmod M)) \bmod M$
2. **Phép nhân:** $(A \times B) \bmod M = ((A \bmod M) \times (B \bmod M)) \bmod M$
3. **Phép trừ:** $(A - B) \bmod M = ((A \bmod M) - (B \bmod M) + M) \bmod M$
4. **Phép lũy thừa:** $A^B \bmod M = (A \bmod M)^B \bmod M$

### 2.2. Tử huyệt lập trình: Bẫy số âm và bẫy tràn số trung gian

> **Cảnh báo bẫy lỗi 1: BẪY SỐ ÂM KHI TRỪ MODULO TRONG C++**

> Trong C++, toán tử `%` là phép chia lấy phần dư định hướng về 0 (truncated division), nghĩa là nếu $A < B$ thì `(A - B) % M` sẽ trả về **số âm** (ví dụ: `(3 - 7) % 5 = -4 % 5 = -4` thay vì $+1$).

> **Quy tắc an toàn tuyệt đối:** Luôn cộng thêm $M$ trước khi lấy dư:
> ```cpp
> long long mod_sub(long long a, long long b, long long m) {
>     return ((a - b) % m + m) % m;
> }
> ```

> **Cảnh báo bẫy lỗi 2: BẪY TRÀN SỐ 32-BIT KHI NHÂN MODULO**

> Khi $A, B \approx 10^9$ và $M = 10^9 + 7$, tích $A \times B \approx 10^{18}$. Nếu khai báo biến kiểu `int`, phép nhân sẽ bị tràn số 32-bit trước khi kịp gọi `% M`. Luôn ép kiểu sang `long long` khi nhân.

> Khi $M \approx 10^{18}$ (số nguyên 64-bit), tích $A \times B \approx 10^{36}$ sẽ làm tràn cả `long long`. Khi đó bắt buộc phải dùng **Nhân Ấn Độ (Binary Multiplication)** hoặc kiểu số nguyên 128-bit `__int128_t`.

---

![Sơ đồ nhân ma trận Fibonacci](assets/l02_matrix_fibonacci_visual.svg)

## 3. Thuật toán lũy thừa nhanh

### 3.1. Ý tưởng thuật toán chia để trị

Để tính $A^B \bmod M$:
* Thuật toán ngây thơ nhân liên tiếp $B$ lần mất $\mathcal{O}(B)$ phép tính $\implies$ Khi $B = 10^{18}$, thời gian chạy là $10^{18}$ bước ($\approx 30$ năm).
* **Lũy thừa nhị phân:** Dựa trên tính chất phân rã nhị phân của số mũ:
$$A^B = \begin{cases} 1 & \text{khi } B = 0 \\ \left(A^{B/2}\right)^2 & \text{khi } B \text{ chẵn} \\ A \times \left(A^{\lfloor B/2 \rfloor}\right)^2 & \text{khi } B \text{ lẻ} \end{cases}$$
Độ phức tạp giảm xuống chỉ còn $\mathcal{O}(\log_2 B)$ bước (với $B = 10^{18}$ chỉ mất $\approx 60$ phép nhân).

### 3.2. Bảng mô phỏng phân rã Fast Power: Tính $3^{13} \bmod 1000$

Biểu diễn nhị phân của $B = 13$ là $1101_2 = 8 + 4 + 1$:
$$3^{13} = 3^8 \times 3^4 \times 3^1 = 6561 \times 81 \times 3$$

| Bước $k$ | Số Mũ $B$ | $B \bmod 2$ (Bit cuối) | Cơ Số $A$ Hiện Tại | Biến Tích Lũy `ans` ($ans = (ans \times A) \bmod M$) | Trạng Thái $(A_{next} = A^2, B_{next} = B/2)$ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | 13 | 1 (Lẻ) | $3$ | $1 \times 3 = \mathbf{3}$ | $A \leftarrow 3^2 = 9, B \leftarrow 6$ |
| 2 | 6 | 0 (Chẵn) | $9$ | Giữ nguyên $\mathbf{3}$ | $A \leftarrow 9^2 = 81, B \leftarrow 3$ |
| 3 | 3 | 1 (Lẻ) | $81$ | $3 \times 81 = \mathbf{243}$ | $A \leftarrow 81^2 = 6561 \equiv 561, B \leftarrow 1$ |
| 4 | 1 | 1 (Lẻ) | $561$ | $243 \times 561 = 136323 \equiv \mathbf{323}$ | $B \leftarrow 0$ (Dừng) |
| **Kết quả** | **0** | — | — | **$ans = 323$** | **$3^{13} \bmod 1000 = 323$** |

### 3.3. Cài đặt C++ lũy thừa nhanh chuẩn thi đấu

```cpp
long long power_mod(long long a, long long b, long long m) {
    long long ans = 1;
    a %= m;
    while (b > 0) {
        if (b & 1) ans = (__int128_t)ans * a % m;
        a = (__int128_t)a * a % m;
        b >>= 1;
    }
    return ans;
}
```

---

## 4. Nghịch đảo modulo (Modular Inverse) & Phép chia đồng dư

### 4.1. Khái niệm nghịch đảo modulo

Trong số học thông thường, phép chia $\frac{A}{B}$ tương đương với phép nhân $A \times B^{-1}$ với $B^{-1} = \frac{1}{B}$.  
Trong số học đồng dư, **nghịch đảo modulo** của $B$ theo modulo $M$ là một số nguyên $X$ thỏa mãn:
$$B \times X \equiv 1 \pmod{M}$$
Ký hiệu $X = B^{-1} \bmod M$. Khi đó:
$$\frac{A}{B} \bmod M = (A \times B^{-1}) \bmod M$$

> **Điều kiện tồn tại:** Nghịch đảo modulo $B^{-1} \pmod{M}$ tồn tại khi và chỉ khi $\gcd(B, M) = 1$ (hai số nguyên tố cùng nhau).

### 4.2. Hai phương pháp tìm nghịch đảo modulo

#### Phương pháp 1: Định lý Fermat nhỏ (Áp dụng khi $M$ là số nguyên tố)
> **Định lý Fermat nhỏ:** Nếu $M$ là số nguyên tố và $B$ không chia hết cho $M$, thì $B^{M-1} \equiv 1 \pmod{M}$.  
> Nhân cả 2 vế với $B^{-1}$, ta có:
$$B^{-1} \equiv B^{M-2} \pmod{M}$$

```cpp
// Khi M là số nguyên tố (ví dụ 10^9 + 7)
long long modInverse_Fermat(long long b, long long m) {
    return power_mod(b, m - 2, m);
}
```

#### Phương pháp 2: Thuật toán Euclid mở rộng (Áp dụng khi $M$ bất kỳ, miễn là $\gcd(B, M) = 1$)
Giải phương trình Diophantine: $B \cdot x + M \cdot y = \gcd(B, M) = 1 \implies B \cdot x \equiv 1 \pmod{M}$. Nghiệm $x$ chính là nghịch đảo modulo:
```cpp
long long extgcd(long long a, long long b, long long &x, long long &y) {
    if (b == 0) { x = 1; y = 0; return a; }
    long long x1, y1;
    long long g = extgcd(b, a % b, x1, y1);
    x = y1;
    y = x1 - (a / b) * y1;
    return g;
}

long long modInverse_Euclid(long long b, long long m) {
    long long x, y;
    long long g = extgcd(b, m, x, y);
    if (g != 1) return -1; // Không tồn tại nghịch đảo
    return (x % m + m) % m;
}
```

---

## 5. Kỹ thuật nâng cao: Tiền xử lý nghịch đảo tuyến tính $\mathcal{O}(N)$

Khi cần tính tổ hợp $C_n^k \bmod M$ hoặc nghịch đảo cho tất cả các số từ $1$ đến $N$ (với $N = 10^6$), nếu dùng Fast Power cho từng số sẽ mất $\mathcal{O}(N \log M)$.  
Ta có công thức truy hồi tính nghịch đảo của mọi số $i \in [1, N]$ trong **thời gian tuyến tính $\mathcal{O}(N)$**:
$$\text{inv}[i] = - \lfloor M / i \rfloor \times \text{inv}[M \bmod i] \pmod{M}$$

```cpp
const int MAXN = 1000000;
long long inv[MAXN + 1];

void precompute_inverses(long long m) {
    inv[1] = 1;
    for (int i = 2; i <= MAXN; ++i) {
        inv[i] = m - (m / i) * inv[m % i] % m;
    }
}
```

---

## 6. Mẫu cài đặt chuẩn thi đấu (Competitive Template)

```cpp
#include <bits/stdc++.h>
using namespace std;

const long long MOD = 1000000007;

long long power_mod(long long a, long long b, long long m = MOD) {
    long long ans = 1;
    a %= m;
    while (b > 0) {
        if (b & 1) ans = (ans * a) % m;
        a = (a * a) % m;
        b >>= 1;
    }
    return ans;
}

long long mod_inverse(long long a, long long m = MOD) {
    return power_mod(a, m - 2, m);
}

long long mod_divide(long long a, long long b, long long m = MOD) {
    return (a % m * mod_inverse(b, m)) % m;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long a, b;
    if (!(cin >> a >> b)) return 0;

    // Tính (a / b) % MOD
    cout << mod_divide(a, b) << "\n";
    return 0;
}
```

---

## 7. Ranh giới áp dụng: Khi nào dùng Fermat vs Euclid mở rộng vs BigInt?

| Tình Huống Bài Toán | Điều Kiện Modulo $M$ | Kỹ Thuật Tối Ưu | Độ Phức Tạp |
|---|---|---|:---:|
| $M$ là số nguyên tố ($10^9+7, 998244353$) | $M$ nguyên tố | Fermat nhỏ $B^{M-2} \bmod M$ | $\mathcal{O}(\log M)$ |
| $M$ là hợp số nhưng $\gcd(B, M) = 1$ | $M$ bất kỳ | Euclid mở rộng giải $Bx + My = 1$ | $\mathcal{O}(\log M)$ |
| Cần nghịch đảo cho mảng $1 \dots N$ | $M$ nguyên tố | Tiền xử lý mảng `inv[i]` tuyến tính | $\mathcal{O}(N)$ |
| Số mũ $B$ cực lớn ($B \le 10^{100000}$) | $M$ nguyên tố | Hạ bậc số mũ: $A^B \equiv A^{B \bmod (M-1)} \pmod{M}$ | $\mathcal{O}(\text{length}(B) + \log M)$ |

---

## Câu hỏi trắc nghiệm củng cố khái niệm

#### Câu 1 (Bẫy số âm — Arithmetic):
Trong C++, biểu thức `(-7) % 5` cho kết quả bằng bao nhiêu, và giá trị đồng dư chuẩn trong khoảng $[0, 4]$ là bao nhiêu?
- **A.** `-2` và `3`
- **B.** **[Đáp án đúng]** `-2` trong C++, và giá trị chuẩn là `3` (vì $-7 \equiv 3 \pmod 5$).
- **C.** `3` và `3`
- **D.** `-2` và `-2`

> *Giải thích:* C++ thực hiện chia lấy dư cụt về 0 nên `(-7) % 5 = -2`. Để đưa về $[0, M-1]$, ta dùng công thức `((-7) % 5 + 5) % 5 = 3`.

#### Câu 2 (Độ phức tạp Fast Power — Performance):
Để tính $A^{10^{18}} \bmod (10^9+7)$, thuật toán lũy thừa nhị phân cần thực hiện tối đa bao nhiêu phép nhân?
- **A.** $10^{18}$ phép tính
- **B.** $10^9$ phép tính
- **C.** **[Đáp án đúng]** Khoảng 60 phép tính (vì $\log_2(10^{18}) \approx 60$).
- **D.** $1$ phép tính

> *Giải thích:* Mỗi bước chia đôi số mũ $B \leftarrow B / 2$, nên số bước là $\lfloor \log_2(10^{18}) \rfloor \approx 60$.

#### Câu 3 (Điều kiện nghịch đảo — Number Theory):
Phép chia modulo $\frac{A}{B} \bmod M$ tồn tại kết quả duy nhất khi và chỉ khi:
- **A.** $A$ chia hết cho $B$.
- **B.** $M$ chia hết cho $B$.
- **C.** **[Đáp án đúng]** $\gcd(B, M) = 1$.
- **D.** $A > B$.

> *Giải thích:* Nghịch đảo modulo $B^{-1} \pmod M$ tồn tại khi và chỉ khi $B$ và $M$ nguyên tố cùng nhau.

#### Câu 4 (Định lý Fermat nhỏ — Inverse):
Theo định lý Fermat nhỏ, nếu $M = 10^9 + 7$ (số nguyên tố), nghịch đảo modulo của $B$ được tính bằng:
- **A.** $B^{M} \bmod M$
- **B.** **[Đáp án đúng]** $B^{M-2} \bmod M$
- **C.** $B^{-1} \bmod M$
- **D.** $B^{M-1} \bmod M$

> *Giải thích:* $B^{M-1} \equiv 1 \pmod M \implies B \cdot B^{M-2} \equiv 1 \pmod M \implies B^{-1} \equiv B^{M-2} \pmod M$.

#### Câu 5 (Hạ bậc số mũ lớn — Euler):
Nếu $M = 10^9 + 7$ và số mũ $B = 10^{18}$, ta có thể rút gọn số mũ $B$ khi tính $A^B \bmod M$ bằng cách lấy $B$ modulo cho bao nhiêu?
- **A.** $M = 10^9 + 7$
- **B.** **[Đáp án đúng]** $M - 1 = 10^9 + 6$
- **C.** $M + 1$
- **D.** $\sqrt{M}$

> *Giải thích:* Theo định lý Fermat nhỏ, chu kỳ lũy thừa là $M - 1$. Do đó $A^B \equiv A^{B \bmod (M-1)} \pmod M$.

#### Câu 6 (Tiền xử lý tuyến tính — Precomputation):
Mục đích của công thức `inv[i] = M - (M / i) * inv[M % i] % M` là gì?
- **A.** Tìm số nguyên tố nhanh.
- **B.** **[Đáp án đúng]** Tiền xử lý nghịch đảo modulo cho mọi số từ $1$ đến $N$ trong thời gian tuyến tính $\mathcal{O}(N)$.
- **C.** Sắp xếp mảng trong $\mathcal{O}(N)$.
- **D.** Tính giai thừa.

> *Giải thích:* Cho phép tính nghịch đảo của $N$ số đầu tiên trong đúng $\mathcal{O}(N)$ thay vì $\mathcal{O}(N \log M)$.

#### Câu 7 (Tràn số 64-bit — Robustness):
Khi tính $(A \times B) \bmod M$ với $A, B, M \approx 10^{18}$, giải pháp nào trong C++ giúp tránh tràn số mà không cần cài BigInt?
- **A.** Dùng kiểu `unsigned long long`.
- **B.** **[Đáp án đúng]** Dùng kiểu `__int128_t` hoặc thuật toán Nhân Ấn Độ.
- **C.** Ép kiểu sang `double`.
- **D.** Dùng `int`.

> *Giải thích:* Tích hai số $10^{18}$ lên tới $10^{36}$, vượt ngưỡng $1.8 \times 10^{19}$ của `unsigned long long`. Kiểu `__int128_t` chứa được số tới $\approx 3.4 \times 10^{38}$.

#### Câu 8 (Biểu diễn nhị phân — Bitwise):
Trong hàm Fast Power, điều kiện `if (b & 1)` kiểm tra điều gì?
- **A.** Kiểm tra $b$ có bằng 1 không.
- **B.** **[Đáp án đúng]** Kiểm tra bit cuối cùng của $b$ có bật (tức $b$ là số lẻ) hay không.
- **C.** Kiểm tra $b$ có phải là lũy thừa của 2 không.
- **D.** Kiểm tra $b$ có âm không.

> *Giải thích:* Phép toán bit `b & 1` trả về 1 khi và chỉ khi $b$ là số lẻ.

#### Câu 9 (Phân số modulo — Division):
Giá trị của $\frac{1}{2} \bmod 7$ bằng bao nhiêu?
- **A.** $0.5$
- **B.** **[Đáp án đúng]** $4$ (vì $2 \times 4 = 8 \equiv 1 \pmod 7$).
- **C.** $3$
- **D.** $1$

> *Giải thích:* $2 \times 4 = 8 \equiv 1 \pmod 7$, do đó $2^{-1} \equiv 4 \pmod 7$. Khi đó $1 \times 4 \equiv 4 \pmod 7$.

#### Câu 10 (Fast Power với $B = 0$ — Boundary):
Giá trị của $A^0 \bmod M$ (với $M > 1$) luôn bằng bao nhiêu?
- **A.** $0$
- **B.** **[Đáp án đúng]** $1$
- **C.** $A$
- **D.** $M$

> *Giải thích:* Quy ước toán học $A^0 = 1$ với mọi $A$, do đó $A^0 \bmod M = 1 \bmod M = 1$.

---

## Ma trận bài tập thực hành (P0 → P5)

| STT | Mã Bài | Tên Bài Toán | Cấp Độ | Ràng Buộc Dữ Liệu | Mục Tiêu Rèn Luyện |
|:---:|:---:|---|:---:|---|---|
| 01 | `CPPB2-L02-01` | **Lũy Thừa Nhanh Cơ Bản** | `P0` | $T \le 10^5, A, B \le 10^{18}, M = 10^9+7$ | Cài đặt hàm `power_mod` nhị phân |
| 02 | `CPPB2-L02-02` | **Tính Giá Trị Phân Số Modulo** | `P0` | $T \le 10^5, P, Q \le 10^9, M = 10^9+7$ | Nghịch đảo modulo Fermat tính $P/Q \bmod M$ |
| 03 | `CPPB2-L02-03` | **Lũy Thừa Ma Trận 2x2 (Dãy Fibonacci Lớn)** | `P1` | $T \le 10^4, N \le 10^{18}, M = 10^9+7$ | Áp dụng Fast Power cho nhân ma trận $2 \times 2$ |
| 04 | `CPPB2-L02-04` | **Nghịch Đảo Modulo Tổng Quát** | `P1` | $T \le 10^5, A, M \le 10^9, M$ bất kỳ | Euclid mở rộng tìm nghịch đảo khi $M$ không nguyên tố |
| 05 | `CPPB2-L02-05` | **Tính Tổ Hợp $C_n^k \bmod (10^9+7)$** | `P2` | $Q \le 10^5, N, K \le 10^6$ | Tiền xử lý giai thừa & nghịch đảo giai thừa |
| 06 | `CPPB2-L02-06` | **Lũy Thừa Với Số Mũ Cực Lớn** | `P2` | $A \le 10^9, B \le 10^{100000}, M = 10^9+7$ | Hạ bậc số mũ bằng định lý Fermat $B \bmod (M-1)$ |
| 07 | `CPPB2-L02-07` | **Nhân Modulo Hai Số Cực Lớn (Nhân Ấn Độ)** | `P2` | $T \le 10^5, A, B, M \le 10^{18}$ | Xử lý chống tràn số khi $M$ lớn bằng nhân nhị phân |
| 08 | `CPPB2-L02-08` | **Tổng Cấp Số Nhân $S_N = \sum_{i=0}^N A^i \bmod M$** | `P3` | $T \le 10^4, A, N \le 10^{18}, M = 10^9+7$ | Chia để trị tính tổng cấp số nhân $\mathcal{O}(\log N)$ |
| 09 | `CPPB2-L02-09` | **Tháp Lũy Thừa $A^{B^C} \bmod M$** | `P3` | $T \le 10^4, A, B, C \le 10^9, M$ nguyên tố | Áp dụng hạ bậc số mũ 2 tầng qua Euler |
| 10 | `CPPB2-L02-10` | **Đếm Dãy Ngoặc Đúng (Số Catalan Modulo)** | `P3` | $T \le 10^5, N \le 10^6, M = 10^9+7$ | Công thức $C_n = \frac{1}{n+1} C_{2n}^n \bmod M$ |
| 11 | `CPPB2-L02-11` | **Hệ Phương Trình Đồng Dư (Chinese Remainder Theorem)** | `P4` | $K \le 10, M_i \le 10^9$ đôi một nguyên tố cùng nhau | Định lý phần dư Trung Hoa giải hệ đồng dư |
| 12 | `CPPB2-L02-12` | **Tiền Xử Lý Nghịch Đảo Tuyến Tính $\mathcal{O}(N)$** | `P4` | $N \le 10^7, M = 10^9+7$ | Cài đặt mảng `inv[i]` trong $\mathcal{O}(N)$ |
| 13 | `CPPB2-L02-13` | **Lũy Thừa Ma Trận Kích Thước $K \times K$** | `P4` | $K \le 10, N \le 10^{18}, M = 10^9+7$ | Giải bài toán quy hoạch động truy hồi qua ma trận |
| 14 | `CPPB2-L02-14` | **Căn Bậc Hai Modulo Nguyên Tố (Thuật Toán Tonelli-Shanks)** | `P5` | $T \le 1000, A, P \le 10^9, P$ nguyên tố lẻ | Tìm $X$ thỏa $X^2 \equiv A \pmod P$ |
| 15 | `CPPB2-L02-15` | **Lũy Thừa Số Mũ Lớn Khi Modulo Là Hợp Số** | `P5` | $A \le 10^9, B \le 10^{100000}, M \le 10^9$ hợp số | Áp dụng định lý Euler mở rộng $A^B \equiv A^{B \bmod \phi(M) + \phi(M)}$ |
| 16 | `CPPB2-L02-16` | **Logarit Rời Rạc (Baby-step Giant-step)** | `P5` | $A, B, M \le 10^9, \gcd(A, M) = 1$ | Tìm $X$ nhỏ nhất thỏa $A^X \equiv B \pmod M$ trong $\mathcal{O}(\sqrt{M})$ |
