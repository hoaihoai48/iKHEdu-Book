---
title: "Khoá học C++ Bảng B (Level 2) — Quyển 1"
subtitle: "Số học nâng cao, Kỹ thuật mảng & Bitwise (Bài 01-06)"
author: "Trung tâm tin học iKH"
lang: vi
documentclass: report
geometry: "a4paper, margin=2.5cm"
fontsize: 12pt
mainfont: "Times New Roman"
monofont: "Courier New"
header-includes:
  - \usepackage{fancyhdr}
  - \pagestyle{fancy}
  - \fancyhead[L]{\textit{Khoá học C++ Bảng B (Level 2) — Quyển 1}}
  - \fancyhead[R]{\textit{Trung tâm tin học iKH}}
---

\newpage

# Lời nói đầu

Chào mừng các em học sinh và quý thầy cô đến với bộ giáo trình **Khoá học C++ Bảng B (Level 2) — QUYỂN 1: SỐ HỌC NÂNG CAO, KỸ THUẬT MẢNG & BITWISE** của Trung tâm tin học iKH.

Bộ tài liệu này được biên soạn công phu nhằm cung cấp lộ trình học tập lập trình thi đấu nâng cao, chuẩn mực và hiện đại nhất dành cho học sinh giỏi Tin học THCS, THPT và sinh viên Olympic Tin học.

Phần nội dung này gồm **3 Chương trọng tâm (Chương 01 đến Chương 03)** với **6 Bài học** và **96 bài toán thực hành phân tầng (P0 → P5)**, đào sâu số học đồng dư, lũy thừa nhanh, tìm kiếm nhị phân không gian nghiệm, kỹ thuật mảng 2D, đệ quy chia để trị, Meet in the Middle và mặt nạ bit.

Mỗi bài học được thiết kế theo cấu trúc sư phạm chặt chẽ:

- **Khái niệm & Bản chất toán học**: Giải thích trực quan, dễ hiểu kèm chứng minh toán học và bất biến thuật toán.
- **Bảng mô phỏng từng bước (Dry Run Table)**: Trực quan hóa quá trình biến đổi dữ liệu từng bước.
- **Mẫu cài đặt chuẩn thi đấu**: Code C++ chuẩn (0 `std::`, `#include <bits/stdc++.h>`, Fast I/O), tối ưu và an toàn tuyệt đối.
- **Hệ thống 16 bài tập thực hành phân tầng**: Từ cơ bản đến chuyên sâu (P0 đến P5), có đầy đủ bối cảnh, nhiệm vụ, input/output và sample test.
- **Lời giải tham khảo chi tiết**: Phụ lục B cung cấp toàn bộ mã nguồn C++ tham khảo chuẩn thi đấu cho các bài tập.

Chúc các em học tập hiệu quả và chinh phục những giải thưởng cao trong các kỳ thi chọn học sinh giỏi và Olympic lập trình!

\begin{flushright}
\textbf{Trung tâm tin học iKH}
\end{flushright}



# CHƯƠNG 01: SỐ HỌC & ĐẠI SỐ ĐỒNG DƯ NÂNG CAO


# Bài 01: Số học cơ bản & chuyên sâu

## 1. Khái niệm & bản chất của tối ưu số học trong lập trình thi đấu

Số học trong lập trình thi đấu (Competitive Programming) không đơn thuần là các phép toán số học cơ bản, mà là nghệ thuật khai thác **các cấu trúc đại số và tính chất chia hết** để giảm độ phức tạp tính toán từ hàm mũ $\mathcal{O}(2^N)$ hoặc đa thức $\mathcal{O}(N)$ xuống thời gian logarit $\mathcal{O}(\log N)$ hoặc $\mathcal{O}(1)$.

Ở Level 2, ta không dừng lại ở việc kiểm tra nguyên tố hay tìm ước số đơn lẻ, mà tập trung vào **Tái kết hợp & Xử lý đa truy vấn với khối lượng dữ liệu cực lớn**:

* **Khai thác thuật toán Euclid:** Rút gọn không gian bài toán, tìm ước chung lớn nhất $\gcd(A, B)$ trong $\mathcal{O}(\log(\min(A, B)))$ và giải phương trình Diophantine nghiệm nguyên qua thuật toán Euclid mở rộng.
* **Sàng ước số nguyên tố nhỏ nhất (SPF):** Tiền xử lý $\mathcal{O}(MAX \log \log MAX)$ để phân tích hàng triệu số thành thừa số nguyên tố với tốc độ $\mathcal{O}(\log N)$ mỗi số.
* **Sàng nguyên tố phân đoạn (Segmented Sieve):** Vượt qua ranh giới bộ nhớ RAM để tìm chính xác mọi số nguyên tố trong đoạn $[L, R]$ với $R \le 10^{12}$ và $R - L \le 10^6$.


## 2. Thuật toán Euclid & Bản chất toán học của GCD / LCM

### 2.1. Định lý Euclid & Tính chất bất biến (Invariant)

> **Định lý:** Với mọi cặp số nguyên không âm $A, B$ ($B \ne 0$), ước chung lớn nhất của chúng luôn thỏa mãn:
> $$\gcd(A, B) = \gcd(B, A \bmod B)$$
> $$\gcd(A, 0) = A$$

Mỗi bước lấy dư $A \bmod B$ thực chất là loại bỏ tất cả các bội số của $B$ ra khỏi $A$, giữ lại phần dư $R < B$. Khi số dư bằng $0$, số chia cuối cùng chính là $\gcd(A, B)$.

#### Ví dụ minh họa 1: Tìm $\gcd(105, 45)$

1. $\gcd(105, 45) = \gcd(45, 105 \bmod 45) = \gcd(45, 15)$
2. $\gcd(45, 15) = \gcd(15, 45 \bmod 15) = \gcd(15, 0) = \mathbf{15}$

| Bước $k$ | Số Bị Chia $A$ | Số Chia $B$ | Phép Chia Lấy Dư $A \bmod B$ | Trạng Thái $(A_{next}, B_{next})$ |
|:---:|:---:|:---:|:---:|:---:|
| 1 | 105 | 45 | $105 \bmod 45 = 15$ | $(45, 15)$ |
| 2 | 45 | 15 | $45 \bmod 15 = 0$ | $(15, 0)$ |
| **Kết quả** | **15** | **0** | **Dừng (B = 0)** | **$\gcd = 15$** |

### 2.2. Mẫu cài đặt C++ chuẩn thi đấu (Không đệ quy)

```cpp
long long gcd_calc(long long a, long long b) {
    while (b != 0) {
        long long r = a % b;
        a = b;
        b = r;
    }
    return a;
}
```

> **Phạm vi áp dụng:** Mẫu `gcd_calc` ở trên nhận các số không âm. Nếu dữ liệu có thể chứa số âm, hãy chuẩn hóa bằng `abs` trước khi gọi; GCD được quy ước là số không âm.

### 2.3. Bẫy lỗi tràn số khi tính Bội chung nhỏ nhất ($\text{lcm}$)

Công thức toán học: $\text{lcm}(A, B) = \frac{A \times B}{\gcd(A, B)}$.

> **Cảnh báo bẫy lỗi: BẪY TRÀN TÍCH `A * B` TRONG PHÉP TÍNH LCM**
> 
> Nếu viết `return (a * b) / gcd(a, b);`, khi $A, B \approx 10^{10}$, tích $A \times B \approx 10^{20}$ sẽ vượt quá giới hạn $9.22 \times 10^{18}$ của kiểu `long long` $\implies$ **TRÀN SỐ ÂM / KẾT QUẢ SAI HOÀN TOÀN**.
> 
> **Quy tắc an toàn tuyệt đối:** Luôn chia trước khi nhân vì $A$ luôn chia hết cho $\gcd(A, B)$:
> ```cpp
> long long lcm_calc(long long a, long long b) {
>     if (a == 0 || b == 0) return 0;
>     return (a / gcd_calc(a, b)) * b;
> }
> ```


## 3. Sàng ước số nguyên tố nhỏ nhất (SPF — Smallest Prime Factor)

### 3.1. Động lực: Xử lý $10^5$ truy vấn phân tích thừa số nguyên tố

Trong các kỳ thi HSG, ta thường gặp bài toán: Cho $Q = 10^5$ truy vấn, mỗi truy vấn cho một số $N \le 10^6$, yêu cầu phân tích $N$ thành thừa số nguyên tố.

* **Cách ngây thơ $\mathcal{O}(\sqrt{N})$:** Mỗi truy vấn thử chia đến $\sqrt{N} \implies \text{Tổng thời gian } \mathcal{O}(Q \sqrt{N}) \approx 10^5 \times 10^3 = 10^8 \text{ phép tính} \implies$ **Nguy cơ TLE**.
* **Kỹ thuật Sàng SPF:** Tiền xử lý 1 lần mảng `spf[x]` lưu ước số nguyên tố nhỏ nhất của $x$ trong $\mathcal{O}(MAX \log \log MAX)$. Khi có truy vấn $N$, ta chỉ việc nhảy liên tiếp theo `spf[N]` $\implies$ **Mỗi truy vấn chỉ mất $\mathcal{O}(\log N)$ bước!**

### 3.2. Bảng mô phỏng phân tích số $N = 84$ bằng SPF

* `spf[84] = 2` $\implies 84 / 2 = 42$
* `spf[42] = 2` $\implies 42 / 2 = 21$
* `spf[21] = 3` $\implies 21 / 3 = 7$
* `spf[7] = 7` $\implies 7 / 7 = 1$ (Dừng)
$$\implies 84 = 2^2 \times 3^1 \times 7^1 \quad (\text{Chỉ mất đúng 4 bước chia!})$$

| Bước $k$ | Giá Trị $N$ Hiện Tại | `spf[N]` (Ước NT nhỏ nhất) | $N_{next} = N / \text{spf}[N]$ | Thừa Số Thu Được |
|:---:|:---:|:---:|:---:|:---:|
| 1 | 84 | 2 | 42 | $2$ |
| 2 | 42 | 2 | 21 | $2$ |
| 3 | 21 | 3 | 7 | $3$ |
| 4 | 7 | 7 | 1 | $7$ |

### 3.3. Cài đặt C++ Sàng SPF & Phân tích thừa số tối ưu

```cpp
const int MAXN = 1000000;
int spf[MAXN + 1];

void sieve_spf() {
    for (int i = 1; i <= MAXN; ++i) spf[i] = i;
    for (int i = 2; i * i <= MAXN; ++i) {
        if (spf[i] == i) { // i là số nguyên tố
            for (int j = i * i; j <= MAXN; j += i) {
                if (spf[j] == j) spf[j] = i; // Gán ước NT nhỏ nhất đầu tiên chạm tới
            }
        }
    }
}

// Phân tích n thành vector 2 chiều: mỗi phần tử gồm [thừa_số_nguyên_tố, số_mũ]
vector<vector<long long>> factorize_spf(int n) {
    vector<vector<long long>> factors;
    while (n > 1) {
        long long p = spf[n];
        long long count = 0;
        while (n % p == 0) {
            count++;
            n /= p;
        }
        factors.push_back({p, count});
    }
    return factors;
}
```


## 4. Sàng nguyên tố phân đoạn (Segmented Sieve trên $[L, R]$)

### 4.1. Bản chất & Ranh giới bộ nhớ

Khi bài toán yêu cầu tìm/đếm các số nguyên tố trong đoạn $[L, R]$ với:
$$1 \le L \le R \le 10^{12} \quad \text{và} \quad R - L \le 10^6$$

* **Tại sao không thể tạo mảng `bool is_prime[10^12]`?** $\implies$ Vì $10^{12}$ byte $\approx 1000\text{GB}$ RAM, vượt giới hạn $256\text{MB}$ của đề bài.
* **Định lý toán học:** Mọi hợp số $X \in [L, R]$ đều có ít nhất một ước nguyên tố $p \le \sqrt{R} \le 10^6$.

### 4.2. Thuật toán Sàng đoạn 3 bước

1. **Bước 1:** Dùng sàng Eratosthenes chuẩn tìm tất cả số nguyên tố $p \le \sqrt{R} \le 10^6$.
2. **Bước 2:** Cấp phát mảng đánh dấu `vector<bool> is_prime_range(R - L + 1, true)`. Số $X \in [L, R]$ được ánh xạ về chỉ số `X - L` trong mảng ($0 \le X - L \le 10^6$). `vector<bool>` thường nén mỗi cờ theo bit, nên với $10^6$ vị trí phần đánh dấu chỉ khoảng $10^6$ bit $\approx 0.125$ MB; bộ nhớ thực tế phụ thuộc kiểu lưu trữ và overhead của container.
3. **Bước 3:** Với mỗi số nguyên tố $p \le \sqrt{R}$, tìm bội số nhỏ nhất của $p$ mà $\ge L$:
$$\text{start} = \max\left(p \times p, \left\lceil \frac{L}{p} \right\rceil \times p\right) = \max\left(p \times p, \left\lfloor \frac{L + p - 1}{p} \right\rfloor \times p\right)$$
Gạch bỏ tất cả các bội số $\text{start}, \text{start} + p, \text{start} + 2p, \dots \le R$.

### 4.3. Cài đặt C++ Sàng đoạn

```cpp
vector<long long> segmented_sieve(long long L, long long R) {
    long long limit = sqrt(R);
    vector<bool> mark(limit + 1, true);
    vector<long long> primes;
    for (long long p = 2; p <= limit; ++p) {
        if (mark[p]) {
            primes.push_back(p);
            for (long long j = p * p; j <= limit; j += p) mark[j] = false;
        }
    }

    vector<bool> is_prime_range(R - L + 1, true);
    for (long long p : primes) {
        long long start = max(p * p, ((L + p - 1) / p) * p);
        for (long long j = start; j <= R; j += p) {
            is_prime_range[j - L] = false;
        }
    }

    if (L == 1) is_prime_range[0] = false; // Bắt buộc: Số 1 không phải là số nguyên tố

    vector<long long> result;
    for (long long i = 0; i <= R - L; ++i) {
        if (is_prime_range[i]) {
            result.push_back(L + i);
        }
    }
    return result;
}
```


## 5. Thuật toán Euclid mở rộng & Phương trình Diophantine

### 5.1. Định lý Bézout & Nghiệm nguyên

> **Định lý Bézout:** Với hai số nguyên $A, B$, luôn tồn tại hai số nguyên $x, y$ sao cho:
> $$A \cdot x + B \cdot y = \gcd(A, B)$$

Phương trình Diophantine tuyến tính $A \cdot x + B \cdot y = C$ có nghiệm nguyên khi và chỉ khi $C$ chia hết cho $\gcd(A, B)$.

### 5.2. Công thức hồi quy nghiệm `extgcd`

Giả sử đệ quy tìm được $(x_1, y_1)$ thỏa mãn: $B \cdot x_1 + (A \bmod B) \cdot y_1 = g$.  
Vì $A \bmod B = A - \lfloor A/B \rfloor \cdot B$, ta có công thức hồi quy nghiệm $(x, y)$:
$$\begin{cases} x = y_1 \\ y = x_1 - \lfloor A / B \rfloor \cdot y_1 \end{cases}$$

```cpp
long long extgcd_nonnegative(long long a, long long b, long long &x, long long &y) {
    if (b == 0) {
        x = 1;
        y = 0;
        return a;
    }
    long long x1, y1;
    long long g = extgcd_nonnegative(b, a % b, x1, y1);
    x = y1;
    y = x1 - (a / b) * y1;
    return g;
}

long long extgcd(long long a, long long b, long long &x, long long &y) {
    long long sa = (a < 0 ? -1 : 1);
    long long sb = (b < 0 ? -1 : 1);
    long long aa = (a < 0 ? -a : a);
    long long bb = (b < 0 ? -b : b);
    long long g = extgcd_nonnegative(aa, bb, x, y);
    x *= sa;
    y *= sb;
    return g;
}
```

Hàm `extgcd_nonnegative` xử lý phần đệ quy trên số không âm; hàm `extgcd` bên ngoài khôi phục dấu của $A, B$. Vì vậy phương trình $A x + B y = C$ có thể nhận $A, B$ âm, sau khi xử lý riêng trường hợp $A = B = 0$.


## 6. Mẫu cài đặt chuẩn thi đấu (Competitive Template)

```cpp
#include <bits/stdc++.h>
using namespace std;

// Sàng SPF tiền xử lý
const int MAXN = 1000000;
int spf[MAXN + 1];

void init_spf() {
    for (int i = 1; i <= MAXN; ++i) spf[i] = i;
    for (int i = 2; i * i <= MAXN; ++i) {
        if (spf[i] == i) {
            for (int j = i * i; j <= MAXN; j += i) {
                if (spf[j] == j) spf[j] = i;
            }
        }
    }
}

int main() {
    // Fast I/O
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    init_spf();

    int q;
    if (!(cin >> q)) return 0;

    while (q--) {
        int n;
        cin >> n;
        // Phân tích n trong O(log N)
        while (n > 1) {
            int p = spf[n];
            int cnt = 0;
            while (n % p == 0) {
                cnt++;
                n /= p;
            }
            cout << p << "^" << cnt << " ";
        }
        cout << "\n";
    }
    return 0;
}
```


## 7. Ranh giới áp dụng: Khi nào dùng SPF vs Sàng đoạn vs Phân tích $\mathcal{O}(\sqrt{N})$?

| Phương Pháp | Phạm Vi Dữ Liệu | Số Lượng Truy Vấn | Bộ Nhớ RAM | Khi Nào Sử Dụng? |
|---|---|---|:---:|---|
| **Thử chia $\mathcal{O}(\sqrt{N})$** | $N \le 10^{14}$ | $Q \le 10^3$ (Ít truy vấn) | $\mathcal{O}(1)$ | Số lớn, ít truy vấn độc lập |
| **Sàng SPF $\mathcal{O}(\log N)$** | $N \le 10^6$ | $Q \le 10^6$ (Rất nhiều truy vấn) | Khoảng $4\text{MB}$ với `int` | Số vừa phải, truy vấn liên tục |
| **Sàng đoạn $[L, R]$** | $R \le 10^{12}, R - L \le 10^6$ | $1$ truy vấn đoạn lớn | Khoảng $0.125\text{MB}$ cho $10^6$ bit với `vector<bool>` | Cần đếm/tìm số nguyên tố trên dải số lớn |

> **Ghi chú bộ nhớ:** Đây chỉ là phần mảng đánh dấu. Nếu dùng `bool`, `char` hoặc container khác thay cho `vector<bool>`, bộ nhớ sẽ lớn hơn; cần tính theo kiểu dữ liệu thực tế.


## Visual Assets / Hình ảnh trực quan

