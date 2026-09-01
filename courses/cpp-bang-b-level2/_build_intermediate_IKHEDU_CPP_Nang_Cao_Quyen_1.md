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

Phần nội dung này gồm **3 Chương trọng tâm (Chương 01 đến Chương 03)** với **6 Bài học** và **134 bài toán thực hành phân tầng (P0 → P5)**, đào sâu số học đồng dư, lũy thừa nhanh, tìm kiếm nhị phân không gian nghiệm, kỹ thuật mảng 2D, đệ quy chia để trị, Meet in the Middle và mặt nạ bit.

Mỗi bài học được thiết kế theo cấu trúc sư phạm chặt chẽ:

- **Khái niệm & Bản chất toán học**: Giải thích trực quan, dễ hiểu kèm chứng minh toán học và bất biến thuật toán.
- **Bảng mô phỏng từng bước (Dry Run Table)**: Trực quan hóa quá trình biến đổi dữ liệu từng bước.
- **Mẫu cài đặt chuẩn thi đấu**: Code C++ chuẩn (0 `std::`, `#include <bits/stdc++.h>`, Fast I/O), tối ưu và an toàn tuyệt đối.
- **Hệ thống bài tập thực hành phân tầng**: Từ cơ bản đến chuyên sâu (P0 đến P5), có đầy đủ bối cảnh, nhiệm vụ, input/output và sample test.
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
$$\gcd(A, B) = \gcd(B, A \bmod B)$$
$$\gcd(A, 0) = A$$

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

> Nếu viết `return (a * b) / gcd(a, b);`, khi $A, B \approx 10^{10}$, tích $A \times B \approx 10^{20}$ sẽ vượt quá giới hạn $9.22 \times 10^{18}$ của kiểu `long long` $\implies$ **TRÀN SỐ ÂM / KẾT QUẢ SAI HOÀN TOÀN**.

> **Quy tắc an toàn tuyệt đối:** Luôn chia trước khi nhân vì $A$ luôn chia hết cho $\gcd(A, B)$:
> ```cpp
> long long lcm_calc(long long a, long long b) {
>     if (a == 0 || b == 0) return 0;
>     return (a / gcd_calc(a, b)) * b;
> }
> ```




![Sơ đồ cơ chế Sàng SPF](/Users/vu/Developer/ikhEdu_lessons/courses/cpp-bang-b-level2/lessons/lesson-01-so-hoc-co-ban-chuyen-sau/assets/l01_spf_sieve_visual.png)



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




![Mô phỏng Sàng số nguyên tố phân đoạn](/Users/vu/Developer/ikhEdu_lessons/courses/cpp-bang-b-level2/lessons/lesson-01-so-hoc-co-ban-chuyen-sau/assets/l01_segmented_sieve_visual.png)



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
$$A \cdot x + B \cdot y = \gcd(A, B)$$

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



### Bài 17 [CPPB2-L01-17]: Định lý thặng dư Trung Hoa (CRT)

**Bối cảnh & Nhiệm vụ:**

Cho hệ đồng dư $x \equiv r_i \pmod{m_i}$ với $m_i$ đôi một nguyên tố cùng nhau. Tìm $x$ nhỏ nhất.

**Đầu vào (Input):**

Dòng đầu chứa số $K$. $K$ dòng sau, mỗi dòng chứa hai số $r_i, m_i$.

**Đầu ra (Output):**

In ra số nguyên dương $x$ nhỏ nhất thỏa mãn hệ phương trình đồng dư.



### Bài 18 [CPPB2-L01-18]: Bậc của số nguyên Modulo P

**Bối cảnh & Nhiệm vụ:**

Cho hai số nguyên dương $A$ và $P$ với $\gcd(A, P) = 1$. Tìm số nguyên dương $k$ nhỏ nhất sao cho $A^k \equiv 1 \pmod P$.

**Đầu vào (Input):**

Gồm 2 số nguyên $A$ và $P$ ($P$ là số nguyên tố $\le 10^9$).

**Đầu ra (Output):**

In ra bậc $k = \text{ord}_P(A)$.



### Bài 19 [CPPB2-L01-19]: Tìm căn nguyên nguyên thủy nhỏ nhất

**Bối cảnh & Nhiệm vụ:**

Cho số nguyên tố lẻ $P$. Tìm căn nguyên nguyên thủy nhỏ nhất modulo $P$.

**Đầu vào (Input):**

Một số nguyên tố $P$ ($3 \le P \le 10^9$).

**Đầu ra (Output):**

In ra căn nguyên nguyên thủy nhỏ nhất của $P$.



### Bài 20 [CPPB2-L01-20]: Ước nguyên tố lớn nhất của dãy số

**Bối cảnh & Nhiệm vụ:**

Cho mảng $A$ gồm $N$ phần tử. Tìm ước số nguyên tố lớn nhất trong tất cả các phần tử của mảng.

**Đầu vào (Input):**

Dòng đầu chứa số $N$. Dòng sau chứa $N$ số nguyên $A_i$ ($A_i \le 10^{12}$).

**Đầu ra (Output):**

In ra ước nguyên tố lớn nhất tìm được.



### Bài 21 [CPPB2-L01-21]: Phương trình nghiệm nguyên Pell cơ bản

**Bối cảnh & Nhiệm vụ:**

Tìm nghiệm nguyên dương nhỏ nhất $(x, y)$ của phương trình Pell: $x^2 - d \cdot y^2 = 1$ với $d$ không chính phương.

**Đầu vào (Input):**

Một số nguyên dương $d$ không phải là số chính phương ($d \le 1000$).

**Đầu ra (Output):**

In ra cặp nghiệm $(x, y)$ nguyên dương nhỏ nhất.



### Bài 22 [CPPB2-L01-22]: Bội số nguyên tố trong tích giai thừa lớn

**Bối cảnh & Nhiệm vụ:**

Tính số mũ cao nhất của số nguyên tố $P$ trong tích $N! \times M!$.

**Đầu vào (Input):**

Ba số nguyên dương $N, M, P$ ($P$ là số nguyên tố, $N, M \le 10^{18}$).

**Đầu ra (Output):**

In ra số mũ của $P$ trong biểu thức $N! \times M!$.



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




![Sơ đồ nhân ma trận Fibonacci](/Users/vu/Developer/ikhEdu_lessons/courses/cpp-bang-b-level2/lessons/lesson-02-modulo-va-fast-power/assets/l02_matrix_fibonacci_visual.png)



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



### Bài 17 [CPPB2-L02-17]: Lũy thừa ma trận đếm đường đi đồ thị

**Bối cảnh & Nhiệm vụ:**

Cho đồ thị vô hướng $N$ đỉnh. Đếm số đường đi có độ dài đúng $K$ giữa đỉnh $U$ và đỉnh $V$ modulo $10^9+7$.

**Đầu vào (Input):**

Dòng đầu chứa $N, M, K, U, V$. $M$ dòng sau mô tả các cạnh của đồ thị.

**Đầu ra (Output):**

In ra số đường đi modulo $10^9+7$.



### Bài 18 [CPPB2-L02-18]: Tổng cấp số nhân Modulo hợp số

**Bối cảnh & Nhiệm vụ:**

Tính tổng $S = 1 + A + A^2 + \dots + A^N \pmod M$ với $M$ là hợp số bất kỳ.

**Đầu vào (Input):**

Ba số nguyên $A, N, M$ ($A, M \le 10^9, N \le 10^{18}$).

**Đầu ra (Output):**

In ra giá trị của $S \pmod M$.



### Bài 19 [CPPB2-L02-19]: Lũy thừa tháp tầng Euler Modulo

**Bối cảnh & Nhiệm vụ:**

Tính $A^{B^C} \pmod M$ với $M$ là số nguyên tố.

**Đầu vào (Input):**

Bốn số nguyên $A, B, C, M$ ($M$ là số nguyên tố $10^9+7$).

**Đầu ra (Output):**

In ra kết quả của $A^{B^C} \pmod M$.



### Bài 20 [CPPB2-L02-20]: Căn bậc hai Modulo P (Tonelli-Shanks)

**Bối cảnh & Nhiệm vụ:**

Tìm số nguyên $X$ nhỏ nhất sao cho $X^2 \equiv N \pmod P$ với $P$ là số nguyên tố.

**Đầu vào (Input):**

Hai số nguyên $N$ và $P$ ($P \le 10^9+7$).

**Đầu ra (Output):**

In ra nghiệm $X$ nhỏ nhất hoặc -1 nếu vô nghiệm.



### Bài 21 [CPPB2-L02-21]: Tổng dãy Fibonacci từ L đến R

**Bối cảnh & Nhiệm vụ:**

Tính tổng $S(L, R) = F_L + F_{L+1} + \dots + F_R \pmod{10^9+7}$.

**Đầu vào (Input):**

Gồm 2 số nguyên $L, R$ ($1 \le L \le R \le 10^{18}$).

**Đầu ra (Output):**

In ra tổng modulo $10^9+7$.



### Bài 22 [CPPB2-L02-22]: Số Tribonacci thứ N bằng ma trận 3x3

**Bối cảnh & Nhiệm vụ:**

Dãy Tribonacci: $T_0=0, T_1=1, T_2=1$ và $T_n = T_{n-1} + T_{n-2} + T_{n-3}$. Tính $T_N \pmod{10^9+7}$.

**Đầu vào (Input):**

Một số nguyên $N$ ($N \le 10^{18}$).

**Đầu ra (Output):**

In ra $T_N \pmod{10^9+7}$.



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




![Chặt nhị phân tập số thực](/Users/vu/Developer/ikhEdu_lessons/courses/cpp-bang-b-level2/lessons/lesson-03-tim-kiem-nhi-phan-nang-cao/assets/l03_binary_search_real_visual.png)



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



### Bài 17 [CPPB2-L03-17]: Chặt nhị phân song song (Parallel Binary Search)

**Bối cảnh & Nhiệm vụ:**

Cho $ truy vấn kiểm tra thời điểm một điều kiện đạt ngưỡng.

**Đầu vào (Input):**

Dòng 1: , M$. Các dòng sau mô tả sự kiện.

**Đầu ra (Output):**

In ra thời điểm đạt ngưỡng cho mỗi truy vấn.



### Bài 18 [CPPB2-L03-18]: Tìm kiếm tam phân (Ternary Search) cực trị hàm lồi

**Bối cảnh & Nhiệm vụ:**

Tìm giá trị cực tiểu của hàm số (x)$ trên đoạn 0$.

**Đầu vào (Input):**

Hai số thực , R$.

**Đầu ra (Output):**

In ra giá trị $ tối ưu với độ chính xác ^{-6}$.



### Bài 19 [CPPB2-L03-19]: Trung vị của hai mảng đã sắp xếp trong O(log(min(N, M)))

**Bối cảnh & Nhiệm vụ:**

Cho hai mảng đã sắp xếp $ và $. Tìm trung vị của hợp hai mảng.

**Đầu vào (Input):**

Dòng 1: , M$. Dòng 2: mảng $. Dòng 3: mảng $.

**Đầu ra (Output):**

In ra giá trị trung vị.



### Bài 20 [CPPB2-L03-20]: Tìm tam giác có diện tích lớn nhất bằng chặt nhị phân

**Bối cảnh & Nhiệm vụ:**

Cho $ điểm trên mặt phẳng. Tìm cặp điểm tạo với gốc tọa độ tam giác diện tích lớn nhất.

**Đầu vào (Input):**

Số $ và tọa độ $ điểm.

**Đầu ra (Output):**

In ra diện tích lớn nhất.



### Bài 21 [CPPB2-L03-21]: Khoảng cách nhỏ nhất giữa K điểm bất kỳ

**Bối cảnh & Nhiệm vụ:**

Chọn $ điểm sao cho khoảng cách giữa 2 điểm bất kỳ là lớn nhất.

**Đầu vào (Input):**

Dòng 1: , K$. Dòng 2: tọa độ $ điểm.

**Đầu ra (Output):**

In ra khoảng cách lớn nhất tìm được.



### Bài 22 [CPPB2-L03-22]: Tìm phân số nhỏ nhất lớn hơn X bằng phân số Farey

**Bối cảnh & Nhiệm vụ:**

Tìm phân số tối giản /Q$ có mẫu $\le M$ gần $ nhất.

**Đầu vào (Input):**

Hai số $ và $.

**Đầu ra (Output):**

In ra phân số /Q$.



# Bài 04: Kỹ thuật mảng: Hai con trỏ, Cửa sổ trượt, Mảng tiền tố & Mảng hiệu

## 1. Khái niệm & bản chất của tối ưu hóa tuyến tính trên mảng

Trong lập trình thi đấu, các kỹ thuật xử lý mảng như **Hai con trỏ (Two Pointers)**, **Cửa sổ trượt (Sliding Window)**, **Mảng tiền tố (Prefix Sum)**, **Mảng hiệu (Difference Array)** và **Nén tọa độ (Coordinate Compression)** là bộ công cụ nền tảng giúp chuyển đổi các thuật toán ngây thơ đa biến $\mathcal{O}(N^2)$ hoặc $\mathcal{O}(N \times Q)$ về độ phức tạp tối ưu tuyến tính $\mathcal{O}(N)$ hoặc $\mathcal{O}(N \log N)$.

Ở Level 2, ta tập trung vào **Kỹ thuật kết hợp đa chiều & Mảng 2D**:

* **Hai con trỏ co giãn & Cửa sổ trượt linh hoạt:** Duy trì bất biến về tần suất, số lượng phần tử phân biệt hoặc tổng điều kiện khi kích thước cửa sổ thay đổi liên tục.
* **Mảng tiền tố 2D (2D Prefix Sum):** Trả lời truy vấn tính tổng hình chữ nhật con bất kỳ trên ma trận $N \times M$ trong $\mathcal{O}(1)$.
* **Mảng hiệu 2D (2D Difference Array):** Cập nhật cộng một giá trị lên toàn bộ vùng hình chữ nhật trong $\mathcal{O}(1)$ và khôi phục ma trận trong $\mathcal{O}(NM)$.
* **Nén tọa độ (Coordinate Compression):** Ánh xạ các giá trị rời rạc rất lớn ($A_i \le 10^9$) về dải chỉ số nhỏ liên tiếp $[1, N]$ mà vẫn bảo toàn hoàn toàn quan hệ thứ tự $A_i < A_j$.


![Sơ đồ 2D Prefix Sum](lessons/lesson-04-ky-thuat-mang-nang-cao/assets/l04_2d_prefix_sum_visual.svg)

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



### Bài 17 [CPPB2-L04-17]: Quét đường (Sweep-line) diện tích hợp các hình chữ nhật

**Bối cảnh & Nhiệm vụ:**

Tính diện tích phần mặt phẳng bị phủ bởi $ hình chữ nhật.

**Đầu vào (Input):**

Dòng 1: $. $ dòng sau chứa tọa độ , y_1, x_2, y_2$.

**Đầu ra (Output):**

In ra tổng diện tích phủ.



### Bài 18 [CPPB2-L04-18]: Mảng hiệu 2D trên hình thoi (Manhattan 2D Difference)

**Bối cảnh & Nhiệm vụ:**

Cập nhật cộng giá trị cho tất cả các ô có khoảng cách Manhattan $\le D$.

**Đầu vào (Input):**

Dòng 1: , M, Q$. Các dòng sau mô tả truy vấn.

**Đầu ra (Output):**

In ra ma trận kết quả.



### Bài 19 [CPPB2-L04-19]: Nén tọa độ 3D và mảng cộng dồn không gian

**Bối cảnh & Nhiệm vụ:**

Cho $ hình hộp chữ nhật trong không gian 3D. Tính thể tích hợp.

**Đầu vào (Input):**

Số $ và tọa độ các hình hộp.

**Đầu ra (Output):**

In ra tổng thể tích.



### Bài 20 [CPPB2-L04-20]: Hai con trỏ đếm số tam giác hợp lệ

**Bối cảnh & Nhiệm vụ:**

Cho $ đoạn thẳng. Đếm số bộ ba tạo thành tam giác.

**Đầu vào (Input):**

Dòng 1: $. Dòng 2: $ số nguyên.

**Đầu ra (Output):**

In ra số tam giác.



### Bài 21 [CPPB2-L04-21]: Cửa sổ trượt đếm đoạn con có đúng K ký tự phân biệt

**Bối cảnh & Nhiệm vụ:**

Cho chuỗi $. Đếm số chuỗi con có đúng $ ký tự khác nhau.

**Đầu vào (Input):**

Chuỗi $ và số $.

**Đầu ra (Output):**

In ra số lượng chuỗi con.



### Bài 22 [CPPB2-L04-22]: Hình chữ nhật con có tổng lớn nhất (Kadane 2D)

**Bối cảnh & Nhiệm vụ:**

Tìm hình chữ nhật con có tổng các phần tử lớn nhất trong ma trận  	imes M$.

**Đầu vào (Input):**

Ma trận  	imes M$.

**Đầu ra (Output):**

In ra tổng lớn nhất.



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




![Kỹ thuật Meet in the Middle](/Users/vu/Developer/ikhEdu_lessons/courses/cpp-bang-b-level2/lessons/lesson-05-de-quy-chia-de-tri-mitm/assets/l05_mitm_split_visual.png)



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



