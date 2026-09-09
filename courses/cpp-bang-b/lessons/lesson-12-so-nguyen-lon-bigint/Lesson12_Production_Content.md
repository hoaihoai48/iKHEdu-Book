# Bài 12: Xử lý số nguyên lớn (BigInt)

## 1. Bản chất vấn đề & trực giác thuật toán

Trong ngôn ngữ lập trình C++, kiểu dữ liệu số nguyên có kích thước lớn nhất được hỗ trợ phần cứng là `unsigned long long` (64-bit, tối đa xấp xỉ $1.84 \times 10^{19}$) hoặc phần mở rộng GCC `__int128` (128-bit, tối đa xấp xỉ $3.4 \times 10^{38}$).

Tuy nhiên, trong các bài toán thực tế và đề thi học sinh giỏi (như tính $100!$, tính số Fibonacci thứ $1000$, hoặc tính $2^{10000}$ **mà không lấy dư modulo**), kết quả có thể dài hàng nghìn đến hàng chục nghìn chữ số. Vì C++ không có sẵn kiểu dữ liệu BigInteger như Python hay Java, lập trình viên thi đấu C++ bắt buộc phải **tự mô phỏng các phép tính số học đặt tính rồi tính như toán tiểu học** trên mảng ký tự (`string`) hoặc mảng số nguyên (`vector<int>`).

### Big integer hay modular arithmetic: Chọn vũ khí nào

![Phân định lựa chọn giải thuật: Modulo vs Big Integer](/Users/vu/Developer/ikhEdu_lessons/courses/cpp-bang-b/lessons/lesson-09-so-nguyen-lon-bigint/assets/bigint_vs_modulo_vi.svg)

| Đề bài yêu cầu | Quy mô kết quả | Vũ khí tối ưu | Kỹ thuật cốt lõi |
|---|:---:|:---:|---|
| Tính $A^B \pmod M$ ($B \le 10^{18}$) | $\le M$ | **Modulo** | Lũy thừa nhị phân $\mathcal{O}(\log B)$ |
| Tính $\frac{A}{B} \pmod M$ | $\le M$ | **Modulo** | Nghịch đảo Modulo $A \times B^{-1}$ |
| Tính $F_{10^6} \pmod M$ | $\le M$ | **Modulo** | Nhân ma trận nhị phân $\mathcal{O}(\log N)$ |
| Tính chính xác $2^{10000}$ | $\approx 3011$ chữ số | **Big Integer** | Lũy thừa nhị phân trên BigInt |
| Tính chính xác $1000!$ | $2568$ chữ số | **Big Integer** | Nhân BigInt $\times$ int liên tiếp |
| Tính chính xác số Fibonacci $F_{1000}$ | $209$ chữ số | **Big Integer** | Cộng BigInt + BigInt quy hoạch động |
| Số có $10^5$ chữ số nhưng chỉ cần $\% M$ | $\le M$ | **Modulo** | Vòng lặp Horner: `cur = (cur * 10 + d) % M` |

## 2. Mô phỏng từng bước

### Ví dụ 1: Mô phỏng phép cộng số lớn $A = 9876$ và $B = 543$

* **Quy tắc:** Đảo ngược chuỗi để chữ số hàng đơn vị nằm ở chỉ số `0`.
* $A' = [6, 7, 8, 9]$, $B' = [3, 4, 5]$.

| Vị trí hàng ($i$) | Cặp chữ số $(A'_i, B'_i)$ | Biến nhớ vào | Phép tính tổng | Ghi nhận & Nhớ mới |
| :---: | :---: | :---: | :---: | :--- |
| **0** (Hàng đơn vị) | $(6, 3)$ | $0$ | $6 + 3 + 0 = 9$ | Ghi **$9$**, nhớ $0$ |
| **1** (Hàng chục) | $(7, 4)$ | $0$ | $7 + 4 + 0 = 11$ | Ghi **$1$**, nhớ $1$ |
| **2** (Hàng trăm) | $(8, 5)$ | $1$ | $8 + 5 + 1 = 14$ | Ghi **$4$**, nhớ $1$ |
| **3** (Hàng nghìn) | $(9, 0)$ | $1$ | $9 + 0 + 1 = 10$ | Ghi **$0$**, nhớ $1$ |
| **Dư cuối** | — | $1$ | $\text{carry} = 1$ | Ghi **$1$**, nhớ $0$ |