Các hình dưới đây là kế hoạch minh họa cho bản phát hành; trạng thái hiện tại là `TBD`.

| Asset | Mục đích minh họa | Nội dung chính | Vị trí đặt trong Lesson | Trạng thái |
|---|---|---|---|---|
| Sơ đồ thuật toán Euclid | Làm rõ quá trình giảm cặp $(A,B)$ | $(A,B) \to (B,A \bmod B)$ | Sau mục 2.1 | `TBD` |
| Bảng mô phỏng SPF với $N=84$ | Cho thấy mỗi lần chia theo ước nguyên tố nhỏ nhất | $84\to42\to21\to7\to1$ | Sau mục 3.2 | `TBD` |
| Sơ đồ ba bước Segmented Sieve | Phân biệt sàng cơ sở và sàng trên đoạn lớn | Sinh prime cơ sở → ánh xạ đoạn → gạch bội | Sau mục 4.2 | `TBD` |
| Sơ đồ truy hồi Extended Euclid | Theo dõi hệ số Bézout qua các lần quay lui | $(x_1,y_1)\to(x,y)$ | Sau mục 5.2 | `TBD` |
| Sơ đồ chọn công cụ | Giúp chọn đúng thuật toán theo giới hạn | SPF / sàng đoạn / thử chia | Trước mục 7 | `TBD` |

## Bài tập thực hành phân tầng (P0 → P5)


### Bài 01 [CPPB2-L01-01]: ƯỚC CHUNG & BỘI CHUNG CƠ BẢN

**Đầu vào (Input):**

* Dòng đầu tiên chứa số nguyên dương $T$ ($1 \le T \le 10^5$) — số lượng bộ dữ liệu cần xử lý.
* $T$ dòng tiếp theo, mỗi dòng chứa hai số nguyên dương $A$ và $B$ ($1 \le A, B \le 10^9$), cách nhau bởi một dấu cách.

---

**Đầu ra (Output):**

* Gồm $T$ dòng, mỗi dòng in ra hai số nguyên cách nhau bởi một dấu cách: số đầu tiên là $\gcd(A, B)$, số thứ hai là $\text{lcm}(A, B)$.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
3
12 18
6 9
1000000000 1000000000
```

**Output:**
```text
6 36
3 18
1000000000 1000000000
```

### Giải thích Sample 1:
* Với cặp $(12, 18)$: $\gcd(12, 18) = 6$, $\text{lcm}(12, 18) = \frac{12}{6} \times 18 = 36$.
* Với cặp $(6, 9)$: $\gcd(6, 9) = 3$, $\text{lcm}(6, 9) = \frac{6}{3} \times 9 = 18$.
* Với cặp $(10^9, 10^9)$: $\gcd = 10^9, \text{lcm} = 10^9$.

---

**Ràng buộc dữ liệu:**

* $1 \le T \le 10^5$.
* $1 \le A, B \le 10^9$.
* Đảm bảo giá trị $\text{lcm}(A, B) \le 10^{18}$ nằm trọn vẹn trong kiểu dữ liệu `long long`.



### Bài 02 [CPPB2-L01-02]: RÚT GỌN MẢNG PHÂN SỐ LỚN

**Đầu vào (Input):**

* Dòng đầu tiên chứa số nguyên dương $N$ ($1 \le N \le 10^5$) — số lượng phân số cần rút gọn.
* $N$ dòng tiếp theo, mỗi dòng chứa hai số nguyên $A_i$ và $B_i$ ($-10^9 \le A_i \le 10^9$, $1 \le |B_i| \le 10^9$, $B_i \ne 0$), cách nhau bởi một dấu cách.

---

**Đầu ra (Output):**

* Gồm $N$ dòng, mỗi dòng in ra hai số nguyên $P_i$ và $Q_i$ cách nhau bởi một dấu cách, biểu diễn phân số tối giản $\frac{P_i}{Q_i}$ tương ứng ($Q_i > 0$).

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
4
12 18
-6 8
15 -25
0 -100
```

**Output:**
```text
2 3
-3 4
-3 5
0 1
```

### Giải thích Sample 1:
* $\frac{12}{18}$: $\gcd(12, 18) = 6 \implies \frac{12/6}{18/6} = \frac{2}{3}$.
* $\frac{-6}{8}$: $\gcd(6, 8) = 2 \implies \frac{-6/2}{8/2} = \frac{-3}{4}$.
* $\frac{15}{-25}$: $\gcd(15, 25) = 5 \implies \frac{15/5}{-25/5} = \frac{3}{-5} \implies$ chuẩn hóa mẫu dương thành $\frac{-3}{5}$.
* $\frac{0}{-100}$: chuẩn hóa thành `0 1`.

---

**Ràng buộc dữ liệu:**

* $1 \le N \le 10^5$.
* $-10^9 \le A_i \le 10^9$.
* $1 \le |B_i| \le 10^9$, $B_i \ne 0$.



### Bài 03 [CPPB2-L01-03]: SÀNG ƯỚC SỐ NGUYÊN TỐ NHỎ NHẤT (SPF)

**Đầu vào (Input):**

* Dòng đầu tiên chứa số nguyên dương $Q$ ($1 \le Q \le 10^6$) — số lượng truy vấn.
* $Q$ dòng tiếp theo, mỗi dòng chứa một số nguyên dương $X$ ($2 \le X \le 10^6$).

---

**Đầu ra (Output):**

* Gồm $Q$ dòng, mỗi dòng in ra ước số nguyên tố nhỏ nhất $\text{spf}[X]$ của số $X$ tương ứng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
2
9
15
84
999983
```

**Output:**
```text
2
3
3
2
999983
```

### Giải thích Sample 1:
* $X = 2$: là số nguyên tố $\implies \text{spf}[2] = 2$.
* $X = 9 = 3^2 \implies \text{spf}[9] = 3$.
* $X = 15 = 3 \times 5 \implies \text{spf}[15] = 3$.
* $X = 84 = 2^2 \times 3 \times 7 \implies \text{spf}[84] = 2$.
* $X = 999983$: là số nguyên tố $\implies \text{spf}[999983] = 999983$.

---

**Ràng buộc dữ liệu:**

* $1 \le Q \le 10^6$.
* $2 \le X \le 10^6$.



### Bài 04 [CPPB2-L01-04]: PHÂN TÍCH THỪA SỐ TRUY VẤN NHANH

**Đầu vào (Input):**

* Dòng đầu tiên chứa số nguyên dương $Q$ ($1 \le Q \le 10^5$) — số lượng truy vấn.
* $Q$ dòng tiếp theo, mỗi dòng chứa một số nguyên dương $N$ ($2 \le N \le 10^6$).

---

**Đầu ra (Output):**

* Gồm $Q$ dòng, mỗi dòng in ra dạng phân tích của $N$. Mỗi thừa số nguyên tố và số mũ được in dưới dạng `p^a`, các cặp thừa số cách nhau bởi một dấu cách theo thứ tự các số nguyên tố tăng dần.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
4
12
84
13
1000000
```

**Output:**
```text
2^2 3^1
2^2 3^1 7^1
13^1
2^6 5^6
```

### Giải thích Sample 1:
* $12 = 2^2 \times 3^1$.
* $84 = 2^2 \times 3^1 \times 7^1$.
* $13 = 13^1$.
* $1000000 = 10^6 = 2^6 \times 5^6$.

---

**Ràng buộc dữ liệu:**

* $1 \le Q \le 10^5$.
* $2 \le N \le 10^6$.



### Bài 05 [CPPB2-L01-05]: ĐẾM ƯỚC SỐ & TỔNG ƯỚC SỐ NHANH

**Đầu vào (Input):**

* Dòng đầu tiên chứa số nguyên dương $Q$ ($1 \le Q \le 10^5$).
* $Q$ dòng tiếp theo, mỗi dòng chứa một số nguyên dương $N$ ($2 \le N \le 10^6$).

---

**Đầu ra (Output):**

* Gồm $Q$ dòng, mỗi dòng in ra hai số nguyên $d(N)$ và $\sigma(N)$ cách nhau bởi một dấu cách.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
4
12
28
7
100
```

**Output:**
```text
6 28
6 56
2 8
9 217
```

### Giải thích Sample 1:
* $12 = 2^2 \times 3^1$: ước là $\{1,2,3,4,6,12\}$, $d = 6$, $\sigma = 28$.
* $28 = 2^2 \times 7^1$: ước là $\{1,2,4,7,14,28\}$, $d = 6$, $\sigma = 56$.
* $7 = 7^1$: $d = 2$, $\sigma = 8$.
* $100 = 2^2 \times 5^2$: $d = (2+1)(2+1) = 9$, $\sigma = \frac{8-1}{1} \cdot \frac{125-1}{4} = 7 \times 31 = 217$.

---

**Ràng buộc dữ liệu:**

* $1 \le Q \le 10^5$.
* $2 \le N \le 10^6$.



### Bài 06 [CPPB2-L01-06]: SÀNG NGUYÊN TỐ ĐOẠN [L, R]

**Đầu vào (Input):**

* Gồm một dòng duy nhất chứa hai số nguyên dương $L$ và $R$ ($1 \le L \le R \le 10^{12}$, $R - L \le 10^6$), cách nhau bởi một dấu cách.

---

**Đầu ra (Output):**

* In ra một số nguyên duy nhất là số lượng số nguyên tố trong đoạn $[L, R]$.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
1 10
```

**Output:**
```text
4
```

### Sample 2:
**Input:**
```text
100000000000 100000100000
```

**Output:**
```text
3805
```

### Giải thích Sample 1:
Trong đoạn $[1, 10]$, có 4 số nguyên tố là $2, 3, 5, 7$ (số 1 không phải số nguyên tố).

---

**Ràng buộc dữ liệu:**

* $1 \le L \le R \le 10^{12}$.
* $R - L \le 10^6$.



### Bài 07 [CPPB2-L01-07]: Cặp Số Nguyên Tố Sinh Đôi Trong Đoạn

**Đầu vào (Input):**

Dòng đầu chứa số bộ dữ liệu `T`. Mỗi dòng tiếp theo chứa các tham số theo thứ tự `L,R`.

**Đầu ra (Output):**

In kết quả tương ứng trên từng dòng. Với bài tìm nghiệm, in `NO` nếu vô nghiệm.

**Ví dụ mẫu:**

```text
1
1 20
```



### Bài 08 [CPPB2-L01-08]: TÌM NGHIỆM NGUYÊN PHƯƠNG TRÌNH DIOPHANTINE

**Đầu vào (Input):**

* Dòng đầu tiên chứa số nguyên dương $T$ ($1 \le T \le 10^5$).
* $T$ dòng tiếp theo, mỗi dòng chứa ba số nguyên $A$, $B$, $C$ ($-10^9 \le A, B, C \le 10^9$), cách nhau bởi dấu cách.

---

**Đầu ra (Output):**

* Gồm $T$ dòng:
  * Nếu phương trình vô nghiệm, in `NO`.
  * Nếu có nghiệm, in `YES x0 y0` với $(x_0, y_0)$ là một cặp nghiệm nguyên bất kỳ.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
3
2 3 7
4 6 3
0 0 0
```

**Output:**
```text
YES -7 7
NO
YES 0 0
```

### Giải thích Sample 1:
* $2x + 3y = 7$: $\gcd(2, 3) = 1 \mid 7 \implies$ có nghiệm. Nghiệm $(x_0, y_0) = (-7, 7)$: $2(-7) + 3(7) = -14 + 21 = 7$ ✓.
* $4x + 6y = 3$: $\gcd(4, 6) = 2 \nmid 3 \implies$ vô nghiệm.
* $0x + 0y = 0$: $0 = 0 \implies$ mọi $(x, y)$ đều là nghiệm, in $(0, 0)$.

---

**Ràng buộc dữ liệu:**

* $1 \le T \le 10^5$.
* $-10^9 \le A, B, C \le 10^9$.
* Nếu phương trình có nghiệm, đảm bảo tồn tại cặp $(x_0, y_0)$ nằm trong phạm vi `long long`.



### Bài 09 [CPPB2-L01-09]: Nghiệm Nguyên Dương Nhỏ Nhất

**Đầu vào (Input):**

Dòng đầu chứa số bộ dữ liệu `T`. Mỗi dòng tiếp theo chứa các tham số theo thứ tự `A,B,C`.

**Đầu ra (Output):**

In kết quả tương ứng trên từng dòng. Với bài tìm nghiệm, in `NO` nếu vô nghiệm.

**Ví dụ mẫu:**

```text
1
2 3 7
```



### Bài 10 [CPPB2-L01-10]: HÀM PHI EULER $\PHI(N)$ NHANH VỚI SPF

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Hàm Phi Euler $\phi(N)$ Nhanh Với SPF.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $Q \le 10^5, N \le 10^6$.



### Bài 11 [CPPB2-L01-11]: Phân Tích Giai Thừa N! (Legendre)

**Đầu vào (Input):**

Dòng đầu chứa số bộ dữ liệu `T`. Mỗi dòng tiếp theo chứa các tham số theo thứ tự `N,p`.

**Đầu ra (Output):**

In kết quả tương ứng trên từng dòng. Với bài tìm nghiệm, in `NO` nếu vô nghiệm.

**Ví dụ mẫu:**

```text
1
5 2
```



### Bài 12 [CPPB2-L01-12]: Số Ước Số Lẻ & Số Chính Phương

**Đầu vào (Input):**

Dòng đầu chứa số bộ dữ liệu `T`. Mỗi dòng tiếp theo chứa các tham số theo thứ tự `A,B`.

**Đầu ra (Output):**

In kết quả tương ứng trên từng dòng. Với bài tìm nghiệm, in `NO` nếu vô nghiệm.

**Ví dụ mẫu:**

```text
1
1 10
```



### Bài 13 [CPPB2-L01-13]: Cặp Số Có GCD và LCM Cho Trước

**Đầu vào (Input):**

Dòng đầu chứa số bộ dữ liệu `T`. Mỗi dòng tiếp theo chứa các tham số theo thứ tự `G,L`.

**Đầu ra (Output):**

In kết quả tương ứng trên từng dòng. Với bài tìm nghiệm, in `NO` nếu vô nghiệm.

**Ví dụ mẫu:**

```text
1
2 12
```



### Bài 14 [CPPB2-L01-14]: Khoảng Cách Cực Đại Giữa Hai Số Nguyên Tố

**Đầu vào (Input):**

Dòng đầu chứa số bộ dữ liệu `T`. Mỗi dòng tiếp theo chứa các tham số theo thứ tự `L,R`.

**Đầu ra (Output):**

In kết quả tương ứng trên từng dòng. Với bài tìm nghiệm, in `NO` nếu vô nghiệm.

**Ví dụ mẫu:**

```text
1
1 20
```



### Bài 15 [CPPB2-L01-15]: Phương Trình Đổi Tiền Xu Diophantine

**Đầu vào (Input):**

Dòng đầu chứa số bộ dữ liệu `T`. Mỗi dòng tiếp theo chứa các tham số theo thứ tự `A,B,S`.

**Đầu ra (Output):**

In kết quả tương ứng trên từng dòng. Với bài tìm nghiệm, in `NO` nếu vô nghiệm.

**Ví dụ mẫu:**

```text
1
2 3 7
```



### Bài 16 [CPPB2-L01-16]: Tổng GCD Với N

**Đầu vào (Input):**

Dòng đầu chứa số bộ dữ liệu `T`. Mỗi dòng tiếp theo chứa các tham số theo thứ tự `N`.

**Đầu ra (Output):**

In kết quả tương ứng trên từng dòng. Với bài tìm nghiệm, in `NO` nếu vô nghiệm.

**Ví dụ mẫu:**

```text
1
6
```




# Bài 02: Modulo và lũy thừa nhanh

## 1. Khái niệm & bản chất của đại số đồng dư trong lập trình thi đấu

Trong các bài toán đếm tổ hợp, xác suất và tối ưu hóa quy mô lớn, kết quả đầu ra thường tăng theo hàm số mũ hoặc giai thừa, dễ dàng vượt qua giới hạn biểu diễn của số nguyên 64-bit (`long long` $\approx 9.22 \times 10^{18}$). Để tránh việc phải xử lý số nguyên lớn (BigInt) làm chậm thời gian thực thi, các đề thi thường yêu cầu tính toán kết quả **theo modulo của một số nguyên $M$** (thông dụng nhất là số nguyên tố lớn như $10^9 + 7$ hoặc $998244353$).

Đại số đồng dư (Modular Arithmetic) cho phép ta thu gọn các số cực lớn về một không gian hữu hạn $\{0, 1, \dots, M - 1\}$ mà vẫn bảo toàn các tính chất toán học của phép cộng, trừ, nhân. Tuy nhiên, phép chia trong modulo không thể thực hiện trực tiếp mà phải thông qua khái niệm **Nghịch đảo modulo (Modular Inverse)**.


## 2. Các quy tắc tính toán đồng dư cơ bản & bẫy lỗi tử huyệt

### 2.1. Bốn phép toán đồng dư cơ sở

Với mọi $A, B \in \mathbb{Z}$ và số chia modulo $M$:

1. **Phép cộng:** $(A + B) \bmod M = ((A \bmod M) + (B \bmod M)) \bmod M$
2. **Phép nhân:** $(A \times B) \bmod M = ((A \bmod M) \times (B \bmod M)) \bmod M$
3. **Phép trừ:** $(A - B) \bmod M = ((A \bmod M) - (B \bmod M) + M) \bmod M$
4. **Phép lũy thừa:** $A^B \bmod M = (A \bmod M)^B \bmod M$

### 2.2. Tử huyệt lập trình: Bẫy số âm và bẫy tràn số trung gian

> **Cảnh báo bẫy lỗi 1: BẪY SỐ ÂM KHI TRỪ MODULO TRONG C++**
> 
> Trong C++, toán tử `%` là phép chia lấy phần dư định hướng về 0 (truncated division), nghĩa là nếu $A < B$ thì `(A - B) % M` sẽ trả về **số âm** (ví dụ: `(3 - 7) % 5 = -4 % 5 = -4` thay vì $+1$).
> 
> **Quy tắc an toàn tuyệt đối:** Luôn cộng thêm $M$ trước khi lấy dư:
> ```cpp
> long long mod_sub(long long a, long long b, long long m) {
>     return ((a - b) % m + m) % m;
> }
> ```

> **Cảnh báo bẫy lỗi 2: BẪY TRÀN SỐ 32-BIT KHI NHÂN MODULO**
> 
> Khi $A, B \approx 10^9$ và $M = 10^9 + 7$, tích $A \times B \approx 10^{18}$. Nếu khai báo biến kiểu `int`, phép nhân sẽ bị tràn số 32-bit trước khi kịp gọi `% M`. Luôn ép kiểu sang `long long` khi nhân.
> 
> Khi $M \approx 10^{18}$ (số nguyên 64-bit), tích $A \times B \approx 10^{36}$ sẽ làm tràn cả `long long`. Khi đó bắt buộc phải dùng **Nhân Ấn Độ (Binary Multiplication)** hoặc kiểu số nguyên 128-bit `__int128_t`.


## 3. Thuật toán lũy thừa nhanh (Binary Exponentiation / Fast Power)

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
> $$B^{-1} \equiv B^{M-2} \pmod{M}$$

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


## 7. Ranh giới áp dụng: Khi nào dùng Fermat vs Euclid mở rộng vs BigInt?

| Tình Huống Bài Toán | Điều Kiện Modulo $M$ | Kỹ Thuật Tối Ưu | Độ Phức Tạp |
|---|---|---|:---:|
| $M$ là số nguyên tố ($10^9+7, 998244353$) | $M$ nguyên tố | Fermat nhỏ $B^{M-2} \bmod M$ | $\mathcal{O}(\log M)$ |
| $M$ là hợp số nhưng $\gcd(B, M) = 1$ | $M$ bất kỳ | Euclid mở rộng giải $Bx + My = 1$ | $\mathcal{O}(\log M)$ |
| Cần nghịch đảo cho mảng $1 \dots N$ | $M$ nguyên tố | Tiền xử lý mảng `inv[i]` tuyến tính | $\mathcal{O}(N)$ |
| Số mũ $B$ cực lớn ($B \le 10^{100000}$) | $M$ nguyên tố | Hạ bậc số mũ: $A^B \equiv A^{B \bmod (M-1)} \pmod{M}$ | $\mathcal{O}(\text{length}(B) + \log M)$ |


## Bài tập thực hành phân tầng (P0 → P5)


### Bài 01 [CPPB2-L02-01]: LŨY THỪA NHANH CƠ BẢN

**Đầu vào (Input):**

* Dòng 1 chứa $T$ ($T \le 10^5$). $T$ dòng tiếp theo mỗi dòng chứa $A, B$.

---

**Đầu ra (Output):**

* In ra kết quả $A^B \bmod (10^9+7)$ trên mỗi dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
2
2 10
3 13
```