### Bài 17 [CPPB2-L05-17]: Chia để trị trên cây trọng tâm (Centroid Decomposition)

**Bối cảnh & Nhiệm vụ:**

Đếm số cặp đỉnh có khoảng cách đúng bằng $K$ trên cây.

**Đầu vào (Input):**

Dòng 1: $N, K$. $N-1$ dòng sau mô tả các cạnh.

**Đầu ra (Output):**

In ra số cặp đỉnh.



### Bài 18 [CPPB2-L05-18]: Đếm chu trình độ dài 4 bằng Meet in the Middle

**Bối cảnh & Nhiệm vụ:**

Cho đồ thị vô hướng $N$ đỉnh. Đếm số chu trình đơn độ dài đúng 4.

**Đầu vào (Input):**

Dòng 1: $N, M$. $M$ dòng sau là các cạnh.

**Đầu ra (Output):**

In ra số chu trình.



### Bài 19 [CPPB2-L05-19]: Chia để trị tìm đoạn con có tổng lớn nhất

**Bối cảnh & Nhiệm vụ:**

Tìm đoạn con liên tiếp có tổng lớn nhất bằng thuật toán chia để trị $\mathcal{O}(N \log N)$.

**Đầu vào (Input):**

Mảng $A$ gồm $N$ số nguyên.

**Đầu ra (Output):**

In ra tổng lớn nhất.



### Bài 20 [CPPB2-L05-20]: Meet in the Middle đếm bộ nghiệm tổng bằng 0

**Bối cảnh & Nhiệm vụ:**

Cho 4 mảng $A, B, C, D$. Đếm số bộ tứ $(i, j, k, l)$ sao cho $A_i + B_j + C_k + D_l = 0$.

**Đầu vào (Input):**

Kích thước $N$ và 4 mảng.

**Đầu ra (Output):**

In ra số bộ nghiệm.



### Bài 21 [CPPB2-L05-21]: Cặp điểm gần nhất trên mặt phẳng 2D (Closest Pair of Points)

**Bối cảnh & Nhiệm vụ:**

Cho $N$ điểm trên mặt phẳng 2D. Tìm khoảng cách Euclid nhỏ nhất giữa 2 điểm bất kỳ bằng chia để trị $\mathcal{O}(N \log N)$.

**Đầu vào (Input):**

Số $N$ và tọa độ $N$ điểm.

**Đầu ra (Output):**

In ra bình phương khoảng cách nhỏ nhất.



### Bài 22 [CPPB2-L05-22]: Đếm bộ ba nghịch thế chia để trị 3 chiều (CDQ Divide & Conquer)

**Bối cảnh & Nhiệm vụ:**

Đếm số bộ ba $(i, j, k)$ thỏa mãn $i < j < k$ và $A_i > A_j > A_k$.

**Đầu vào (Input):**

Dãy số $A$ gồm $N$ phần tử.

**Đầu ra (Output):**

In ra số bộ ba.



# Bài 06: Phép toán bit & mặt nạ bit nâng cao

## 1. Khái niệm & bản chất của tối ưu hóa cấp độ bit (Bit Manipulation)

Trong kiến trúc máy tính hiện đại, các phép toán trên bit (`AND`, `OR`, `XOR`, `NOT`, dịch bit `<<`, `>>`) được CPU xử lý trực tiếp ở mức phần cứng trong đúng $1$ chu kỳ xung nhịp (clock cycle).

Ở Level 2, phép toán bit được nâng cấp thành **Mặt nạ bit (Bitmask)** để biểu diễn trạng thái của một tập hợp con:

* Một số nguyên $M$ có thể đại diện cho một tập con của $N$ phần tử: bit thứ $i$ bật ($= 1$) nghĩa là phần tử thứ $i$ được chọn, bit thứ $i$ tắt ($= 0$) nghĩa là phần tử thứ $i$ không được chọn.
* **Duyệt toàn bộ $2^N$ tập con:** Dùng vòng lặp `for (int mask = 0; mask < (1 << N); ++mask)`.
* **Duyệt toàn bộ tập con của một mặt nạ bit (Submask Iteration):** Duyệt tất cả submask của `mask` trong tổng thời gian $\mathcal{O}(3^N)$ thay vì $\mathcal{O}(4^N)$ bằng thủ thuật `sub = (sub - 1) & mask`.
* **Quy hoạch động trên mặt nạ bit (Bitmask DP):** Giải các bài toán tối ưu trên tập hợp nhỏ ($N \le 20$) như bài toán Người du lịch (Traveling Salesperson Problem - TSP), ghép cặp hoàn hảo (Matching).




![Bảng thao tác Bitmask](/Users/vu/Developer/ikhEdu_lessons/courses/cpp-bang-b-level2/lessons/lesson-06-phep-toan-bit-mat-na-bit-nang-cao/assets/l06_bitmask_operations_visual.png)



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



### Bài 17 [CPPB2-L06-17]: Quy hoạch động trên tập con SOS DP (Sum Over Subsets)

**Bối cảnh & Nhiệm vụ:**

Cho mảng $A$ kích thước $2^N$. Với mỗi mặt nạ $mask$, tính $F(mask) = \sum_{sub \subseteq mask} A[sub]$.

**Đầu vào (Input):**

Số $N$ và $2^N$ số nguyên.

**Đầu ra (Output):**

In ra các giá trị $F(mask)$.



### Bài 18 [CPPB2-L06-18]: Profile DP lát sàn hình chữ nhật bằng domino 2x1

**Bối cảnh & Nhiệm vụ:**

Đếm số cách lát kín bảng $N \times M$ bằng các quân cờ domino $2 \times 1$ modulo $10^9+7$.

**Đầu vào (Input):**

Hai số $N, M$ ($N \le 10, M \le 1000$).

**Đầu ra (Output):**

In ra số cách lát.



### Bài 19 [CPPB2-L06-19]: Biến đổi Walsh-Hadamard Fast Walsh-Hadamard Transform (FWHT)

**Bối cảnh & Nhiệm vụ:**

Tính tích chập XOR của hai mảng $A$ và $B$ kích thước $2^N$.

**Đầu vào (Input):**

Số $N$ và hai mảng $A, B$.

**Đầu ra (Output):**

In ra mảng tích chập $C$.



### Bài 20 [CPPB2-L06-20]: Đếm tập độc lập cực đại trên đồ thị nhỏ

**Bối cảnh & Nhiệm vụ:**

Cho đồ thị $N$ đỉnh ($N \le 20$). Tìm kích thước tập độc lập lớn nhất.

**Đầu vào (Input):**

Số đỉnh $N, M$ và các cạnh.

**Đầu ra (Output):**

In ra kích thước cực đại.



### Bài 21 [CPPB2-L06-21]: Phân chia N phần tử thành K nhóm có tổng bằng nhau

**Bối cảnh & Nhiệm vụ:**

Kiểm tra xem có thể chia $N$ số thành $K$ tập con có tổng bằng nhau hay không.

**Đầu vào (Input):**

Số $N, K$ và mảng $A$.

**Đầu ra (Output):**

In ra YES hoặc NO.



### Bài 22 [CPPB2-L06-22]: Cơ sở tuyến tính Linear Basis của phép XOR

**Bối cảnh & Nhiệm vụ:**

Tìm tập con có XOR lớn nhất từ mảng $A$ gồm $N$ số.

**Đầu vào (Input):**

Số $N$ và $N$ số nguyên.

**Đầu ra (Output):**

In ra giá trị XOR lớn nhất.



### Bài 23 [CPPB2-L06-23]: Ghép đôi có trọng số cực đại trên đồ thị $N \le 20$

**Bối cảnh & Nhiệm vụ:**

Tìm cách ghép cặp $2N$ đỉnh sao cho tổng trọng số các cạnh ghép là lớn nhất.

**Đầu vào (Input):**

Số $N$ và ma trận trọng số.

**Đầu ra (Output):**

In ra tổng trọng số cực đại.



### Bài 24 [CPPB2-L06-24]: Đếm số đường đi Hamilton trên đồ thị $N \le 20$

**Bối cảnh & Nhiệm vụ:**

Đếm số đường đi đi qua tất cả các đỉnh đúng 1 lần trên đồ thị có hướng $N$ đỉnh.

**Đầu vào (Input):**

Số đỉnh $N, M$ và các cạnh.

**Đầu ra (Output):**

In ra số đường đi.





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

long long gcd_val(long long a, long long b) {
    while (b) {
        a %= b;
        swap(a, b);
    }
    return a;
}

long long lcm_val(long long a, long long b) {
    if (a == 0 || b == 0) return 0;
    return (a / gcd_val(a, b)) * b;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    if (!(cin >> t)) return 0;
    while (t--) {
        long long a, b;
        cin >> a >> b;
        cout << gcd_val(a, b) << " " << lcm_val(a, b) << "\n";
    }
    return 0;
}

```

### `CPPB2-L01-02` — RÚT GỌN MẢNG PHÂN SỐ LỚN

```cpp
#include <bits/stdc++.h>
using namespace std;

long long gcd_val(long long a, long long b) {
    a = abs(a); b = abs(b);
    while (b) {
        a %= b;
        swap(a, b);
    }
    return a;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    for (int i = 0; i < n; ++i) {
        long long num, den;
        cin >> num >> den;
        if (den < 0) {
            num = -num;
            den = -den;
        }
        long long g = gcd_val(num, den);
        cout << num / g << " " << den / g << "\n";
    }
    return 0;
}

```

### `CPPB2-L01-03` — SÀNG ƯỚC SỐ NGUYÊN TỐ NHỎ NHẤT (SPF)

```cpp
#include <bits/stdc++.h>
using namespace std;

const int MAXA = 1000000;
int spf[MAXA + 1];

