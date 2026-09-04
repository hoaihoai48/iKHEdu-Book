---
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


### Bài 01 [CPPB2-L01-01]: Ước chung & bội chung cơ bản

**Bối cảnh & Nhiệm vụ:**

Trong các kỳ thi lập trình thi đấu, việc tìm **Ước chung lớn nhất ($\gcd$)** và **Bội chung nhỏ nhất ($\text{lcm}$)** là một trong những khối xử lý cơ sở nền tảng nhất. Tuy nhiên, khi các số đầu vào có giá trị lớn (lên tới $10^9$), việc tính toán bất cẩn phép nhân trong $\text{lcm}$ rất dễ dẫn đến lỗi tràn số nguyên 64-bit (`long long`).

Cho $T$ bộ dữ liệu, mỗi bộ gồm hai số nguyên dương $A$ và $B$.

**Bối cảnh & Nhiệm vụ:**

Nhiệm vụ của bạn là tính và in ra $\gcd(A, B)$ và $\text{lcm}(A, B)$.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số nguyên dương $T$ ($1 \le T \le 10^5$) — số lượng bộ dữ liệu cần xử lý.
- $T$ dòng tiếp theo, mỗi dòng chứa hai số nguyên dương $A$ và $B$ ($1 \le A, B \le 10^9$), cách nhau bởi một dấu cách.

**Đầu ra (Output):**

- Gồm $T$ dòng, mỗi dòng in ra hai số nguyên cách nhau bởi một dấu cách: số đầu tiên là $\gcd(A, B)$, số thứ hai là $\text{lcm}(A, B)$.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>3<br/>12 18<br/>6 9<br/>1000000000 1000000000<br/>``` | ```text<br/>6 36<br/>3 18<br/>1000000000 1000000000<br/>``` |

**Giải thích:**

* Với cặp $(12, 18)$: $\gcd(12, 18) = 6$, $\text{lcm}(12, 18) = \frac{12}{6} \times 18 = 36$.

* Với cặp $(6, 9)$: $\gcd(6, 9) = 3$, $\text{lcm}(6, 9) = \frac{6}{3} \times 9 = 18$.

* Với cặp $(10^9, 10^9)$: $\gcd = 10^9, \text{lcm} = 10^9$.



### Bài 02 [CPPB2-L01-02]: Rút gọn mảng phân số lớn

**Bối cảnh & Nhiệm vụ:**

Trong toán học và lập trình thi đấu, việc chuẩn hóa phân số về dạng **tối giản** là thao tác then chốt để so sánh và tính toán chính xác mà không gặp sai số dấu phẩy động (`floating-point error`).

Một phân số $\frac{A}{B}$ được gọi là tối giản chuẩn khi:
1. $\gcd(|P|, |Q|) = 1$ với phân số tối giản $\frac{P}{Q}$.
2. Mẫu số luôn dương: $Q > 0$. Nếu phân số âm, dấu âm phải được đặt ở tử số ($P < 0$).
3. Nếu tử số bằng $0$, phân số tối giản luôn biểu diễn là `0 1`.

Cho $N$ phân số, mỗi phân số có dạng $\frac{A_i}{B_i}$ ($B_i \ne 0$). Hãy rút gọn từng phân số về dạng tối giản chuẩn.

**Bối cảnh & Nhiệm vụ:**

Cho $N$ phân số $A_i/B_i$. Hãy lập trình rút gọn mỗi phân số về dạng tối giản chuẩn: mẫu số dương, tử và mẫu nguyên tố cùng nhau, riêng phân số $0$ luôn viết thành `0 1`.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số nguyên dương $N$ ($1 \le N \le 10^5$) — số lượng phân số cần rút gọn.
- $N$ dòng tiếp theo, mỗi dòng chứa hai số nguyên $A_i$ và $B_i$ ($-10^9 \le A_i \le 10^9$, $1 \le |B_i| \le 10^9$, $B_i \ne 0$), cách nhau bởi một dấu cách.

**Đầu ra (Output):**

- Gồm $N$ dòng, mỗi dòng in ra hai số nguyên $P_i$ và $Q_i$ cách nhau bởi một dấu cách, biểu diễn phân số tối giản $\frac{P_i}{Q_i}$ tương ứng ($Q_i > 0$).

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>4<br/>12 18<br/>-6 8<br/>15 -25<br/>0 -100<br/>``` | ```text<br/>2 3<br/>-3 4<br/>-3 5<br/>0 1<br/>``` |

**Giải thích:**

* $\frac{12}{18}$: $\gcd(12, 18) = 6 \implies \frac{12/6}{18/6} = \frac{2}{3}$.

* $\frac{-6}{8}$: $\gcd(6, 8) = 2 \implies \frac{-6/2}{8/2} = \frac{-3}{4}$.

* $\frac{15}{-25}$: $\gcd(15, 25) = 5 \implies \frac{15/5}{-25/5} = \frac{3}{-5} \implies$ chuẩn hóa mẫu dương thành $\frac{-3}{5}$.

* $\frac{0}{-100}$: chuẩn hóa thành `0 1`.



### Bài 03 [CPPB2-L01-03]: Sàng ước số nguyên tố nhỏ nhất (SPF)

**Bối cảnh & Nhiệm vụ:**

Trong các bài toán xử lý số học nhiều truy vấn, việc tìm **ước số nguyên tố nhỏ nhất** ($\text{Smallest Prime Factor} - \text{SPF}$) của một số là bước tiền xử lý nền tảng giúp phân tích thừa số nguyên tố, đếm ước số, tính hàm nhân tính và tìm các số nguyên tố cùng nhau trong thời gian logarit $\mathcal{O}(\log N)$.

Cho $Q$ truy vấn, mỗi truy vấn gồm một số nguyên dương $X$ ($2 \le X \le 10^6$). Hãy tìm ước số nguyên tố nhỏ nhất của $X$ (ký hiệu là $\text{spf}[X]$).

**Bối cảnh & Nhiệm vụ:**

Cho $Q$ truy vấn, mỗi truy vấn gồm một số nguyên dương $X$. Hãy lập trình tìm ước số nguyên tố nhỏ nhất $\text{spf}[X]$ của mỗi số.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số nguyên dương $Q$ ($1 \le Q \le 10^6$) — số lượng truy vấn.
- $Q$ dòng tiếp theo, mỗi dòng chứa một số nguyên dương $X$ ($2 \le X \le 10^6$).

**Đầu ra (Output):**

- Gồm $Q$ dòng, mỗi dòng in ra ước số nguyên tố nhỏ nhất $\text{spf}[X]$ của số $X$ tương ứng.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>5<br/>2<br/>9<br/>15<br/>84<br/>999983<br/>``` | ```text<br/>2<br/>3<br/>3<br/>2<br/>999983<br/>``` |

**Giải thích:**

* $X = 2$: là số nguyên tố $\implies \text{spf}[2] = 2$.

* $X = 9 = 3^2 \implies \text{spf}[9] = 3$.

* $X = 15 = 3 \times 5 \implies \text{spf}[15] = 3$.

* $X = 84 = 2^2 \times 3 \times 7 \implies \text{spf}[84] = 2$.

* $X = 999983$: là số nguyên tố $\implies \text{spf}[999983] = 999983$.



### Bài 04 [CPPB2-L01-04]: Phân tích thừa số truy vấn nhanh

**Bối cảnh & Nhiệm vụ:**

Phân tích một số nguyên dương $N$ thành tích các thừa số nguyên tố:
$$N = p_1^{a_1} \cdot p_2^{a_2} \cdots p_k^{a_k} \quad (p_1 < p_2 < \dots < p_k, a_i \ge 1)$$
là thao tác kinh điển trong số học. Khi cần phân tích số lượng lớn các số ($Q = 10^5$), thuật toán thử chia $\mathcal{O}(\sqrt{N})$ cho từng số sẽ bị quá thời gian. Việc áp dụng mảng **Sàng ước số nguyên tố nhỏ nhất (SPF)** cho phép phân tích mỗi số chỉ trong thời gian $\mathcal{O}(\log N)$.

Cho $Q$ truy vấn, mỗi truy vấn gồm một số nguyên dương $N$ ($2 \le N \le 10^6$). Hãy in ra dạng phân tích thừa số nguyên tố của $N$.

**Bối cảnh & Nhiệm vụ:**

Cho $Q$ truy vấn, mỗi truy vấn gồm một số nguyên dương $N$. Hãy lập trình in ra dạng phân tích thừa số nguyên tố của $N$ dưới dạng `p^a`, các thừa số xếp theo thứ tự tăng dần.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số nguyên dương $Q$ ($1 \le Q \le 10^5$) — số lượng truy vấn.
- $Q$ dòng tiếp theo, mỗi dòng chứa một số nguyên dương $N$ ($2 \le N \le 10^6$).

**Đầu ra (Output):**

- Gồm $Q$ dòng, mỗi dòng in ra dạng phân tích của $N$. Mỗi thừa số nguyên tố và số mũ được in dưới dạng `p^a`, các cặp thừa số cách nhau bởi một dấu cách theo thứ tự các số nguyên tố tăng dần.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>4<br/>12<br/>84<br/>13<br/>1000000<br/>``` | ```text<br/>2^2 3^1<br/>2^2 3^1 7^1<br/>13^1<br/>2^6 5^6<br/>``` |

**Giải thích:**

* $12 = 2^2 \times 3^1$.

* $84 = 2^2 \times 3^1 \times 7^1$.

* $13 = 13^1$.

* $1000000 = 10^6 = 2^6 \times 5^6$.



### Bài 05 [CPPB2-L01-05]: Đếm ước số & tổng ước số nhanh

**Bối cảnh & Nhiệm vụ:**

Cho $Q$ truy vấn, mỗi truy vấn gồm một số nguyên dương $N$ ($2 \le N \le 10^6$). Với mỗi $N$, hãy tính:
1. **Số lượng ước số** $d(N)$ — tổng số ước dương của $N$.
2. **Tổng các ước số** $\sigma(N)$ — tổng tất cả các ước dương của $N$.

Sử dụng phân tích thừa số nguyên tố qua mảng SPF: nếu $N = p_1^{a_1} \cdot p_2^{a_2} \cdots p_k^{a_k}$ thì:
$$d(N) = \prod_{i=1}^k (a_i + 1) \qquad \sigma(N) = \prod_{i=1}^k \frac{p_i^{a_i + 1} - 1}{p_i - 1}$$

**Bối cảnh & Nhiệm vụ:**

Cho $Q$ truy vấn, mỗi truy vấn gồm một số nguyên dương $N$. Hãy lập trình tính số lượng ước $d(N)$ và tổng các ước $\sigma(N)$ của mỗi số.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số nguyên dương $Q$ ($1 \le Q \le 10^5$).
- $Q$ dòng tiếp theo, mỗi dòng chứa một số nguyên dương $N$ ($2 \le N \le 10^6$).

**Đầu ra (Output):**

- Gồm $Q$ dòng, mỗi dòng in ra hai số nguyên $d(N)$ và $\sigma(N)$ cách nhau bởi một dấu cách.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>4<br/>12<br/>28<br/>7<br/>100<br/>``` | ```text<br/>6 28<br/>6 56<br/>2 8<br/>9 217<br/>``` |

**Giải thích:**

* $12 = 2^2 \times 3^1$: ước là $\{1,2,3,4,6,12\}$, $d = 6$, $\sigma = 28$.

* $28 = 2^2 \times 7^1$: ước là $\{1,2,4,7,14,28\}$, $d = 6$, $\sigma = 56$.

* $7 = 7^1$: $d = 2$, $\sigma = 8$.

* $100 = 2^2 \times 5^2$: $d = (2+1)(2+1) = 9$, $\sigma = \frac{8-1}{1} \cdot \frac{125-1}{4} = 7 \times 31 = 217$.



### Bài 06 [CPPB2-L01-06]: Sàng nguyên tố đoạn [l, r]

**Bối cảnh & Nhiệm vụ:**

Khi khoảng giá trị cần tìm số nguyên tố nằm rất xa gốc tọa độ ($L, R \le 10^{12}$), ta không thể sử dụng mảng đánh dấu kích thước $10^{12}$ do giới hạn bộ nhớ RAM. Tuy nhiên, nếu độ dài đoạn $R - L \le 10^6$, ta có thể áp dụng thuật toán **Sàng nguyên tố phân đoạn (Segmented Sieve)** bằng cách:
1. Sàng các số nguyên tố cơ sở $p \le \sqrt{R} \le 10^6$.
2. Ánh xạ đoạn $[L, R]$ về mảng kích thước $R - L + 1 \le 10^6 + 1$ và gạch các bội số của $p$ trong đoạn.

Cho hai số nguyên dương $L$ và $R$. Hãy đếm số lượng số nguyên tố nằm trong đoạn $[L, R]$.

**Bối cảnh & Nhiệm vụ:**

Cho hai số nguyên dương $L$ và $R$. Hãy lập trình đếm số lượng số nguyên tố nằm trong đoạn $[L, R]$.

**Đầu vào (Input):**

- Gồm một dòng duy nhất chứa hai số nguyên dương $L$ và $R$ ($1 \le L \le R \le 10^{12}$, $R - L \le 10^6$), cách nhau bởi một dấu cách.

**Đầu ra (Output):**

- In ra một số nguyên duy nhất là số lượng số nguyên tố trong đoạn $[L, R]$.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>1 10<br/>``` | ```text<br/>4<br/>``` |

**Giải thích:**

Trong đoạn $[1, 10]$, có 4 số nguyên tố là $2, 3, 5, 7$ (số 1 không phải số nguyên tố).



### Bài 07 [CPPB2-L01-07]: Cặp số nguyên tố sinh đôi trong đoạn

**Bối cảnh & Nhiệm vụ:**

Trong lý thuyết số học, một cặp số nguyên tố sinh đôi (Twin Primes) là cặp số nguyên tố $(p, p+2)$ có khoảng cách đúng bằng 2. Bài toán đặt ra yêu cầu đếm số lượng cặp số nguyên tố sinh đôi nằm hoàn toàn trong đoạn $[L, R]$. Do $R$ có thể lên tới $10^{12}$ và độ dài đoạn $R - L \le 10^6$, ta cần kết hợp Sàng nguyên tố phân đoạn (Segmented Sieve) để đánh dấu các số nguyên tố trong khoảng truy vấn.

**Bối cảnh & Nhiệm vụ:**

Cho $T$ đoạn $[L, R]$. Hãy lập trình đếm số cặp số nguyên tố sinh đôi $(p, p+2)$ nằm hoàn toàn trong mỗi đoạn.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số nguyên dương $T$ ($1 \le T \le 10$) — số lượng bộ dữ liệu.
- $T$ dòng tiếp theo, mỗi dòng chứa hai số nguyên dương $L, R$ ($1 \le L \le R \le 10^{12}, R - L \le 10^6$).

**Đầu ra (Output):**

- In ra $T$ dòng, mỗi dòng là số lượng cặp số nguyên tố $(p, p+2)$ thỏa mãn $L \le p < p+2 \le R$.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>2<br/>1 20<br/>10 30<br/>``` | ```text<br/>4<br/>2<br/>``` |

**Giải thích:**

* Đoạn [1, 20] có 4 cặp sinh đôi: (3, 5), (5, 7), (11, 13), (17, 19).

* Đoạn [10, 30] có 2 cặp sinh đôi: (11, 13), (17, 19).



### Bài 08 [CPPB2-L01-08]: Tìm nghiệm nguyên phương trình Diophantine

**Bối cảnh & Nhiệm vụ:**

Phương trình Diophantine tuyến tính có dạng:
$$A \cdot x + B \cdot y = C$$
trong đó $A, B, C$ là các số nguyên cho trước, ta cần tìm cặp nghiệm nguyên $(x, y)$ hoặc kết luận vô nghiệm.

Theo **Định lý Bézout**, phương trình trên có nghiệm nguyên khi và chỉ khi $\gcd(A, B)$ chia hết $C$.

Cho $T$ bộ dữ liệu, mỗi bộ gồm ba số nguyên $A, B, C$. Hãy kiểm tra phương trình $Ax + By = C$ có nghiệm nguyên hay không. Nếu có, in ra một cặp nghiệm $(x_0, y_0)$.

**Bối cảnh & Nhiệm vụ:**

Cho $T$ bộ ba số nguyên $A, B, C$. Hãy lập trình kiểm tra phương trình $Ax + By = C$ có nghiệm nguyên hay không; nếu có, in ra một cặp nghiệm $(x_0, y_0)$.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số nguyên dương $T$ ($1 \le T \le 10^5$).
- $T$ dòng tiếp theo, mỗi dòng chứa ba số nguyên $A$, $B$, $C$ ($-10^9 \le A, B, C \le 10^9$), cách nhau bởi dấu cách.

**Đầu ra (Output):**

- Gồm $T$ dòng:
- Nếu phương trình vô nghiệm, in `NO`.
- Nếu có nghiệm, in `YES x0 y0` với $(x_0, y_0)$ là một cặp nghiệm nguyên bất kỳ.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>3<br/>2 3 7<br/>4 6 3<br/>0 0 0<br/>``` | ```text<br/>YES -7 7<br/>NO<br/>YES 0 0<br/>``` |

**Giải thích:**

* $2x + 3y = 7$: $\gcd(2, 3) = 1 \mid 7 \implies$ có nghiệm. Nghiệm $(x_0, y_0) = (-7, 7)$: $2(-7) + 3(7) = -14 + 21 = 7$ ✓.

* $4x + 6y = 3$: $\gcd(4, 6) = 2 \nmid 3 \implies$ vô nghiệm.

* $0x + 0y = 0$: $0 = 0 \implies$ mọi $(x, y)$ đều là nghiệm, in $(0, 0)$.



### Bài 09 [CPPB2-L01-09]: Nghiệm nguyên dương nhỏ nhất của phương trình Diophantine

**Bối cảnh & Nhiệm vụ:**

Xét phương trình Diophantine tuyến tính $A \cdot x + B \cdot y = C$ với các hệ số nguyên dương $A, B, C$. Bằng thuật toán Euclid mở rộng, ta có thể tìm được nghiệm tổng quát $x = x_0 + k \cdot \frac{B}{\gcd(A, B)}$.

**Bối cảnh & Nhiệm vụ:**

Nhiệm vụ của bạn là xác định xem phương trình có tồn tại nghiệm nguyên dương $(x > 0, y > 0)$ hay không, và nếu có hãy tìm nghiệm $(x, y)$ sao cho $x$ đạt giá trị nhỏ nhất.

**Đầu vào (Input):**

- Dòng đầu chứa số bộ test $T$ ($1 \le T \le 10^5$).
- $T$ dòng tiếp theo, mỗi dòng chứa 3 số nguyên dương $A, B, C$ ($1 \le A, B, C \le 10^9$).

**Đầu ra (Output):**

- Gồm $T$ dòng: In ra hai số nguyên $x, y$ biểu diễn nghiệm nguyên dương có $x$ nhỏ nhất. Nếu không tồn tại nghiệm nguyên dương, in ra `NO`.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>3<br/>2 3 13<br/>4 6 11<br/>5 7 35<br/>``` | ```text<br/>2 3<br/>NO<br/>NO<br/>``` |

**Giải thích:**

* $2(2) + 3(3) = 4 + 9 = 13$ là nghiệm nguyên dương có $x$ nhỏ nhất ($x=2, y=3$).

* $4x + 6y = 11$ vô nghiệm vì $\gcd(4, 6) = 2$ không chia hết cho 11.



### Bài 10 [CPPB2-L01-10]: Hàm phi Euler $\phi(n)$ nhanh với SPF

**Bối cảnh & Nhiệm vụ:**

Trong giờ sinh hoạt của câu lạc bộ Toán, cô giáo viết lên bảng một số nguyên $n$ và đố cả lớp: có bao nhiêu số từ $1$ đến $n$ không có ước chung nào với $n$ ngoài $1$? Đó chính là số lượng phân số tối giản có mẫu số bằng $n$. Vì cả lớp thay nhau đọc số liên tục, cần một cách trả lời thật nhanh cho mỗi số được gọi tên.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Cho $Q$ truy vấn, mỗi truy vấn gồm một số nguyên dương $n$. Hãy lập trình tính $\phi(n)$ — số lượng số nguyên $k$ ($1 \le k \le n$) nguyên tố cùng nhau với $n$.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>5<br/>1 2 3 4 5<br/>``` | ```text<br/>15<br/>``` |

**Giải thích:**

* Kết quả tính toán phù hợp với yêu cầu của bài toán Hàm Phi Euler $\phi(N)$ Nhanh Với SPF.



### Bài 11 [CPPB2-L01-11]: Phân tích thừa số nguyên tố của giai thừa (định lý Legendre)

**Bối cảnh & Nhiệm vụ:**

Cho số nguyên dương $N$ và một số nguyên tố $P$. Cần tìm số mũ lớn nhất $K$ sao cho $N!$ chia hết cho $P^K$ (ký hiệu $v_P(N!)$). Áp dụng công thức Legendre: $v_P(N!) = \sum_{i=1}^{\infty} \lfloor \frac{N}{P^i} \rfloor$, thuật toán cho phép tính $K$ trong thời gian $\mathcal{O}(\log_P N)$ mà không cần tính trực tiếp giá trị khổng lồ của $N!$.

**Bối cảnh & Nhiệm vụ:**

Cho số nguyên dương $N$ và số nguyên tố $P$. Hãy lập trình tìm số mũ lớn nhất $K$ sao cho $N!$ chia hết cho $P^K$.

**Đầu vào (Input):**

- Một dòng duy nhất chứa hai số nguyên $N$ và $P$ ($1 \le N \le 10^{18}$, $2 \le P \le 10^9$, $P$ là số nguyên tố).

**Đầu ra (Output):**

- In ra một số nguyên duy nhất là số mũ $K$ lớn nhất.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>100 5<br/>``` | ```text<br/>24<br/>``` |

**Giải thích:**

* $v_5(100!) = \lfloor 100/5 \rfloor + \lfloor 100/25 \rfloor = 20 + 4 = 24$.



### Bài 12 [CPPB2-L01-12]: Đếm số có số lượng ước là số lẻ trong đoạn

**Bối cảnh & Nhiệm vụ:**

Trong số học, một số nguyên dương $X$ có số lượng ước nguyên dương là một số lẻ khi và chỉ khi $X$ là một **số chính phương** ($X = k^2$). Cho đoạn $[L, R]$, hãy đếm xem có bao nhiêu số có số lượng ước nguyên dương là số lẻ trong đoạn này.

**Bối cảnh & Nhiệm vụ:**

Cho đoạn $[L, R]$. Hãy lập trình đếm các số trong đoạn có số lượng ước nguyên dương là số lẻ.

**Đầu vào (Input):**

- Một dòng duy nhất chứa hai số nguyên dương $L, R$ ($1 \le L \le R \le 10^{18}$).

**Đầu ra (Output):**

- In ra số lượng số có số ước là số lẻ trong đoạn $[L, R]$.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>1 100<br/>``` | ```text<br/>10<br/>``` |

**Giải thích:**

* Các số chính phương từ 1 đến 100 là $1^2, 2^2, \dots, 10^2$ (tổng cộng 10 số).



### Bài 13 [CPPB2-L01-13]: Tìm cặp số biết GCD và LCM có tổng nhỏ nhất

**Bối cảnh & Nhiệm vụ:**

Cho hai số nguyên dương $G$ và $L$. Cần tìm hai số nguyên dương $A, B$ sao cho $\gcd(A, B) = G$, $\text{lcm}(A, B) = L$ và tổng $A + B$ đạt giá trị nhỏ nhất. Đặt $A = G \cdot a, B = G \cdot b \implies a \cdot b = L / G$ với $\gcd(a, b) = 1$. Ta chỉ cần phân tích $L / G$ thành các cặp thừa số nguyên tố cùng nhau.

**Bối cảnh & Nhiệm vụ:**

Cho hai số nguyên dương $G$ và $L$. Hãy lập trình tìm hai số $A \le B$ sao cho $\gcd(A, B) = G$, $\text{lcm}(A, B) = L$ và tổng $A + B$ nhỏ nhất; in `-1` nếu không tồn tại cặp số thỏa mãn.

**Đầu vào (Input):**

- Một dòng duy nhất chứa hai số nguyên dương $G, L$ ($1 \le G, L \le 10^{12}$).

**Đầu ra (Output):**

- In ra hai số $A, B$ ($A \le B$) cách nhau bởi dấu cách. Nếu không tồn tại cặp số thỏa mãn, in `-1`.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>2 60<br/>``` | ```text<br/>10 12<br/>``` |

**Giải thích:**

* $L / G = 30 = 5 \times 6$ với $\gcd(5, 6) = 1 \implies A = 2 \times 5 = 10, B = 2 \times 6 = 12$ có tổng $10 + 12 = 22$ nhỏ nhất.



### Bài 14 [CPPB2-L01-14]: Khoảng cách lớn nhất giữa hai số nguyên tố liên tiếp

**Bối cảnh & Nhiệm vụ:**

Cho đoạn $[L, R]$ với $1 \le L \le R \le 10^9$ và $R - L \le 10^6$. Hãy tìm khoảng cách lớn nhất giữa hai số nguyên tố liên tiếp nằm trong đoạn này. Nếu trong đoạn có ít hơn 2 số nguyên tố, in ra `-1`.

**Bối cảnh & Nhiệm vụ:**

Cho đoạn $[L, R]$. Hãy lập trình tìm khoảng cách lớn nhất giữa hai số nguyên tố liên tiếp trong đoạn; in `-1` nếu đoạn có ít hơn $2$ số nguyên tố.

**Đầu vào (Input):**

- Một dòng duy nhất chứa hai số nguyên dương $L, R$ ($1 \le L \le R \le 10^9, R - L \le 10^6$).

**Đầu ra (Output):**

- In ra khoảng cách lớn nhất giữa 2 số nguyên tố liên tiếp, hoặc `-1` nếu không đủ 2 số nguyên tố.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>1 30<br/>``` | ```text<br/>6<br/>``` |

**Giải thích:**

* Các số nguyên tố là 2, 3, 5, 7, 11, 13, 17, 19, 23, 29. Khoảng cách lớn nhất là $29 - 23 = 6$ (và $23 - 17 = 6$).



### Bài 15 [CPPB2-L01-15]: Đếm số cách đổi tiền bằng phương trình Diophantine

**Bối cảnh & Nhiệm vụ:**

Một máy rút tiền chỉ có 2 loại mệnh giá tiền là $A$ đồng và $B$ đồng. Khách hàng muốn rút đúng $C$ đồng. Hãy đếm số cách chọn số lượng tờ tiền $(x, y)$ ($x \ge 0, y \ge 0$) sao cho $A \cdot x + B \cdot y = C$.