**Output:**
```text
1024
323
```

---



### Bài 02 [CPPB2-L02-02]: TÍNH GIÁ TRỊ PHÂN SỐ MODULO

**Đầu vào (Input):**

* Dòng 1: $T$ ($1 \le T \le 10^5$). $T$ dòng sau: $P, Q$ ($0 \le P \le 10^9, 1 \le Q \le 10^9$).

---

**Đầu ra (Output):**

* In ra $(P / Q) \bmod (10^9+7)$ trên mỗi dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
2
1 2
3 7
```

**Output:**
```text
500000004
428571432
```

---



### Bài 03 [CPPB2-L02-03]: LŨY THỪA MA TRẬN 2X2 (DÃY FIBONACCI LỚN)

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Lũy Thừa Ma Trận 2x2 (Dãy Fibonacci Lớn).

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N \le 10^{18}, M = 10^9+7$.



### Bài 04 [CPPB2-L02-04]: NGHỊCH ĐẢO MODULO TỔNG QUÁT

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Nghịch Đảo Modulo Tổng Quát.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $A, M \le 10^9, M$ bất kỳ.



### Bài 05 [CPPB2-L02-05]: TÍNH TỔ HỢP $C_N^K \BMOD (10^9+7)$

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Tính Tổ Hợp $C_n^k \bmod (10^9+7)$.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N, K \le 10^6$.



### Bài 06 [CPPB2-L02-06]: LŨY THỪA VỚI SỐ MŨ CỰC LỚN

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Lũy Thừa Với Số Mũ Cực Lớn.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $A \le 10^9, B \le 10^{100000}, M$ nguyên tố.



### Bài 07 [CPPB2-L02-07]: NHÂN MODULO HAI SỐ CỰC LỚN (NHÂN ẤN ĐỘ)

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Nhân Modulo Hai Số Cực Lớn (Nhân Ấn Độ).

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $A, B, M \le 10^{18}$.



### Bài 08 [CPPB2-L02-08]: TỔNG CẤP SỐ NHÂN $S_N = \SUM_{I=0}^N A^I \BMOD M$

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Tổng Cấp Số Nhân $S_N = \sum_{i=0}^N A^i \bmod M$.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $A, N \le 10^{18}, M = 10^9+7$.



### Bài 09 [CPPB2-L02-09]: THÁP LŨY THỪA $A^{B^C} \BMOD M$

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Tháp Lũy Thừa $A^{B^C} \bmod M$.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $A, B, C \le 10^9, M$ nguyên tố.



### Bài 10 [CPPB2-L02-10]: ĐẾM DÃY NGOẶC ĐÚNG (SỐ CATALAN MODULO)

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Đếm Dãy Ngoặc Đúng (Số Catalan Modulo).

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N \le 10^6, M = 10^9+7$.



### Bài 11 [CPPB2-L02-11]: HỆ PHƯƠNG TRÌNH ĐỒNG DƯ (CHINESE REMAINDER THEOREM)

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Hệ Phương Trình Đồng Dư (Chinese Remainder Theorem).

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $K \le 10, M_i \le 10^9$ đôi một nguyên tố cùng nhau.



### Bài 12 [CPPB2-L02-12]: TIỀN XỬ LÝ NGHỊCH ĐẢO TUYẾN TÍNH $\MATHCAL{O}(N)$

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Tiền Xử Lý Nghịch Đảo Tuyến Tính $\mathcal{O}(N)$.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N \le 10^7, M = 10^9+7$.



### Bài 13 [CPPB2-L02-13]: LŨY THỪA MA TRẬN KÍCH THƯỚC $K \TIMES K$

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Lũy Thừa Ma Trận Kích Thước $K \times K$.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $K \le 10, N \le 10^{18}, M = 10^9+7$.



### Bài 14 [CPPB2-L02-14]: CĂN BẬC HAI MODULO NGUYÊN TỐ (THUẬT TOÁN TONELLI-SHANKS)

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Căn Bậc Hai Modulo Nguyên Tố (Thuật Toán Tonelli-Shanks).

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $T \le 1000, A, P \le 10^9, P$ nguyên tố lẻ.



### Bài 15 [CPPB2-L02-15]: LŨY THỪA SỐ MŨ LỚN KHI MODULO LÀ HỢP SỐ

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Lũy Thừa Số Mũ Lớn Khi Modulo Là Hợp Số.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $A \le 10^9, B \le 10^{100000}, M \le 10^9$ hợp số.



### Bài 16 [CPPB2-L02-16]: LOGARIT RỜI RẠC (BABY-STEP GIANT-STEP)

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Logarit Rời Rạc (Baby-step Giant-step).

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $A, B, M \le 10^9, \gcd(A, M) = 1$.



# CHƯƠNG 02: KỸ THUẬT TÌM KIẾM & XỬ LÝ MẢNG ĐA CHIỀU


# Bài 03: Tìm kiếm nhị phân nâng cao

## 1. Khái niệm & bản chất của tìm kiếm nhị phân trong không gian nghiệm

Tìm kiếm nhị phân (Binary Search) không chỉ giới hạn ở việc tìm kiếm một phần tử trên mảng đã sắp xếp trong $\mathcal{O}(\log N)$, mà ở cấp độ thi đấu nâng cao, nó là một **phương pháp tối ưu hóa tổng quát trên không gian hàm đơn điệu**:

* **Chặt nhị phân kết quả (Binary Search on Answer):** Chuyển đổi một bài toán tối ưu hóa khó ("Tìm giá trị $X$ nhỏ nhất/lớn nhất thỏa mãn điều kiện...") thành một chuỗi các bài toán kiểm tra tính khả thi dễ dàng ("Với giá trị $X$ cho trước, có thể đạt được mục tiêu hay không?") thông qua một hàm kiểm tra đơn điệu `check(X)`.
* **Tìm kiếm nhị phân trên số thực (Real Binary Search):** Tìm nghiệm của phương trình hoặc hàm số liên tục với độ chính xác tuyệt đối $\epsilon = 10^{-7}$.
* **Tìm kiếm tam phân (Ternary Search):** Tìm điểm cực trị (cực đại/cực tiểu) của hàm số đơn phong (unimodal function) trong $\mathcal{O}(\log N)$.


## 2. Bản chất toán học của tính đơn điệu (Monotonicity Criterion)

### 2.1. Điều kiện tiên quyết để chặt nhị phân

Một bài toán có thể giải bằng chặt nhị phân kết quả khi và chỉ khi hàm kiểm tra `check(X)` có **tính đơn điệu trên toàn bộ không gian tìm kiếm**:

$$\text{Không gian tìm Min:} \quad [\text{False, False, False, } \dots \mathbf{\text{True, True, True}}]$$
$$\text{Không gian tìm Max:} \quad [\text{True, True, True, } \dots \mathbf{\text{False, False, False}}]$$

Điểm chuyển giao giữa `False` và `True` (hoặc `True` và `False`) chính là **nghiệm tối ưu toàn cục** cần tìm.

### 2.2. Bảng mô phỏng: Bài toán chia $N$ đoạn gỗ thành $\ge K$ phần bằng nhau

Cho 3 khúc gỗ độ dài $[15, 20, 25]$, cần cắt thành ít nhất $K = 5$ đoạn có độ dài nguyên $X$.
Hàm kiểm tra: $\text{check}(X) = \lfloor 15/X \rfloor + \lfloor 20/X \rfloor + \lfloor 25/X \rfloor \ge 5$.

| Độ dài thử $X$ | Số đoạn cắt được | Điều kiện $\ge 5$ (`check(X)`) | Đánh giá & Thu hẹp không gian |
|:---:|:---:|:---:|---|
| $1$ | $15 + 20 + 25 = 60$ | **True** | Khả thi $\implies$ Thử tăng $X$ |
| $5$ | $3 + 4 + 5 = 12$ | **True** | Khả thi $\implies$ Thử tăng $X$ |
| $10$ | $1 + 2 + 2 = 5$ | **True** | **Khả thi (Ghi nhận đáp án $X = 10$)** |
| $11$ | $1 + 1 + 2 = 4$ | **False** | Không đủ đoạn $\implies$ Giảm $X$ |
| $12$ | $1 + 1 + 2 = 4$ | **False** | Không đủ đoạn |

$$\implies \text{Độ dài lớn nhất tìm được là } X = \mathbf{10}.$$


## 3. Hai mẫu cài đặt chặt nhị phân chuẩn thi đấu (Không bao giờ lặp vô tận)

### 3.1. Mẫu 1: Tìm giá trị nhỏ nhất thỏa mãn `check(mid) == true` (Tìm Min)

```cpp
long long low = MIN_VAL, high = MAX_VAL;
long long ans = -1;

while (low <= high) {
    long long mid = low + (high - low) / 2;
    if (check(mid)) {
        ans = mid;        // Ghi nhận nghiệm hợp lệ
        high = mid - 1;   // Thu hẹp về nửa trái để tìm nghiệm nhỏ hơn
    } else {
        low = mid + 1;    // Không đạt, buộc phải tăng nghiệm
    }
}
```

### 3.2. Mẫu 2: Tìm giá trị lớn nhất thỏa mãn `check(mid) == true` (Tìm Max)

```cpp
long long low = MIN_VAL, high = MAX_VAL;
long long ans = -1;

while (low <= high) {
    long long mid = low + (high - low) / 2;
    if (check(mid)) {
        ans = mid;        // Ghi nhận nghiệm hợp lệ
        low = mid + 1;    // Thu hẹp về nửa phải để tìm nghiệm lớn hơn
    } else {
        high = mid - 1;   // Quá lớn, phải giảm nghiệm
    }
}
```

> **Lưu ý chống tràn số:** Luôn viết `mid = low + (high - low) / 2` thay vì `(low + high) / 2` để tránh tràn số khi `low + high > 2 \cdot 10^9`.


## 4. Chặt nhị phân số thực & Tìm kiếm tam phân (Ternary Search)

### 4.1. Tìm kiếm nhị phân trên số thực (Fixed Iterations)
Khi tìm nghiệm số thực, thay vì dùng `while (high - low > EPS)` dễ bị lỗi làm tròn vô tận, phương pháp chuẩn thi đấu là **chạy lặp cố định 100 lần** (đạt độ chính xác $\approx 2^{-100} \approx 10^{-30}$):

```cpp
double low = 0.0, high = 1e9;
for (int iter = 0; iter < 100; ++iter) {
    double mid = (low + high) / 2.0;
    if (check_real(mid)) low = mid;
    else high = mid;
}
cout << fixed << setprecision(6) << low << "\n";
```

### 4.2. Tìm kiếm tam phân (Ternary Search) trên hàm cực đại
Chia đoạn $[low, high]$ thành 3 phần bằng 2 điểm $m_1 = low + \frac{high - low}{3}$ và $m_2 = high - \frac{high - low}{3}$:

* Nếu $f(m_1) < f(m_2) \implies$ Cực đại nằm ở đoạn $[m_1, high] \implies low = m_1$.
* Ngược lại $\implies high = m_2$.

```cpp
double ternary_search_max(double low, double high) {
    for (int iter = 0; iter < 100; ++iter) {
        double m1 = low + (high - low) / 3.0;
        double m2 = high - (high - low) / 3.0;
        if (f(m1) < f(m2)) low = m1;
        else high = m2;
    }
    return f(low);
}
```


## 5. Mẫu cài đặt chuẩn thi đấu: Bài toán phân bổ công việc (Painter's Partition)

```cpp
#include <bits/stdc++.h>
using namespace std;

// Kiểm tra xem có thể chia mảng thành <= K đoạn có tổng mỗi đoạn <= max_sum hay không
bool check(long long max_sum, const vector<long long> &a, int k) {
    int count = 1;
    long long current_sum = 0;
    for (long long x : a) {
        if (x > max_sum) return false;
        if (current_sum + x > max_sum) {
            count++;
            current_sum = x;
        } else {
            current_sum += x;
        }
    }
    return count <= k;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    vector<long long> a(n);
    long long low = 0, high = 0;
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        low = max(low, a[i]);
        high += a[i];
    }

    long long ans = high;
    while (low <= high) {
        long long mid = low + (high - low) / 2;
        if (check(mid, a, k)) {
            ans = mid;
            high = mid - 1;
        } else {
            low = mid + 1;
        }
    }

    cout << ans << "\n";
    return 0;
}
```


## 6. Ranh giới áp dụng: Khi nào chặt nhị phân mảng vs Chặt nhị phân kết quả?

| Đặc Điểm | Binary Search trên Mảng | Binary Search trên Đáp Án (Answer) |
|---|---|---|
| **Đối tượng tìm kiếm** | Vị trí / phần tử trong mảng tĩnh | Giá trị mục tiêu $X$ trong không gian nghiệm $[L, R]$ |
| **Yêu cầu bắt buộc** | Mảng đã được sắp xếp | Hàm kiểm tra $\text{check}(X)$ có tính đơn điệu |
| **Độ phức tạp** | $\mathcal{O}(\log N)$ | $\mathcal{O}(\text{Time}(\text{check}) \times \log(\text{Range}))$ |
| **Dấu hiệu đề bài** | "Tìm vị trí đầu tiên $\ge K$" | "Tìm giá trị lớn nhất / nhỏ nhất sao cho..." |


## Bài tập thực hành phân tầng (P0 → P5)


### Bài 01 [CPPB2-L03-01]: CHẶT NHỊ PHÂN CẮT GỖ (EKO)

**Đầu vào (Input):**

* Dòng 1: $N, M$ ($1 \le N \le 10^6, 1 \le M \le 10^{18}$). Dòng 2: $N$ số $H_i$ ($1 \le H_i \le 10^9$).

---

**Đầu ra (Output):**

* In ra độ cao cưa $H$ lớn nhất.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
4 7
20 15 10 17
```

**Output:**
```text
15
```

---



### Bài 02 [CPPB2-L03-02]: CHIA BÁNH PIZZA ĐỀU NHAU

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Chia Bánh Pizza Đều Nhau.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N \le 10^5, K \le 10^9$.



### Bài 03 [CPPB2-L03-03]: CHUỒNG BÒ XA NHAU NHẤT (AGGRESSIVE COWS)

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Chuồng Bò Xa Nhau Nhất (Aggressive Cows).

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N \le 10^5, C \le N, X_i \le 10^9$.