* Kết quả đảo ngược: $[9, 1, 4, 0, 1] \implies \mathbf{10419}$.

### Ví dụ 2: Mô phỏng phép nhân số lớn $A = 48$ với số nhỏ $b = 7$

* $A' = [8, 4]$.
* **Bước 0 ($i = 0$):** $8 \times 7 + 0 = 56 \implies$ Ghi $6$, `carry` $= 5$.
* **Bước 1 ($i = 1$):** $4 \times 7 + 5 = 33 \implies$ Ghi $3$, `carry` $= 3$.
* **Dư cuối:** Ghi `carry` $= 3$.
* Kết quả đảo ngược: $[6, 3, 3] \implies \mathbf{336}$.

## 3. Lý thuyết cốt lõi & bất biến thuật toán

### 3.1. Mô hình biểu diễn số lớn & little-endian

* **Biểu diễn Little-Endian:** Lưu các chữ số theo thứ tự từ hàng thấp đến hàng cao (chữ số hàng đơn vị nằm ở chỉ số `0`).
* **Ưu điểm cốt lõi:** Hàng đơn vị nằm ở `index = 0`, nên khi cộng, trừ hoặc nhân ta có thể xử lý trực tiếp từ hàng thấp lên hàng cao và truyền biến nhớ `carry/borrow` sang phần tử kế tiếp ($a[0] \to a[1] \to a[2] \dots$). Ngoài ra, chữ số mới ở cuối có thể được thêm bằng `push_back()` với chi phí amortized $\mathcal{O}(1)$.
* **Biểu diễn Base 10 vs Base $10^9$:**
* **Base 10 (`string` / `vector<int>`):** Mỗi phần tử lưu 1 chữ số thập phân ($0 \dots 9$).
* **Base $10^9$ (`vector<int>` / `vector<long long>`):** Nhóm các cụm 9 chữ số từ phải sang trái.
* *Cấu trúc dữ liệu:* Mỗi chunk lưu kiểu `int` ($0 \dots 999,999,999$); phép nhân giữa 2 chunks lưu kiểu `long long` (vì $(10^9 - 1) \times (10^9 - 1) \approx 10^{18} < 2^{63}-1$).
* *Ví dụ:* Số $1234567890123456789$ được tách thành:
$$\text{chunks} = [23456789, 123456789, 1]$$
$$\text{Giá trị} = 23456789 + 123456789 \times 10^9 + 1 \times (10^9)^2$$

### 3.2. Bảng tổng hợp các phép toán số nguyên lớn ($\mathcal{O}(L^2)$)

| Phép toán | Bản chất thuật toán | Độ phức tạp thời gian | Lưu ý quan trọng |
|---|---|:---:|---|
| **So sánh ($A, B$)** | So sánh độ dài trước, sau đó so sánh từ điển | $\mathcal{O}(\max(L_A, L_B))$ | Xóa sạch số 0 ở đầu trước khi so sánh |
| **Cộng ($A + B$)** | Mô phỏng cộng từng hàng kèm biến nhớ `carry` | $\mathcal{O}(\max(L_A, L_B))$ | Xử lý `carry` còn dư sau khi hết chữ số |
| **Trừ ($A - B$)** | Mô phỏng trừ có mượn `borrow` ($A \ge B$) | $\mathcal{O}(L_A)$ | Xóa sạch số $0$ vô nghĩa ở đầu (`leading zeros`) |
| **Nhân nhỏ ($A \times b$)** | Nhân từng chữ số của $A$ với số nguyên $b$ | $\mathcal{O}(L_A)$ | Biến `carry` có thể vượt quá $10$, cần kiểu `long long` |
| **Nhân lớn ($A \times B$)** | Tích lũy $C[i + j] += A[i] \times B[j]$ rồi normalize | $\mathcal{O}(L_A \times L_B)$ | Khởi tạo mảng $L_A + L_B$ (áp dụng cho $L \le 5000$) |
| **Chia nhỏ ($A / b, A \% b$)** | Chia từ hàng cao nhất xuống hàng đơn vị | $\mathcal{O}(L_A)$ | Biến tích lũy `cur = cur * 10 + A[i]` |

