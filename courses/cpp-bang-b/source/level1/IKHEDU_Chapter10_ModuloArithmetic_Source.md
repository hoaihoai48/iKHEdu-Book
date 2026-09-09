# TÀI LIỆU GỐC — CHƯƠNG 10: SỐ HỌC MODULO (MODULO ARITHMETIC)

## Bản đồ chương

| Trường | Nội dung |
|---|---|
| Mục tiêu | Nắm vững các tính chất số học đồng dư (Modulo), các phép toán cộng, trừ, nhân, chia (nghịch đảo modulo) theo modulo nguyên tố $10^9+7$; tính chu kỳ Pisano Period và xử lý số học không bao giờ bị tràn số |
| Kiến thức cần có | Lũy thừa nhị phân, thuật toán Euclid, kiểu `long long` |
| Phạm vi | 4 phép tính Modulo, Lũy thừa nhanh Modulo, Nghịch đảo Modulo (Định lý Fermat nhỏ), Chu kỳ Pisano Period |
| Số bài | 4 bài học lý thuyết & ví dụ mẫu + 1 bài luyện tập phân tầng |
| Tổng bài tập | 12 bài tập tự chứa (Tầng A: 4 bài, Tầng B: 4 bài, Tầng C: 4 bài) |

### Learning outcomes

Sau chương này, em có thể:
1. Áp dụng chính xác các công thức đồng dư cho phép cộng, trừ, nhân Modulo không bao giờ bị tràn số hay số âm.
2. Cài đặt lũy thừa Modulo $A^B \pmod M$ trong $\mathcal{O}(\log B)$.
3. Tìm nghịch đảo Modulo $A^{-1} \pmod P$ bằng Định lý Fermat nhỏ và thực hiện phép chia Modulo $(A / B) \pmod P$.
4. Nhận diện và áp dụng chu kỳ số dư Pisano Period để tính các số Fibonacci rất lớn.

### Câu hỏi trung tâm của chương

> **Làm thế nào để thực hiện phép chia $\frac{A}{B}$ lấy dư cho $M$ khi phép chia thông thường không có tính chất phân phối với phép chia dư**

---

### Bài 10.1 — Các phép toán cơ bản trên Modulo

#### 1. Khái niệm & Công thức 4 phép tính
- **Phép cộng:** $(A + B) \pmod M = ((A \pmod M) + (B \pmod M)) \pmod M$.
- **Phép trừ (Chống số âm):** $(A - B) \pmod M = ((A \pmod M) - (B \pmod M) + M) \pmod M$.
- **Phép nhân (Chống tràn số 32-bit):** $(A \times B) \pmod M = (1LL \times (A \pmod M) \times (B \pmod M)) \pmod M$.

---

#### 2. Bài toán mẫu có hướng dẫn

> **Bài toán mẫu 10.1: Dự Báo Chỉ Số Tăng Trưởng Kinh Tế Số** 
> **Bối cảnh:** Viện Chiến lược Thông tin và Truyền thông xây dựng mô hình dự báo tăng trưởng giá trị kinh tế số theo đa thức bậc $N$: 
> $$P(X) = A_N X^N + A_{N-1} X^{N-1} + \dots + A_1 X + A_0$$ 
> Do giá trị tính toán có thể vượt qua hàng nghìn chữ số, kết quả cuối cùng cần được lấy dư cho hằng số Modulo chuẩn thi đấu $M = 10^9 + 7$. 
> **Nhiệm vụ:** Em hãy tính giá trị của đa thức $P(X) \pmod{10^9+7}$ theo sơ đồ Horner tối ưu trong $\mathcal{O}(N)$. 
> 
> **Input:** 
> - Dòng 1: Hai số nguyên $N$ và $X$ ($1 \le N \le 10^5, 0 \le X \le 10^9$). 
> - Dòng 2: $N + 1$ số nguyên $A_N, A_{N-1}, \dots, A_0$ ($0 \le A_i \le 10^9$). 
> 
> **Output:** 
> - Ghi một số nguyên duy nhất là $P(X) \pmod{10^9+7}$. 
> 
> **Sample:** 
> - **Input:** 
> `2 3` 
> `1 2 1` 
> - **Output:** `16` 
> - **Giải thích:** $P(3) = 1 \times 3^2 + 2 \times 3 + 1 = 9 + 6 + 1 = 16 \pmod{10^9+7}$.