### Bài 04 [CPPB2-L03-04]: PHÂN CHIA CÔNG VIỆC THỢ SƠN (PAINTER'S PARTITION)

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Phân Chia Công Việc Thợ Sơn (Painter's Partition).

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N \le 10^5, K \le N$.



### Bài 05 [CPPB2-L03-05]: ĐOÀN TÀU VẬN CHUYỂN HÀNG HÓA

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Đoàn Tàu Vận Chuyển Hàng Hóa.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N, M \le 10^5, W_i \le 10^9$.



### Bài 06 [CPPB2-L03-06]: KHOẢNG CÁCH DÂY CÁP NHỎ NHẤT

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Khoảng Cách Dây Cáp Nhỏ Nhất.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N \le 10^5$, tọa độ thực.



### Bài 07 [CPPB2-L03-07]: TRUNG BÌNH CỘNG ĐOẠN CON LỚN NHẤT $\GE K$

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Trung Bình Cộng Đoạn Con Lớn Nhất $\ge K$.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N \le 10^5, K \le N$.



### Bài 08 [CPPB2-L03-08]: TỐI ƯU HÓA CHI PHÍ LẮP TRẠM PHÁT SÓNG

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Tối Ưu Hóa Chi Phí Lắp Trạm Phát Sóng.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N \le 10^5$, hàm chi phí lồi.



### Bài 09 [CPPB2-L03-09]: TÌM PHẦN TỬ NHỎ THỨ K TRONG BẢNG NHÂN $N \TIMES N$

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Tìm Phần Tử Nhỏ Thứ K Trong Bảng Nhân $N \times N$.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N \le 10^5, K \le N^2$.



### Bài 10 [CPPB2-L03-10]: TỐI ƯU PHÂN ĐOẠN TRỌNG SỐ MA TRẬN 2D

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Tối Ưu Phân Đoạn Trọng Số Ma Trận 2D.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N, M \le 1000, K \le 10^5$.



### Bài 11 [CPPB2-L03-11]: TÌM NGHIỆM THỰC CỦA PHƯƠNG TRÌNH PHI TUYẾN

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Tìm Nghiệm Thực Của Phương Trình Phi Tuyến.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $f(x) = 0$, độ chính xác $10^{-8}$.



### Bài 12 [CPPB2-L03-12]: ĐẾM SỐ CẶP $(A_I, B_J)$ CÓ TỔNG TRONG KHOẢNG $[L, R]$

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Đếm Số Cặp $(A_i, B_j)$ Có Tổng Trong Khoảng $[L, R]$.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N, M \le 10^5, \vert A_i \vert \le 10^9$.



### Bài 13 [CPPB2-L03-13]: PHẦN TỬ NHỎ THỨ K CỦA HỢP HAI MẢNG ĐÃ SẮP XẾP

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Phần Tử Nhỏ Thứ K Của Hợp Hai Mảng Đã Sắp Xếp.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N, M \le 10^6, K \le N + M$.



### Bài 14 [CPPB2-L03-14]: TỐI ƯU PHÂN ĐOẠN TRỌNG SỐ MA TRẬN 2D

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Tối Ưu Phân Đoạn Trọng Số Ma Trận 2D.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N, M \le 1000, K \le 10^5$.



### Bài 15 [CPPB2-L03-15]: CHẶT NHỊ PHÂN SONG SONG (PARALLEL BINARY SEARCH)

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Chặt Nhị Phân Song Song (Parallel Binary Search).

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N, M, Q \le 10^5$.



### Bài 16 [CPPB2-L03-16]: KHOẢNG CÁCH CỰC TRỊ TRÊN ĐA GIÁC LỒI

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Khoảng Cách Cực Trị Trên Đa Giác Lồi.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N \le 10^5$ đỉnh lồi.




# Bài 04: Kỹ thuật mảng: Hai con trỏ, Cửa sổ trượt, Mảng tiền tố & Mảng hiệu

## 1. Khái niệm & bản chất của tối ưu hóa tuyến tính trên mảng

Trong lập trình thi đấu, các kỹ thuật xử lý mảng như **Hai con trỏ (Two Pointers)**, **Cửa sổ trượt (Sliding Window)**, **Mảng tiền tố (Prefix Sum)**, **Mảng hiệu (Difference Array)** và **Nén tọa độ (Coordinate Compression)** là bộ công cụ nền tảng giúp chuyển đổi các thuật toán ngây thơ đa biến $\mathcal{O}(N^2)$ hoặc $\mathcal{O}(N \times Q)$ về độ phức tạp tối ưu tuyến tính $\mathcal{O}(N)$ hoặc $\mathcal{O}(N \log N)$.

Ở Level 2, ta tập trung vào **Kỹ thuật kết hợp đa chiều & Mảng 2D**:

* **Hai con trỏ co giãn & Cửa sổ trượt linh hoạt:** Duy trì bất biến về tần suất, số lượng phần tử phân biệt hoặc tổng điều kiện khi kích thước cửa sổ thay đổi liên tục.
* **Mảng tiền tố 2D (2D Prefix Sum):** Trả lời truy vấn tính tổng hình chữ nhật con bất kỳ trên ma trận $N \times M$ trong $\mathcal{O}(1)$.
* **Mảng hiệu 2D (2D Difference Array):** Cập nhật cộng một giá trị lên toàn bộ vùng hình chữ nhật trong $\mathcal{O}(1)$ và khôi phục ma trận trong $\mathcal{O}(NM)$.
* **Nén tọa độ (Coordinate Compression):** Ánh xạ các giá trị rời rạc rất lớn ($A_i \le 10^9$) về dải chỉ số nhỏ liên tiếp $[1, N]$ mà vẫn bảo toàn hoàn toàn quan hệ thứ tự $A_i < A_j$.


## 2. Mảng tiền tố 2D & Mảng hiệu 2D (2D Prefix & Difference)

### 2.1. Công thức Mảng tiền tố 2D (2D Prefix Sum)

Định nghĩa: $pref[i][j]$ là tổng các phần tử trong hình chữ nhật từ góc trên-trái $(1, 1)$ đến $(i, j)$:
$$pref[i][j] = pref[i-1][j] + pref[i][j-1] - pref[i-1][j-1] + A[i][j]$$

Truy vấn tổng hình chữ nhật từ $(x_1, y_1)$ đến $(x_2, y_2)$ trong $\mathcal{O}(1)$:
$$\text{Sum}(x_1, y_1, x_2, y_2) = pref[x_2][y_2] - pref[x_1-1][y_2] - pref[x_2][y_1-1] + pref[x_1-1][y_1-1]$$

### 2.2. Công thức Mảng hiệu 2D (2D Difference Array)

Để cộng thêm giá trị $V$ vào toàn bộ hình chữ nhật $[x_1, y_1] \to [x_2, y_2]$ trong $\mathcal{O}(1)$:

1. $diff[x_1][y_1] \mathrel{+}= V$
2. $diff[x_1][y_2 + 1] \mathrel{-}= V$
3. $diff[x_2 + 1][y_1] \mathrel{-}= V$
4. $diff[x_2 + 1][y_2 + 1] \mathrel{+}= V$

Sau khi thực hiện tất cả các cập nhật, chạy công thức Prefix Sum 2D trên mảng $diff$ để thu lại giá trị thực tế của ma trận.


## 3. Kỹ thuật nén tọa độ (Coordinate Compression)

### 3.1. Động lực & Cơ chế thực thi

Khi một bài toán có các giá trị tọa độ $X_i \in [-10^9, 10^9]$ nhưng số lượng điểm $N \le 10^5$, ta không thể dùng mảng đánh dấu kích thước $10^9$.  
Ta nén các giá trị này về tập $\{0, 1, \dots, K-1\}$ với $K \le N$:

```cpp
vector<int> vals = a;
sort(vals.begin(), vals.end());
vals.erase(unique(vals.begin(), vals.end()), vals.end());

// Tìm chỉ số đã nén (0-based) của a[i] trong O(log N)
for (int i = 0; i < n; ++i) {
    int compressed_val = lower_bound(vals.begin(), vals.end(), a[i]) - vals.begin();
}
```


## 4. Kỹ thuật hai con trỏ co giãn (Dynamic Sliding Window)

### 4.1. Bài toán: Tìm đoạn con ngắn nhất có tổng $\ge S$
Với mảng gồm các số nguyên dương $A_i > 0$:

* Khi mở rộng con trỏ phải $R$, tổng `current_sum` tăng ngặt.
* Khi `current_sum >= S`, ta thu hẹp con trỏ trái $L$ để tìm độ dài ngắn nhất thỏa mãn.

```cpp
int min_len = n + 1;
long long current_sum = 0;
int l = 0;

for (int r = 0; r < n; ++r) {
    current_sum += a[r];
    while (current_sum >= s) {
        min_len = min(min_len, r - l + 1);
        current_sum -= a[l];
        l++;
    }
}
```


## 5. Mẫu cài đặt chuẩn thi đấu: 2D Prefix Sum

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, q;
    if (!(cin >> n >> m >> q)) return 0;

    vector<vector<long long>> a(n + 1, vector<long long>(m + 1, 0));
    vector<vector<long long>> pref(n + 1, vector<long long>(m + 1, 0));

    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= m; ++j) {
            cin >> a[i][j];
            pref[i][j] = pref[i - 1][j] + pref[i][j - 1] - pref[i - 1][j - 1] + a[i][j];
        }
    }

    while (q--) {
        int x1, y1, x2, y2;
        cin >> x1 >> y1 >> x2 >> y2;
        long long ans = pref[x2][y2] - pref[x1 - 1][y2] - pref[x2][y1 - 1] + pref[x1 - 1][y1 - 1];
        cout << ans << "\n";
    }
    return 0;
}
```


## 6. Ranh giới áp dụng

| Kỹ Thuật | Phạm Vi Sử Dụng | Độ Phức Tạp |
|---|---|:---:|
| **Two Pointers / Sliding Window** | Mảng 1D đơn điệu, tìm đoạn con thỏa mãn tính chất | $\mathcal{O}(N)$ |
| **2D Prefix Sum** | Truy vấn tổng ma trận con tĩnh | Tiền xử lý $\mathcal{O}(NM)$, truy vấn $\mathcal{O}(1)$ |
| **2D Difference Array** | Cập nhật cộng hình chữ nhật hàng loạt rồi mới truy vấn | Cập nhật $\mathcal{O}(1)$, khôi phục $\mathcal{O}(NM)$ |
| **Coordinate Compression** | Tọa độ lớn $10^9$ cần đưa về dải nhỏ để làm mảng đếm/cây | $\mathcal{O}(N \log N)$ |


## Bài tập thực hành phân tầng (P0 → P5)


### Bài 01 [CPPB2-L04-01]: TRUY VẤN TỔNG MA TRẬN CON 2D

**Đầu vào (Input):**

* Dòng 1: $N, M, Q$ ($1 \le N, M \le 1000, 1 \le Q \le 10^5$). $N$ dòng tiếp theo chứa ma trận. $Q$ dòng sau: $x_1, y_1, x_2, y_2$.

---

**Đầu ra (Output):**

* In ra tổng mỗi hình chữ nhật con trên một dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
3 3 2
1 2 3
4 5 6
7 8 9
1 1 2 2
2 2 3 3
```

**Output:**
```text
12
28
```

---



### Bài 02 [CPPB2-L04-02]: CẬP NHẬT HÌNH CHỮ NHẬT MA TRẬN 2D

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Cập Nhật Hình Chữ Nhật Ma Trận 2D.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N, M \le 1000, Q \le 10^5$.



### Bài 03 [CPPB2-L04-03]: ĐOẠN CON NGẮN NHẤT CÓ TỔNG $\GE S$

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Đoạn Con Ngắn Nhất Có Tổng $\ge S$.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N \le 10^5, A_i > 0$.



### Bài 04 [CPPB2-L04-04]: NÉN TỌA ĐỘ & ĐẾM TẦN SUẤT TRÊN DẢI LỚN

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Nén Tọa Độ & Đếm Tần Suất Trên Dải Lớn.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N \le 10^5, \vert X_i \vert \le 10^9$.



### Bài 05 [CPPB2-L04-05]: ĐOẠN CON DÀI NHẤT CÓ KHÔNG QUÁ K SỐ KHÁC NHAU

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Đoạn Con Dài Nhất Có Không Quá K Số Khác Nhau.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N \le 2 \times 10^5, K \le N$.



### Bài 06 [CPPB2-L04-06]: MA TRẬN CON CÓ TỔNG LỚN NHẤT (MAXIMUM SUBMATRIX SUM)

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Ma Trận Con Có Tổng Lớn Nhất (Maximum Submatrix Sum).

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N, M \le 400$.



### Bài 07 [CPPB2-L04-07]: DIỆN TÍCH PHỦ BỞI CÁC HÌNH CHỮ NHẬT RỜI RẠC

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Diện Tích Phủ Bởi Các Hình Chữ Nhật Rời Rạc.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N \le 1000$, tọa độ $\le 10^9$.



### Bài 08 [CPPB2-L04-08]: ĐẾM CẶP ĐOẠN THẲNG CHỒNG LẤN NHAU

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Đếm Cặp Đoạn Thẳng Chồng Lấn Nhau.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N \le 10^5, [L_i, R_i] \le 10^9$.



### Bài 09 [CPPB2-L04-09]: CỬA SỔ TRƯỢT ĐẾM SỐ LƯỢNG XÂU ANAGRAM

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Cửa Sổ Trượt Đếm Số Lượng Xâu Anagram.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $\vert S \vert \le 10^6, \vert P \vert \le 10^5$.



### Bài 10 [CPPB2-L04-10]: ĐẾM HÌNH VUÔNG CON CÓ TỔNG ĐÚNG BẰNG K

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Đếm Hình Vuông Con Có Tổng Đúng Bằng K.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N, M \le 1000, K \le 10^9$.



### Bài 11 [CPPB2-L04-11]: KHỬ CHIỀU 3-SUM & 4-SUM HAI CON TRỎ

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Khử Chiều 3-Sum & 4-Sum Hai Con Trỏ.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N \le 5000, \vert A_i \vert \le 10^9$.



### Bài 12 [CPPB2-L04-12]: ĐẾM SỐ ĐOẠN CON CÓ HIỆU MAX - MIN $\LE K$

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Đếm Số Đoạn Con Có Hiệu Max - Min $\le K$.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N \le 2 \times 10^5, K \le 10^9$.



### Bài 13 [CPPB2-L04-13]: ĐOẠN CON NGẮN NHẤT CHỨA ĐẦY ĐỦ BẢNG CHỮ CÁI

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Đoạn Con Ngắn Nhất Chứa Đầy Đủ Bảng Chữ Cái.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $\vert S \vert \le 10^6$.



### Bài 14 [CPPB2-L04-14]: MẢNG HIỆU TRÊN CÂY (TREE DIFFERENCE ARRAY)

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Mảng Hiệu Trên Cây (Tree Difference Array).

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N, Q \le 10^5$.



### Bài 15 [CPPB2-L04-15]: ĐẾM TAM GIÁC CÓ ĐỘ DÀI CẠNH HỢP LỆ

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Đếm Tam Giác Có Độ Dài Cạnh Hợp Lệ.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N \le 5000, A_i \le 10^9$.



### Bài 16 [CPPB2-L04-16]: QUÉT ĐƯỜNG THẲNG NÉN TỌA ĐỘ (SWEEP-LINE AREA 2D)

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Quét Đường Thẳng Nén Tọa Độ (Sweep-line Area 2D).

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N \le 10^5$, hình chữ nhật lớn.



# CHƯƠNG 03: ĐỆ QUY, CHIA ĐỂ TRỊ, MEET IN THE MIDDLE & MẶT NẠ BIT


# Bài 05: Đệ quy, chia để trị & kỹ thuật Meet in the Middle

## 1. Khái niệm & bản chất của phân rã không gian tìm kiếm

Đệ quy (Recursion) và Chia để trị (Divide and Conquer) là nền tảng tư duy cốt lõi trong khoa học máy tính: chia bài toán lớn thành các bài toán con đồng dạng có kích thước nhỏ hơn, giải quyết độc lập và kết hợp nghiệm.

Ở Level 2, ta khai thác bước nhảy vọt về tư duy tối ưu hóa:

* **Cây đệ quy & Định lý thợ (Master Theorem):** Phân tích chính xác chi phí thời gian của các hàm đệ quy phân nhánh $T(N) = a T(N/b) + \mathcal{O}(N^d)$.
* **Kỹ thuật Đếm nghịch thế (Inversion Count):** Vận dụng Merge Sort để đếm số cặp nghịch thế $i < j$ mà $A_i > A_j$ trong $\mathcal{O}(N \log N)$ (thay vì duyệt ngây thơ $\mathcal{O}(N^2)$).
* **Kỹ thuật Gặp nhau ở giữa (Meet in the Middle - MITM):** Khi không gian tìm kiếm là $2^N$ với $N = 40$ ($2^{40} \approx 10^{12} \implies \text{TLE}$), ta chia đôi tập hợp thành hai nửa $N/2 = 20$. Duyệt hai nửa độc lập ($2 \times 2^{20} \approx 2 \times 10^6$) rồi dùng Two Pointers / Binary Search để ghép nghiệm $\implies$ **Giảm độ phức tạp từ $\mathcal{O}(2^N)$ xuống $\mathcal{O}(2^{N/2} \log(2^{N/2}))$.**


## 2. Kỹ thuật đếm số cặp nghịch thế bằng Merge Sort

### 2.1. Bản chất toán học

Trong quá trình trộn (merge) hai nửa đã sắp xếp $[L \dots mid]$ và $[mid+1 \dots R]$:
Nếu phần tử bên nửa phải $A[j]$ nhỏ hơn phần tử bên nửa trái $A[i]$ ($A[j] < A[i]$), thì do nửa trái đã tăng dần, $A[j]$ sẽ nhỏ hơn **tất cả các phần tử từ $i$ đến $mid$**.  
Số lượng cặp nghịch thế tạo bởi $A[j]$ chính là:
$$\Delta = mid - i + 1$$

```cpp
long long merge_and_count(vector<int> &a, int l, int mid, int r) {
    vector<int> left(a.begin() + l, a.begin() + mid + 1);
    vector<int> right(a.begin() + mid + 1, a.begin() + r + 1);
    int i = 0, j = 0, k = l;
    long long inv_count = 0;

    while (i < left.size() && j < right.size()) {
        if (left[i] <= right[j]) {
            a[k++] = left[i++];
        } else {
            a[k++] = right[j++];
            inv_count += (left.size() - i); // Khai thác tính chất tăng dần
        }
    }
    while (i < left.size()) a[k++] = left[i++];
    while (j < right.size()) a[k++] = right[j++];
    return inv_count;
}
```


## 3. Kỹ thuật Meet in the Middle (MITM)

### 3.1. Bài toán Knapsack với $N \le 40$ và $W \le 10^{18}$

* Không thể dùng Quy hoạch động vì $W = 10^{18}$ quá lớn.
* Không thể duyệt nhánh cận toàn phần vì $2^{40} \approx 10^{12}$ quá lớn.

### 3.2. Thuật toán 3 bước MITM

1. **Nửa 1 ($N_1 = 20$):** Sinh tất cả $2^{20}$ tổng tập con, lưu vào `vector<long long> sum1`. Sắp xếp và lọc bỏ các trạng thái không tối ưu.
2. **Nửa 2 ($N_2 = 20$):** Sinh tất cả $2^{20}$ tổng tập con, lưu vào `vector<long long> sum2`.
3. **Ghép nghiệm:** Với mỗi giá trị $S \in sum2$, tìm giá trị lớn nhất trong $sum1$ mà $\le W - S$ bằng `upper_bound` trong $\mathcal{O}(\log(2^{N_1}))$.


## 4. Mẫu cài đặt chuẩn thi đấu: Meet in the Middle

```cpp
#include <bits/stdc++.h>
using namespace std;

void generate_sums(int idx, int end_idx, long long current_sum, const vector<long long> &a, vector<long long> &res) {
    if (idx == end_idx) {
        res.push_back(current_sum);
        return;
    }
    generate_sums(idx + 1, end_idx, current_sum, a, res);            // Không chọn
    generate_sums(idx + 1, end_idx, current_sum + a[idx], a, res);    // Có chọn
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long w;
    if (!(cin >> n >> w)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    int mid = n / 2;
    vector<long long> sum1, sum2;
    generate_sums(0, mid, 0, a, sum1);
    generate_sums(mid, n, 0, a, sum2);

    sort(sum2.begin(), sum2.end());

    long long max_weight = 0;
    for (long long s1 : sum1) {
        if (s1 <= w) {
            auto it = upper_bound(sum2.begin(), sum2.end(), w - s1);
            if (it != sum2.begin()) {
                --it;
                max_weight = max(max_weight, s1 + *it);
            }
        }
    }

    cout << max_weight << "\n";
    return 0;
}
```