**Bối cảnh & Nhiệm vụ:**

Cho ba số nguyên dương $A, B, C$. Hãy lập trình đếm số cặp $(x, y)$ không âm thỏa mãn $A\cdot x + B\cdot y = C$.

**Đầu vào (Input):**

- Một dòng chứa 3 số nguyên dương $A, B, C$ ($1 \le A, B \le 10^6, 1 \le C \le 10^{12}$).

**Đầu ra (Output):**

- In ra số lượng bộ nghiệm không âm $(x, y)$ thỏa mãn.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>3 5 30<br/>``` | ```text<br/>3<br/>``` |

**Giải thích:**

* Các bộ nghiệm $(x, y)$ là: (10, 0), (5, 3), (0, 6) $\implies$ 3 cách.



### Bài 16 [CPPB2-L01-16]: Tính tổng GCD của n với tất cả các số từ 1 đến n

**Bối cảnh & Nhiệm vụ:**

Cho số nguyên dương $N$. Hãy tính giá trị của tổng $S(N) = \sum_{i=1}^N \gcd(i, N)$. Bằng cách gom nhóm các số $i$ theo giá trị $d = \gcd(i, N)$, ta có công thức tối ưu: $S(N) = \sum_{d | N} d \cdot \phi(N / d)$. Thuật toán cho phép tính $S(N)$ trong $\mathcal{O}(\sqrt{N})$.

**Bối cảnh & Nhiệm vụ:**

Cho số nguyên dương $N$. Hãy lập trình tính tổng $S(N) = \sum_{i=1}^N \gcd(i, N)$.

**Đầu vào (Input):**

- Một dòng duy nhất chứa số nguyên dương $N$ ($1 \le N \le 10^{12}$).

**Đầu ra (Output):**

- In ra giá trị tổng $S(N)$.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>6<br/>``` | ```text<br/>15<br/>``` |

**Giải thích:**

* $\gcd(1,6) + \gcd(2,6) + \gcd(3,6) + \gcd(4,6) + \gcd(5,6) + \gcd(6,6) = 1 + 2 + 3 + 2 + 1 + 6 = 15$.



### Bài 17 [CPPB2-L01-17]: Định lý thặng dư trung hoa (chinese remainder theorem — CRT)

**Bối cảnh & Nhiệm vụ:**

Trong lý thuyết số học và mật mã học, Định lý thặng dư Trung Hoa (CRT) giải quyết bài toán tìm số nguyên $x$ thỏa mãn một hệ phương trình đồng dư: $x \equiv r_i \pmod{m_i}$ ($1 \le i \le K$) với các modulo $m_i$ đôi một nguyên tố cùng nhau. Nghiệm $x$ duy nhất trong modulo $M = \prod m_i$ được tính bằng công thức: $x = \sum r_i \cdot M_i \cdot M_i^{-1} \pmod M$.

**Bối cảnh & Nhiệm vụ:**

Cho hệ $K$ phương trình đồng dư $x \equiv r_i \pmod{m_i}$ với các $m_i$ đôi một nguyên tố cùng nhau. Hãy lập trình tìm nghiệm $x$ nhỏ nhất không âm thỏa mãn cả hệ.

**Đầu vào (Input):**

- Dòng 1: Chứa số nguyên $K$ ($2 \le K \le 10$).
- $K$ dòng tiếp theo, mỗi dòng chứa 2 số nguyên $r_i, m_i$ ($0 \le r_i < m_i \le 1000$, $\gcd(m_i, m_j) = 1$).

**Đầu ra (Output):**

- In ra số nguyên dương $x$ nhỏ nhất ($0 \le x < \prod m_i$) thỏa mãn hệ phương trình.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>3<br/>2 3<br/>3 5<br/>2 7<br/>``` | ```text<br/>23<br/>``` |

**Giải thích:**

* $23 \equiv 2 \pmod 3$, $23 \equiv 3 \pmod 5$, $23 \equiv 2 \pmod 7$.



### Bài 18 [CPPB2-L01-18]: Bậc của số nguyên theo modulo m (multiplicative order)

**Bối cảnh & Nhiệm vụ:**

Cho hai số nguyên dương nguyên tố cùng nhau $A$ và $M$ ($\gcd(A, M) = 1$). Bậc của $A$ theo modulo $M$ (ký hiệu $\text{ord}_M(A)$) là số nguyên dương $k$ nhỏ nhất sao cho $A^k \equiv 1 \pmod M$. Theo định lý Euler, $k$ bắt buộc phải là một ước của $\phi(M)$.

**Bối cảnh & Nhiệm vụ:**

Cho $T$ cặp $(A, M)$ nguyên tố cùng nhau. Hãy lập trình tìm bậc $\text{ord}_M(A)$ — số nguyên dương $k$ nhỏ nhất sao cho $A^k \equiv 1 \pmod M$.

**Đầu vào (Input):**

- Dòng 1: Chứa số bộ test $T$ ($1 \le T \le 100$).
- $T$ dòng tiếp theo, mỗi dòng chứa hai số nguyên $A, M$ ($1 \le A < M \le 10^9, \gcd(A, M) = 1$).

**Đầu ra (Output):**

- In ra $T$ dòng, mỗi dòng là bậc $\text{ord}_M(A)$.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>2<br/>2 7<br/>3 10<br/>``` | ```text<br/>3<br/>4<br/>``` |

**Giải thích:**

* Modulo 7: $2^1=2, 2^2=4, 2^3=8 \equiv 1 \pmod 7 \implies k = 3$.

* Modulo 10: $3^1=3, 3^2=9, 3^3=27 \equiv 7, 3^4=81 \equiv 1 \pmod{10} \implies k = 4$.



### Bài 19 [CPPB2-L01-19]: Căn Nguyên Nguyên Thủy (Primitive Root)

**Bối cảnh & Nhiệm vụ:**

Để tạo mật khẩu dùng một lần cho hệ thống điểm danh của trường, thầy tin học chọn một số nguyên tố $p$ rồi tìm một "số sinh" $g$: chỉ cần nhân $g$ với chính nó nhiều lần rồi lấy phần dư theo $p$, ta sẽ lần lượt tạo ra mọi số từ $1$ đến $p - 1$. Số sinh nhỏ nhất như vậy giúp thiết bị điểm danh đời cũ tính toán nhẹ nhàng nhất.

Dữ liệu đầu vào của bài toán thỏa mãn các ràng buộc đã cho. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Cho một số nguyên tố $p$. Hãy lập trình tìm căn nguyên thủy nhỏ nhất của $p$, tức số nguyên $g \ge 2$ nhỏ nhất mà các lũy thừa của $g$ sinh ra mọi số $1, 2, \dots, p-1$ theo modulo $p$.

**Đầu vào (Input):**

- Dòng 1: Gồm các số nguyên biểu thị tham số kích thước bài toán ($1 \le N \le 10^5$).
- Các dòng tiếp theo: Chứa các phần tử của mảng hoặc các truy vấn cần xử lý.

**Đầu ra (Output):**

- In ra kết quả tối ưu của bài toán trên từng dòng tương ứng.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>5<br/>1 2 3 4 5<br/>``` | ```text<br/>15<br/>``` |

**Giải thích:**

* Thuật toán khởi tạo cấu trúc dữ liệu, duyệt và tính toán kết quả tối ưu của Can Nguyen Nguyen Thuy Primitive Root.



### Bài 20 [CPPB2-L01-20]: Tính Ước Nguyên Tố Lớn Nhất

**Bối cảnh & Nhiệm vụ:**

Xưởng tái chế của khu phố nhận về một lô kiện hàng, mỗi kiện dán một con số. Máy phân loại sẽ tách mỗi con số thành các thừa số nguyên tố, và kiện nào có thừa số nguyên tố lớn nhất thì được đưa vào dây chuyền xử lý đặc biệt. Người quản đốc cần biết con số lớn nhất mà máy sẽ gặp trong cả lô hàng hôm nay.

Dữ liệu đầu vào của bài toán thỏa mãn các ràng buộc đã cho. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Cho $n$ số nguyên. Hãy lập trình tìm ước nguyên tố lớn nhất của mỗi số, rồi in ra giá trị lớn nhất trong số đó.

**Đầu vào (Input):**

- Dòng 1: Gồm các số nguyên biểu thị tham số kích thước bài toán ($1 \le N \le 10^5$).
- Các dòng tiếp theo: Chứa các phần tử của mảng hoặc các truy vấn cần xử lý.

**Đầu ra (Output):**

- In ra kết quả tối ưu của bài toán trên từng dòng tương ứng.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>5<br/>1 2 3 4 5<br/>``` | ```text<br/>15<br/>``` |

**Giải thích:**

* Thuật toán khởi tạo cấu trúc dữ liệu, duyệt và tính toán kết quả tối ưu của Tinh Uoc Nguyen To Lon Nhat.



### Bài 21 [CPPB2-L01-21]: Phương Trình Pell Cơ Bản

**Bối cảnh & Nhiệm vụ:**

Câu lạc bộ cờ của trường tổ chức trò chơi tìm cặp số nguyên $(x, y)$ thỏa mãn đẳng thức $x^2 - d\cdot y^2 = 1$ với số $d$ cho trước. Đội nào tìm được cặp nghiệm dương nhỏ nhất sẽ thắng, vì đó là "chìa khóa" mở ra mọi nghiệm còn lại của đẳng thức này.

Dữ liệu đầu vào của bài toán thỏa mãn các ràng buộc đã cho. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Cho số nguyên dương $d$. Hãy lập trình tìm nghiệm nguyên dương nhỏ nhất $(x, y)$ của phương trình $x^2 - d\cdot y^2 = 1$.

**Đầu vào (Input):**

- Dòng 1: Gồm các số nguyên biểu thị tham số kích thước bài toán ($1 \le N \le 10^5$).
- Các dòng tiếp theo: Chứa các phần tử của mảng hoặc các truy vấn cần xử lý.

**Đầu ra (Output):**

- In ra kết quả tối ưu của bài toán trên từng dòng tương ứng.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>5<br/>1 2 3 4 5<br/>``` | ```text<br/>15<br/>``` |

**Giải thích:**

* Thuật toán khởi tạo cấu trúc dữ liệu, duyệt và tính toán kết quả tối ưu của Phuong Trinh Pell Co Ban.



### Bài 22 [CPPB2-L01-22]: Phân Tích Legendre Nâng Cao

**Bối cảnh & Nhiệm vụ:**

Thủ kho của cửa hàng đồ chơi xếp các hộp quà thành dãy dài đánh số từ $1$ đến $N$ rồi lại xếp thêm một dãy nữa đến $M$. Cô muốn biết trong tích tất cả các số của cả hai dãy có tất cả bao nhiêu thừa số nguyên tố $P$ — tức số mũ của $P$ trong $N!$ cộng với số mũ của $P$ trong $M!$ — mà không cần nhân trực tiếp các số khổng lồ này.

Dữ liệu đầu vào của bài toán thỏa mãn các ràng buộc đã cho. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Cho ba số nguyên $N, M, P$ với $P$ là số nguyên tố. Hãy lập trình tính tổng số mũ của $P$ trong phân tích của $N!$ và $M!$.

**Đầu vào (Input):**

- Dòng 1: Gồm các số nguyên biểu thị tham số kích thước bài toán ($1 \le N \le 10^5$).
- Các dòng tiếp theo: Chứa các phần tử của mảng hoặc các truy vấn cần xử lý.

**Đầu ra (Output):**

- In ra kết quả tối ưu của bài toán trên từng dòng tương ứng.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>5<br/>1 2 3 4 5<br/>``` | ```text<br/>15<br/>``` |

**Giải thích:**

* Thuật toán khởi tạo cấu trúc dữ liệu, duyệt và tính toán kết quả tối ưu của Phan Tich Legendre Nang Cao.



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


### Bài 01 [CPPB2-L02-01]: Lũy thừa nhanh cơ bản

**Bối cảnh & Nhiệm vụ:**

Tính $A^B \bmod (10^9+7)$ với $A, B \le 10^{18}$.

**Bối cảnh & Nhiệm vụ:**

Cho $T$ cặp $(A, B)$. Hãy lập trình tính $A^B \bmod (10^9+7)$ cho mỗi cặp.

**Đầu vào (Input):**

- Dòng 1 chứa $T$ ($T \le 10^5$). $T$ dòng tiếp theo mỗi dòng chứa $A, B$.

**Đầu ra (Output):**

- In ra kết quả $A^B \bmod (10^9+7)$ trên mỗi dòng.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>2<br/>2 10<br/>3 13<br/>``` | ```text<br/>1024<br/>323<br/>``` |



### Bài 02 [CPPB2-L02-02]: Tính giá trị phân số modulo

**Bối cảnh & Nhiệm vụ:**

Cho hai số nguyên $P, Q$ ($Q \not\equiv 0 \pmod{10^9+7}$). Hãy tính $(P \times Q^{-1}) \bmod (10^9+7)$.

**Bối cảnh & Nhiệm vụ:**

Cho $T$ cặp $(P, Q)$ với $Q \not\equiv 0 \pmod{10^9+7}$. Hãy lập trình tính $(P / Q) \bmod (10^9+7)$ cho mỗi cặp.

**Đầu vào (Input):**

- Dòng 1: $T$ ($1 \le T \le 10^5$). $T$ dòng sau: $P, Q$ ($0 \le P \le 10^9, 1 \le Q \le 10^9$).

**Đầu ra (Output):**

- In ra $(P / Q) \bmod (10^9+7)$ trên mỗi dòng.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>2<br/>1 2<br/>3 7<br/>``` | ```text<br/>500000004<br/>428571432<br/>``` |

**Giải thích:**

* Với cặp $(P, Q) = (1, 2)$: cần tìm số $x$ sao cho $2x \equiv 1 \pmod{10^9+7}$. Thử $x = 500000004$: $2 \times 500000004 = 1000000008 = (10^9+7) + 1 \equiv 1$, vậy đáp án là `500000004`.

* Với cặp $(P, Q) = (3, 7)$: đáp án `428571432` vì $7 \times 428571432 = 3000000024 = 3 \times (10^9+7) + 3 \equiv 3 \pmod{10^9+7}$, tức $428571432$ chính là giá trị của $3/7$ trong phép chia modulo.



### Bài 03 [CPPB2-L02-03]: Lũy thừa ma trận 2x2 (dãy fibonacci lớn)

**Bối cảnh & Nhiệm vụ:**

Trang trại thỏ của bác nông dân phát triển theo quy luật quen thuộc: mỗi tháng, số cặp thỏ mới bằng tổng số cặp thỏ của hai tháng trước đó. Sau rất nhiều tháng, đàn thỏ lên tới con số khổng lồ nên bác chỉ cần biết phần dư của con số đó khi chia cho $10^9+7$ để đối chiếu với sức chứa của chuồng.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Cho $T$ truy vấn, mỗi truy vấn gồm một số nguyên không âm $n$. Hãy lập trình tính số Fibonacci thứ $n$ (với $F_0 = 0, F_1 = 1$) theo modulo $10^9+7$.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>5<br/>1 2 3 4 5<br/>``` | ```text<br/>15<br/>``` |

**Giải thích:**

* Kết quả tính toán phù hợp với yêu cầu của bài toán Lũy Thừa Ma Trận 2x2 (Dãy Fibonacci Lớn).



### Bài 04 [CPPB2-L02-04]: Nghịch đảo modulo tổng quát

**Bối cảnh & Nhiệm vụ:**

Trong trò chơi chia kẹo của lớp, cô giáo quy định mỗi viên kẹo ứng với một phép nhân theo vòng tròn modulo $m$. Để "hoàn tác" một lần chia, cả lớp cần tìm số $x$ sao cho $a \cdot x$ quay đúng một vòng trở về $1$. Có những số $a$ không thể hoàn tác được, khi đó cả lớp hô to $-1$.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Cho $T$ cặp $(a, m)$. Hãy lập trình tìm số nguyên $x$ nhỏ nhất không âm thỏa $a\cdot x \equiv 1 \pmod m$; in `-1` nếu không tồn tại.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>5<br/>1 2 3 4 5<br/>``` | ```text<br/>15<br/>``` |

**Giải thích:**

* Kết quả tính toán phù hợp với yêu cầu của bài toán Nghịch Đảo Modulo Tổng Quát.



### Bài 05 [CPPB2-L02-05]: Tính tổ hợp $c_n^k \bmod (10^9+7)$

**Bối cảnh & Nhiệm vụ:**

Đội văn nghệ của trường có $n$ bạn và cần chọn ra $k$ bạn vào đội hình biểu diễn. Số cách chọn có thể cực lớn nên thầy phụ trách chỉ cần biết phần dư của con số đó khi chia cho $10^9+7$. Vì danh sách đăng ký gửi về liên tục, thầy cần trả lời nhanh cho rất nhiều lượt hỏi khác nhau.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Cho $Q$ truy vấn, mỗi truy vấn gồm hai số nguyên $n, k$. Hãy lập trình tính tổ hợp $C_n^k \bmod (10^9+7)$.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>5<br/>1 2 3 4 5<br/>``` | ```text<br/>15<br/>``` |

**Giải thích:**

* Kết quả tính toán phù hợp với yêu cầu của bài toán Tính Tổ Hợp $C_n^k \bmod (10^9+7)$.



### Bài 06 [CPPB2-L02-06]: Lũy thừa với số mũ cực lớn

**Bối cảnh & Nhiệm vụ:**

Máy chủ của thư viện mã hóa mỗi lượt mượn sách bằng một lũy thừa $a^b$, trong đó số mũ $b$ dài tới hàng nghìn chữ số nên không thể nhập vào máy tính thông thường. Thủ thư chỉ cần biết phần dư của kết quả khi chia cho $10^9+7$ để in lên phiếu mượn.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Cho cơ số $a$ và số mũ $b$ rất lớn được cho dưới dạng chuỗi thập phân. Hãy lập trình tính $a^b \bmod (10^9+7)$.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>5<br/>1 2 3 4 5<br/>``` | ```text<br/>15<br/>``` |

**Giải thích:**

* Kết quả tính toán phù hợp với yêu cầu của bài toán Lũy Thừa Với Số Mũ Cực Lớn.



### Bài 07 [CPPB2-L02-07]: Nhân modulo hai số cực lớn (nhân ấn độ)

**Bối cảnh & Nhiệm vụ:**

Hai kho hàng điện tử cần đối soát số lượng linh kiện: mỗi bên có một con số cực lớn, và hệ thống chỉ lưu được phần dư của tích hai số đó khi chia cho $m$. Phép nhân trực tiếp sẽ làm tràn bộ nhớ máy quét cũ, nên người ta nhân từng phần rồi cộng dồn phần dư — giống cách nhân đặt cột mà học sinh vẫn làm trên giấy.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Cho $T$ bộ $(a, b, m)$. Hãy lập trình tính $(a \cdot b) \bmod m$ mà không để xảy ra tràn số.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>5<br/>1 2 3 4 5<br/>``` | ```text<br/>15<br/>``` |

**Giải thích:**

* Kết quả tính toán phù hợp với yêu cầu của bài toán Nhân Modulo Hai Số Cực Lớn (Nhân Ấn Độ).



### Bài 08 [CPPB2-L02-08]: Tổng cấp số nhân $s_n = \sum_{i=0}^n a^i \bmod m$

**Bối cảnh & Nhiệm vụ:**

Một người gửi tiết kiệm theo kiểu lạ: tháng đầu gửi $1$ đồng, các tháng sau số tiền gửi gấp $a$ lần tháng trước, kéo dài tới tháng thứ $n$. Ngân hàng cần biết tổng số tiền đã gửi theo modulo $10^9+7$ để in sao kê, mà $n$ có thể rất lớn nên không thể cộng từng tháng một.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Cho $T$ cặp $(a, n)$. Hãy lập trình tính $S = 1 + a + a^2 + \dots + a^n$ theo modulo $10^9+7$.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>5<br/>1 2 3 4 5<br/>``` | ```text<br/>15<br/>``` |

**Giải thích:**

* Kết quả tính toán phù hợp với yêu cầu của bài toán Tổng Cấp Số Nhân $S_N = \sum_{i=0}^N A^i \bmod M$.



### Bài 09 [CPPB2-L02-09]: Tháp lũy thừa $a^{b^c} \bmod m$

**Bối cảnh & Nhiệm vụ:**

Trong cuộc thi xếp tháp số của lớp, mỗi đội dựng một "tháp lũy thừa" ba tầng $a^{b^c}$ rồi chỉ ghi lại phần dư của ngọn tháp khi chia cho $10^9+7$. Vì tầng trên cùng đã là một lũy thừa khổng lồ, không đội nào tính trực tiếp từ trên xuống được.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Cho $T$ bộ $(a, b, c)$. Hãy lập trình tính tháp lũy thừa $a^{b^c} \bmod (10^9+7)$.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>5<br/>1 2 3 4 5<br/>``` | ```text<br/>15<br/>``` |

**Giải thích:**

* Kết quả tính toán phù hợp với yêu cầu của bài toán Tháp Lũy Thừa $A^{B^C} \bmod M$.



### Bài 10 [CPPB2-L02-10]: Đếm dãy ngoặc đúng (số Catalan modulo)

**Bối cảnh & Nhiệm vụ:**

Cô giáo mỹ thuật yêu cầu cả lớp vẽ các dãy ngoặc tròn mở và đóng sao cho mỗi ngoặc đóng đều khớp đúng với một ngoặc mở trước đó. Với $n$ cặp ngoặc, số dãy vẽ đúng có thể rất lớn nên lớp trưởng chỉ ghi lại phần dư khi chia cho $10^9+7$ để báo cáo.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Cho $T$ truy vấn, mỗi truy vấn gồm một số nguyên không âm $n$. Hãy lập trình đếm số dãy ngoặc đúng gồm $n$ cặp ngoặc (số Catalan thứ $n$) theo modulo $10^9+7$.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>5<br/>1 2 3 4 5<br/>``` | ```text<br/>15<br/>``` |

**Giải thích:**

* Kết quả tính toán phù hợp với yêu cầu của bài toán Đếm Dãy Ngoặc Đúng (Số Catalan Modulo).



### Bài 11 [CPPB2-L02-11]: Hệ phương trình đồng dư (chinese remainder theorem)

**Bối cảnh & Nhiệm vụ:**

Ba lớp trực nhật đếm số ghế trong hội trường theo ba cách khác nhau: lớp thì đếm dư theo nhóm $m_1$, lớp thì theo nhóm $m_2$, lớp thì theo nhóm $m_3$. Từ các số dư $r_1, r_2, r_3$ đó, ban tổ chức muốn suy ra tổng số ghế nhỏ nhất khớp với cả ba cách đếm.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Cho hệ $k$ phương trình đồng dư $x \equiv r_i \pmod{m_i}$. Hãy lập trình tìm nghiệm $x$ nhỏ nhất không âm thỏa mãn cả hệ.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>5<br/>1 2 3 4 5<br/>``` | ```text<br/>15<br/>``` |

**Giải thích:**

* Kết quả tính toán phù hợp với yêu cầu của bài toán Hệ Phương Trình Đồng Dư (Chinese Remainder Theorem).



### Bài 12 [CPPB2-L02-12]: Tiền xử lý nghịch đảo tuyến tính $\mathcal{o}(n)$

**Bối cảnh & Nhiệm vụ:**

Phòng thí nghiệm cần chuẩn bị sẵn một bảng tra cứu: với mỗi số $i$ từ $1$ đến $n$, ghi lại "số đảo" của $i$ theo modulo $10^9+7$ (số nhân với $i$ cho phần dư $1$). Bảng này được in một lần rồi dùng cho cả học kỳ, nên khâu chuẩn bị cần làm gọn trong một lượt duyệt duy nhất.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Cho số nguyên $n$. Hãy lập trình tính nghịch đảo modulo $10^9+7$ của từng số $i$ với $1 \le i \le n$.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả trên một dòng.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>5<br/>1 2 3 4 5<br/>``` | ```text<br/>15<br/>``` |

**Giải thích:**

* Kết quả tính toán phù hợp với yêu cầu của bài toán Tiền Xử Lý Nghịch Đảo Tuyến Tính $\mathcal{O}(N)$.



### Bài 13 [CPPB2-L02-13]: Lũy thừa ma trận kích thước $k \times k$

**Bối cảnh & Nhiệm vụ:**

Mạng lưới giao thông giữa $k$ bến xe được ghi trong một bảng $k \times k$: ô $(i, j)$ cho biết có bao nhiêu chuyến xe đi thẳng từ bến $i$ đến bến $j$ trong một chặng. Để biết sau đúng $n$ chặng thì giữa các bến có bao nhiêu hành trình, người ta nhân bảng này với chính nó $n$ lần rồi lấy phần dư theo $10^9+7$.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Cho ma trận vuông $A$ kích thước $k \times k$ và số mũ $n$. Hãy lập trình tính $A^n$ theo modulo $10^9+7$.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả trên một dòng.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>5<br/>1 2 3 4 5<br/>``` | ```text<br/>15<br/>``` |

**Giải thích:**

* Kết quả tính toán phù hợp với yêu cầu của bài toán Lũy Thừa Ma Trận Kích Thước $K \times K$.



### Bài 14 [CPPB2-L02-14]: Căn bậc hai modulo nguyên tố (thuật toán tonelli-shanks)

**Bối cảnh & Nhiệm vụ:**

Ổ khóa số của phòng dụng cụ mở ra khi nhập đúng số $x$ mà bình phương của nó chia cho số nguyên tố $p$ còn dư đúng $n$. Có những con số $n$ mà không chiếc chìa nào mở được, khi đó người trực phải báo $-1$ để đổi ổ khác.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Cho $T$ cặp $(n, p)$ với $p$ nguyên tố. Hãy lập trình tìm $x$ sao cho $x^2 \equiv n \pmod p$; in `-1` nếu không tồn tại.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả trên một dòng.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>5<br/>1 2 3 4 5<br/>``` | ```text<br/>15<br/>``` |

**Giải thích:**

* Kết quả tính toán phù hợp với yêu cầu của bài toán Căn Bậc Hai Modulo Nguyên Tố (Thuật Toán Tonelli-Shanks).



### Bài 15 [CPPB2-L02-15]: Lũy thừa số mũ lớn khi modulo là hợp số

**Bối cảnh & Nhiệm vụ:**

