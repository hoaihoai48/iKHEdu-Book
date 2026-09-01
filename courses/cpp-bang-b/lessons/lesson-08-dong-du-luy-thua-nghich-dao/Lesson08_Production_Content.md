# Chuyên đề 08: Đồng dư thức, lũy thừa nhị phân & nghịch đảo modulo

## 1. Bản chất vấn đề & trực giác thuật toán (the core problem & intuition)

Trong nhiều bài toán lập trình và thi đấu thuật toán, kết quả tính toán hoặc số cách đếm tổ hợp thường tăng rất nhanh và vượt quá giới hạn lưu trữ của kiểu số nguyên 64-bit (`long long`). Để tránh việc phải xử lý số lớn phức tạp, đề bài thường yêu cầu: **"In ra kết quả sau khi chia lấy dư cho $M$"** (thông thường $M = 10^9 + 7$ hoặc $998244353$ — là các số nguyên tố lớn).

Từ yêu cầu thực tế này, bộ ba kỹ thuật nền tảng được hình thành:
$\text{Đồng Dư Cơ Bản (+, -, *)} \longrightarrow \text{Lũy Thừa Nhị Phân } \mathcal{O}(\log B) \longrightarrow \text{Nghịch Đảo Modulo } (B^{-1})$

### Vấn đề 1: Phép tính lũy thừa $A^B \pmod M$
* **Cách ngây thơ:** Nhân $B$ lần liên tiếp: $A \times A \times \cdots \times A \implies \mathcal{O}(B)$. Khi $B = 10^{18}$, cách này hoàn toàn bất khả thi.
* **Trực giác Chia để trị (Binary Exponentiation):**
* Nếu $B$ chẵn: $A^B = (A^2)^{B / 2} = (A^{B / 2})^2$.
* Nếu $B$ lẻ: $A^B = A \times A^{B - 1}$.
* Sau mỗi bước, số mũ $B$ giảm đi một nửa $\implies$ Số phép nhân chỉ còn $\mathcal{O}(\log_2 B)$ (chưa tới $60$ phép tính với $B = 10^{18}$).

### Vấn đề 2: Phép chia trên vành modulo $\left(\frac{A}{B} \pmod M\right)$
* Trong số học đồng dư, **không thể thực hiện phép chia bằng phép chia số nguyên thông thường** (tức $\frac{A}{B} \pmod M \not\equiv \frac{A \pmod M}{B \pmod M}$).
* **Nghịch đảo Modulo ($B^{-1}$):** Muốn tính $\frac{A}{B} \pmod M$, ta chuyển phép chia thành phép nhân với nghịch đảo modulo $B^{-1}$ (nếu nghịch đảo tồn tại):
$$\frac{A}{B} \pmod M \equiv (A \times B^{-1}) \pmod M$$
với $B^{-1}$ là số nguyên thỏa mãn: $(B \times B^{-1}) \equiv 1 \pmod M$.

## 2. Mô phỏng từng bước (visual step-by-step simulation)

### Ví dụ 1: Mô phỏng tính $3^{13} \pmod{1000}$ bằng lũy thừa nhị phân

Biểu diễn nhị phân của số mũ $13 = 1101_2 = 8 + 4 + 1$.
Do đó: $3^{13} = 3^8 \times 3^4 \times 3^1$.

| Bước lặp | Số mũ $B$ | Trạng thái ($B$ chẵn hay lẻ) | Cơ số $A$ ($A \gets A^2 \pmod M$) | Kết quả tích lũy $ans$ ($ans \gets ans \times A \pmod M$) |
|:---:|:---:|:---:|:---:|:---:|
| **Khởi tạo** | $13$ | Lẻ (bit $0 = 1$) | $A = 3$ | $ans = 1 \times 3 = 3$ |
| **1** | $6$ | Chẵn (bit $1 = 0$) | $A \gets 3^2 = 9$ | $ans = 3$ (không nhân) |
| **2** | $3$ | Lẻ (bit $2 = 1$) | $A \gets 9^2 = 81$ | $ans \gets (3 \times 81) = 243$ |
| **3** | $1$ | Lẻ (bit $3 = 1$) | $A \gets 81^2 = 6561 \equiv 561$ | $ans \gets (243 \times 561) \pmod{1000} = \mathbf{323}$ |
| **Kết thúc** | $0$ | Dừng | — | **Đáp án:** $3^{13} \pmod{1000} = \mathbf{323}$ (vì $3^{13} = 1594323$) |