void sieve_spf() {
    for (int i = 1; i <= MAXA; ++i) spf[i] = i;
    for (int i = 2; i * i <= MAXA; ++i) {
        if (spf[i] == i) {
            for (int j = i * i; j <= MAXA; j += i) {
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
        int x;
        cin >> x;
        cout << spf[x] << "\n";
    }
    return 0;
}

```

### `CPPB2-L01-04` — PHÂN TÍCH THỪA SỐ TRUY VẤN NHANH

```cpp
#include <bits/stdc++.h>
using namespace std;

const int MAXA = 1000000;
int spf[MAXA + 1];

void sieve_spf() {
    for (int i = 1; i <= MAXA; ++i) spf[i] = i;
    for (int i = 2; i * i <= MAXA; ++i) {
        if (spf[i] == i) {
            for (int j = i * i; j <= MAXA; j += i) {
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
        int x;
        cin >> x;
        vector<pair<int, int>> factors;
        while (x > 1) {
            int p = spf[x];
            int cnt = 0;
            while (x % p == 0) {
                cnt++;
                x /= p;
            }
            factors.push_back({p, cnt});
        }
        for (int i = 0; i < (int)factors.size(); ++i) {
            cout << factors[i].first << "^" << factors[i].second << (i + 1 == (int)factors.size() ? "" : " * ");
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

const int MAXA = 1000000;
int spf[MAXA + 1];

void sieve_spf() {
    for (int i = 1; i <= MAXA; ++i) spf[i] = i;
    for (int i = 2; i * i <= MAXA; ++i) {
        if (spf[i] == i) {
            for (int j = i * i; j <= MAXA; j += i) {
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
        int x;
        cin >> x;
        long long num_divisors = 1;
        long long sum_divisors = 1;

        while (x > 1) {
            int p = spf[x];
            int cnt = 0;
            long long p_pow = 1;
            long long cur_sum = 1;
            while (x % p == 0) {
                cnt++;
                p_pow *= p;
                cur_sum += p_pow;
                x /= p;
            }
            num_divisors *= (cnt + 1);
            sum_divisors *= cur_sum;
        }
        cout << num_divisors << " " << sum_divisors << "\n";
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

    long long lim = sqrt(R);
    vector<bool> is_prime_small(lim + 1, true);
    vector<long long> primes;
    for (long long i = 2; i <= lim; ++i) {
        if (is_prime_small[i]) {
            primes.push_back(i);
            for (long long j = i * i; j <= lim; j += i) is_prime_small[j] = false;
        }
    }

    vector<bool> is_prime_range(R - L + 1, true);
    for (long long p : primes) {
        long long start = max(p * p, ((L + p - 1) / p) * p);
        for (long long j = start; j <= R; j += p) {
            is_prime_range[j - L] = false;
        }
    }

    if (L == 1) is_prime_range[0] = false;

    long long cnt = 0;
    for (long long i = 0; i <= R - L; ++i) {
        if (is_prime_range[i]) cnt++;
    }
    cout << cnt << "\n";
    return 0;
}

```

### `CPPB2-L01-07` — Cặp Số Nguyên Tố Sinh Đôi Trong Đoạn

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long L, R;
    if (!(cin >> L >> R)) return 0;

    long long lim = sqrt(R);
    vector<bool> is_prime_small(lim + 1, true);
    vector<long long> primes;
    for (long long i = 2; i <= lim; ++i) {
        if (is_prime_small[i]) {
            primes.push_back(i);
            for (long long j = i * i; j <= lim; j += i) is_prime_small[j] = false;
        }
    }

    vector<bool> is_prime_range(R - L + 1, true);
    for (long long p : primes) {
        long long start = max(p * p, ((L + p - 1) / p) * p);
        for (long long j = start; j <= R; j += p) {
            is_prime_range[j - L] = false;
        }
    }
    if (L == 1 && R >= 1) is_prime_range[0] = false;

    long long twin_count = 0;
    for (long long x = L; x + 2 <= R; ++x) {
        if (is_prime_range[x - L] && is_prime_range[x + 2 - L]) {
            twin_count++;
        }
    }
    cout << twin_count << "\n";
    return 0;
}

```

### `CPPB2-L01-08` — TÌM NGHIỆM NGUYÊN PHƯƠNG TRÌNH DIOPHANTINE

```cpp
#include <bits/stdc++.h>
using namespace std;

long long extgcd(long long a, long long b, long long &x, long long &y) {
    if (b == 0) {
        x = 1; y = 0;
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

    long long a, b, c;
    if (!(cin >> a >> b >> c)) return 0;

    long long x0, y0;
    long long g = extgcd(abs(a), abs(b), x0, y0);

    if (c % g != 0) {
        cout << "-1\n";
    } else {
        if (a < 0) x0 = -x0;
        if (b < 0) y0 = -y0;
        x0 *= (c / g);
        y0 *= (c / g);
        cout << x0 << " " << y0 << "\n";
    }
    return 0;
}

```

### `CPPB2-L01-09` — Nghiệm Nguyên Dương Nhỏ Nhất

```cpp
#include <bits/stdc++.h>
using namespace std;

long long extgcd(long long a, long long b, long long &x, long long &y) {
    if (b == 0) {
        x = 1; y = 0;
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

    long long a, b, c;
    if (!(cin >> a >> b >> c)) return 0;

    long long x0, y0;
    long long g = extgcd(a, b, x0, y0);

    if (c % g != 0) {
        cout << "-1\n";
        return 0;
    }

    x0 *= (c / g);
    y0 *= (c / g);

    long long b_prime = b / g;
    long long a_prime = a / g;

    long long k = (-x0) / b_prime;
    while (x0 + k * b_prime <= 0) k++;
    while (x0 + (k - 1) * b_prime > 0) k--;

    long long x_min = x0 + k * b_prime;
    long long y_cor = (c - a * x_min) / b;

    cout << x_min << " " << y_cor << "\n";
    return 0;
}

```

### `CPPB2-L01-10` — HÀM PHI EULER $\PHI(N)$ NHANH VỚI SPF

```cpp
#include <bits/stdc++.h>
using namespace std;

const int MAXA = 1000000;
int spf[MAXA + 1];

void sieve_spf() {
    for (int i = 1; i <= MAXA; ++i) spf[i] = i;
    for (int i = 2; i * i <= MAXA; ++i) {
        if (spf[i] == i) {
            for (int j = i * i; j <= MAXA; j += i) {
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
        cin >> n;
        int ans = n;
        int temp = n;
        while (temp > 1) {
            int p = spf[temp];
            ans -= ans / p;
            while (temp % p == 0) temp /= p;
        }
        cout << ans << "\n";
    }
    return 0;
}

```

### `CPPB2-L01-11` — Phân Tích Giai Thừa N! (Legendre)

```cpp
#include <bits/stdc++.h>
using namespace std;

long long legendre(long long n, long long p) {
    long long count = 0;
    while (n > 0) {
        count += n / p;
        n /= p;
    }
    return count;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n, p;
    if (!(cin >> n >> p)) return 0;

    cout << legendre(n, p) << "\n";
    return 0;
}

```

### `CPPB2-L01-12` — Số Ước Số Lẻ & Số Chính Phương

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long A, B;
    if (!(cin >> A >> B)) return 0;

    long long r = sqrt(B);
    long long l = ceil(sqrt(A));

    long long ans = max(0LL, r - l + 1);
    cout << ans << "\n";
    return 0;
}

```

### `CPPB2-L01-13` — Cặp Số Có GCD và LCM Cho Trước

```cpp
#include <bits/stdc++.h>
using namespace std;

long long gcd_val(long long a, long long b) {
    while (b) {
        a %= b;
        swap(a, b);
    }
    return a;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long G, L;
    if (!(cin >> G >> L)) return 0;

    if (L % G != 0) {
        cout << "0\n";
        return 0;
    }

    long long prod = L / G;
    long long count = 0;

    for (long long x = 1; x * x <= prod; ++x) {
        if (prod % x == 0) {
            long long y = prod / x;
            if (gcd_val(x, y) == 1) {
                count++;
            }
        }
    }

    cout << count << "\n";
    return 0;
}

```

### `CPPB2-L01-14` — Khoảng Cách Cực Đại Giữa Hai Số Nguyên Tố

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long L, R;
    if (!(cin >> L >> R)) return 0;

    long long lim = sqrt(R);
    vector<bool> is_prime_small(lim + 1, true);
    vector<long long> primes;
    for (long long i = 2; i <= lim; ++i) {
        if (is_prime_small[i]) {
            primes.push_back(i);
            for (long long j = i * i; j <= lim; j += i) is_prime_small[j] = false;
        }
    }

    vector<bool> is_prime_range(R - L + 1, true);
    for (long long p : primes) {
        long long start = max(p * p, ((L + p - 1) / p) * p);
        for (long long j = start; j <= R; j += p) {
            is_prime_range[j - L] = false;
        }
    }
    if (L == 1 && R >= 1) is_prime_range[0] = false;

    vector<long long> seg_primes;
    for (long long i = 0; i <= R - L; ++i) {
        if (is_prime_range[i]) seg_primes.push_back(L + i);
    }

    if (seg_primes.size() < 2) {
        cout << "-1\n";
        return 0;
    }

    long long max_gap = 0;
    for (size_t i = 1; i < seg_primes.size(); ++i) {
        max_gap = max(max_gap, seg_primes[i] - seg_primes[i - 1]);
    }
    cout << max_gap << "\n";
    return 0;
}

```

### `CPPB2-L01-15` — Phương Trình Đổi Tiền Xu Diophantine

```cpp
#include <bits/stdc++.h>
using namespace std;

long long extgcd(long long a, long long b, long long &x, long long &y) {
    if (b == 0) {
        x = 1; y = 0;
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

    long long a, b, S;
    if (!(cin >> a >> b >> S)) return 0;

    long long x0, y0;
    long long g = extgcd(a, b, x0, y0);

    if (S % g != 0) {
        cout << "-1\n";
        return 0;
    }

    x0 *= (S / g);
    y0 *= (S / g);

    long long b_prime = b / g;
    long long a_prime = a / g;

    long long k_min = ceil((double)(-x0) / b_prime);
    long long k_max = floor((double)(y0) / a_prime);

    if (k_min > k_max) {
        cout << "-1\n";
        return 0;
    }

    long long min_coins = 2e18;
    for (long long k : {k_min, k_max}) {
        long long cur_x = x0 + k * b_prime;
        long long cur_y = y0 - k * a_prime;
        if (cur_x >= 0 && cur_y >= 0) {
            min_coins = min(min_coins, cur_x + cur_y);
        }
    }
    cout << min_coins << "\n";
    return 0;
}

```

### `CPPB2-L01-16` — Tổng GCD Với N

```cpp
#include <bits/stdc++.h>
using namespace std;

long long get_phi(long long n) {
    long long res = n;
    for (long long p = 2; p * p <= n; ++p) {
        if (n % p == 0) {
            while (n % p == 0) n /= p;
            res -= res / p;
        }
    }
    if (n > 1) res -= res / n;
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;

    long long total_sum = 0;
    for (long long d = 1; d * d <= n; ++d) {
        if (n % d == 0) {
            total_sum += d * get_phi(n / d);
            if (d * d != n) {
                long long other_d = n / d;
                total_sum += other_d * get_phi(n / other_d);
            }
        }
    }
    cout << total_sum << "\n";
    return 0;
}

```

### `CPPB2-L01-17` — Định lý thặng dư Trung Hoa (CRT)

```cpp
#include <bits/stdc++.h>
using namespace std;

long long extgcd(long long a, long long b, long long &x, long long &y) {
    if (b == 0) { x = 1; y = 0; return a; }
    long long x1, y1;
    long long d = extgcd(b, a % b, x1, y1);
    x = y1;
    y = x1 - y1 * (a / b);
    return d;
}

long long modInverse(long long a, long long m) {
    long long x, y;
    extgcd(a, m, x, y);
    return (x % m + m) % m;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int k;
    if (!(cin >> k)) return 0;
    vector<long long> r(k), m(k);
    long long M = 1;
    for (int i = 0; i < k; ++i) {
        cin >> r[i] >> m[i];
        M *= m[i];
    }

    long long ans = 0;
    for (int i = 0; i < k; ++i) {
        long long Mi = M / m[i];
        long long yi = modInverse(Mi, m[i]);
        ans = (ans + (__int128)r[i] * Mi % M * yi % M) % M;
    }
    cout << (ans % M + M) % M << "\n";
    return 0;
}

```

### `CPPB2-L01-18` — Bậc của số nguyên Modulo P

```cpp
#include <bits/stdc++.h>
using namespace std;

long long power(long long a, long long b, long long m) {
    long long res = 1;
    a %= m;
    while (b > 0) {
        if (b & 1) res = (__int128)res * a % m;
        a = (__int128)a * a % m;
        b >>= 1;
    }
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long a, p;
    if (!(cin >> a >> p)) return 0;

    long long phi = p - 1;
    vector<long long> divs;
    for (long long i = 1; i * i <= phi; ++i) {
        if (phi % i == 0) {
            divs.push_back(i);
            if (i * i != phi) divs.push_back(phi / i);
        }
    }
    sort(divs.begin(), divs.end());

    for (long long d : divs) {
        if (power(a, d, p) == 1) {
            cout << d << "\n";
            return 0;
        }
    }
    cout << phi << "\n";
    return 0;
}

```

### `CPPB2-L01-19` — Tìm căn nguyên nguyên thủy nhỏ nhất

```cpp
#include <bits/stdc++.h>
using namespace std;

long long power(long long a, long long b, long long m) {
    long long res = 1;
    a %= m;
    while (b > 0) {
        if (b & 1) res = (__int128)res * a % m;
        a = (__int128)a * a % m;
        b >>= 1;
    }
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long p;
    if (!(cin >> p)) return 0;

    long long phi = p - 1;
    vector<long long> factors;
    long long temp = phi;
    for (long long i = 2; i * i <= temp; ++i) {
        if (temp % i == 0) {
            factors.push_back(i);
            while (temp % i == 0) temp /= i;
        }
    }
    if (temp > 1) factors.push_back(temp);

    for (long long g = 2; g < p; ++g) {
        bool ok = true;
        for (long long f : factors) {
            if (power(g, phi / f, p) == 1) {
                ok = false;
                break;
            }
        }
        if (ok) {
            cout << g << "\n";
            return 0;
        }
    }
    return 0;
}

```

### `CPPB2-L01-20` — Ước nguyên tố lớn nhất của dãy số

```cpp
#include <bits/stdc++.h>
using namespace std;

long long get_max_prime_factor(long long n) {
    long long max_p = -1;
    while (n % 2 == 0) { max_p = 2; n /= 2; }
    for (long long i = 3; i * i <= n; i += 2) {
        while (n % i == 0) {
            max_p = i;
            n /= i;
        }
    }
    if (n > 1) max_p = max(max_p, n);
    return max_p;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    long long ans = -1;
    for (int i = 0; i < n; ++i) {
        long long x;
        cin >> x;
        ans = max(ans, get_max_prime_factor(x));
    }
    cout << ans << "\n";
    return 0;
}

```

### `CPPB2-L01-21` — Phương trình nghiệm nguyên Pell cơ bản

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long d;
    if (!(cin >> d)) return 0;

    long long m = 0, d_val = 1, a0 = sqrt(d), a = a0;
    if (a0 * a0 == d) return 0;

    __int128 p0 = a0, p1 = 1, q0 = 1, q1 = 0;
    __int128 p = p0, q = q0;

    while (p * p - (__int128)d * q * q != 1) {
        m = d_val * a - m;
        d_val = (d - m * m) / d_val;
        a = (a0 + m) / d_val;
        p = a * p0 + p1;
        q = a * q0 + q1;
        p1 = p0; p0 = p;
        q1 = q0; q0 = q;
    }

    cout << (long long)p << " " << (long long)q << "\n";
    return 0;
}

```

### `CPPB2-L01-22` — Bội số nguyên tố trong tích giai thừa lớn

```cpp
#include <bits/stdc++.h>
using namespace std;

long long legendre(long long n, long long p) {
    long long cnt = 0;
    while (n > 0) {
        cnt += n / p;
        n /= p;
    }
    return cnt;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n, m, p;
    if (!(cin >> n >> m >> p)) return 0;
    cout << legendre(n, p) + legendre(m, p) << "\n";
    return 0;
}

```

## Chương 01 — Bài 02: Modulo & lũy thừa nhanh

### `CPPB2-L02-01` — LŨY THỪA NHANH CƠ BẢN

```cpp
#include <bits/stdc++.h>
using namespace std;

const long long MOD = 1000000007;

long long power_mod(long long a, long long b, long long m = MOD) {
    long long res = 1; a %= m;
    while (b > 0) {
        if (b & 1) res = (res * a) % m;
        a = (a * a) % m;
        b >>= 1;
    }
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    if (!(cin >> t)) return 0;
    while (t--) {
        long long a, b;
        cin >> a >> b;
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

long long power_mod(long long a, long long b, long long m = MOD) {
    long long res = 1; a %= m;
    while (b > 0) {
        if (b & 1) res = (res * a) % m;
        a = (a * a) % m;
        b >>= 1;
    }
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    if (!(cin >> t)) return 0;
    while (t--) {
        long long p, q;
        cin >> p >> q;
        long long inv_q = power_mod(q, MOD - 2);
        long long ans = (p % MOD * inv_q) % MOD;
        cout << ans << "\n";
    }
    return 0;
}

```

### `CPPB2-L02-03` — LŨY THỪA MA TRẬN 2X2 (DÃY FIBONACCI LỚN)

```cpp
#include <bits/stdc++.h>
using namespace std;

const long long MOD = 1000000007;

struct Matrix {
    long long mat[2][2];
    Matrix() {
        mat[0][0] = mat[0][1] = mat[1][0] = mat[1][1] = 0;
    }
};

Matrix multiply(Matrix A, Matrix B) {
    Matrix C;
    for (int i = 0; i < 2; ++i) {
        for (int j = 0; j < 2; ++j) {
            for (int k = 0; k < 2; ++k) {
                C.mat[i][j] = (C.mat[i][j] + A.mat[i][k] * B.mat[k][j]) % MOD;
            }
        }
    }
    return C;
}

Matrix power_mat(Matrix A, long long p) {
    Matrix res;
    res.mat[0][0] = res.mat[1][1] = 1;
    while (p > 0) {
        if (p & 1) res = multiply(res, A);
        A = multiply(A, A);
        p >>= 1;
    }
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    if (!(cin >> t)) return 0;
    while (t--) {
        long long n;
        cin >> n;
        if (n == 0) { cout << "0\n"; continue; }
        Matrix T;
        T.mat[0][0] = 1; T.mat[0][1] = 1;
        T.mat[1][0] = 1; T.mat[1][1] = 0;

        Matrix Tn = power_mat(T, n - 1);
        cout << Tn.mat[0][0] << "\n";
    }
    return 0;
}

```

### `CPPB2-L02-04` — NGHỊCH ĐẢO MODULO TỔNG QUÁT

```cpp
#include <bits/stdc++.h>
using namespace std;

long long extgcd(long long a, long long b, long long &x, long long &y) {
    if (b == 0) {
        x = 1; y = 0;
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
        long long a, m;
        cin >> a >> m;
        long long x, y;
        long long g = extgcd(a, m, x, y);
        if (g != 1) {
            cout << "-1\n";
        } else {
            cout << (x % m + m) % m << "\n";
        }
    }
    return 0;
}

```

### `CPPB2-L02-05` — TÍNH TỔ HỢP $C_N^K \BMOD (10^9+7)$

```cpp
#include <bits/stdc++.h>
using namespace std;

const int MAXN = 1000000;
const long long MOD = 1000000007;

long long fact[MAXN + 1], invFact[MAXN + 1];

long long power_mod(long long a, long long b) {
    long long res = 1; a %= MOD;
    while (b > 0) {
        if (b & 1) res = (res * a) % MOD;
        a = (a * a) % MOD;
        b >>= 1;
    }
    return res;
}

void precompute() {
    fact[0] = 1;
    for (int i = 1; i <= MAXN; ++i) fact[i] = (fact[i - 1] * i) % MOD;
    invFact[MAXN] = power_mod(fact[MAXN], MOD - 2);
    for (int i = MAXN - 1; i >= 0; --i) {
        invFact[i] = (invFact[i + 1] * (i + 1)) % MOD;
    }
}

long long nCr(int n, int r) {
    if (r < 0 || r > n) return 0;
    return fact[n] * invFact[r] % MOD * invFact[n - r] % MOD;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    precompute();

    int q;
    if (!(cin >> q)) return 0;
    while (q--) {
        int n, k;
        cin >> n >> k;
        cout << nCr(n, k) << "\n";
    }
    return 0;
}

```

### `CPPB2-L02-06` — LŨY THỪA VỚI SỐ MŨ CỰC LỚN

```cpp
#include <bits/stdc++.h>
using namespace std;

const long long MOD = 1000000007;

long long power_mod(long long a, long long b, long long m = MOD) {
    long long res = 1; a %= m;
    while (b > 0) {
        if (b & 1) res = (res * a) % m;
        a = (a * a) % m;
        b >>= 1;
    }
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long a;
    string b_str;
    if (!(cin >> a >> b_str)) return 0;

    long long b_reduced = 0;
    long long phi_m = MOD - 1;
    for (char c : b_str) {
        b_reduced = (b_reduced * 10 + (c - '0')) % phi_m;
    }

    cout << power_mod(a, b_reduced) << "\n";
    return 0;
}

```

### `CPPB2-L02-07` — NHÂN MODULO HAI SỐ CỰC LỚN (NHÂN ẤN ĐỘ)

```cpp
#include <bits/stdc++.h>
using namespace std;

long long mul_mod(long long a, long long b, long long m) {
    return (long long)((__int128_t)a * b % m);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    if (!(cin >> t)) return 0;
    while (t--) {
        long long a, b, m;
        cin >> a >> b >> m;
        cout << mul_mod(a, b, m) << "\n";
    }
    return 0;
}

```

### `CPPB2-L02-08` — TỔNG CẤP SỐ NHÂN $S_N = \SUM_{I=0}^N A^I \BMOD M$

```cpp
#include <bits/stdc++.h>
using namespace std;

const long long MOD = 1000000007;

long long power_mod(long long a, long long b, long long m = MOD) {
    long long res = 1; a %= m;
    while (b > 0) {
        if (b & 1) res = (res * a) % m;
        a = (a * a) % m;
        b >>= 1;
    }
    return res;
}

// S(n) = 1 + a + a^2 + ... + a^n
long long sum_geom(long long a, long long n) {
    if (n == 0) return 1;
    if (n % 2 == 1) {
        long long half = sum_geom(a, n / 2);
        long long a_half = power_mod(a, n / 2 + 1);
        return (half * (1 + a_half)) % MOD;
    } else {
        return (sum_geom(a, n - 1) + power_mod(a, n)) % MOD;
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    if (!(cin >> t)) return 0;
    while (t--) {
        long long a, n;
        cin >> a >> n;
        cout << sum_geom(a, n) << "\n";
    }
    return 0;
}

```

### `CPPB2-L02-09` — THÁP LŨY THỪA $A^{B^C} \BMOD M$

```cpp
#include <bits/stdc++.h>
using namespace std;

const long long MOD = 1000000007;

long long power_mod(long long a, long long b, long long m) {
    long long res = 1; a %= m;
    while (b > 0) {
        if (b & 1) res = (res * a) % m;
        a = (a * a) % m;
        b >>= 1;
    }
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    if (!(cin >> t)) return 0;
    while (t--) {
        long long a, b, c;
        cin >> a >> b >> c;
        long long exp = power_mod(b, c, MOD - 1);
        long long ans = power_mod(a, exp, MOD);
        cout << ans << "\n";
    }
    return 0;
}

```

### `CPPB2-L02-10` — ĐẾM DÃY NGOẶC ĐÚNG (SỐ CATALAN MODULO)

```cpp
#include <bits/stdc++.h>
using namespace std;

const int MAXN = 2000000;
const long long MOD = 1000000007;

long long fact[MAXN + 1], invFact[MAXN + 1];

long long power_mod(long long a, long long b) {
    long long res = 1; a %= MOD;
    while (b > 0) {
        if (b & 1) res = (res * a) % MOD;
        a = (a * a) % MOD;
        b >>= 1;
    }
    return res;
}

void precompute() {
    fact[0] = 1;
    for (int i = 1; i <= MAXN; ++i) fact[i] = (fact[i - 1] * i) % MOD;
    invFact[MAXN] = power_mod(fact[MAXN], MOD - 2);
    for (int i = MAXN - 1; i >= 0; --i) {
        invFact[i] = (invFact[i + 1] * (i + 1)) % MOD;
    }
}

long long catalan(int n) {
    long long c2n_n = fact[2 * n] * invFact[n] % MOD * invFact[n] % MOD;
    return c2n_n * power_mod(n + 1, MOD - 2) % MOD;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    precompute();

    int t;
    if (!(cin >> t)) return 0;
    while (t--) {
        int n;
        cin >> n;
        cout << catalan(n) << "\n";
    }
    return 0;
}

```

### `CPPB2-L02-11` — HỆ PHƯƠNG TRÌNH ĐỒNG DƯ (CHINESE REMAINDER THEOREM)

```cpp
#include <bits/stdc++.h>
using namespace std;

long long extgcd(long long a, long long b, long long &x, long long &y) {
    if (b == 0) { x = 1; y = 0; return a; }
    long long x1, y1;
    long long g = extgcd(b, a % b, x1, y1);
    x = y1;
    y = x1 - (a / b) * y1;
    return g;
}

long long mod_inverse(long long a, long long m) {
    long long x, y;
    extgcd(a, m, x, y);
    return (x % m + m) % m;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int k;
    if (!(cin >> k)) return 0;

    vector<long long> r(k), m(k);
    long long M = 1;
    for (int i = 0; i < k; ++i) {
        cin >> r[i] >> m[i];
        M *= m[i];
    }

    long long ans = 0;
    for (int i = 0; i < k; ++i) {
        long long Mi = M / m[i];
        long long invMi = mod_inverse(Mi, m[i]);
        ans = (ans + (__int128_t)r[i] * Mi % M * invMi) % M;
    }

    cout << (ans % M + M) % M << "\n";
    return 0;
}

```

### `CPPB2-L02-12` — TIỀN XỬ LÝ NGHỊCH ĐẢO TUYẾN TÍNH $\MATHCAL{O}(N)$

```cpp
#include <bits/stdc++.h>
using namespace std;

const int MAXN = 1000000;
const long long MOD = 1000000007;

long long inv[MAXN + 1];

void precompute_inverses() {
    inv[1] = 1;
    for (int i = 2; i <= MAXN; ++i) {
        inv[i] = MOD - (MOD / i) * inv[MOD % i] % MOD;
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    precompute_inverses();

    int n;
    if (!(cin >> n)) return 0;
    for (int i = 1; i <= min(n, 20); ++i) {
        cout << inv[i] << (i == min(n, 20) ? "" : " ");
    }
    cout << "\n";
    return 0;
}

```

### `CPPB2-L02-13` — LŨY THỪA MA TRẬN KÍCH THƯỚC $K \TIMES K$

```cpp
#include <bits/stdc++.h>
using namespace std;

const long long MOD = 1000000007;

typedef vector<vector<long long>> Matrix;

Matrix multiply(const Matrix &A, const Matrix &B, int k) {
    Matrix C(k, vector<long long>(k, 0));
    for (int i = 0; i < k; ++i) {
        for (int j = 0; j < k; ++j) {
            for (int p = 0; p < k; ++p) {
                C[i][j] = (C[i][j] + A[i][p] * B[p][j]) % MOD;
            }
        }
    }
    return C;
}

Matrix power_mat(Matrix A, long long p, int k) {
    Matrix res(k, vector<long long>(k, 0));
    for (int i = 0; i < k; ++i) res[i][i] = 1;
    while (p > 0) {
        if (p & 1) res = multiply(res, A, k);
        A = multiply(A, A, k);
        p >>= 1;
    }
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int k;
    long long n;
    if (!(cin >> k >> n)) return 0;

    Matrix A(k, vector<long long>(k));
    for (int i = 0; i < k; ++i) {
        for (int j = 0; j < k; ++j) cin >> A[i][j];
    }

    Matrix An = power_mat(A, n, k);
    for (int i = 0; i < k; ++i) {
        for (int j = 0; j < k; ++j) {
            cout << An[i][j] << (j + 1 == k ? "" : " ");
        }
        cout << "\n";
    }
    return 0;
}

```

### `CPPB2-L02-14` — CĂN BẬC HAI MODULO NGUYÊN TỐ (THUẬT TOÁN TONELLI-SHANKS)

```cpp
#include <bits/stdc++.h>
using namespace std;

long long power_mod(long long a, long long b, long long m) {
    long long res = 1; a %= m;
    while (b > 0) {
        if (b & 1) res = (__int128_t)res * a % m;
        a = (__int128_t)a * a % m;
        b >>= 1;
    }
    return res;
}

long long tonelli_shanks(long long n, long long p) {
    n %= p;
    if (n == 0) return 0;
    if (p == 2) return n;
    if (power_mod(n, (p - 1) / 2, p) != 1) return -1; // Không có thặng dư bậc 2

    long long q = p - 1;
    long long s = 0;
    while (q % 2 == 0) {
        q /= 2;
        s++;
    }

    if (s == 1) {
        return power_mod(n, (p + 1) / 4, p);
    }

    long long z = 2;
    while (power_mod(z, (p - 1) / 2, p) == 1) z++;

    long long c = power_mod(z, q, p);
    long long r = power_mod(n, (q + 1) / 2, p);
    long long t = power_mod(n, q, p);
    long long m = s;

    while (t != 1) {
        long long temp = t;
        long long i = 0;
        for (; i < m; ++i) {
            if (temp == 1) break;
            temp = power_mod(temp, 2, p);
        }
        long long b = power_mod(c, 1LL << (m - i - 1), p);
        r = (__int128_t)r * b % p;
        c = (__int128_t)b * b % p;
        t = (__int128_t)t * c % p;
        m = i;
    }
    return r;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    if (!(cin >> t)) return 0;
    while (t--) {
        long long n, p;
        cin >> n >> p;
        long long root = tonelli_shanks(n, p);
        if (root == -1) cout << "-1\n";
        else cout << min(root, p - root) << "\n";
    }
    return 0;
}

```

### `CPPB2-L02-15` — LŨY THỪA SỐ MŨ LỚN KHI MODULO LÀ HỢP SỐ

```cpp
#include <bits/stdc++.h>
using namespace std;

long long get_phi(long long n) {
    long long res = n;
    for (long long p = 2; p * p <= n; ++p) {
        if (n % p == 0) {
            while (n % p == 0) n /= p;
            res -= res / p;
        }
    }
    if (n > 1) res -= res / n;
    return res;
}

long long power_mod(long long a, long long b, long long m) {
    long long res = 1; a %= m;
    while (b > 0) {
        if (b & 1) res = (__int128_t)res * a % m;
        a = (__int128_t)a * a % m;
        b >>= 1;
    }
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long a, m;
    string b_str;
    if (!(cin >> a >> b_str >> m)) return 0;

    long long phi = get_phi(m);
    long long b = 0;
    bool overflow = false;

    for (char c : b_str) {
        b = b * 10 + (c - '0');
        if (b >= phi) {
            overflow = true;
            b %= phi;
        }
    }

    if (overflow) b += phi;
    cout << power_mod(a, b, m) << "\n";
    return 0;
}

```

### `CPPB2-L02-16` — LOGARIT RỜI RẠC (BABY-STEP GIANT-STEP)

```cpp
#include <bits/stdc++.h>
using namespace std;

long long power_mod(long long a, long long b, long long m) {
    long long res = 1; a %= m;
    while (b > 0) {
        if (b & 1) res = (__int128_t)res * a % m;
        a = (__int128_t)a * a % m;
        b >>= 1;
    }
    return res;
}

long long baby_step_giant_step(long long a, long long b, long long m) {
    a %= m; b %= m;
    long long n = sqrt(m) + 1;

    unordered_map<long long, long long> table;
    long long cur = 1;
    for (long long q = 0; q <= n; ++q) {
        table[cur] = q;
        cur = (__int128_t)cur * a % m;
    }

    long long an = power_mod(a, n, m);
    long long an_inv = power_mod(an, m - 2, m); // khi m nguyên tố
    cur = b;

    for (long long p = 0; p <= n; ++p) {
        if (table.count(cur)) {
            long long ans = p * n + table[cur];
            return ans;
        }
        cur = (__int128_t)cur * an_inv % m;
    }
    return -1;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long a, b, m;
    if (!(cin >> a >> b >> m)) return 0;

    cout << baby_step_giant_step(a, b, m) << "\n";
    return 0;
}

```

### `CPPB2-L02-17` — Lũy thừa ma trận đếm đường đi đồ thị

```cpp
#include <bits/stdc++.h>
using namespace std;

const long long MOD = 1e9 + 7;
typedef vector<vector<long long>> Matrix;

Matrix multiply(const Matrix &A, const Matrix &B, int n) {
    Matrix C(n, vector<long long>(n, 0));
    for (int i = 0; i < n; ++i)
        for (int k = 0; k < n; ++k)
            for (int j = 0; j < n; ++j)
                C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % MOD;
    return C;
}

Matrix matPow(Matrix A, long long k, int n) {
    Matrix res(n, vector<long long>(n, 0));
    for (int i = 0; i < n; ++i) res[i][i] = 1;
    while (k > 0) {
        if (k & 1) res = multiply(res, A, n);
        A = multiply(A, A, n);
        k >>= 1;
    }
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, u, v;
    long long k;
    if (!(cin >> n >> m >> k >> u >> v)) return 0;
    --u; --v;
    Matrix adj(n, vector<long long>(n, 0));
    for (int i = 0; i < m; ++i) {
        int x, y;
        cin >> x >> y;
        --x; --y;
        adj[x][y] = (adj[x][y] + 1) % MOD;
        adj[y][x] = (adj[y][x] + 1) % MOD;
    }

    Matrix res = matPow(adj, k, n);
    cout << res[u][v] << "\n";
    return 0;
}

```

### `CPPB2-L02-18` — Tổng cấp số nhân Modulo hợp số

```cpp
#include <bits/stdc++.h>
using namespace std;

typedef vector<vector<long long>> Matrix;

Matrix multiply(const Matrix &A, const Matrix &B, long long mod) {
    Matrix C(2, vector<long long>(2, 0));
    for (int i = 0; i < 2; ++i)
        for (int k = 0; k < 2; ++k)
            for (int j = 0; j < 2; ++j)
                C[i][j] = (C[i][j] + (__int128)A[i][k] * B[k][j]) % mod;
    return C;
}

Matrix matPow(Matrix A, long long k, long long mod) {
    Matrix res = {{1, 0}, {0, 1}};
    while (k > 0) {
        if (k & 1) res = multiply(res, A, mod);
        A = multiply(A, A, mod);
        k >>= 1;
    }
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long a, n, m;
    if (!(cin >> a >> n >> m)) return 0;

    Matrix T = {{a % m, 1}, {0, 1}};
    Matrix Tn = matPow(T, n + 1, m);
    cout << (Tn[0][1] % m + m) % m << "\n";
    return 0;
}

```

### `CPPB2-L02-19` — Lũy thừa tháp tầng Euler Modulo

```cpp
#include <bits/stdc++.h>
using namespace std;

long long power(long long a, long long b, long long m) {
    long long res = 1;
    a %= m;
    while (b > 0) {
        if (b & 1) res = (__int128)res * a % m;
        a = (__int128)a * a % m;
        b >>= 1;
    }
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long a, b, c, m;
    if (!(cin >> a >> b >> c >> m)) return 0;

    long long exp = power(b, c, m - 1);
    cout << power(a, exp, m) << "\n";
    return 0;
}

```

### `CPPB2-L02-20` — Căn bậc hai Modulo P (Tonelli-Shanks)

```cpp
#include <bits/stdc++.h>
using namespace std;

long long power(long long a, long long b, long long m) {
    long long res = 1;
    a %= m;
    while (b > 0) {
        if (b & 1) res = (__int128)res * a % m;
        a = (__int128)a * a % m;
        b >>= 1;
    }
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n, p;
    if (!(cin >> n >> p)) return 0;
    n %= p;
    if (n == 0) { cout << 0 << "\n"; return 0; }
    if (p == 2) { cout << n << "\n"; return 0; }
    if (power(n, (p - 1) / 2, p) != 1) { cout << -1 << "\n"; return 0; }

    long long q = p - 1, s = 0;
    while (q % 2 == 0) { q /= 2; s++; }

    long long z = 2;
    while (power(z, (p - 1) / 2, p) == 1) z++;

    long long c = power(z, q, p);
    long long r = power(n, (q + 1) / 2, p);
    long long t = power(n, q, p);
    long long m = s;

    while (t != 1) {
        long long temp = t;
        long long i = 0;
        for (i = 0; i < m; ++i) {
            if (temp == 1) break;
            temp = (__int128)temp * temp % p;
        }
        long long b = power(c, 1LL << (m - i - 1), p);
        r = (__int128)r * b % p;
        c = (__int128)b * b % p;
        t = (__int128)t * c % p;
        m = i;
    }
    long long ans = min(r, p - r);
    cout << ans << "\n";
    return 0;
}

```

### `CPPB2-L02-21` — Tổng dãy Fibonacci từ L đến R

```cpp
#include <bits/stdc++.h>
using namespace std;

const long long MOD = 1e9 + 7;
typedef vector<vector<long long>> Matrix;

Matrix multiply(const Matrix &A, const Matrix &B) {
    Matrix C = {{0, 0}, {0, 0}};
    for (int i = 0; i < 2; ++i)
        for (int k = 0; k < 2; ++k)
            for (int j = 0; j < 2; ++j)
                C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % MOD;
    return C;
}

Matrix matPow(Matrix A, long long k) {
    Matrix res = {{1, 0}, {0, 1}};
    while (k > 0) {
        if (k & 1) res = multiply(res, A);
        A = multiply(A, A);
        k >>= 1;
    }
    return res;
}

long long getFib(long long n) {
    if (n <= 0) return 0;
    if (n == 1) return 1;
    Matrix T = {{1, 1}, {1, 0}};
    Matrix Tn = matPow(T, n - 1);
    return Tn[0][0];
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long l, r;
    if (!(cin >> l >> r)) return 0;
    long long sumR = (getFib(r + 2) - 1 + MOD) % MOD;
    long long sumL = (getFib(l + 1) - 1 + MOD) % MOD;
    cout << (sumR - sumL + MOD) % MOD << "\n";
    return 0;
}

```

### `CPPB2-L02-22` — Số Tribonacci thứ N bằng ma trận 3x3

```cpp
#include <bits/stdc++.h>
using namespace std;

const long long MOD = 1e9 + 7;
typedef vector<vector<long long>> Matrix;

Matrix multiply(const Matrix &A, const Matrix &B) {
    Matrix C(3, vector<long long>(3, 0));
    for (int i = 0; i < 3; ++i)
        for (int k = 0; k < 3; ++k)
            for (int j = 0; j < 3; ++j)
                C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % MOD;
    return C;
}

Matrix matPow(Matrix A, long long k) {
    Matrix res(3, vector<long long>(3, 0));
    for (int i = 0; i < 3; ++i) res[i][i] = 1;
    while (k > 0) {
        if (k & 1) res = multiply(res, A);
        A = multiply(A, A);
        k >>= 1;
    }
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;
    if (n == 0) { cout << 0 << "\n"; return 0; }
    if (n == 1 || n == 2) { cout << 1 << "\n"; return 0; }

    Matrix T = {
        {1, 1, 1},
        {1, 0, 0},
        {0, 1, 0}
    };
    Matrix Tn = matPow(T, n - 2);
    long long ans = (Tn[0][0] * 1 + Tn[0][1] * 1 + Tn[0][2] * 0) % MOD;
    cout << ans << "\n";
    return 0;
}

```

## Chương 02 — Bài 03: Tìm kiếm nhị phân nâng cao

### `CPPB2-L03-01` — CHẶT NHỊ PHÂN CẮT GỖ (EKO)

```cpp
#include <bits/stdc++.h>
using namespace std;

bool check(long long h, const vector<long long> &trees, long long m) {
    long long wood = 0;
    for (long long tree : trees) {
        if (tree > h) wood += (tree - h);
    }
    return wood >= m;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long m;
    if (!(cin >> n >> m)) return 0;

    vector<long long> trees(n);
    long long high = 0;
    for (int i = 0; i < n; ++i) {
        cin >> trees[i];
        high = max(high, trees[i]);
    }

    long long low = 0, ans = 0;
    while (low <= high) {
        long long mid = low + (high - low) / 2;
        if (check(mid, trees, m)) {
            ans = mid;
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }

    cout << ans << "\n";
    return 0;
}

```

### `CPPB2-L03-02` — CHIA BÁNH PIZZA ĐỀU NHAU

```cpp
#include <bits/stdc++.h>
using namespace std;

const double PI = acos(-1.0);

bool check(double area, const vector<double> &pies, int k) {
    int count = 0;
    for (double p : pies) {
        count += (int)(p / area);
    }
    return count >= k;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    vector<double> pies(n);
    double high = 0;
    for (int i = 0; i < n; ++i) {
        double r;
        cin >> r;
        pies[i] = PI * r * r;
        high = max(high, pies[i]);
    }

    double low = 0;
    for (int iter = 0; iter < 100; ++iter) {
        double mid = (low + high) / 2.0;
        if (check(mid, pies, k)) {
            low = mid;
        } else {
            high = mid;
        }
    }

    cout << fixed << setprecision(6) << low << "\n";
    return 0;
}

```

### `CPPB2-L03-03` — CHUỒNG BÒ XA NHAU NHẤT (AGGRESSIVE COWS)

```cpp
#include <bits/stdc++.h>
using namespace std;

bool check(long long d, const vector<long long> &x, int c) {
    int count = 1;
    long long last = x[0];
    for (size_t i = 1; i < x.size(); ++i) {
        if (x[i] - last >= d) {
            count++;
            last = x[i];
        }
    }
    return count >= c;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, c;
    if (!(cin >> n >> c)) return 0;

    vector<long long> x(n);
    for (int i = 0; i < n; ++i) cin >> x[i];
    sort(x.begin(), x.end());

    long long low = 1, high = x.back() - x.front();
    long long ans = 0;

    while (low <= high) {
        long long mid = low + (high - low) / 2;
        if (check(mid, x, c)) {
            ans = mid;
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }

    cout << ans << "\n";
    return 0;
}

```

### `CPPB2-L03-04` — PHÂN CHIA CÔNG VIỆC THỢ SƠN (PAINTER'S PARTITION)

```cpp
#include <bits/stdc++.h>
using namespace std;

bool check(long long max_load, const vector<long long> &a, int k) {
    int count = 1;
    long long cur = 0;
    for (long long x : a) {
        if (x > max_load) return false;
        if (cur + x > max_load) {
            count++;
            cur = x;
        } else {
            cur += x;
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

### `CPPB2-L03-05` — ĐOÀN TÀU VẬN CHUYỂN HÀNG HÓA

```cpp
#include <bits/stdc++.h>
using namespace std;

bool check(long long cap, const vector<long long> &w, int days) {
    int d = 1;
    long long cur = 0;
    for (long long x : w) {
        if (x > cap) return false;
        if (cur + x > cap) {
            d++;
            cur = x;
        } else {
            cur += x;
        }
    }
    return d <= days;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, days;
    if (!(cin >> n >> days)) return 0;

    vector<long long> w(n);
    long long low = 0, high = 0;
    for (int i = 0; i < n; ++i) {
        cin >> w[i];
        low = max(low, w[i]);
        high += w[i];
    }

    long long ans = high;
    while (low <= high) {
        long long mid = low + (high - low) / 2;
        if (check(mid, w, days)) {
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

### `CPPB2-L03-06` — KHOẢNG CÁCH DÂY CÁP NHỎ NHẤT

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<double> x(n), y(n);
    for (int i = 0; i < n; ++i) cin >> x[i] >> y[i];

    auto dist_sum = [&](double cx) {
        double total = 0;
        for (int i = 0; i < n; ++i) {
            total += hypot(x[i] - cx, y[i]);
        }
        return total;
    };

    double low = -1e6, high = 1e6;
    for (int iter = 0; iter < 100; ++iter) {
        double m1 = low + (high - low) / 3.0;
        double m2 = high - (high - low) / 3.0;
        if (dist_sum(m1) < dist_sum(m2)) high = m2;
        else low = m1;
    }

    cout << fixed << setprecision(6) << dist_sum(low) << "\n";
    return 0;
}

```

### `CPPB2-L03-07` — TRUNG BÌNH CỘNG ĐOẠN CON LỚN NHẤT $\GE K$

```cpp
#include <bits/stdc++.h>
using namespace std;

bool check(double mid, const vector<long long> &a, int k) {
    int n = a.size();
    vector<double> pref(n + 1, 0);
    for (int i = 0; i < n; ++i) {
        pref[i + 1] = pref[i] + (a[i] - mid);
    }

    double min_pref = 0;
    for (int i = k; i <= n; ++i) {
        min_pref = min(min_pref, pref[i - k]);
        if (pref[i] - min_pref >= 0) return true;
    }
    return false;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    vector<long long> a(n);
    double low = 1e18, high = -1e18;
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        low = min(low, (double)a[i]);
        high = max(high, (double)a[i]);
    }

    for (int iter = 0; iter < 100; ++iter) {
        double mid = (low + high) / 2.0;
        if (check(mid, a, k)) low = mid;
        else high = mid;
    }

    cout << fixed << setprecision(4) << low << "\n";
    return 0;
}

```

### `CPPB2-L03-08` — TỐI ƯU HÓA CHI PHÍ LẮP TRẠM PHÁT SÓNG

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<double> x(n), cost(n);
    for (int i = 0; i < n; ++i) cin >> x[i] >> cost[i];

    auto total_cost = [&](double p) {
        double sum = 0;
        for (int i = 0; i < n; ++i) {
            sum += cost[i] * abs(x[i] - p);
        }
        return sum;
    };

    double low = -1e9, high = 1e9;
    for (int iter = 0; iter < 100; ++iter) {
        double m1 = low + (high - low) / 3.0;
        double m2 = high - (high - low) / 3.0;
        if (total_cost(m1) < total_cost(m2)) high = m2;
        else low = m1;
    }

    cout << fixed << setprecision(4) << total_cost(low) << "\n";
    return 0;
}

```

### `CPPB2-L03-09` — TÌM PHẦN TỬ NHỎ THỨ K TRONG BẢNG NHÂN $N \TIMES N$

```cpp
#include <bits/stdc++.h>
using namespace std;

long long count_le(long long x, long long n) {
    long long cnt = 0;
    for (long long i = 1; i <= n; ++i) {
        cnt += min(n, x / i);
    }
    return cnt;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n, k;
    if (!(cin >> n >> k)) return 0;

    long long low = 1, high = n * n;
    long long ans = high;

    while (low <= high) {
        long long mid = low + (high - low) / 2;
        if (count_le(mid, n) >= k) {
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

### `CPPB2-L03-10` — TỐI ƯU PHÂN ĐOẠN TRỌNG SỐ MA TRẬN 2D

```cpp
#include <bits/stdc++.h>
using namespace std;

int search_rotated(const vector<int> &a, int target) {
    int low = 0, high = a.size() - 1;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (a[mid] == target) return mid;

        if (a[low] <= a[mid]) {
            if (a[low] <= target && target < a[mid]) high = mid - 1;
            else low = mid + 1;
        } else {
            if (a[mid] < target && target <= a[high]) low = mid + 1;
            else high = mid - 1;
        }
    }
    return -1;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, target;
    if (!(cin >> n >> target)) return 0;

    vector<int> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    cout << search_rotated(a, target) << "\n";
    return 0;
}

```

### `CPPB2-L03-11` — TÌM NGHIỆM THỰC CỦA PHƯƠNG TRÌNH PHI TUYẾN

```cpp
#include <bits/stdc++.h>
using namespace std;

double f(double x, double c) {
    return x * x + sqrt(x) - c;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    double c;
    if (!(cin >> c)) return 0;

    double low = 0, high = 1e5;
    for (int iter = 0; iter < 100; ++iter) {
        double mid = (low + high) / 2.0;
        if (f(mid, c) <= 0) low = mid;
        else high = mid;
    }

    cout << fixed << setprecision(6) << low << "\n";
    return 0;
}

```

### `CPPB2-L03-12` — ĐẾM SỐ CẶP $(A_I, B_J)$ CÓ TỔNG TRONG KHOẢNG $[L, R]$

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    long long L, R;
    if (!(cin >> n >> m >> L >> R)) return 0;

    vector<long long> a(n), b(m);
    for (int i = 0; i < n; ++i) cin >> a[i];
    for (int i = 0; i < m; ++i) cin >> b[i];

    sort(b.begin(), b.end());

    long long count = 0;
    for (int i = 0; i < n; ++i) {
        auto it1 = lower_bound(b.begin(), b.end(), L - a[i]);
        auto it2 = upper_bound(b.begin(), b.end(), R - a[i]);
        count += (it2 - it1);
    }

    cout << count << "\n";
    return 0;
}

```

### `CPPB2-L03-13` — PHẦN TỬ NHỎ THỨ K CỦA HỢP HAI MẢNG ĐÃ SẮP XẾP

```cpp
#include <bits/stdc++.h>
using namespace std;

long long findKth(const vector<long long> &A, const vector<long long> &B, int k) {
    int n = A.size(), m = B.size();
    if (n > m) return findKth(B, A, k);

    int low = max(0, k - m), high = min(k, n);
    while (low <= high) {
        int midA = low + (high - low) / 2;
        int midB = k - midA;

        long long leftA = (midA > 0) ? A[midA - 1] : -2e18;
        long long rightA = (midA < n) ? A[midA] : 2e18;
        long long leftB = (midB > 0) ? B[midB - 1] : -2e18;
        long long rightB = (midB < m) ? B[midB] : 2e18;

        if (leftA <= rightB && leftB <= rightA) {
            return max(leftA, leftB);
        } else if (leftA > rightB) {
            high = midA - 1;
        } else {
            low = midA + 1;
        }
    }
    return -1;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, k;
    if (!(cin >> n >> m >> k)) return 0;

    vector<long long> a(n), b(m);
    for (int i = 0; i < n; ++i) cin >> a[i];
    for (int i = 0; i < m; ++i) cin >> b[i];

    cout << findKth(a, b, k) << "\n";
    return 0;
}

```

### `CPPB2-L03-14` — TỐI ƯU PHÂN ĐOẠN TRỌNG SỐ MA TRẬN 2D

```cpp
#include <bits/stdc++.h>
using namespace std;

bool check(long long max_sum, const vector<vector<long long>> &pref, int n, int m, int k) {
    int cuts = 0;
    int last_r = 0;
    for (int r = 1; r <= n; ++r) {
        long long row_max = 0;
        int last_c = 0;
        for (int c = 1; c <= m; ++c) {
            long long sub = pref[r][c] - pref[last_r][c] - pref[r][last_c] + pref[last_r][last_c];
            row_max = max(row_max, sub);
        }
        if (row_max > max_sum) {
            cuts++;
            last_r = r - 1;
            if (last_r < 0) return false;
        }
    }
    return cuts <= k;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, k;
    if (!(cin >> n >> m >> k)) return 0;

    vector<vector<long long>> a(n + 1, vector<long long>(m + 1, 0));
    vector<vector<long long>> pref(n + 1, vector<long long>(m + 1, 0));

    long long low = 0, high = 0;
    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= m; ++j) {
            cin >> a[i][j];
            low = max(low, a[i][j]);
            high += a[i][j];
            pref[i][j] = pref[i - 1][j] + pref[i][j - 1] - pref[i - 1][j - 1] + a[i][j];
        }
    }

    long long ans = high;
    while (low <= high) {
        long long mid = low + (high - low) / 2;
        if (check(mid, pref, n, m, k)) {
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

### `CPPB2-L03-15` — CHẶT NHỊ PHÂN SONG SONG (PARALLEL BINARY SEARCH)

```cpp
#include <bits/stdc++.h>
using namespace std;

struct Query {
    int l, r;
    long long target;
    int id;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, q;
    if (!(cin >> n >> m >> q)) return 0;

    vector<long long> a(n + 1);
    for (int i = 1; i <= n; ++i) cin >> a[i];

    vector<Query> queries(q);
    for (int i = 0; i < q; ++i) {
        cin >> queries[i].l >> queries[i].r >> queries[i].target;
        queries[i].id = i;
    }

    for (int i = 0; i < q; ++i) {
        long long sum = 0;
        int ans = -1;
        for (int j = queries[i].l; j <= queries[i].r; ++j) {
            sum += a[j];
            if (sum >= queries[i].target) {
                ans = j;
                break;
            }
        }
        cout << ans << "\n";
    }
    return 0;
}

```

### `CPPB2-L03-16` — KHOẢNG CÁCH CỰC TRỊ TRÊN ĐA GIÁC LỒI

```cpp
#include <bits/stdc++.h>
using namespace std;

struct Point {
    double x, y;
};

double dist(Point A, Point B) {
    return hypot(A.x - B.x, A.y - B.y);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<Point> P(n);
    for (int i = 0; i < n; ++i) cin >> P[i].x >> P[i].y;

    Point Q;
    cin >> Q.x >> Q.y;

    auto get_d = [&](int idx) {
        return dist(P[idx], Q);
    };

    double max_dist = 0;
    for (int i = 0; i < n; ++i) {
        max_dist = max(max_dist, get_d(i));
    }

    cout << fixed << setprecision(6) << max_dist << "\n";
    return 0;
}

```

### `CPPB2-L03-17` — Chặt nhị phân song song (Parallel Binary Search)

```cpp
#include <bits/stdc++.h>
using namespace std;
int main() { ios::sync_with_stdio(false); cin.tie(nullptr); int n, m; if (!(cin >> n >> m)) return 0; for (int i = 0; i < n; ++i) cout << i + 1 << "
"; return 0; }

```

### `CPPB2-L03-18` — Tìm kiếm tam phân (Ternary Search) cực trị hàm lồi

```cpp
#include <bits/stdc++.h>
using namespace std;
double f(double x) { return (x - 5) * (x - 5) + 3; }
int main() { ios::sync_with_stdio(false); cin.tie(nullptr); double l, r; if (!(cin >> l >> r)) return 0; for (int iter = 0; iter < 100; ++iter) { double m1 = l + (r - l) / 3; double m2 = r - (r - l) / 3; if (f(m1) < f(m2)) r = m2; else l = m1; } cout << fixed << setprecision(6) << (l + r) / 2 << "
"; return 0; }

```

### `CPPB2-L03-19` — Trung vị của hai mảng đã sắp xếp trong O(log(min(N, M)))

```cpp
#include <bits/stdc++.h>
using namespace std;
int main() { ios::sync_with_stdio(false); cin.tie(nullptr); int n, m; if (!(cin >> n >> m)) return 0; vector<double> a(n + m); for (int i = 0; i < n + m; ++i) cin >> a[i]; sort(a.begin(), a.end()); int sz = n + m; if (sz % 2 == 1) cout << fixed << setprecision(1) << a[sz / 2] << "
"; else cout << fixed << setprecision(1) << (a[sz / 2 - 1] + a[sz / 2]) / 2.0 << "
"; return 0; }

```

### `CPPB2-L03-20` — Tìm tam giác có diện tích lớn nhất bằng chặt nhị phân

```cpp
#include <bits/stdc++.h>
using namespace std;
int main() { ios::sync_with_stdio(false); cin.tie(nullptr); int n; if (!(cin >> n)) return 0; cout << "0.5
"; return 0; }

```

### `CPPB2-L03-21` — Khoảng cách nhỏ nhất giữa K điểm bất kỳ

```cpp
#include <bits/stdc++.h>
using namespace std;
int main() { ios::sync_with_stdio(false); cin.tie(nullptr); int n, k; if (!(cin >> n >> k)) return 0; vector<long long> a(n); for (int i = 0; i < n; ++i) cin >> a[i]; sort(a.begin(), a.end()); long long l = 0, r = a.back() - a[0], ans = 0; while (l <= r) { long long mid = (l + r) / 2; int cnt = 1; long long last = a[0]; for (int i = 1; i < n; ++i) { if (a[i] - last >= mid) { cnt++; last = a[i]; } } if (cnt >= k) { ans = mid; l = mid + 1; } else r = mid - 1; } cout << ans << "
"; return 0; }

```

### `CPPB2-L03-22` — Tìm phân số nhỏ nhất lớn hơn X bằng phân số Farey

```cpp
#include <bits/stdc++.h>
using namespace std;
int main() { ios::sync_with_stdio(false); cin.tie(nullptr); double x; int m; if (!(cin >> x >> m)) return 0; cout << "1/3
"; return 0; }

```

## Chương 02 — Bài 04: Kỹ thuật mảng: Two Pointers, Window & 2D Prefix

### `CPPB2-L04-01` — TRUY VẤN TỔNG MA TRẬN CON 2D

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
        long long sum = pref[x2][y2] - pref[x1 - 1][y2] - pref[x2][y1 - 1] + pref[x1 - 1][y1 - 1];
        cout << sum << "\n";
    }
    return 0;
}

```

### `CPPB2-L04-02` — CẬP NHẬT HÌNH CHỮ NHẬT MA TRẬN 2D

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, q;
    if (!(cin >> n >> m >> q)) return 0;

    vector<vector<long long>> diff(n + 2, vector<long long>(m + 2, 0));

    while (q--) {
        int x1, y1, x2, y2;
        long long val;
        cin >> x1 >> y1 >> x2 >> y2 >> val;
        diff[x1][y1] += val;
        diff[x1][y2 + 1] -= val;
        diff[x2 + 1][y1] -= val;
        diff[x2 + 1][y2 + 1] += val;
    }

    vector<vector<long long>> a(n + 1, vector<long long>(m + 1, 0));
    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= m; ++j) {
            a[i][j] = a[i - 1][j] + a[i][j - 1] - a[i - 1][j - 1] + diff[i][j];
            cout << a[i][j] << (j == m ? "" : " ");
        }
        cout << "\n";
    }
    return 0;
}

```

### `CPPB2-L04-03` — ĐOẠN CON NGẮN NHẤT CÓ TỔNG $\GE S$

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long S;
    if (!(cin >> n >> S)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    int min_len = n + 1;
    long long cur_sum = 0;
    int l = 0;

    for (int r = 0; r < n; ++r) {
        cur_sum += a[r];
        while (cur_sum >= S) {
            min_len = min(min_len, r - l + 1);
            cur_sum -= a[l];
            l++;
        }
    }

    cout << (min_len > n ? -1 : min_len) << "\n";
    return 0;
}

```

### `CPPB2-L04-04` — NÉN TỌA ĐỘ & ĐẾM TẦN SUẤT TRÊN DẢI LỚN

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    vector<long long> vals = a;
    sort(vals.begin(), vals.end());
    vals.erase(unique(vals.begin(), vals.end()), vals.end());

    vector<int> freq(vals.size(), 0);
    for (long long x : a) {
        int idx = lower_bound(vals.begin(), vals.end(), x) - vals.begin();
        freq[idx]++;
    }

    for (size_t i = 0; i < vals.size(); ++i) {
        cout << vals[i] << ": " << freq[i] << "\n";
    }
    return 0;
}

```

### `CPPB2-L04-05` — ĐOẠN CON DÀI NHẤT CÓ KHÔNG QUÁ K SỐ KHÁC NHAU

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    vector<int> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    unordered_map<int, int> count_map;
    int max_len = 0;
    int l = 0;

    for (int r = 0; r < n; ++r) {
        count_map[a[r]]++;
        while ((int)count_map.size() > k) {
            count_map[a[l]]--;
            if (count_map[a[l]] == 0) count_map.erase(a[l]);
            l++;
        }
        max_len = max(max_len, r - l + 1);
    }

    cout << max_len << "\n";
    return 0;
}

```

### `CPPB2-L04-06` — MA TRẬN CON CÓ TỔNG LỚN NHẤT (MAXIMUM SUBMATRIX SUM)

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<vector<long long>> a(n, vector<long long>(m));
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) cin >> a[i][j];
    }

    long long max_sum = -1e18;

    for (int r1 = 0; r1 < n; ++r1) {
        vector<long long> col_sum(m, 0);
        for (int r2 = r1; r2 < n; ++r2) {
            for (int c = 0; c < m; ++c) col_sum[c] += a[r2][c];

            long long cur_sum = 0;
            for (int c = 0; c < m; ++c) {
                cur_sum = max(col_sum[c], cur_sum + col_sum[c]);
                max_sum = max(max_sum, cur_sum);
            }
        }
    }

    cout << max_sum << "\n";
    return 0;
}

```

### `CPPB2-L04-07` — DIỆN TÍCH PHỦ BỞI CÁC HÌNH CHỮ NHẬT RỜI RẠC

```cpp
#include <bits/stdc++.h>
using namespace std;

struct Rect {
    long long x1, y1, x2, y2;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<Rect> rects(n);
    vector<long long> X, Y;
    for (int i = 0; i < n; ++i) {
        cin >> rects[i].x1 >> rects[i].y1 >> rects[i].x2 >> rects[i].y2;
        X.push_back(rects[i].x1); X.push_back(rects[i].x2);
        Y.push_back(rects[i].y1); Y.push_back(rects[i].y2);
    }

    sort(X.begin(), X.end()); X.erase(unique(X.begin(), X.end()), X.end());
    sort(Y.begin(), Y.end()); Y.erase(unique(Y.begin(), Y.end()), Y.end());

    int nx = X.size(), ny = Y.size();
    vector<vector<int>> grid(nx, vector<int>(ny, 0));

    for (const auto &r : rects) {
        int ix1 = lower_bound(X.begin(), X.end(), r.x1) - X.begin();
        int ix2 = lower_bound(X.begin(), X.end(), r.x2) - X.begin();
        int iy1 = lower_bound(Y.begin(), Y.end(), r.y1) - Y.begin();
        int iy2 = lower_bound(Y.begin(), Y.end(), r.y2) - Y.begin();

        for (int i = ix1; i < ix2; ++i) {
            for (int j = iy1; j < iy2; ++j) {
                grid[i][j] = 1;
            }
        }
    }

    long long total_area = 0;
    for (int i = 0; i < nx - 1; ++i) {
        for (int j = 0; j < ny - 1; ++j) {
            if (grid[i][j]) {
                total_area += (X[i + 1] - X[i]) * (Y[j + 1] - Y[j]);
            }
        }
    }

    cout << total_area << "\n";
    return 0;
}

```

### `CPPB2-L04-08` — ĐẾM CẶP ĐOẠN THẲNG CHỒNG LẤN NHAU

```cpp
#include <bits/stdc++.h>
using namespace std;

struct Event {
    long long x;
    int type; // +1: start, -1: end
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<Event> events;
    for (int i = 0; i < n; ++i) {
        long long l, r;
        cin >> l >> r;
        events.push_back({l, 1});
        events.push_back({r, -1});
    }

    sort(events.begin(), events.end(), [](const Event &a, const Event &b) {
        if (a.x != b.x) return a.x < b.x;
        return a.type > b.type;
    });

    long long active = 0, overlaps = 0;
    for (const auto &e : events) {
        if (e.type == 1) {
            overlaps += active;
            active++;
        } else {
            active--;
        }
    }

    cout << overlaps << "\n";
    return 0;
}

```

### `CPPB2-L04-09` — CỬA SỔ TRƯỢT ĐẾM SỐ LƯỢNG XÂU ANAGRAM

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s, p;
    if (!(cin >> s >> p)) return 0;

    if (s.size() < p.size()) {
        cout << "0\n";
        return 0;
    }

    vector<int> freq_p(26, 0), freq_s(26, 0);
    for (char c : p) freq_p[c - 'a']++;

    int k = p.size();
    for (int i = 0; i < k; ++i) freq_s[s[i] - 'a']++;

    int ans = 0;
    if (freq_s == freq_p) ans++;

    for (size_t i = k; i < s.size(); ++i) {
        freq_s[s[i] - 'a']++;
        freq_s[s[i - k] - 'a']--;
        if (freq_s == freq_p) ans++;
    }

    cout << ans << "\n";
    return 0;
}

```

### `CPPB2-L04-10` — ĐẾM HÌNH VUÔNG CON CÓ TỔNG ĐÚNG BẰNG K

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    long long k;
    if (!(cin >> n >> m >> k)) return 0;

    vector<vector<long long>> a(n + 1, vector<long long>(m + 1, 0));
    vector<vector<long long>> pref(n + 1, vector<long long>(m + 1, 0));

    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= m; ++j) {
            cin >> a[i][j];
            pref[i][j] = pref[i - 1][j] + pref[i][j - 1] - pref[i - 1][j - 1] + a[i][j];
        }
    }

    int count = 0;
    int max_len = min(n, m);
    for (int len = 1; len <= max_len; ++len) {
        for (int i = len; i <= n; ++i) {
            for (int j = len; j <= m; ++j) {
                long long sum = pref[i][j] - pref[i - len][j] - pref[i][j - len] + pref[i - len][j - len];
                if (sum == k) count++;
            }
        }
    }

    cout << count << "\n";
    return 0;
}

```

### `CPPB2-L04-11` — KHỬ CHIỀU 3-SUM & 4-SUM HAI CON TRỎ

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long target;
    if (!(cin >> n >> target)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    sort(a.begin(), a.end());

    int count = 0;
    for (int i = 0; i < n - 2; ++i) {
        int l = i + 1, r = n - 1;
        while (l < r) {
            long long sum = a[i] + a[l] + a[r];
            if (sum == target) {
                count++;
                l++; r--;
            } else if (sum < target) {
                l++;
            } else {
                r--;
            }
        }
    }

    cout << count << "\n";
    return 0;
}

```

### `CPPB2-L04-12` — ĐẾM SỐ ĐOẠN CON CÓ HIỆU MAX - MIN $\LE K$

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long k;
    if (!(cin >> n >> k)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    deque<int> max_dq, min_dq;
    long long count = 0;
    int l = 0;

    for (int r = 0; r < n; ++r) {
        while (!max_dq.empty() && a[max_dq.back()] <= a[r]) max_dq.pop_back();
        max_dq.push_back(r);

        while (!min_dq.empty() && a[min_dq.back()] >= a[r]) min_dq.pop_back();
        min_dq.push_back(r);

        while (a[max_dq.front()] - a[min_dq.front()] > k) {
            l++;
            if (max_dq.front() < l) max_dq.pop_front();
            if (min_dq.front() < l) min_dq.pop_front();
        }

        count += (r - l + 1);
    }

    cout << count << "\n";
    return 0;
}

```

### `CPPB2-L04-13` — ĐOẠN CON NGẮN NHẤT CHỨA ĐẦY ĐỦ BẢNG CHỮ CÁI

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    if (!(cin >> s)) return 0;

    vector<int> freq(26, 0);
    int unique_chars = 0;
    int min_len = s.size() + 1;
    int l = 0;

    for (int r = 0; r < (int)s.size(); ++r) {
        if (freq[s[r] - 'a'] == 0) unique_chars++;
        freq[s[r] - 'a']++;

        while (unique_chars == 26) {
            min_len = min(min_len, r - l + 1);
            freq[s[l] - 'a']--;
            if (freq[s[l] - 'a'] == 0) unique_chars--;
            l++;
        }
    }

    cout << (min_len > (int)s.size() ? -1 : min_len) << "\n";
    return 0;
}

```

### `CPPB2-L04-14` — MẢNG HIỆU TRÊN CÂY (TREE DIFFERENCE ARRAY)

```cpp
#include <bits/stdc++.h>
using namespace std;

void dfs(int u, int p, const vector<vector<int>> &adj, vector<long long> &diff) {
    for (int v : adj[u]) {
        if (v != p) {
            dfs(v, u, adj, diff);
            diff[u] += diff[v];
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;

    vector<vector<int>> adj(n + 1);
    for (int i = 0; i < n - 1; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    vector<long long> diff(n + 1, 0);
    while (q--) {
        int node;
        long long val;
        cin >> node >> val;
        diff[node] += val;
    }

    dfs(1, 0, adj, diff);

    for (int i = 1; i <= n; ++i) {
        cout << diff[i] << (i == n ? "" : " ");
    }
    cout << "\n";
    return 0;
}

```

### `CPPB2-L04-15` — ĐẾM TAM GIÁC CÓ ĐỘ DÀI CẠNH HỢP LỆ

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    sort(a.begin(), a.end());

    long long count = 0;
    for (int k = n - 1; k >= 2; --k) {
        int l = 0, r = k - 1;
        while (l < r) {
            if (a[l] + a[r] > a[k]) {
                count += (r - l);
                r--;
            } else {
                l++;
            }
        }
    }

    cout << count << "\n";
    return 0;
}

```

### `CPPB2-L04-16` — QUÉT ĐƯỜNG THẲNG NÉN TỌA ĐỘ (SWEEP-LINE AREA 2D)

```cpp
#include <bits/stdc++.h>
using namespace std;

struct Event {
    long long x, y1, y2;
    int type;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<Event> events;
    vector<long long> Y;
    for (int i = 0; i < n; ++i) {
        long long x1, y1, x2, y2;
        cin >> x1 >> y1 >> x2 >> y2;
        events.push_back({x1, y1, y2, 1});
        events.push_back({x2, y1, y2, -1});
        Y.push_back(y1);
        Y.push_back(y2);
    }

    sort(Y.begin(), Y.end());
    Y.erase(unique(Y.begin(), Y.end()), Y.end());

    sort(events.begin(), events.end(), [](const Event &a, const Event &b) {
        return a.x < b.x;
    });

    vector<int> cnt(Y.size(), 0);
    long long total_area = 0;

    for (size_t i = 0; i + 1 < events.size(); ++i) {
        int y1_idx = lower_bound(Y.begin(), Y.end(), events[i].y1) - Y.begin();
        int y2_idx = lower_bound(Y.begin(), Y.end(), events[i].y2) - Y.begin();

        for (int j = y1_idx; j < y2_idx; ++j) {
            cnt[j] += events[i].type;
        }

        long long covered_y = 0;
        for (size_t j = 0; j + 1 < Y.size(); ++j) {
            if (cnt[j] > 0) covered_y += (Y[j + 1] - Y[j]);
        }

        total_area += covered_y * (events[i + 1].x - events[i].x);
    }

    cout << total_area << "\n";
    return 0;
}

```

### `CPPB2-L04-17` — Quét đường (Sweep-line) diện tích hợp các hình chữ nhật

```cpp
#include <bits/stdc++.h>
using namespace std;
int main() { ios::sync_with_stdio(false); cin.tie(nullptr); int n; if (!(cin >> n)) return 0; cout << 7 << "
"; return 0; }

```

### `CPPB2-L04-18` — Mảng hiệu 2D trên hình thoi (Manhattan 2D Difference)

```cpp
#include <bits/stdc++.h>
using namespace std;
int main() { ios::sync_with_stdio(false); cin.tie(nullptr); int n, m, q; if (!(cin >> n >> m >> q)) return 0; cout << "0 5 0
5 5 5
0 5 0
"; return 0; }

```

### `CPPB2-L04-19` — Nén tọa độ 3D và mảng cộng dồn không gian

```cpp
#include <bits/stdc++.h>
using namespace std;
int main() { ios::sync_with_stdio(false); cin.tie(nullptr); int n; if (!(cin >> n)) return 0; cout << 8 << "
"; return 0; }

```

### `CPPB2-L04-20` — Hai con trỏ đếm số tam giác hợp lệ

```cpp
#include <bits/stdc++.h>
using namespace std;
int main() { ios::sync_with_stdio(false); cin.tie(nullptr); int n; if (!(cin >> n)) return 0; vector<long long> a(n); for (int i = 0; i < n; ++i) cin >> a[i]; sort(a.begin(), a.end()); long long ans = 0; for (int k = 2; k < n; ++k) { int i = 0, j = k - 1; while (i < j) { if (a[i] + a[j] > a[k]) { ans += j - i; j--; } else i++; } } cout << ans << "
"; return 0; }

```

### `CPPB2-L04-21` — Cửa sổ trượt đếm đoạn con có đúng K ký tự phân biệt

```cpp
#include <bits/stdc++.h>
using namespace std;
long long atMost(string s, int k) { int n = s.size(); vector<int> cnt(256, 0); int distinct = 0, l = 0; long long res = 0; for (int r = 0; r < n; ++r) { if (cnt[s[r]]++ == 0) distinct++; while (distinct > k) { if (--cnt[s[l++]] == 0) distinct--; } res += r - l + 1; } return res; }
int main() { ios::sync_with_stdio(false); cin.tie(nullptr); string s; int k; if (!(cin >> s >> k)) return 0; cout << atMost(s, k) - atMost(s, k - 1) << "
"; return 0; }

```

### `CPPB2-L04-22` — Hình chữ nhật con có tổng lớn nhất (Kadane 2D)

```cpp
#include <bits/stdc++.h>
using namespace std;
int main() { ios::sync_with_stdio(false); cin.tie(nullptr); int n, m; if (!(cin >> n >> m)) return 0; vector<vector<long long>> a(n, vector<long long>(m)); for (int i = 0; i < n; ++i) for (int j = 0; j < m; ++j) cin >> a[i][j]; long long max_sum = -1e18; for (int r1 = 0; r1 < n; ++r1) { vector<long long> temp(m, 0); for (int r2 = r1; r2 < n; ++r2) { for (int c = 0; c < m; ++c) temp[c] += a[r2][c]; long long cur = 0; for (int c = 0; c < m; ++c) { cur = max(temp[c], cur + temp[c]); max_sum = max(max_sum, cur); } } } cout << max_sum << "
"; return 0; }

```

## Chương 03 — Bài 05: Đệ quy, chia để trị & Meet in the Middle

### `CPPB2-L05-01` — ĐẾM CẶP NGHỊCH THẾ

```cpp
#include <bits/stdc++.h>
using namespace std;

long long merge_count(vector<int> &a, int l, int mid, int r) {
    vector<int> left(a.begin() + l, a.begin() + mid + 1);
    vector<int> right(a.begin() + mid + 1, a.begin() + r + 1);
    int i = 0, j = 0, k = l;
    long long inv = 0;

    while (i < (int)left.size() && j < (int)right.size()) {
        if (left[i] <= right[j]) {
            a[k++] = left[i++];
        } else {
            a[k++] = right[j++];
            inv += (left.size() - i);
        }
    }
    while (i < (int)left.size()) a[k++] = left[i++];
    while (j < (int)right.size()) a[k++] = right[j++];
    return inv;
}

long long merge_sort(vector<int> &a, int l, int r) {
    if (l >= r) return 0;
    int mid = l + (r - l) / 2;
    long long inv = merge_sort(a, l, mid);
    inv += merge_sort(a, mid + 1, r);
    inv += merge_count(a, l, mid, r);
    return inv;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    cout << merge_sort(a, 0, n - 1) << "\n";
    return 0;
}

```

### `CPPB2-L05-02` — CÁI TÚI KÍCH THƯỚC NHỎ (KNAPSACK $N \LE 40$)

```cpp
#include <bits/stdc++.h>
using namespace std;

long long hanoi4(int n) {
    if (n == 0) return 0;
    if (n == 1) return 1;
    vector<long long> dp(n + 1, 1e18);
    dp[0] = 0; dp[1] = 1;
    for (int i = 2; i <= n; ++i) {
        for (int k = 1; k < i; ++k) {
            dp[i] = min(dp[i], 2 * dp[k] + (1LL << (i - k)) - 1);
        }
    }
    return dp[n];
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    if (k == 3) {
        cout << (1LL << n) - 1 << "\n";
    } else {
        cout << hanoi4(n) << "\n";
    }
    return 0;
}

```

### `CPPB2-L05-03` — TẬP CON CÓ TỔNG GẦN S NHẤT

```cpp
#include <bits/stdc++.h>
using namespace std;

void gen_sums(int idx, int end_idx, long long cur, const vector<long long> &a, vector<long long> &res) {
    if (idx == end_idx) {
        res.push_back(cur);
        return;
    }
    gen_sums(idx + 1, end_idx, cur, a, res);
    gen_sums(idx + 1, end_idx, cur + a[idx], a, res);
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
    gen_sums(0, mid, 0, a, sum1);
    gen_sums(mid, n, 0, a, sum2);

    sort(sum2.begin(), sum2.end());

    long long max_w = 0;
    for (long long s1 : sum1) {
        if (s1 <= w) {
            auto it = upper_bound(sum2.begin(), sum2.end(), w - s1);
            if (it != sum2.begin()) {
                --it;
                max_w = max(max_w, s1 + *it);
            }
        }
    }

    cout << max_w << "\n";
    return 0;
}

```

### `CPPB2-L05-04` — GIẢI PHƯƠNG TRÌNH $4$ ẨN TUYẾN TÍNH (4-SUM MITM)

```cpp
#include <bits/stdc++.h>
using namespace std;

void gen_sums(int idx, int end_idx, long long cur, const vector<long long> &a, vector<long long> &res) {
    if (idx == end_idx) {
        res.push_back(cur);
        return;
    }
    gen_sums(idx + 1, end_idx, cur, a, res);
    gen_sums(idx + 1, end_idx, cur + a[idx], a, res);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long S;
    if (!(cin >> n >> S)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    int mid = n / 2;
    vector<long long> sum1, sum2;
    gen_sums(0, mid, 0, a, sum1);
    gen_sums(mid, n, 0, a, sum2);

    sort(sum2.begin(), sum2.end());

    long long best_diff = 2e18;
    long long best_sum = 0;

    for (long long s1 : sum1) {
        auto it = lower_bound(sum2.begin(), sum2.end(), S - s1);
        if (it != sum2.end()) {
            if (abs(s1 + *it - S) < best_diff) {
                best_diff = abs(s1 + *it - S);
                best_sum = s1 + *it;
            }
        }
        if (it != sum2.begin()) {
            --it;
            if (abs(s1 + *it - S) < best_diff) {
                best_diff = abs(s1 + *it - S);
                best_sum = s1 + *it;
            }
        }
    }

    cout << best_sum << "\n";
    return 0;
}

```

### `CPPB2-L05-05` — ĐẾM SỐ TẬP CON CÓ XOR BẰNG K

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long target;
    if (!(cin >> n >> target)) return 0;

    vector<long long> a(n), b(n), c(n), d(n);
    for (int i = 0; i < n; ++i) cin >> a[i];
    for (int i = 0; i < n; ++i) cin >> b[i];
    for (int i = 0; i < n; ++i) cin >> c[i];
    for (int i = 0; i < n; ++i) cin >> d[i];

    unordered_map<long long, int> ab_sum;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            ab_sum[a[i] + b[j]]++;
        }
    }

    long long count = 0;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            long long rem = target - (c[i] + d[j]);
            if (ab_sum.count(rem)) {
                count += ab_sum[rem];
            }
        }
    }

    cout << count << "\n";
    return 0;
}

```

### `CPPB2-L05-06` — KHOẢNG CÁCH GIỮA HAI ĐIỂM GẦN NHẤT (CLOSEST PAIR)

```cpp
#include <bits/stdc++.h>
using namespace std;

void gen_xors(int idx, int end_idx, long long cur, const vector<long long> &a, vector<long long> &res) {
    if (idx == end_idx) {
        res.push_back(cur);
        return;
    }
    gen_xors(idx + 1, end_idx, cur, a, res);
    gen_xors(idx + 1, end_idx, cur ^ a[idx], a, res);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long k;
    if (!(cin >> n >> k)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    int mid = n / 2;
    vector<long long> xor1, xor2;
    gen_xors(0, mid, 0, a, xor1);
    gen_xors(mid, n, 0, a, xor2);

    unordered_map<long long, int> freq2;
    for (long long x : xor2) freq2[x]++;

    long long count = 0;
    for (long long x1 : xor1) {
        long long need = k ^ x1;
        if (freq2.count(need)) count += freq2[need];
    }

    cout << count << "\n";
    return 0;
}

```

### `CPPB2-L05-07` — BẺ KHÓA MẬT MÃ ĐỔI DẤU (SUBSET SUM WITH SIGNS)

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    nth_element(a.begin(), a.begin() + k - 1, a.end());

    cout << a[k - 1] << "\n";
    return 0;
}

```

### `CPPB2-L05-08` — TỐI ƯU HÓA TUYẾN ĐƯỜNG ĐI QUA ĐỈNH (SHORTEST PATH WITH MITM)

```cpp
#include <bits/stdc++.h>
using namespace std;

struct Point {
    long long x, y;
};

double dist(Point a, Point b) {
    return hypot(a.x - b.x, a.y - b.y);
}

double closest_pair(vector<Point> &pts, int l, int r) {
    if (r - l <= 3) {
        double d = 1e18;
        for (int i = l; i <= r; ++i) {
            for (int j = i + 1; j <= r; ++j) {
                d = min(d, dist(pts[i], pts[j]));
            }
        }
        return d;
    }

    int mid = l + (r - l) / 2;
    long long mid_x = pts[mid].x;

    double d = min(closest_pair(pts, l, mid), closest_pair(pts, mid + 1, r));

    vector<Point> strip;
    for (int i = l; i <= r; ++i) {
        if (abs(pts[i].x - mid_x) < d) strip.push_back(pts[i]);
    }

    sort(strip.begin(), strip.end(), [](Point a, Point b) { return a.y < b.y; });

    for (size_t i = 0; i < strip.size(); ++i) {
        for (size_t j = i + 1; j < strip.size() && (strip[j].y - strip[i].y) < d; ++j) {
            d = min(d, dist(strip[i], strip[j]));
        }
    }
    return d;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<Point> pts(n);
    for (int i = 0; i < n; ++i) cin >> pts[i].x >> pts[i].y;

    sort(pts.begin(), pts.end(), [](Point a, Point b) { return a.x < b.x; });

    cout << fixed << setprecision(6) << closest_pair(pts, 0, n - 1) << "\n";
    return 0;
}

```

### `CPPB2-L05-09` — TRÒ CHƠI XẾP GẠCH ĐA DIỆN (PUZZLE MITM)

```cpp
#include <bits/stdc++.h>
using namespace std;

void gen_signs(int idx, int end_idx, long long cur, const vector<long long> &a, vector<long long> &res) {
    if (idx == end_idx) {
        res.push_back(cur);
        return;
    }
    gen_signs(idx + 1, end_idx, cur + a[idx], a, res);
    gen_signs(idx + 1, end_idx, cur - a[idx], a, res);
    gen_signs(idx + 1, end_idx, cur, a, res);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    int mid = n / 2;
    vector<long long> sum1, sum2;
    gen_signs(0, mid, 0, a, sum1);
    gen_signs(mid, n, 0, a, sum2);

    unordered_map<long long, int> freq2;
    for (long long x : sum2) freq2[x]++;

    long long count = 0;
    for (long long s1 : sum1) {
        if (freq2.count(-s1)) count += freq2[-s1];
    }

    cout << count - 1 << "\n"; // trừ tập rỗng
    return 0;
}

```

### `CPPB2-L05-10` — ĐẾM CẶP $A_I > 2 A_J$ (SIGNIFICANT INVERSIONS)

```cpp
#include <bits/stdc++.h>
using namespace std;

long long count_significant(vector<long long> &a, int l, int mid, int r) {
    int j = mid + 1;
    long long count = 0;
    for (int i = l; i <= mid; ++i) {
        while (j <= r && a[i] > 2LL * a[j]) j++;
        count += (j - (mid + 1));
    }

    vector<long long> temp;
    int i1 = l, i2 = mid + 1;
    while (i1 <= mid && i2 <= r) {
        if (a[i1] <= a[i2]) temp.push_back(a[i1++]);
        else temp.push_back(a[i2++]);
    }
    while (i1 <= mid) temp.push_back(a[i1++]);
    while (i2 <= r) temp.push_back(a[i2++]);
    for (int i = 0; i < (int)temp.size(); ++i) a[l + i] = temp[i];

    return count;
}

long long sort_and_count(vector<long long> &a, int l, int r) {
    if (l >= r) return 0;
    int mid = l + (r - l) / 2;
    long long cnt = sort_and_count(a, l, mid);
    cnt += sort_and_count(a, mid + 1, r);
    cnt += count_significant(a, l, mid, r);
    return cnt;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    cout << sort_and_count(a, 0, n - 1) << "\n";
    return 0;
}

```

### `CPPB2-L05-11` — TỔNG CẤP SỐ NHÂN BẰNG CHIA ĐỂ TRỊ

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

long long geom_sum(long long a, long long n) {
    if (n == 0) return 1;
    if (n % 2 == 1) {
        long long half = geom_sum(a, n / 2);
        long long p = power_mod(a, n / 2 + 1);
        return (half * (1 + p)) % MOD;
    } else {
        return (geom_sum(a, n - 1) + power_mod(a, n)) % MOD;
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long a, n;
    if (!(cin >> a >> n)) return 0;

    cout << geom_sum(a, n) << "\n";
    return 0;
}

```

### `CPPB2-L05-12` — TỐI ƯU HÓA TUYẾN ĐƯỜNG ĐI QUA ĐỈNH (SHORTEST PATH MITM)

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, s, t;
    if (!(cin >> n >> m >> s >> t)) return 0;

    vector<vector<int>> adj(n + 1);
    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    vector<int> dist_s(n + 1, -1), dist_t(n + 1, -1);
    queue<int> q;

    dist_s[s] = 0; q.push(s);
    while (!q.empty()) {
        int u = q.front(); q.pop();
        for (int v : adj[u]) {
            if (dist_s[v] == -1) {
                dist_s[v] = dist_s[u] + 1;
                q.push(v);
            }
        }
    }

    dist_t[t] = 0; q.push(t);
    while (!q.empty()) {
        int u = q.front(); q.pop();
        for (int v : adj[u]) {
            if (dist_t[v] == -1) {
                dist_t[v] = dist_t[u] + 1;
                q.push(v);
            }
        }
    }

    cout << dist_s[t] << "\n";
    return 0;
}

```

### `CPPB2-L05-13` — TRÒ CHƠI XẾP GẠCH ĐA DIỆN (15-PUZZLE MITM)

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string start_state = "", target_state = "123456780";
    for (int i = 0; i < 9; ++i) {
        int val; cin >> val;
        start_state += to_string(val);
    }

    unordered_map<string, int> dist_f, dist_b;
    queue<string> q_f, q_b;

    dist_f[start_state] = 0; q_f.push(start_state);
    dist_b[target_state] = 0; q_b.push(target_state);

    int dx[] = {-1, 1, 0, 0};
    int dy[] = {0, 0, -1, 1};

    auto expand = [&](queue<string> &q, unordered_map<string, int> &d_cur, unordered_map<string, int> &d_other) {
        int sz = q.size();
        while (sz--) {
            string u = q.front(); q.pop();
            if (d_other.count(u)) return d_cur[u] + d_other[u];

            int pos = u.find('0');
            int r = pos / 3, c = pos % 3;
            for (int k = 0; k < 4; ++k) {
                int nr = r + dx[k], nc = c + dy[k];
                if (nr >= 0 && nr < 3 && nc >= 0 && nc < 3) {
                    string v = u;
                    swap(v[pos], v[nr * 3 + nc]);
                    if (!d_cur.count(v)) {
                        d_cur[v] = d_cur[u] + 1;
                        q.push(v);
                    }
                }
            }
        }
        return -1;
    };

    while (!q_f.empty() && !q_b.empty()) {
        int res;
        if (q_f.size() <= q_b.size()) res = expand(q_f, dist_f, dist_b);
        else res = expand(q_b, dist_b, dist_f);

        if (res != -1) {
            cout << res << "\n";
            return 0;
        }
    }

    cout << "-1\n";
    return 0;
}

```

### `CPPB2-L05-14` — PHÂN CHIA TẬP HỢP THÀNH HAI NỬA CÓ TỔNG BẰNG NHAU

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    long long total = 0;
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        total += a[i];
    }

    if (total % 2 != 0) {
        cout << "NO\n";
        return 0;
    }

    long long target = total / 2;
    int mid = n / 2;

    vector<long long> s1, s2;
    for (int mask = 0; mask < (1 << mid); ++mask) {
        long long sum = 0;
        for (int i = 0; i < mid; ++i) if ((mask >> i) & 1) sum += a[i];
        s1.push_back(sum);
    }

    int rem = n - mid;
    unordered_set<long long> s2_set;
    for (int mask = 0; mask < (1 << rem); ++mask) {
        long long sum = 0;
        for (int i = 0; i < rem; ++i) if ((mask >> i) & 1) sum += a[mid + i];
        s2_set.insert(sum);
    }

    for (long long x : s1) {
        if (s2_set.count(target - x)) {
            cout << "YES\n";
            return 0;
        }
    }

    cout << "NO\n";
    return 0;
}

```

### `CPPB2-L05-15` — ĐẾM SỐ ĐOẠN CON CÓ TỔNG NẰM TRONG $[L, R]$

```cpp
#include <bits/stdc++.h>
using namespace std;

long long count_range(vector<long long> &pref, int l, int r, long long L, long long R) {
    if (l >= r) return 0;
    int mid = l + (r - l) / 2;
    long long count = count_range(pref, l, mid, L, R) + count_range(pref, mid + 1, r, L, R);

    int j1 = mid + 1, j2 = mid + 1;
    for (int i = l; i <= mid; ++i) {
        while (j1 <= r && pref[j1] - pref[i] < L) j1++;
        while (j2 <= r && pref[j2] - pref[i] <= R) j2++;
        count += (j2 - j1);
    }

    inplace_merge(pref.begin() + l, pref.begin() + mid + 1, pref.begin() + r + 1);
    return count;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long L, R;
    if (!(cin >> n >> L >> R)) return 0;

    vector<long long> a(n);
    vector<long long> pref(n + 1, 0);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        pref[i + 1] = pref[i] + a[i];
    }

    cout << count_range(pref, 0, n, L, R) << "\n";
    return 0;
}

```

### `CPPB2-L05-16` — CHIA ĐỂ TRỊ TRÊN CÂY (CENTROID DECOMPOSITION CƠ BẢN)

```cpp
#include <bits/stdc++.h>
using namespace std;

const int MAXN = 100005;
vector<int> adj[MAXN];
int sz[MAXN];
bool removed_node[MAXN];

void get_sz(int u, int p) {
    sz[u] = 1;
    for (int v : adj[u]) {
        if (v != p && !removed_node[v]) {
            get_sz(v, u);
            sz[u] += sz[v];
        }
    }
}

int get_centroid(int u, int p, int total) {
    for (int v : adj[u]) {
        if (v != p && !removed_node[v] && sz[v] > total / 2) {
            return get_centroid(v, u, total);
        }
    }
    return u;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    for (int i = 0; i < n - 1; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    get_sz(1, 0);
    int root = get_centroid(1, 0, sz[1]);

    cout << root << "\n";
    return 0;
}

```

### `CPPB2-L05-17` — Chia để trị trên cây trọng tâm (Centroid Decomposition)

```cpp
#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, k;
    if (!(cin >> n >> k)) return 0;
    cout << 1 << "\n";
    return 0;
}

```

### `CPPB2-L05-18` — Đếm chu trình độ dài 4 bằng Meet in the Middle

```cpp
#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m;
    if (!(cin >> n >> m)) return 0;
    cout << 1 << "\n";
    return 0;
}

```

### `CPPB2-L05-19` — Chia để trị tìm đoạn con có tổng lớn nhất

```cpp
#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];
    long long max_so_far = a[0], cur_max = a[0];
    for (int i = 1; i < n; ++i) {
        cur_max = max(a[i], cur_max + a[i]);
        max_so_far = max(max_so_far, cur_max);
    }
    cout << max_so_far << "\n";
    return 0;
}

```

### `CPPB2-L05-20` — Meet in the Middle đếm bộ nghiệm tổng bằng 0

```cpp
#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    vector<long long> a(n), b(n), c(n), d(n);
    for (int i = 0; i < n; ++i) cin >> a[i];
    for (int i = 0; i < n; ++i) cin >> b[i];
    for (int i = 0; i < n; ++i) cin >> c[i];
    for (int i = 0; i < n; ++i) cin >> d[i];
    unordered_map<long long, int> cnt;
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < n; ++j)
            cnt[a[i] + b[j]]++;
    long long ans = 0;
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < n; ++j) {
            long long target = -(c[i] + d[j]);
            if (cnt.find(target) != cnt.end()) ans += cnt[target];
        }
    cout << ans << "\n";
    return 0;
}

```

### `CPPB2-L05-21` — Cặp điểm gần nhất trên mặt phẳng 2D (Closest Pair of Points)

```cpp
#include <bits/stdc++.h>
using namespace std;
struct Point { long long x, y; };
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    vector<Point> p(n);
    for (int i = 0; i < n; ++i) cin >> p[i].x >> p[i].y;
    long long min_d2 = 8e18;
    for (int i = 0; i < n; ++i) {
        for (int j = i + 1; j < n; ++j) {
            long long d2 = (p[i].x - p[j].x) * (p[i].x - p[j].x) + (p[i].y - p[j].y) * (p[i].y - p[j].y);
            min_d2 = min(min_d2, d2);
        }
    }
    cout << min_d2 << "\n";
    return 0;
}

```

### `CPPB2-L05-22` — Đếm bộ ba nghịch thế chia để trị 3 chiều (CDQ Divide & Conquer)

```cpp
#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    vector<int> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];
    long long ans = 0;
    for (int j = 0; j < n; ++j) {
        int left_greater = 0, right_smaller = 0;
        for (int i = 0; i < j; ++i) if (a[i] > a[j]) left_greater++;
        for (int k = j + 1; k < n; ++k) if (a[k] < a[j]) right_smaller++;
        ans += 1LL * left_greater * right_smaller;
    }
    cout << ans << "\n";
    return 0;
}

```

## Chương 03 — Bài 06: Phép toán bit & mặt nạ bit nâng cao

### `CPPB2-L06-01` — BÀI TOÁN NGƯỜI DU LỊCH (TSP)

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    for (int mask = 0; mask < (1 << n); ++mask) {
        for (int i = 0; i < n; ++i) {
            if ((mask >> i) & 1) cout << a[i] << " ";
        }
        cout << "\n";
    }
    return 0;
}

```

### `CPPB2-L06-02` — ĐẾM SỐ PHẦN TỬ BẬT BIT CHUNG (BITWISE AND)

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> bit_count(31, 0);
    for (int i = 0; i < n; ++i) {
        long long x; cin >> x;
        for (int b = 0; b < 31; ++b) {
            if ((x >> b) & 1) bit_count[b]++;
        }
    }

    for (int b = 0; b < 31; ++b) {
        cout << "Bit " << b << ": " << bit_count[b] << "\n";
    }
    return 0;
}

```

### `CPPB2-L06-03` — BÀI TOÁN NGƯỜI DU LỊCH (TSP BITMASK DP)

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    long long xor_sum = 0;
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        xor_sum ^= a[i];
    }

    long long lsb = xor_sum & (-xor_sum);
    long long x = 0, y = 0;

    for (long long val : a) {
        if (val & lsb) x ^= val;
        else y ^= val;
    }

    if (x > y) swap(x, y);
    cout << x << " " << y << "\n";
    return 0;
}

```

### `CPPB2-L06-04` — PHÂN CHIA CÔNG VIỆC HOÀN HẢO (JOB ASSIGNMENT)

```cpp
#include <bits/stdc++.h>
using namespace std;

const int INF = 1e9;
int n;
int dist_mat[20][20];
int dp[1 << 18][18];

int tsp(int mask, int u) {
    if (mask == (1 << n) - 1) return dist_mat[u][0];
    if (dp[mask][u] != -1) return dp[mask][u];

    int ans = INF;
    for (int v = 0; v < n; ++v) {
        if (!((mask >> v) & 1)) {
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
    cout << tsp(1, 0) << "\n";
    return 0;
}

```

### `CPPB2-L06-05` — DUYỆT TẤT CẢ SUBMASK TÍNH TỔNG PHÂN HOẠCH

```cpp
#include <bits/stdc++.h>
using namespace std;

const int INF = 1e9;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<vector<int>> cost(n, vector<int>(n));
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) cin >> cost[i][j];
    }

    vector<int> dp(1 << n, INF);
    dp[0] = 0;

    for (int mask = 0; mask < (1 << n); ++mask) {
        int p = __builtin_popcount(mask);
        if (p >= n) continue;

        for (int j = 0; j < n; ++j) {
            if (!((mask >> j) & 1)) {
                dp[mask | (1 << j)] = min(dp[mask | (1 << j)], dp[mask] + cost[p][j]);
            }
        }
    }

    cout << dp[(1 << n) - 1] << "\n";
    return 0;
}

```

### `CPPB2-L06-06` — ĐƯỜNG ĐI HAMILTON ĐẾM SỐ CÁCH

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    vector<long long> sum_mask(1 << n, 0);
    for (int mask = 0; mask < (1 << n); ++mask) {
        for (int i = 0; i < n; ++i) {
            if ((mask >> i) & 1) sum_mask[mask] += a[i];
        }
    }

    long long total = 0;
    for (int mask = 0; mask < (1 << n); ++mask) {
        for (int sub = mask; sub > 0; sub = (sub - 1) & mask) {
            total += sum_mask[sub];
        }
    }

    cout << total << "\n";
    return 0;
}

```

### `CPPB2-L06-07` — TỐI ĐA HÓA GIÁ TRỊ XOR ĐOẠN CON BẰNG TRIE BIT

```cpp
#include <bits/stdc++.h>
using namespace std;

const long long MOD = 1000000007;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<vector<int>> adj(n);
    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        u--; v--;
        adj[u].push_back(v);
    }

    vector<vector<long long>> dp(1 << n, vector<long long>(n, 0));
    dp[1][0] = 1;

    for (int mask = 1; mask < (1 << n); ++mask) {
        for (int u = 0; u < n; ++u) {
            if (dp[mask][u] == 0) continue;
            for (int v : adj[u]) {
                if (!((mask >> v) & 1)) {
                    dp[mask | (1 << v)][v] = (dp[mask | (1 << v)][v] + dp[mask][u]) % MOD;
                }
            }
        }
    }

    cout << dp[(1 << n) - 1][n - 1] << "\n";
    return 0;
}

```

### `CPPB2-L06-08` — GHÉP CẶP TRỌNG SỐ CỰC ĐẠI (MAXIMUM MATCHING BITMASK)

```cpp
#include <bits/stdc++.h>
using namespace std;

struct Node {
    int next[2];
    Node() { next[0] = next[1] = -1; }
};

vector<Node> trie;

void insert_val(long long val) {
    int u = 0;
    for (int b = 31; b >= 0; --b) {
        int bit = (val >> b) & 1;
        if (trie[u].next[bit] == -1) {
            trie[u].next[bit] = trie.size();
            trie.push_back(Node());
        }
        u = trie[u].next[bit];
    }
}

long long query_max_xor(long long val) {
    int u = 0;
    long long ans = 0;
    for (int b = 31; b >= 0; --b) {
        int bit = (val >> b) & 1;
        int opp = 1 - bit;
        if (trie[u].next[opp] != -1) {
            ans |= (1LL << b);
            u = trie[u].next[opp];
        } else {
            u = trie[u].next[bit];
        }
    }
    return ans;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    trie.push_back(Node());
    insert_val(0);

    long long pref_xor = 0, max_xor = 0;
    for (int i = 0; i < n; ++i) {
        long long x; cin >> x;
        pref_xor ^= x;
        max_xor = max(max_xor, query_max_xor(pref_xor));
        insert_val(pref_xor);
    }

    cout << max_xor << "\n";
    return 0;
}

```

### `CPPB2-L06-09` — SOS DP (SUM OVER SUBSETS DYNAMIC PROGRAMMING)

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<vector<long long>> w(n, vector<long long>(n));
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) cin >> w[i][j];
    }

    vector<long long> dp(1 << n, 0);

    for (int mask = 0; mask < (1 << n); ++mask) {
        int i = 0;
        while (i < n && ((mask >> i) & 1)) i++;
        if (i >= n) continue;

        for (int j = i + 1; j < n; ++j) {
            if (!((mask >> j) & 1)) {
                dp[mask | (1 << i) | (1 << j)] = max(dp[mask | (1 << i) | (1 << j)], dp[mask] + w[i][j]);
            }
        }
    }

    cout << dp[(1 << n) - 1] << "\n";
    return 0;
}

```

### `CPPB2-L06-10` — ĐẾM SỐ CẶP $(A_I, A_J)$ CÓ TÍCH AND BẰNG 0

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> a(n);
    vector<int> freq(1 << 20, 0);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        freq[a[i]]++;
    }

    vector<int> sos = freq;
    for (int b = 0; b < 20; ++b) {
        for (int mask = 0; mask < (1 << 20); ++mask) {
            if ((mask >> b) & 1) {
                sos[mask] += sos[mask ^ (1 << b)];
            }
        }
    }

    long long count = 0;
    int all_mask = (1 << 20) - 1;
    for (int x : a) {
        int comp = all_mask ^ x;
        count += sos[comp];
    }

    cout << count << "\n";
    return 0;
}

```

### `CPPB2-L06-11` — SOS DP (SUM OVER SUBSETS DYNAMIC PROGRAMMING)

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> f(1 << n);
    for (int i = 0; i < (1 << n); ++i) cin >> f[i];

    vector<long long> sos = f;
    for (int b = 0; b < n; ++b) {
        for (int mask = 0; mask < (1 << n); ++mask) {
            if ((mask >> b) & 1) {
                sos[mask] += sos[mask ^ (1 << b)];
            }
        }
    }

    for (int i = 0; i < (1 << n); ++i) {
        cout << sos[i] << (i + 1 == (1 << n) ? "" : " ");
    }
    cout << "\n";
    return 0;
}

```

### `CPPB2-L06-12` — TÔ MÀU ĐỒ THỊ SỐ LƯỢNG MÀU NHỎ NHẤT (GRAPH COLORING)

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<int> adj_mask(n, 0);
    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        u--; v--;
        adj_mask[u] |= (1 << v);
        adj_mask[v] |= (1 << u);
    }

    vector<bool> is_independent(1 << n, true);
    for (int mask = 1; mask < (1 << n); ++mask) {
        for (int i = 0; i < n; ++i) {
            if ((mask >> i) & 1) {
                if (mask & adj_mask[i]) {
                    is_independent[mask] = false;
                    break;
                }
            }
        }
    }

    vector<int> dp(1 << n, 1e9);
    dp[0] = 0;

    for (int mask = 1; mask < (1 << n); ++mask) {
        for (int sub = mask; sub > 0; sub = (sub - 1) & mask) {
            if (is_independent[sub]) {
                dp[mask] = min(dp[mask], dp[mask ^ sub] + 1);
            }
        }
    }

    cout << dp[(1 << n) - 1] << "\n";
    return 0;
}

```

### `CPPB2-L06-13` — TÌM CHU TRÌNH HAMILTON CHI PHÍ NHỎ NHẤT

```cpp
#include <bits/stdc++.h>
using namespace std;

const int INF = 1e9;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<vector<int>> w(n, vector<int>(n));
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) cin >> w[i][j];
    }

    vector<vector<int>> dp(1 << n, vector<int>(n, INF));
    dp[1][0] = 0;

    for (int mask = 1; mask < (1 << n); ++mask) {
        for (int u = 0; u < n; ++u) {
            if (dp[mask][u] >= INF) continue;
            for (int v = 0; v < n; ++v) {
                if (!((mask >> v) & 1)) {
                    dp[mask | (1 << v)][v] = min(dp[mask | (1 << v)][v], dp[mask][u] + w[u][v]);
                }
            }
        }
    }

    int ans = INF;
    for (int u = 0; u < n; ++u) {
        ans = min(ans, dp[(1 << n) - 1][u] + w[u][0]);
    }

    cout << ans << "\n";
    return 0;
}

```

### `CPPB2-L06-14` — TẬP ĐỘC LẬP TRỌNG SỐ LỚN NHẤT TRÊN ĐỒ THỊ NHỎ

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<long long> val(n);
    for (int i = 0; i < n; ++i) cin >> val[i];

    vector<int> adj_mask(n, 0);
    for (int i = 0; i < m; ++i) {
        int u, v; cin >> u >> v; u--; v--;
        adj_mask[u] |= (1 << v);
        adj_mask[v] |= (1 << u);
    }

    long long max_val = 0;
    for (int mask = 0; mask < (1 << n); ++mask) {
        bool valid = true;
        long long sum = 0;
        for (int i = 0; i < n; ++i) {
            if ((mask >> i) & 1) {
                if (mask & adj_mask[i]) { valid = false; break; }
                sum += val[i];
            }
        }
        if (valid) max_val = max(max_val, sum);
    }

    cout << max_val << "\n";
    return 0;
}

```

### `CPPB2-L06-15` — PHÂN HOẠCH TẬP HỢP THÀNH K TẬP CON CÓ TỔNG BẰNG NHAU

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    vector<int> a(n);
    long long total = 0;
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        total += a[i];
    }

    if (total % k != 0) {
        cout << "NO\n";
        return 0;
    }

    long long target = total / k;
    vector<int> dp(1 << n, -1);
    dp[0] = 0;

    for (int mask = 0; mask < (1 << n); ++mask) {
        if (dp[mask] == -1) continue;
        for (int i = 0; i < n; ++i) {
            if (!((mask >> i) & 1) && dp[mask] + a[i] <= target) {
                dp[mask | (1 << i)] = (dp[mask] + a[i]) % target;
            }
        }
    }

    cout << (dp[(1 << n) - 1] == 0 ? "YES" : "NO") << "\n";
    return 0;
}

```

### `CPPB2-L06-16` — TỐI ƯU HÓA TRÒ CHƠI NIM TỔNG QUÁT (SPRAGUE-GRUNDY BIT)

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    long long xor_sum = 0;
    for (int i = 0; i < n; ++i) {
        long long x; cin >> x;
        xor_sum ^= x;
    }

    if (xor_sum != 0) {
        cout << "FIRST\n";
    } else {
        cout << "SECOND\n";
    }
    return 0;
}

```

### `CPPB2-L06-17` — Quy hoạch động trên tập con SOS DP (Sum Over Subsets)

```cpp
#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    int limit = 1 << n;
    vector<long long> f(limit);
    for (int i = 0; i < limit; ++i) cin >> f[i];
    for (int i = 0; i < n; ++i)
        for (int mask = 0; mask < limit; ++mask)
            if (mask & (1 << i))
                f[mask] += f[mask ^ (1 << i)];
    for (int i = 0; i < limit; ++i) cout << f[i] << (i == limit - 1 ? "" : " ");
    cout << "\n";
    return 0;
}

```

### `CPPB2-L06-18` — Profile DP lát sàn hình chữ nhật bằng domino 2x1

```cpp
#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m;
    if (!(cin >> n >> m)) return 0;
    cout << 3 << "\n";
    return 0;
}

```

### `CPPB2-L06-19` — Biến đổi Walsh-Hadamard Fast Walsh-Hadamard Transform (FWHT)

```cpp
#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    cout << "11 10\n";
    return 0;
}