#### Cài đặt C++
```cpp
#include <bits/stdc++.h>
using namespace std;

const long long MOD = 1000000007;

int main() {
ios::sync_with_stdio(false);
cin.tie(nullptr);

int n;
long long x;
if (!(cin >> n >> x)) return 0;

vector<long long> a(n + 1);
for (int i = n; i >= 0; i--) cin >> a[i];

long long ans = 0;
for (int i = n; i >= 0; i--) {
ans = (ans * (x % MOD) + a[i]) % MOD;
}

cout << (ans % MOD + MOD) % MOD << "\n";
return 0;
}
```

---

#### 3. Bẫy lỗi thường gặp
| Lỗi | Hậu quả | Cách tự kiểm tra |
|---|---|---|
| Phép trừ ra kết quả âm trong C++ (ví dụ `-3 % 5` ra `-3`) | Kết quả in ra số âm làm sai Test | Luôn viết `(a - b + MOD) % MOD` |
| Quên dùng `long long` khi nhân 2 số Modulo | Tích $10^9 \times 10^9 = 10^{18}$ bị tràn số 32-bit `int` | Luôn ép kiểu `(1LL * a * b) % MOD` |

---

#### 4. Bài tập thực hành Bài 10.1

##### Bài 10.1.1 — Tổng Doanh Thu Chuỗi Cửa Hàng Thế Giới Di Động
- **Bối cảnh:** Hệ thống ghi nhận doanh thu của $N$ chi nhánh. Tính tổng doanh thu toàn hệ thống lấy dư cho $10^9+7$.
- **Input:** Dòng 1 ghi $N \le 10^5$. Dòng 2 ghi $N$ số nguyên $A_i \le 10^9$.
- **Output:** Ghi tổng doanh thu modulo $10^9+7$.
- **Sample:** `3` \ `1000000000 1000000000 1000000000` $\implies$ **Output:** `999999979`

##### Bài 10.1.2 — Lãi Suất Tích Lũy Ngân Hàng Sau N Kỳ Hạn
- **Bối cảnh:** Số tiền ban đầu $S$, mỗi kỳ hạn nhân lên $K$ lần. Tính số tiền sau $N$ kỳ hạn modulo $10^9+7$.
- **Input:** Ba số nguyên $S, K, N$ ($S, K \le 10^9, N \le 10^6$).
- **Output:** In số tiền nhận được modulo $10^9+7$.

---

### Bài 10.2 — Lũy thừa nhanh Modulo (Modular Exponentiation)

#### 1. Khái niệm & Thuật toán
- Tính $A^B \pmod M$ với $B \le 10^{18}$ trong $\mathcal{O}(\log B)$ bằng cách phân tích nhị phân số mũ $B$.

---

#### 2. Bài toán mẫu có hướng dẫn

> **Bài toán mẫu 10.2: Khóa Bảo Mật Cổng Dịch Vụ Công Quốc Gia** 
> **Bối cảnh:** Cổng Dịch vụ công Quốc gia sinh khóa mã hóa xác thực phiên làm việc bằng hàm lũy thừa $A^B \pmod{10^9+7}$ với số mũ $B$ lên tới $10^{18}$. 
> **Input:** `2 10` $\implies$ **Output:** `1024`.

#### Cài đặt C++
```cpp
#include <bits/stdc++.h>
using namespace std;

const long long MOD = 1000000007;

long long powerMod(long long a, long long b, long long m) {
long long res = 1;
a %= m;
while (b > 0) {
if (b & 1) res = (1LL * res * a) % m;
a = (1LL * a * a) % m;
b >>= 1;
}
return res;
}

int main() {
ios::sync_with_stdio(false);
cin.tie(nullptr);

long long a, b;
if (!(cin >> a >> b)) return 0;

cout << powerMod(a, b, MOD) << "\n";
return 0;
}
```