### Ví dụ 2: Mô phỏng tìm nghịch đảo modulo của $3 \pmod 7$
Ta cần tìm số nguyên $X \in \{1, \dots, 6\}$ sao cho $(3 \times X) \pmod 7 = 1$.

| Thử giá trị $X$ | Phép nhân $3 \times X$ | Lấy dư $(3 \times X) \pmod 7$ | Kết luận |
|:---:|:---:|:---:|:---:|
| $X = 1$ | $3 \times 1 = 3$ | $3$ | Không thỏa mãn |
| $X = 2$ | $3 \times 2 = 6$ | $6$ | Không thỏa mãn |
| $X = 3$ | $3 \times 3 = 9$ | $2$ | Không thỏa mãn |
| $X = 4$ | $3 \times 4 = 12$ | $5$ | Không thỏa mãn |
| **$X = 5$** | $3 \times 5 = 15$ | **$1$** | **$3^{-1} \equiv 5 \pmod 7$ (Thỏa mãn)** |

> **Kiểm chứng bằng Định lý Fermat nhỏ:** $3^{7-2} = 3^5 = 243 \equiv 5 \pmod 7$.

## 3. Lý thuyết cốt lõi & bất biến toán học (core invariants)

### 3.1. Các quy tắc đồng dư cơ bản (+, -, \*)
1. **Phép Cộng:** $(A + B) \pmod M = ((A \pmod M) + (B \pmod M)) \pmod M$.
2. **Phép Trừ (Tránh số âm):** $(A - B) \pmod M = ((A \pmod M) - (B \pmod M) + M) \pmod M$.
3. **Phép Nhân:** $(A \times B) \pmod M = ((A \pmod M) \times (B \pmod M)) \pmod M$.

### Cảnh báo quan trọng:
**2 Bẫy Lỗi KHI THỰC HIỆN PHÉP TOÁN ĐỒNG DƯ:**

> 1. **Số dư âm trong C++:** Trong C++, phép toán `-7 % 5` trả về `-2` (không phải `3`). Để luôn nhận kết quả không âm, bắt buộc phải viết: `(a % m + m) % m`.
> 2. **Tràn số 32-bit khi nhân:** Nếu $A, B \approx 10^9$, tích $A \times B \approx 10^{18}$ vượt giới hạn kiểu `int`. Bắt buộc phải ép kiểu 64-bit trước khi nhân: `(1LL * a * b) % m`.

### 3.2. Định lý Fermat nhỏ & nghịch đảo modulo
Nếu $M$ là một **số nguyên tố** và $A$ không chia hết cho $M$ ($\gcd(A, M) = 1$), thì:
$$A^{M - 1} \equiv 1 \pmod M \implies A \times A^{M - 2} \equiv 1 \pmod M$$

$$\implies \mathbf{A^{-1} \equiv A^{M - 2} \pmod M}$$

Ta có thể tính $A^{-1} \pmod M$ chỉ bằng một hàm Lũy thừa nhị phân: `power(A, M - 2, M)` trong $\mathcal{O}(\log M)$.

### Chú ý:
**ĐIỀU KIỆN TIÊN QUYẾT CỦA ĐỊNH LÝ FERMAT NHỎ:**

> * Quy tắc $A^{M - 1} \equiv 1 \pmod M$ và việc rút gọn số mũ $B \gets B \pmod{(M - 1)}$ **CHỈ ĐÚNG KHI $M$ LÀ SỐ NGUYÊN TỐ VÀ $\gcd(A, M) = 1$**.
> * Tuyệt đối không tùy tiện áp dụng nếu $A$ chia hết cho $M$ hoặc $M$ là hợp số.

