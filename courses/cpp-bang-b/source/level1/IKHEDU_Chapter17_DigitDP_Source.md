# TÀI LIỆU GỐC — CHƯƠNG 17: QUY HOẠCH ĐỘNG CHỮ SỐ (DIGIT DP)

## Bản đồ chương

| Trường | Nội dung |
|---|---|
| Mục tiêu | Nắm vững kỹ thuật Quy hoạch động chữ số (Digit DP) để giải quyết các bài toán đếm số lượng số trong đoạn $[L, R]$ thỏa mãn các tính chất đặc biệt (tổng chữ số, chia hết, không chứa chữ số cấm, đối xứng) với $R \le 10^{18}$ trong $\mathcal{O}(\text{len} \times \text{states})$ |
| Kiến thức cần có | Đệ quy có nhớ (Memoization), xâu ký tự, chuyển đổi hệ thập phân |
| Phạm vi | Biến cờ `tight` (giới hạn cận trên), Biến cờ `leading_zero` (số 0 ở đầu), Hàm `count(N)` và công thức đoạn `count(R) - count(L - 1)`, Đếm số Palindrome, Đếm số có tổng chữ số chia hết cho $K$ |
| Số bài | 4 bài học lý thuyết & ví dụ mẫu + 1 bài luyện tập phân tầng |
| Tổng bài tập | 12 bài tập tự chứa (Tầng A: 4 bài, Tầng B: 4 bài, Tầng C: 4 bài) |

### Learning outcomes

Sau chương này, em có thể:
1. Chuyển đổi bài toán đếm trong đoạn $[L, R]$ thành `count(R) - count(L - 1)`.
2. Thiết kế hàm đệ quy có nhớ với trạng thái cơ bản `(index, tight, leading_zero, sum, rem)`.
3. Xử lý chính xác biến cờ `tight` để không vượt quá cận trên của số $N$.
4. Áp dụng Digit DP giải các bài toán đếm số chia hết, số không chứa chữ số 4/13, và số Palindrome trong $\mathcal{O}(\log_{10} N \times \text{states})$.

### Câu hỏi trung tâm của chương

> **Làm thế nào để đếm xem có bao nhiêu số nguyên từ $1$ đến $10^{18}$ có tổng các chữ số là số nguyên tố mà chỉ mất chưa tới $0.01$ giây**

---

### Bài 17.1 — Ý tưởng cốt lõi và Biến cờ `tight`

#### 1. Khái niệm & Trạng thái Digit DP
- **Chuyển về bài toán đoạn:** $\text{Count}([L, R]) = \text{Count}(R) - \text{Count}(L - 1)$.
- **Biến cờ `tight`:**
- `tight = 1`: Các chữ số trước đó đều chạm trần $N \implies$ Chữ số hiện tại chỉ được chọn từ $0$ đến $D[index]$.
- `tight = 0`: Đã có chữ số trước đó nhỏ hơn trần $N \implies$ Chữ số hiện tại tự do chọn từ $0$ đến $9$.

---

#### 2. Bài toán mẫu có hướng dẫn

> **Bài toán mẫu 17.1: Đếm Số May Mắn Không Chứa Chữ Số 4** 
> **Bối cảnh:** Trong quan niệm phong thủy của một số nước Á Đông, số 4 phát âm giống chữ "tử" nên các tòa nhà cao ốc thường tránh đánh số tầng chứa chữ số 4. 
> **Nhiệm vụ:** Em hãy đếm xem trong đoạn $[L, R]$ có bao nhiêu số nguyên không chứa bất kỳ chữ số 4 nào ($1 \le L \le R \le 10^{18}$). 
> **Input:** `1 20` $\implies$ **Output:** `18` (loại 2 số là 4 và 14).

#### Cài đặt C++
```cpp
#include <bits/stdc++.h>
using namespace std;

string numStr;
long long memo[20][2];

long long solveDP(int idx, bool tight) {
if (idx == (int)numStr.size()) return 1;
if (memo[idx][tight] != -1) return memo[idx][tight];

int limit = tight (numStr[idx] - '0') : 9;
long long ans = 0;

for (int digit = 0; digit <= limit; digit++) {
if (digit == 4) continue;
bool nextTight = tight && (digit == limit);
ans += solveDP(idx + 1, nextTight);
}

return memo[idx][tight] = ans;
}

long long countValid(long long n) {
if (n < 0) return 0;
numStr = to_string(n);
memset(memo, -1, sizeof(memo));
return solveDP(0, true);
}

int main() {
ios::sync_with_stdio(false);
cin.tie(nullptr);

long long l, r;
if (!(cin >> l >> r)) return 0;

cout << countValid(r) - countValid(l - 1) << "\n";
return 0;
}
```