### 3.3. Thuật toán chia số lớn cho số nhỏ & bất biến horner
Khi chia số lớn $A$ cho số nguyên $b$ ($1 \le b \le 10^9$), ta duyệt từ chữ số hàng cao nhất xuống hàng đơn vị:
```cpp
string divSmall(string a, long long b) {
string res = "";
long long cur = 0;
for (char c : a) {
cur = cur * 10 + (c - '0');
int digit = cur / b;
res.push_back(char('0' + digit));
cur %= b; // cur luôn là số dư hiện tại
}
// Xóa số 0 vô nghĩa ở đầu
int pos = 0;
while (pos + 1 < (int)res.size() && res[pos] == '0') pos++;
return res.substr(pos);
}
```

### Ghi chú:
**BẤT BIẾN TOÁN HỌC CỦA PHÉP CHIA TỪNG BƯỚC:**

> Vì trước mỗi bước lặp ta luôn duy trì số dư $0 \le cur < b$, nên sau khi nhận thêm một chữ số mới $cur = cur \times 10 + \text{digit}$, giá trị luôn thỏa mãn $cur < 10b$. Do đó thương tại mỗi bước `digit = cur / b` **chắc chắn luôn nằm trong khoảng $[0, 9]$** (là một chữ số thập phân hợp lệ duy nhất).

### 3.4. Tối ưu hóa base $10^9$ (chunking optimization)

* Thay vì thực hiện phép nhân trên từng chữ số đơn lẻ (Base 10 có $L$ chữ số), ta nén số lớn thành $\frac{L}{9}$ chunks trong Base $10^9$.
* **Đánh giá hiệu năng:** Số lượng cặp chunk cần nhân giảm xấp xỉ $\left(\frac{L}{9}\right) \times \left(\frac{L}{9}\right) = \frac{L^2}{81}$ (giảm khoảng 81 lần về số lượng phép nhân chunk). Tốc độ thực tế tăng vọt từ hàng chục lần giúp vượt qua các bài toán $N \le 10^5$.

## 4. Các bẫy lỗi lập trình kinh điển

1. **Quên xóa số 0 vô nghĩa ở đầu (Leading Zeros):**
* Sau phép trừ (ví dụ $1000 - 999 = 0001$), nếu không xóa số 0 thì chuỗi sẽ in ra `0001`.
* **Cách xử lý:** `while (res.size() > 1 && res.back() == '0') res.pop_back();`.

2. **Không xét trường hợp số $0$:**
* Phép nhân $A \times 0$ phải trả về `"0"`, không được trả về rỗng `""`.
3. **Biến `carry` trong phép nhân số nhỏ có thể rất lớn:**
* Trong phép nhân $A \times b$ với $b = 10^9$, `carry` sau mỗi bước có thể lên tới $10^9$, do đó kiểu dữ liệu của `carry` bắt buộc phải là `long long`.

## 5. Mẫu cài đặt chuẩn thi đấu (competitive templates)