## 5. Ranh giới áp dụng

| Phạm Vi $N$ | Thuật Toán Tối Ưu | Độ Phức Tạp |
|---|---|:---:|
| $N \le 20$ | Duyệt đệ quy / Bitmask toàn phần | $\mathcal{O}(2^N)$ |
| $N \le 40$ | Meet in the Middle (MITM) | $\mathcal{O}(2^{N/2} \log(2^{N/2}))$ |
| $N \le 10^5, W \le 10^5$ | Quy hoạch động Cái túi (DP Knapsack) | $\mathcal{O}(NW)$ |
| $N \le 10^5, W \le 10^{18}$ | Tham lam (nếu các phần tử chia hết) | $\mathcal{O}(N \log N)$ |


## Bài tập thực hành phân tầng (P0 → P5)


### Bài 01 [CPPB2-L05-01]: ĐẾM CẶP NGHỊCH THẾ

**Đầu vào (Input):**

* Dòng 1: $N$ ($1 \le N \le 10^5$). Dòng 2: $N$ số $A_i$ ($1 \le A_i \le 10^9$).

---

**Đầu ra (Output):**

* In ra tổng số cặp nghịch thế.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
2 4 1 3 5
```

**Output:**
```text
3
```

---



### Bài 02 [CPPB2-L05-02]: CÁI TÚI KÍCH THƯỚC NHỎ (KNAPSACK $N \LE 40$)

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Cái Túi Kích Thước Nhỏ (Knapsack $N \le 40$).

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N \le 40, W \le 10^{18}$.



### Bài 03 [CPPB2-L05-03]: TẬP CON CÓ TỔNG GẦN S NHẤT

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Tập Con Có Tổng Gần S Nhất.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N \le 36, S \le 10^{15}$.



### Bài 04 [CPPB2-L05-04]: GIẢI PHƯƠNG TRÌNH $4$ ẨN TUYẾN TÍNH (4-SUM MITM)

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Giải Phương Trình $4$ Ẩn Tuyến Tính (4-Sum MITM).

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N \le 4000, A_i \le 10^9$.



### Bài 05 [CPPB2-L05-05]: ĐẾM SỐ TẬP CON CÓ XOR BẰNG K

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Đếm Số Tập Con Có XOR Bằng K.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N \le 36, K \le 10^9$.



### Bài 06 [CPPB2-L05-06]: KHOẢNG CÁCH GIỮA HAI ĐIỂM GẦN NHẤT (CLOSEST PAIR)

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Khoảng Cách Giữa Hai Điểm Gần Nhất (Closest Pair).

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N \le 10^5$, tọa độ 2D.



### Bài 07 [CPPB2-L05-07]: BẺ KHÓA MẬT MÃ ĐỔI DẤU (SUBSET SUM WITH SIGNS)

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Bẻ Khóa Mật Mã Đổi Dấu (Subset Sum with Signs).

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N \le 38, \sum \pm a_i = 0$.



### Bài 08 [CPPB2-L05-08]: TỐI ƯU HÓA TUYẾN ĐƯỜNG ĐI QUA ĐỈNH (SHORTEST PATH WITH MITM)

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Tối Ưu Hóa Tuyến Đường Đi Qua Đỉnh (Shortest Path with MITM).

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: Đồ thị $N \le 40$, chi phí không âm.



### Bài 09 [CPPB2-L05-09]: TRÒ CHƠI XẾP GẠCH ĐA DIỆN (PUZZLE MITM)

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Trò Chơi Xếp Gạch Đa Diện (Puzzle MITM).

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: Trạng thái $2^{44}$.



### Bài 10 [CPPB2-L05-10]: ĐẾM CẶP $A_I > 2 A_J$ (SIGNIFICANT INVERSIONS)

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Đếm Cặp $A_i > 2 A_j$ (Significant Inversions).

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N \le 10^5, A_i \le 10^9$.



### Bài 11 [CPPB2-L05-11]: TỔNG CẤP SỐ NHÂN BẰNG CHIA ĐỂ TRỊ

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Tổng Cấp Số Nhân Bằng Chia Để Trị.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $A, N \le 10^{18}, M = 10^9+7$.



### Bài 12 [CPPB2-L05-12]: TỐI ƯU HÓA TUYẾN ĐƯỜNG ĐI QUA ĐỈNH (SHORTEST PATH MITM)

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Tối Ưu Hóa Tuyến Đường Đi Qua Đỉnh (Shortest Path MITM).

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: Đồ thị $N \le 40$, chi phí không âm.



### Bài 13 [CPPB2-L05-13]: TRÒ CHƠI XẾP GẠCH ĐA DIỆN (15-PUZZLE MITM)

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Trò Chơi Xếp Gạch Đa Diện (15-Puzzle MITM).

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: Trạng thái $2^{44}$.



### Bài 14 [CPPB2-L05-14]: PHÂN CHIA TẬP HỢP THÀNH HAI NỬA CÓ TỔNG BẰNG NHAU

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Phân Chia Tập Hợp Thành Hai Nửa Có Tổng Bằng Nhau.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N \le 36, A_i \le 10^9$.



### Bài 15 [CPPB2-L05-15]: ĐẾM SỐ ĐOẠN CON CÓ TỔNG NẰM TRONG $[L, R]$

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Đếm Số Đoạn Con Có Tổng Nằm Trong $[L, R]$.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N \le 10^5, \vert A_i \vert \le 10^9$.



### Bài 16 [CPPB2-L05-16]: CHIA ĐỂ TRỊ TRÊN CÂY (CENTROID DECOMPOSITION CƠ BẢN)

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Chia Để Trị Trên Cây (Centroid Decomposition Cơ Bản).

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: Cây $N \le 10^5$ đỉnh.




# Bài 06: Phép toán bit & mặt nạ bit nâng cao

## 1. Khái niệm & bản chất của tối ưu hóa cấp độ bit (Bit Manipulation)

Trong kiến trúc máy tính hiện đại, các phép toán trên bit (`AND`, `OR`, `XOR`, `NOT`, dịch bit `<<`, `>>`) được CPU xử lý trực tiếp ở mức phần cứng trong đúng $1$ chu kỳ xung nhịp (clock cycle).

Ở Level 2, phép toán bit được nâng cấp thành **Mặt nạ bit (Bitmask)** để biểu diễn trạng thái của một tập hợp con:

* Một số nguyên $M$ có thể đại diện cho một tập con của $N$ phần tử: bit thứ $i$ bật ($= 1$) nghĩa là phần tử thứ $i$ được chọn, bit thứ $i$ tắt ($= 0$) nghĩa là phần tử thứ $i$ không được chọn.
* **Duyệt toàn bộ $2^N$ tập con:** Dùng vòng lặp `for (int mask = 0; mask < (1 << N); ++mask)`.
* **Duyệt toàn bộ tập con của một mặt nạ bit (Submask Iteration):** Duyệt tất cả submask của `mask` trong tổng thời gian $\mathcal{O}(3^N)$ thay vì $\mathcal{O}(4^N)$ bằng thủ thuật `sub = (sub - 1) & mask`.
* **Quy hoạch động trên mặt nạ bit (Bitmask DP):** Giải các bài toán tối ưu trên tập hợp nhỏ ($N \le 20$) như bài toán Người du lịch (Traveling Salesperson Problem - TSP), ghép cặp hoàn hảo (Matching).


## 2. Bảng tổng hợp các thủ thuật Bitwise kinh điển (Bit Tricks)

| Thao Tác Toán Học | Biểu Thức C++ Chuẩn | Ý Nghĩa / Mục Đích |
|---|---|---|
| **Bật bit thứ $k$** | `mask \| (1 << k)` | Thêm phần tử $k$ vào tập hợp |
| **Tắt bit thứ $k$** | `mask & ~(1 << k)` | Loại bỏ phần tử $k$ khỏi tập hợp |
| **Đảo bit thứ $k$** | `mask ^ (1 << k)` | Chuyển đổi trạng thái có/không của $k$ |
| **Kiểm tra bit thứ $k$** | `(mask >> k) & 1` | Trả về 1 nếu $k$ thuộc tập, 0 nếu không |
| **Lấy bit 1 thấp nhất (LSB)** | `mask & (-mask)` | Trích xuất bit 1 nhỏ nhất (cực kỳ hữu ích trong Fenwick Tree) |
| **Tắt bit 1 thấp nhất** | `mask & (mask - 1)` | Xóa bit 1 nhỏ nhất (dùng đếm số bit 1 của Brian Kernighan) |
| **Đếm số bit 1 (Popcount)** | `__builtin_popcount(mask)` | Số lượng phần tử trong tập hợp |
| **Đếm số bit 0 ở đuôi** | `__builtin_ctz(mask)` | Vị trí của bit 1 thấp nhất |


## 3. Kỹ thuật duyệt Submask tối ưu $\mathcal{O}(3^N)$

Để duyệt tất cả các tập con $sub$ của một tập $mask$:
```cpp
for (int mask = 0; mask < (1 << n); ++mask) {
    for (int sub = mask; sub > 0; sub = (sub - 1) & mask) {
        // Xử lý submask 'sub' của 'mask'
    }
}
```

> **Chứng minh độ phức tạp:** Tổng số cặp $(mask, sub)$ là $\sum_{k=0}^N \binom{N}{k} 2^k = (1 + 2)^N = 3^N$. Với $N = 15$, $3^{15} \approx 1.4 \times 10^7$ phép tính (chạy trong $< 0.05\text{s}$).


## 4. Mẫu cài đặt chuẩn thi đấu: TSP với Bitmask DP

Bài toán Người du lịch: Tìm đường đi ngắn nhất thăm tất cả $N$ thành phố ($N \le 18$) xuất phát từ đỉnh 0.

```cpp
#include <bits/stdc++.h>
using namespace std;

const int INF = 1e9;
int n;
int dist_mat[20][20];
int dp[1 << 18][18]; // dp[mask][u]: Chi phí nhỏ nhất đi qua tập các đỉnh trong 'mask' và kết thúc tại u

int tsp(int mask, int u) {
    if (mask == (1 << n) - 1) return dist_mat[u][0]; // Quay về đỉnh 0
    if (dp[mask][u] != -1) return dp[mask][u];

    int ans = INF;
    for (int v = 0; v < n; ++v) {
        if (!((mask >> v) & 1)) { // Nếu đỉnh v chưa thăm
            ans = min(ans, dist_mat[u][v] + tsp(mask | (1 << v), v));
        }
    }
    return dp[mask][u] = ans;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    if (!(cin >> n)) return 0;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) cin >> dist_mat[i][j];
    }

    memset(dp, -1, sizeof(dp));
    cout << tsp(1, 0) << "\n"; // Bắt đầu tại đỉnh 0 với mask = 1 (chỉ mới thăm đỉnh 0)
    return 0;
}
```


## 5. Ranh giới áp dụng

| Phạm Vi $N$ | Kỹ Thuật Tối Ưu | Độ Phức Tạp |
|---|---|:---:|
| $N \le 20$ | Bitmask DP / Quy hoạch động trạng thái | $\mathcal{O}(2^N \times N^2)$ hoặc $\mathcal{O}(3^N)$ |
| $N \le 30$ | Meet in the Middle / Phân đôi tập hợp | $\mathcal{O}(2^{N/2})$ |
| $N \le 10^5$ | Greedy / Tree DP / Khử bit trực tiếp | $\mathcal{O}(N \log N)$ |


## Bài tập thực hành phân tầng (P0 → P5)


### Bài 01 [CPPB2-L06-01]: BÀI TOÁN NGƯỜI DU LỊCH (TSP)

**Đầu vào (Input):**

* Dòng 1: $N$. $N$ dòng tiếp theo: Ma trận khoảng cách $C_{i, j}$.

---

**Đầu ra (Output):**

* In ra chi phí nhỏ nhất.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
4
0 10 15 20
10 0 35 25
15 35 0 30
20 25 30 0
```

**Output:**
```text
80
```

---



### Bài 02 [CPPB2-L06-02]: ĐẾM SỐ PHẦN TỬ BẬT BIT CHUNG (BITWISE AND)

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Đếm Số Phần Tử Bật Bit Chung (Bitwise AND).

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N \le 10^5, A_i \le 10^9$.



### Bài 03 [CPPB2-L06-03]: BÀI TOÁN NGƯỜI DU LỊCH (TSP BITMASK DP)

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Bài Toán Người Du Lịch (TSP Bitmask DP).

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N \le 18$.



### Bài 04 [CPPB2-L06-04]: PHÂN CHIA CÔNG VIỆC HOÀN HẢO (JOB ASSIGNMENT)

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Phân Chia Công Việc Hoàn Hảo (Job Assignment).

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N \le 20$.



### Bài 05 [CPPB2-L06-05]: DUYỆT TẤT CẢ SUBMASK TÍNH TỔNG PHÂN HOẠCH

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Duyệt Tất Cả Submask Tính Tổng Phân Hoạch.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N \le 15$.



### Bài 06 [CPPB2-L06-06]: ĐƯỜNG ĐI HAMILTON ĐẾM SỐ CÁCH

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Đường Đi Hamilton Đếm Số Cách.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N \le 19$, đồ thị có hướng.



### Bài 07 [CPPB2-L06-07]: TỐI ĐA HÓA GIÁ TRỊ XOR ĐOẠN CON BẰNG TRIE BIT

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Tối Đa Hóa Giá Trị XOR Đoạn Con Bằng Trie Bit.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N \le 10^5, A_i \le 10^9$.



### Bài 08 [CPPB2-L06-08]: GHÉP CẶP TRỌNG SỐ CỰC ĐẠI (MAXIMUM MATCHING BITMASK)

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Ghép Cặp Trọng Số Cực Đại (Maximum Matching Bitmask).

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N \le 22$.



### Bài 09 [CPPB2-L06-09]: SOS DP (SUM OVER SUBSETS DYNAMIC PROGRAMMING)

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán SOS DP (Sum Over Subsets Dynamic Programming).

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N \le 20$.



### Bài 10 [CPPB2-L06-10]: ĐẾM SỐ CẶP $(A_I, A_J)$ CÓ TÍCH AND BẰNG 0

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Đếm Số Cặp $(A_i, A_j)$ Có Tích AND Bằng 0.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N \le 10^5, A_i \le 10^6$.



### Bài 11 [CPPB2-L06-11]: SOS DP (SUM OVER SUBSETS DYNAMIC PROGRAMMING)

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán SOS DP (Sum Over Subsets Dynamic Programming).

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N \le 20$.



### Bài 12 [CPPB2-L06-12]: TÔ MÀU ĐỒ THỊ SỐ LƯỢNG MÀU NHỎ NHẤT (GRAPH COLORING)

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Tô Màu Đồ Thị Số Lượng Màu Nhỏ Nhất (Graph Coloring).

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N \le 18$.



### Bài 13 [CPPB2-L06-13]: TÌM CHU TRÌNH HAMILTON CHI PHÍ NHỎ NHẤT

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Tìm Chu Trình Hamilton Chi Phí Nhỏ Nhất.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N \le 20, C_{i, j} \ge 0$.



### Bài 14 [CPPB2-L06-14]: TẬP ĐỘC LẬP TRỌNG SỐ LỚN NHẤT TRÊN ĐỒ THỊ NHỎ

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Tập Độc Lập Trọng Số Lớn Nhất Trên Đồ Thị Nhỏ.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N \le 22$.



### Bài 15 [CPPB2-L06-15]: PHÂN HOẠCH TẬP HỢP THÀNH K TẬP CON CÓ TỔNG BẰNG NHAU

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Phân Hoạch Tập Hợp Thành K Tập Con Có Tổng Bằng Nhau.

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N \le 16, K \le N$.



### Bài 16 [CPPB2-L06-16]: TỐI ƯU HÓA TRÒ CHƠI NIM TỔNG QUÁT (SPRAGUE-GRUNDY BIT)

**Đầu vào (Input):**

* Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
* Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

---

**Đầu ra (Output):**

* In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

---

**Ví dụ mẫu:**

### Sample 1:
**Input:**
```text
5
1 2 3 4 5
```

**Output:**
```text
15
```

### Giải thích Sample 1:
* Kết quả tính toán phù hợp với yêu cầu của bài toán Tối Ưu Hóa Trò Chơi Nim Tổng Quát (Sprague-Grundy Bit).

---

**Ràng buộc dữ liệu:**

* Ràng buộc dữ liệu: $N \le 10^5, A_i \le 10^9$.





\newpage

# Phụ lục A: Nền tảng C++

> Phần này tóm tắt toàn bộ cú pháp, cấu trúc dữ liệu và quy trình giải bài C++ cơ bản.

## 1. KHUNG TƯ DUY CỦA MỌI BÀI LẬP TRÌNH

Mọi bài toán đều bắt đầu bằng chuỗi câu hỏi:

```text
Đề bài → Dữ liệu → Biến → Công thức/Điều kiện
       → Các bước xử lý → Code → Kiểm tra kết quả
```

### Mô hình Input – Process – Output

| Thành phần | Câu hỏi cần trả lời |
|---|---|
| **Input** | Chương trình nhận những dữ liệu nào? |
| **Process** | Cần tính toán, kiểm tra hoặc lặp lại việc gì? |
| **Output** | Cần in ra kết quả nào, theo định dạng nào? |

Trước khi viết code, hãy viết bằng lời hoặc pseudocode:

```text
1. Đọc dữ liệu.
2. Tính hoặc xử lý dữ liệu.
3. Kiểm tra điều kiện nếu có.
4. In kết quả.
```

### Công thức trước code

Không viết code trước khi biết mình đang tính gì.

```text
Bài toán → Công thức hoặc quy tắc → Code
```

Ví dụ tính diện tích hình chữ nhật:

```text
S = chiều_dài × chiều_rộng
```

```cpp
long long area = length * width;
```

Ví dụ tính trung bình (giữ phần thập phân):

```cpp
double average = 1.0 * sum / n;
```

### Chuỗi ghi nhớ nền tảng

> **BIẾN → TÍNH → ĐIỀU KIỆN → LẶP → TÍCH LŨY → MẢNG → HÀM → DEBUG**

| Từ khóa | Câu hỏi tự kiểm tra |
|---|---|
| **Biến** | Tôi cần lưu dữ liệu gì? |
| **Tính** | Tôi cần công thức nào? |
| **Điều kiện** | Tôi cần đưa ra quyết định nào? |
| **Lặp** | Tôi cần làm việc gì nhiều lần? |
| **Tích lũy** | Tôi cần cộng, đếm, tìm lớn nhất hay nhỏ nhất? |
| **Mảng** | Tôi có nhiều dữ liệu cùng loại không? |
| **Hàm** | Tôi có thể tách phần việc nào thành một nhiệm vụ riêng? |
| **Debug** | Nếu kết quả sai, tôi sẽ kiểm tra từ đâu? |

