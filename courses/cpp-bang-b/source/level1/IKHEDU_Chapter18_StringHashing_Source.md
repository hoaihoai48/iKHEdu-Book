# TÀI LIỆU GỐC — CHƯƠNG 18: MÃ HÓA XÂU (STRING HASHING)

## Bản đồ chương

| Trường | Nội dung |
|---|---|
| Mục tiêu | Nắm vững kỹ thuật Băm xâu đa thức (Polynomial Rolling Hash) để so sánh 2 xâu con bất kỳ $S[L.R]$ và $T[L'.R']$ trong thời gian $\mathcal{O}(1)$; làm chủ kỹ thuật Băm đôi (Double Hashing) triệt tiêu hoàn toàn va chạm mã băm; kết hợp Hashing với Tìm kiếm nhị phân |
| Kiến thức cần có | Xử lý xâu, mảng tiền tố (Prefix Sum), số học Modulo, lũy thừa nhanh |
| Phạm vi | Hàm băm đa thức, Mảng tiền tố Hash $H[i]$, Lấy mã băm đoạn con $S[L.R]$ trong $\mathcal{O}(1)$, Kỹ thuật Băm đôi (Double Hashing), Tìm xâu con chung dài nhất bằng Hashing + Binary Search $\mathcal{O}(N \log N)$ |
| Số bài | 4 bài học lý thuyết & ví dụ mẫu + 1 bài luyện tập phân tầng |
| Tổng bài tập | 12 bài tập tự chứa (Tầng A: 4 bài, Tầng B: 4 bài, Tầng C: 4 bài) |

### Learning outcomes

Sau chương này, em có thể:
1. Xây dựng mảng tiền tố mã băm $H[i]$ và mảng lũy thừa cơ số $P^i$ trong thời gian $\mathcal{O}(N)$.
2. Lấy giá trị mã băm của đoạn con $S[L.R]$ bất kỳ trong thời gian $\mathcal{O}(1)$ bằng công thức đồng dư.
3. Cài đặt Băm đôi (Double Hashing) với 2 modulo độc lập (ví dụ $10^9+7$ và $10^9+9$) để chống tràn và triệt tiêu va chạm.
4. Kết hợp Hashing với Tìm kiếm nhị phân để tìm xâu đối xứng dài nhất hoặc tiền tố chung dài nhất (LCP) trong $\mathcal{O}(N \log N)$.

### Câu hỏi trung tâm của chương

> **Làm thế nào để so sánh xem hai đoạn văn bản dài hàng triệu ký tự có giống hệt nhau không chỉ trong $1$ phép so sánh duy nhất**

---

### Bài 18.1 — Hàm băm đa thức và Mảng tiền tố Hash

#### 1. Khái niệm & Công thức mã băm
- **Công thức mã băm đa thức:**
$$H[i] = (H[i - 1] \times \text{BASE} + S[i]) \pmod M$$
(với $\text{BASE} = 311$, $M = 10^9+7$).
- **Mã băm của đoạn con $S[L.R]$:**
$$\text{getHash}(L, R) = (H[R] - H[L - 1] \times \text{BASE}^{R - L + 1} + M \times M) \pmod M$$

---

#### 2. Bài toán mẫu có hướng dẫn

> **Bài toán mẫu 18.1: So Khớp Mẫu Mã Độc Trong Tệp Thực Thi** 
> **Bối cảnh:** Phần mềm diệt virus Bkav cần tìm tất cả các vị trí xuất hiện của chuỗi chữ ký mã độc $P$ trong tệp thực thi $T$. 
> **Input:** `ikheducppikhedu` \ `ikhedu` $\implies$ **Output:** `1 10` (xuất hiện tại vị trí 1 và 10).

#### Cài đặt C++
```cpp
#include <bits/stdc++.h>
using namespace std;

const long long BASE = 311;
const long long MOD = 1000000007;

int main() {
ios::sync_with_stdio(false);
cin.tie(nullptr);

string t, p;
if (!(cin >> t >> p)) return 0;

int n = t.size(), m = p.size();
t = " " + t;
p = " " + p;

vector<long long> power(n + 1, 1), h(n + 1, 0);
for (int i = 1; i <= n; i++) {
power[i] = (power[i - 1] * BASE) % MOD;
h[i] = (h[i - 1] * BASE + t[i]) % MOD;
}

long long hashP = 0;
for (int i = 1; i <= m; i++) {
hashP = (hashP * BASE + p[i]) % MOD;
}

for (int i = 1; i <= n - m + 1; i++) {
long long currentHash = (h[i + m - 1] - h[i - 1] * power[m] % MOD + MOD) % MOD;
if (currentHash == hashP) {
cout << i << " ";
}
}
cout << "\n";

return 0;
}
```