### 3.3. Thuật toán euclid mở rộng (extended euclidean algorithm)
Khi $M$ **không phải là số nguyên tố** (nhưng $\gcd(A, M) = 1$), định lý Fermat nhỏ không áp dụng được. Ta dùng thuật toán Euclid mở rộng để giải phương trình nghiệm nguyên:
$$A \times x + M \times y = \gcd(A, M) = 1$$
Khi đó, $x \pmod M$ chính là nghịch đảo modulo $A^{-1}$.

### 3.4. Tính tổ hợp $C(N, K) \pmod M$ trong $\mathcal{O}(1)$ mỗi truy vấn
Công thức số tổ hợp chập $K$ của $N$:
$$C(N, K) = \frac{N!}{K! \times (N - K)!} \equiv N! \times (K!)^{-1} \times ((N - K)!)^{-1} \pmod M$$

* **Tiền xử lý trong $\mathcal{O}(N)$:**
1. Tính mảng giai thừa: `fact[i] = (fact[i-1] * i) % M`.
2. Tính mảng nghịch đảo giai thừa: `invFact[N] = power(fact[N], M - 2, M)`, sau đó đi ngược về 0: `invFact[i - 1] = (invFact[i] * i) % M`.
* **Trả lời mỗi truy vấn trong $\mathcal{O}(1)$:**
$$C(N, K) = \text{fact}[N] \times \text{invFact}[K] \pmod M \times \text{invFact}[N - K] \pmod M$$

### 3.5. Tính tổng cấp số nhân modulo bằng chia để trị
Cần tính tổng:
$$S_N = 1 + A + A^2 + \cdots + A^N \pmod M$$
* **Trường hợp cơ sở:** Nếu $N = 0 \implies S_0 = 1$.
* **Nếu $N$ lẻ (Tổng có $N + 1$ số hạng chẵn):**
$$S_N = (1 + A + \cdots + A^{(N-1)/2}) + A^{(N+1)/2} (1 + A + \cdots + A^{(N-1)/2})$$
$$S_N = S_{(N-1)/2} \times \left(1 + A^{(N+1)/2}\right) \pmod M$$
* **Nếu $N$ chẵn:** Tách riêng số hạng cuối cùng:
$$S_N = 1 + A \times S_{N-1} \pmod M$$
* **Độ phức tạp:** $\mathcal{O}(\log^2 N)$ hoặc $\mathcal{O}(\log N)$, mở đường cho kỹ thuật nhân lũy thừa ma trận và quy hoạch động cấu trúc đại số.

## 4. Các bẫy lỗi lập trình kinh điển (bug traps)

1. **Chia trực tiếp trên Modulo:**
* Viết `((A % M) / (B % M)) % M` là **HOÀN TOÀN SAI BẢN CHẤT TOÁN HỌC**. Phép chia bắt buộc phải chuyển thành nhân với nghịch đảo: `(A * inverse(B)) % M`.
2. **Quên xử lý trường hợp $K > N$ hoặc $K < 0$ khi tính tổ hợp:**

* $C(N, K) = 0$ khi $K < 0$ hoặc $K > N$. Nếu không kiểm tra sẽ bị truy cập ô nhớ âm hoặc rác.

3. **Trường hợp $M = 1$:**
* $A^B \pmod 1$ luôn bằng $0$. Hàm lũy thừa cần trả về `0` khi $M = 1$.

## 5. Mẫu cài đặt chuẩn thi đấu (competitive templates)