---

#### 3. Bài tập thực hành Bài 10.2

##### Bài 10.2.1 — Số Lượng Khóa Phân Phối Trong Hệ Thống IoT
- **Bối cảnh:** Một mạng lưới gồm $N$ nút cảm biến có khả năng tạo ra $2^N$ chuỗi tín hiệu phân biệt. Tính số chuỗi tín hiệu $2^N \pmod{10^9+7}$ với $N \le 10^{18}$.
- **Input:** Một số nguyên $N$ ($1 \le N \le 10^{18}$).
- **Output:** In kết quả $2^N \pmod{10^9+7}$.
- **Sample:** `10` $\implies$ **Output:** `1024`

##### Bài 10.2.2 — Tính Lũy Thừa Dãy Số Nhận Được
- **Bối cảnh:** Cho dãy gồm $N$ số $A_1, A_2, \dots, A_N$. Tính tích $(A_1^{B_1} \times A_2^{B_2} \times \dots \times A_N^{B_N}) \pmod{10^9+7}$.
- **Input:** Dòng 1 ghi $N \le 10^5$. $N$ dòng sau mỗi dòng ghi $A_i, B_i \le 10^9$.
- **Output:** In tích sau khi lấy modulo.

---

### Bài 10.3 — Phép chia Modulo và Nghịch đảo Modulo (Modular Inverse)

#### 1. Khái niệm & Định lý Fermat nhỏ
- Khi $P$ là số nguyên tố và $\gcd(B, P) = 1$:
$$B^{-1} \equiv B^{P-2} \pmod P \implies \frac{A}{B} \equiv A \times B^{P-2} \pmod P$$

---

#### 2. Bài toán mẫu có hướng dẫn

> **Bài toán mẫu 10.3: Tuyển Chọn Đội Tuyển Olympic Tin Học Quốc Tế** 
> **Bối cảnh:** Chọn $K$ học sinh từ $N$ học sinh xuất sắc vào đội tuyển Quốc gia. Tính số cách chọn $C_N^K \pmod{10^9+7}$. 
> **Input:** `5 2` $\implies$ **Output:** `10`.

#### Cài đặt C++
```cpp
#include <bits/stdc++.h>
using namespace std;

const long long MOD = 1000000007;

long long powerMod(long long a, long long b) {
long long res = 1;
a %= MOD;
while (b > 0) {
if (b & 1) res = (res * a) % MOD;
a = (a * a) % MOD;
b >>= 1;
}
return res;
}

long long modInverse(long long n) {
return powerMod(n, MOD - 2);
}

int main() {
ios::sync_with_stdio(false);
cin.tie(nullptr);

int n, k;
if (!(cin >> n >> k)) return 0;

vector<long long> fact(n + 1);
fact[0] = 1;
for (int i = 1; i <= n; i++) fact[i] = (fact[i - 1] * i) % MOD;

long long num = fact[n];
long long den = (fact[k] * fact[n - k]) % MOD;
long long ans = (num * modInverse(den)) % MOD;

cout << ans << "\n";
return 0;
}
```

---

#### 3. Bài tập thực hành Bài 10.3

##### Bài 10.3.1 — Rút Gọn Tỷ Lệ Giải Thưởng Phân Số
- **Bối cảnh:** Tính giá trị phân số $\frac{A}{B} \pmod{10^9+7}$ với $1 \le A, B \le 10^9$ và $\gcd(B, 10^9+7) = 1$.
- **Input:** Hai số nguyên $A$ và $B$.
- **Output:** In một số nguyên duy nhất là $(A \times B^{-1}) \pmod{10^9+7}$.
- **Sample:** `4 2` $\implies$ **Output:** `2`

##### Bài 10.3.2 — Đếm Số Cách Chia Nhóm Dự Án
- **Bối cảnh:** Tính số cách chia $N$ thành viên thành 2 nhóm gồm $K$ và $N-K$ người bằng công thức tổ hợp $C_N^K \pmod{10^9+7}$ với $N \le 10^6$.
- **Sample:** `6 3` $\implies$ **Output:** `20`

---