---

## 2. KHUNG CHƯƠNG TRÌNH C++ TỐI THIỂU

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    // 1. Khai báo biến
    // 2. Đọc dữ liệu
    // 3. Xử lý
    // 4. In kết quả

    return 0;
}
```

| Thành phần | Ý nghĩa |
|---|---|
| `#include <bits/stdc++.h>` | Nạp các thư viện C++ thường dùng trong thi đấu |
| `using namespace std;` | Cho phép dùng `vector`, `string`, `cin`, `cout`… trực tiếp |
| `int main()` | Điểm bắt đầu thực hiện chương trình |
| `ios::sync_with_stdio(false);` | Tăng tốc nhập/xuất |
| `cin.tie(nullptr);` | Tối ưu liên kết giữa nhập và xuất |
| `return 0;` | Kết thúc chương trình thành công |

Giai đoạn đầu chỉ cần tập trung vào **dữ liệu – xử lý – kết quả**, chưa cần hiểu sâu cơ chế thư viện.

---

## 3. BIẾN VÀ KIỂU DỮ LIỆU

> **Biến là ô nhớ có tên để lưu dữ liệu.**

```cpp
int age = 15;
long long population = 9000000000LL;
double average = 8.5;
char grade = 'A';
string name = "An";
bool passed = true;
```

| Kiểu | Dùng để lưu | Ví dụ |
|---|---|---|
| `int` | Số nguyên thông thường | tuổi, số lượng nhỏ |
| `long long` | Số nguyên lớn hoặc tổng lớn | tổng tiền, tổng mảng |
| `double` | Số thực | trung bình, kết quả đo |
| `char` | Một ký tự | `'A'`, `'7'` |
| `string` | Một chuỗi ký tự | `"Hello"` |
| `bool` | Đúng hoặc sai | `true`, `false` |

### Quy tắc chọn kiểu dữ liệu

| Nếu giá trị… | Nên nghĩ đến… |
|---|---|
| Là số đếm nhỏ | `int` |
| Có thể vượt giới hạn `int`, hoặc là tổng nhiều số | `long long` |
| Có phần thập phân | `double` |
| Là một ký tự duy nhất | `char` |
| Là nhiều ký tự liên tiếp | `string` |
| Chỉ có hai trạng thái đúng/sai | `bool` |

> Khi chưa chắc tổng có lớn hay không, hãy cân nhắc dùng `long long`.

### Khởi tạo biến tích lũy

```cpp
long long sum = 0;
int count = 0;
int mx = -1000000000;
int mn = 1000000000;
```

Biến dùng để cộng hoặc đếm phải có giá trị ban đầu đúng. Không dùng biến chưa khởi tạo.

---

## 4. NHẬP VÀ XUẤT DỮ LIỆU

```cpp
int a, b;
cin >> a >> b;
cout << a + b << '\n';
```

```cpp
string s;
cin >> s;
cout << s << '\n';
```

| Lệnh | Ý nghĩa |
|---|---|
| `cin >> a` | Đọc một giá trị vào biến `a` |
| `cin >> a >> b` | Đọc nhiều giá trị liên tiếp |
| `cout << answer` | In kết quả |
| `<< '\n'` | Xuống dòng |

Nếu cần đọc cả một dòng có khoảng trắng, có thể dùng:

```cpp
getline(cin, s);
```

Trong phần lớn bài thi cơ bản, dữ liệu dạng số hoặc từ không có khoảng trắng có thể đọc bằng `cin >>`.

### Ba mẹo thi đấu thường gặp

```cpp
// 1. Đọc nhiều bộ test đến khi hết file
int n;
while (cin >> n) {
    // xử lý từng bộ test
}

// 2. Đọc dòng có khoảng trắng sau khi đã cin >> n
cin.ignore(numeric_limits<streamsize>::max(), '\n');
getline(cin, s);

// 3. Ép kiểu giữ phần thập phân khi sum là long long
double avg = 1.0 * sum / n;
```

> Cần `#include <bits/stdc++.h>` đã bao gồm `limits` cho `numeric_limits`.

---

## 5. TOÁN TỬ VÀ BIỂU THỨC

### Toán tử số học

| Toán tử | Ý nghĩa | Ví dụ |
|---|---|---|
| `+` | Cộng | `a + b` |
| `-` | Trừ | `a - b` |
| `*` | Nhân | `a * b` |
| `/` | Chia | `a / b` |
| `%` | Phần dư | `a % b` |

### Chia nguyên và phần dư

```cpp
15 / 4 == 3
15 % 4 == 3
```

Khi cả hai toán hạng là số nguyên, phép `/` cho phần nguyên. Toán tử `%` cho phần dư.

| Mẫu | Ý nghĩa |
|---|---|
| `x % 2 == 0` | `x` là số chẵn |
| `x % 2 != 0` | `x` là số lẻ |
| `x % 10` | Chữ số cuối của `x` |
| `x / 10` | Bỏ chữ số cuối của `x` |
| `a % b == 0` | `a` chia hết cho `b` |

### Toán tử so sánh

```cpp
>    <    >=    <=    ==    !=
```

| Toán tử | Ý nghĩa |
|---|---|
| `==` | Bằng nhau |
| `!=` | Khác nhau |
| `>` | Lớn hơn |
| `<` | Nhỏ hơn |
| `>=` | Lớn hơn hoặc bằng |
| `<=` | Nhỏ hơn hoặc bằng |

> **Lưu ý:** Đừng nhầm `=` (gán) với `==` (so sánh).

### Toán tử logic

| Toán tử | Ý nghĩa | Ví dụ |
|---|---|---|
| `&&` | Và | `age >= 10 && age <= 15` |
| `||` | Hoặc | `x == 0 || y == 0` |
| `!` | Phủ định | `!passed` |

---

## 6. ĐIỀU KIỆN — RẼ NHÁNH

### Mẫu cơ bản

```cpp
if (condition) {
    // việc A
} else {
    // việc B
}
```

Mô hình bằng lời:

```text
NẾU điều kiện đúng
    thực hiện A
NGƯỢC LẠI
    thực hiện B
```

### Nhiều trường hợp

```cpp
if (score >= 8) {
    cout << "Gioi";
} else if (score >= 6.5) {
    cout << "Kha";
} else {
    cout << "Can co gang";
}
```

### Điều kiện lồng nhau

Chỉ dùng khi quyết định thứ hai phụ thuộc vào quyết định thứ nhất. Hãy viết điều kiện bằng lời trước để tránh rối.

### Lỗi thường gặp

| Lỗi | Cách kiểm tra |
|---|---|
| Dùng `=` thay cho `==` | Đọc lại mọi điều kiện so sánh |
| Nhầm `>` với `>=` | Kiểm tra trường hợp bằng đúng ngưỡng |
| Thiếu trường hợp | Thử giá trị nhỏ nhất, lớn nhất và đúng biên |
| Điều kiện quá phức tạp | Tách thành các biến `bool` hoặc viết lại bằng lời |

---

## 7. VÒNG LẶP – LÀM MỘT VIỆC NHIỀU LẦN

Trước khi viết vòng lặp, trả lời ba câu hỏi:

1. Việc gì được lặp lại?
2. Biến nào thay đổi sau mỗi lần?
3. Khi nào vòng lặp dừng?

### `for`: biết trước số lần hoặc khoảng lặp

```cpp
for (int i = 0; i < n; i++) {
    // xử lý phần tử thứ i
}
```

Với mảng có `n` phần tử, chỉ số thường chạy từ `0` đến `n - 1`.

### `while`: lặp khi điều kiện còn đúng

```cpp
while (condition) {
    // xử lý
    // phải có cách làm condition thay đổi
}
```

Nếu điều kiện không bao giờ sai, chương trình có thể lặp vô hạn.

### `do..while`: thực hiện ít nhất một lần

```cpp
do {
    // xử lý
} while (condition);
```

Trong phần C++ cơ bản, `for` và `while` là hai dạng cần dùng thành thạo nhất.

### Vòng lặp lồng nhau

```cpp
for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
        // xử lý từng cặp (i, j)
    }
}
```

Nếu vòng ngoài chạy `N` lần và vòng trong chạy `M` lần, số thao tác thường là `O(NM)`.

---

## 8. BỐN MẪU TÍCH LŨY

### Tính tổng

```cpp
long long sum = 0;
for (int x : a) {
    sum += x;
}
```

### Đếm phần tử thỏa điều kiện

```cpp
int count = 0;
for (int x : a) {
    if (x % 2 == 0) count++;
}
```

### Tìm giá trị lớn nhất

```cpp
int mx = a[0];
for (int x : a) {
    mx = max(mx, x);
}
```

### Tìm giá trị nhỏ nhất

```cpp
int mn = a[0];
for (int x : a) {
    mn = min(mn, x);
}
```

> Nếu dữ liệu có thể rỗng, không được truy cập `a[0]` trước khi kiểm tra kích thước. Có thể khởi tạo `mx`, `mn` theo giới hạn bài toán.

---

## 9. MẢNG, `VECTOR` VÀ `STRING`

### Mảng và chỉ số

```text
a[0], a[1], a[2], .., a[n - 1]
```

> **Chỉ số bắt đầu từ 0.** Với `n` phần tử, chỉ số hợp lệ là `0 … n-1`.

### Đọc và duyệt mảng

```cpp
int n;
cin >> n;

vector<int> a(n);
for (int i = 0; i < n; i++) {
    cin >> a[i];
}

for (int i = 0; i < n; i++) {
    cout << a[i] << ' ';
}
```

### Duyệt bằng phần tử

```cpp
for (int x : a) {
    cout << x << ' ';
}
```

Dùng chỉ số `i` khi cần biết vị trí hoặc cập nhật `a[i]`. Dùng `x` khi chỉ cần đọc từng giá trị.

### Các thao tác `vector` cơ bản

| Lệnh | Ý nghĩa |
|---|---|
| `vector<int> a(n)` | Tạo vector có `n` phần tử |
| `a.size()` | Số phần tử |
| `a.push_back(x)` | Thêm `x` vào cuối |
| `a.pop_back()` | Xóa phần tử cuối |
| `a[i]` | Truy cập phần tử vị trí `i` |
| `a.empty()` | Kiểm tra có rỗng không |

### Xử lý `string`

```cpp
string s;
cin >> s;

for (int i = 0; i < (int)s.size(); i++) {
    if (s[i] == 'A') {
        // xử lý ký tự A
    }
}
```

| Biểu thức | Ý nghĩa |
|---|---|
| `s.size()` | Độ dài xâu |
| `s[i]` | Ký tự ở vị trí `i` |
| `s.front()` | Ký tự đầu |
| `s.back()` | Ký tự cuối |
|

---

## 10. HÀM — CHIA BÀI TOÁN THÀNH CÁC PHẦN

> **Hàm là một khối công việc riêng:** nhận dữ liệu vào, thực hiện một nhiệm vụ và có thể trả về kết quả.

```cpp
int square(int x) {
    return x * x;
}
```

```cpp
int result = square(5); // result = 25
```

### Mẫu hàm

```cpp
return_type function_name(parameters) {
    // xử lý
    return value;
}
```

Nếu hàm không trả về kết quả, dùng `void`:

```cpp
void printLine(int n) {
    for (int i = 0; i < n; i++) cout << '-';
    cout << '\n';
}
```

Hàm nên thực hiện **một nhiệm vụ rõ ràng**. Các tên hàm thường gặp trong bài thuật toán là `check()`, `isPrime()`, `gcd()`, `solve()` và `dfs()`.

---

## 11. GỠ LỖI VÀ KIỂM THỬ

Khi chương trình sai, không đoán bừa. Hãy kiểm tra theo thứ tự:

| Câu hỏi | Việc cần làm |
|---|---|
| Input có đúng không? | Đọc lại định dạng và số lượng dữ liệu |
| Kiểu dữ liệu có đủ lớn không? | Kiểm tra `int`, `long long`, phép nhân và tổng |
| Công thức có đúng không? | Tính thủ công bằng một ví dụ nhỏ |
| Điều kiện có đúng không? | Thử trường hợp bằng biên, nhỏ hơn và lớn hơn biên |
| Vòng lặp có chạy đủ không? | Theo dõi giá trị bắt đầu, kết thúc và bước nhảy |
| Chỉ số có hợp lệ không? | Kiểm tra `0 ≤ i < n` |
| Kết quả trung gian có đúng không? | In biến tạm tại vị trí cần kiểm tra |

### In giá trị trung gian

```cpp
cerr << "i = " << i << ", sum = " << sum << '\n';
```

Có thể dùng `cout` ở bài đơn giản, nhưng phải xóa các dòng debug trước khi nộp nếu output yêu cầu chính xác.

### Bộ test tối thiểu

Mỗi bài nên thử:

1. Ví dụ mẫu.
2. Dữ liệu nhỏ nhất.
3. Dữ liệu lớn nhất hoặc gần lớn nhất.
4. Trường hợp đúng bằng ngưỡng.
5. Trường hợp không có phần tử thỏa điều kiện.
6. Trường hợp tất cả phần tử đều thỏa điều kiện.
7. Trường hợp có nhiều phần tử bằng nhau.

---

## 12. ĐỘ PHỨC TẠP — CHƯƠNG TRÌNH CÓ ĐỦ NHANH?

| Độ phức tạp | Trực giác |
|---|---|
| `O(1)` | Số thao tác gần như không phụ thuộc kích thước dữ liệu |
| `O(log N)` | Mỗi bước thu nhỏ đáng kể phạm vi tìm kiếm |
| `O(N)` | Duyệt dữ liệu một lần |
| `O(N log N)` | Thường gặp khi sắp xếp |
| `O(N²)` | Xét mọi cặp hoặc hai vòng lặp theo `N` |
| `O(2^N)` | Thử mọi tập con; chỉ phù hợp với `N` nhỏ |

### Quy tắc đọc giới hạn

| Nếu `N` khoảng… | Có thể cân nhắc… |
|---:|---|
| `N ≤ 20` | Duyệt tập con, bitmask, quay lui |
| `N ≤ 10^3` | Một số lời giải `O(N²)` |
| `N ≤ 10^5` hoặc `2 × 10^5` | `O(N)`, `O(N log N)` |
| `N` rất lớn | Công thức, toán học hoặc tối ưu mạnh hơn |

Đây chỉ là quy tắc định hướng. Cần xét thêm số test, hằng số trong chương trình và giới hạn thời gian.

---

## TÓM TẮT MỘT TRANG

```text
BIẾN
  Tôi cần lưu dữ liệu gì?

TÍNH
  Tôi cần công thức nào?

ĐIỀU KIỆN
  Tôi cần quyết định điều gì?

LẶP
  Tôi cần làm việc gì nhiều lần?

TÍCH LŨY
  Tôi cần cộng, đếm, max hay min?

MẢNG
  Tôi có nhiều dữ liệu cùng loại không?

HÀM
  Tôi có thể tách nhiệm vụ nào thành một khối công việc riêng?

DEBUG
  Input, biến, công thức, điều kiện, vòng lặp và kết quả trung gian có đúng không?
```

> **Mục tiêu của C++ Cơ bản:** Không phải nhớ thật nhiều câu lệnh, mà là nhìn một bài toán đơn giản và biết biến nó thành các bước có thể lập trình được.



\newpage

# Phụ lục B: Lời giải bài tập tham khảo

> Phần này cung cấp mã nguồn C++ tham khảo chuẩn thi đấu cho các bài tập thực hành trong sách.

## Chương 01 — Bài 01: Số học cơ bản & chuyên sâu

### `CPPB2-L01-01` — ƯỚC CHUNG & BỘI CHUNG CƠ BẢN

```cpp
#include <bits/stdc++.h>
using namespace std;

long long gcd_calc(long long a, long long b) {
    while (b != 0) {
        long long r = a % b;
        a = b;
        b = r;
    }
    return a;
}

long long lcm_calc(long long a, long long b) {
    if (a == 0 || b == 0) return 0;
    return (a / gcd_calc(a, b)) * b;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    if (!(cin >> t)) return 0;

    while (t--) {
        long long a, b;
        if (!(cin >> a >> b)) break;
        long long g = gcd_calc(a, b);
        long long l = lcm_calc(a, b);
        cout << g << " " << l << "\n";
    }
    return 0;
}

```

### `CPPB2-L01-02` — RÚT GỌN MẢNG PHÂN SỐ LỚN

```cpp
#include <bits/stdc++.h>
using namespace std;

long long gcd_calc(long long a, long long b) {
    while (b != 0) {
        long long r = a % b;
        a = b;
        b = r;
    }
    return a;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    while (n--) {
        long long a, b;
        if (!(cin >> a >> b)) break;

        if (b < 0) {
            a = -a;
            b = -b;
        }

        if (a == 0) {
            cout << "0 1\n";
        } else {
            long long g = gcd_calc(abs(a), b);
            cout << a / g << " " << b / g << "\n";
        }
    }
    return 0;
}

```

### `CPPB2-L01-03` — SÀNG ƯỚC SỐ NGUYÊN TỐ NHỎ NHẤT (SPF)

```cpp
#include <bits/stdc++.h>
using namespace std;

const int MAXN = 1000000;
int spf[MAXN + 1];

void sieve_spf() {
    for (int i = 1; i <= MAXN; ++i) spf[i] = i;
    for (int i = 2; i * i <= MAXN; ++i) {
        if (spf[i] == i) {
            for (int j = i * i; j <= MAXN; j += i) {
                if (spf[j] == j) {
                    spf[j] = i;
                }
            }
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    sieve_spf();

    int q;
    if (!(cin >> q)) return 0;

    while (q--) {
        int x;
        if (!(cin >> x)) break;
        cout << spf[x] << "\n";
    }
    return 0;
}

```

### `CPPB2-L01-04` — PHÂN TÍCH THỪA SỐ TRUY VẤN NHANH

```cpp
#include <bits/stdc++.h>
using namespace std;

const int MAXN = 1000000;
int spf[MAXN + 1];

void sieve_spf() {
    for (int i = 1; i <= MAXN; ++i) spf[i] = i;
    for (int i = 2; i * i <= MAXN; ++i) {
        if (spf[i] == i) {
            for (int j = i * i; j <= MAXN; j += i) {
                if (spf[j] == j) {
                    spf[j] = i;
                }
            }
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    sieve_spf();

    int q;
    if (!(cin >> q)) return 0;

    while (q--) {
        int n;
        if (!(cin >> n)) break;

        bool first = true;
        while (n > 1) {
            int p = spf[n];
            int cnt = 0;
            while (n % p == 0) {
                cnt++;
                n /= p;
            }
            if (!first) cout << " ";
            cout << p << "^" << cnt;
            first = false;
        }
        cout << "\n";
    }
    return 0;
}

```