### Mẫu 1: Lũy thừa nhị phân & nghịch đảo modulo chuẩn
```cpp
#include <bits/stdc++.h>
using namespace std;

// Tính (a^b) % m trong O(log b)
long long powerMod(long long a, long long b, long long m) {
    if (m == 1) return 0;
    long long ans = 1 % m;
    a %= m;
    while (b > 0) {

        if (b & 1) ans = (ans * a) % m;
        a = (a * a) % m;
        b >>= 1;
    }
    return ans;
}

// Nghịch đảo Modulo bằng Định lý Fermat nhỏ (khi m là số nguyên tố)
long long modInversePrime(long long a, long long m) {
    return powerMod(a, m - 2, m);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long a, b, m;
    if (!(cin >> a >> b >> m)) return 0;

    cout << powerMod(a, b, m) << "\n";
    return 0;
}
```

### Mẫu 2: Tiền xử lý tổ hợp $C(N, K) \pmod M$ trong $\mathcal{O}(1)$ mỗi truy vấn
```cpp
#include <bits/stdc++.h>
using namespace std;

const int MAXN = 1000000;
const long long MOD = 1000000007;

vector<long long> fact(MAXN + 1);

vector<long long> invFact(MAXN + 1);

long long powerMod(long long a, long long b, long long m) {
    long long ans = 1;
    a %= m;
    while (b > 0) {

        if (b & 1) ans = (ans * a) % m;
        a = (a * a) % m;
        b >>= 1;
    }
    return ans;
}

void precomputeCombinatorics() {
    fact[0] = 1;
    for (int i = 1; i <= MAXN; ++i) {
        fact[i] = (fact[i - 1] * i) % MOD;
    }
    invFact[MAXN] = powerMod(fact[MAXN], MOD - 2, MOD);
    for (int i = MAXN; i >= 1; --i) {
        invFact[i - 1] = (invFact[i] * i) % MOD;
    }
}

long long nCr(int n, int r) {
    if (r < 0 || r > n) return 0;

    return fact[n] * invFact[r] % MOD * invFact[n - r] % MOD;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    precomputeCombinatorics();

    int q;
    if (!(cin >> q)) return 0;

    while (q--) {
        int n, r;
        cin >> n >> r;

        cout << nCr(n, r) << "\n";
    }
    return 0;
}
```

## Câu hỏi trắc nghiệm củng cố khái niệm

#### Câu 1 (Độ phức tạp):

Thuật toán Lũy thừa nhị phân (Binary Exponentiation) tính $A^B \bmod M$ có độ phức tạp thời gian là:

- **A.** $\mathcal{O}(B)$

- **B.** $\mathcal{O}(\sqrt{B})$

- **C.** **[Đáp án đúng]** $\mathcal{O}(\log_2 B)$

- **D.** $\mathcal{O}(1)$

> *Giải thích:* Sau mỗi vòng lặp, số mũ $B$ giảm đi một nửa ($B \gets \lfloor B / 2 \rfloor$). Do đó số lần lặp tối đa là $\lfloor \log_2 B \rfloor + 1$.

#### Câu 2 (Xử lý số âm):

Trong C++, biểu thức $(-8) \bmod 5$ trả về kết quả là $-3$. Cách viết chuẩn mực nào để luôn nhận được số dư không âm trong khoảng $[0, M - 1]$?

- **A.** $abs((-8) % 5)$

- **B.** **[Đáp án đúng]** $((-8) % 5 + 5) % 5$

- **C.** $(-8) % 5 + 5$

- **D.** $5 - ((-8) % 5)$

> *Giải thích:* Cộng thêm $M$ rồi lấy dư lại lần nữa đảm bảo nếu số dư ban đầu là âm (thuộc $(-M, 0)$), nó sẽ được đưa về miền dương $[0, M - 1]$, còn nếu ban đầu đã dương thì không đổi.

#### Câu 3 (Định lý Fermat nhỏ):

Định lý Fermat nhỏ phát biểu rằng: Nếu $M$ là số nguyên tố và $\gcd(A, M) = 1$, thì $A^{M-1} \equiv 1 \pmod M$. Từ đó suy ra nghịch đảo modulo $A^{-1} \pmod M$ bằng biểu thức nào?

- **A.** $A^M \bmod M$

- **B.** $A^{M+1} \bmod M$