---

#### 3. Bài tập thực hành Bài 17.1

##### Bài 17.1.1 — Đếm Số Không Chứa Cặp Số 13
- **Bối cảnh:** Đếm số trong đoạn $[L, R]$ không chứa 2 chữ số 13 đứng cạnh nhau ($R \le 10^{18}$).
- **Input:** `1 20` $\implies$ **Output:** `19` (loại số 13).

##### Bài 17.1.2 — Đếm Số Không Chứa Chữ Số 7
- **Bối cảnh:** Đếm số lượng số trong đoạn $[1, N]$ không chứa bất kỳ chữ số 7 nào ($N \le 10^{18}$).
- **Input:** `10` $\implies$ **Output:** `9`

---

### Bài 17.2 — Đếm số theo Tổng chữ số và Điều kiện chia hết

#### 1. Khái niệm & Thuật toán
- Trạng thái thêm biến `sumDigits` hoặc `remainder`.

---

#### 2. Bài toán mẫu có hướng dẫn

> **Bài toán mẫu 17.2: Đếm Số Có Tổng Chữ Số Bằng S** 
> **Bối cảnh:** Đếm số trong đoạn $[1, N]$ ($N \le 10^{18}$) có tổng các chữ số đúng bằng $S$ ($S \le 180$). 
> **Input:** `20 2` $\implies$ **Output:** `2` (số 2 và 11, 20 $\implies$ tổng 2: 2, 11, 20 có 3 số).

#### Cài đặt C++
```cpp
#include <bits/stdc++.h>
using namespace std;

string numStr;
long long memo[20][2][200];

long long solveDP(int idx, bool tight, int currentSum, int targetSum) {
if (idx == (int)numStr.size()) return (currentSum == targetSum);
if (memo[idx][tight][currentSum] != -1) return memo[idx][tight][currentSum];

int limit = tight (numStr[idx] - '0') : 9;
long long ans = 0;

for (int digit = 0; digit <= limit; digit++) {
if (currentSum + digit > targetSum) continue;
bool nextTight = tight && (digit == limit);
ans += solveDP(idx + 1, nextTight, currentSum + digit, targetSum);
}

return memo[idx][tight][currentSum] = ans;
}

long long countWithSum(long long n, int s) {
if (n <= 0) return 0;
numStr = to_string(n);
memset(memo, -1, sizeof(memo));
return solveDP(0, true, 0, s);
}

int main() {
ios::sync_with_stdio(false);
cin.tie(nullptr);

long long n;
int s;
if (!(cin >> n >> s)) return 0;

cout << countWithSum(n, s) << "\n";
return 0;
}
```

---

#### 3. Bài tập thực hành Bài 17.2

##### Bài 17.2.1 — Đếm Số Có Tổng Chữ Số Chia Hết Cho K
- **Bối cảnh:** Đếm số lượng số trong đoạn $[1, N]$ ($N \le 10^{18}$) có tổng các chữ số chia hết cho $K$ ($1 \le K \le 50$).
- **Input:** `30 5` $\implies$ **Output:** `6` (các số: 5, 14, 19, 23, 28..).

##### Bài 17.2.2 — Đếm Số Có Tổng Chữ Số Là Số Chẵn
- **Bối cảnh:** Đếm số trong $[L, R]$ có tổng các chữ số là số chẵn ($R \le 10^{18}$).
- **Input:** `1 10` $\implies$ **Output:** `5` (2, 4, 6, 8, 11.. -> 2, 4, 6, 8)

---

### Bài 17.3 — Xử lý số 0 ở đầu (Leading Zeros)

#### 1. Khái niệm & Thuật toán
- Biến `leading_zero`: Chỉ kích hoạt các quy tắc tích lũy khi đã xuất hiện chữ số đầu tiên $> 0$.

---

#### 2. Bài toán mẫu có hướng dẫn

> **Bài toán mẫu 17.3: Đếm Số Lượng Chữ Số 0 Xuất Hiện Trong Dãy** 
> **Bối cảnh:** Đếm tổng số chữ số `0` có nghĩa xuất hiện khi viết tất cả các số từ $1$ đến $N$ ($N \le 10^{18}$). 
> **Input:** `10` $\implies$ **Output:** `1` (số 10 có một chữ số 0, các số từ 1.9 không tính số 0 vô nghĩa).