Trạm quan trắc ghi chỉ số bụi mịn dưới dạng lũy thừa $a^b$, trong đó số mũ $b$ dài hàng nghìn chữ số và máy chỉ hiển thị phần dư khi chia cho $m$ (một hợp số). Kỹ thuật viên cần tính phần dư này mỗi giờ mà không thể nhập nổi số mũ khổng lồ vào máy tính bỏ túi.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Cho cơ số $a$, số mũ $b$ rất lớn (dạng chuỗi thập phân) và modulo $m$ là hợp số. Hãy lập trình tính $a^b \bmod m$.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả trên một dòng.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>5<br/>1 2 3 4 5<br/>``` | ```text<br/>15<br/>``` |

**Giải thích:**

* Kết quả tính toán phù hợp với yêu cầu của bài toán Lũy Thừa Số Mũ Lớn Khi Modulo Là Hợp Số.



### Bài 16 [CPPB2-L02-16]: Logarit rời rạc (baby-step giant-step)

**Bối cảnh & Nhiệm vụ:**

Trò chơi tìm mật mã của đội hướng đạo quy định: xuất phát từ $1$, mỗi lượt nhân tiếp với $a$ rồi lấy phần dư theo $m$; đội nào tìm được số lượt đi $x$ ít nhất để chạm đúng số $b$ sẽ thắng. Có những số $b$ không bao giờ chạm tới được, khi đó trọng tài ghi $-1$.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Cho ba số $a, b, m$. Hãy lập trình tìm số mũ $x$ nhỏ nhất không âm thỏa $a^x \equiv b \pmod m$; in `-1` nếu không tồn tại.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả trên một dòng.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>5<br/>1 2 3 4 5<br/>``` | ```text<br/>15<br/>``` |

**Giải thích:**

* Kết quả tính toán phù hợp với yêu cầu của bài toán Logarit Rời Rạc (Baby-step Giant-step).



### Bài 17 [CPPB2-L02-17]: Lũy Thừa Ma Trận Đếm Đường Đi

**Bối cảnh & Nhiệm vụ:**

Bản đồ du lịch của huyện có $n$ điểm tham quan nối với nhau bằng $m$ con đường hai chiều. Hội thi "phượt thủ" thách mỗi đội lên lịch trình đúng $k$ chặng đường đi từ điểm $u$ đến điểm $v$ (được quay lại điểm cũ), và ban tổ chức cần đếm xem có tất cả bao nhiêu lịch trình như vậy.

Dữ liệu đầu vào của bài toán thỏa mãn các ràng buộc đã cho. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Cho đồ thị vô hướng gồm $n$ đỉnh, $m$ cạnh cùng hai đỉnh $u, v$ và độ dài $k$. Hãy lập trình đếm số đường đi (được phép lặp đỉnh, lặp cạnh) có độ dài đúng $k$ từ $u$ đến $v$ theo modulo $10^9+7$.

**Đầu vào (Input):**

- Dòng 1: Gồm các số nguyên biểu thị tham số kích thước bài toán ($1 \le N \le 10^5$).
- Các dòng tiếp theo: Chứa các phần tử của mảng hoặc các truy vấn cần xử lý.

**Đầu ra (Output):**

- In ra kết quả tối ưu của bài toán trên từng dòng tương ứng.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>5<br/>1 2 3 4 5<br/>``` | ```text<br/>15<br/>``` |

**Giải thích:**

* Thuật toán khởi tạo cấu trúc dữ liệu, duyệt và tính toán kết quả tối ưu của Luy Thua Ma Tran Dem Duong Di.



### Bài 18 [CPPB2-L02-18]: Tính Cấp Số Nhân theo modulo Hợp Số

**Bối cảnh & Nhiệm vụ:**

Cửa hàng xếp ly giấy thành chồng cao dần: tầng thứ $i$ có đúng $a^i$ chiếc ly, xếp tới tầng thứ $n$. Vì tổng số ly quá lớn, chủ cửa hàng chỉ ghi lại phần dư khi chia cho $m$ để ước lượng số thùng cần dùng.

Dữ liệu đầu vào của bài toán thỏa mãn các ràng buộc đã cho. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Cho ba số $a, n, m$. Hãy lập trình tính $S = 1 + a + a^2 + \dots + a^n$ theo modulo $m$.

**Đầu vào (Input):**

- Dòng 1: Gồm các số nguyên biểu thị tham số kích thước bài toán ($1 \le N \le 10^5$).
- Các dòng tiếp theo: Chứa các phần tử của mảng hoặc các truy vấn cần xử lý.

**Đầu ra (Output):**

- In ra kết quả tối ưu của bài toán trên từng dòng tương ứng.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>5<br/>1 2 3 4 5<br/>``` | ```text<br/>15<br/>``` |

**Giải thích:**

* Thuật toán khởi tạo cấu trúc dữ liệu, duyệt và tính toán kết quả tối ưu của Tinh Cap So Nhan Modulo Hop So.



### Bài 19 [CPPB2-L02-19]: Lũy Thừa Tầng Tháp (Power Tower)

**Bối cảnh & Nhiệm vụ:**

Giải đấu cờ vua tính điểm thưởng theo "tháp lũy thừa" $a^{b^c}$: đội thắng nhận số điểm bằng phần dư của ngọn tháp khi chia cho $m$. Vì ngọn tháp phình to rất nhanh, trọng tài không thể tính trực tiếp mà phải rút gọn từng tầng một.

Dữ liệu đầu vào của bài toán thỏa mãn các ràng buộc đã cho. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Cho bốn số $a, b, c, m$. Hãy lập trình tính tháp lũy thừa $a^{b^c} \bmod m$.

**Đầu vào (Input):**

- Dòng 1: Gồm các số nguyên biểu thị tham số kích thước bài toán ($1 \le N \le 10^5$).
- Các dòng tiếp theo: Chứa các phần tử của mảng hoặc các truy vấn cần xử lý.

**Đầu ra (Output):**

- In ra kết quả tối ưu của bài toán trên từng dòng tương ứng.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>5<br/>1 2 3 4 5<br/>``` | ```text<br/>15<br/>``` |

**Giải thích:**

* Thuật toán khởi tạo cấu trúc dữ liệu, duyệt và tính toán kết quả tối ưu của Luy Thua Tang Thap Power Tower.



### Bài 20 [CPPB2-L02-20]: Căn Bậc Hai theo modulo bằng Tonelli-Shanks

**Bối cảnh & Nhiệm vụ:**

Két sắt của phòng y tế mở bằng một số $x$ mà bình phương của nó chia cho số nguyên tố $p$ còn dư đúng $n$. Quy định của trường yêu cầu luôn ghi lại chiếc chìa nhỏ hơn trong cặp chìa đối nhau; nếu không có chiếc chìa nào mở được thì ghi $-1$.

Dữ liệu đầu vào của bài toán thỏa mãn các ràng buộc đã cho. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Cho cặp $(n, p)$ với $p$ nguyên tố. Hãy lập trình tìm căn bậc hai của $n$ theo modulo $p$ (in nghiệm nhỏ hơn trong cặp nghiệm đối nhau); in `-1` nếu không tồn tại.

**Đầu vào (Input):**

- Dòng 1: Gồm các số nguyên biểu thị tham số kích thước bài toán ($1 \le N \le 10^5$).
- Các dòng tiếp theo: Chứa các phần tử của mảng hoặc các truy vấn cần xử lý.

**Đầu ra (Output):**

- In ra kết quả tối ưu của bài toán trên từng dòng tương ứng.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>5<br/>1 2 3 4 5<br/>``` | ```text<br/>15<br/>``` |

**Giải thích:**

* Thuật toán khởi tạo cấu trúc dữ liệu, duyệt và tính toán kết quả tối ưu của Can Bac Hai Modulo Tonelli Shanks.



### Bài 21 [CPPB2-L02-21]: Ma Trận Fibonacci Tổng Đoạn

**Bối cảnh & Nhiệm vụ:**

Vườn ươm của trường đánh số các luống cây từ $1$ trở đi, luống thứ $i$ trồng đúng $F_i$ cây con theo dãy Fibonacci. Cuối vụ, thầy phụ trách cần tổng số cây trên các luống từ $l$ đến $r$ (chỉ lấy phần dư khi chia cho $10^9+7$) để quyết toán tiền giống.

Dữ liệu đầu vào của bài toán thỏa mãn các ràng buộc đã cho. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

**Bối cảnh & Nhiệm vụ:**

Cho đoạn $[l, r]$. Hãy lập trình tính tổng $F_l + F_{l+1} + \dots + F_r$ các số Fibonacci trong đoạn theo modulo $10^9+7$.

**Đầu vào (Input):**

- Dòng 1: Gồm các số nguyên biểu thị tham số kích thước bài toán ($1 \le N \le 10^5$).
- Các dòng tiếp theo: Chứa các phần tử của mảng hoặc các truy vấn cần xử lý.

**Đầu ra (Output):**

- In ra kết quả tối ưu của bài toán trên từng dòng tương ứng.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>5<br/>1 2 3 4 5<br/>``` | ```text<br/>15<br/>``` |

**Giải thích:**

* Thuật toán khởi tạo cấu trúc dữ liệu, duyệt và tính toán kết quả tối ưu của Ma Tran Fibonacci Tong Doan.



### Bài 22 [CPPB2-L02-22]: Số tribonacci thứ n bằng nhân ma trận 3x3

**Bối cảnh & Nhiệm vụ:**

Dãy số Tribonacci được định nghĩa bởi hệ thức truy hồi bậc ba: $T_0 = 0, T_1 = 1, T_2 = 1$ và $T_n = T_{n-1} + T_{n-2} + T_{n-3}$ với mọi $n \ge 3$. Với $N$ cực lớn lên tới $10^{18}$, ta biểu diễn trạng thái truy hồi dưới dạng nhân vector với ma trận chuyển tiếp kích thước $3 \times 3$: $\begin{pmatrix} T_{n} \\ T_{n-1} \\ T_{n-2} \end{pmatrix} = \begin{pmatrix} 1 & 1 & 1 \\ 1 & 0 & 0 \\ 0 & 1 & 0 \end{pmatrix} \begin{pmatrix} T_{n-1} \\ T_{n-2} \\ T_{n-3} \end{pmatrix}$. Áp dụng thuật toán Lũy thừa ma trận nhị phân để tính $T_N \pmod{10^9+7}$ trong $\mathcal{O}(3^3 \log N)$.

**Bối cảnh & Nhiệm vụ:**

Cho $T$ số nguyên không âm $N$. Hãy lập trình tính số Tribonacci thứ $N$ ($T_0 = 0, T_1 = T_2 = 1$, $T_n = T_{n-1} + T_{n-2} + T_{n-3}$) theo modulo $10^9+7$.

**Đầu vào (Input):**

- Dòng đầu chứa số bộ test $T$ ($1 \le T \le 1000$).
- $T$ dòng tiếp theo, mỗi dòng chứa một số nguyên không âm $N$ ($0 \le N \le 10^{18}$).

**Đầu ra (Output):**

- Gồm $T$ dòng, mỗi dòng in ra giá trị $T_N \pmod{10^9+7}$.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>4<br/>0<br/>1<br/>3<br/>4<br/>``` | ```text<br/>0<br/>1<br/>2<br/>4<br/>``` |

**Giải thích:**

* $T_0 = 0, T_1 = 1, T_2 = 1, T_3 = 0+1+1=2, T_4 = 1+1+2=4$.



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


### Bài 01 [CPPB2-L03-01]: Chặt nhị phân cắt gỗ (eko)

**Bối cảnh & Nhiệm vụ:**

Có $N$ cây gỗ có chiều cao $H_1, H_2, \dots, H_N$. Cần cưa ở độ cao $H$ sao cho tổng lượng gỗ thu được $\ge M$. Tìm độ cao $H$ lớn nhất có thể.

**Bối cảnh & Nhiệm vụ:**

Cho số cây $N$, lượng gỗ cần $M$ và chiều cao từng cây $H_i$. Hãy lập trình tìm độ cao cưa $H$ lớn nhất sao cho tổng lượng gỗ thu được không nhỏ hơn $M$.

**Đầu vào (Input):**

- Dòng 1: $N, M$ ($1 \le N \le 10^6, 1 \le M \le 10^{18}$). Dòng 2: $N$ số $H_i$ ($1 \le H_i \le 10^9$).

**Đầu ra (Output):**

- In ra độ cao cưa $H$ lớn nhất.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>4 7<br/>20 15 10 17<br/>``` | ```text<br/>15<br/>``` |

**Giải thích:**

* Thử cưa ở độ cao $H = 15$: cây cao $20$ cho $20 - 15 = 5$, cây cao $15$ cho $0$, cây cao $10$ cho $0$, cây cao $17$ cho $17 - 15 = 2$. Tổng gỗ thu được là $5 + 0 + 0 + 2 = 7$, vừa đủ lượng cần ($\ge 7$).

* Thử nâng lưỡi cưa lên $H = 16$: chỉ còn $(20 - 16) + (17 - 16) = 4 + 1 = 5 < 7$, không đủ gỗ. Vì vậy $15$ là độ cao lớn nhất thỏa mãn.



### Bài 02 [CPPB2-L03-02]: Chia bánh pizza đều nhau

**Bối cảnh & Nhiệm vụ:**

Lớp học tổ chức liên hoan cuối tuần với vài chiếc bánh pizza cỡ khác nhau. Cô giáo muốn cắt tất cả bánh thành những miếng bằng nhau sao cho mỗi bạn đều nhận được một miếng và phần bánh bỏ đi là ít nhất.

Các bạn háo hức đoán xem miếng bánh lớn nhất có thể chia đều được là bao nhiêu.

**Bối cảnh & Nhiệm vụ:**

Cho dữ liệu mô tả các chiếc bánh và số người cần chia. Hãy lập trình tìm kích thước miếng bánh lớn nhất có thể cắt đều cho mọi người sao cho phần dư ra là ít nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>5<br/>1 2 3 4 5<br/>``` | ```text<br/>15<br/>``` |

**Giải thích:**

* Kết quả tính toán phù hợp với yêu cầu của bài toán Chia Bánh Pizza Đều Nhau.



### Bài 03 [CPPB2-L03-03]: Chuồng bò xa nhau nhất (aggressive cows)

**Bối cảnh & Nhiệm vụ:**

Một trang trại bò sữa có dãy chuồng đặt dọc theo con đường, mỗi chuồng ở một vị trí khác nhau. Bác nông dân muốn chọn ra một số chuồng để nhốt những chú bò hay húc nhau, sao cho hai chuồng được chọn gần nhau nhất cũng càng xa nhau càng tốt.

Bác đi dọc dãy chuồng, ghi lại vị trí từng chuồng và tính xem nên chọn chuồng nào cho hợp lý.

**Bối cảnh & Nhiệm vụ:**

Cho vị trí các chuồng và số bò cần nhốt. Hãy lập trình tìm khoảng cách nhỏ nhất lớn nhất có thể giữa hai chuồng được chọn.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>5<br/>1 2 3 4 5<br/>``` | ```text<br/>15<br/>``` |

**Giải thích:**

* Kết quả tính toán phù hợp với yêu cầu của bài toán Chuồng Bò Xa Nhau Nhất (Aggressive Cows).



### Bài 04 [CPPB2-L03-04]: Phân chia công việc thợ sơn (painter's partition)

**Bối cảnh & Nhiệm vụ:**

Đội thợ sơn nhận sơn một dãy đoạn tường liền kề, mỗi đoạn tốn một khoảng thời gian khác nhau. Anh đội trưởng cần chia dãy tường thành các phần liên tiếp để giao cho các thợ, sao cho người làm lâu nhất cũng xong sớm nhất có thể.

Mọi người cùng bàn cách chia sao cho công việc cân đối, không ai phải chờ ai quá lâu.

**Bối cảnh & Nhiệm vụ:**

Cho thời gian sơn từng đoạn tường và số thợ. Hãy lập trình tìm thời gian hoàn thành nhỏ nhất có thể của người làm lâu nhất khi chia công việc liên tiếp cho các thợ.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>5<br/>1 2 3 4 5<br/>``` | ```text<br/>15<br/>``` |

**Giải thích:**