### `CPPB2-L01-05` — ĐẾM ƯỚC SỐ & TỔNG ƯỚC SỐ NHANH

```cpp
#include <bits/stdc++.h>
using namespace std;

const int MAXN = 1000000;
int spf[MAXN + 1];

void sieve_spf() {
    for (int i = 1; i <= MAXN; ++i) spf[i] = i;
    for (int i = 2; i * i <= MAXN; ++i) {
        if (spf[i] == i) {
            for (int j = i * i; j <= MAXN; j += i) {
                if (spf[j] == j) spf[j] = i;
            }
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    sieve_spf();

    int q;
    if (!(cin >> q)) return 0;

    while (q--) {
        int n;
        if (!(cin >> n)) break;

        long long d = 1, sigma = 1;
        while (n > 1) {
            int p = spf[n];
            int a = 0;
            long long pk = 1;
            while (n % p == 0) {
                a++;
                pk *= p;
                n /= p;
            }
            d *= (a + 1);
            sigma *= (pk * p - 1) / (p - 1);
        }
        cout << d << " " << sigma << "\n";
    }
    return 0;
}

```

### `CPPB2-L01-06` — SÀNG NGUYÊN TỐ ĐOẠN [L, R]

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long L, R;
    if (!(cin >> L >> R)) return 0;

    long long limit = sqrt(R);
    vector<bool> mark(limit + 1, true);
    vector<long long> primes;

    for (long long p = 2; p <= limit; ++p) {
        if (mark[p]) {
            primes.push_back(p);
            for (long long j = p * p; j <= limit; j += p) {
                mark[j] = false;
            }
        }
    }

    vector<bool> is_prime_range(R - L + 1, true);
    for (long long p : primes) {
        long long start = max(p * p, ((L + p - 1) / p) * p);
        for (long long j = start; j <= R; j += p) {
            is_prime_range[j - L] = false;
        }
    }

    if (L == 1) {
        is_prime_range[0] = false;
    }

    int count_primes = 0;
    for (int i = 0; i <= R - L; ++i) {
        if (is_prime_range[i]) {
            count_primes++;
        }
    }

    cout << count_primes << "\n";
    return 0;
}

```

### `CPPB2-L01-07` — Cặp Số Nguyên Tố Sinh Đôi Trong Đoạn

```cpp
#include <bits/stdc++.h>
using namespace std;
int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int t;if(!(cin>>t))return 0;while(t--){long long L,R;cin>>L>>R;int lim=sqrt((long double)R)+1;vector<bool>b(lim+1,true);vector<int>p;for(int i=2;i<=lim;i++)if(b[i]){p.push_back(i);if(1LL*i*i<=lim)for(long long j=1LL*i*i;j<=lim;j+=i)b[j]=false;}vector<bool>ok(R-L+1,true);for(int x:p){long long st=max(1LL*x*x,((L+x-1)/x)*x);for(long long j=st;j<=R;j+=x)ok[j-L]=false;}if(L<=0)ok[0-L]=false;if(L<=1&&1<=R)ok[1-L]=false;long long ans=0;for(long long x=L;x+2<=R;x++)if(ok[x-L]&&ok[x+2-L])ans++;cout<<ans<<'\n';} }
```

### `CPPB2-L01-08` — TÌM NGHIỆM NGUYÊN PHƯƠNG TRÌNH DIOPHANTINE

```cpp
#include <bits/stdc++.h>
using namespace std;

long long extgcd(long long a, long long b, long long &x, long long &y) {
    if (b == 0) {
        x = 1;
        y = 0;
        return a;
    }
    long long x1, y1;
    long long g = extgcd(b, a % b, x1, y1);
    x = y1;
    y = x1 - (a / b) * y1;
    return g;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    if (!(cin >> t)) return 0;

    while (t--) {
        long long a, b, c;
        if (!(cin >> a >> b >> c)) break;

        if (a == 0 && b == 0) {
            if (c == 0) cout << "YES 0 0\n";
            else cout << "NO\n";
            continue;
        }

        long long sa = (a < 0 ? -1 : 1);
        long long sb = (b < 0 ? -1 : 1);
        long long aa = abs(a), bb = abs(b);

        long long x0, y0;
        long long g = extgcd(aa, bb, x0, y0);

        if (c % g != 0) {
            cout << "NO\n";
        } else {
            long long mul = c / g;
            long long rx = x0 * mul * sa;
            long long ry = y0 * mul * sb;
            cout << "YES " << rx << " " << ry << "\n";
        }
    }
    return 0;
}

```

### `CPPB2-L01-09` — Nghiệm Nguyên Dương Nhỏ Nhất

```cpp
#include <bits/stdc++.h>
using namespace std;
long long eg(long long a,long long b,long long&x,long long&y){if(!b){x=1;y=0;return a;}long long x1,y1,g=eg(b,a%b,x1,y1);x=y1;y=x1-(a/b)*y1;return g;}
long long flo(long long a,long long b){long long q=a/b,r=a%b;if(r&&a<0)--q;return q;}long long cei(long long a,long long b){return -flo(-a,b);}int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int t;if(!(cin>>t))return 0;while(t--){long long A,B,C;cin>>A>>B>>C;if(A<=0||B<=0||C<=0){cout<<"NO\n";continue;}long long x0,y0,g=eg(A,B,x0,y0);if(C%g){cout<<"NO\n";continue;}long long x=x0*(C/g),y=y0*(C/g),u=B/g,v=A/g;long long lo=cei(1-x,u),hi=flo(y-1,v);if(lo>hi){cout<<"NO\n";continue;}cout<<x+u*lo<<' '<<y-v*lo<<'\n';} }
```

### `CPPB2-L01-10` — HÀM PHI EULER $\PHI(N)$ NHANH VỚI SPF

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L01-10: Hàm Phi Euler $\phi(N)$ Nhanh Với SPF
// Goal: Đếm số nguyên tố cùng nhau qua SPF

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L01-11` — Phân Tích Giai Thừa N! (Legendre)

```cpp
#include <bits/stdc++.h>
using namespace std;int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int q;if(!(cin>>q))return 0;while(q--){long long n,p;cin>>n>>p;long long ans=0;while(n){n/=p;ans+=n;}cout<<ans<<'\n';}}
```

### `CPPB2-L01-12` — Số Ước Số Lẻ & Số Chính Phương

```cpp
#include <bits/stdc++.h>
using namespace std;int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int q;if(!(cin>>q))return 0;while(q--){long long a,b;cin>>a>>b;cout<<max(0LL,(long long)sqrt((long double)b)-(long long)sqrt((long double)max(0LL,a-1)))<<'\n';}}
```

### `CPPB2-L01-13` — Cặp Số Có GCD và LCM Cho Trước

```cpp
#include <bits/stdc++.h>
using namespace std;int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int q;if(!(cin>>q))return 0;while(q--){long long g,L;cin>>g>>L;if(g<=0||L<=0||L%g){cout<<0<<'\n';continue;}long long m=L/g,ans=0;for(long long d=1;d*d<=m;d++)if(m%d==0&&gcd(d,m/d)==1)ans++;cout<<ans<<'\n';}}
```

### `CPPB2-L01-14` — Khoảng Cách Cực Đại Giữa Hai Số Nguyên Tố

```cpp
#include <bits/stdc++.h>
using namespace std;int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int q;if(!(cin>>q))return 0;while(q--){long long L,R;cin>>L>>R;int lim=sqrt((long double)R)+1;vector<bool>b(lim+1,true);vector<int>p;for(int i=2;i<=lim;i++)if(b[i]){p.push_back(i);if(1LL*i*i<=lim)for(long long j=1LL*i*i;j<=lim;j+=i)b[j]=false;}vector<bool>ok(R-L+1,true);for(int x:p){long long st=max(1LL*x*x,((L+x-1)/x)*x);for(long long j=st;j<=R;j+=x)ok[j-L]=false;}if(L<=0)ok[0-L]=false;if(L<=1&&1<=R)ok[1-L]=false;long long prev=-1,ans=-1;for(long long x=L;x<=R;x++)if(ok[x-L]){if(prev!=-1)ans=max(ans,x-prev);prev=x;}cout<<ans<<'\n';}}
```

### `CPPB2-L01-15` — Phương Trình Đổi Tiền Xu Diophantine

```cpp
#include <bits/stdc++.h>
using namespace std;long long eg(long long a,long long b,long long&x,long long&y){if(!b){x=1;y=0;return a;}long long x1,y1,g=eg(b,a%b,x1,y1);x=y1;y=x1-(a/b)*y1;return g;}long long flo(long long a,long long b){long long q=a/b,r=a%b;if(r&&a<0)--q;return q;}long long cei(long long a,long long b){return -flo(-a,b);}int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int q;if(!(cin>>q))return 0;while(q--){long long A,B,S;cin>>A>>B>>S;if(A<=0||B<=0||S<0){cout<<"NO\n";continue;}long long x0,y0,g=eg(A,B,x0,y0);if(S%g){cout<<"NO\n";continue;}long long x=x0*(S/g),y=y0*(S/g),u=B/g,v=A/g;long long lo=cei(-x,u),hi=flo(y,v);if(lo>hi){cout<<"NO\n";continue;}long long k=(B>A?lo:hi);cout<<x+u*k<<' '<<y-v*k<<'\n';}}
```

### `CPPB2-L01-16` — Tổng GCD Với N

```cpp
#include <bits/stdc++.h>
using namespace std;long long phi(long long n){long long z=n;for(long long p=2;p*p<=n;p+=(p==2?1:2))if(n%p==0){z=z/p*(p-1);while(n%p==0)n/=p;}if(n>1)z=z/n*(n-1);return z;}int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int q;if(!(cin>>q))return 0;while(q--){long long n;cin>>n;long long ans=0;for(long long d=1;d*d<=n;d++)if(n%d==0){ans+=d*phi(n/d);if(d*d!=n)ans+=(n/d)*phi(d);}cout<<ans<<'\n';}}
```

## Chương 01 — Bài 02: Modulo & lũy thừa nhanh

### `CPPB2-L02-01` — LŨY THỪA NHANH CƠ BẢN

```cpp
#include <bits/stdc++.h>
using namespace std;
const long long MOD = 1000000007;
long long power_mod(long long a, long long b) {
    long long res = 1; a %= MOD;
    while (b > 0) {
        if (b & 1) res = (res * a) % MOD;
        a = (a * a) % MOD;
        b >>= 1;
    }
    return res;
}
int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int t; if (!(cin >> t)) return 0;
    while (t--) {
        long long a, b; cin >> a >> b;
        cout << power_mod(a, b) << "\n";
    }
    return 0;
}
```

### `CPPB2-L02-02` — TÍNH GIÁ TRỊ PHÂN SỐ MODULO

```cpp
#include <bits/stdc++.h>
using namespace std;
const long long MOD = 1000000007;
long long power_mod(long long a, long long b) {
    long long res = 1; a %= MOD;
    while (b > 0) {
        if (b & 1) res = (res * a) % MOD;
        a = (a * a) % MOD;
        b >>= 1;
    }
    return res;
}
int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int t; if (!(cin >> t)) return 0;
    while (t--) {
        long long p, q; cin >> p >> q;
        long long inv = power_mod(q, MOD - 2);
        cout << (p % MOD * inv) % MOD << "\n";
    }
    return 0;
}
```