#### Cài đặt C++
```cpp
#include <bits/stdc++.h>
using namespace std;

string numStr;
long long memo[20][2][2][20];

long long solveDP(int idx, bool tight, bool isLeading, int zeroCount) {
if (idx == (int)numStr.size()) return zeroCount;
if (memo[idx][tight][isLeading][zeroCount] != -1) return memo[idx][tight][isLeading][zeroCount];

int limit = tight (numStr[idx] - '0') : 9;
long long ans = 0;

for (int digit = 0; digit <= limit; digit++) {
bool nextTight = tight && (digit == limit);
bool nextLeading = isLeading && (digit == 0);
int nextZeroCount = zeroCount + (!nextLeading && digit == 0);
ans += solveDP(idx + 1, nextTight, nextLeading, nextZeroCount);
}

return memo[idx][tight][isLeading][zeroCount] = ans;
}

long long countZeros(long long n) {
if (n < 0) return 0;
numStr = to_string(n);
memset(memo, -1, sizeof(memo));
return solveDP(0, true, true, 0);
}

int main() {
ios::sync_with_stdio(false);
cin.tie(nullptr);

long long n;
if (!(cin >> n)) return 0;

cout << countZeros(n) << "\n";
return 0;
}
```

---

#### 3. Bài tập thực hành Bài 17.3

##### Bài 17.3.1 — Đếm Số Lượng Chữ Số 7 Trong Đoạn $[L, R]$
- **Bối cảnh:** Đếm tổng số lần xuất hiện của chữ số 7 trong tất cả các số từ $L$ đến $R$ ($1 \le L \le R \le 10^{18}$).
- **Input:** `1 20` $\implies$ **Output:** `2` (số 7 và số 17).

##### Bài 17.3.2 — Đếm Số Không Có Hai Chữ Số Giống Nhau Đứng Cạnh Nhau
- **Bối cảnh:** Đếm số trong $[1, N]$ không có 2 chữ số kề nhau bằng nhau (xử lý leading zero).
- **Input:** `20` $\implies$ **Output:** `18` (loại 11)

---

### Bài 17.4 — Bài toán số Palindrome và điều kiện đối xứng

#### 1. Khái niệm & Thuật toán
- Cố định nửa đầu, suy ra nửa sau đối xứng để kiểm tra điều kiện.

---

#### 2. Bài toán mẫu có hướng dẫn

> **Bài toán mẫu 17.4: Đếm Số Đối Xứng (Palindrome) Đến N** 
> **Bối cảnh:** Đếm số lượng số nguyên dương đối xứng trong đoạn $[1, N]$ với $N \le 10^{18}$. 
> **Input:** `100` $\implies$ **Output:** `18` (1.9 và 11, 22, 33, 44, 55, 66, 77, 88, 99).

#### Cài đặt C++
```cpp
#include <bits/stdc++.h>
using namespace std;

long long countPalindromes(long long n) {
if (n <= 0) return 0;
string s = to_string(n);
int len = s.size();

long long total = 0;
// Đếm số Palindrome có độ dài < len
for (int l = 1; l < len; l++) {
int half = (l + 1) / 2;
long long count = 9;
for (int i = 1; i < half; i++) count *= 10;
total += count;
}

// Đếm số Palindrome có độ dài đúng bằng len
int halfLen = (len + 1) / 2;
long long prefix = stoll(s.substr(0, halfLen));
long long minPrefix = 1;
for (int i = 1; i < halfLen; i++) minPrefix *= 10;

total += (prefix - minPrefix);

// Kiểm tra chính số prefix tạo thành Palindrome có <= n không
string firstHalf = to_string(prefix);
string secondHalf = firstHalf;
if (len % 2 == 1) secondHalf.pop_back();
reverse(secondHalf.begin(), secondHalf.end());
string fullPalin = firstHalf + secondHalf;

if (stoll(fullPalin) <= n) total++;

return total;
}

int main() {
ios::sync_with_stdio(false);
cin.tie(nullptr);

long long n;
if (!(cin >> n)) return 0;

cout << countPalindromes(n) << "\n";
return 0;
}
```

---

#### 3. Bài tập thực hành Bài 17.4

##### Bài 17.4.1 — Đếm Số Palindrome Trong Đoạn $[L, R]$
- **Bối cảnh:** Cho hai số $L, R \le 10^{18}$. Đếm số lượng số Palindrome trong đoạn $[L, R]$.
- **Input:** `10 100` $\implies$ **Output:** `9` (11, 22, .., 99).