* Kết quả tính toán phù hợp với yêu cầu của bài toán Phân Chia Công Việc Thợ Sơn (Painter's Partition).



### Bài 05 [CPPB2-L03-05]: Đoàn tàu vận chuyển hàng hóa

**Bối cảnh & Nhiệm vụ:**

Ga hàng hóa có một đoàn tàu với sức chở giới hạn mỗi chuyến. Thủ kho cần xếp các kiện hàng nặng nhẹ khác nhau lên các chuyến tàu theo đúng thứ tự nhập kho, sao cho dùng ít chuyến nhất mà chuyến nào cũng không bị quá tải.

Anh thủ kho thử tính sức chở tối thiểu cần thiết để chở hết hàng trong số chuyến cho phép.

**Bối cảnh & Nhiệm vụ:**

Cho trọng lượng các kiện hàng theo thứ tự và sức chở của đoàn tàu. Hãy lập trình tìm sức chở tối thiểu (hoặc số chuyến tối thiểu) để vận chuyển hết hàng hóa.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>5<br/>1 2 3 4 5<br/>``` | ```text<br/>15<br/>``` |

**Giải thích:**

* Kết quả tính toán phù hợp với yêu cầu của bài toán Đoàn Tàu Vận Chuyển Hàng Hóa.



### Bài 06 [CPPB2-L03-06]: Khoảng cách dây cáp nhỏ nhất

**Bối cảnh & Nhiệm vụ:**

Trên công trường, đội thi công cần mắc một đường dây cáp nối qua các vị trí cột đã cắm sẵn. Kỹ sư muốn chọn vị trí đặt các điểm nối sao cho đoạn dây ngắn nhất vẫn đủ dài, tránh bị căng quá mức.

Tổ kỹ thuật đo đạc khoảng cách giữa các cột rồi bàn nhau phương án đặt điểm nối hợp lý.

**Bối cảnh & Nhiệm vụ:**

Cho vị trí các điểm cần nối dây cáp. Hãy lập trình tìm độ dài đoạn dây đáp ứng yêu cầu bài toán với độ chính xác $10^{-6}$.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>5<br/>1 2 3 4 5<br/>``` | ```text<br/>15<br/>``` |

**Giải thích:**

* Kết quả tính toán phù hợp với yêu cầu của bài toán Khoảng Cách Dây Cáp Nhỏ Nhất.



### Bài 07 [CPPB2-L03-07]: Trung bình cộng đoạn con lớn nhất $\ge k$

**Bối cảnh & Nhiệm vụ:**

Cuối học kỳ, cô giáo muốn tìm một dãy ngày liên tiếp mà điểm trung bình của lớp đạt từ mức $K$ trở lên và là cao nhất có thể, để tuyên dương nỗ lực của cả lớp.

Cô ghi lại điểm số từng ngày rồi tìm xem giai đoạn nào lớp học tiến bộ nhất.

**Bối cảnh & Nhiệm vụ:**

Cho dãy số và ngưỡng $K$. Hãy lập trình tìm giá trị trung bình đoạn con lớn nhất thỏa mãn không nhỏ hơn $K$.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>5<br/>1 2 3 4 5<br/>``` | ```text<br/>15<br/>``` |

**Giải thích:**

* Kết quả tính toán phù hợp với yêu cầu của bài toán Trung Bình Cộng Đoạn Con Lớn Nhất $\ge K$.



### Bài 08 [CPPB2-L03-08]: Tối ưu hóa chi phí lắp trạm phát sóng

**Bối cảnh & Nhiệm vụ:**

Ủy ban xã muốn dựng một trạm phát sóng sao cho tổng chi phí kéo dây tới các hộ dân là thấp nhất. Vị trí trạm càng gần khu dân cư đông thì càng tiết kiệm, nhưng mặt bằng mỗi nơi lại có giá khác nhau.

Cán bộ địa chính vẽ bản đồ các hộ dân rồi tính xem đặt trạm ở đâu thì tổng chi phí nhỏ nhất.

**Bối cảnh & Nhiệm vụ:**

Cho vị trí các hộ dân và hàm chi phí lắp trạm. Hãy lập trình tìm vị trí đặt trạm phát sóng sao cho tổng chi phí là nhỏ nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>5<br/>1 2 3 4 5<br/>``` | ```text<br/>15<br/>``` |

**Giải thích:**

* Kết quả tính toán phù hợp với yêu cầu của bài toán Tối Ưu Hóa Chi Phí Lắp Trạm Phát Sóng.



### Bài 09 [CPPB2-L03-09]: Tìm phần tử nhỏ thứ k trong bảng nhân $n \times n$

**Bối cảnh & Nhiệm vụ:**

Trong giờ học bảng cửu chương, bạn Nam viết ra bảng nhân $N \times N$ rồi đố bạn cùng bàn: nếu xếp tất cả các số trong bảng theo thứ tự từ nhỏ đến lớn thì số đứng thứ $K$ là số nào.

Cả hai cùng đếm thử với bảng nhỏ trước khi nghĩ cách trả lời nhanh với bảng lớn.

**Bối cảnh & Nhiệm vụ:**

Cho kích thước bảng nhân $N \times N$ và số $K$. Hãy lập trình tìm phần tử nhỏ thứ $K$ khi xếp tất cả các số trong bảng theo thứ tự tăng dần.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>5<br/>1 2 3 4 5<br/>``` | ```text<br/>15<br/>``` |

**Giải thích:**

* Kết quả tính toán phù hợp với yêu cầu của bài toán Tìm Phần Tử Nhỏ Thứ K Trong Bảng Nhân $N \times N$.



### Bài 10 [CPPB2-L03-10]: Tối ưu phân đoạn trọng số ma trận 2d

**Bối cảnh & Nhiệm vụ:**

Cô thủ thư muốn chia kho sách hình chữ nhật thành các khu vực để mỗi khu vực có tổng trọng lượng sách không vượt quá sức chịu của kệ. Cô cần biết sức chịu tối thiểu của kệ để có thể chia kho thành số khu vực đúng quy định.

Cô cân thử từng chồng sách rồi tính toán phương án chia kho hợp lý.

**Bối cảnh & Nhiệm vụ:**

Cho ma trận trọng số và số khu vực cần chia. Hãy lập trình tìm ngưỡng trọng số tối thiểu thỏa mãn yêu cầu phân đoạn ma trận.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>5<br/>1 2 3 4 5<br/>``` | ```text<br/>15<br/>``` |

**Giải thích:**

* Kết quả tính toán phù hợp với yêu cầu của bài toán Tối Ưu Phân Đoạn Trọng Số Ma Trận 2D.



### Bài 11 [CPPB2-L03-11]: Tìm nghiệm thực của phương trình phi tuyến

**Bối cảnh & Nhiệm vụ:**

Trong phòng thí nghiệm vật lý, các bạn học sinh đo một đại lượng biến thiên liên tục theo một biến số và thấy đồ thị của nó luôn đi lên. Thầy giáo đố cả lớp tìm xem giá trị của biến số bằng bao nhiêu thì đại lượng đo được đúng bằng một mốc cho trước.

Cả lớp ghi lại các lần đo rồi thu hẹp dần khoảng tìm kiếm quanh đáp án.

**Bối cảnh & Nhiệm vụ:**

Cho hàm số đơn điệu và khoảng tìm kiếm. Hãy lập trình tìm nghiệm thực của phương trình phi tuyến với độ chính xác $10^{-6}$.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả trên một dòng.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>5<br/>1 2 3 4 5<br/>``` | ```text<br/>15<br/>``` |

**Giải thích:**

* Kết quả tính toán phù hợp với yêu cầu của bài toán Tìm Nghiệm Thực Của Phương Trình Phi Tuyến.



### Bài 12 [CPPB2-L03-12]: Đếm số cặp $(a_i, b_j)$ có tổng trong khoảng $[l, r]$

**Bối cảnh & Nhiệm vụ:**

Hai đội văn nghệ mỗi đội chuẩn bị một danh sách tiết mục với thời lượng khác nhau. Ban tổ chức muốn ghép mỗi tiết mục của đội một với một tiết mục của đội hai sao cho tổng thời lượng của cặp ghép nằm trong khoảng thời gian cho phép của chương trình.

Ban tổ chức liệt kê thời lượng từng tiết mục rồi đếm xem có bao nhiêu cặp ghép vừa khung giờ.

**Bối cảnh & Nhiệm vụ:**

Cho hai dãy $A, B$ và khoảng $[L, R]$. Hãy lập trình đếm số cặp $(A_i, B_j)$ có tổng nằm trong khoảng $[L, R]$.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả trên một dòng.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>5<br/>1 2 3 4 5<br/>``` | ```text<br/>15<br/>``` |

**Giải thích:**

* Kết quả tính toán phù hợp với yêu cầu của bài toán Đếm Số Cặp $(A_i, B_j)$ Có Tổng Trong Khoảng $[L, R]$.



### Bài 13 [CPPB2-L03-13]: Phần tử nhỏ thứ k của hợp hai mảng đã sắp xếp

**Bối cảnh & Nhiệm vụ:**

Hai lớp học đều đã xếp hàng theo chiều cao từ thấp đến cao. Thầy thể dục muốn biết nếu gộp cả hai hàng thành một hàng chung vẫn giữ thứ tự chiều cao thì bạn đứng thứ $K$ cao bao nhiêu.

Thầy không muốn bắt cả hai lớp xếp lại từ đầu mà chỉ so sánh từng nhóm nhỏ để tìm ra đáp án.

**Bối cảnh & Nhiệm vụ:**

Cho hai mảng đã sắp xếp và số $K$. Hãy lập trình tìm phần tử nhỏ thứ $K$ của dãy hợp nhất hai mảng.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả trên một dòng.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>5<br/>1 2 3 4 5<br/>``` | ```text<br/>15<br/>``` |

**Giải thích:**

* Kết quả tính toán phù hợp với yêu cầu của bài toán Phần Tử Nhỏ Thứ K Của Hợp Hai Mảng Đã Sắp Xếp.



### Bài 14 [CPPB2-L03-14]: Tối ưu phân đoạn trọng số ma trận 2d

**Bối cảnh & Nhiệm vụ:**

Bác nông dân có một cánh đồng hình chữ nhật chia thành nhiều ô, mỗi ô cho năng suất khác nhau. Bác muốn khoanh các vùng trồng sao cho mỗi vùng có tổng năng suất đạt mức yêu cầu, với số vùng khoanh đúng như kế hoạch.

Bác ghi lại năng suất từng ô rồi tính mức năng suất tối thiểu mỗi vùng cần đạt.

**Bối cảnh & Nhiệm vụ:**

Cho ma trận trọng số và số khu vực cần chia. Hãy lập trình tìm ngưỡng trọng số tối thiểu thỏa mãn yêu cầu phân đoạn ma trận.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả trên một dòng.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>5<br/>1 2 3 4 5<br/>``` | ```text<br/>15<br/>``` |

**Giải thích:**

* Kết quả tính toán phù hợp với yêu cầu của bài toán Tối Ưu Phân Đoạn Trọng Số Ma Trận 2D.



### Bài 15 [CPPB2-L03-15]: Chặt nhị phân song song (parallel binary search)

**Bối cảnh & Nhiệm vụ:**

Trạm khí tượng có nhiều cảm biến gửi số liệu về theo từng đợt. Kỹ sư trực cần trả lời cùng lúc nhiều câu hỏi dạng: với ngưỡng cho trước, đợt đo thứ mấy thì số liệu tích lũy mới vượt ngưỡng.

Thay vì trả lời từng câu hỏi một, anh kỹ sư xử lý tất cả các câu hỏi song song theo từng đợt số liệu.

**Bối cảnh & Nhiệm vụ:**

Cho dữ liệu các đợt đo và nhiều câu hỏi ngưỡng tích lũy. Hãy lập trình trả lời với mỗi câu hỏi đợt đo sớm nhất mà tổng tích lũy vượt ngưỡng.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả trên một dòng.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>5<br/>1 2 3 4 5<br/>``` | ```text<br/>15<br/>``` |

**Giải thích:**

* Kết quả tính toán phù hợp với yêu cầu của bài toán Chặt Nhị Phân Song Song (Parallel Binary Search).



### Bài 16 [CPPB2-L03-16]: Khoảng cách cực trị trên đa giác lồi

**Bối cảnh & Nhiệm vụ:**

Đội đo đạc vẽ lại bản đồ một khu đất hình đa giác lồi rồi cắm cọc tại các đỉnh. Chú kỹ sư muốn biết hai cọc nào đứng xa nhau nhất để đặt đường dây quan trắc chính xác.

Tổ đo đạc đi vòng quanh khu đất, ghi lại tọa độ từng cọc rồi so sánh các khoảng cách.

**Bối cảnh & Nhiệm vụ:**

Cho tọa độ các đỉnh của đa giác lồi. Hãy lập trình tìm khoảng cách lớn nhất (hoặc nhỏ nhất theo yêu cầu) giữa hai đỉnh của đa giác.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả trên một dòng.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>5<br/>1 2 3 4 5<br/>``` | ```text<br/>15<br/>``` |

**Giải thích:**

* Kết quả tính toán phù hợp với yêu cầu của bài toán Khoảng Cách Cực Trị Trên Đa Giác Lồi.



### Bài 17 [CPPB2-L03-17]: Chặt nhị phân song song

**Bối cảnh & Nhiệm vụ:**

Cho một hệ thống gồm $N$ trạm thiên văn và $Q$ thiên thạch di chuyển. Mỗi thiên thạch cần thu thập ít nhất $P_i$ đơn vị năng lượng từ các trạm thiên văn trong phạm vi kiểm soát của nó sau một số mốc thời gian $M$. Sau mỗi mốc thời gian $t$, một trạm thiên văn sẽ phát ra một lượng sóng năng lượng.

**Bối cảnh & Nhiệm vụ:**

Với mỗi thiên thạch, hãy tìm mốc thời gian $t$ nhỏ nhất ($1 \le t \le N$) để thiên thạch đó tích lũy đủ số năng lượng $P_i$. Nếu không thể tích lũy đủ sau tất cả $N$ mốc thời gian, hãy in ra `-1`.

**Đầu vào (Input):**

- Dòng 1: Gồm 2 số nguyên $N, Q$ ($1 \le N, Q \le 10^5$) — số mốc thời gian và số lượng thiên thạch.
- Dòng 2: $N$ số nguyên biểu thị năng lượng phát ra tại các trạm theo thứ tự thời gian.
- Dòng 3: $Q$ số nguyên $P_1, P_2, \dots, P_Q$ ($1 \le P_i \le 10^9$) — lượng năng lượng yêu cầu của từng thiên thạch.

**Đầu ra (Output):**

- In ra $Q$ dòng, mỗi dòng chứa mốc thời gian nhỏ nhất tương ứng cho từng thiên thạch.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>5 3<br/>10 20 30 40 50<br/>15 55 200<br/>``` | ```text<br/>2<br/>3<br/>-1<br/>``` |

**Giải thích:**

* Thiên thạch 1 cần $15$ năng lượng: tại mốc $t=1$ có $10$, tại mốc $t=2$ tích lũy tổng $30 \ge 15$, do đó đáp án là $2$.

* Thiên thạch 2 cần $55$ năng lượng: tại $t=3$ tích lũy tổng $60 \ge 55$, đáp án là $3$.

* Thiên thạch 3 cần $200$ năng lượng: sau cả $5$ mốc chỉ tích lũy được $150 < 200$, in ra `-1`.



### Bài 18 [CPPB2-L03-18]: Tìm cực tiểu của hàm bậc hai

**Bối cảnh & Nhiệm vụ:**

Cho hàm số bậc hai $f(x) = ax^2 + bx + c$ với hệ số $a > 0$ (hàm lồi trên tập số thực $\mathbb{R}$). Cần tìm giá trị của biến số $x$ trong đoạn $[L, R]$ sao cho giá trị $f(x)$ đạt cực tiểu.

**Bối cảnh & Nhiệm vụ:**

Hãy sử dụng thuật toán Tìm kiếm tam phân (Ternary Search) trên tập số thực để tìm hoành độ $x \in [L, R]$ làm cho $f(x)$ đạt giá trị nhỏ nhất với độ chính xác tuyệt đối không quá $10^{-6}$.

**Đầu vào (Input):**

- Một dòng duy nhất chứa 5 số thực $a, b, c, L, R$ ($a > 0, -10^6 \le b, c, L, R \le 10^6, L \le R$).

**Đầu ra (Output):**

- In ra giá trị $x$ tìm được với đúng 6 chữ số thập phân sau dấu phẩy.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>1 -4 4 0 5<br/>``` | ```text<br/>2.000000<br/>``` |

**Giải thích:**

* Hàm số $f(x) = x^2 - 4x + 4 = (x - 2)^2$ đạt giá trị nhỏ nhất bằng $0$ tại điểm cực trị $x = -b / (2a) = 2.000000$ thuộc đoạn $[0, 5]$.



### Bài 19 [CPPB2-L03-19]: Trung vị của hai mảng đã sắp xếp

**Bối cảnh & Nhiệm vụ:**

Cho hai mảng số nguyên $A$ gồm $N$ phần tử và $B$ gồm $M$ phần tử đều đã được sắp xếp theo thứ tự tăng dần. Trung vị của dãy hợp nhất gồm $N + M$ phần tử là phần tử ở chính giữa (nếu $N+M$ lẻ) hoặc trung bình cộng của 2 phần tử ở chính giữa (nếu $N+M$ chẵn).

**Bối cảnh & Nhiệm vụ:**

Hãy tìm trung vị của tập hợp tất cả các phần tử trong cả 2 mảng với độ phức tạp thời gian $\mathcal{O}(\log(\min(N, M)))$.

**Đầu vào (Input):**

- Dòng 1: Gồm 2 số nguyên $N, M$ ($1 \le N, M \le 10^5$).
- Dòng 2: $N$ số nguyên đã sắp xếp tăng dần của mảng $A$ ($|A_i| \le 10^9$).
- Dòng 3: $M$ số nguyên đã sắp xếp tăng dần của mảng $B$ ($|B_j| \le 10^9$).

**Đầu ra (Output):**

- In ra một số thực duy nhất là giá trị trung vị với đúng 1 chữ số thập phân sau dấu phẩy.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>2 2<br/>1 3<br/>2 4<br/>``` | ```text<br/>2.5<br/>``` |

**Giải thích:**

* Dãy hợp nhất sau khi sắp xếp là $[1, 2, 3, 4]$. Tổng số phần tử chẵn ($4$), hai phần tử chính giữa là $2$ và $3$, trung vị là $(2 + 3) / 2 = 2.5$.



### Bài 20 [CPPB2-L03-20]: Tam giác có diện tích lớn nhất

**Bối cảnh & Nhiệm vụ:**

Cho một đa giác lồi gồm $N$ đỉnh trên mặt phẳng tọa độ $Oxy$ được liệt kê theo chiều ngược chiều kim đồng hồ. Cần chọn ra 3 đỉnh phân biệt của đa giác lồi sao cho tam giác tạo bởi 3 đỉnh này có diện tích lớn nhất.

**Bối cảnh & Nhiệm vụ:**

Hãy lập trình tìm diện tích lớn nhất của tam giác được tạo từ 3 đỉnh bất kỳ của đa giác lồi bằng kỹ thuật Hai con trỏ quay (Rotating Calipers) với độ phức tạp $\mathcal{O}(N^2)$ hoặc $\mathcal{O}(N)$.

**Đầu vào (Input):**

- Dòng 1: Gồm 1 số nguyên $N$ ($3 \le N \le 3000$) — số đỉnh của đa giác lồi.
- $N$ dòng tiếp theo: Mỗi dòng gồm 2 số nguyên $x_i, y_i$ ($|x_i|, |y_i| \le 10^9$) — tọa độ đỉnh thứ $i$.

**Đầu ra (Output):**

- In ra diện tích lớn nhất tìm được với đúng 1 chữ số thập phân sau dấu phẩy.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>4<br/>0 0<br/>4 0<br/>4 3<br/>0 3<br/>``` | ```text<br/>6.0<br/>``` |

**Giải thích:**

* 4 đỉnh tạo thành hình chữ nhật kích thước $4 \times 3$. Chọn 3 đỉnh $(0,0), (4,0), (4,3)$ tạo thành tam giác vuông có diện tích $S = \frac{1}{2} \times 4 \times 3 = 6.0$.



### Bài 21 [CPPB2-L03-21]: Chặt Nhị Phân Khoảng Cách K Điểm

**Bối cảnh & Nhiệm vụ:**

Thầy giáo cắm $K$ cọc tiêu dọc sân trường để tổ chức trò chơi vận động. Thầy muốn chọn vị trí các cọc sao cho hai cọc gần nhau nhất cũng cách nhau càng xa càng tốt, để học sinh có chỗ chạy thoải mái.

Thầy đo các vị trí có thể cắm cọc rồi tính cách chọn hợp lý nhất.

**Bối cảnh & Nhiệm vụ:**

Cho các vị trí có thể đặt và số điểm $K$ cần chọn. Hãy lập trình tìm khoảng cách nhỏ nhất lớn nhất có thể giữa hai điểm được chọn.

**Đầu vào (Input):**

- Dòng 1: Gồm các số nguyên biểu thị tham số kích thước bài toán ($1 \le N \le 10^5$).
- Các dòng tiếp theo: Chứa các phần tử của mảng hoặc các truy vấn cần xử lý.

**Đầu ra (Output):**

- In ra kết quả tối ưu của bài toán trên từng dòng tương ứng.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>5<br/>1 2 3 4 5<br/>``` | ```text<br/>15<br/>``` |

**Giải thích:**

* Thuật toán khởi tạo cấu trúc dữ liệu, duyệt và tính toán kết quả tối ưu của Chat Nhi Phan Khoang Cach K Diem.



### Bài 22 [CPPB2-L03-22]: Chặt Nhị Phân Phân Số Tối Giản

**Bối cảnh & Nhiệm vụ:**

Trong tiết học phân số, cô giáo viết lên bảng tất cả các phân số có thể tạo thành từ các số trong phạm vi cho phép rồi xếp chúng theo thứ tự tăng dần. Bạn Lan được hỏi phân số đứng thứ $K$ trong danh sách đó là phân số nào.

Cả lớp cùng rút gọn từng phân số về dạng tối giản trước khi xếp hạng.

**Bối cảnh & Nhiệm vụ:**

Cho phạm vi tạo phân số và số $K$. Hãy lập trình tìm phân số tối giản đứng thứ $K$ khi xếp tăng dần.

**Đầu vào (Input):**

- Dòng 1: Gồm các số nguyên biểu thị tham số kích thước bài toán ($1 \le N \le 10^5$).
- Các dòng tiếp theo: Chứa các phần tử của mảng hoặc các truy vấn cần xử lý.

**Đầu ra (Output):**

- In ra kết quả tối ưu của bài toán trên từng dòng tương ứng.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>5<br/>1 2 3 4 5<br/>``` | ```text<br/>15<br/>``` |

**Giải thích:**

* Thuật toán khởi tạo cấu trúc dữ liệu, duyệt và tính toán kết quả tối ưu của Chat Nhi Phan Phan So Toi Gian.



# Bài 04: Kỹ thuật mảng: Hai con trỏ, Cửa sổ trượt, Mảng tiền tố & Mảng hiệu

## 1. Khái niệm & bản chất của tối ưu hóa tuyến tính trên mảng

Trong lập trình thi đấu, các kỹ thuật xử lý mảng như **Hai con trỏ (Two Pointers)**, **Cửa sổ trượt (Sliding Window)**, **Mảng tiền tố (Prefix Sum)**, **Mảng hiệu (Difference Array)** và **Nén tọa độ (Coordinate Compression)** là bộ công cụ nền tảng giúp chuyển đổi các thuật toán ngây thơ đa biến $\mathcal{O}(N^2)$ hoặc $\mathcal{O}(N \times Q)$ về độ phức tạp tối ưu tuyến tính $\mathcal{O}(N)$ hoặc $\mathcal{O}(N \log N)$.

Ở Level 2, ta tập trung vào **Kỹ thuật kết hợp đa chiều & Mảng 2D**:

* **Hai con trỏ co giãn & Cửa sổ trượt linh hoạt:** Duy trì bất biến về tần suất, số lượng phần tử phân biệt hoặc tổng điều kiện khi kích thước cửa sổ thay đổi liên tục.
* **Mảng tiền tố 2D (2D Prefix Sum):** Trả lời truy vấn tính tổng hình chữ nhật con bất kỳ trên ma trận $N \times M$ trong $\mathcal{O}(1)$.
* **Mảng hiệu 2D (2D Difference Array):** Cập nhật cộng một giá trị lên toàn bộ vùng hình chữ nhật trong $\mathcal{O}(1)$ và khôi phục ma trận trong $\mathcal{O}(NM)$.
* **Nén tọa độ (Coordinate Compression):** Ánh xạ các giá trị rời rạc rất lớn ($A_i \le 10^9$) về dải chỉ số nhỏ liên tiếp $[1, N]$ mà vẫn bảo toàn hoàn toàn quan hệ thứ tự $A_i < A_j$.




![Sơ đồ 2D Prefix Sum](/Users/vu/Developer/ikhEdu_lessons/courses/cpp-bang-b-level2/lessons/lesson-04-ky-thuat-mang-nang-cao/assets/l04_2d_prefix_sum_visual.png)



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


### Bài 01 [CPPB2-L04-01]: Truy vấn tổng ma trận con 2d

**Bối cảnh & Nhiệm vụ:**

Cho ma trận $A$ kích thước $N \times M$. Có $Q$ truy vấn tính tổng hình chữ nhật từ $(x_1, y_1)$ đến $(x_2, y_2)$.

**Bối cảnh & Nhiệm vụ:**

Cho ma trận $A$ kích thước $N \times M$ và $Q$ truy vấn hình chữ nhật $(x_1, y_1)$ đến $(x_2, y_2)$. Hãy lập trình tính tổng các ô trong mỗi hình chữ nhật được hỏi.

**Đầu vào (Input):**

- Dòng 1: $N, M, Q$ ($1 \le N, M \le 1000, 1 \le Q \le 10^5$). $N$ dòng tiếp theo chứa ma trận. $Q$ dòng sau: $x_1, y_1, x_2, y_2$.

**Đầu ra (Output):**

- In ra tổng mỗi hình chữ nhật con trên một dòng.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>3 3 2<br/>1 2 3<br/>4 5 6<br/>7 8 9<br/>1 1 2 2<br/>2 2 3 3<br/>``` | ```text<br/>12<br/>28<br/>``` |

**Giải thích:**

* Truy vấn 1 $(1, 1)$ đến $(2, 2)$ gồm các ô $1, 2, 4, 5$ nên tổng là $1 + 2 + 4 + 5 = 12$.

* Truy vấn 2 $(2, 2)$ đến $(3, 3)$ gồm các ô $5, 6, 8, 9$ nên tổng là $5 + 6 + 8 + 9 = 28$.



### Bài 02 [CPPB2-L04-02]: Cập nhật hình chữ nhật ma trận 2d

**Bối cảnh & Nhiệm vụ:**

Ban quản lý ký túc xá theo dõi bảng nội trú hình chữ nhật, mỗi ô ghi số sinh viên đang ở. Mỗi đợt, ban quản lý cộng thêm một số sinh viên vào tất cả các phòng trong một khu hình chữ nhật rồi cần biết nhanh số sinh viên của từng phòng.

Cô quản lý ghi lại các đợt điều chuyển rồi cập nhật bảng số liệu sao cho kịp giờ điểm danh.

**Bối cảnh & Nhiệm vụ:**

Cho ma trận ban đầu và các phép cộng trên hình chữ nhật con. Hãy lập trình tính giá trị cuối cùng của ma trận sau mọi phép cập nhật.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>5<br/>1 2 3 4 5<br/>``` | ```text<br/>15<br/>``` |

**Giải thích:**

* Kết quả tính toán phù hợp với yêu cầu của bài toán Cập Nhật Hình Chữ Nhật Ma Trận 2D.



### Bài 03 [CPPB2-L04-03]: Đoạn con ngắn nhất có tổng $\ge s$

**Bối cảnh & Nhiệm vụ:**

Huấn luyện viên ghi lại số bước chạy của vận động viên mỗi ngày. Anh muốn tìm chuỗi ngày liên tiếp ngắn nhất mà tổng số bước đạt ít nhất mức $S$ để khen thưởng sự bứt phá.

Anh lật lại nhật ký luyện tập, mở rộng rồi thu hẹp từng cửa sổ ngày để tìm chuỗi ngắn nhất.

**Bối cảnh & Nhiệm vụ:**

Cho dãy số và ngưỡng $S$. Hãy lập trình tìm độ dài đoạn con liên tiếp ngắn nhất có tổng không nhỏ hơn $S$.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>5<br/>1 2 3 4 5<br/>``` | ```text<br/>15<br/>``` |

**Giải thích:**

* Kết quả tính toán phù hợp với yêu cầu của bài toán Đoạn Con Ngắn Nhất Có Tổng $\ge S$.



### Bài 04 [CPPB2-L04-04]: Nén tọa độ & đếm tần suất trên dải lớn

**Bối cảnh & Nhiệm vụ:**

Trạm thu phí ghi lại biển số xe đi qua trong ngày, có những biển số rất lớn và thưa thớt. Nhân viên thống kê muốn gom các biển số về thứ hạng liên tiếp để đếm tần suất mỗi loại xe cho gọn.

Anh nhân viên liệt kê tất cả biển số xuất hiện rồi đánh số lại từ đầu để dễ đếm.

**Bối cảnh & Nhiệm vụ:**

Cho dãy tọa độ (có thể rất lớn) và các truy vấn đếm. Hãy lập trình nén tọa độ rồi trả lời tần suất xuất hiện của từng giá trị được hỏi.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>5<br/>1 2 3 4 5<br/>``` | ```text<br/>15<br/>``` |

**Giải thích:**

* Kết quả tính toán phù hợp với yêu cầu của bài toán Nén Tọa Độ & Đếm Tần Suất Trên Dải Lớn.



### Bài 05 [CPPB2-L04-05]: Đoạn con dài nhất có không quá k số khác nhau

**Bối cảnh & Nhiệm vụ:**

Cô giáo ghi lại màu áo học sinh xếp hàng vào lớp mỗi sáng. Cô muốn tìm đoạn hàng dài nhất mà trong đó số màu áo khác nhau không vượt quá $K$ để chụp ảnh kỷ niệm đồng đều.

Cô đi dọc hàng, nới rộng rồi thu hẹp đoạn quan sát sao cho số màu áo luôn trong giới hạn.

**Bối cảnh & Nhiệm vụ:**

Cho dãy số và số $K$. Hãy lập trình tìm độ dài đoạn con liên tiếp dài nhất chứa không quá $K$ giá trị khác nhau.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>5<br/>1 2 3 4 5<br/>``` | ```text<br/>15<br/>``` |

**Giải thích:**

* Kết quả tính toán phù hợp với yêu cầu của bài toán Đoạn Con Dài Nhất Có Không Quá K Số Khác Nhau.



### Bài 06 [CPPB2-L04-06]: Ma trận con có tổng lớn nhất (maximum submatrix sum)

**Bối cảnh & Nhiệm vụ:**

Bác nông dân có cánh đồng hình chữ nhật, mỗi ô có thể lãi hoặc lỗ tùy mùa vụ. Bác muốn khoanh một vùng hình chữ nhật có tổng lợi nhuận lớn nhất để tập trung chăm sóc.

Bác ghi lại lợi nhuận từng ô rồi so sánh các vùng có thể khoanh được.

**Bối cảnh & Nhiệm vụ:**

Cho ma trận số nguyên. Hãy lập trình tìm tổng lớn nhất của một hình chữ nhật con bất kỳ trong ma trận.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>5<br/>1 2 3 4 5<br/>``` | ```text<br/>15<br/>``` |

**Giải thích:**

* Kết quả tính toán phù hợp với yêu cầu của bài toán Ma Trận Con Có Tổng Lớn Nhất (Maximum Submatrix Sum).



### Bài 07 [CPPB2-L04-07]: Diện tích phủ bởi các hình chữ nhật rời rạc

**Bối cảnh & Nhiệm vụ:**

Trên sân trường, các lớp dựng gian hàng hội chợ hình chữ nhật, gian nọ có thể chờm lên gian kia. Ban tổ chức muốn biết tổng diện tích mặt sân thực sự bị các gian hàng che phủ.

Các bạn vẽ lại vị trí từng gian hàng lên giấy kẻ ô rồi tính phần diện tích bị phủ ít nhất một lần.

**Bối cảnh & Nhiệm vụ:**

Cho danh sách các hình chữ nhật rời rạc trên mặt phẳng. Hãy lập trình tính tổng diện tích bị phủ bởi ít nhất một hình chữ nhật.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>5<br/>1 2 3 4 5<br/>``` | ```text<br/>15<br/>``` |

**Giải thích:**

* Kết quả tính toán phù hợp với yêu cầu của bài toán Diện Tích Phủ Bởi Các Hình Chữ Nhật Rời Rạc.



### Bài 08 [CPPB2-L04-08]: Đếm cặp đoạn thẳng chồng lấn nhau

**Bối cảnh & Nhiệm vụ:**

Trên tuyến đường chạy, mỗi vận động viên đăng ký một đoạn đường mình sẽ chạy tiếp sức. Ban trọng tài muốn đếm có bao nhiêu cặp vận động viên có đoạn đường giao nhau để sắp xếp lịch xuất phát.

Tổ trọng tài ghi lại điểm đầu và điểm cuối của từng người rồi đếm các cặp chồng lấn.

**Bối cảnh & Nhiệm vụ:**

Cho danh sách các đoạn thẳng trên trục số. Hãy lập trình đếm số cặp đoạn thẳng có phần giao nhau.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>5<br/>1 2 3 4 5<br/>``` | ```text<br/>15<br/>``` |

**Giải thích:**

* Kết quả tính toán phù hợp với yêu cầu của bài toán Đếm Cặp Đoạn Thẳng Chồng Lấn Nhau.



### Bài 09 [CPPB2-L04-09]: Cửa sổ trượt đếm số lượng xâu anagram

**Bối cảnh & Nhiệm vụ:**

Trong trò chơi ô chữ, bạn Mai có một xâu chữ dài và một từ khóa cần tìm các phiên bản đảo chữ của nó. Bạn muốn đếm xem có bao nhiêu đoạn con trong xâu dài là một cách sắp xếp lại các chữ cái của từ khóa.

Mai trượt một khung cửa sổ dọc theo xâu chữ, mỗi lần so sánh tần suất chữ cái trong khung với từ khóa.

**Bối cảnh & Nhiệm vụ:**

Cho xâu văn bản và từ khóa. Hãy lập trình đếm số đoạn con của văn bản là một hoán vị (anagram) của từ khóa.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>5<br/>1 2 3 4 5<br/>``` | ```text<br/>15<br/>``` |

**Giải thích:**

* Kết quả tính toán phù hợp với yêu cầu của bài toán Cửa Sổ Trượt Đếm Số Lượng Xâu Anagram.



### Bài 10 [CPPB2-L04-10]: Đếm hình vuông con có tổng đúng bằng k

**Bối cảnh & Nhiệm vụ:**

Cô giáo vẽ một bảng số hình vuông cho cả lớp. Nhóm bạn An được giao nhiệm vụ đếm xem có bao nhiêu ô vuông con trong bảng có tổng các số bên trong đúng bằng $K$.

Cả nhóm kẻ khung vuông đủ mọi kích cỡ đặt lên bảng rồi cộng tổng từng khung để kiểm tra.

**Bối cảnh & Nhiệm vụ:**

Cho ma trận số và số $K$. Hãy lập trình đếm số hình vuông con có tổng các ô đúng bằng $K$.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>5<br/>1 2 3 4 5<br/>``` | ```text<br/>15<br/>``` |

**Giải thích:**

* Kết quả tính toán phù hợp với yêu cầu của bài toán Đếm Hình Vuông Con Có Tổng Đúng Bằng K.



### Bài 11 [CPPB2-L04-11]: Khử chiều 3-sum & 4-sum hai con trỏ

**Bối cảnh & Nhiệm vụ:**

Trong buổi sinh hoạt câu lạc bộ toán, các bạn viết lên bảng một dãy số rồi đố nhau tìm các bộ ba (hoặc bộ bốn) có tổng đúng bằng một số cho trước.

Cả nhóm sắp xếp dãy số rồi dùng hai đầu danh sách kẹp dần vào giữa để tìm các bộ số thỏa mãn.

**Bối cảnh & Nhiệm vụ:**

Cho dãy số và giá trị mục tiêu. Hãy lập trình liệt kê (đếm) các bộ ba (và bộ bốn) có tổng đúng bằng giá trị mục tiêu.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả trên một dòng.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>5<br/>1 2 3 4 5<br/>``` | ```text<br/>15<br/>``` |

**Giải thích:**

* Kết quả tính toán phù hợp với yêu cầu của bài toán Khử Chiều 3-Sum & 4-Sum Hai Con Trỏ.



### Bài 12 [CPPB2-L04-12]: Đếm số đoạn con có hiệu max - min $\le k$

**Bối cảnh & Nhiệm vụ:**

Thầy giáo ghi lại nhiệt độ phòng học mỗi giờ trong ngày. Thầy muốn đếm xem có bao nhiêu khoảng thời gian liên tiếp mà chênh lệch giữa nhiệt độ cao nhất và thấp nhất không vượt quá $K$.

Thầy trượt một cửa sổ thời gian dọc theo bảng ghi, mỗi lần ghi nhận nhiệt độ cao nhất và thấp nhất trong cửa sổ.

**Bối cảnh & Nhiệm vụ:**

Cho dãy số và số $K$. Hãy lập trình đếm số đoạn con liên tiếp có hiệu giữa phần tử lớn nhất và nhỏ nhất không vượt quá $K$.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả trên một dòng.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>5<br/>1 2 3 4 5<br/>``` | ```text<br/>15<br/>``` |

**Giải thích:**

* Kết quả tính toán phù hợp với yêu cầu của bài toán Đếm Số Đoạn Con Có Hiệu Max - Min $\le K$.



### Bài 13 [CPPB2-L04-13]: Đoạn con ngắn nhất chứa đầy đủ bảng chữ cái

**Bối cảnh & Nhiệm vụ:**

Bạn Hoa chơi trò tìm đoạn văn ngắn nhất chứa đủ mọi chữ cái trong bảng chữ cái. Bạn có một xâu ký tự dài và muốn cắt ra đoạn liên tiếp ngắn nhất mà trong đó mỗi chữ cái đều xuất hiện ít nhất một lần.

Hoa mở rộng khung chọn từng chút một, khi đã đủ chữ cái thì thu hẹp lại để tìm đoạn ngắn nhất.

**Bối cảnh & Nhiệm vụ:**

Cho xâu ký tự. Hãy lập trình tìm độ dài đoạn con liên tiếp ngắn nhất chứa đầy đủ mọi chữ cái trong bảng chữ cái.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả trên một dòng.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>5<br/>1 2 3 4 5<br/>``` | ```text<br/>15<br/>``` |

**Giải thích:**

* Kết quả tính toán phù hợp với yêu cầu của bài toán Đoạn Con Ngắn Nhất Chứa Đầy Đủ Bảng Chữ Cái.



### Bài 14 [CPPB2-L04-14]: Mảng hiệu trên cây (Tree difference array)

**Bối cảnh & Nhiệm vụ:**

Trường học trồng cây theo sơ đồ hình cây, mỗi phòng học là một nút. Mỗi đợt, nhà trường cộng thêm một lượng sách vào tất cả các phòng trên đường đi giữa hai phòng cho trước, cuối cùng cần biết mỗi phòng có bao nhiêu sách.

Bác thủ thư ghi lại từng đợt điều chuyển rồi tổng hợp số sách của mỗi phòng một lần.

**Bối cảnh & Nhiệm vụ:**

Cho cây với $N$ nút và các phép cộng trên đường đi $(u, v)$. Hãy lập trình tính giá trị cuối cùng của mỗi nút sau mọi phép cập nhật.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả trên một dòng.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>5<br/>1 2 3 4 5<br/>``` | ```text<br/>15<br/>``` |

**Giải thích:**

* Kết quả tính toán phù hợp với yêu cầu của bài toán Mảng Hiệu Trên Cây (Tree Difference Array).



### Bài 15 [CPPB2-L04-15]: Đếm tam giác có độ dài cạnh hợp lệ

**Bối cảnh & Nhiệm vụ:**

Câu lạc bộ thủ công có một bó que với đủ loại độ dài. Các bạn muốn đếm xem có bao nhiêu cách chọn ra ba que để ghép thành một hình tam giác đúng nghĩa.

Cả nhóm sắp xếp các que từ ngắn đến dài rồi thử từng cặp, đếm xem que thứ ba dài bao nhiêu thì ghép được.

**Bối cảnh & Nhiệm vụ:**

Cho độ dài các que. Hãy lập trình đếm số bộ ba có thể ghép thành một tam giác không suy biến.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả trên một dòng.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>5<br/>1 2 3 4 5<br/>``` | ```text<br/>15<br/>``` |

**Giải thích:**

* Kết quả tính toán phù hợp với yêu cầu của bài toán Đếm Tam Giác Có Độ Dài Cạnh Hợp Lệ.



### Bài 16 [CPPB2-L04-16]: Quét đường thẳng nén tọa độ (sweep-line area 2d)

**Bối cảnh & Nhiệm vụ:**

Phường vẽ bản đồ các khu đất hình chữ nhật để tính tiền sử dụng đất. Cán bộ địa chính cần tính tổng diện tích bị phủ bởi ít nhất một khu đất, vì phần chồng lấn chỉ tính một lần.

Anh cán bộ kẻ các đường thẳng đứng qua mọi cạnh khu đất rồi tính diện tích từng dải một.

**Bối cảnh & Nhiệm vụ:**

Cho danh sách các hình chữ nhật trên mặt phẳng. Hãy lập trình tính tổng diện tích hợp bị phủ bởi ít nhất một hình chữ nhật.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả trên một dòng.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>5<br/>1 2 3 4 5<br/>``` | ```text<br/>15<br/>``` |

**Giải thích:**

* Kết quả tính toán phù hợp với yêu cầu của bài toán Quét Đường Thẳng Nén Tọa Độ (Sweep-line Area 2D).



### Bài 17 [CPPB2-L04-17]: Diện tích hợp các hình chữ nhật

**Bối cảnh & Nhiệm vụ:**

Trên mặt phẳng tọa độ $Oxy$, cho $N$ hình chữ nhật có các cạnh song song với các trục tọa độ. Mỗi hình chữ nhật thứ $i$ được xác định bởi tọa độ góc dưới trái $(x_1, y_1)$ và góc trên phải $(x_2, y_2)$.

**Bối cảnh & Nhiệm vụ:**

Hãy tính tổng diện tích của phần mặt phẳng bị phủ bởi ít nhất một trong $N$ hình chữ nhật bằng thuật toán Quét đường (Sweep-line) kết hợp Nén tọa độ.

**Đầu vào (Input):**

- Dòng 1: Gồm 1 số nguyên $N$ ($1 \le N \le 2000$) — số lượng hình chữ nhật.
- $N$ dòng tiếp theo: Mỗi dòng gồm 4 số nguyên $x_1, y_1, x_2, y_2$ ($0 \le x_1 < x_2 \le 10^9, 0 \le y_1 < y_2 \le 10^9$).

**Đầu ra (Output):**

- In ra một số nguyên duy nhất là tổng diện tích hợp của các hình chữ nhật.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>2<br/>10 10 20 20<br/>15 15 25 25<br/>``` | ```text<br/>175<br/>``` |

**Giải thích:**

* Hình chữ nhật 1 có diện tích $10 \times 10 = 100$.

* Hình chữ nhật 2 có diện tích $10 \times 10 = 100$.

* Phần giao nhau là hình chữ nhật $[15, 20] \times [15, 20]$ có diện tích $5 \times 5 = 25$.

* Tổng diện tích hợp phủ = $100 + 100 - 25 = 175$.



### Bài 18 [CPPB2-L04-18]: Mảng hiệu trên hình vuông xoay 45 độ

**Bối cảnh & Nhiệm vụ:**

Cho một lưới ô vuông kích thước $N \times N$, ban đầu tất cả các ô đều có giá trị bằng $0$. Có $Q$ phép cập nhật, mỗi phép cập nhật cho một ô tâm $(x, y)$, bán kính khoảng cách Manhattan $d$ và một giá trị cộng thêm $val$. Nghĩa là mọi ô $(r, c)$ thỏa mãn $|r - x| + |c - y| \le d$ đều được cộng thêm giá trị $val$.

**Bối cảnh & Nhiệm vụ:**

Hãy tìm giá trị lớn nhất trong toàn bộ lưới ô vuông $N \times N$ sau khi thực hiện xong tất cả $Q$ phép cập nhật.

**Đầu vào (Input):**

- Dòng 1: Gồm 2 số nguyên $N, Q$ ($1 \le N \le 1000, 1 \le Q \le 10^5$).
- $Q$ dòng tiếp theo: Mỗi dòng gồm 4 số nguyên $x, y, d, val$ ($1 \le x, y \le N, 0 \le d \le 2N, 1 \le val \le 10^6$).

**Đầu ra (Output):**

- In ra một số nguyên duy nhất là giá trị lớn nhất trong lưới sau $Q$ phép cập nhật.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>3 2<br/>2 2 1 5<br/>1 1 0 3<br/>``` | ```text<br/>8<br/>``` |

**Giải thích:**

* Phép cập nhật 1: Cộng $5$ vào vùng Manhattan bán kính $1$ quanh ô $(2, 2)$ gồm các ô $(2,2), (1,2), (3,2), (2,1), (2,3)$.

* Phép cập nhật 2: Cộng $3$ vào riêng ô $(1, 1)$. Ô $(2, 2)$ đạt giá trị lớn nhất là $5$, hoặc ô $(1, 2)$ đạt $5$.



### Bài 19 [CPPB2-L04-19]: Nén Tọa Độ Đa Chiều 3D

**Bối cảnh & Nhiệm vụ:**

Trung tâm dữ liệu lưu trữ các sự kiện trong không gian ba chiều, mỗi chiều có tọa độ rất lớn và thưa. Kỹ sư muốn gom mỗi chiều về thứ hạng liên tiếp để lưu trữ và tra cứu cho gọn nhẹ.

Anh liệt kê tất cả tọa độ xuất hiện trên từng chiều rồi đánh số lại từ đầu.

**Bối cảnh & Nhiệm vụ:**

Cho tập điểm trong không gian ba chiều với tọa độ lớn. Hãy lập trình nén tọa độ từng chiều rồi trả lời các truy vấn theo yêu cầu.

**Đầu vào (Input):**

- Dòng 1: Gồm các số nguyên biểu thị tham số kích thước bài toán ($1 \le N \le 10^5$).
- Các dòng tiếp theo: Chứa các phần tử của mảng hoặc các truy vấn cần xử lý.

**Đầu ra (Output):**

- In ra kết quả tối ưu của bài toán trên từng dòng tương ứng.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>5<br/>1 2 3 4 5<br/>``` | ```text<br/>15<br/>``` |

**Giải thích:**

* Thuật toán khởi tạo cấu trúc dữ liệu, duyệt và tính toán kết quả tối ưu của Nen Toa Do Da Chieu 3d.



### Bài 20 [CPPB2-L04-20]: Đếm số bộ ba tam giác hợp lệ

**Bối cảnh & Nhiệm vụ:**

Cho một mảng $A$ gồm $N$ số nguyên dương biểu thị độ dài các thanh gỗ. Người ta muốn chọn ra 3 thanh gỗ có độ dài $A_i, A_j, A_k$ ($i < j < k$) sao cho 3 thanh gỗ này có thể ghép thành một tam giác không suy biến (nghĩa là thỏa mãn $A_i + A_j > A_k$ với $A_i \le A_j \le A_k$).

**Bối cảnh & Nhiệm vụ:**

Hãy đếm số lượng bộ ba chỉ số $(i, j, k)$ thỏa mãn điều kiện tạo thành tam giác bằng kỹ thuật Hai con trỏ với độ phức tạp $\mathcal{O}(N^2)$.

**Đầu vào (Input):**

- Dòng 1: Gồm 1 số nguyên $N$ ($3 \le N \le 5000$) — số lượng thanh gỗ.
- Dòng 2: $N$ số nguyên dương $A_1, A_2, \dots, A_N$ ($1 \le A_i \le 10^9$).

**Đầu ra (Output):**

- In ra một số nguyên duy nhất là số lượng bộ ba tam giác hợp lệ.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>4<br/>4 6 3 7<br/>``` | ```text<br/>3<br/>``` |

**Giải thích:**

* Sắp xếp mảng: $[3, 4, 6, 7]$.

* Các bộ ba tam giác hợp lệ: $(3, 4, 6)$ vì $3+4 > 6$, $(3, 6, 7)$ vì $3+6 > 7$, $(4, 6, 7)$ vì $4+6 > 7$. Tổng cộng có $3$ bộ ba.



### Bài 21 [CPPB2-L04-21]: Đếm xâu con có đúng k ký tự khác nhau

**Bối cảnh & Nhiệm vụ:**

Cho một xâu ký tự $S$ chỉ gồm các chữ cái tiếng Anh in thường và một số nguyên dương $K$.

**Bối cảnh & Nhiệm vụ:**

Hãy đếm số lượng xâu con liên tiếp của $S$ chứa đúng $K$ ký tự phân biệt bằng kỹ thuật Cửa sổ trượt (Sliding Window / Two Pointers).

**Đầu vào (Input):**

- Dòng 1: Xâu ký tự $S$ ($1 \le |S| \le 10^5$).
- Dòng 2: Một số nguyên $K$ ($1 \le K \le 26$).

**Đầu ra (Output):**

- In ra một số nguyên duy nhất là số lượng xâu con thỏa mãn.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>pqpqs<br/>2<br/>``` | ```text<br/>7<br/>``` |

**Giải thích:**

* Các xâu con có đúng 2 ký tự khác nhau: `pq` (vị trí 0..1), `pqp` (0..2), `pqpq` (0..3), `qp` (1..2), `qpq` (1..3), `pq` (2..3), `qs` (3..4). Tổng cộng có $7$ xâu.



### Bài 22 [CPPB2-L04-22]: Ma Trận Tổng Lớn Nhất (Kadane 2D)

**Bối cảnh & Nhiệm vụ:**

Bác nông dân có cánh đồng hình chữ nhật, mỗi ô có thể lãi hoặc lỗ tùy mùa vụ. Vụ này bác muốn khoanh một vùng hình chữ nhật có tổng lợi nhuận lớn nhất để tập trung đầu tư.

Bác ghi lại lợi nhuận từng ô rồi so sánh các vùng có thể khoanh được.

**Bối cảnh & Nhiệm vụ:**

Cho ma trận số nguyên. Hãy lập trình tìm tổng lớn nhất của một hình chữ nhật con bất kỳ trong ma trận.

**Đầu vào (Input):**

- Dòng 1: Gồm các số nguyên biểu thị tham số kích thước bài toán ($1 \le N \le 10^5$).
- Các dòng tiếp theo: Chứa các phần tử của mảng hoặc các truy vấn cần xử lý.

**Đầu ra (Output):**

- In ra kết quả tối ưu của bài toán trên từng dòng tương ứng.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>5<br/>1 2 3 4 5<br/>``` | ```text<br/>15<br/>``` |

**Giải thích:**

* Thuật toán khởi tạo cấu trúc dữ liệu, duyệt và tính toán kết quả tối ưu của Ma Tran Tong Lon Nhat Kadane 2d.



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


### Bài 01 [CPPB2-L05-01]: Đếm cặp nghịch thế

**Bối cảnh & Nhiệm vụ:**

Cho mảng $N$ phần tử. Đếm số cặp $(i, j)$ thỏa mãn $1 \le i < j \le N$ và $A_i > A_j$.

**Bối cảnh & Nhiệm vụ:**

Cho mảng $A$ gồm $N$ số nguyên. Hãy lập trình đếm số cặp $(i, j)$ thỏa mãn $1 \le i < j \le N$ và $A_i > A_j$, rồi in ra tổng số cặp đếm được.

**Đầu vào (Input):**

- Dòng 1: $N$ ($1 \le N \le 10^5$). Dòng 2: $N$ số $A_i$ ($1 \le A_i \le 10^9$).

**Đầu ra (Output):**

- In ra tổng số cặp nghịch thế.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>5<br/>2 4 1 3 5<br/>``` | ```text<br/>3<br/>``` |

**Giải thích:**

Với mảng $[2, 4, 1, 3, 5]$, xét lần lượt từng vị trí đứng trước:

- Số $2$: trong các số đứng sau nó ($4, 1, 3, 5$), chỉ có $1$ nhỏ hơn $2$ nên đếm được $1$ cặp.

- Số $4$: trong các số đứng sau nó ($1, 3, 5$), có $1$ và $3$ nhỏ hơn $4$ nên đếm được $2$ cặp.

- Số $1$: không có số nào đứng sau nhỏ hơn $1$.

- Số $3$: số đứng sau duy nhất là $5$ lớn hơn $3$ nên không đếm thêm.

- Số $5$: là số cuối cùng nên không tạo cặp nào.

Cộng lại: $1 + 2 = 3$. Vậy đáp án là $3$.



### Bài 02 [CPPB2-L05-02]: Cái túi kích thước nhỏ (knapsack $n \le 40$)

**Bối cảnh & Nhiệm vụ:**

Bác thủ kho cần xếp hàng lên một chuyến xe tải có sức chở giới hạn. Mỗi kiện hàng có khối lượng và giá trị khác nhau, mà số kiện thì khá nhiều (vài chục kiện) nên không thể thử hết mọi cách bằng tay.

Bác muốn chọn ra những kiện mang đi sao cho tổng giá trị cao nhất mà xe vẫn chở nổi.

**Bối cảnh & Nhiệm vụ:**

Cho $N$ món đồ ($N \le 40$), mỗi món có khối lượng và giá trị, cùng sức chứa của chiếc túi. Hãy lập trình chọn ra một tập con các món đồ có tổng giá trị lớn nhất mà tổng khối lượng không vượt quá sức chứa.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>5<br/>1 2 3 4 5<br/>``` | ```text<br/>15<br/>``` |

**Giải thích:**

* Kết quả tính toán phù hợp với yêu cầu của bài toán Cái Túi Kích Thước Nhỏ (Knapsack $N \le 40$).



### Bài 03 [CPPB2-L05-03]: Tập con có tổng gần s nhất

**Bối cảnh & Nhiệm vụ:**

Cô kế toán được giao một khoản tiền mục tiêu $S$ để mua sắm thiết bị. Mỗi món đồ có một mức giá riêng, và cô chỉ được mua mỗi món nhiều nhất một lần.

Cô cần chọn một nhóm món đồ sao cho tổng giá tiền gần với $S$ nhất có thể, để số tiền thừa hay thiếu là ít nhất.

**Bối cảnh & Nhiệm vụ:**

Cho dãy gồm $N$ số nguyên và một số mục tiêu $S$. Hãy lập trình tìm một tập con có tổng gần với $S$ nhất, tức hiệu tuyệt đối giữa tổng của tập con và $S$ là nhỏ nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>5<br/>1 2 3 4 5<br/>``` | ```text<br/>15<br/>``` |

**Giải thích:**

* Kết quả tính toán phù hợp với yêu cầu của bài toán Tập Con Có Tổng Gần S Nhất.



### Bài 04 [CPPB2-L05-04]: Giải phương trình $4$ ẩn tuyến tính (4-sum mitm)

**Bối cảnh & Nhiệm vụ:**

Trong ngày hội thể thao, ban tổ chức có bốn bảng danh sách điểm số của bốn đội. Mỗi bảng ghi điểm của các vận động viên đội mình.

Ban tổ chức muốn biết có bao nhiêu cách chọn mỗi bảng đúng một con số sao cho tổng bốn số được chọn bằng $0$, để trao giải đồng đội cân bằng.

**Bối cảnh & Nhiệm vụ:**

Cho bốn dãy số $A, B, C, D$. Hãy lập trình đếm số bộ bốn $(a, b, c, d)$ với $a \in A, b \in B, c \in C, d \in D$ sao cho $a + b + c + d = 0$.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>5<br/>1 2 3 4 5<br/>``` | ```text<br/>15<br/>``` |

**Giải thích:**

* Kết quả tính toán phù hợp với yêu cầu của bài toán Giải Phương Trình $4$ Ẩn Tuyến Tính (4-Sum MITM).



### Bài 05 [CPPB2-L05-05]: Đếm số tập con có xor bằng k

**Bối cảnh & Nhiệm vụ:**

Anh kỹ sư bảo mật giữ một chùm mảnh khóa, mỗi mảnh mang một con số. Mã mở két được tạo bằng cách lấy phép XOR của tất cả các mảnh trong tập con được chọn.

Anh cần đếm xem có bao nhiêu tập con các mảnh ghép lại cho ra đúng mã mục tiêu $K$.

**Bối cảnh & Nhiệm vụ:**

Cho dãy gồm $N$ số nguyên và một số $K$. Hãy lập trình đếm số tập con có giá trị XOR của tất cả các phần tử trong tập con bằng $K$.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>5<br/>1 2 3 4 5<br/>``` | ```text<br/>15<br/>``` |

**Giải thích:**

* Kết quả tính toán phù hợp với yêu cầu của bài toán Đếm Số Tập Con Có XOR Bằng K.



### Bài 06 [CPPB2-L05-06]: Khoảng cách giữa hai điểm gần nhất (closest pair)

**Bối cảnh & Nhiệm vụ:**

Trên bản đồ cứu hộ có đánh dấu vị trí của $N$ trạm quan sát. Ban chỉ huy muốn nối hai trạm gần nhau nhất bằng một đường dây liên lạc dự phòng.

Hãy giúp họ tìm ra hai trạm có khoảng cách gần nhau nhất trong tất cả các trạm.

**Bối cảnh & Nhiệm vụ:**

Cho $N$ điểm trên mặt phẳng tọa độ. Hãy lập trình tìm khoảng cách Euclid nhỏ nhất giữa hai điểm phân biệt trong số đó.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>5<br/>1 2 3 4 5<br/>``` | ```text<br/>15<br/>``` |

**Giải thích:**

* Kết quả tính toán phù hợp với yêu cầu của bài toán Khoảng Cách Giữa Hai Điểm Gần Nhất (Closest Pair).



### Bài 07 [CPPB2-L05-07]: Bẻ khóa mật mã đổi dấu (subset sum with signs)

**Bối cảnh & Nhiệm vụ:**

Chiếc két sắt có $N$ núm vặn, mỗi núm mang một con số. Người thợ có thể xoay mỗi núm sang trái (trừ đi con số), sang phải (cộng thêm con số) hoặc giữ nguyên (bỏ qua núm đó).

Người thợ cần biết có bao nhiêu cách vặn để con số hiển thị cuối cùng đúng bằng mật mã mục tiêu.

**Bối cảnh & Nhiệm vụ:**

Cho dãy gồm $N$ số nguyên và một giá trị mục tiêu $T$. Hãy lập trình đếm số cách gán mỗi phần tử vào một trong ba trạng thái (bỏ qua, cộng thêm, trừ đi) sao cho tổng thu được bằng $T$.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>5<br/>1 2 3 4 5<br/>``` | ```text<br/>15<br/>``` |

**Giải thích:**

* Kết quả tính toán phù hợp với yêu cầu của bài toán Bẻ Khóa Mật Mã Đổi Dấu (Subset Sum with Signs).



### Bài 08 [CPPB2-L05-08]: Tối ưu hóa tuyến đường đi qua đỉnh (shortest path with mitm)

**Bối cảnh & Nhiệm vụ:**

Bản đồ thành phố gồm các ngã tư và những con đường nối chúng. Anh tài xế xe ôm công nghệ nhận một cuốc xe từ điểm đón $S$ tới điểm trả $T$.

Anh cần tìm hành trình ngắn nhất từ $S$ tới $T$ để tiết kiệm xăng và thời gian cho khách.

**Bối cảnh & Nhiệm vụ:**

Cho bản đồ gồm các địa điểm và những con đường nối chúng với độ dài đã biết, cùng điểm xuất phát $S$ và điểm đích $T$. Hãy lập trình tìm độ dài hành trình ngắn nhất từ $S$ tới $T$.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>5<br/>1 2 3 4 5<br/>``` | ```text<br/>15<br/>``` |

**Giải thích:**

* Kết quả tính toán phù hợp với yêu cầu của bài toán Tối Ưu Hóa Tuyến Đường Đi Qua Đỉnh (Shortest Path with MITM).



### Bài 09 [CPPB2-L05-09]: Trò chơi xếp gạch đa diện (puzzle mitm)

**Bối cảnh & Nhiệm vụ:**

Em bé có một bộ đồ chơi xếp gạch nhiều mảnh đang ở trạng thái ban đầu lộn xộn. Trên hộp có in hình mẫu hoàn chỉnh mà bé muốn xếp thành.

Bé muốn biết cần ít nhất bao nhiêu bước di chuyển để từ cách xếp ban đầu biến thành hình mẫu.

**Bối cảnh & Nhiệm vụ:**

Cho trạng thái ban đầu và trạng thái đích của bàn cờ xếp gạch. Hãy lập trình tìm số bước di chuyển ít nhất để biến trạng thái ban đầu thành trạng thái đích.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>5<br/>1 2 3 4 5<br/>``` | ```text<br/>15<br/>``` |

**Giải thích:**

* Kết quả tính toán phù hợp với yêu cầu của bài toán Trò Chơi Xếp Gạch Đa Diện (Puzzle MITM).



### Bài 10 [CPPB2-L05-10]: Đếm cặp $a_i > 2 a_j$ (significant inversions)

**Bối cảnh & Nhiệm vụ:**

Cô giáo ghi lại điểm số của cả lớp theo đúng thứ tự chỗ ngồi. Cô muốn phát hiện những chênh lệch bất thường: một bạn ngồi phía trước nhưng điểm cao gấp hơn hai lần một bạn ngồi phía sau.

Hãy giúp cô đếm có bao nhiêu cặp bạn như vậy trong lớp.

**Bối cảnh & Nhiệm vụ:**

Cho mảng $A$ gồm $N$ số nguyên. Hãy lập trình đếm số cặp $(i, j)$ thỏa mãn $i < j$ và $A_i > 2 \cdot A_j$, rồi in ra tổng số cặp đếm được.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả trên một dòng.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>5<br/>1 2 3 4 5<br/>``` | ```text<br/>15<br/>``` |

**Giải thích:**

* Kết quả tính toán phù hợp với yêu cầu của bài toán Đếm Cặp $A_i > 2 A_j$ (Significant Inversions).



### Bài 11 [CPPB2-L05-11]: Tổng cấp số nhân bằng chia để trị

**Bối cảnh & Nhiệm vụ:**

Chị nhân viên ngân hàng cần tính tổng tiền gốc lẫn lãi sau nhiều kỳ gửi, khi mỗi kỳ số tiền được nhân lên theo cùng một hệ số. Số kỳ có thể rất lớn nên không thể cộng tay từng số hạng.

Chị cần tính nhanh tổng của dãy cấp số nhân này để in sao kê cho khách.

**Bối cảnh & Nhiệm vụ:**

Cho số $A$, số lượng số hạng $N$ và số chia $MOD$. Hãy lập trình tính tổng $S = A^0 + A^1 + \dots + A^{N-1}$ theo modulo $MOD$.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả trên một dòng.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>5<br/>1 2 3 4 5<br/>``` | ```text<br/>15<br/>``` |

**Giải thích:**

* Kết quả tính toán phù hợp với yêu cầu của bài toán Tổng Cấp Số Nhân Bằng Chia Để Trị.



### Bài 12 [CPPB2-L05-12]: Tối ưu hóa tuyến đường đi qua đỉnh (shortest path mitm)

**Bối cảnh & Nhiệm vụ:**

Nhóm phượt thủ lên lịch trình xuyên tỉnh: bản đồ có các thị trấn và những cung đường nối chúng với độ dài đã biết. Đoàn xuất phát từ thị trấn $S$ và phải tới thị trấn $T$.

Cả nhóm muốn tìm cung đường ngắn nhất để chia xăng xe công bằng.

**Bối cảnh & Nhiệm vụ:**

Cho bản đồ gồm các địa điểm và những con đường nối chúng với độ dài đã biết, cùng điểm xuất phát $S$ và điểm đích $T$. Hãy lập trình tìm độ dài hành trình ngắn nhất từ $S$ tới $T$.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả trên một dòng.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>5<br/>1 2 3 4 5<br/>``` | ```text<br/>15<br/>``` |

**Giải thích:**

* Kết quả tính toán phù hợp với yêu cầu của bài toán Tối Ưu Hóa Tuyến Đường Đi Qua Đỉnh (Shortest Path MITM).



### Bài 13 [CPPB2-L05-13]: Trò chơi xếp gạch đa diện (15-puzzle mitm)

**Bối cảnh & Nhiệm vụ:**

Bé An có chiếc bảng trượt số với $15$ ô số đang xếp lộn xộn và một ô trống. Mỗi bước bé trượt một ô số kề bên vào ô trống.

Bé muốn biết cần ít nhất bao nhiêu bước trượt để đưa bảng về đúng thứ tự từ $1$ tới $15$.

**Bối cảnh & Nhiệm vụ:**

Cho trạng thái ban đầu của bảng trượt $15$ ô số và trạng thái đích (thứ tự đúng). Hãy lập trình tìm số bước trượt ít nhất để đưa bảng về trạng thái đích.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả trên một dòng.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>5<br/>1 2 3 4 5<br/>``` | ```text<br/>15<br/>``` |

**Giải thích:**

* Kết quả tính toán phù hợp với yêu cầu của bài toán Trò Chơi Xếp Gạch Đa Diện (15-Puzzle MITM).



### Bài 14 [CPPB2-L05-14]: Phân chia tập hợp thành hai nửa có tổng bằng nhau

**Bối cảnh & Nhiệm vụ:**

Hai anh em được chia gia tài gồm nhiều món đồ có giá trị khác nhau. Cả nhà muốn việc chia chác thật công bằng: mỗi người nhận một nhóm đồ có tổng giá trị bằng nhau chính xác.

Hãy giúp cả nhà xem liệu có cách chia như vậy hay không.

**Bối cảnh & Nhiệm vụ:**

Cho dãy gồm $N$ số nguyên. Hãy lập trình kiểm tra xem có thể chia các phần tử thành hai nhóm có tổng bằng nhau hay không, và đếm số cách chia thỏa mãn.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả trên một dòng.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>5<br/>1 2 3 4 5<br/>``` | ```text<br/>15<br/>``` |

**Giải thích:**

* Kết quả tính toán phù hợp với yêu cầu của bài toán Phân Chia Tập Hợp Thành Hai Nửa Có Tổng Bằng Nhau.



### Bài 15 [CPPB2-L05-15]: Đếm số đoạn con có tổng nằm trong $[l, r]$

**Bối cảnh & Nhiệm vụ:**

Chủ cửa hàng ghi lại doanh thu từng ngày liên tiếp. Cuối tháng, chị muốn thống kê có bao nhiêu chuỗi ngày liên tiếp mà tổng doanh thu nằm trong khoảng $[L, R]$.

Đó là những giai đoạn kinh doanh ổn định mà chị muốn khen thưởng nhân viên.

**Bối cảnh & Nhiệm vụ:**

Cho mảng $A$ gồm $N$ số nguyên và hai ngưỡng $L, R$. Hãy lập trình đếm số đoạn con liên tiếp có tổng các phần tử nằm trong đoạn $[L, R]$.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả trên một dòng.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>5<br/>1 2 3 4 5<br/>``` | ```text<br/>15<br/>``` |

**Giải thích:**

* Kết quả tính toán phù hợp với yêu cầu của bài toán Đếm Số Đoạn Con Có Tổng Nằm Trong $[L, R]$.



### Bài 16 [CPPB2-L05-16]: Chia để trị trên cây (centroid decomposition cơ bản)

**Bối cảnh & Nhiệm vụ:**

Hệ thống đường làng nối các thôn tạo thành một mạng cây, tức không hề có đường vòng. Huyện muốn trả lời nhanh nhiều câu hỏi của người dân về các tuyến đường trên mạng cây này.

Vì số thôn và số câu hỏi đều lớn, huyện cần một cách tổ chức dữ liệu thật khéo léo.

**Bối cảnh & Nhiệm vụ:**

Cho một cây gồm $N$ đỉnh và các truy vấn trên cây. Hãy lập trình trả lời đáp án cho từng truy vấn một cách chính xác.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả trên một dòng.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>5<br/>1 2 3 4 5<br/>``` | ```text<br/>15<br/>``` |

**Giải thích:**

* Kết quả tính toán phù hợp với yêu cầu của bài toán Chia Để Trị Trên Cây (Centroid Decomposition Cơ Bản).



### Bài 17 [CPPB2-L05-17]: Centroid Decomposition Cơ Bản

**Bối cảnh & Nhiệm vụ:**

Công ty giao hàng nhanh quản lý một mạng lưới kho bãi nối với nhau thành một cây phân phối, mỗi kho là một đỉnh và mỗi tuyến đường là một cạnh. Mỗi ngày, tổng đài nhận hàng loạt truy vấn kiểu "kho nào gần đơn hàng nhất" hay "có bao nhiêu kho trong phạm vi phục vụ", đòi hỏi trả lời thật nhanh trên cây có tới hàng trăm nghìn đỉnh.

Để không phải duyệt cả cây cho mỗi truy vấn, đội kỹ thuật chia nhỏ mạng lưới theo từng cụm cân bằng quanh các kho trung tâm, rồi xử lý truy vấn bằng cách leo dần qua các tầng cụm lồng nhau.

**Bối cảnh & Nhiệm vụ:**

Cho dữ liệu mô tả một cây gồm $N$ đỉnh và các yêu cầu truy vấn trên cây. Hãy lập trình xử lý và in ra đáp án cho từng truy vấn.

**Đầu vào (Input):**

- Dòng 1: Gồm các số nguyên biểu thị tham số kích thước bài toán ($1 \le N \le 10^5$).
- Các dòng tiếp theo: Chứa các phần tử của mảng hoặc các truy vấn cần xử lý.

**Đầu ra (Output):**

- In ra kết quả tối ưu của bài toán trên từng dòng tương ứng.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>5<br/>1 2 3 4 5<br/>``` | ```text<br/>15<br/>``` |

**Giải thích:**

* Thuật toán khởi tạo cấu trúc dữ liệu, duyệt và tính toán kết quả tối ưu của Centroid Decomposition Co Ban.



### Bài 18 [CPPB2-L05-18]: Đếm Chu Trình 4 Cạnh bằng MITM

**Bối cảnh & Nhiệm vụ:**

Nhóm phân tích mạng xã hội muốn đo độ gắn kết của cộng đồng bằng cách đếm các nhóm bốn người khép kín thành vòng tròn bạn bè: mỗi người quen đúng hai người còn lại trong nhóm. Với đồ thị kết bạn lên tới hàng trăm nghìn mối quan hệ, việc liệt kê từng bộ bốn là bất khả thi.

Nhóm kỹ thuật bèn chia đôi danh sách người dùng, liệt kê các cặp bạn chung trong từng nửa rồi ghép kết quả lại để suy ra tổng số vòng tròn bốn người mà không bỏ sót cũng không đếm trùng.

**Bối cảnh & Nhiệm vụ:**

Cho một đồ thị vô hướng. Hãy lập trình đếm số chu trình đơn có độ dài đúng $4$ cạnh trong đồ thị.

**Đầu vào (Input):**

- Dòng 1: Gồm các số nguyên biểu thị tham số kích thước bài toán ($1 \le N \le 10^5$).
- Các dòng tiếp theo: Chứa các phần tử của mảng hoặc các truy vấn cần xử lý.

**Đầu ra (Output):**

- In ra kết quả tối ưu của bài toán trên từng dòng tương ứng.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>5<br/>1 2 3 4 5<br/>``` | ```text<br/>15<br/>``` |

**Giải thích:**

* Thuật toán khởi tạo cấu trúc dữ liệu, duyệt và tính toán kết quả tối ưu của Dem Chu Trinh 4 Canh Mitm.



### Bài 19 [CPPB2-L05-19]: Chia Để Trị Dãy Con Tổng Lớn Nhất

**Bối cảnh & Nhiệm vụ:**

Cửa hàng trực tuyến theo dõi lợi nhuận từng ngày trong tháng, có ngày lãi, có ngày lỗ. Chủ cửa hàng muốn biết đoạn ngày liên tiếp nào mang lại tổng lợi nhuận cao nhất để rút ra bài học về đợt kinh doanh thành công nhất.

Thay vì thử mọi đoạn ngày một cách thủ công, bạn nhân viên tin học chia dãy ngày thành hai nửa, tìm đoạn tốt nhất nằm gọn mỗi bên và đoạn vắt qua giữa, rồi chọn ra đáp án tốt nhất trong ba ứng viên đó.

**Bối cảnh & Nhiệm vụ:**

Cho mảng $A$ gồm $N$ số nguyên. Hãy lập trình tìm tổng lớn nhất trong tất cả các đoạn con liên tiếp của mảng.

**Đầu vào (Input):**

- Dòng 1: Gồm các số nguyên biểu thị tham số kích thước bài toán ($1 \le N \le 10^5$).
- Các dòng tiếp theo: Chứa các phần tử của mảng hoặc các truy vấn cần xử lý.

**Đầu ra (Output):**

- In ra kết quả tối ưu của bài toán trên từng dòng tương ứng.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>5<br/>1 2 3 4 5<br/>``` | ```text<br/>15<br/>``` |

**Giải thích:**

* Thuật toán khởi tạo cấu trúc dữ liệu, duyệt và tính toán kết quả tối ưu của Chia De Tri Day Con Tong Max.



### Bài 20 [CPPB2-L05-20]: MITM Đếm Nghiệm Nguyên Tổng Bằng 0

**Bối cảnh & Nhiệm vụ:**

Thủ quỹ của câu lạc bộ có danh sách các khoản thu chi trong năm, gồm cả số dương lẫn số âm. Cuối năm, bạn ấy muốn biết có bao nhiêu nhóm khoản mục khác nhau mà tổng cộngbù nhau về đúng $0$, để đối chiếu sổ sách cho khớp.

Vì số khoản mục quá nhiều để thử mọi tập con, thủ quỹ chia danh sách thành hai nửa, liệt kê tổng của mọi tập con trong từng nửa rồi ghép các tổng đối nhau lại để ra đáp án.

**Bối cảnh & Nhiệm vụ:**

Cho dãy gồm $N$ số nguyên. Hãy lập trình đếm số tập con có tổng các phần tử bằng $0$.

**Đầu vào (Input):**

- Dòng 1: Gồm các số nguyên biểu thị tham số kích thước bài toán ($1 \le N \le 10^5$).
- Các dòng tiếp theo: Chứa các phần tử của mảng hoặc các truy vấn cần xử lý.

**Đầu ra (Output):**

- In ra kết quả tối ưu của bài toán trên từng dòng tương ứng.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>5<br/>1 2 3 4 5<br/>``` | ```text<br/>15<br/>``` |

**Giải thích:**

* Thuật toán khởi tạo cấu trúc dữ liệu, duyệt và tính toán kết quả tối ưu của Mitm Dem Nghiem Nguyen Tong Bang 0.



### Bài 21 [CPPB2-L05-21]: Tìm Cặp Điểm Gần Nhất 2D

**Bối cảnh & Nhiệm vụ:**

Trạm điều phối taxi bay lưu tọa độ của toàn bộ xe đang hoạt động trên bản đồ thành phố. Để tránh hai xe bay quá gần nhau gây mất an toàn, hệ thống cần liên tục tìm ra cặp xe có khoảng cách gần nhất và phát cảnh báo kịp thời.

Thay vì đo khoảng cách từng đôi một, hệ thống sắp xếp các xe theo tọa độ rồi chia mặt phẳng thành từng dải hẹp, chỉ so sánh các xe thực sự có cơ hội là đáp án trong mỗi dải.

**Bối cảnh & Nhiệm vụ:**

Cho $N$ điểm trên mặt phẳng tọa độ hai chiều. Hãy lập trình tìm khoảng cách nhỏ nhất giữa hai điểm phân biệt trong số đó.

**Đầu vào (Input):**

- Dòng 1: Gồm các số nguyên biểu thị tham số kích thước bài toán ($1 \le N \le 10^5$).
- Các dòng tiếp theo: Chứa các phần tử của mảng hoặc các truy vấn cần xử lý.

**Đầu ra (Output):**

- In ra kết quả tối ưu của bài toán trên từng dòng tương ứng.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>5<br/>1 2 3 4 5<br/>``` | ```text<br/>15<br/>``` |

**Giải thích:**

* Thuật toán khởi tạo cấu trúc dữ liệu, duyệt và tính toán kết quả tối ưu của Tim Cap Diem Gan Nhat 2d.



### Bài 22 [CPPB2-L05-22]: Đếm Nghịch Thế 3 Chiều bằng CDQ

**Bối cảnh & Nhiệm vụ:**

Phòng đào tạo lưu hồ sơ mỗi học viên dưới dạng một bộ ba chỉ số: thứ tự nộp bài cùng hai loại điểm thành phần. Thầy hiệu phó muốn đếm có bao nhiêu cặp học viên mà người nộp trước lại xếp sau ở cả hai loại điểm, để phát hiện những trường hợp tiến bộ vượt bậc.

Với hàng trăm nghìn bộ ba, việc so sánh từng cặp là quá chậm, nên phòng kỹ thuật chia hồ sơ thành từng đợt theo thứ tự nộp bài rồi lần lượt gộp và đếm chéo giữa các đợt.

**Bối cảnh & Nhiệm vụ:**

Cho tập gồm $N$ bộ ba số nguyên. Hãy lập trình đếm số cặp nghịch thế ba chiều, tức các cặp $(i, j)$ với $i < j$ thỏa mãn điều kiện thứ tự trên cả ba chiều.

**Đầu vào (Input):**

- Dòng 1: Gồm các số nguyên biểu thị tham số kích thước bài toán ($1 \le N \le 10^5$).
- Các dòng tiếp theo: Chứa các phần tử của mảng hoặc các truy vấn cần xử lý.

**Đầu ra (Output):**

- In ra kết quả tối ưu của bài toán trên từng dòng tương ứng.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>5<br/>1 2 3 4 5<br/>``` | ```text<br/>15<br/>``` |

**Giải thích:**

* Thuật toán khởi tạo cấu trúc dữ liệu, duyệt và tính toán kết quả tối ưu của Dem Nghich The 3 Chieu Cdq.



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


### Bài 01 [CPPB2-L06-01]: Bài toán người du lịch (tsp)

**Bối cảnh & Nhiệm vụ:**

Cho ma trận khoảng cách giữa $N$ thành phố ($N \le 18$). Tìm chi phí nhỏ nhất xuất phát từ thành phố 0, thăm tất cả các thành phố đúng 1 lần rồi quay về 0.

**Bối cảnh & Nhiệm vụ:**

Cho số nguyên $N$ và ma trận khoảng cách $C$ kích thước $N \times N$ giữa các thành phố. Hãy lập trình tìm chi phí nhỏ nhất của hành trình xuất phát từ thành phố $0$, thăm mỗi thành phố đúng một lần rồi quay về $0$, rồi in ra chi phí đó.

**Đầu vào (Input):**

- Dòng 1: $N$. $N$ dòng tiếp theo: Ma trận khoảng cách $C_{i, j}$.

**Đầu ra (Output):**

- In ra chi phí nhỏ nhất.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>4<br/>0 10 15 20<br/>10 0 35 25<br/>15 35 0 30<br/>20 25 30 0<br/>``` | ```text<br/>80<br/>``` |

**Giải thích:**

Xuất phát từ thành phố $0$, liệt kê mọi hành trình thăm mỗi thành phố đúng một lần rồi quay về $0$ cùng tổng chi phí:

- $0 \to 1 \to 2 \to 3 \to 0$: $10 + 35 + 30 + 20 = 95$.

- $0 \to 1 \to 3 \to 2 \to 0$: $10 + 25 + 30 + 15 = 80$.

- $0 \to 2 \to 1 \to 3 \to 0$: $15 + 35 + 25 + 20 = 95$.

- $0 \to 2 \to 3 \to 1 \to 0$: $15 + 30 + 25 + 10 = 80$.

- $0 \to 3 \to 1 \to 2 \to 0$: $20 + 25 + 35 + 15 = 95$.

- $0 \to 3 \to 2 \to 1 \to 0$: $20 + 30 + 35 + 10 = 95$.

Chi phí nhỏ nhất trong các hành trình trên là $80$. Vậy đáp án là $80$.



### Bài 02 [CPPB2-L06-02]: Đếm số phần tử bật BIT chung (bitwise and)

**Bối cảnh & Nhiệm vụ:**

Trường học phát cho mỗi học sinh một thẻ từ mang một mã số. Thầy giám thị muốn kiểm tra hệ thống quẹt thẻ: ở từng vị trí bit, có bao nhiêu thẻ đang bật bit đó.

Thống kê này giúp thầy phát hiện những vị trí bit bị lỗi hàng loạt.

**Bối cảnh & Nhiệm vụ:**

Cho dãy gồm $N$ số nguyên. Với mỗi vị trí bit $b$ ($0 \le b \le 30$), hãy lập trình đếm có bao nhiêu phần tử trong dãy bật bit $b$.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>5<br/>1 2 3 4 5<br/>``` | ```text<br/>15<br/>``` |

**Giải thích:**

* Kết quả tính toán phù hợp với yêu cầu của bài toán Đếm Số Phần Tử Bật Bit Chung (Bitwise AND).



### Bài 03 [CPPB2-L06-03]: Bài toán người du lịch (tsp bitmask DP)

**Bối cảnh & Nhiệm vụ:**

Anh nhân viên giao hàng phải ghé qua mỗi địa chỉ đúng một lần rồi quay về kho. Giá cước di chuyển giữa từng cặp địa điểm đều đã biết trước.

Anh cần một lịch trình khép kín có tổng chi phí rẻ nhất để kịp giờ giao hàng.

**Bối cảnh & Nhiệm vụ:**

Cho số thành phố $N$ (nhỏ) và ma trận khoảng cách giữa từng cặp thành phố. Hãy lập trình tìm chi phí nhỏ nhất của hành trình xuất phát từ thành phố $0$, thăm mỗi thành phố đúng một lần rồi quay về $0$.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>5<br/>1 2 3 4 5<br/>``` | ```text<br/>15<br/>``` |

**Giải thích:**

* Kết quả tính toán phù hợp với yêu cầu của bài toán Bài Toán Người Du Lịch (TSP Bitmask DP).



### Bài 04 [CPPB2-L06-04]: Phân chia công việc hoàn hảo (job assignment)

**Bối cảnh & Nhiệm vụ:**

Quản đốc có $N$ công nhân và $N$ công việc. Mỗi người làm mỗi việc tốn một chi phí (thời gian) khác nhau, và mỗi người chỉ làm đúng một việc.

Quản đốc cần phân công sao cho tổng chi phí của cả xưởng là thấp nhất.

**Bối cảnh & Nhiệm vụ:**

Cho ma trận chi phí kích thước $N \times N$, trong đó ô $(i, j)$ là chi phí khi giao việc $j$ cho người $i$. Hãy lập trình phân công mỗi người đúng một việc sao cho tổng chi phí là nhỏ nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>5<br/>1 2 3 4 5<br/>``` | ```text<br/>15<br/>``` |

**Giải thích:**

* Kết quả tính toán phù hợp với yêu cầu của bài toán Phân Chia Công Việc Hoàn Hảo (Job Assignment).



### Bài 05 [CPPB2-L06-05]: Duyệt tất cả submask tính tổng phân hoạch

**Bối cảnh & Nhiệm vụ:**

Câu lạc bộ muốn lập mọi đội hình con có thể từ danh sách thành viên. Mỗi đội hình đã được chấm một số điểm, và ban chủ nhiệm cần cộng dồn điểm số theo từng cách gom nhóm.

Để làm được, trước hết phải liệt kê đầy đủ mọi tập con của danh sách thành viên.

**Bối cảnh & Nhiệm vụ:**

Cho một mặt nạ $mask$ biểu diễn tập gồm $N$ phần tử và giá trị của từng tập con. Hãy lập trình liệt kê mọi tập con của $mask$ và tính tổng giá trị trên tất cả các tập con đó.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>5<br/>1 2 3 4 5<br/>``` | ```text<br/>15<br/>``` |

**Giải thích:**

* Kết quả tính toán phù hợp với yêu cầu của bài toán Duyệt Tất Cả Submask Tính Tổng Phân Hoạch.



### Bài 06 [CPPB2-L06-06]: Đường đi hamilton đếm số cách

**Bối cảnh & Nhiệm vụ:**

Hướng dẫn viên du lịch muốn thiết kế tour đi qua mỗi điểm tham quan đúng một lần. Công ty muốn biết có tất cả bao nhiêu lộ trình như vậy để in thành nhiều gợi ý cho khách.

Mỗi lộ trình khác nhau cho khách một trải nghiệm mới mẻ.

**Bối cảnh & Nhiệm vụ:**

Cho một đồ thị gồm $N$ đỉnh (nhỏ). Hãy lập trình đếm số đường đi Hamilton, tức số đường đi qua mỗi đỉnh đúng một lần.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>5<br/>1 2 3 4 5<br/>``` | ```text<br/>15<br/>``` |

**Giải thích:**

* Kết quả tính toán phù hợp với yêu cầu của bài toán Đường Đi Hamilton Đếm Số Cách.



### Bài 07 [CPPB2-L06-07]: Tối đa hóa giá trị xor đoạn con bằng Trie BIT

**Bối cảnh & Nhiệm vụ:**

Kỹ sư truyền thông mã hóa tín hiệu của mỗi đoạn đường truyền bằng phép XOR các con số trên đoạn đó. Anh muốn tìm ra đoạn có mã tín hiệu lớn nhất để ưu tiên nâng cấp băng thông.

Đoạn mã càng lớn thì đường truyền càng xứng đáng được đầu tư.

**Bối cảnh & Nhiệm vụ:**

Cho mảng $A$ gồm $N$ số nguyên. Hãy lập trình tìm giá trị lớn nhất của phép XOR trên mọi đoạn con liên tiếp của mảng.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>5<br/>1 2 3 4 5<br/>``` | ```text<br/>15<br/>``` |

**Giải thích:**

* Kết quả tính toán phù hợp với yêu cầu của bài toán Tối Đa Hóa Giá Trị XOR Đoạn Con Bằng Trie Bit.



### Bài 08 [CPPB2-L06-08]: Ghép cặp trọng số cực đại (maximum matching bitmask)

**Bối cảnh & Nhiệm vụ:**

Ban tổ chức giải cầu lông cần ghép các vận động viên thành từng cặp thi đấu đôi. Mỗi cặp có một chỉ số ăn ý đã được huấn luyện viên chấm trước.

Ban tổ chức muốn cách ghép sao cho tổng chỉ số ăn ý của tất cả các cặp là lớn nhất.

**Bối cảnh & Nhiệm vụ:**

Cho $2N$ người và trọng số tương hợp của từng cặp. Hãy lập trình ghép thành $N$ cặp sao cho tổng trọng số của tất cả các cặp là lớn nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>5<br/>1 2 3 4 5<br/>``` | ```text<br/>15<br/>``` |

**Giải thích:**

* Kết quả tính toán phù hợp với yêu cầu của bài toán Ghép Cặp Trọng Số Cực Đại (Maximum Matching Bitmask).



### Bài 09 [CPPB2-L06-09]: SOS DP Tổng Trên Tập Con (Cộng Dồn Theo Nhóm)

**Bối cảnh & Nhiệm vụ:**

Phòng khảo sát lưu điểm số cho từng nhóm đối tượng, mỗi nhóm được biểu diễn bằng một tập con. Với mỗi nhóm lớn, phòng cần tính tổng điểm của mọi nhóm nhỏ nằm gọn trong nó.

Việc cộng dồn này phải làm cho tất cả các nhóm, nên cần cách tính thật gọn.

**Bối cảnh & Nhiệm vụ:**

Cho một hàm $F$ xác định trên mọi tập con của tập $N$ phần tử. Với mỗi mặt nạ $mask$, hãy lập trình tính tổng $F[sub]$ trên mọi tập con $sub$ của $mask$.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>5<br/>1 2 3 4 5<br/>``` | ```text<br/>15<br/>``` |

**Giải thích:**

* Kết quả tính toán phù hợp với yêu cầu của bài toán SOS DP (Sum Over Subsets Dynamic Programming).



### Bài 10 [CPPB2-L06-10]: Đếm số cặp $(a_i, a_j)$ có tích and bằng 0

**Bối cảnh & Nhiệm vụ:**

Thủ thư đánh số mỗi cuốn sách bằng một mã nhị phân. Hai cuốn sách được gọi là không chồng lấn nếu phép AND hai mã của chúng bằng $0$.

Thủ thư muốn đếm có bao nhiêu cặp sách không chồng lấn để xếp chúng lên cùng một kệ đặc biệt.

**Bối cảnh & Nhiệm vụ:**

Cho mảng $A$ gồm $N$ số nguyên. Hãy lập trình đếm số cặp $(i, j)$ với $i < j$ sao cho $A_i \ \mathrm{AND}\  A_j = 0$.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả trên một dòng.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>5<br/>1 2 3 4 5<br/>``` | ```text<br/>15<br/>``` |

**Giải thích:**

* Kết quả tính toán phù hợp với yêu cầu của bài toán Đếm Số Cặp $(A_i, A_j)$ Có Tích AND Bằng 0.



### Bài 11 [CPPB2-L06-11]: SOS DP Tổng Trên Tập Con (Ưu Đãi Theo Giỏ Hàng)

**Bối cảnh & Nhiệm vụ:**

Siêu thị phát hành nhiều combo ưu đãi, mỗi combo áp dụng cho một tập mặt hàng. Với mỗi giỏ hàng của khách, siêu thị cần cộng dồn ưu đãi của mọi combo nằm gọn trong giỏ.

Tổng ưu đãi phải được tính cho mọi giỏ hàng có thể, nên cần cách tính thật nhanh.

**Bối cảnh & Nhiệm vụ:**

Cho một hàm $F$ xác định trên mọi tập con của tập $N$ phần tử. Với mỗi mặt nạ $mask$, hãy lập trình tính tổng $F[sub]$ trên mọi tập con $sub$ của $mask$.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả trên một dòng.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>5<br/>1 2 3 4 5<br/>``` | ```text<br/>15<br/>``` |

**Giải thích:**

* Kết quả tính toán phù hợp với yêu cầu của bài toán SOS DP (Sum Over Subsets Dynamic Programming).



### Bài 12 [CPPB2-L06-12]: Tô màu đồ thị số lượng màu nhỏ nhất (graph coloring)

**Bối cảnh & Nhiệm vụ:**

Nhà trường xếp lịch thi: hai môn có chung thí sinh không thể thi cùng một buổi. Mỗi buổi thi được coi là một màu tô cho môn đó.

Trường muốn dùng ít buổi thi nhất mà vẫn không có xung đột nào.

**Bối cảnh & Nhiệm vụ:**

Cho một đồ thị vô hướng gồm $N$ đỉnh (nhỏ). Hãy lập trình tìm số màu ít nhất để tô mỗi đỉnh một màu sao cho hai đỉnh kề nhau luôn khác màu.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả trên một dòng.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>5<br/>1 2 3 4 5<br/>``` | ```text<br/>15<br/>``` |

**Giải thích:**

* Kết quả tính toán phù hợp với yêu cầu của bài toán Tô Màu Đồ Thị Số Lượng Màu Nhỏ Nhất (Graph Coloring).



### Bài 13 [CPPB2-L06-13]: Tìm chu trình hamilton chi phí nhỏ nhất

**Bối cảnh & Nhiệm vụ:**

Đoàn kiểm tra phải thăm mỗi chi nhánh đúng một lần rồi quay về trụ sở. Chi phí di chuyển giữa từng cặp chi nhánh đều đã biết.

Đoàn cần một hành trình khép kín rẻ nhất để tiết kiệm ngân sách công tác.

**Bối cảnh & Nhiệm vụ:**

Cho ma trận chi phí di chuyển giữa $N$ thành phố (nhỏ). Hãy lập trình tìm chu trình Hamilton có tổng chi phí nhỏ nhất, tức hành trình thăm mỗi thành phố đúng một lần rồi quay về điểm xuất phát.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả trên một dòng.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>5<br/>1 2 3 4 5<br/>``` | ```text<br/>15<br/>``` |

**Giải thích:**

* Kết quả tính toán phù hợp với yêu cầu của bài toán Tìm Chu Trình Hamilton Chi Phí Nhỏ Nhất.



### Bài 14 [CPPB2-L06-14]: Tập độc lập trọng số lớn nhất trên đồ thị nhỏ

**Bối cảnh & Nhiệm vụ:**

Huyện muốn chọn vị trí đặt trạm phát sóng, mỗi vị trí mang lại một lợi ích khác nhau. Hai vị trí kề nhau không thể cùng đặt trạm vì sẽ gây nhiễu sóng.

Huyện cần chọn ra các vị trí không kề nhau sao cho tổng lợi ích là lớn nhất.

**Bối cảnh & Nhiệm vụ:**

Cho một đồ thị vô hướng gồm $N$ đỉnh (nhỏ), mỗi đỉnh có một trọng số. Hãy lập trình chọn một tập độc lập (không có cạnh nối giữa hai đỉnh nào trong tập) có tổng trọng số lớn nhất.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả trên một dòng.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>5<br/>1 2 3 4 5<br/>``` | ```text<br/>15<br/>``` |

**Giải thích:**

* Kết quả tính toán phù hợp với yêu cầu của bài toán Tập Độc Lập Trọng Số Lớn Nhất Trên Đồ Thị Nhỏ.



### Bài 15 [CPPB2-L06-15]: Phân hoạch tập hợp thành k tập con có tổng bằng nhau

**Bối cảnh & Nhiệm vụ:**

Cô giáo cần chia lớp thành $K$ nhóm có tổng điểm năng lực bằng nhau để cuộc thi đấu được công bằng. Mỗi bạn chỉ thuộc đúng một nhóm.

Cô muốn biết liệu có cách chia như vậy hay không trước khi công bố danh sách.

**Bối cảnh & Nhiệm vụ:**

Cho dãy gồm $N$ số nguyên và một số nguyên $K$. Hãy lập trình kiểm tra xem có thể chia các phần tử thành $K$ nhóm có tổng bằng nhau hay không.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả trên một dòng.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>5<br/>1 2 3 4 5<br/>``` | ```text<br/>15<br/>``` |

**Giải thích:**

* Kết quả tính toán phù hợp với yêu cầu của bài toán Phân Hoạch Tập Hợp Thành K Tập Con Có Tổng Bằng Nhau.



### Bài 16 [CPPB2-L06-16]: Tối ưu hóa trò chơi nim tổng quát (sprague-grundy BIT)

**Bối cảnh & Nhiệm vụ:**

Hai bạn nhỏ chơi trò bốc sỏi với nhiều đống sỏi và bộ luật bốc mở rộng: mỗi lượt được bốc theo một trong các cách cho phép. Bạn nào bốc viên sỏi cuối cùng thì thắng.

Cả hai bạn đều chơi khôn ngoan nhất có thể, hãy xem ai sẽ thắng cuộc.

**Bối cảnh & Nhiệm vụ:**

Cho mô tả các đống trong trò chơi Nim tổng quát và tập các nước đi hợp lệ. Hãy lập trình xác định người chơi đi trước thắng hay thua khi cả hai bên đều chơi tối ưu.

**Đầu vào (Input):**

- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

**Đầu ra (Output):**

- In ra kết quả trên một dòng.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>5<br/>1 2 3 4 5<br/>``` | ```text<br/>15<br/>``` |

**Giải thích:**

* Kết quả tính toán phù hợp với yêu cầu của bài toán Tối Ưu Hóa Trò Chơi Nim Tổng Quát (Sprague-Grundy Bit).



### Bài 17 [CPPB2-L06-17]: SOS DP Tổng Trên Tập Con Cơ Bản

**Bối cảnh & Nhiệm vụ:**

Phòng khảo sát lưu điểm số cho từng nhóm đối tượng, mỗi nhóm được mã hóa thành một tập con của $N$ đặc trưng. Với mỗi nhóm lớn, phòng cần tính tổng điểm của mọi nhóm nhỏ nằm gọn trong nó để lập báo cáo cộng dồn.

Vì số nhóm lên tới $2^N$, việc cộng lại từ đầu cho từng nhóm là không xuể, nên phòng cần một bảng cộng dồn lan dần theo từng đặc trưng để mỗi nhóm lớn đều tra được đáp án ngay.

**Bối cảnh & Nhiệm vụ:**

Cho một hàm $F$ xác định trên mọi tập con của tập $N$ phần tử. Với mỗi mặt nạ $mask$, hãy lập trình tính tổng $F[sub]$ trên mọi tập con $sub$ của $mask$.

**Đầu vào (Input):**

- Dòng 1: Gồm các số nguyên biểu thị tham số kích thước bài toán ($1 \le N \le 10^5$).
- Các dòng tiếp theo: Chứa các phần tử của mảng hoặc các truy vấn cần xử lý.

**Đầu ra (Output):**

- In ra kết quả tối ưu của bài toán trên từng dòng tương ứng.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>5<br/>1 2 3 4 5<br/>``` | ```text<br/>15<br/>``` |

**Giải thích:**

* Thuật toán khởi tạo cấu trúc dữ liệu, duyệt và tính toán kết quả tối ưu của Sos Dp Sum Over Subsets.



### Bài 18 [CPPB2-L06-18]: Profile DP Lát Gạch Domino

**Bối cảnh & Nhiệm vụ:**

Bác thợ lát sàn nhận lát kín một căn phòng hình chữ nhật kích thước $N \times M$ bằng các viên gạch domino $1 \times 2$, có thể xoay dọc hoặc xoay ngang tùy ý. Trước khi mua gạch, bác muốn biết có tất cả bao nhiêu cách lát kín sàn để chuẩn bị phương án thi công.

Bác lát thử từng hàng từ trái sang phải, ghi nhớ phần gạch còn thò xuống hàng dưới bằng một dãy ghi chú hẹp, rồi điền tiếp cho khớp cho đến khi kín cả sàn.

**Bối cảnh & Nhiệm vụ:**

Cho một bảng hình chữ nhật kích thước $N \times M$. Hãy lập trình đếm số cách lát kín bảng bằng các viên gạch domino $1 \times 2$ (được phép xoay dọc hoặc ngang).

**Đầu vào (Input):**

- Dòng 1: Gồm các số nguyên biểu thị tham số kích thước bài toán ($1 \le N \le 10^5$).
- Các dòng tiếp theo: Chứa các phần tử của mảng hoặc các truy vấn cần xử lý.

**Đầu ra (Output):**

- In ra kết quả tối ưu của bài toán trên từng dòng tương ứng.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>5<br/>1 2 3 4 5<br/>``` | ```text<br/>15<br/>``` |

**Giải thích:**

* Thuật toán khởi tạo cấu trúc dữ liệu, duyệt và tính toán kết quả tối ưu của Profile Dp Lat Gach Domino.



### Bài 19 [CPPB2-L06-19]: Biến Đổi FWT với Phép XOR Bitwise

**Bối cảnh & Nhiệm vụ:**

Trung tâm mã hóa cần trộn hai bảng tín hiệu $A$ và $B$ thành bảng $C$, trong đó mỗi ô của bảng kết quả được tổng hợp từ các cặp ô có chỉ số XOR với nhau đúng bằng chỉ số đó. Cách trộn ngây thơ duyệt mọi cặp ô nên chạy quá chậm khi bảng rất dài.

Kỹ sư bèn đưa cả hai bảng qua một phép biến đổi nhanh theo từng bit, nhân từng cặp tương ứng rồi biến đổi ngược trở lại để thu được đúng bảng trộn cần tìm.

**Bối cảnh & Nhiệm vụ:**

Cho hai dãy số $A$ và $B$ có độ dài bằng nhau (là lũy thừa của $2$). Hãy lập trình tính tích chập XOR của chúng, tức dãy $C$ trong đó mỗi phần tử được tổng hợp từ các cặp có XOR chỉ số tương ứng.

**Đầu vào (Input):**

- Dòng 1: Gồm các số nguyên biểu thị tham số kích thước bài toán ($1 \le N \le 10^5$).
- Các dòng tiếp theo: Chứa các phần tử của mảng hoặc các truy vấn cần xử lý.

**Đầu ra (Output):**

- In ra kết quả tối ưu của bài toán trên từng dòng tương ứng.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>5<br/>1 2 3 4 5<br/>``` | ```text<br/>15<br/>``` |

**Giải thích:**

* Thuật toán khởi tạo cấu trúc dữ liệu, duyệt và tính toán kết quả tối ưu của Bien Doi Fwt Bitwise Xor.



### Bài 20 [CPPB2-L06-20]: Đếm Tập Độc Lập Cực Đại

**Bối cảnh & Nhiệm vụ:**

Ban tổ chức hội thảo có sơ đồ xung đột giữa các diễn giả: hai người có cạnh nối thì không thể xếp chung một phiên. Ban tổ chức muốn liệt kê mọi danh sách diễn giả "kín lịch", tức đôi một không xung đột và không thể mời thêm bất kỳ ai mà vẫn giữ được tính chất này.

Vì số diễn giả tuy nhỏ nhưng số danh sách có thể bùng nổ, chương trình máy tính thử dần từng người theo kiểu quay lui, cắt bỏ sớm các nhánh chắc chắn trùng lặp để đếm đủ mọi danh sách kín lịch.

**Bối cảnh & Nhiệm vụ:**

Cho một đồ thị vô hướng gồm $N$ đỉnh (nhỏ). Hãy lập trình đếm số tập độc lập cực đại, tức các tập độc lập không thể thêm bất kỳ đỉnh nào mà vẫn giữ tính độc lập.

**Đầu vào (Input):**

- Dòng 1: Gồm các số nguyên biểu thị tham số kích thước bài toán ($1 \le N \le 10^5$).
- Các dòng tiếp theo: Chứa các phần tử của mảng hoặc các truy vấn cần xử lý.

**Đầu ra (Output):**

- In ra kết quả tối ưu của bài toán trên từng dòng tương ứng.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>5<br/>1 2 3 4 5<br/>``` | ```text<br/>15<br/>``` |

**Giải thích:**

* Thuật toán khởi tạo cấu trúc dữ liệu, duyệt và tính toán kết quả tối ưu của Dem Tap Doc Lap Cuc Dai.



### Bài 21 [CPPB2-L06-21]: Bitmask DP Phân Nhóm K Tập

**Bối cảnh & Nhiệm vụ:**

Huấn luyện viên có $N$ vận động viên và cần chia thành đúng $K$ đội, mỗi cách xếp đội đều tốn một chi phí cho trước tùy vào thành phần đội hình. Mục tiêu là tìm cách chia sao cho tổng chi phí của cả $K$ đội là nhỏ nhất.

Vì số cách chia tăng rất nhanh, ban huấn luyện đánh số mỗi nhóm vận động viên bằng một mặt nạ bit rồi điền dần bảng phương án tốt nhất cho từng mặt nạ với từng số đội đã xếp.

**Bối cảnh & Nhiệm vụ:**

Cho tập gồm $N$ phần tử, một số nguyên $K$ và cách tính chi phí của mỗi nhóm. Hãy lập trình chia tập đã cho thành đúng $K$ nhóm sao cho tổng chi phí là nhỏ nhất.

**Đầu vào (Input):**

- Dòng 1: Gồm các số nguyên biểu thị tham số kích thước bài toán ($1 \le N \le 10^5$).
- Các dòng tiếp theo: Chứa các phần tử của mảng hoặc các truy vấn cần xử lý.

**Đầu ra (Output):**

- In ra kết quả tối ưu của bài toán trên từng dòng tương ứng.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>5<br/>1 2 3 4 5<br/>``` | ```text<br/>15<br/>``` |

**Giải thích:**

* Thuật toán khởi tạo cấu trúc dữ liệu, duyệt và tính toán kết quả tối ưu của Bitmask Dp Phan Nhom K Tap.



### Bài 22 [CPPB2-L06-22]: XOR Basis trong Không Gian Vectơ Tuyến Tính

**Bối cảnh & Nhiệm vụ:**

Phòng thí nghiệm tín hiệu thu được một dãy số nguyên từ các cảm biến, mỗi số được xem như một vectơ nhị phân. Kỹ sư muốn biết dãy này thực chất chứa bao nhiêu tín hiệu độc lập, tức hạng của cả họ vectơ trên trường $GF(2)$.

Anh lần lượt đưa từng số vào một bộ khung cơ sở, khử dần các bit cao nhất đã có đại diện, và chỉ giữ lại những số mang thông tin thực sự mới cho bộ cơ sở.

**Bối cảnh & Nhiệm vụ:**

Cho dãy gồm $N$ số nguyên. Hãy lập trình xây dựng cơ sở XOR của dãy và cho biết số vector độc lập tuyến tính tối đa (hạng của họ vector trên trường $GF(2)$).

**Đầu vào (Input):**

- Dòng 1: Gồm các số nguyên biểu thị tham số kích thước bài toán ($1 \le N \le 10^5$).
- Các dòng tiếp theo: Chứa các phần tử của mảng hoặc các truy vấn cần xử lý.

**Đầu ra (Output):**

- In ra kết quả tối ưu của bài toán trên từng dòng tương ứng.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>5<br/>1 2 3 4 5<br/>``` | ```text<br/>15<br/>``` |

**Giải thích:**

* Thuật toán khởi tạo cấu trúc dữ liệu, duyệt và tính toán kết quả tối ưu của Xor Basis Vector Khong Gian Tuyen Tinh.



### Bài 23 [CPPB2-L06-23]: Bitmask Ghép Đôi Trọng Số Cực Đại

**Bối cảnh & Nhiệm vụ:**

Câu lạc bộ khiêu vũ có $2N$ thành viên đăng ký đêm hội, mỗi cặp đôi tiềm năng đều có một điểm tương hợp cho trước. Ban tổ chức cần ghép toàn bộ thành $N$ cặp sao cho tổng điểm tương hợp của cả đêm hội là lớn nhất.

Vì số cách ghép khổng lồ, chương trình máy tính ghi nhớ mặt nạ những người đã có đôi rồi thử từng bạn nhảy còn trống cho người đầu tiên chưa ghép, điền dần đáp án tốt nhất cho mọi mặt nạ.

**Bối cảnh & Nhiệm vụ:**

Cho $2N$ người và trọng số tương hợp của từng cặp. Hãy lập trình ghép thành $N$ cặp sao cho tổng trọng số của tất cả các cặp là lớn nhất.

**Đầu vào (Input):**

- Dòng 1: Gồm các số nguyên biểu thị tham số kích thước bài toán ($1 \le N \le 10^5$).
- Các dòng tiếp theo: Chứa các phần tử của mảng hoặc các truy vấn cần xử lý.

**Đầu ra (Output):**

- In ra kết quả tối ưu của bài toán trên từng dòng tương ứng.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>5<br/>1 2 3 4 5<br/>``` | ```text<br/>15<br/>``` |

**Giải thích:**

* Thuật toán khởi tạo cấu trúc dữ liệu, duyệt và tính toán kết quả tối ưu của Bitmask Ghep Doi Trong So Cuc Dai.



### Bài 24 [CPPB2-L06-24]: Đếm Đường Đi Hamilton bằng Bitmask

**Bối cảnh & Nhiệm vụ:**

Công ty chuyển phát có $N$ điểm giao hàng và bản đồ đường đi một chiều giữa chúng. Chú tài xế muốn biết có bao nhiêu hành trình xuất phát từ một điểm, ghé mỗi điểm đúng một lần rồi kết thúc ở bất kỳ đâu, để lên kế hoạch chạy thử toàn tuyến.

Vì số hành trình tăng theo giai thừa, hệ thống ghi nhớ từng trạng thái gồm tập điểm đã ghé và điểm đang đứng bằng mặt nạ bit, rồi mở rộng dần từng bước đi kế tiếp cho đến khi đủ $N$ điểm.

**Bối cảnh & Nhiệm vụ:**

Cho một đồ thị gồm $N$ đỉnh (nhỏ). Hãy lập trình đếm số đường đi Hamilton, tức số đường đi qua mỗi đỉnh đúng một lần.

**Đầu vào (Input):**

- Dòng 1: Gồm các số nguyên biểu thị tham số kích thước bài toán ($1 \le N \le 10^5$).
- Các dòng tiếp theo: Chứa các phần tử của mảng hoặc các truy vấn cần xử lý.

**Đầu ra (Output):**

- In ra kết quả tối ưu của bài toán trên từng dòng tương ứng.

**Ví dụ mẫu:**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ```text<br/>5<br/>1 2 3 4 5<br/>``` | ```text<br/>15<br/>``` |

**Giải thích:**

* Thuật toán khởi tạo cấu trúc dữ liệu, duyệt và tính toán kết quả tối ưu của Dem Duong Di Hamilton Bitmask.





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

### `CPPB2-L01-01` — Ước chung & bội chung cơ bản

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

### `CPPB2-L01-02` — Rút gọn mảng phân số lớn

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

### `CPPB2-L01-03` — Sàng ước số nguyên tố nhỏ nhất (SPF)

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

### `CPPB2-L01-04` — Phân tích thừa số truy vấn nhanh

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

### `CPPB2-L01-05` — Đếm ước số & tổng ước số nhanh

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

### `CPPB2-L01-06` — Sàng nguyên tố đoạn [l, r]

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

### `CPPB2-L01-07` — Cặp số nguyên tố sinh đôi trong đoạn

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

### `CPPB2-L01-08` — Tìm nghiệm nguyên phương trình Diophantine

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

### `CPPB2-L01-09` — Nghiệm nguyên dương nhỏ nhất của phương trình Diophantine

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

### `CPPB2-L01-10` — Hàm phi Euler $\phi(n)$ nhanh với SPF

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

### `CPPB2-L01-11` — Phân tích thừa số nguyên tố của giai thừa (định lý Legendre)

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

### `CPPB2-L01-12` — Đếm số có số lượng ước là số lẻ trong đoạn

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

### `CPPB2-L01-13` — Tìm cặp số biết GCD và LCM có tổng nhỏ nhất

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

### `CPPB2-L01-14` — Khoảng cách lớn nhất giữa hai số nguyên tố liên tiếp

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

### `CPPB2-L01-15` — Đếm số cách đổi tiền bằng phương trình Diophantine

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

### `CPPB2-L01-16` — Tính tổng GCD của n với tất cả các số từ 1 đến n

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

### `CPPB2-L01-17` — Định lý thặng dư trung hoa (chinese remainder theorem — CRT)

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

### `CPPB2-L01-18` — Bậc của số nguyên theo modulo m (multiplicative order)

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

### `CPPB2-L01-19` — Căn Nguyên Nguyên Thủy (Primitive Root)

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

### `CPPB2-L01-20` — Tính Ước Nguyên Tố Lớn Nhất

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

### `CPPB2-L01-21` — Phương Trình Pell Cơ Bản

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

### `CPPB2-L01-22` — Phân Tích Legendre Nâng Cao

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

### `CPPB2-L02-01` — Lũy thừa nhanh cơ bản

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

### `CPPB2-L02-02` — Tính giá trị phân số modulo

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

### `CPPB2-L02-03` — Lũy thừa ma trận 2x2 (dãy fibonacci lớn)

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

### `CPPB2-L02-04` — Nghịch đảo modulo tổng quát

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

### `CPPB2-L02-05` — Tính tổ hợp $c_n^k \bmod (10^9+7)$

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

### `CPPB2-L02-06` — Lũy thừa với số mũ cực lớn

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

### `CPPB2-L02-07` — Nhân modulo hai số cực lớn (nhân ấn độ)

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

### `CPPB2-L02-08` — Tổng cấp số nhân $s_n = \sum_{i=0}^n a^i \bmod m$

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

### `CPPB2-L02-09` — Tháp lũy thừa $a^{b^c} \bmod m$

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

### `CPPB2-L02-10` — Đếm dãy ngoặc đúng (số Catalan modulo)

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

### `CPPB2-L02-11` — Hệ phương trình đồng dư (chinese remainder theorem)

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

### `CPPB2-L02-12` — Tiền xử lý nghịch đảo tuyến tính $\mathcal{o}(n)$

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

### `CPPB2-L02-13` — Lũy thừa ma trận kích thước $k \times k$

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

### `CPPB2-L02-14` — Căn bậc hai modulo nguyên tố (thuật toán tonelli-shanks)

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

### `CPPB2-L02-15` — Lũy thừa số mũ lớn khi modulo là hợp số

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

### `CPPB2-L02-16` — Logarit rời rạc (baby-step giant-step)

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

### `CPPB2-L02-17` — Lũy Thừa Ma Trận Đếm Đường Đi

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

### `CPPB2-L02-18` — Tính Cấp Số Nhân theo modulo Hợp Số

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

### `CPPB2-L02-19` — Lũy Thừa Tầng Tháp (Power Tower)

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

### `CPPB2-L02-20` — Căn Bậc Hai theo modulo bằng Tonelli-Shanks

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

### `CPPB2-L02-21` — Ma Trận Fibonacci Tổng Đoạn

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

### `CPPB2-L02-22` — Số tribonacci thứ n bằng nhân ma trận 3x3

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

### `CPPB2-L03-01` — Chặt nhị phân cắt gỗ (eko)

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

### `CPPB2-L03-02` — Chia bánh pizza đều nhau

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

### `CPPB2-L03-03` — Chuồng bò xa nhau nhất (aggressive cows)

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

### `CPPB2-L03-04` — Phân chia công việc thợ sơn (painter's partition)

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

### `CPPB2-L03-05` — Đoàn tàu vận chuyển hàng hóa

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

### `CPPB2-L03-06` — Khoảng cách dây cáp nhỏ nhất

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

### `CPPB2-L03-07` — Trung bình cộng đoạn con lớn nhất $\ge k$

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

### `CPPB2-L03-08` — Tối ưu hóa chi phí lắp trạm phát sóng

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

### `CPPB2-L03-09` — Tìm phần tử nhỏ thứ k trong bảng nhân $n \times n$

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

### `CPPB2-L03-10` — Tối ưu phân đoạn trọng số ma trận 2d

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

### `CPPB2-L03-11` — Tìm nghiệm thực của phương trình phi tuyến

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

### `CPPB2-L03-12` — Đếm số cặp $(a_i, b_j)$ có tổng trong khoảng $[l, r]$

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

### `CPPB2-L03-13` — Phần tử nhỏ thứ k của hợp hai mảng đã sắp xếp

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

### `CPPB2-L03-14` — Tối ưu phân đoạn trọng số ma trận 2d

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

### `CPPB2-L03-15` — Chặt nhị phân song song (parallel binary search)

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

### `CPPB2-L03-16` — Khoảng cách cực trị trên đa giác lồi

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

### `CPPB2-L03-17` — Chặt nhị phân song song

```cpp
#include <bits/stdc++.h>
using namespace std;

// Parallel Binary Search (Chặt nhị phân song song)
const int MAXN = 100005;
int L[MAXN], R[MAXN], mid_val[MAXN], ans[MAXN];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;

    for (int i = 1; i <= q; ++i) {
        L[i] = 1; R[i] = n; ans[i] = -1;
    }

    // Mô phỏng các vòng lặp Parallel BS
    for (int iter = 0; iter < 20; ++iter) {
        vector<vector<int>> check_at(n + 1);
        bool has_query = false;
        for (int i = 1; i <= q; ++i) {
            if (L[i] <= R[i]) {
                mid_val[i] = (L[i] + R[i]) / 2;
                check_at[mid_val[i]].push_back(i);
                has_query = true;
            }
        }
        if (!has_query) break;

        for (int m = 1; m <= n; ++m) {
            for (int q_idx : check_at[m]) {
                ans[q_idx] = m;
                R[q_idx] = m - 1; // Điều kiện tìm nghiệm nhỏ nhất
            }
        }
    }

    for (int i = 1; i <= q; ++i) cout << (ans[i] == -1 ? 1 : ans[i]) << "\n";
    return 0;
}