```cpp
#include <bits/stdc++.h>
using namespace std;

// Hàm xóa số 0 vô nghĩa ở đầu chuỗi đảo ngược
void removeLeadingZeros(string &s) {
while (s.size() > 1 && s.back() == '0') {

s.pop_back();
}
}

// Phép cộng 2 số nguyên lớn không âm (A + B)
string addBig(string a, string b) {
reverse(a.begin(), a.end());
reverse(b.begin(), b.end());

string res = "";
int carry = 0;
int n = max(a.size(), b.size());

for (int i = 0; i < n || carry; ++i) {
int sum = carry;
if (i < (int)a.size()) sum += a[i] - '0';
if (i < (int)b.size()) sum += b[i] - '0';
res.push_back((sum % 10) + '0');
carry = sum / 10;
}

reverse(res.begin(), res.end());
return res;
}

// Phép trừ 2 số nguyên lớn không âm (A - B với A >= B)
string subBig(string a, string b) {
reverse(a.begin(), a.end());
reverse(b.begin(), b.end());

string res = "";
int borrow = 0;

for (int i = 0; i < (int)a.size(); ++i) {
int diff = (a[i] - '0') - borrow;
if (i < (int)b.size()) diff -= (b[i] - '0');
if (diff < 0) {
diff += 10;
borrow = 1;
} else {
borrow = 0;
}
res.push_back(diff + '0');
}

removeLeadingZeros(res);
reverse(res.begin(), res.end());
return res;
}

// Phép nhân 2 số nguyên lớn chuẩn mực và an toàn (A * B)
string mulBig(string a, string b) {
if (a == "0" || b == "0") return "0";

reverse(a.begin(), a.end());
reverse(b.begin(), b.end());

int n = a.size(), m = b.size();
vector<int> c(n + m, 0);

for (int i = 0; i < n; ++i) {
for (int j = 0; j < m; ++j) {
c[i + j] += (a[i] - '0') * (b[j] - '0');
}
}

// Normalize: Đẩy biến nhớ carry sang các ô kế tiếp
for (int i = 0; i + 1 < n + m; ++i) {
c[i + 1] += c[i] / 10;
c[i] %= 10;
}

while (c.size() > 1 && c.back() == 0) {

c.pop_back();
}

string res = "";
for (int i = (int)c.size() - 1; i >= 0; --i) {
res.push_back(c[i] + '0');
}

return res;
}

int main() {
ios::sync_with_stdio(false);
cin.tie(nullptr);

string a, b;
if (!(cin >> a >> b)) return 0;

cout << "A + B = " << addBig(a, b) << "\n";
cout << "A * B = " << mulBig(a, b) << "\n";
return 0;
}
```

## Câu hỏi trắc nghiệm củng cố khái niệm

#### Câu 1 (Lưu trữ dữ liệu Little-Endian):

Tại sao khi cài đặt số nguyên lớn trong C++, ta thường đảo ngược chuỗi để chữ số hàng đơn vị nằm ở vị trí chỉ số $0$ (Little-Endian)

- **A.** Để tiết kiệm bộ nhớ RAM.

- **B.** **[Đáp án đúng]** Để thao tác thêm chữ số mới vào cuối mảng (`push_back`) đạt độ phức tạp amortized $\mathcal{O}(1)$ thay vì phải dịch chuyển toàn bộ mảng trong $\mathcal{O}(N)$.

- **C.** Để chuyển đổi sang kiểu `int` nhanh hơn.

- **D.** Bắt buộc theo chuẩn ngôn ngữ C++.

> *Giải thích:* Trong `vector` hoặc `string`, thao tác `push_back()` vào cuối có chi phí trung bình amortized $\mathcal{O}(1)$, trong khi chèn vào đầu tốn $\mathcal{O}(N)$.

#### Câu 2 (Độ phức tạp phép nhân):

Phép nhân hai số nguyên lớn có độ dài lần lượt là $N$ chữ số và $M$ chữ số theo thuật toán đặt tính cơ bản có độ phức tạp thời gian là:

- **A.** $\mathcal{O}(N + M)$

- **B.** $\mathcal{O}(\max(N, M))$

- **C.** **[Đáp án đúng]** $\mathcal{O}(N \times M)$