---

#### 3. Bài tập thực hành Bài 18.1

##### Bài 18.1.1 — Đếm Số Lần Xuất Hiện Của Xâu Mẫu
- **Bối cảnh:** Đếm tổng số lần xâu $P$ xuất hiện trong xâu $T$ bằng hàm băm Rolling Hash.
- **Input:** `aaaaa` \ `aa` $\implies$ **Output:** `4`

##### Bài 18.1.2 — Tìm Vị Trí Đầu Tiên Của Xâu Mẫu
- **Bối cảnh:** Tìm chỉ số xuất hiện đầu tiên của $P$ trong $T$. Nếu không có in -1.
- **Input:** `abcdef` \ `cde` $\implies$ **Output:** `3`

---

### Bài 18.2 — Lấy mã băm đoạn con $S[L.R]$ trong $\mathcal{O}(1)$

#### 1. Khái niệm & Thuật toán
- Sử dụng mảng tiền tố `h` và mảng lũy thừa `power` lấy mã băm trong $\mathcal{O}(1)$.

---

#### 2. Bài toán mẫu có hướng dẫn

> **Bài toán mẫu 18.2: So Sánh Hai Đoạn Văn Bản Trong $\mathcal{O}(1)$** 
> **Bối cảnh:** Nhập xâu $S$. Thực hiện $Q$ truy vấn kiểm tra xem đoạn con $S[a.b]$ có giống hệt đoạn con $S[c.d]$ hay không. 
> **Input:** `abacaba` \ `2` \ `1 3 5 7` \ `1 2 4 5` $\implies$ **Output:** `YES` \ `NO`.

#### Cài đặt C++
```cpp
#include <bits/stdc++.h>
using namespace std;

const long long BASE = 311;
const long long MOD = 1000000007;

int main() {
ios::sync_with_stdio(false);
cin.tie(nullptr);

string s;
int q;
if (!(cin >> s >> q)) return 0;

int n = s.size();
s = " " + s;

vector<long long> power(n + 1, 1), h(n + 1, 0);
for (int i = 1; i <= n; i++) {
power[i] = (power[i - 1] * BASE) % MOD;
h[i] = (h[i - 1] * BASE + s[i]) % MOD;
}

auto getHash = [&](int l, int r) {
return (h[r] - h[l - 1] * power[r - l + 1] % MOD + MOD) % MOD;
};

while (q--) {
int a, b, c, d;
cin >> a >> b >> c >> d;
if (b - a == d - c && getHash(a, b) == getHash(c, d)) {
cout << "YES\n";
} else {
cout << "NO\n";
}
}

return 0;
}
```

---

#### 3. Bài tập thực hành Bài 18.2

##### Bài 18.2.1 — Kiểm Tra Xâu Đối Xứng Palindrome Trong $\mathcal{O}(1)$
- **Bối cảnh:** Dựng 2 mảng Hash xuôi và ngược. Trả lời $Q$ truy vấn kiểm tra xem đoạn $S[L.R]$ có phải Palindrome không.
- **Input:** `abacaba 1` \ `1 7` $\implies$ **Output:** `YES`

##### Bài 18.2.2 — So Sánh Hai Đoạn Xâu Con Độ Dài Khác Nhau
- **Bối cảnh:** $Q$ truy vấn kiểm tra xem $S[a.b]$ có bằng $S[c.d]$ không.
- **Input:** `abcabc 1` \ `1 3 4 6` $\implies$ **Output:** `YES`

---

### Bài 18.3 — Kỹ thuật Băm đôi (Double Hashing) chống va chạm

#### 1. Khái niệm & Thuật toán
- Sử dụng đồng thời 2 bộ $(\text{BASE}_1, \text{MOD}_1)$ và $(\text{BASE}_2, \text{MOD}_2)$ để xác suất va chạm giảm xuống $\approx 10^{-18}$ (tuyệt đối an toàn).

---

#### 2. Bài toán mẫu có hướng dẫn

> **Bài toán mẫu 18.3: Băm Đôi Chống Bộ Dữ Liệu Tấn Công Thử Nghiệm** 
> **Bối cảnh:** Cài đặt hàm lấy mã băm đôi cho xâu $S$ với 2 Modulo $10^9+7$ và $10^9+9$.