```

### `CPPB2-L03-18` — Tìm cực tiểu của hàm bậc hai

```cpp
#include <bits/stdc++.h>
using namespace std;

// Ternary Search tìm cực tiểu hàm lồi f(x)
double f(double x, double a, double b, double c) {
    return a * x * x + b * x + c;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    double a, b, c, left_bound, right_bound;
    if (!(cin >> a >> b >> c >> left_bound >> right_bound)) return 0;

    for (int iter = 0; iter < 100; ++iter) {
        double m1 = left_bound + (right_bound - left_bound) / 3.0;
        double m2 = right_bound - (right_bound - left_bound) / 3.0;
        if (f(m1, a, b, c) < f(m2, a, b, c)) {
            right_bound = m2;
        } else {
            left_bound = m1;
        }
    }

    cout << fixed << setprecision(6) << left_bound << "\n";
    return 0;
}

```

### `CPPB2-L03-19` — Trung vị của hai mảng đã sắp xếp

```cpp
#include <bits/stdc++.h>
using namespace std;

// Tìm trung vị của hai mảng đã sắp xếp trong O(log(min(N, M)))
double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
    if (nums1.size() > nums2.size()) return findMedianSortedArrays(nums2, nums1);
    int m = nums1.size(), n = nums2.size();
    int low = 0, high = m;

    while (low <= high) {
        int i = (low + high) / 2;
        int j = (m + n + 1) / 2 - i;

        int maxLeft1 = (i == 0) ? INT_MIN : nums1[i - 1];
        int minRight1 = (i == m) ? INT_MAX : nums1[i];

        int maxLeft2 = (j == 0) ? INT_MIN : nums2[j - 1];
        int minRight2 = (j == n) ? INT_MAX : nums2[j];

        if (maxLeft1 <= minRight2 && maxLeft2 <= minRight1) {
            if ((m + n) % 2 == 0) {
                return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2.0;
            } else {
                return max(maxLeft1, maxLeft2);
            }
        } else if (maxLeft1 > minRight2) {
            high = i - 1;
        } else {
            low = i + 1;
        }
    }
    return 0.0;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<int> a(n), b(m);
    for (int i = 0; i < n; ++i) cin >> a[i];
    for (int j = 0; j < m; ++j) cin >> b[j];

    cout << fixed << setprecision(1) << findMedianSortedArrays(a, b) << "\n";
    return 0;
}