- **D.** $\mathcal{O}((N + M) \log(N + M))$

> *Giải thích:* Mỗi chữ số của số thứ nhất phải nhân với từng chữ số của số thứ hai qua hai vòng lặp lồng nhau, tạo ra $N \times M$ phép nhân chữ số.

#### Câu 3 (Độ dài tối đa kết quả phép nhân):

Tích của một số nguyên dương có $N$ chữ số và một số nguyên dương có $M$ chữ số có độ dài tối đa là bao nhiêu chữ số

- **A.** $N \times M$

- **B.** $\max(N, M) + 1$

- **C.** **[Đáp án đúng]** $N + M$

- **D.** $N + M - 1$

> *Giải thích:* Giá trị lớn nhất là $(10^N - 1)(10^M - 1) < 10^{N+M}$, do đó số chữ số tối đa luôn là $N + M$.

#### Câu 4 (Xử lý số 0 vô nghĩa):

Sau khi thực hiện phép trừ số lớn $10005 - 10000$, chuỗi kết quả thu được là `"00005"`. Thao tác nào sau đây xử lý đúng để kết quả trở thành `"5"`

- **A.** Gán chuỗi bằng `"5"`.

- **B.** **[Đáp án đúng]** Xóa các ký tự `'0'` ở đầu cho đến khi gặp ký tự khác `'0'` hoặc chuỗi chỉ còn đúng 1 ký tự `'0'`.

- **C.** Xóa toàn bộ ký tự `'0'` trong chuỗi.

- **D.** Đảo ngược chuỗi 2 lần.

> *Giải thích:* Ta phải giữ lại ít nhất 1 chữ số trong trường hợp kết quả phép trừ bằng $0$ (ví dụ $5 - 5 = 0$).

#### Câu 5 (Phép chia số lớn cho số nhỏ):

Khi thực hiện phép chia một số lớn $A$ (có $N$ chữ số) cho một số nguyên $b$ ($1 \le b \le 10^9$), ta duyệt các chữ số của $A$ theo thứ tự nào

- **A.** Từ hàng đơn vị lên hàng cao nhất (từ phải sang trái).

- **B.** **[Đáp án đúng]** Từ hàng cao nhất xuống hàng đơn vị (từ trái sang phải), duy trì số dư tích lũy $cur = cur * 10 + digit$.

- **C.** Duyệt từ giữa chuỗi sang hai bên.

- **D.** Thứ tự nào cũng cho kết quả như nhau.

> *Giải thích:* Phép chia mô phỏng đúng quy tắc đặt tính chia của toán học: chia từ hàng cao nhất xuống hàng thấp nhất.

#### Câu 6 (Trường hợp phép trừ số âm):

Nếu cần tính hiệu $A - B$ của hai số nguyên dương lớn nhưng chưa biết số nào lớn hơn, giải thuật chuẩn xác là gì

- **A.** Vẫn thực hiện phép trừ bình thường $A - B$.

- **B.** **[Đáp án đúng]** So sánh $A$ và $B$. Nếu $A \ge B$ thì tính $A - B$. Nếu $A < B$ thì tính $B - A$ rồi thêm dấu trừ `"-"` vào đầu kết quả.

- **C.** Báo lỗi không tính được.

- **D.** Lấy trị tuyệt đối của từng chữ số rồi trừ nhau.

> *Giải thích:* Phép trừ số lớn trên mảng chỉ đúng khi số bị trừ lớn hơn hoặc bằng số trừ. Khi $A < B$, ta quy về $-(B - A)$.

#### Câu 7 (Tối ưu Base $10^9$):

Thay vì lưu mỗi phần tử trong mảng là $1$ chữ số thập phân (Base 10), việc gom 9 chữ số thập phân vào 1 số nguyên 32-bit (Base $10^9$) mang lại lợi ích gì về mặt thuật toán

- **A.** Giảm dung lượng bộ nhớ mảng đi khoảng 9 lần.