##### Bài 17.4.2 — Tìm Số Palindrome Nhỏ Nhất Lớn Hơn N
- **Bối cảnh:** Cho số nguyên $N \le 10^{18}$. Tìm số Palindrome nhỏ nhất lớn hơn $N$.
- **Input:** `123` $\implies$ **Output:** `131`

---

### Bài 17.5 — Luyện tập tổng hợp và đánh giá chương

### Đề bài 12 bài tập phân tầng tự chứa (iKHEDU Standard)

#### Tầng A — Củng cố nền tảng (Rating 1000 - 1200)

##### Bài 17.5.1 — Đếm Số Không Chứa Chữ Số Cấm
- **Bối cảnh:** Đếm số trong đoạn $[L, R]$ không chứa chữ số $K$.

##### Bài 17.5.2 — Đếm Số Có Tổng Chữ Số Bằng S
- **Bối cảnh:** Đếm số trong $[1, N]$ có tổng các chữ số đúng bằng $S$.

##### Bài 17.5.3 — Đếm Số Chia Hết Cho K
- **Bối cảnh:** Đếm số có tổng chữ số chia hết cho $K$ ($K \le 100$).

##### Bài 17.5.4 — Số Lượng Chữ Số 1 Xuất Hiện Trong Dãy
- **Bối cảnh:** Đếm tổng số lần xuất hiện của chữ số 1 trong các số từ $1$ đến $N$.

---

#### Tầng B — Vận dụng thi đấu (Rating 1200 - 1500)

##### Bài 17.5.5 — Biển Số Xe Phát Tài Không Chứa Số 4 Và 7
- **Bối cảnh:** Đếm số lượng biển số xe may mắn trong đoạn $[L, R]$.

##### Bài 17.5.6 — Số Lượng Số Tự Chia Hết Cho Tổng Chữ Số Của Nó
- **Bối cảnh:** Đếm số Harshad ($N \% \text{sumDigits}(N) == 0$) với $N \le 10^{18}$.

##### Bài 17.5.7 — Số Lượng Số Đối Xứng (Palindrome) Trong Đoạn $[L, R]$
- **Bối cảnh:** Đếm số Palindrome từ $L$ đến $R$ ($R \le 10^{18}$).

##### Bài 17.5.8 — Đếm Số Có Các Chữ Số Đôi Một Khác Nhau
- **Bối cảnh:** Digit DP kết hợp Bitmask lưu tập các chữ số đã dùng.

---

#### Tầng C — Chuyển giao & Nâng cao (Rating 1500 - 1800)

##### Bài 17.5.9 — Tổng Tất Cả Các Số Thỏa Mãn Trong Đoạn $[L, R]$
- **Bối cảnh:** Tính tổng giá trị (không chỉ đếm số lượng) các số thỏa mãn modulo $10^9+7$.

##### Bài 17.5.10 — Tìm Số Thứ K Thỏa Mãn Tính Chất Bằng Binary Search + Digit DP
- **Bối cảnh:** Chặt nhị phân kết quả kết hợp hàm đếm Digit DP tìm số thứ $K$.

##### Bài 17.5.11 — Đếm Số Lượng Cặp Số Có Tổng XOR Bằng Tổng Đại Số
- **Bối cảnh:** $A \oplus B = A + B \iff A \text{ AND } B = 0$ trên dải $[1, N]$.

##### Bài 17.5.12 — Số Siêu Nguyên Tố Digit DP Trên Nhiều Hệ Cơ Số
- **Bối cảnh:** Chuyển đổi số sang hệ cơ số $B$ và đếm số thỏa mãn cấu trúc chữ số.

---

### Bẫy lỗi thường gặp & Rubric đánh giá
| Lỗi thường gặp | Cách kiểm soát |
|---|---|
| Lưu mảng `memo` cho cả trạng thái `tight = true` | Chỉ nhớ kết quả khi `tight = false` (hoặc khai báo mảng `memo` có chiều `tight`) |
| Quên xử lý `leading_zero` khiến các số 0 vô nghĩa ở đầu bị tính vào tích/tổng | Luôn duy trì biến `bool leadingZero` |

### Rubric hoàn thành chương
| Mức độ | Tiêu chí đánh giá |
|---|---|
| **Cơ bản (Tầng A)** | Cài đặt đệ quy Digit DP có cờ `tight` không lỗi tràn số. |
| **Vận dụng (Tầng B)** | Đếm số Palindrome và số không chứa chữ số cấm trong $\mathcal{O}(\log_{10} N)$. |
| **Thành thạo (Tầng C)** | Kết hợp Digit DP với Bitmask và tính tổng giá trị các số. |