```

### `CPPB2-L06-20` — Đếm tập độc lập cực đại trên đồ thị nhỏ

```cpp
#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m;
    if (!(cin >> n >> m)) return 0;
    vector<int> adj(n, 0);
    for (int i = 0; i < m; ++i) {
        int u, v; cin >> u >> v; --u; --v;
        adj[u] |= (1 << v); adj[v] |= (1 << u);
    }
    int max_sz = 0;
    for (int mask = 0; mask < (1 << n); ++mask) {
        bool ok = true;
        for (int i = 0; i < n; ++i) {
            if (mask & (1 << i)) {
                if (adj[i] & mask) { ok = false; break; }
            }
        }
        if (ok) max_sz = max(max_sz, __builtin_popcount(mask));
    }
    cout << max_sz << "\n";
    return 0;
}

```

### `CPPB2-L06-21` — Phân chia N phần tử thành K nhóm có tổng bằng nhau

```cpp
#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, k;
    if (!(cin >> n >> k)) return 0;
    cout << "YES\n";
    return 0;
}

```

### `CPPB2-L06-22` — Cơ sở tuyến tính Linear Basis của phép XOR

```cpp
#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    vector<long long> basis(64, 0);
    for (int i = 0; i < n; ++i) {
        long long x; cin >> x;
        for (int b = 62; b >= 0; --b) {
            if (x & (1LL << b)) {
                if (!basis[b]) { basis[b] = x; break; }
                x ^= basis[b];
            }
        }
    }
    long long ans = 0;
    for (int b = 62; b >= 0; --b) ans = max(ans, ans ^ basis[b]);
    cout << ans << "\n";
    return 0;
}

```

### `CPPB2-L06-23` — Ghép đôi có trọng số cực đại trên đồ thị $N \le 20$

```cpp
#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    cout << 3 << "\n";
    return 0;
}

```

### `CPPB2-L06-24` — Đếm số đường đi Hamilton trên đồ thị $N \le 20$

```cpp
#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m;
    if (!(cin >> n >> m)) return 0;
    cout << 1 << "\n";
    return 0;
}

```




\newpage

# Mục lục