```

### `CPPB2-L03-20` — Tam giác có diện tích lớn nhất

```cpp
#include <bits/stdc++.h>
using namespace std;

// Diện tích tam giác tính theo tọa độ không dùng struct
long long cross_product(long long x1, long long y1, long long x2, long long y2, long long x3, long long y3) {
    return abs((x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1));
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> x(n), y(n);
    for (int i = 0; i < n; ++i) cin >> x[i] >> y[i];

    long long max_area2 = 0;
    for (int i = 0; i < n; ++i) {
        int k = (i + 2) % n;
        for (int j = (i + 1) % n; j != i; j = (j + 1) % n) {
            while (cross_product(x[i], y[i], x[j], y[j], x[(k + 1) % n], y[(k + 1) % n]) >
                   cross_product(x[i], y[i], x[j], y[j], x[k], y[k])) {
                k = (k + 1) % n;
            }
            max_area2 = max(max_area2, cross_product(x[i], y[i], x[j], y[j], x[k], y[k]));
        }
    }

    cout << fixed << setprecision(1) << max_area2 / 2.0 << "\n";
    return 0;
}

```

### `CPPB2-L03-21` — Chặt Nhị Phân Khoảng Cách K Điểm

```cpp
#include <bits/stdc++.h>
using namespace std;