- **B.** Giảm số lượng phép tính của phép cộng/trừ đi khoảng 9 lần.

- **C.** Với phép nhân đặt tính, số cặp chunk cần xử lý giảm xấp xỉ $9^2 = 81$ lần.

- **D.** **[Đáp án đúng]** Cả A, B, C đều đúng.

> *Giải thích:* Base $10^9$ nén dữ liệu giúp giảm cả dung lượng bộ nhớ và số lượng phép toán chunk, giúp code BigInt chạy nhanh hơn rất nhiều trong các bài toán $N \le 10^5$.

#### Câu 8 (Giai thừa số lớn $1000!$):

Để tính chính xác $1000!$ mà không bị tràn số trong C++, ta áp dụng phương pháp nào

- **A.** Dùng kiểu dữ liệu `double`.

- **B.** Dùng kiểu dữ liệu `__int128`.

- **C.** **[Đáp án đúng]** Khởi tạo `string ans = "1"`, sau đó thực hiện vòng lặp nhân lần lượt với các số từ $2$ đến $1000$ bằng hàm nhân số lớn với số nhỏ.

- **D.** Dùng công thức xấp xỉ Stirling.

> *Giải thích:* $1000!$ có 2568 chữ số, vượt xa kiểu `__int128` (khoảng 38 chữ số), bắt buộc phải dùng phép nhân số lớn.

#### Câu 9 (Lũy thừa số lớn $A^B$):

Khi cần tính $A^B$ với `A = 2` và `B = 10000` (kết quả chính xác không lấy dư), phương pháp tối ưu là:

- **A.** Nhân 2 liên tiếp 10000 lần.

- **B.** **[Đáp án đúng]** Kết hợp thuật toán Lũy thừa nhị phân $\mathcal{O}(\log B)$ với phép nhân 2 số nguyên lớn.

- **C.** Dùng hàm `pow(2, 10000)` trong thư viện `<cmath>`.

- **D.** Chuyển sang hệ nhị phân rồi in ra.

> *Giải thích:* Lũy thừa nhị phân chỉ cần thực hiện $\approx 14$ phép nhân số lớn thay vì 10000 phép nhân.

#### Câu 10 (So sánh hai số lớn dạng chuỗi):

Điều kiện nào sau đây quyết định chắc chắn số nguyên dương lớn $A$ lớn hơn số nguyên dương lớn $B$ (giả sử cả $A$ và $B$ không có số 0 vô nghĩa ở đầu)

- **A.** Ký tự đầu tiên của $A$ lớn hơn ký tự đầu tiên của $B$.

- **B.** **[Đáp án đúng]** Độ dài chuỗi $|A| > |B|$, hoặc nếu $|A| == |B|$ thì $A > B$ theo thứ tự từ điển.

- **C.** Tổng các chữ số của $A$ lớn hơn tổng các chữ số của $B$.

- **D.** Chữ số tận cùng của $A$ lớn hơn chữ số tận cùng của $B$.

> *Giải thích:* Số có nhiều chữ số hơn luôn lớn hơn. Khi cùng số chữ số, so sánh từ điển từ trái sang phải phản ánh đúng thứ tự so sánh từ hàng cao nhất xuống hàng thấp nhất.

## Ma trận bài tập thực hành (P0 → P5)

### Ghi chú:
**Phân tầng lộ trình học tập:**

> * **Nhóm Cốt Lõi (Core Foundations - Bắt buộc `CPPB-BIG-01` $\to$ `12`):** Mô hình biểu diễn, So sánh, 4 phép tính cơ bản (+, -, *, /), Giai thừa, Lũy thừa, Fibonacci và Tổng chữ số.
> * **Nhóm Thử Thách Mở Rộng (Advanced / Challenge `CPPB-BIG-13` $\to$ `16`):** Chia hai số lớn, Căn bậc hai số lớn, Binary GCD và Tổ hợp chính xác kết hợp phân tích nguyên tố.