- **C.** **[Đáp án đúng]** $A^{M-2} \bmod M$

- **D.** $A^{M-1} - 1 \bmod M$

> *Giải thích:* Nhân cả 2 vế của $A^{M-1} \equiv 1 \pmod M$ với $A^{-1}$, ta được $A^{-1} \equiv A^{M-2} \pmod M$.

#### Câu 4 (Phép chia Modulo):

Khi cần tính giá trị biểu thức $\frac{A}{B} \pmod M$ với $M = 10^9 + 7$ (số nguyên tố) và $B \not\equiv 0 \pmod M$, ta thực hiện phép toán nào sau đây?

- **A.** $(A / B) % M$

- **B.** $(A % M) / (B % M)$

- **C.** **[Đáp án đúng]** $(A % M) * powerMod(B, M - 2, M) % M$

- **D.** $(A % M) * powerMod(B, M - 1, M) % M$

> *Giải thích:* Phép chia trên vành modulo bắt buộc phải nhân với nghịch đảo của mẫu số: $A \cdot B^{-1} \pmod M$.

#### Câu 5 (Điều kiện tồn tại Nghịch đảo):

Nghịch đảo modulo của số nguyên $A$ theo modulo $M$ (tức số $X$ sao cho $A \cdot X \equiv 1 \pmod M$) **chắc chắn tồn tại** khi và chỉ khi:

- **A.** $A$ và $M$ đều là số lẻ.

- **B.** `A < M`.

- **C.** **[Đáp án đúng]** `gcd(A, M) = 1` ($A$ và $M$ nguyên tố cùng nhau).

- **D.** $M$ phải là số chẵn.

> *Giải thích:* Theo định lý Bézout, phương trình $Ax + My = 1$ chỉ có nghiệm nguyên khi và chỉ khi `gcd(A, M) = 1`.

#### Câu 6 (Tổ hợp Modulo $\mathcal{O}(1)$):

Để trả lời $10^5$ truy vấn tính số tổ hợp $\binom{N}{K} \pmod{10^9 + 7}$ với $N, K \le 10^6$ trong tổng thời gian dưới `0.1s`, phương pháp tối ưu nhất là gì?

- **A.** Tính trực tiếp $C(N, K)$ bằng tam giác Pascal tại mỗi truy vấn.

- **B.** Tính $N!$, $K!$, $(N-K)!$ từ đầu tại mỗi truy vấn.

- **C.** **[Đáp án đúng]** Tiền xử lý mảng Giai thừa `fact[]` và Nghịch đảo giai thừa `invFact[]` trong $\mathcal{O}(N)$, sau đó trả lời mỗi truy vấn trong $\mathcal{O}(1)$.

- **D.** Dùng đệ quy quay lui có nhớ.

> Giải thích: Tiền xử lý $\mathcal{O}(N)$ cho phép tính $C(N, K) = \text{fact}[N] \cdot \text{invFact}[K] \cdot \text{invFact}[N-K] \pmod M$ trong đúng $\mathcal{O}(1)$ phép nhân.

#### Câu 7 (Tối ưu tính Nghịch đảo giai thừa):

Thay vì gọi hàm lũy thừa $N$ lần để tính `invFact[i]`, ta có thể tính toàn bộ mảng $invFact$ từ $1 \dots N$ chỉ với **1 lần gọi hàm lũy thừa duy nhất** bằng công thức quy nạp lùi nào?

- **A.** $invFact[i - 1] = invFact[i] / i$

- **B.** **[Đáp án đúng]** $invFact[i - 1] = (invFact[i] * i) % MOD$

- **C.** $invFact[i - 1] = (invFact[i] * (MOD - i)) % MOD$

- **D.** $invFact[i] = invFact[i - 1] * (i + 1)$

> *Giải thích:* Vì $\frac{1}{(i-1)!} = \frac{1}{i!} \cdot i$, do đó $invFact[i - 1] = (invFact[i] * i) % MOD$. Ta chỉ cần tính $invFact[N] = power(fact[N], MOD - 2)$ rồi đi lùi về $0$.