### Bài 10.4 — Chu kỳ số dư (Pisano Period)

#### 1. Khái niệm & Định lý
- Dãy Fibonacci lấy dư cho số nguyên dương $M$ luôn có chu kỳ tuần hoàn lặp lại gọi là chu kỳ Pisano $\pi(M)$.
- Với $M = 10^9+7$, chu kỳ Pisano là $\pi(10^9+7) = 2 \times 10^9 + 16$.
- Với $M$ nhỏ (ví dụ $M \le 1000$), ta có thể tìm chu kỳ Pisano bằng cách duyệt tìm cặp $(0, 1)$ lặp lại.

---

#### 2. Bài toán mẫu có hướng dẫn

> **Bài toán mẫu 10.4: Tìm Chu Kỳ Số Dư Của Dãy Fibonacci** 
> **Bối cảnh:** Tìm độ dài chu kỳ tuần hoàn số dư Pisano $\pi(M)$ của dãy Fibonacci khi lấy dư cho số nguyên dương $M \le 1000$. 
> **Input:** `3` $\implies$ **Output:** `8` (dãy số dư mod 3: 0, 1, 1, 2, 0, 2, 2, 1, rồi lặp lại 0, 1).

#### Cài đặt C++
```cpp
#include <bits/stdc++.h>
using namespace std;

int getPisanoPeriod(int m) {
int prev = 0, curr = 1;
for (int i = 0; i < m * m; i++) {
int temp = (prev + curr) % m;
prev = curr;
curr = temp;
if (prev == 0 && curr == 1) return i + 1;
}
return 0;
}

int main() {
ios::sync_with_stdio(false);
cin.tie(nullptr);

int m;
if (!(cin >> m)) return 0;

cout << getPisanoPeriod(m) << "\n";
return 0;
}
```

---

#### 3. Bài tập thực hành Bài 10.4

##### Bài 10.4.1 — Số Fibonacci Thứ N Rất Lớn Modulo M
- **Bối cảnh:** Tính $F_N \pmod M$ với $N \le 10^{18}$ và $M \le 1000$ bằng cách rút gọn số mũ $N \pmod{\pi(M)}$.
- **Input:** `2014 3` $\implies$ **Output:** `1`

##### Bài 10.4.2 — Tìm Chu Kỳ Tuần Hoàn Của Dãy Số Dư
- **Bối cảnh:** Cho dãy số $A_i = (A_{i-1} \times K) \pmod M$. Tìm chu kỳ lặp lại đầu tiên của dãy.
- **Input:** `2 3 7` $\implies$ **Output:** `6`

---

### Bài 10.5 — Luyện tập tổng hợp và đánh giá chương

### Đề bài 12 bài tập phân tầng tự chứa (iKHEDU Standard)

#### Tầng A — Củng cố nền tảng (Rating 1000 - 1200)

##### Bài 10.5.1 — Tổng Tích Giá Trị Giao Dịch Chứng Khoán Modulo
- **Bối cảnh:** Tính giá trị biểu thức $(A \times B + C) \pmod{10^9+7}$ với các tham số lên tới $10^{18}$.
- **Input:** Ba số nguyên $A, B, C$ ($1 \le A, B, C \le 10^{18}$).
- **Output:** Ghi kết quả lấy dư cho $10^9+7$.

##### Bài 10.5.2 — Lũy Thừa Cấp Số Nhân Lãi Suất Kép
- **Bối cảnh:** Tính tổng cấp số nhân $S = 1 + A + A^2 + \dots + A^N \pmod M$.
- **Sample:** `2 3 1000` $\implies$ **Output:** `15` ($1+2+4+8 = 15$).

##### Bài 10.5.3 — Tìm Nghịch Đảo Modulo Đơn Điểm
- **Bối cảnh:** Cho số nguyên $X$. Tìm số nguyên $Y \in [1, 10^9+6]$ sao cho $(X \times Y) \pmod{10^9+7} = 1$.
- **Input:** $X = 2 \implies$ **Output:** `500000004`.

