# PHÉP TOÁN BIT & BIỂU DIỄN TRẠNG THÁI
## Tối Ưu Hóa Cấp Độ Thanh Ghi & Kỹ Thuật Mặt Nạ Bit (Bitmask) Trong C++

---

## 1. Khái Niệm & 6 Phép Toán Bit Cơ Bản

Máy tính biểu diễn tất cả dữ liệu dưới dạng chuỗi nhị phân (gồm các bit $0$ và $1$). **Phép toán bit (Bitwise Operations)** là các thao tác tác động trực tiếp lên từng bit của thanh ghi CPU, đạt tốc độ thực thi nhanh nhất trong mọi câu lệnh phần mềm.

### 1.1. Bảng chân trị của 6 phép toán bit trong C++

| Toán Tử C++ | Tên Phép Toán | Ký Hiệu Toán | Quy Tắc Bit | Ví Dụ ($a = 5 = 101_2, b = 3 = 011_2$) |
|:---:|---|:---:|---|---|
| `&` | **AND** (Và) | $\wedge$ | Ra $1$ khi và chỉ khi cả 2 bit đều là $1$ | $5 \ \& \ 3 = 101_2 \ \& \ 011_2 = 001_2 = 1$ |
| `|` | **OR** (Hoặc) | $\vee$ | Ra $1$ khi có ít nhất một bit là $1$ | $5 \ \| \ 3 = 101_2 \ \| \ 011_2 = 111_2 = 7$ |
| `^` | **XOR** (Hoặc loại trừ) | $\oplus$ | Ra $1$ khi 2 bit khác nhau, ra $0$ khi 2 bit giống nhau | $5 \ \hat{} \ 3 = 101_2 \ \hat{} \ 011_2 = 110_2 = 6$ |
| `~` | **NOT** (Đảo bit) | $\neg$ | Đổi $0 \to 1$ và $1 \to 0$ | $\sim 5 = \sim(00\dots0101_2) = -6$ |
| `<<` | **Dịch trái** (Left Shift) | $\ll$ | Dịch các bit sang trái $k$ vị trí (nhân $2^k$) | $5 \ll 2 = 10100_2 = 20$ |
| `>>` | **Dịch phải** (Right Shift) | $\gg$ | Dịch các bit sang phải $k$ vị trí (chia nguyên $2^k$) | $5 \gg 1 = 10_2 = 2$ |

---

### 1.2. Các tính chất đại số quan trọng của phép XOR ($\oplus$)
* Tính tự triệt tiêu: $A \oplus A = 0$.
* Phần tử trung hòa: $A \oplus 0 = A$.
* Giao hoán & Kết hợp: $A \oplus B = B \oplus A$ và $(A \oplus B) \oplus C = A \oplus (B \oplus C)$.
* Đổi giá trị 2 biến không cần biến phụ: `a ^= b; b ^= a; a ^= b;`.

---

## 2. 4 Thao Tác Thao Tác Bit Chuẩn Thi Đấu

Quy ước đánh số các bit từ phải sang trái, bắt đầu từ bit $0$ (bit có trọng số nhỏ nhất $2^0$).

### 2.1. Kiểm tra bit thứ $k$ có đang bật (bằng 1) hay không:
```cpp
bool is_set = (mask >> k) & 1;
// Hoặc: bool is_set = (mask & (1LL << k)) != 0;
```

### 2.2. Bật bit thứ $k$ (gán thành 1):
```cpp
mask = mask | (1LL << k);
// Viết gọn: mask |= (1LL << k);
```

### 2.3. Tắt bit thứ $k$ (gán thành 0):
```cpp
mask = mask & ~(1LL << k);
// Viết gọn: mask &= ~(1LL << k);
```

### 2.4. Đảo bit thứ $k$ ($0 \to 1, 1 \to 0$):
```cpp
mask = mask ^ (1LL << k);
// Viết gọn: mask ^= (1LL << k);
```

#### 💡 Ví Dụ Minh Họa 1: Thao tác trên số $N = 13 = 1101_2$

| Trọng số nhị phân | $2^4 = 16$ | $2^3 = 8$ | $2^2 = 4$ | $2^1 = 2$ | $2^0 = 1$ | Giá trị thập phân |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
| **Vị trí bit ($k$)** | Bit 4 | Bit 3 | Bit 2 | Bit 1 | Bit 0 | — |
| **Giá trị bit của $N$** | `0` | `1` | `1` | `0` | `1` | **$13$** |