#### Câu 8 (Rút gọn số mũ lớn):

Theo định lý Fermat nhỏ, với $M = 10^9 + 7$ (số nguyên tố) và `gcd(A, M) = 1`, nếu số mũ $B$ là một số khổng lồ gồm hàng chục nghìn chữ số, ta có thể rút gọn số mũ $B$ trước khi tính lũy thừa bằng cách nào?

- **A.** $B \gets B \bmod M$

- **B.** **[Đáp án đúng]** $B \gets B \bmod (M - 1)$

- **C.** $B \gets B \bmod (M + 1)$

- **D.** $B \gets B \bmod \sqrt{M}$

> *Giải thích:* Vì $M$ là số nguyên tố và `gcd(A, M) = 1`, theo Fermat nhỏ $A^{M-1} \equiv 1 \pmod M$. Do đó $A^B = A^{q(M-1)+r} = (A^{M-1})^q \cdot A^r \equiv 1^q \cdot A^r \equiv A^r \pmod M$ với $r = B \bmod (M - 1)$.

#### Câu 9 (Nhân an toàn chống tràn số 64-bit):

Khi nào phép nhân trực tiếp $(a * b) % m$ có nguy cơ gây tràn số và bắt buộc phải áp dụng kỹ thuật nhân modulo an toàn (như Nhân Ấn Độ $\mathcal{O}(\log B)$ hoặc kiểu dữ liệu `__int128`)?

- **A.** Khi $A, B \le 10^9$ và $M = 10^9 + 7$.

- **B.** **[Đáp án đúng]** Khi $A, B \le 10^{18}$ và $M \le 10^{18}$ (tích $A \times B$ có thể lên tới $10^{36}$, vượt quá giới hạn 64-bit của `unsigned long long`).

- **C.** Khi $M$ là số chẵn.

- **D.** Khi $B$ là số âm.

> *Giải thích:* Khi $A, B \approx 10^{18}$, tích $A \times B \approx 10^{36}$ vượt xa ngưỡng $2^{64}-1 \approx 1.8 \times 10^{19}$. Ta cần phân rã phép nhân thành các phép cộng có lấy dư (Nhân Ấn Độ) hoặc dùng kiểu số nguyên 128-bit.

#### Câu 10 (Phương trình Diophantine & Euclid mở rộng):

Thuật toán Euclid mở rộng tìm cặp nghiệm nguyên `(x, y)` cho phương trình $Ax + My = \gcd(A, M)$. Nếu `gcd(A, M) = 1`, giá trị $x \bmod M$ đại diện cho đại lượng nào?

- **A.** Ước chung lớn nhất của $A$ và $M$.

- **B.** Phần dư của $A$ chia cho $M$.

- **C.** **[Đáp án đúng]** Nghịch đảo modulo của $A$ theo modulo $M$ ($A^{-1} \pmod M$).

- **D.** Bội chung nhỏ nhất của $A$ và $M$.

> *Giải thích:* Phương trình $Ax + My = 1 \iff Ax \equiv 1 \pmod M$, nghĩa là $x$ chính là nghịch đảo modulo của $A$.

## Ma trận bài tập thực hành (P0 → P5)

### Ghi chú:
**Phân tầng lộ trình học tập:**

> * **Nhóm Cốt Lõi (Core Foundations - Bắt buộc `CPPB-MOD-01` $\to$ `09`):** Nắm vững các phép toán đồng dư, lũy thừa nhị phân, nghịch đảo Fermat/Euclid và tổ hợp $C(N, K)$.
> * **Nhóm Thử Thách Mở Rộng (Advanced / Challenge `CPPB-MOD-10` $\to$ `16`):** Dành cho học sinh giỏi nâng cao tiếp cận các mô hình toán học chuyên sâu.