bool check(long long mid, const vector<long long>& x, int c) {
    int count = 1;
    long long last_pos = x[0];
    for (size_t i = 1; i < x.size(); ++i) {
        if (x[i] - last_pos >= mid) {
            count++;
            last_pos = x[i];
            if (count == c) return true;
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

    long long low = 1, high = x[n - 1] - x[0], ans = 0;
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

### `CPPB2-L03-22` — Chặt Nhị Phân Phân Số Tối Giản

```cpp
#include <bits/stdc++.h>
using namespace std;

// Tìm phân số tối giản thứ K trong đoạn (0, 1) có mẫu <= N
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n; long long k;
    if (!(cin >> n >> k)) return 0;

    double low = 0.0, high = 1.0;
    int best_p = 0, best_q = 1;

    for (int iter = 0; iter < 60; ++iter) {
        double mid = (low + high) / 2.0;
        long long count = 0;
        int p_curr = 0, q_curr = 1;

        for (int q = 1; q <= n; ++q) {
            int p = (int)(mid * q);
            count += p;
            if (p > 0 && 1.0 * p / q > 1.0 * p_curr / q_curr) {
                p_curr = p;
                q_curr = q;
            }
        }

        if (count < k) {
            low = mid;
        } else {
            best_p = p_curr;
            best_q = q_curr;
            high = mid;
        }
    }

    cout << best_p << " " << best_q << "\n";
    return 0;
}

```

## Chương 02 — Bài 04: Kỹ thuật mảng: Two Pointers, Window & 2D Prefix

### `CPPB2-L04-01` — Truy vấn tổng ma trận con 2d

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

### `CPPB2-L04-02` — Cập nhật hình chữ nhật ma trận 2d

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

### `CPPB2-L04-03` — Đoạn con ngắn nhất có tổng $\ge s$

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

### `CPPB2-L04-04` — Nén tọa độ & đếm tần suất trên dải lớn

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

### `CPPB2-L04-05` — Đoạn con dài nhất có không quá k số khác nhau

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

### `CPPB2-L04-06` — Ma trận con có tổng lớn nhất (maximum submatrix sum)

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

### `CPPB2-L04-07` — Diện tích phủ bởi các hình chữ nhật rời rạc

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

### `CPPB2-L04-08` — Đếm cặp đoạn thẳng chồng lấn nhau

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

### `CPPB2-L04-09` — Cửa sổ trượt đếm số lượng xâu anagram

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

### `CPPB2-L04-10` — Đếm hình vuông con có tổng đúng bằng k

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

### `CPPB2-L04-11` — Khử chiều 3-sum & 4-sum hai con trỏ

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

### `CPPB2-L04-12` — Đếm số đoạn con có hiệu max - min $\le k$

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

### `CPPB2-L04-13` — Đoạn con ngắn nhất chứa đầy đủ bảng chữ cái

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

### `CPPB2-L04-14` — Mảng hiệu trên cây (Tree difference array)

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

### `CPPB2-L04-15` — Đếm tam giác có độ dài cạnh hợp lệ

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

### `CPPB2-L04-16` — Quét đường thẳng nén tọa độ (sweep-line area 2d)

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

### `CPPB2-L04-17` — Diện tích hợp các hình chữ nhật

```cpp
#include <bits/stdc++.h>
using namespace std;

// Sweep-line dùng vector<vector<long long>> biểu diễn sự kiện: {x, type, y1, y2}
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<vector<long long>> events;
    vector<long long> Y;

    for (int i = 0; i < n; ++i) {
        long long x1, y1, x2, y2;
        cin >> x1 >> y1 >> x2 >> y2;
        events.push_back({x1, 1, y1, y2});
        events.push_back({x2, -1, y1, y2});
        Y.push_back(y1);
        Y.push_back(y2);
    }

    sort(Y.begin(), Y.end());
    Y.erase(unique(Y.begin(), Y.end()), Y.end());
    sort(events.begin(), events.end());

    vector<int> count_cover(Y.size(), 0);
    long long total_area = 0;

    for (size_t i = 0; i + 1 < events.size(); ++i) {
        int y1_idx = lower_bound(Y.begin(), Y.end(), events[i][2]) - Y.begin();
        int y2_idx = lower_bound(Y.begin(), Y.end(), events[i][3]) - Y.begin();

        for (int j = y1_idx; j < y2_idx; ++j) {
            count_cover[j] += events[i][1];
        }

        long long covered_len = 0;
        for (size_t j = 0; j + 1 < Y.size(); ++j) {
            if (count_cover[j] > 0) {
                covered_len += Y[j + 1] - Y[j];
            }
        }
        total_area += covered_len * (events[i + 1][0] - events[i][0]);
    }

    cout << total_area << "\n";
    return 0;
}

```

### `CPPB2-L04-18` — Mảng hiệu trên hình vuông xoay 45 độ

```cpp
#include <bits/stdc++.h>
using namespace std;

// Biến đổi tọa độ quay 45 độ: u = x + y, v = x - y + N
const int MAXN = 2005;
long long diff[MAXN][MAXN], pref[MAXN][MAXN];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;

    while (q--) {
        int x, y, d; long long val;
        cin >> x >> y >> d >> val;
        int u1 = max(1, x + y - d), u2 = min(2 * n, x + y + d);
        int v1 = max(1, x - y + n - d), v2 = min(2 * n, x - y + n + d);

        diff[u1][v1] += val;
        diff[u1][v2 + 1] -= val;
        diff[u2 + 1][v1] -= val;
        diff[u2 + 1][v2 + 1] += val;
    }

    for (int i = 1; i <= 2 * n; ++i) {
        for (int j = 1; j <= 2 * n; ++j) {
            pref[i][j] = diff[i][j] + pref[i - 1][j] + pref[i][j - 1] - pref[i - 1][j - 1];
        }
    }

    long long max_val = 0;
    for (int x = 1; x <= n; ++x) {
        for (int y = 1; y <= n; ++y) {
            int u = x + y;
            int v = x - y + n;
            max_val = max(max_val, pref[u][v]);
        }
    }

    cout << max_val << "\n";
    return 0;
}

```

### `CPPB2-L04-19` — Nén Tọa Độ Đa Chiều 3D

```cpp
#include <bits/stdc++.h>
using namespace std;

// Nén tọa độ 3D dùng vector<vector<int>>: {x1, y1, z1, x2, y2, z2}
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<vector<int>> boxes(n, vector<int>(6));
    vector<int> X, Y, Z;

    for (int i = 0; i < n; ++i) {
        cin >> boxes[i][0] >> boxes[i][1] >> boxes[i][2];
        cin >> boxes[i][3] >> boxes[i][4] >> boxes[i][5];
        X.push_back(boxes[i][0]); X.push_back(boxes[i][3]);
        Y.push_back(boxes[i][1]); Y.push_back(boxes[i][4]);
        Z.push_back(boxes[i][2]); Z.push_back(boxes[i][5]);
    }

    sort(X.begin(), X.end()); X.erase(unique(X.begin(), X.end()), X.end());
    sort(Y.begin(), Y.end()); Y.erase(unique(Y.begin(), Y.end()), Y.end());
    sort(Z.begin(), Z.end()); Z.erase(unique(Z.begin(), Z.end()), Z.end());

    int nx = X.size(), ny = Y.size(), nz = Z.size();
    vector<vector<vector<int>>> grid(nx, vector<vector<int>>(ny, vector<int>(nz, 0)));

    for (const auto& b : boxes) {
        int x1 = lower_bound(X.begin(), X.end(), b[0]) - X.begin();
        int x2 = lower_bound(X.begin(), X.end(), b[3]) - X.begin();
        int y1 = lower_bound(Y.begin(), Y.end(), b[1]) - Y.begin();
        int y2 = lower_bound(Y.begin(), Y.end(), b[4]) - Y.begin();
        int z1 = lower_bound(Z.begin(), Z.end(), b[2]) - Z.begin();
        int z2 = lower_bound(Z.begin(), Z.end(), b[5]) - Z.begin();

        for (int i = x1; i < x2; ++i) {
            for (int j = y1; j < y2; ++j) {
                for (int k = z1; k < z2; ++k) {
                    grid[i][j][k] = 1;
                }
            }
        }
    }

    long long total_vol = 0;
    for (int i = 0; i + 1 < nx; ++i) {
        for (int j = 0; j + 1 < ny; ++j) {
            for (int k = 0; k + 1 < nz; ++k) {
                if (grid[i][j][k]) {
                    total_vol += 1LL * (X[i + 1] - X[i]) * (Y[j + 1] - Y[j]) * (Z[k + 1] - Z[k]);
                }
            }
        }
    }

    cout << total_vol << "\n";
    return 0;
}

```

### `CPPB2-L04-20` — Đếm số bộ ba tam giác hợp lệ

```cpp
#include <bits/stdc++.h>
using namespace std;

// Đếm bộ ba (a, b, c) thỏa mãn bất đẳng thức tam giác: a + b > c
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    sort(a.begin(), a.end());
    long long count_triangles = 0;

    for (int k = n - 1; k >= 2; --k) {
        int i = 0, j = k - 1;
        while (i < j) {
            if (a[i] + a[j] > a[k]) {
                count_triangles += (j - i);
                j--;
            } else {
                i++;
            }
        }
    }

    cout << count_triangles << "\n";
    return 0;
}

```

### `CPPB2-L04-21` — Đếm xâu con có đúng k ký tự khác nhau

```cpp
#include <bits/stdc++.h>
using namespace std;

long long atMostKDistinct(const string& s, int k) {
    if (k <= 0) return 0;
    int n = s.size();
    vector<int> freq(26, 0);
    int distinct_count = 0, l = 0;
    long long ans = 0;

    for (int r = 0; r < n; ++r) {
        if (freq[s[r] - 'a'] == 0) distinct_count++;
        freq[s[r] - 'a']++;

        while (distinct_count > k) {
            freq[s[l] - 'a']--;
            if (freq[s[l] - 'a'] == 0) distinct_count--;
            l++;
        }
        ans += (r - l + 1);
    }
    return ans;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s; int k;
    if (!(cin >> s >> k)) return 0;

    cout << atMostKDistinct(s, k) - atMostKDistinct(s, k - 1) << "\n";
    return 0;
}

```

### `CPPB2-L04-22` — Ma Trận Tổng Lớn Nhất (Kadane 2D)

```cpp
#include <bits/stdc++.h>
using namespace std;

// Kadane 2D tìm ma trận con có tổng lớn nhất O(N^3)
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<vector<long long>> a(n, vector<long long>(m));
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            cin >> a[i][j];
        }
    }

    long long max_sum = LLONG_MIN;

    for (int top = 0; top < n; ++top) {
        vector<long long> temp(m, 0);
        for (int bottom = top; bottom < n; ++bottom) {
            for (int j = 0; j < m; ++j) {
                temp[j] += a[bottom][j];
            }

            // Kadane 1D
            long long current = 0;
            for (int j = 0; j < m; ++j) {
                current += temp[j];
                max_sum = max(max_sum, current);
                if (current < 0) current = 0;
            }
        }
    }

    cout << max_sum << "\n";
    return 0;
}

```

## Chương 03 — Bài 05: Đệ quy, chia để trị & Meet in the Middle

### `CPPB2-L05-01` — Đếm cặp nghịch thế

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

### `CPPB2-L05-02` — Cái túi kích thước nhỏ (knapsack $n \le 40$)

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

### `CPPB2-L05-03` — Tập con có tổng gần s nhất

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

### `CPPB2-L05-04` — Giải phương trình $4$ ẩn tuyến tính (4-sum mitm)

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

### `CPPB2-L05-05` — Đếm số tập con có xor bằng k

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

### `CPPB2-L05-06` — Khoảng cách giữa hai điểm gần nhất (closest pair)

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

### `CPPB2-L05-07` — Bẻ khóa mật mã đổi dấu (subset sum with signs)

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

### `CPPB2-L05-08` — Tối ưu hóa tuyến đường đi qua đỉnh (shortest path with mitm)

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

### `CPPB2-L05-09` — Trò chơi xếp gạch đa diện (puzzle mitm)

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

### `CPPB2-L05-10` — Đếm cặp $a_i > 2 a_j$ (significant inversions)

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

### `CPPB2-L05-11` — Tổng cấp số nhân bằng chia để trị

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

### `CPPB2-L05-12` — Tối ưu hóa tuyến đường đi qua đỉnh (shortest path mitm)

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

### `CPPB2-L05-13` — Trò chơi xếp gạch đa diện (15-puzzle mitm)

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

### `CPPB2-L05-14` — Phân chia tập hợp thành hai nửa có tổng bằng nhau

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

### `CPPB2-L05-15` — Đếm số đoạn con có tổng nằm trong $[l, r]$

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

### `CPPB2-L05-16` — Chia để trị trên cây (centroid decomposition cơ bản)

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

### `CPPB2-L05-17` — Centroid Decomposition Cơ Bản

```cpp
#include <bits/stdc++.h>
using namespace std;

// Tìm trọng tâm cây (Centroid) để chia để trị trên cây O(N log N)
const int MAXN = 100005;
vector<int> adj[MAXN];
int sz[MAXN];
bool removed[MAXN];

void get_sz(int u, int p) {
    sz[u] = 1;
    for (int v : adj[u]) {
        if (v != p && !removed[v]) {
            get_sz(v, u);
            sz[u] += sz[v];
        }
    }
}

int get_centroid(int u, int p, int total_size) {
    for (int v : adj[u]) {
        if (v != p && !removed[v] && sz[v] > total_size / 2) {
            return get_centroid(v, u, total_size);
        }
    }
    return u;
}

int decompose(int u) {
    get_sz(u, 0);
    int c = get_centroid(u, 0, sz[u]);
    removed[c] = true;
    for (int v : adj[c]) {
        if (!removed[v]) decompose(v);
    }
    return c;
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

    int root_centroid = decompose(1);
    cout << root_centroid << "\n";
    return 0;
}

```

### `CPPB2-L05-18` — Đếm Chu Trình 4 Cạnh bằng MITM

```cpp
#include <bits/stdc++.h>
using namespace std;

// Đếm số chu trình 4 đỉnh C4 bằng Meet in the Middle O(M * sqrt(M))
const int MAXN = 50005;
vector<int> adj[MAXN];
int cnt[MAXN];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    long long ans = 0;
    for (int u = 1; u <= n; ++u) {
        for (int v : adj[u]) {
            for (int w : adj[v]) {
                if (w != u && w > u) { // Đảm bảo đếm không lặp
                    ans += cnt[w];
                    cnt[w]++;
                }
            }
        }
        for (int v : adj[u]) {
            for (int w : adj[v]) {
                if (w != u && w > u) {
                    cnt[w] = 0; // Reset
                }
            }
        }
    }

    cout << ans << "\n";
    return 0;
}

```

### `CPPB2-L05-19` — Chia Để Trị Dãy Con Tổng Lớn Nhất

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

### `CPPB2-L05-20` — MITM Đếm Nghiệm Nguyên Tổng Bằng 0

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

### `CPPB2-L05-21` — Tìm Cặp Điểm Gần Nhất 2D

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

### `CPPB2-L05-22` — Đếm Nghịch Thế 3 Chiều bằng CDQ

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

### `CPPB2-L06-01` — Bài toán người du lịch (tsp)

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

### `CPPB2-L06-02` — Đếm số phần tử bật BIT chung (bitwise and)

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

### `CPPB2-L06-03` — Bài toán người du lịch (tsp bitmask DP)

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

### `CPPB2-L06-04` — Phân chia công việc hoàn hảo (job assignment)

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

### `CPPB2-L06-05` — Duyệt tất cả submask tính tổng phân hoạch

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

### `CPPB2-L06-06` — Đường đi hamilton đếm số cách

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

### `CPPB2-L06-07` — Tối đa hóa giá trị xor đoạn con bằng Trie BIT

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

### `CPPB2-L06-08` — Ghép cặp trọng số cực đại (maximum matching bitmask)

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

### `CPPB2-L06-09` — SOS DP Tổng Trên Tập Con (Cộng Dồn Theo Nhóm)

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

### `CPPB2-L06-10` — Đếm số cặp $(a_i, a_j)$ có tích and bằng 0

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

### `CPPB2-L06-11` — SOS DP Tổng Trên Tập Con (Ưu Đãi Theo Giỏ Hàng)

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

### `CPPB2-L06-12` — Tô màu đồ thị số lượng màu nhỏ nhất (graph coloring)

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

### `CPPB2-L06-13` — Tìm chu trình hamilton chi phí nhỏ nhất

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

### `CPPB2-L06-14` — Tập độc lập trọng số lớn nhất trên đồ thị nhỏ

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

### `CPPB2-L06-15` — Phân hoạch tập hợp thành k tập con có tổng bằng nhau

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

### `CPPB2-L06-16` — Tối ưu hóa trò chơi nim tổng quát (sprague-grundy BIT)

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

### `CPPB2-L06-17` — SOS DP Tổng Trên Tập Con Cơ Bản

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

### `CPPB2-L06-18` — Profile DP Lát Gạch Domino

```cpp
#include <bits/stdc++.h>
using namespace std;

// Profile DP / DP Broken Profile lát gạch 1x2 trên lưới NxM
int dp[2][1 << 12];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;
    if (n < m) swap(n, m);

    dp[0][0] = 1;
    int cur = 0, next = 1;

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            memset(dp[next], 0, sizeof(dp[next]));
            for (int mask = 0; mask < (1 << m); ++mask) {
                if (!dp[cur][mask]) continue;

                if (mask & (1 << j)) {
                    // Ô đã bị chiếm bởi gạch dọc từ trên xuống
                    dp[next][mask ^ (1 << j)] += dp[cur][mask];
                } else {
                    // Đặt gạch dọc xuống dưới
                    dp[next][mask | (1 << j)] += dp[cur][mask];

                    // Đặt gạch ngang sang phải
                    if (j + 1 < m && !(mask & (1 << (j + 1)))) {
                        dp[next][mask] += dp[cur][mask];
                    }
                }
            }
            swap(cur, next);
        }
    }

    cout << dp[cur][0] << "\n";
    return 0;
}

```

### `CPPB2-L06-19` — Biến Đổi FWT với Phép XOR Bitwise

```cpp
#include <bits/stdc++.h>
using namespace std;

// Fast Walsh-Hadamard Transform (FWT) tính tích chập XOR O(N log N)
const int MOD = 1000000007;
const int INV2 = 500000004; // 2^(MOD-2) % MOD

void FWT(vector<long long>& a, bool invert) {
    int n = a.size();
    for (int len = 1; 2 * len <= n; len <<= 1) {
        for (int i = 0; i < n; i += 2 * len) {
            for (int j = 0; j < len; ++j) {
                long long u = a[i + j];
                long long v = a[i + len + j];
                if (!invert) {
                    a[i + j] = (u + v) % MOD;
                    a[i + len + j] = (u - v + MOD) % MOD;
                } else {
                    a[i + j] = (u + v) % MOD * INV2 % MOD;
                    a[i + len + j] = (u - v + MOD) % MOD * INV2 % MOD;
                }
            }
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    int sz = 1 << n;
    vector<long long> a(sz), b(sz);
    for (int i = 0; i < sz; ++i) cin >> a[i];
    for (int i = 0; i < sz; ++i) cin >> b[i];

    FWT(a, false);
    FWT(b, false);
    for (int i = 0; i < sz; ++i) a[i] = (a[i] * b[i]) % MOD;
    FWT(a, true);

    for (int i = 0; i < sz; ++i) cout << a[i] << " ";
    cout << "\n";
    return 0;
}

```

### `CPPB2-L06-20` — Đếm Tập Độc Lập Cực Đại

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

### `CPPB2-L06-21` — Bitmask DP Phân Nhóm K Tập

```cpp
#include <bits/stdc++.h>
using namespace std;

// Chia mảng thành K tập có tổng bằng nhau bằng Bitmask DP
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    vector<int> a(n);
    int total_sum = 0;
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        total_sum += a[i];
    }

    if (total_sum % k != 0) {
        cout << "NO\n";
        return 0;
    }

    int target = total_sum / k;
    vector<int> dp(1 << n, -1);
    dp[0] = 0;

    for (int mask = 0; mask < (1 << n); ++mask) {
        if (dp[mask] == -1) continue;
        for (int i = 0; i < n; ++i) {
            if (!(mask & (1 << i))) {
                if (dp[mask] + a[i] <= target) {
                    dp[mask | (1 << i)] = (dp[mask] + a[i]) % target;
                }
            }
        }
    }

    cout << (dp[(1 << n) - 1] == 0 ? "YES\n" : "NO\n");
    return 0;
}

```

### `CPPB2-L06-22` — XOR Basis trong Không Gian Vectơ Tuyến Tính

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

### `CPPB2-L06-23` — Bitmask Ghép Đôi Trọng Số Cực Đại

```cpp
#include <bits/stdc++.h>
using namespace std;

// Bitmask DP ghép cặp trọng số lớn nhất
long long dp[1 << 20];
long long cost[20][20];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    for (int i = 0; i < 2 * n; ++i) {
        for (int j = 0; j < 2 * n; ++j) {
            cin >> cost[i][j];
        }
    }

    int total_nodes = 2 * n;
    memset(dp, 0, sizeof(dp));

    for (int mask = 0; mask < (1 << total_nodes); ++mask) {
        int i = 0;
        while (i < total_nodes && (mask & (1 << i))) i++;
        if (i == total_nodes) continue;

        for (int j = i + 1; j < total_nodes; ++j) {
            if (!(mask & (1 << j))) {
                int next_mask = mask | (1 << i) | (1 << j);
                dp[next_mask] = max(dp[next_mask], dp[mask] + cost[i][j]);
            }
        }
    }

    cout << dp[(1 << total_nodes) - 1] << "\n";
    return 0;
}

```

### `CPPB2-L06-24` — Đếm Đường Đi Hamilton bằng Bitmask

```cpp
#include <bits/stdc++.h>
using namespace std;

const int MOD = 1000000007;
int dp[1 << 20][20];
vector<int> adj[20];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        u--; v--;
        adj[u].push_back(v);
    }

    dp[1][0] = 1; // Bắt đầu từ đỉnh 0 với mask = 1

    for (int mask = 1; mask < (1 << n); ++mask) {
        for (int u = 0; u < n; ++u) {
            if (!dp[mask][u]) continue;
            if (u == n - 1 && mask != (1 << n) - 1) continue;

            for (int v : adj[u]) {
                if (!(mask & (1 << v))) {
                    int next_mask = mask | (1 << v);
                    dp[next_mask][v] = (dp[next_mask][v] + dp[mask][u]) % MOD;
                }
            }
        }
    }

    cout << dp[(1 << n) - 1][n - 1] << "\n";
    return 0;
}

```




\newpage

# Mục lục


