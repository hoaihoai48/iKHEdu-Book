# CHUYÊN ĐỀ 07: LÝ THUYẾT SỐ & SỐ NGUYÊN TỐ (NUMBER THEORY FOUNDATIONS)
*(GCD / LCM, Prime Factorization, Sieve of Eratosthenes, SPF, Segmented Sieve, Legendre & Euler's Totient)*

---

## 1. Bản Chất Vấn Đề & Trực Giác Thuật Toán (The Core Problem & Intuition)

Trong khoa học máy tính và lập trình thi đấu, các bài toán xoay quanh **ước số, bội số và số nguyên tố** là nền tảng của mật mã học (như thuật toán mã hóa khóa công khai RSA), phân tích độ phức tạp thuật toán và tối ưu hóa tài nguyên.

### Vấn đề 1: Tìm Ước chung lớn nhất (GCD)
Cho hai số nguyên dương $A$ và $B$. Ước chung lớn nhất $\gcd(A, B)$ là số nguyên dương lớn nhất đồng thời chia hết cả $A$ và $B$.
* **Cách ngây thơ:** Thử tất cả các số từ $\min(A, B)$ giảm dần về $1 \implies \mathcal{O}(\min(A, B))$. Khi $A, B \approx 10^{18}$, cách này hoàn toàn bất khả thi.
* **Định lý Euclid:** $\gcd(A, B) = \gcd(B, A \pmod B)$.
  * Mỗi bước lấy dư $A \pmod B$, giá trị giảm ít nhất một nửa sau mỗi 2 bước lặp $\implies$ Thuật toán dừng lại sau tối đa $\mathcal{O}(\log(\min(A, B)))$ bước (khoảng $\le 60$ phép tính với số $10^{18}$).

### Vấn đề 2: Kiểm tra số nguyên tố & Phân tích thừa số nguyên tố
Một số nguyên $N > 1$ là số nguyên tố nếu nó chỉ có đúng 2 ước là $1$ và chính nó.
* **Tính chất đối xứng của ước số:** Nếu $d$ là ước của $N$ thì $\frac{N}{d}$ cũng là ước của $N$.
* **Bất biến $\sqrt{N}$:** Nếu $N$ là hợp số, nó **bắt buộc phải có ít nhất một ước nguyên tố $p \le \sqrt{N}$**. Do đó, ta chỉ cần duyệt kiểm tra các số từ $2$ đến $\lfloor \sqrt{N} \rfloor$ trong $\mathcal{O}(\sqrt{N})$ thay vì $\mathcal{O}(N)$.

---

## 2. Mô Phỏng Từng Bước (Visual Step-by-Step Simulation)

### 💡 Ví Dụ 1: Mô phỏng thuật toán Euclid tìm $\gcd(252, 105)$

| Bước lặp | $A$ | $B$ | Phép chia lấy dư $A \pmod B$ | Trạng thái tiếp theo $(A', B') = (B, A \pmod B)$ |
|:---:|:---:|:---:|:---:|:---:|
| **1** | $252$ | $105$ | $252 \pmod{105} = 42$ | $(105, 42)$ |
| **2** | $105$ | $42$ | $105 \pmod{42} = 21$ | $(42, 21)$ |
| **3** | $42$ | $21$ | $42 \pmod{21} = 0$ | $(21, 0)$ |
| **Kết thúc** | $21$ | $0$ | $B = 0 \implies \text{Dừng}$ | **$\gcd(252, 105) = 21$** |

---

### 💡 Ví Dụ 2: Mô phỏng Sàng Eratosthenes tìm các số nguyên tố $\le 20$

1. Khởi tạo mảng đánh dấu `isPrime` từ $2 \dots 20$ đều là `true`.
2. Xét $i = 2$ (nguyên tố) $\implies$ Gạch bỏ các bội $4, 6, 8, 10, 12, 14, 16, 18, 20$.
3. Xét $i = 3$ (nguyên tố) $\implies$ Gạch bỏ các bội $9, 12, 15, 18$ (bắt đầu gạch từ $i^2 = 9$).
4. Xét $i = 4$ (đã bị gạch) $\implies$ Bỏ qua.
5. Vì $i^2 = 5^2 = 25 > 20$, vòng lặp dừng lại.

| $N$ | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Trạng thái** | 🟢 | 🟢 | ❌ | 🟢 | ❌ | 🟢 | ❌ | ❌ | ❌ | 🟢 | ❌ | 🟢 | ❌ | ❌ | ❌ | 🟢 | ❌ | 🟢 | ❌ |

> **Danh sách số nguyên tố $\le 20$:** $\{2, 3, 5, 7, 11, 13, 17, 19\}$ (gồm 8 số).

---

## 3. Lý Thuyết Cốt Lõi & Bất Biến Toán Học (Core Invariants)

### 3.1. Mối quan hệ giữa GCD và LCM
$$\gcd(A, B) \times \text{lcm}(A, B) = A \times B \implies \text{lcm}(A, B) = \frac{A}{\gcd(A, B)} \times B$$

> [!CAUTION]
> **TỬ HUYỆT TRÀN SỐ KHI TÍNH BỘI CHUNG NHỎ NHẤT (LCM):**
> * Không viết `(A * B) / gcd(A, B)` vì tích $A \times B$ có thể lên tới $10^{36}$ gây tràn số `long long`.
> * Luôn viết: `long long lcm = (a / gcd(a, b)) * b;`
> * **Lưu ý chuyên sâu:** Việc chia trước giúp triệt tiêu nguy cơ tràn số ở bước trung gian; tuy nhiên, nếu bản thân giá trị $\text{lcm}(A, B)$ thực tế vượt quá $9 \cdot 10^{18}$ (giới hạn của `long long`), ta bắt buộc phải sử dụng `__int128` hoặc kiểu dữ liệu số lớn (Big Integer).

---

### 3.2. Định lý cơ bản của Số học & Công thức nhân tính
Mọi số nguyên $N > 1$ đều phân tích duy nhất thành tích các thừa số nguyên tố:
$$N = p_1^{a_1} \times p_2^{a_2} \times \dots \times p_k^{a_k}$$

* **Số lượng ước số của $N$ ($\sigma_0(N)$):**
  $$\text{d}(N) = (a_1 + 1)(a_2 + 1)\dots(a_k + 1)$$
* **Tổng các ước số của $N$ ($\sigma_1(N)$):**
  $$\sigma(N) = \frac{p_1^{a_1+1} - 1}{p_1 - 1} \times \frac{p_2^{a_2+1} - 1}{p_2 - 1} \times \dots \times \frac{p_k^{a_k+1} - 1}{p_k - 1}$$

---

### 3.3. Sàng Ước Nguyên Tố Nhỏ Nhất (SPF - Smallest Prime Factor)
Thay vì chỉ lưu mảng `bool`, ta lưu mảng `spf[x]` là **ước số nguyên tố nhỏ nhất của $x$**.
* Phân tích thừa số nguyên tố bằng SPF cần tối đa $\mathcal{O}(\log X)$ lần chia liên tiếp, giúp trả lời cực nhanh cho hàng trăm nghìn truy vấn độc lập.

---

### 3.4. Phi Hàm Euler (Euler's Totient Function $\phi(N)$)
Phi hàm Euler $\phi(N)$ đếm số lượng số nguyên dương trong đoạn $[1, N]$ nguyên tố cùng nhau với $N$ ($\gcd(k, N) = 1$):
$$\phi(N) = N \times \left(1 - \frac{1}{p_1}\right) \times \left(1 - \frac{1}{p_2}\right) \dots \left(1 - \frac{1}{p_k}\right)$$

* **Tính chất bất biến:** $\sum_{d | N} \phi(d) = N$.
* **Sàng Phi hàm Euler trong $\mathcal{O}(N \log \log N)$:** Cho phép tính $\phi(1) \dots \phi(N)$ đồng thời trên mảng, dùng để đếm tổng số cặp số $(x, y) \le N$ thỏa mãn $\gcd(x, y) = 1$ qua công thức $2 \sum_{i=1}^N \phi(i) - 1$.

---

## 4. Các Bẫy Lỗi Lập Trình Kinh Điển (Bug Traps)

1. **Tràn số khi so sánh vòng lặp căn bậc hai:**
   * Viết `for (int i = 2; i * i <= n; ++i)` sẽ bị tràn số số nguyên 32-bit nếu $i \approx 46341 \implies i^2 < 0$ dẫn đến vòng lặp vô tận (TLE).
   * **Cách sửa:** Dùng `1LL * i * i <= n` hoặc `i <= n / i`.

2. **Quên xử lý phần dư cuối cùng sau khi phân tích $\mathcal{O}(\sqrt{N})$:**
   * Sau khi chia triệt để cho các ước nguyên tố $p \le \sqrt{N}$, nếu $N > 1$ thì giá trị còn lại của $N$ **chắc chắn là một số nguyên tố lớn hơn $\sqrt{N}$**. Nếu bỏ qua bước này sẽ thiếu thừa số cuối cùng.

3. **Số $0$ và số $1$ không phải là số nguyên tố:**
   * Hàm kiểm tra số nguyên tố bắt buộc phải kiểm tra `if (n < 2) return false;`.

---

## 5. Mẫu Cài Đặt Chuẩn Thi Đấu (Competitive Templates)

### Mẫu 1: Ước Chung Lớn Nhất & Bội Chung Nhỏ Nhất
```cpp
#include <bits/stdc++.h>
using namespace std;

// GCD bằng thuật toán Euclid lặp O(log(min(A, B)))
long long getGcd(long long a, long long b) {
    while (b != 0) {
        long long r = a % b;
        a = b;
        b = r;
    }
    return a;
}

// LCM an toàn chống tràn số
long long getLcm(long long a, long long b) {
    if (a == 0 || b == 0) return 0;
    return (a / getGcd(a, b)) * b;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long a, b;
    if (!(cin >> a >> b)) return 0;

    cout << getGcd(a, b) << " " << getLcm(a, b) << "\n";
    return 0;
}
```

---

### Mẫu 2: Sàng Eratosthenes & Sàng SPF (Tối Ưu Phân Tích Thừa Số)
```cpp
#include <bits/stdc++.h>
using namespace std;

const int MAXN = 1000000;
vector<int> spf(MAXN + 1);

// Tiền xử lý Sàng SPF trong O(N log log N)
void sieveSPF() {
    for (int i = 1; i <= MAXN; ++i) spf[i] = i;
    for (int i = 2; 1LL * i * i <= MAXN; ++i) {
        if (spf[i] == i) { // i là số nguyên tố
            for (int j = i * i; j <= MAXN; j += i) {
                if (spf[j] == j) {
                    spf[j] = i;
                }
            }
        }
    }
}

// Phân tích thừa số nguyên tố O(log N) cho mỗi truy vấn
vector<pair<int, int>> factorize(int n) {
    vector<pair<int, int>> factors;
    while (n > 1) {
        int p = spf[n];
        int count = 0;
        while (n % p == 0) {
            count++;
            n /= p;
        }
        factors.push_back({p, count});
    }
    return factors;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    sieveSPF();

    int q;
    if (!(cin >> q)) return 0;

    while (q--) {
        int n;
        cin >> n;
        auto factors = factorize(n);
        for (int i = 0; i < (int)factors.size(); ++i) {
            cout << factors[i].first << "^" << factors[i].second << (i + 1 == (int)factors.size() ? "" : " * ");
        }
        cout << "\n";
    }
    return 0;
}
```

---

## 6. Hệ Thống Câu Hỏi Kiểm Tra Khái Niệm (Concept Quiz)

#### Câu 1 (Độ phức tạp):
Thuật toán Euclid tìm $\gcd(A, B)$ có độ phức tạp thời gian trong trường hợp xấu nhất là bao nhiêu?
* A. $\mathcal{O}(\min(A, B))$
* B. **(Đáp án đúng)** $\mathcal{O}(\log(\min(A, B)))$
* C. $\mathcal{O}(\sqrt{\min(A, B)})$
* D. $\mathcal{O}(1)$
> *Giải thích:* Sau mỗi hai bước lặp của phép lấy dư Euclid, số nhỏ hơn sẽ giảm ít nhất một nửa, do đó số bước lặp tối đa không vượt quá $2 \log_2(\min(A, B))$.

---

#### Câu 2 (Bản chất toán học):
Trường hợp xấu nhất khiến thuật toán Euclid phải thực hiện số bước lặp nhiều nhất xảy ra khi $A$ và $B$ là hai số nào sau đây?
* A. Hai lũy thừa của 2: $A = 2^x, B = 2^y$.
* B. **(Đáp án đúng)** Hai số Fibonacci liên tiếp: $A = F_{k+1}, B = F_k$.
* C. Hai số nguyên tố rất lớn: $A = p, B = q$.
* D. Một số chẵn và một số lẻ.
> *Giải thích:* Định lý Lamé chứng minh rằng hai số Fibonacci liên tiếp luôn tạo ra các thương số bằng $1$ ở mọi bước lặp, khiến phép chia lấy dư thu hẹp chậm nhất.

---

#### Câu 3 (Cú pháp & Bẫy lỗi):
Trong template C++ chuẩn thi đấu, công thức nào sau đây được sử dụng để tính Bội chung nhỏ nhất $\text{lcm}(A, B)$ nhằm triệt tiêu nguy cơ tràn số ở bước nhân trung gian?
* A. `(a * b) / getGcd(a, b)`
* B. **(Đáp án đúng)** `(a / getGcd(a, b)) * b`
* C. `a * b * getGcd(a, b)`
* D. `(a + b) / getGcd(a, b)`
> *Giải thích:* Vì $A$ luôn chia hết cho $\gcd(A, B)$, ta thực hiện phép chia trước `(a / gcd(a, b))` để thu nhỏ giá trị trung gian trước khi nhân với $B$, giúp chống tràn số 64-bit hiệu quả.

---

#### Câu 4 (Thuật toán kiểm tra số nguyên tố):
Tại sao để kiểm tra số $N$ có phải là số nguyên tố hay không, ta chỉ cần kiểm tra các ước nguyên từ $2$ đến $\lfloor \sqrt{N} \rfloor$?
* A. Vì các số lớn hơn $\sqrt{N}$ luôn là số lẻ.
* B. **(Đáp án đúng)** Vì nếu $N = a \times b$, không thể xảy ra trường hợp cả $a$ và $b$ đều đồng thời lớn hơn $\sqrt{N}$.
* C. Vì hàm `sqrt(N)` trong C++ chạy trong $\mathcal{O}(1)$.
* D. Vì số lượng ước của $N$ không bao giờ vượt quá $\sqrt{N}$.
> *Giải thích:* Nếu $a > \sqrt{N}$ và $b > \sqrt{N}$ thì $a \times b > N$ (vô lý). Do đó, nếu $N$ là hợp số, ước nhỏ hơn bắt buộc phải nằm trong khoảng $[2, \sqrt{N}]$.

---

#### Câu 5 (Ứng dụng Sàng nguyên tố):
Độ phức tạp thời gian chuẩn của thuật toán Sàng Eratosthenes để tìm tất cả các số nguyên tố $\le N$ là:
* A. $\mathcal{O}(N \sqrt{N})$
* B. $\mathcal{O}(N \log N)$
* C. **(Đáp án đúng)** $\mathcal{O}(N \log \log N)$
* D. $\mathcal{O}(N)$
> *Giải thích:* Tổng số thao tác gạch bỏ bằng $N \sum_{p \le N} \frac{1}{p}$. Theo định lý Mertens, chuỗi nghịch đảo các số nguyên tố có tổng tiệm cận $\ln(\ln N)$, do đó độ phức tạp là $\mathcal{O}(N \log \log N)$, gần như tuyến tính tuyệt đối.

---

#### Câu 6 (Sàng SPF):
Trong kỹ thuật Sàng Ước Nguyên Tố Nhỏ Nhất (SPF), mảng `spf[x]` lưu thông tin gì?
* A. Số lượng ước nguyên tố của $x$.
* B. Tổng các chữ số của $x$.
* C. **(Đáp án đúng)** Ước số nguyên tố nhỏ nhất của số nguyên $x$.
* D. Số nguyên tố lớn nhất nhỏ hơn hoặc bằng $x$.
> *Giải thích:* `spf[x]` lưu Smallest Prime Factor của $x$, giúp phân tích thừa số nguyên tố của $x$ trong $\mathcal{O}(\log x)$ bước chia liên tiếp.

---

#### Câu 7 (Đếm số lượng ước):
Một số nguyên $N$ có dạng phân tích thừa số nguyên tố $N = p_1^3 \times p_2^4 \times p_3^1$ (với $p_1, p_2, p_3$ là các số nguyên tố phân biệt). Số $N$ có tất cả bao nhiêu ước số nguyên dương?
* A. $3 \times 4 \times 1 = 12$
* B. $3 + 4 + 1 = 8$
* C. **(Đáp án đúng)** $(3+1) \times (4+1) \times (1+1) = 4 \times 5 \times 2 = 40$ ước
* D. $40 - 1 = 39$ ước
> *Giải thích:* Theo công thức nhân tính, số lượng ước số của $N = \prod p_i^{a_i}$ là $\prod (a_i + 1)$.

---

#### Câu 8 (Đặc điểm số chính phương):
Một số nguyên dương $N$ là số chính phương ($N = k^2$) khi và chỉ khi điều kiện nào sau đây được thỏa mãn?
* A. $N$ có số lượng thừa số nguyên tố phân biệt là một số chẵn.
* B. Tổng các chữ số của $N$ chia hết cho 9.
* C. **(Đáp án đúng)** Số lượng ước số nguyên dương của $N$ là một số lẻ (tương đương số mũ của mọi thừa số nguyên tố đều là số chẵn).
* D. $N$ có chữ số tận cùng thuộc tập $\{2, 3, 7, 8\}$.
> *Giải thích:* Các ước số luôn đi thành từng cặp đối xứng $(d, \frac{N}{d})$. Chỉ khi $N = k^2$ thì cặp ước tại $k = \frac{N}{k}$ mới trùng nhau, tạo ra số lượng ước số lẻ. Về mặt thừa số nguyên tố, $N = \prod p_i^{2a_i}$ nên số lượng ước $(2a_1 + 1)(2a_2 + 1)\dots$ luôn là tích các số lẻ (kết quả là số lẻ).

---

#### Câu 9 (Công thức Legendre):
Công thức Legendre $E_p(N!) = \sum_{k=1}^{\infty} \lfloor \frac{N}{p^k} \rfloor$ dùng để tính đại lượng nào?
* A. Số lượng số nguyên tố nhỏ hơn $N!$.
* B. **(Đáp án đúng)** Số mũ của thừa số nguyên tố $p$ trong phân tích thừa số nguyên tố của $N!$.
* C. Ước chung lớn nhất của $N!$ và $p$.
* D. Số chữ số của $N!$.
> *Giải thích:* Công thức Legendre đếm số lượng bội của $p, p^2, p^3 \dots$ đóng góp vào tích $N! = 1 \times 2 \times \dots \times N$.

---

#### Câu 10 (Chữ số 0 tận cùng):
Số lượng chữ số $0$ liên tiếp tận cùng của $100!$ là bao nhiêu?
* A. $10$
* B. $20$
* C. **(Đáp án đúng)** $\lfloor \frac{100}{5} \rfloor + \lfloor \frac{100}{25} \rfloor = 20 + 4 = 24$
* D. $25$
> *Giải thích:* Mỗi chữ số 0 tận cùng được tạo bởi tích $2 \times 5$. Trong $N!$, số lượng thừa số 2 luôn nhiều hơn số lượng thừa số 5, do đó số chữ số 0 bằng số mũ của 5 trong $100!$.

---

#### Câu 11 (Sàng phân đoạn - Segmented Sieve):
Kỹ thuật Sàng phân đoạn (Segmented Sieve) được sử dụng tối ưu nhất trong tình huống nào?
* A. Khi cần tìm số nguyên tố trong khoảng $[1 \dots 10^7]$.
* B. **(Đáp án đúng)** Khi cần tìm số nguyên tố trong đoạn $[L, R]$ với $R \le 10^{12}$ nhưng độ dài đoạn $R - L \le 10^6$.
* C. Khi $L$ và $R$ đều là số chẵn.
* D. Khi bộ nhớ RAM máy tính có dung lượng trên 16GB.
> *Giải thích:* Ta không thể tạo mảng kích thước $10^{12}$, nhưng có thể sàng trên mảng kích thước $R - L + 1 \le 10^6$ bằng cách chỉ dùng các số nguyên tố $\le \sqrt{R} \le 10^6$.

---

#### Câu 12 (Số nguyên tố cùng nhau):
Hai số nguyên dương $A$ và $B$ được gọi là nguyên tố cùng nhau (Coprime) khi và chỉ khi:
* A. Cả $A$ và $B$ đều là số nguyên tố.
* B. $A + B$ là số nguyên tố.
* C. **(Đáp án đúng)** $\gcd(A, B) = 1$.
* D. $\text{lcm}(A, B) = A \times B + 1$.
> *Giải thích:* Hai số nguyên tố cùng nhau là hai số không có ước chung nào khác ngoài $1$, tức $\gcd(A, B) = 1$.

---

## 7. Ma Trận Bài Tập Thực Hành (Practice Problems $P0 \to P5$)

| STT | Mã Bài | Tên Bài Toán | Cấp Độ | Dạng Thuật Toán & Kỹ Năng Cốt Lõi |
|:---:|:---:|---|:---:|---|
| 01 | `CPPB-NT-01` | **Ước Chung Lớn Nhất & Bội Chung Nhỏ Nhất** | `P0` | Thuật toán Euclid tối ưu và chia trước nhân sau |
| 02 | `CPPB-NT-02` | **Kiểm Tra Số Nguyên Tố Cơ Bản** | `P0` | Kiểm tra nguyên tố trong $\mathcal{O}(\sqrt{N})$ bước nhảy 6k $\pm$ 1 |
| 03 | `CPPB-NT-03` | **Phân Tích Thừa Số Nguyên Tố** | `P1` | Phân tích $N = \prod p_i^{a_i}$ trong $\mathcal{O}(\sqrt{N})$ |
| 04 | `CPPB-NT-04` | **Đếm Số Lượng & Tính Tổng Các Ước** | `P1` | Ứng dụng công thức nhân tính $\sigma_0(N)$ và $\sigma_1(N)$ |
| 05 | `CPPB-NT-05` | **Số Chính Phương & Số Lập Phương** | `P1` | Kiểm tra số có số lượng ước lẻ bằng căn bậc hai nguyên |
| 06 | `CPPB-NT-06` | **Sàng Nguyên Tố Eratosthenes Kinh Điển** | `P2` | Cài đặt sàng nguyên tố với mảng `vector<bool>` $N \le 10^7$ |
| 07 | `CPPB-NT-07` | **Đếm Số Nguyên Tố Trong Đoạn [L, R]** | `P2` | Sàng Eratosthenes kết hợp Mảng Tiền Tố $\mathcal{O}(1)$ mỗi truy vấn |
| 08 | `CPPB-NT-08` | **Sàng Ước Nguyên Tố Nhỏ Nhất (SPF)** | `P2` | Phân tích thừa số nguyên tố $\mathcal{O}(\log N)$ cho $10^5$ truy vấn |
| 09 | `CPPB-NT-09` | **Sàng Phân Đoạn (Segmented Sieve)** | `P3` | Sàng trên khoảng $[L, R]$ với $R \le 10^{12}, R - L \le 10^6$ |
| 10 | `CPPB-NT-10` | **Cặp Số Nguyên Tố Sinh Đôi (Twin Primes)** | `P3` | Tìm cặp $(p, p+2)$ bằng Sàng Eratosthenes |
| 11 | `CPPB-NT-11` | **Số Hoàn Hảo & Định Lý Euclid-Euler** | `P3` | Kiểm tra số hoàn hảo dạng $2^{p-1}(2^p - 1)$ |
| 12 | `CPPB-NT-12` | **Số Có Đúng 3 Ước Số** | `P3` | Nhận diện số có dạng $p^2$ với $p$ là số nguyên tố |
| 13 | `CPPB-NT-13` | **Số Gần Nguyên Tố (Almost Prime)** | `P4` | Sàng đếm số lượng ước nguyên tố phân biệt của mọi số $\le N$ |
| 14 | `CPPB-NT-14` | **Phân Tích Giai Thừa Ra Thừa Số (Legendre)** | `P4` | Công thức Legendre $E_p(N!) = \sum \lfloor \frac{N}{p^k} \rfloor$ |
| 15 | `CPPB-NT-15` | **Đếm Số Số Không Tận Cùng Của N!** | `P4` | Đếm số mũ của 5 trong phân tích $N!$ |
| 16 | `CPPB-NT-16` | **Số Học Cực Hạn: Cặp Nguyên Tố Cùng Nhau Cực Đại** | `P5` | Ứng dụng Hàm Phi Euler $\phi(N)$ và sàng nguyên tố đa năng |