**Bảng mô phỏng 4 thao tác bit:**

| Thao Tác Cần Thực Hiện | Mã Lệnh C++ | Phép Toán Nhị Phân | Kết Quả Nhị Phân | Giá Trị Thập Phân Mới |
|---|---|---|:---:|:---:|
| **1. Kiểm tra bit 2** | `(n >> 2) & 1` | `(1101 >> 2) & 0001 = 0011 & 0001` | `1` | Bit 2 đang bật (`true`) |
| **2. Bật bit 1** | `n |= (1 << 1)` | `1101 | 0010` | `1111` | $13 \to \mathbf{15}$ |
| **3. Tắt bit 3** | `n &= ~(1 << 3)` | `1101 & ~(1000) = 1101 & 0111` | `0101` | $13 \to \mathbf{5}$ |
| **4. Đảo bit 0** | `n ^= (1 << 0)` | `1101 ^ 0001` | `1100` | $13 \to \mathbf{12}$ |

---

## 3. Các Tuyệt Kỹ Bit & Hàm Nội Tại CPU (Builtin Functions)

### 3.1. Kiểm tra một số nguyên dương có phải là lũy thừa của 2
Một số $N > 0$ là lũy thừa của 2 ($2^k$) khi và chỉ khi trong biểu diễn nhị phân của nó có **đúng duy nhất một bit 1**:
```cpp
bool is_power_of_two = (n > 0) && ((n & (n - 1)) == 0);
```

### 3.2. Lấy bit 1 nhỏ nhất (Lowest Set Bit / Lowbit)
Dùng trong cấu trúc Fenwick Tree và giải thuật bit:
```cpp
long long lowbit = x & (-x);
```

### 3.3. Các hàm nội tại tối ưu hóa phần cứng trong GCC/Clang:
* `__builtin_popcount(unsigned int x)` / `__builtin_popcountll(unsigned long long x)`: Đếm số lượng bit 1 trong $\mathcal{O}(1)$ chu kỳ CPU.
* `__builtin_clz(x)` / `__builtin_clzll(x)`: Đếm số lượng bit 0 liên tiếp ở đầu (Count Leading Zeros).
* `__builtin_ctz(x)` / `__builtin_ctzll(x)`: Đếm số lượng bit 0 liên tiếp ở cuối (Count Trailing Zeros).

---

## 4. Kỹ Thuật Mặt Nạ Bit (Bitmask & Subset Enumeration)

Mặt nạ bit (**Bitmask**) là kỹ thuật dùng một số nguyên $N$ bit để biểu diễn một tập hợp con gồm các phần tử được chọn từ tập $N$ phần tử:
* Bit thứ $i = 1 \implies$ Phần tử thứ $i$ được chọn.
* Bit thứ $i = 0 \implies$ Phần tử thứ $i$ không được chọn.

### 4.1. Duyệt toàn bộ $2^N$ tập con (Vét cạn nhị phân):
```cpp
int n = 4;
for (int mask = 0; mask < (1 << n); ++mask) {
    for (int i = 0; i < n; ++i) {
        if ((mask >> i) & 1) {
            // Phần tử i thuộc tập con hiện tại
        }
    }
}
```

### 4.2. Duyệt tất cả tập con (submasks) của một mask trong $\mathcal{O}(3^N)$:
```cpp
for (int sub = mask; sub > 0; sub = (sub - 1) & mask) {
    // sub là một tập con hợp lệ của mask
}
```

#### 💡 Ví Dụ Minh Họa 2: Biểu diễn tập con của tập 3 phần tử $S = \{A_0, A_1, A_2\}$
Với $N = 3$, có $2^3 = 8$ mặt nạ bit từ $0$ đến $7$:

| Giá Trị Mask (Thập phân) | Biểu Diễn Nhị Phân ($b_2 b_1 b_0$) | Bit $2$ ($A_2$) | Bit $1$ ($A_1$) | Bit $0$ ($A_0$) | Tập Con Tương Ứng |
|:---:|:---:|:---:|:---:|:---:|---|
| **0** | `000` | $0$ | $0$ | $0$ | $\emptyset$ (Tập rỗng) |
| **1** | `001` | $0$ | $0$ | $1$ | $\{A_0\}$ |
| **2** | `010` | $0$ | $1$ | $0$ | $\{A_1\}$ |
| **3** | `011` | $0$ | $1$ | $1$ | $\{A_0, A_1\}$ |
| **4** | `100` | $1$ | $0$ | $0$ | $\{A_2\}$ |
| **5** | `101` | $1$ | $0$ | $1$ | $\{A_0, A_2\}$ |
| **6** | `110` | $1$ | $1$ | $0$ | $\{A_1, A_2\}$ |
| **7** | `111` | $1$ | $1$ | $1$ | $\{A_0, A_1, A_2\}$ (Tập đầy đủ) |

---

## 5. Mẫu Cài Đặt Chuẩn Thi Đấu (Competitive Template)

### Mẫu 1: Vét Cạn Tập Con Bằng Mặt Nạ Bit (Subset Sum)

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long target_s;
    if (!(cin >> n >> target_s)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    bool found = false;
    int total_masks = (1 << n);

    for (int mask = 0; mask < total_masks; ++mask) {
        long long current_sum = 0;
        for (int i = 0; i < n; ++i) {
            if ((mask >> i) & 1) {
                current_sum += a[i];
            }
        }
        if (current_sum == target_s) {
            found = true;
            break;
        }
    }

    cout << (found ? "YES\n" : "NO\n");
    return 0;
}
```

---

## 6. Các Bẫy Lỗi Lập Trình Kinh Điển (Bug Traps)

1. **Bẫy thứ tự ưu tiên toán tử (Operator Precedence Bug):** Trong C++, các phép toán bit `&`, `|`, `^` có độ ưu tiên **thấp hơn** các phép toán so sánh `==`, `!=`, `<`, `>`.
   * ❌ Lỗi sai: `if (mask & (1 << k) != 0)` sẽ bị hiểu thành `if (mask & ((1 << k) != 0))` $\implies$ Sai kết quả!
   * ✅ Cú pháp chuẩn: `if ((mask & (1 << k)) != 0)` hoặc `if ((mask >> k) & 1)`.
2. **Bẫy tràn số khi dịch bit quá 31:** Hằng số `1` mặc định là số nguyên 32-bit có dấu. Biểu thức `1 << 40` sẽ gây tràn số và lỗi hành vi không xác định (Undefined Behavior).
   * ✅ Quy tắc bắt buộc: Luôn viết `1LL << k` khi $k \ge 31$.

---

## 7. Ranh Giới Áp Dụng: Khi Nào Nên & Không Nên Dùng?

* **KHI NÀO ÁP DỤNG:**
  * Kích thước tập hợp nhỏ: $N \le 20$ ($2^{20} \approx 10^6$ phép tính) hoặc $N \le 24$ ($2^{24} \approx 1.6 \cdot 10^7$ phép tính).
  * Cần tối ưu bộ nhớ trạng thái và tốc độ truy vấn tập hợp $\mathcal{O}(1)$.
* **KHI NÀO THẤT BẠI:**
  * Khi $N \ge 30$ ($2^{30} \approx 10^9$ phép tính $\implies$ TLE). Lúc này bắt buộc phải dùng:
    * **Chia đôi tập hợp (Meet-in-the-middle)** khi $N \le 40$ ($\mathcal{O}(2^{N/2}) = 2^{20} \approx 10^6$).
    * Quy hoạch động hoặc Thuật toán Tham lam nếu bài toán có cấu trúc con tối ưu.

---

# CÂU HỎI TRẮC NGHIỆM ĐO LƯỜNG TƯ DUY (CONCEPT QUIZ)

#### Câu 1 (Bản chất XOR — Identity):
Giá trị của biểu thức $A \oplus B \oplus A$ trong C++ luôn bằng gì?
* A. 0
* B. $A$
* C. **(Đáp án đúng)** $B$ (vì $A \oplus A = 0$ và $0 \oplus B = B$).
* D. $2A + B$
> *Giải thích:* Tính chất giao hoán và tự triệt tiêu của phép XOR: $A \oplus B \oplus A = (A \oplus A) \oplus B = 0 \oplus B = B$.

---

#### Câu 2 (Bẫy độ ưu tiên toán tử — Precedence):
Đoạn mã C++ `if ((mask >> 3) & 1)` có ý nghĩa là gì?
* A. Dịch biến `mask` sang phải 4 vị trí.
* B. **(Đáp án đúng)** Kiểm tra xem bit thứ 3 của `mask` có đang được bật (bằng 1) hay không.
* C. Bật bit thứ 3 của `mask` lên 1.
* D. Tắt bit thứ 3 của `mask`.
> *Giải thích:* Dịch phải 3 vị trí đưa bit thứ 3 về vị trí số 0, sau đó `& 1` sẽ trích xuất đúng giá trị của bit này (0 hoặc 1).

---

#### Câu 3 (Kỹ thuật bật bit — Manipulation):
Để bật bit thứ $k$ của biến số nguyên `mask` lên 1 mà không làm thay đổi các bit khác, ta dùng câu lệnh nào?
* A. `mask = mask & (1LL << k);`
* B. **(Đáp án đúng)** `mask = mask | (1LL << k);`
* C. `mask = mask ^ (1LL << k);`
* D. `mask = mask + (1LL << k);`
> *Giải thích:* Phép OR với số có bit thứ $k$ bằng 1 và các bit khác bằng 0 sẽ biến bit thứ $k$ thành 1 mà giữ nguyên các bit còn lại.

---

#### Câu 4 (Kỹ thuật tắt bit — Manipulation):
Để tắt bit thứ $k$ của biến số nguyên `mask` về 0, ta dùng câu lệnh nào?
* A. `mask = mask | ~(1LL << k);`
* B. `mask = mask - (1LL << k);`
* C. **(Đáp án đúng)** `mask = mask & ~(1LL << k);`
* D. `mask = mask ^ (1LL << k);`
> *Giải thích:* `~(1LL << k)` tạo ra một mặt nạ chứa toàn bit 1 ngoại trừ bit $k$ bằng 0. Khi `&` với mask, bit thứ $k$ chắc chắn về 0.

---

#### Câu 5 (Lũy thừa của 2 — Bit Trick):
Biểu thức `n > 0 && (n & (n - 1)) == 0` trả về `true` khi và chỉ khi:
* A. $n$ là một số nguyên chẵn.
* B. **(Đáp án đúng)** $n$ là một lũy thừa của 2 ($n = 2^k$ với $k \ge 0$).
* C. $n$ là một số nguyên tố.
* D. $n$ chia hết cho 4.
> *Giải thích:* Một lũy thừa của 2 có dạng $100\dots0_2$, khi trừ 1 sẽ thành $011\dots1_2$. Phép AND giữa hai số này bằng đúng 0.

---

#### Câu 6 (Đếm bit 1 — Builtin):
Để đếm số lượng bit 1 của một số nguyên 64-bit `long long x` trong thời gian $\mathcal{O}(1)$, hàm nào sau đây là chuẩn xác nhất?
* A. `__builtin_popcount(x)`
* B. **(Đáp án đúng)** `__builtin_popcountll(x)`
* C. `__builtin_ctzll(x)`
* D. `__builtin_clzll(x)`
> *Giải thích:* Với kiểu `long long` 64-bit, bắt buộc phải dùng phiên bản có hậu tố `ll` là `__builtin_popcountll`. Phiên bản không có `ll` chỉ đếm 32 bit thấp.

---

#### Câu 7 (Không gian tập con — Complexity):
Một tập hợp có $N = 20$ phần tử. Số lượng tập con được sinh ra bởi mặt nạ bit là bao nhiêu và thời gian duyệt vét cạn có chạy kịp $1$ giây không?
* A. $20^2 = 400$ tập con, chạy kịp.
* B. **(Đáp án đúng)** $2^{20} = 1,048,576$ tập con, chạy mất khoảng $0.01$ giây, hoàn toàn kịp thời gian $1$ giây.
* C. $20! \approx 2.4 \times 10^{18}$ tập con, bị quá thời gian.
* D. $2^{20} \approx 10^9$ tập con, bị quá thời gian.
> *Giải thích:* Mỗi phần tử có 2 lựa chọn (chọn hoặc không) $\implies 2^{20} \approx 1.05 \times 10^6$ trạng thái. Vòng lặp $10^6$ chạy dưới $0.02$ giây trong C++.

---

#### Câu 8 (Tìm phần tử đơn lẻ — XOR Application):
Cho mảng gồm $2N + 1$ số nguyên, trong đó có đúng một số xuất hiện 1 lần, tất cả các số còn lại đều xuất hiện đúng 2 lần. Thuật toán tìm số xuất hiện 1 lần tối ưu nhất là gì?
* A. Dùng 2 vòng lặp lồng nhau $\mathcal{O}(N^2)$.
* B. Sắp xếp mảng mất $\mathcal{O}(N \log N)$.
* C. **(Đáp án đúng)** Tính XOR tất cả các phần tử trong mảng trong $\mathcal{O}(N)$ thời gian và $\mathcal{O}(1)$ bộ nhớ.
* D. Dùng bảng băm đếm tần suất.
> *Giải thích:* Các cặp số giống nhau khi XOR với nhau sẽ triệt tiêu về 0 ($x \oplus x = 0$). Kết quả XOR của toàn bộ mảng chính là số xuất hiện 1 lần duy nhất.

---

#### Câu 9 (Bẫy dịch bit 64-bit — 64-bit Shift):
Đoạn code `long long mask = 1 << 40;` sẽ gây ra lỗi gì trong C++?
* A. Lỗi biên dịch không thể dịch bit.
* B. **(Đáp án đúng)** Tràn số nguyên 32-bit (vì số `1` mặc định là `int`), dẫn đến kết quả sai hoặc hành vi không xác định (Undefined Behavior).
* C. Lỗi tràn bộ nhớ RAM.
* D. Tự động ép kiểu thành 64-bit mà không có lỗi gì.
> *Giải thích:* Hằng số `1` mang kiểu `int` 32-bit, không thể dịch 40 vị trí. Bắt buộc phải viết `1LL << 40`.

---

#### Câu 10 (Duyệt Submask — Advanced Technique):
Vòng lặp `for (int sub = mask; sub > 0; sub = (sub - 1) & mask)` dùng để làm gì?
* A. Duyệt tất cả các số từ `mask` về 1.
* B. **(Đáp án đúng)** Duyệt chính xác và đầy đủ tất cả các tập con thực sự (Submasks) của `mask` mà không duyệt thừa bất kỳ trạng thái nào khác.
* C. Xóa tất cả các bit 1 của `mask`.
* D. Đếm số lượng bit 0 của `mask`.
> *Giải thích:* Đây là kỹ thuật kinh điển trong quy hoạch động Bitmask để sinh tất cả các tập con của một mặt nạ bit trong $\mathcal{O}(3^N)$ tổng thời gian cho toàn bộ các mask.

---

#### Câu 11 (Cặp tổng lũy thừa của 2 — Power of 2 Pairs):
Cho $A_i \le 10^9$. Để đếm số cặp $A_i + A_j = 2^k$, tại sao ta chỉ cần lặp tối đa $k$ từ $1$ đến $30$?
* A. Vì kiểu `long long` trong C++ chỉ biểu diễn được 30 bit.
* B. **(Đáp án đúng)** Vì giá trị tổng lớn nhất của hai số là $10^9 + 10^9 = 2 \cdot 10^9 < 2^{31}$, do đó chỉ có tối đa 30 lũy thừa của 2 khả dĩ.
* C. Vì số 30 là số nguyên tố.
* D. Do thuật toán chỉ kiểm tra các số chẵn.
> *Giải thích:* $A_i + A_j \le 2 \cdot 10^9 < 2^{31} \approx 2.147 \cdot 10^9$. Do đó $k$ chỉ có thể nhận các giá trị từ $1 \dots 30$.

---

#### Câu 12 (Tập độc lập về bit — Bit Independence):
Hai số nguyên dương $X$ và $Y$ được gọi là độc lập về bit khi biểu thức nào sau đây bằng 0?
* A. $X \oplus Y == 0$.
* B. **(Đáp án đúng)** $X \ \& \ Y == 0$ (hai số không có bất kỳ bit 1 nào nằm ở cùng vị trí).
* C. $X \ | \ Y == 0$.
* D. $X + Y == 0$.
> *Giải thích:* Phép AND kiểm tra các bit trùng nhau. $X \ \& \ Y == 0 \iff$ không có vị trí bit nào mà cả $X$ và $Y$ cùng bằng 1.

---

# DANH SÁCH BÀI TẬP THỰC HÀNH

| STT | Mã Bài | Tên Bài Toán | Cấp Độ | Ràng Buộc Dữ Liệu | Mục Tiêu Rèn Luyện |
|:---:|:---:|---|:---:|---|---|
| 01 | `CPPB-BIT-01` | **Bật, Tắt Và Kiểm Tra Bit Thứ K** | `P0` | $N \le 10^{18}, K \le 60$ | Thao tác `(1LL << k)`, `&`, `|`, `^` |
| 02 | `CPPB-BIT-02` | **Đếm Số Lượng Bit 1 (Popcount)** | `P1` | $N \le 10^{18}$ | `__builtin_popcountll` và thuật toán bit |
| 03 | `CPPB-BIT-03` | **Kiểm Tra Số Có Phải Lũy Thừa Của 2** | `P1` | $N \le 10^{18}$ | Kỹ thuật `n > 0 && (n & (n - 1)) == 0` |
| 04 | `CPPB-BIT-04` | **Tìm Phần Tử Xuất Hiện 1 Lần Duy Nhất** | `P2` | $N \le 2 \cdot 10^5$ | Tính chất tự triệt tiêu $A \oplus A = 0$ |
| 05 | `CPPB-BIT-05` | **Tìm Hai Số Xuất Hiện 1 Lần Duy Nhất** | `P2` | $N \le 2 \cdot 10^5$ | Phân tách nhóm bằng bit khác biệt đầu tiên |
| 06 | `CPPB-BIT-06` | **Đảo Bit Và Giá Trị Bù 1** | `P2` | $N \le 10^9$ | Phép toán NOT kết hợp mặt nạ |
| 07 | `CPPB-BIT-07` | **Duyệt Toàn Bộ $2^N$ Tập Con Bằng Mặt Nạ Bit** | `P2` | $N \le 20$ | `for (int mask = 0; mask < (1 << n); ++mask)` |
| 08 | `CPPB-BIT-08` | **Bài Toán Tổng Tập Con Bằng S (Subset Sum)** | `P3` | $N \le 20, S \le 10^9$ | Duyệt nhị phân vét cạn $2^N$ |
| 09 | `CPPB-BIT-09` | **Chia Tập Hợp Thành 2 Phần Có Tổng Chênh Lệch Nhỏ Nhất** | `P3` | $N \le 20$ | Vét cạn bitmask tối ưu hiệu |
| 10 | `CPPB-BIT-10` | **Đếm Cặp Có Tích Bit AND Bằng 0** | `P3` | $N \le 10^5, A_i < 2^{16}$ | Tần suất bit và kiểm tra tương thích |
| 11 | `CPPB-BIT-11` | **Tìm Cặp Có XOR Lớn Nhất Trong Mảng** | `P4` | $N \le 10^5, A_i \le 10^9$ | Duyệt từng bit từ cao xuống thấp (Greedy Bit) |
| 12 | `CPPB-BIT-12` | **Duyệt Tất Cả Các Tập Con Của Một Mặt Nạ Bit** | `P4` | $N \le 18$ | Kỹ thuật `submask = (submask - 1) & mask` |
| 13 | `CPPB-BIT-13` | **Tìm Dãy Con Có Tổng XOR Bằng K** | `P4` | $N \le 22$ | Vét cạn nâng cao kết hợp bit |
| 14 | `CPPB-BIT-14` | **Tối Ưu Hóa Gán Việc Cho N Người (N <= 20)** | `P5` | $N \le 20$ | Bitmask trạng thái và tối ưu hóa tổ hợp |
| 15 | `CPPB-BIT-15` | **Đếm Số Cặp Có Tổng Bằng Lũy Thừa Của 2** | `P3` | $N \le 10^5, A_i \le 10^9$ | Kết hợp bitmask và hai con trỏ / chặt nhị phân |
| 16 | `CPPB-BIT-16` | **Tập Hợp Độc Lập Về Bit Lớn Nhất** | `P4` | $N \le 24$ | Bitmask đồ thị độc lập cực đại |