#### Cài đặt C++
```cpp
#include <bits/stdc++.h>
using namespace std;

const long long BASE = 311;
const long long MOD1 = 1000000007;
const long long MOD2 = 1000000009;

int main() {
ios::sync_with_stdio(false);
cin.tie(nullptr);

string s;
if (!(cin >> s)) return 0;

int n = s.size();
s = " " + s;

vector<long long> pow1(n + 1, 1), h1(n + 1, 0);
vector<long long> pow2(n + 1, 1), h2(n + 1, 0);

for (int i = 1; i <= n; i++) {
pow1[i] = (pow1[i - 1] * BASE) % MOD1;
h1[i] = (h1[i - 1] * BASE + s[i]) % MOD1;
pow2[i] = (pow2[i - 1] * BASE) % MOD2;
h2[i] = (h2[i - 1] * BASE + s[i]) % MOD2;
}

auto getDoubleHash = [&](int l, int r) {
long long hash1 = (h1[r] - h1[l - 1] * pow1[r - l + 1] % MOD1 + MOD1) % MOD1;
long long hash2 = (h2[r] - h2[l - 1] * pow2[r - l + 1] % MOD2 + MOD2) % MOD2;
return make_pair(hash1, hash2);
};

cout << "Double hash full string: " << getDoubleHash(1, n).first << ", " << getDoubleHash(1, n).second << "\n";
return 0;
}
```

---

#### 3. Bài tập thực hành Bài 18.3

##### Bài 18.3.1 — Đếm Số Xâu Con Khác Nhau Độ Dài K Bằng Double Hash
- **Bối cảnh:** Cho xâu $S$. Đếm số lượng xâu con phân biệt có độ dài đúng bằng $K$ bằng cách lưu Double Hash vào `set<pair<long long, long long>>`.
- **Input:** `aaaa 2` $\implies$ **Output:** `1` (`"aa"`).

##### Bài 18.3.2 — Băm Đôi Kiểm Tra Tập Hợp Xâu Trùng Nhau
- **Bối cảnh:** Cho $N$ xâu. Đếm số lượng xâu phân biệt bằng Double Hash.
- **Input:** `3` \ `abc` \ `def` \ `abc` $\implies$ **Output:** `2`

---

### Bài 18.4 — Kết hợp Hashing với Tìm kiếm nhị phân

#### 1. Khái niệm & Ứng dụng LCP
- Tìm tiền tố chung dài nhất (Longest Common Prefix) của 2 vị trí trong $\mathcal{O}(\log N)$.

---

#### 2. Bài toán mẫu có hướng dẫn

> **Bài toán mẫu 18.4: Tìm Tiền Tố Chung Dài Nhất (LCP)** 
> **Bối cảnh:** Tìm độ dài tiền tố chung dài nhất của 2 hậu tố bắt đầu tại vị trí $i$ và $j$ trong xâu $S$. 
> **Input:** `banana` \ `2 4` $\implies$ **Output:** `3` (`"anana"` và `"ana"` có LCP là `"ana"` dài 3).