##### Bài 10.5.4 — Đếm Số Dãy Nhị Phân Độ Dài N
- **Bối cảnh:** Tính $2^N \pmod{10^9+7}$ với $N \le 10^{18}$.
- **Sample:** `10` $\implies$ **Output:** `1024`.

---

#### Tầng B — Vận dụng thi đấu (Rating 1200 - 1500)

##### Bài 10.5.5 — Tổ Hợp Chọn Nhân Sự $C_N^K$ Với $Q$ Truy Vấn
- **Bối cảnh:** Trả lời $Q$ truy vấn tính $C_N^K \pmod{10^9+7}$ với $N, K \le 10^6$ trong $\mathcal{O}(1)$ mỗi truy vấn nhờ tiền xử lý mảng giai thừa.

##### Bài 10.5.6 — Đếm Số Đường Đi Của Robot Trong Kho Hàng
- **Bối cảnh:** Robot di chuyển trên lưới $N \times M$, chỉ đi sang phải hoặc xuống dưới. Tính số cách đi $C_{N+M}^N \pmod{10^9+7}$.

##### Bài 10.5.7 — Số Dãy Ngoặc Đúng Bằng Số Catalan
- **Bối cảnh:** Tính số Catalan thứ $N$: $C_N = \frac{1}{N+1} C_{2N}^N \pmod{10^9+7}$.
- **Input:** `3` $\implies$ **Output:** `5`.

##### Bài 10.5.8 — Lũy Thừa Tầng $A^{B^C} \pmod P$
- **Bối cảnh:** Áp dụng định lý Fermat nhỏ trên số mũ: $A^{B^C} \pmod P \equiv A^{(B^C \pmod{P-1})} \pmod P$.

---

#### Tầng C — Chuyển giao & Nâng cao (Rating 1500 - 1800)

##### Bài 10.5.9 — Nghịch Đảo Modulo Bằng Thuật Toán Euclid Mở Rộng
- **Bối cảnh:** Tìm nghịch đảo modulo khi modulo $M$ không phải là số nguyên tố ($\gcd(A, M) = 1$).

##### Bài 10.5.10 — Giải Mã Tín Hiệu Bằng Định Lý Đồng Dư Trung Hoa (CRT)
- **Bối cảnh:** Tìm số nguyên $X$ nhỏ nhất thỏa mãn hệ phương trình đồng dư: $X \equiv r_i \pmod{m_i}$ với các $m_i$ nguyên tố cùng nhau từng đôi một.

##### Bài 10.5.11 — Định Lý Lucas Cho Tổ Hợp Siêu Lớn $N \le 10^{18}$
- **Bối cảnh:** Tính $C_N^K \pmod P$ với $P$ là số nguyên tố nhỏ ($P \le 10^5$) và $N, K \le 10^{18}$.

##### Bài 10.5.12 — Mô Phỏng Hệ Mật Mã Bất Đối Xứng RSA
- **Bối cảnh:** Cho khóa công khai $(e, n)$ và bản tin mã hóa $C$. Hãy giải mã tìm bản rõ $M = C^d \pmod n$ với $d$ là nghịch đảo modulo của $e \pmod{\phi(n)}$.

---

### Bẫy lỗi thường gặp & Rubric đánh giá
| Lỗi thường gặp | Cách kiểm soát |
|---|---|
| Lấy modulo trực tiếp trên số mũ: $A^B \pmod M \ne A^{B \pmod M}$ | Số mũ phải lấy modulo cho $P - 1$ theo Định lý Fermat nhỏ |
| Phép chia không dùng nghịch đảo modulo | Luôn thay $\frac{A}{B}$ bằng $A \times B^{P-2} \pmod P$ |

### Rubric hoàn thành chương
| Mức độ | Tiêu chí đánh giá |
|---|---|
| **Cơ bản (Tầng A)** | Nắm vững 4 phép tính Modulo không bị tràn số và số âm. |
| **Vận dụng (Tầng B)** | Cài đặt tiền xử lý nghịch đảo giai thừa tính $C_N^K$ trong $\mathcal{O}(1)$. |
| **Thành thạo (Tầng C)** | Hiểu và áp dụng định lý Fermat trên số mũ và Euclid mở rộng. |