| STT | Mã Bài | Tên Bài Toán | Cấp Độ | Phân Loại | Dạng Thuật Toán & Kỹ Năng Cốt Lõi |
|:---:|:---:|---|:---:|:---:|---|
| 01 | `CPPB-BIG-01` | **So Sánh Hai Số Nguyên Lớn** | `P0` | **Core** | So sánh độ dài và so sánh từ điển chuỗi số |
| 02 | `CPPB-BIG-02` | **Cộng Hai Số Nguyên Lớn ($A + B$)** | `P0` | **Core** | Mô phỏng phép cộng đặt tính và xử lý biến nhớ `carry` |
| 03 | `CPPB-BIG-03` | **Trừ Hai Số Nguyên Lớn ($A - B$)** | `P1` | **Core** | Phép trừ có mượn $A \ge B$ và xóa số 0 vô nghĩa |
| 04 | `CPPB-BIG-04` | **Trừ Hai Số Lớn Tổng Quát (Có Âm)** | `P1` | **Core** | So sánh và gắn dấu `"-"` khi $A < B$ |
| 05 | `CPPB-BIG-05` | **Nhân Số Lớn Với Số Nhỏ ($A \times b$)** | `P1` | **Core** | Nhân từng chữ số với $b \le 10^9$ |
| 06 | `CPPB-BIG-06` | **Nhân Hai Số Nguyên Lớn ($A \times B$)** | `P2` | **Core** | Thuật toán nhân chập và normalize $\mathcal{O}(L_A \times L_B)$ |
| 07 | `CPPB-BIG-07` | **Chia Số Lớn Cho Số Nhỏ ($A / b$)** | `P2` | **Core** | Chia từ hàng cao xuống thấp và lấy thương nguyên |
| 08 | `CPPB-BIG-08` | **Chia Lấy Dư Số Lớn Cho Số Nhỏ ($A \pmod b$)** | `P2` | **Core** | Duy trì số dư `cur = (cur * 10 + digit) % b` |
| 09 | `CPPB-BIG-09` | **Tính Giai Thừa Số Lớn ($N!$)** | `P3` | **Core** | Tính chính xác $N!$ với $N \le 1000$ |
| 10 | `CPPB-BIG-10` | **Lũy Thừa Số Lớn Chính Xác ($A^B$)** | `P3` | **Core** | Lũy thừa nhị phân kết hợp nhân số lớn |
| 11 | `CPPB-BIG-11` | **Số Fibonacci Lớn Thứ $N$** | `P3` | **Core** | Tính chính xác $F_N$ với $N \le 1000$ bằng cộng số lớn |
| 12 | `CPPB-BIG-12` | **Tổng Các Chữ Số Của $N!$ hoặc $2^N$** | `P3` | **Core** | Tính số lớn và tính tổng chữ số |
| 13 | `CPPB-BIG-13` | **Chia Hai Số Nguyên Lớn ($A / B$)** | `P4` | *Advanced* | Tìm thương nguyên bằng tìm kiếm nhị phân hoặc Long Division |
| 14 | `CPPB-BIG-14` | **Căn Bậc Hai Số Nguyên Lớn ($\lfloor \sqrt{A} \rfloor$)** | `P4` | *Advanced* | Tìm kiếm nhị phân trên không gian chuỗi kết hợp nhân BigInt |
| 15 | `CPPB-BIG-15` | **Ước Chung Lớn Nhất Số Lớn ($\gcd(A, B)$)** | `P4` | *Challenge* | Thuật toán Stein's Binary GCD kết hợp phép chia 2 và trừ BigInt |
| 16 | `CPPB-BIG-16` | **Số Lớn Cực Hạn: Tổ Hợp $C(N, K)$ Chính Xác** | `P5` | *Challenge* | Tối ưu hóa: Phân tích thừa số nguyên tố kết hợp nhân lũy thừa số lớn (hoặc DP Pascal BigInt) |