#### Cài đặt C++
```cpp
#include <bits/stdc++.h>
using namespace std;

const long long BASE = 311;
const long long MOD = 1000000007;

int main() {
ios::sync_with_stdio(false);
cin.tie(nullptr);

string s;
int pos1, pos2;
if (!(cin >> s >> pos1 >> pos2)) return 0;

int n = s.size();
s = " " + s;

vector<long long> power(n + 1, 1), h(n + 1, 0);
for (int i = 1; i <= n; i++) {
power[i] = (power[i - 1] * BASE) % MOD;
h[i] = (h[i - 1] * BASE + s[i]) % MOD;
}

auto getHash = [&](int l, int r) {
return (h[r] - h[l - 1] * power[r - l + 1] % MOD + MOD) % MOD;
};

int low = 1, high = min(n - pos1 + 1, n - pos2 + 1), ans = 0;
while (low <= high) {
int mid = low + (high - low) / 2;
if (getHash(pos1, pos1 + mid - 1) == getHash(pos2, pos2 + mid - 1)) {
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

---

#### 3. Bài tập thực hành Bài 18.4

##### Bài 18.4.1 — Tìm Chu Kỳ Nhỏ Nhất Của Xâu Ký Tự
- **Bối cảnh:** Tìm độ dài $K$ nhỏ nhất sao cho xâu $S$ có thể được tạo thành bằng cách lặp lại xâu con độ dài $K$.
- **Input:** `abcabcabc` $\implies$ **Output:** `3`

##### Bài 18.4.2 — Đoạn Con Đối Xứng Dài Nhất Có Tâm Tại K
- **Bối cảnh:** Tìm độ dài Palindrome con lẻ dài nhất nhận vị trí $K$ làm tâm bằng Hashing + Binary Search.
- **Input:** `abacaba 4` $\implies$ **Output:** `7`

---

### Bài 18.5 — Luyện tập tổng hợp và đánh giá chương

### Đề bài 12 bài tập phân tầng tự chứa (iKHEDU Standard)

#### Tầng A — Củng cố nền tảng (Rating 1000 - 1200)

##### Bài 18.5.1 — So Sánh Hai Đoạn Xâu Con Trong $\mathcal{O}(1)$
- **Bối cảnh:** $Q$ truy vấn so sánh xem $S[a.b]$ có bằng $S[c.d]$ không.

##### Bài 18.5.2 — Tìm Kiếm Mẫu Xâu Con Đơn Giản (String Matching)
- **Bối cảnh:** Tìm tất cả vị trí xuất hiện của xâu mẫu $P$ trong văn bản $T$.

##### Bài 18.5.3 — Kiểm Tra Đoạn Con Đối Xứng Bằng Hashing
- **Bối cảnh:** Xây dựng Hash xuôi và Hash ngược để kiểm tra $S[L.R]$ có phải Palindrome không trong $\mathcal{O}(1)$.

##### Bài 18.5.4 — Đếm Số Đoạn Con Bằng Nhau
- **Bối cảnh:** Đếm số lượng đoạn con độ dài $K$ giống nhau trong văn bản.

---

#### Tầng B — Vận dụng thi đấu (Rating 1200 - 1500)

##### Bài 18.5.5 — Tiền Tố Chung Dài Nhất (Longest Common Prefix - LCP)
- **Bối cảnh:** Kết hợp Hashing và Binary Search tìm LCP của 2 hậu tố trong $\mathcal{O}(\log N)$.

##### Bài 18.5.6 — Đoạn Con Đối Xứng Dài Nhất Trong $\mathcal{O}(N \log N)$
- **Bối cảnh:** Tìm độ dài Palindrome con dài nhất bằng Hashing + Binary Search theo tâm.

##### Bài 18.5.7 — Tìm Chu Kỳ Nhỏ Nhất Của Xâu Ký Tự
- **Bối cảnh:** Kiểm tra xâu $S$ có thể được tạo thành bằng cách lặp lại xâu con độ dài $K$ hay không.

##### Bài 18.5.8 — Xâu Con Xuất Hiện Nhiều Lần Nhất Độ Dài K
- **Bối cảnh:** Dùng Hashing kết hợp Bảng băm tìm xâu con độ dài $K$ xuất hiện nhiều lần nhất.

---

#### Tầng C — Chuyển giao & Nâng cao (Rating 1500 - 1800)

##### Bài 18.5.9 — Xâu Con Chung Dài Nhất Của Hai Văn Bản (Longest Common Substring)
- **Bối cảnh:** Tìm độ dài xâu con chung dài nhất của $S$ và $T$ trong $\mathcal{O}((N + M) \log(\min(N, M)))$.

##### Bài 18.5.10 — Cài Đặt Băm Đôi Double Hashing Chống Bộ Test Hack
- **Bối cảnh:** Cài đặt hàm băm đôi với 2 modulo $10^9+7$ và $10^9+9$ vượt qua bộ test anti-hash.

##### Bài 18.5.11 — Đếm Số Lượng Xâu Con Phân Biệt Của Văn Bản
- **Bối cảnh:** Sử dụng Hashing và Suffix Array đếm tổng số xâu con phân biệt trong $\mathcal{O}(N^2)$ hoặc $\mathcal{O}(N \log^2 N)$.

##### Bài 18.5.12 — Mã Hóa Cây Bằng Cây Băm Đồng Cấu (Tree Isomorphism Hashing)
- **Bối cảnh:** Kiểm tra xem hai cây có cấu trúc đồng dạng (isomorphic) hay không bằng hàm băm đệ quy trên cây.

---

### Bẫy lỗi thường gặp & Rubric đánh giá
| Lỗi thường gặp | Cách kiểm soát |
|---|---|
| Bị tràn số âm khi lấy hash đoạn | Luôn cộng thêm `MOD` trước khi `% MOD`: `(h[R] - h[L-1]*power + MOD) % MOD` |
| Bị dính va chạm (Collision) khi chỉ dùng 1 Modulo $10^9+7$ trên tập dữ liệu $10^5$ xâu | Dùng Băm đôi (Double Hashing) |

### Rubric hoàn thành chương
| Mức độ | Tiêu chí đánh giá |
|---|---|
| **Cơ bản (Tầng A)** | Xây dựng mảng tiền tố hash và lấy mã băm đoạn con trong $\mathcal{O}(1)$. |
| **Vận dụng (Tầng B)** | Cài đặt kiểm tra Palindrome và tìm LCP bằng Binary Search trong $\mathcal{O}(\log N)$. |
| **Thành thạo (Tầng C)** | Cài đặt Double Hashing và giải bài toán Longest Common Substring. |