| STT | Mã Bài | Tên Bài Toán | Cấp Độ | Phân Loại | Dạng Thuật Toán & Kỹ Năng Cốt Lõi |
|:---:|:---:|---|:---:|:---:|---|
| 01 | `CPPB-MOD-01` | **Phép Tính Đồng Dư Cơ Bản (+, -, \*)** | `P0` | **Core** | Quy tắc cộng trừ nhân đồng dư và xử lý số dư âm |
| 02 | `CPPB-MOD-02` | **Lũy Thừa Nhị Phân Cơ Bản ($A^B \pmod M$)** | `P0` | **Core** | Thuật toán Lũy thừa nhị phân lặp $\mathcal{O}(\log B)$ |
| 03 | `CPPB-MOD-03` | **Lũy Thừa Chuỗi Số Lớn ($A^B \pmod M$)** | `P1` | **Core** | Định lý Fermat nhỏ và rút gọn số mũ $B \pmod{M - 1}$ |
| 04 | `CPPB-MOD-04` | **Nhân Ấn Độ Chống Tràn Số ($A \times B \pmod M$)** | `P1` | **Core** | Nhân nhân đôi nhị phân $\mathcal{O}(\log B)$ hoặc `__int128` |
| 05 | `CPPB-MOD-05` | **Tính Tổng Cấp Số Nhân Đồng Dư** | `P2` | **Core** | Chia để trị tính $S = 1 + A + \cdots + A^N \pmod M$ |
| 06 | `CPPB-MOD-06` | **Nghịch Đảo Modulo Bằng Fermat Nhỏ** | `P2` | **Core** | Tính $A^{-1} \equiv A^{M-2} \pmod M$ với $M$ nguyên tố |
| 07 | `CPPB-MOD-07` | **Nghịch Đảo Modulo Bằng Euclid Mở Rộng** | `P2` | **Core** | Giải phương trình $Ax + My = 1$ khi $\gcd(A, M) = 1$ |
| 08 | `CPPB-MOD-08` | **Phép Chia Đồng Dư $\frac{A}{B} \pmod M$** | `P2` | **Core** | Thực hiện phép nhân với nghịch đảo modulo $A \times B^{-1}$ |
| 09 | `CPPB-MOD-09` | **Tính Số Tổ Hợp $C(N, K) \pmod M$** | `P3` | **Core** | Tiền xử lý Giai thừa và Nghịch đảo trong $\mathcal{O}(N)$ |
| 10 | `CPPB-MOD-10` | **Tính Số Chỉnh Hợp $A(N, K) \pmod M$** | `P3` | *Advanced* | Tính $A(N, K) = N! \times ((N-K)!)^{-1} \pmod M$ |
| 11 | `CPPB-MOD-11` | **Dãy Fibonacci Đồng Dư Lớn** | `P3` | *Advanced* | Nhân ma trận nhị phân $\mathcal{O}(\log N)$ tính $F_N \pmod M$ |
| 12 | `CPPB-MOD-12` | **Số Catalan Đồng Dư $C_N \pmod M$** | `P3` | *Advanced* | Công thức $C_N = \frac{1}{N+1} C(2N, N) \pmod M$ |
| 13 | `CPPB-MOD-13` | **Lũy Thừa Tầng (Tower of Powers)** | `P4` | *Advanced* | Tính $A^{B^C} \pmod M$ bằng định lý Euler / Fermat nhỏ |
| 14 | `CPPB-MOD-14` | **Nghịch Đảo Tuyến Tính $1 \dots N$ Trong $\mathcal{O}(N)$** | `P4` | *Advanced* | Công thức hồi quy tính nghịch đảo toàn bộ mảng |
| 15 | `CPPB-MOD-15` | **Giải Phương Trình Đồng Dư Tuyến Tính $Ax \equiv B \pmod M$** | `P4` | *Advanced* | Thuật toán Euclid mở rộng tổng quát |
| 16 | `CPPB-MOD-16` | **Đồng Dư Cực Hạn: Căn Bậc Hai Modulo (Tonelli-Shanks)** | `P5` | *Advanced* | Giải phương trình $x^2 \equiv A \pmod P$ |