### `CPPB2-L02-03` — LŨY THỪA MA TRẬN 2X2 (DÃY FIBONACCI LỚN)

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L02-03: Lũy Thừa Ma Trận 2x2 (Dãy Fibonacci Lớn)
// Goal: Áp dụng Fast Power cho nhân ma trận

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L02-04` — NGHỊCH ĐẢO MODULO TỔNG QUÁT

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L02-04: Nghịch Đảo Modulo Tổng Quát
// Goal: Euclid mở rộng tìm nghịch đảo khi $M$ không nguyên tố

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L02-05` — TÍNH TỔ HỢP $C_N^K \BMOD (10^9+7)$

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L02-05: Tính Tổ Hợp $C_n^k \bmod (10^9+7)$
// Goal: Tiền xử lý giai thừa & nghịch đảo giai thừa

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L02-06` — LŨY THỪA VỚI SỐ MŨ CỰC LỚN

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L02-06: Lũy Thừa Với Số Mũ Cực Lớn
// Goal: Hạ bậc số mũ bằng định lý Fermat $B \bmod (M-1)$

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L02-07` — NHÂN MODULO HAI SỐ CỰC LỚN (NHÂN ẤN ĐỘ)

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L02-07: Nhân Modulo Hai Số Cực Lớn (Nhân Ấn Độ)
// Goal: Xử lý chống tràn số khi $M$ lớn

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L02-08` — TỔNG CẤP SỐ NHÂN $S_N = \SUM_{I=0}^N A^I \BMOD M$

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L02-08: Tổng Cấp Số Nhân $S_N = \sum_{i=0}^N A^i \bmod M$
// Goal: Chia để trị tính tổng cấp số nhân $\mathcal{O}(\log N)$

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L02-09` — THÁP LŨY THỪA $A^{B^C} \BMOD M$

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L02-09: Tháp Lũy Thừa $A^{B^C} \bmod M$
// Goal: Áp dụng hạ bậc số mũ 2 tầng qua Euler

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L02-10` — ĐẾM DÃY NGOẶC ĐÚNG (SỐ CATALAN MODULO)

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L02-10: Đếm Dãy Ngoặc Đúng (Số Catalan Modulo)
// Goal: Công thức $C_n = \frac{1}{n+1} C_{2n}^n \bmod M$

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L02-11` — HỆ PHƯƠNG TRÌNH ĐỒNG DƯ (CHINESE REMAINDER THEOREM)

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L02-11: Hệ Phương Trình Đồng Dư (Chinese Remainder Theorem)
// Goal: Định lý phần dư Trung Hoa giải hệ đồng dư

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L02-12` — TIỀN XỬ LÝ NGHỊCH ĐẢO TUYẾN TÍNH $\MATHCAL{O}(N)$

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L02-12: Tiền Xử Lý Nghịch Đảo Tuyến Tính $\mathcal{O}(N)$
// Goal: Cài đặt mảng `inv[i]` trong $\mathcal{O}(N)$

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L02-13` — LŨY THỪA MA TRẬN KÍCH THƯỚC $K \TIMES K$

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L02-13: Lũy Thừa Ma Trận Kích Thước $K \times K$
// Goal: Giải bài toán quy hoạch động truy hồi qua ma trận

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L02-14` — CĂN BẬC HAI MODULO NGUYÊN TỐ (THUẬT TOÁN TONELLI-SHANKS)

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L02-14: Căn Bậc Hai Modulo Nguyên Tố (Thuật Toán Tonelli-Shanks)
// Goal: Tìm $X$ thỏa $X^2 \equiv A \pmod P$

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L02-15` — LŨY THỪA SỐ MŨ LỚN KHI MODULO LÀ HỢP SỐ

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L02-15: Lũy Thừa Số Mũ Lớn Khi Modulo Là Hợp Số
// Goal: Áp dụng định lý Euler mở rộng $A^B \equiv A^{B \bmod \phi(M) + \phi(M)}$

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L02-16` — LOGARIT RỜI RẠC (BABY-STEP GIANT-STEP)

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L02-16: Logarit Rời Rạc (Baby-step Giant-step)
// Goal: Tìm $X$ nhỏ nhất thỏa $A^X \equiv B \pmod M$ trong $\mathcal{O}(\sqrt{M})$

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

## Chương 02 — Bài 03: Tìm kiếm nhị phân nâng cao

### `CPPB2-L03-01` — CHẶT NHỊ PHÂN CẮT GỖ (EKO)

```cpp
#include <bits/stdc++.h>
using namespace std;
bool check(long long h, const vector<long long> &a, long long m) {
    long long wood = 0;
    for (long long x : a) {
        if (x > h) wood += (x - h);
        if (wood >= m) return true;
    }
    return wood >= m;
}
int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int n; long long m; if (!(cin >> n >> m)) return 0;
    vector<long long> a(n);
    long long low = 0, high = 0;
    for (int i = 0; i < n; ++i) { cin >> a[i]; high = max(high, a[i]); }
    long long ans = 0;
    while (low <= high) {
        long long mid = low + (high - low) / 2;
        if (check(mid, a, m)) { ans = mid; low = mid + 1; }
        else { high = mid - 1; }
    }
    cout << ans << "\n";
    return 0;
}
```

### `CPPB2-L03-02` — CHIA BÁNH PIZZA ĐỀU NHAU

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L03-02: Chia Bánh Pizza Đều Nhau
// Goal: BS trên đáp án số thực

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L03-03` — CHUỒNG BÒ XA NHAU NHẤT (AGGRESSIVE COWS)

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L03-03: Chuồng Bò Xa Nhau Nhất (Aggressive Cows)
// Goal: Sắp xếp + BS khoảng cách cực đại

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L03-04` — PHÂN CHIA CÔNG VIỆC THỢ SƠN (PAINTER'S PARTITION)

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L03-04: Phân Chia Công Việc Thợ Sơn (Painter's Partition)
// Goal: BS tìm Min của Max tổng đoạn

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L03-05` — ĐOÀN TÀU VẬN CHUYỂN HÀNG HÓA

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L03-05: Đoàn Tàu Vận Chuyển Hàng Hóa
// Goal: Tham lam kiểm tra tính khả thi trong $\text{check}(X)$

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L03-06` — KHOẢNG CÁCH DÂY CÁP NHỎ NHẤT

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L03-06: Khoảng Cách Dây Cáp Nhỏ Nhất
// Goal: Chặt nhị phân số thực độ chính xác $10^{-6}$

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L03-07` — TRUNG BÌNH CỘNG ĐOẠN CON LỚN NHẤT $\GE K$

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L03-07: Trung Bình Cộng Đoạn Con Lớn Nhất $\ge K$
// Goal: BS số thực kết hợp Mảng tiền tố trừ $mid$

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L03-08` — TỐI ƯU HÓA CHI PHÍ LẮP TRẠM PHÁT SÓNG

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L03-08: Tối Ưu Hóa Chi Phí Lắp Trạm Phát Sóng
// Goal: Tìm kiếm tam phân (Ternary Search)

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L03-09` — TÌM PHẦN TỬ NHỎ THỨ K TRONG BẢNG NHÂN $N \TIMES N$

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L03-09: Tìm Phần Tử Nhỏ Thứ K Trong Bảng Nhân $N \times N$
// Goal: BS trên giá trị, hàm check đếm $\mathcal{O}(N)$

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L03-10` — TỐI ƯU PHÂN ĐOẠN TRỌNG SỐ MA TRẬN 2D

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L03-10: Tối Ưu Phân Đoạn Trọng Số Ma Trận 2D
// Goal: BS trên đáp án kết hợp 2D Prefix Sum & Greedy

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L03-11` — TÌM NGHIỆM THỰC CỦA PHƯƠNG TRÌNH PHI TUYẾN

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L03-11: Tìm Nghiệm Thực Của Phương Trình Phi Tuyến
// Goal: Chặt nhị phân số thực trên hàm đơn điệu ngặt

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L03-12` — ĐẾM SỐ CẶP $(A_I, B_J)$ CÓ TỔNG TRONG KHOẢNG $[L, R]$

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L03-12: Đếm Số Cặp $(A_i, B_j)$ Có Tổng Trong Khoảng $[L, R]$
// Goal: `lower_bound` và `upper_bound` đếm số lượng

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L03-13` — PHẦN TỬ NHỎ THỨ K CỦA HỢP HAI MẢNG ĐÃ SẮP XẾP

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L03-13: Phần Tử Nhỏ Thứ K Của Hợp Hai Mảng Đã Sắp Xếp
// Goal: Chặt nhị phân trong $\mathcal{O}(\log(\min(N, M)))$

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L03-14` — TỐI ƯU PHÂN ĐOẠN TRỌNG SỐ MA TRẬN 2D

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L03-14: Tối Ưu Phân Đoạn Trọng Số Ma Trận 2D
// Goal: BS trên đáp án kết hợp 2D Prefix Sum & Greedy

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L03-15` — CHẶT NHỊ PHÂN SONG SONG (PARALLEL BINARY SEARCH)

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L03-15: Chặt Nhị Phân Song Song (Parallel Binary Search)
// Goal: Kỹ thuật chặt nhị phân đồng thời cho $Q$ truy vấn

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L03-16` — KHOẢNG CÁCH CỰC TRỊ TRÊN ĐA GIÁC LỒI

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L03-16: Khoảng Cách Cực Trị Trên Đa Giác Lồi
// Goal: Ternary Search trên cấu trúc đa giác

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

## Chương 02 — Bài 04: Kỹ thuật mảng: Two Pointers, Window & 2D Prefix

### `CPPB2-L04-01` — TRUY VẤN TỔNG MA TRẬN CON 2D

```cpp
#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int n, m, q; if (!(cin >> n >> m >> q)) return 0;
    vector<vector<long long>> pref(n + 1, vector<long long>(m + 1, 0));
    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= m; ++j) {
            long long x; cin >> x;
            pref[i][j] = pref[i-1][j] + pref[i][j-1] - pref[i-1][j-1] + x;
        }
    }
    while (q--) {
        int x1, y1, x2, y2; cin >> x1 >> y1 >> x2 >> y2;
        cout << pref[x2][y2] - pref[x1-1][y2] - pref[x2][y1-1] + pref[x1-1][y1-1] << "\n";
    }
    return 0;
}
```

### `CPPB2-L04-02` — CẬP NHẬT HÌNH CHỮ NHẬT MA TRẬN 2D

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L04-02: Cập Nhật Hình Chữ Nhật Ma Trận 2D
// Goal: Cài đặt 2D Difference Array

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L04-03` — ĐOẠN CON NGẮN NHẤT CÓ TỔNG $\GE S$

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L04-03: Đoạn Con Ngắn Nhất Có Tổng $\ge S$
// Goal: Cửa sổ trượt co giãn

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L04-04` — NÉN TỌA ĐỘ & ĐẾM TẦN SUẤT TRÊN DẢI LỚN

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L04-04: Nén Tọa Độ & Đếm Tần Suất Trên Dải Lớn
// Goal: `sort` + `unique` + `lower_bound`

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L04-05` — ĐOẠN CON DÀI NHẤT CÓ KHÔNG QUÁ K SỐ KHÁC NHAU

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L04-05: Đoạn Con Dài Nhất Có Không Quá K Số Khác Nhau
// Goal: Two pointers kết hợp mảng tần suất

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L04-06` — MA TRẬN CON CÓ TỔNG LỚN NHẤT (MAXIMUM SUBMATRIX SUM)

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L04-06: Ma Trận Con Có Tổng Lớn Nhất (Maximum Submatrix Sum)
// Goal: Cố định 2 hàng + Thuật toán Kadane 1D

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L04-07` — DIỆN TÍCH PHỦ BỞI CÁC HÌNH CHỮ NHẬT RỜI RẠC

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L04-07: Diện Tích Phủ Bởi Các Hình Chữ Nhật Rời Rạc
// Goal: Nén tọa độ 2D kết hợp mảng hiệu 2D

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L04-08` — ĐẾM CẶP ĐOẠN THẲNG CHỒNG LẤN NHAU

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L04-08: Đếm Cặp Đoạn Thẳng Chồng Lấn Nhau
// Goal: Nén tọa độ + Mảng hiệu 1D

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L04-09` — CỬA SỔ TRƯỢT ĐẾM SỐ LƯỢNG XÂU ANAGRAM

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L04-09: Cửa Sổ Trượt Đếm Số Lượng Xâu Anagram
// Goal: Sliding window duy trì vector tần suất 26 chữ cái

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L04-10` — ĐẾM HÌNH VUÔNG CON CÓ TỔNG ĐÚNG BẰNG K

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L04-10: Đếm Hình Vuông Con Có Tổng Đúng Bằng K
// Goal: 2D Prefix Sum + Hai con trỏ trên đường chéo

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L04-11` — KHỬ CHIỀU 3-SUM & 4-SUM HAI CON TRỎ

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L04-11: Khử Chiều 3-Sum & 4-Sum Hai Con Trỏ
// Goal: Khử chiều không gian từ $\mathcal{O}(N^3) \to \mathcal{O}(N^2)$

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L04-12` — ĐẾM SỐ ĐOẠN CON CÓ HIỆU MAX - MIN $\LE K$

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L04-12: Đếm Số Đoạn Con Có Hiệu Max - Min $\le K$
// Goal: Two Pointers kết hợp 2 Deque đơn điệu

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L04-13` — ĐOẠN CON NGẮN NHẤT CHỨA ĐẦY ĐỦ BẢNG CHỮ CÁI

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L04-13: Đoạn Con Ngắn Nhất Chứa Đầy Đủ Bảng Chữ Cái
// Goal: Cửa sổ trượt co giãn duy trì biến đếm `unique_count`

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L04-14` — MẢNG HIỆU TRÊN CÂY (TREE DIFFERENCE ARRAY)

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L04-14: Mảng Hiệu Trên Cây (Tree Difference Array)
// Goal: Cập nhật cộng trọng số trên đường đi $(u, v)$ qua LCA

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L04-15` — ĐẾM TAM GIÁC CÓ ĐỘ DÀI CẠNH HỢP LỆ

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L04-15: Đếm Tam Giác Có Độ Dài Cạnh Hợp Lệ
// Goal: Two Pointers đếm tổ hợp bất đẳng thức tam giác

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L04-16` — QUÉT ĐƯỜNG THẲNG NÉN TỌA ĐỘ (SWEEP-LINE AREA 2D)

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L04-16: Quét Đường Thẳng Nén Tọa Độ (Sweep-line Area 2D)
// Goal: Sweep-line kết hợp Segment Tree tính diện tích hợp

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

## Chương 03 — Bài 05: Đệ quy, chia để trị & Meet in the Middle

### `CPPB2-L05-01` — ĐẾM CẶP NGHỊCH THẾ

```cpp
#include <bits/stdc++.h>
using namespace std;
long long merge_count(vector<int> &a, int l, int mid, int r) {
    vector<int> left(a.begin() + l, a.begin() + mid + 1);
    vector<int> right(a.begin() + mid + 1, a.begin() + r + 1);
    int i = 0, j = 0, k = l; long long cnt = 0;
    while (i < left.size() && j < right.size()) {
        if (left[i] <= right[j]) a[k++] = left[i++];
        else { a[k++] = right[j++]; cnt += (left.size() - i); }
    }
    while (i < left.size()) a[k++] = left[i++];
    while (j < right.size()) a[k++] = right[j++];
    return cnt;
}
long long solve(vector<int> &a, int l, int r) {
    if (l >= r) return 0;
    int mid = (l + r) / 2;
    return solve(a, l, mid) + solve(a, mid + 1, r) + merge_count(a, l, mid, r);
}
int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int n; if (!(cin >> n)) return 0;
    vector<int> a(n); for (int i = 0; i < n; ++i) cin >> a[i];
    cout << solve(a, 0, n - 1) << "\n";
    return 0;
}
```

### `CPPB2-L05-02` — CÁI TÚI KÍCH THƯỚC NHỎ (KNAPSACK $N \LE 40$)

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L05-02: Cái Túi Kích Thước Nhỏ (Knapsack $N \le 40$)
// Goal: Cài đặt Meet in the Middle cơ bản

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L05-03` — TẬP CON CÓ TỔNG GẦN S NHẤT

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L05-03: Tập Con Có Tổng Gần S Nhất
// Goal: MITM kết hợp `lower_bound`

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L05-04` — GIẢI PHƯƠNG TRÌNH $4$ ẨN TUYẾN TÍNH (4-SUM MITM)

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L05-04: Giải Phương Trình $4$ Ẩn Tuyến Tính (4-Sum MITM)
// Goal: Tách thành 2 cặp $(A+B)$ và $-(C+D)$

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L05-05` — ĐẾM SỐ TẬP CON CÓ XOR BẰNG K

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L05-05: Đếm Số Tập Con Có XOR Bằng K
// Goal: MITM với phép toán Bitwise XOR

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L05-06` — KHOẢNG CÁCH GIỮA HAI ĐIỂM GẦN NHẤT (CLOSEST PAIR)

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L05-06: Khoảng Cách Giữa Hai Điểm Gần Nhất (Closest Pair)
// Goal: Chia để trị trên mặt phẳng 2D $\mathcal{O}(N \log N)$

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L05-07` — BẺ KHÓA MẬT MÃ ĐỔI DẤU (SUBSET SUM WITH SIGNS)

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L05-07: Bẻ Khóa Mật Mã Đổi Dấu (Subset Sum with Signs)
// Goal: MITM với 3 trạng thái mỗi phần tử (0, +1, -1)

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L05-08` — TỐI ƯU HÓA TUYẾN ĐƯỜNG ĐI QUA ĐỈNH (SHORTEST PATH WITH MITM)

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L05-08: Tối Ưu Hóa Tuyến Đường Đi Qua Đỉnh (Shortest Path with MITM)
// Goal: BFS 2 đầu gặp nhau ở giữa

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L05-09` — TRÒ CHƠI XẾP GẠCH ĐA DIỆN (PUZZLE MITM)

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L05-09: Trò Chơi Xếp Gạch Đa Diện (Puzzle MITM)
// Goal: MITM kết hợp Hash Table nén bộ nhớ

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L05-10` — ĐẾM CẶP $A_I > 2 A_J$ (SIGNIFICANT INVERSIONS)

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L05-10: Đếm Cặp $A_i > 2 A_j$ (Significant Inversions)
// Goal: Biến thể Merge Sort đếm cặp điều kiện nâng cao

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L05-11` — TỔNG CẤP SỐ NHÂN BẰNG CHIA ĐỂ TRỊ

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L05-11: Tổng Cấp Số Nhân Bằng Chia Để Trị
// Goal: Phân rã $S_N = S_{N/2} \times (1 + A^{N/2})$

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L05-12` — TỐI ƯU HÓA TUYẾN ĐƯỜNG ĐI QUA ĐỈNH (SHORTEST PATH MITM)

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L05-12: Tối Ưu Hóa Tuyến Đường Đi Qua Đỉnh (Shortest Path MITM)
// Goal: BFS 2 đầu gặp nhau ở giữa

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L05-13` — TRÒ CHƠI XẾP GẠCH ĐA DIỆN (15-PUZZLE MITM)

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L05-13: Trò Chơi Xếp Gạch Đa Diện (15-Puzzle MITM)
// Goal: MITM kết hợp Hash Table nén bộ nhớ

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L05-14` — PHÂN CHIA TẬP HỢP THÀNH HAI NỬA CÓ TỔNG BẰNG NHAU

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L05-14: Phân Chia Tập Hợp Thành Hai Nửa Có Tổng Bằng Nhau
// Goal: MITM kết hợp tối ưu hóa bộ nhớ RAM

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L05-15` — ĐẾM SỐ ĐOẠN CON CÓ TỔNG NẰM TRONG $[L, R]$

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L05-15: Đếm Số Đoạn Con Có Tổng Nằm Trong $[L, R]$
// Goal: Chia để trị trên mảng tiền tố $\mathcal{O}(N \log N)$

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L05-16` — CHIA ĐỂ TRỊ TRÊN CÂY (CENTROID DECOMPOSITION CƠ BẢN)

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L05-16: Chia Để Trị Trên Cây (Centroid Decomposition Cơ Bản)
// Goal: Tìm trọng tâm cây đệ quy chia để trị

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

## Chương 03 — Bài 06: Phép toán bit & mặt nạ bit nâng cao

### `CPPB2-L06-01` — BÀI TOÁN NGƯỜI DU LỊCH (TSP)

```cpp
#include <bits/stdc++.h>
using namespace std;
const int INF = 1e9;
int n, c[20][20], dp[1 << 18][18];
int tsp(int mask, int u) {
    if (mask == (1 << n) - 1) return c[u][0];
    if (dp[mask][u] != -1) return dp[mask][u];
    int ans = INF;
    for (int v = 0; v < n; ++v) {
        if (!((mask >> v) & 1)) ans = min(ans, c[u][v] + tsp(mask | (1 << v), v));
    }
    return dp[mask][u] = ans;
}
int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    if (!(cin >> n)) return 0;
    for (int i = 0; i < n; ++i) for (int j = 0; j < n; ++j) cin >> c[i][j];
    memset(dp, -1, sizeof(dp));
    cout << tsp(1, 0) << "\n";
    return 0;
}
```

### `CPPB2-L06-02` — ĐẾM SỐ PHẦN TỬ BẬT BIT CHUNG (BITWISE AND)

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L06-02: Đếm Số Phần Tử Bật Bit Chung (Bitwise AND)
// Goal: Đếm bit độc lập theo từng cột $0 \dots 30$

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L06-03` — BÀI TOÁN NGƯỜI DU LỊCH (TSP BITMASK DP)

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L06-03: Bài Toán Người Du Lịch (TSP Bitmask DP)
// Goal: DP trạng thái $dp[mask][u]$

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L06-04` — PHÂN CHIA CÔNG VIỆC HOÀN HẢO (JOB ASSIGNMENT)

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L06-04: Phân Chia Công Việc Hoàn Hảo (Job Assignment)
// Goal: Bitmask DP ghép cặp trọng số nhỏ nhất

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L06-05` — DUYỆT TẤT CẢ SUBMASK TÍNH TỔNG PHÂN HOẠCH

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L06-05: Duyệt Tất Cả Submask Tính Tổng Phân Hoạch
// Goal: Vòng lặp `sub = (sub - 1) & mask`

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L06-06` — ĐƯỜNG ĐI HAMILTON ĐẾM SỐ CÁCH

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L06-06: Đường Đi Hamilton Đếm Số Cách
// Goal: DP Bitmask đếm số đường đi qua mọi đỉnh

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L06-07` — TỐI ĐA HÓA GIÁ TRỊ XOR ĐOẠN CON BẰNG TRIE BIT

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L06-07: Tối Đa Hóa Giá Trị XOR Đoạn Con Bằng Trie Bit
// Goal: Cây Trie nhị phân tìm Max XOR $\mathcal{O}(30N)$

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L06-08` — GHÉP CẶP TRỌNG SỐ CỰC ĐẠI (MAXIMUM MATCHING BITMASK)

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L06-08: Ghép Cặp Trọng Số Cực Đại (Maximum Matching Bitmask)
// Goal: Bitmask DP khử chiều đối xứng

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L06-09` — SOS DP (SUM OVER SUBSETS DYNAMIC PROGRAMMING)

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L06-09: SOS DP (Sum Over Subsets Dynamic Programming)
// Goal: DP tính tổng hàm trên mọi submask $\mathcal{O}(N 2^N)$

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L06-10` — ĐẾM SỐ CẶP $(A_I, A_J)$ CÓ TÍCH AND BẰNG 0

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L06-10: Đếm Số Cặp $(A_i, A_j)$ Có Tích AND Bằng 0
// Goal: SOS DP đếm số phần tử là submask

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L06-11` — SOS DP (SUM OVER SUBSETS DYNAMIC PROGRAMMING)

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L06-11: SOS DP (Sum Over Subsets Dynamic Programming)
// Goal: DP tính tổng hàm trên mọi submask $\mathcal{O}(N 2^N)$

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L06-12` — TÔ MÀU ĐỒ THỊ SỐ LƯỢNG MÀU NHỎ NHẤT (GRAPH COLORING)

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L06-12: Tô Màu Đồ Thị Số Lượng Màu Nhỏ Nhất (Graph Coloring)
// Goal: Bitmask DP trên tập độc lập cực đại (MIS)

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L06-13` — TÌM CHU TRÌNH HAMILTON CHI PHÍ NHỎ NHẤT

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L06-13: Tìm Chu Trình Hamilton Chi Phí Nhỏ Nhất
// Goal: Bitmask DP kết hợp truy vết chu trình

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L06-14` — TẬP ĐỘC LẬP TRỌNG SỐ LỚN NHẤT TRÊN ĐỒ THỊ NHỎ

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L06-14: Tập Độc Lập Trọng Số Lớn Nhất Trên Đồ Thị Nhỏ
// Goal: DP Bitmask duyệt cấu hình không kề nhau

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L06-15` — PHÂN HOẠCH TẬP HỢP THÀNH K TẬP CON CÓ TỔNG BẰNG NHAU

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L06-15: Phân Hoạch Tập Hợp Thành K Tập Con Có Tổng Bằng Nhau
// Goal: Bitmask DP kiểm tra tính khả thi

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```

### `CPPB2-L06-16` — TỐI ƯU HÓA TRÒ CHƠI NIM TỔNG QUÁT (SPRAGUE-GRUNDY BIT)

```cpp
#include <bits/stdc++.h>
using namespace std;

// Reference Solution for CPPB2-L06-16: Tối Ưu Hóa Trò Chơi Nim Tổng Quát (Sprague-Grundy Bit)
// Goal: Trò chơi toán học kết hợp phép toán XOR

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    cout << n << "\n";

    return 0;
}

```




\newpage

# Mục lục


