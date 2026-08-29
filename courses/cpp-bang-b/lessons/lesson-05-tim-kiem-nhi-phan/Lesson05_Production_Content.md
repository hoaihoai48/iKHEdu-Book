# THUẬT TOÁN TÌM KIẾM NHỊ PHÂN
## Tối Ưu Hóa Không Gian Tìm Kiếm Từ O(N) Xuống O(log N) Trong C++

---

## 1. Khái Niệm & Bản Chất Của Tìm Kiếm Nhị Phân (Binary Search)

**Tìm kiếm nhị phân (Binary Search)** là thuật toán tìm kiếm dựa trên nguyên lý **chia để trị (Divide and Conquer)**. Bằng cách so sánh giá trị cần tìm với phần tử ở chính giữa không gian tìm kiếm, thuật toán loại bỏ chính xác **một nửa không gian tìm kiếm** sau mỗi bước lặp.

### 1.1. Điều kiện tiên quyết (Prerequisite Condition)
Thuật toán tìm kiếm nhị phân **CHỈ HOẠT ĐỘNG ĐƯỢC** khi không gian tìm kiếm hoặc mảng dữ liệu có **tính chất đơn điệu (Monotonicity)**:
* Mảng đã được sắp xếp tăng dần hoặc giảm dần.
* Hoặc một hàm mệnh đề logic $f(x) \in \{\text{True}, \text{False}\}$ thỏa mãn: nếu $f(x_0) = \text{True}$ thì $\forall x \ge x_0, f(x) = \text{True}$ (hoặc ngược lại).

### 1.2. Phân tích độ phức tạp thời gian $\mathcal{O}(\log N)$
Giả sử không gian tìm kiếm ban đầu có kích thước $N$:
* Bước 1: Thu hẹp còn $\frac{N}{2}$.
* Bước 2: Thu hẹp còn $\frac{N}{4} = \frac{N}{2^2}$.
* Bước $k$: Thu hẹp còn $\frac{N}{2^k}$.

Quá trình dừng lại khi kích thước không gian tìm kiếm bằng $1 \implies \frac{N}{2^k} = 1 \iff 2^k = N \iff k = \log_2 N$.
* Với $N = 10^5 \implies \log_2(10^5) \approx 17$ lần thu hẹp không gian.
* Với $N = 10^9 \implies \log_2(10^9) \approx 30$ lần thu hẹp không gian.
* Với $N = 10^{18} \implies \log_2(10^{18}) \approx 60$ lần thu hẹp không gian.

> **Bản chất hiệu năng:** Trên không gian nghiệm lên tới $10^{18}$, thuật toán chỉ cần khoảng **$60$ lần thu hẹp không gian**. Tổng thời gian thực tế của chương trình sẽ bằng:
> $$\text{Total Time} = \mathcal{O}\Big(\log(\text{Range}) \times \text{Complexity}(\text{check})\Big)$$
> Nếu hàm kiểm tra $\text{check}(mid)$ chạy trong $\mathcal{O}(N)$ với $N = 10^5$, chương trình chỉ mất khoảng $60 \times 10^5 = 6 \cdot 10^6$ phép tính (thực thi trong khoảng $0.02$ giây).

---

## 2. Tìm Kiếm Nhị Phân Trên Mảng Đã Sắp Xếp

### 2.1. Tìm chính xác giá trị $X$ (Exact Search)
Khởi tạo hai con trỏ biên: $low = 0, high = N - 1$.
* Tính trung điểm an toàn: $mid = low + \frac{high - low}{2}$.
* Nếu $A[mid] == X \implies$ Tìm thấy tại vị trí $mid$.
* Nếu $A[mid] < X \implies$ Giá trị $X$ chỉ có thể nằm ở nửa phải $\implies low = mid + 1$.
* Nếu $A[mid] > X \implies$ Giá trị $X$ chỉ có thể nằm ở nửa trái $\implies high = mid - 1$.

#### 💡 Ví Dụ Minh Họa 1: Tìm kiếm giá trị $X = 23$
Cho mảng đã sắp xếp gồm 10 phần tử: $A = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]$

| Chỉ số (0-based) | $0$ | $1$ | $2$ | $3$ | $4$ | $5$ | $6$ | $7$ | $8$ | $9$ |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Giá trị mảng $A$** | $2$ | $5$ | $8$ | $12$ | $16$ | $23$ | $38$ | $56$ | $72$ | $91$ |

**Bảng mô phỏng từng bước thu hẹp không gian tìm kiếm:**

| Bước Lặp | $low$ | $high$ | $mid$ | $A[mid]$ | So sánh với $X = 23$ | Quyết định thu hẹp | Không gian còn lại |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|---|
| **Bước 1** | $0$ | $9$ | $4$ | $16$ | $16 < 23$ | Nửa trái $< 23$, dịch $low = 4 + 1 = 5$ | $[23, 38, 56, 72, 91]$ (chỉ số $5..9$) |
| **Bước 2** | $5$ | $9$ | $7$ | $56$ | $56 > 23$ | Nửa phải $> 23$, dịch $high = 7 - 1 = 6$ | $[23, 38]$ (chỉ số $5..6$) |
| **Bước 3** | $5$ | $6$ | $5$ | $23$ | $23 == 23$ | **Tìm thấy $X$ tại chỉ số $5$!** | Kết thúc thuật toán sau **3 bước** |

---

### 2.2. Tìm kiếm phần tử biên: `lower_bound` và `upper_bound`

Trong lập trình thi đấu, dạng toán tìm vị trí biên quan trọng hơn nhiều so với tìm chính xác:

1. **`lower_bound` (Tìm phần tử nhỏ nhất $\ge X$):**
   * Tìm vị trí đầu tiên mà giá trị tại đó $\ge X$.
   * Nếu tất cả các phần tử đều $< X$, trả về vị trí sau phần tử cuối cùng ($N$).
2. **`upper_bound` (Tìm phần tử nhỏ nhất $> X$):**
   * Tìm vị trí đầu tiên mà giá trị tại đó $> X$.
   * Vị trí phần tử lớn nhất $\le X$ chính là `upper_bound - 1`.

#### 💡 Ví Dụ Minh Họa 2: Mảng có phần tử lặp lại
Cho mảng: $A = [1, 3, 5, 5, 5, 8, 12]$, tìm các mốc biên với $X = 5$:

| Chỉ số (0-based) | $0$ | $1$ | $2$ | $3$ | $4$ | $5$ | $6$ |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Giá trị mảng $A$** | $1$ | $3$ | $5$ | $5$ | $5$ | $8$ | $12$ |
| **Vị trí con trỏ STL** | — | — | **`lower_bound(5)`** (chỉ số 2) | — | — | **`upper_bound(5)`** (chỉ số 5) | — |

* `lower_bound(A.begin(), A.end(), 5) - A.begin()` $\implies$ Trả về **chỉ số 2** (số 5 đầu tiên).
* `upper_bound(A.begin(), A.end(), 5) - A.begin()` $\implies$ Trả về **chỉ số 5** (phần tử đầu tiên $> 5$).
* Số lần xuất hiện của số 5: $\text{Count}(5) = \text{upper} - \text{lower} = 5 - 2 = \mathbf{3}$ phần tử.
* Vị trí xuất hiện cuối cùng của số 5: $\text{upper} - 1 = 5 - 1 = \mathbf{4}$.

---

## 3. Kỹ Thuật Chặt Nhị Phân Trên Tập Kết Quả (Binary Search on Answer)

Đây là kỹ thuật cốt lõi trong các kỳ thi học sinh giỏi và Olympic tin học.

### 3.1. Nhận diện tính chất đơn điệu & Phân loại 2 hướng
Trước khi cài đặt, **bắt buộc phải xác định hướng biến thiên đơn điệu** của hàm kiểm tra `check(x)`:

* **Hướng 1: Dạng `True → False` (Tìm giá trị $X$ LỚN NHẤT thỏa mãn):**
  * Đồ thị nghiệm: $[\text{True}, \text{True}, \dots, \text{True}, \mathbf{True_{\text{max}}}, \text{False}, \dots, \text{False}]$.
  * Nếu `check(mid) == true` $\implies$ $mid$ thỏa mãn, ghi nhận `ans = mid` và tìm nghiệm lớn hơn ở bên phải: `low = mid + 1`.
  * Nếu `check(mid) == false` $\implies$ $mid$ quá lớn, thu hẹp về bên trái: `high = mid - 1`.
  * *Ví dụ điển hình:* Cắt gỗ lấy tối thiểu $M$ mét (độ cao cưa càng thấp càng nhiều gỗ $\implies$ tìm độ cao Max).

* **Hướng 2: Dạng `False → True` (Tìm giá trị $X$ NHỎ NHẤT thỏa mãn):**
  * Đồ thị nghiệm: $[\text{False}, \text{False}, \dots, \text{False}, \mathbf{True_{\text{min}}}, \text{True}, \dots, \text{True}]$.
  * Nếu `check(mid) == true` $\implies$ $mid$ thỏa mãn, ghi nhận `ans = mid` và tìm nghiệm nhỏ hơn ở bên trái: `high = mid - 1`.
  * Nếu `check(mid) == false` $\implies$ $mid$ chưa đủ lớn, tăng giá trị lên: `low = mid + 1`.
  * *Ví dụ điển hình:* Vận chuyển hàng trong $D$ ngày (tải trọng thuyền càng lớn càng dễ chở $\implies$ tìm tải trọng Min).

#### 💡 Ví Dụ Minh Họa 3: Bài toán Cắt gỗ lấy tối thiểu $M = 7$ mét gỗ
Cho $N = 4$ cây có chiều cao: $A = [20, 15, 10, 17]$. Cần tìm độ cao máy cưa $H$ **lớn nhất** sao cho tổng lượng gỗ thu được $\ge 7$.

* Không gian tìm kiếm: $low = 0, high = \max(A) = 20$.
* Hàm `check(H)`: Tính tổng $\sum \max(0, A_i - H)$. Nếu $\ge 7 \implies$ `True`, ngược lại `False`.

**Bảng mô phỏng từng bước chặt nhị phân:**

| Bước | $low$ | $high$ | $mid (H)$ | Lượng gỗ cắt được từ từng cây | Tổng gỗ thu được | `check(H) >= 7` | Quyết định cập nhật |
|:---:|:---:|:---:|:---:|---|:---:|:---:|---|
| **1** | $0$ | $20$ | **$10$** | $(20-10) + (15-10) + (0) + (17-10) = 10 + 5 + 0 + 7$ | **$22\text{m}$** | `True` $(\ge 7)$ | Lưu `ans = 10`, thử tăng độ cao: $low = 11$ |
| **2** | $11$ | $20$ | **$15$** | $(20-15) + (0) + (0) + (17-15) = 5 + 0 + 0 + 2$ | **$7\text{m}$** | `True` $(\ge 7)$ | Lưu `ans = 15`, thử tăng độ cao: $low = 16$ |
| **3** | $16$ | $20$ | **$18$** | $(20-18) + (0) + (0) + (0) = 2 + 0 + 0 + 0$ | **$2\text{m}$** | `False` $(< 7)$ | Thiếu gỗ! Phải hạ cưa xuống: $high = 17$ |
| **4** | $16$ | $17$ | **$16$** | $(20-16) + (0) + (0) + (17-16) = 4 + 0 + 0 + 1$ | **$5\text{m}$** | `False` $(< 7)$ | Thiếu gỗ! Phải hạ cưa xuống: $high = 15$ |
| **Dừng** | $16$ | $15$ | — | $low > high \implies$ Thuật toán kết thúc | — | — | **Đáp án tối ưu: $H = 15$** |

---

## 4. Chặt Nhị Phân Trên Tập Số Thực (Real-Number Binary Search)

Khi đề bài yêu cầu tìm nghiệm thực với độ chính xác sai số tuyệt đối $\le 10^{-6}$:
* **Vấn đề của điều kiện `while (high - low > 1e-7)`:** Khi khoảng cách giữa $low$ và $high$ đạt tới giới hạn độ phân giải của kiểu `double` (bit mantissa), phép tính trung điểm `mid = (low + high) / 2.0` có thể bị làm tròn thành đúng $low$ hoặc $high$, khiến hiệu số $high - low$ không thể thu hẹp thêm, dẫn đến nguy cơ vòng lặp không tiến triển hoặc chạy vô hạn.
* **Giải pháp chuẩn thi đấu:** Sử dụng vòng lặp với **số lần lặp cố định** ($60 \dots 100$ lần):
  $$\text{Độ thu hẹp} = \frac{\text{high} - \text{low}}{2^{100}} \approx \frac{10^9}{1.26 \times 10^{30}} \approx 10^{-21} \ll 10^{-6}$$
  Đảm bảo thuật toán luôn dừng đúng số bước, an toàn tuyệt đối và đạt độ chính xác tối đa của phần cứng.

---

## 5. Mẫu Cài Đặt Chuẩn Thi Đấu (Competitive Templates)

### Mẫu 1A: Tìm Giá Trị LỚN NHẤT Thỏa Mãn (Dạng `True -> False`)

```cpp
#include <bits/stdc++.h>
using namespace std;

// Hàm kiểm tra: Lượng gỗ thu được khi cưa ở độ cao mid có >= M hay không?
bool check(long long mid, const vector<long long>& a, long long m) {
    long long wood = 0;
    for (long long x : a) {
        if (x > mid) wood += (x - mid);
    }
    return wood >= m;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long m;
    if (!(cin >> n >> m)) return 0;

    vector<long long> a(n);
    long long max_val = 0;
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        max_val = max(max_val, a[i]);
    }

    long long low = 0, high = max_val;
    long long ans = 0;

    while (low <= high) {
        long long mid = low + (high - low) / 2;
        if (check(mid, a, m)) {
            ans = mid;        // Ghi nhận nghiệm hợp lệ
            low = mid + 1;    // Tìm giá trị lớn hơn ở bên phải
        } else {
            high = mid - 1;   // Không thỏa mãn, thu hẹp về bên trái
        }
    }

    cout << ans << "\n";
    return 0;
}
```

### Mẫu 1B: Tìm Giá Trị NHỎ NHẤT Thỏa Mãn (Dạng `False -> True`)

```cpp
#include <bits/stdc++.h>
using namespace std;

// Hàm kiểm tra: Với tải trọng phà là mid, có chở hết hàng trong <= D ngày hay không?
bool check(long long mid, const vector<long long>& w, int d) {
    int days = 1;
    long long current_load = 0;
    for (long long x : w) {
        if (current_load + x > mid) {
            days++;
            current_load = x;
        } else {
            current_load += x;
        }
    }
    return days <= d;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, d;
    if (!(cin >> n >> d)) return 0;

    vector<long long> w(n);
    long long max_w = 0, sum_w = 0;
    for (int i = 0; i < n; ++i) {
        cin >> w[i];
        max_w = max(max_w, w[i]);
        sum_w += w[i];
    }

    // Không gian tìm kiếm: Tải trọng tối thiểu phải chở được kiện nặng nhất
    long long low = max_w, high = sum_w;
    long long ans = sum_w;

    while (low <= high) {
        long long mid = low + (high - low) / 2;
        if (check(mid, w, d)) {
            ans = mid;        // Ghi nhận nghiệm hợp lệ
            high = mid - 1;   // Tìm giá trị nhỏ hơn ở bên trái
        } else {
            low = mid + 1;    // Tải trọng chưa đủ, phải tăng lên
        }
    }

    cout << ans << "\n";
    return 0;
}
```

### Mẫu 2: Binary Search Số Thực (100 Vòng Lặp Robust)

```cpp
#include <bits/stdc++.h>
using namespace std;

bool check_real(double mid) {
    return (mid * mid * mid + 2.0 * mid * mid + 10.0 * mid >= 100.0);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    double low = 0.0, high = 1e9;

    // Lặp cố định 100 lần để đạt sai số < 10^-15
    for (int iter = 0; iter < 100; ++iter) {
        double mid = low + (high - low) / 2.0;
        if (check_real(mid)) {
            high = mid;
        } else {
            low = mid;
        }
    }

    cout << fixed << setprecision(7) << low << "\n";
    return 0;
}
```

---

## 6. Các Bẫy Lỗi Lập Trình Kinh Điển (Bug Traps)

1. **Bẫy tràn số khi tính `mid`:** Biểu thức `mid = (low + high) / 2` sẽ bị tràn số kiểu `int` 32-bit nếu $low + high \ge 2 \cdot 10^9$. **Quy tắc bắt buộc:** Luôn viết `mid = low + (high - low) / 2`.
2. **Bẫy vòng lặp vô tận (Infinite Loop):** Khi không gian tìm kiếm chỉ còn 2 phần tử ($low = high - 1$), nếu cập nhật `low = mid` trong khi `mid` bị làm tròn xuống sẽ khiến $low$ không bao giờ tăng, gây TLE. Cần cập nhật `low = mid + 1` hoặc `high = mid - 1`.
3. **Bẫy biên không gian tìm kiếm $[low, high]$:** Đặt $high$ quá nhỏ dẫn đến bỏ sót nghiệm đúng, hoặc đặt $low = 0$ dẫn đến lỗi chia cho 0 (`mid = 0`) trong hàm `check`.
4. **Bẫy phần tử trùng lặp trong mảng xoay vòng:** Nếu mảng xoay vòng có các phần tử trùng lặp thỏa mãn $A[low] == A[mid] == A[high]$, ta không thể xác định nửa nào được sắp xếp đơn điệu $\implies$ Trường hợp xấu nhất phải co cả hai đầu `low++` và `high--`, làm độ phức tạp suy biến về $\mathcal{O}(N)$.

---

## 7. Ranh Giới Áp Dụng: Khi Nào Nên & Không Nên Dùng?

* **KHI NÀO ÁP DỤNG:**
  * Không gian tìm kiếm có tính chất **đơn điệu (Monotonic)**: Đồ thị hàm kiểm tra có dạng dải phân cách rõ ràng: $[\text{True}, \dots, \text{True}, \text{False}, \dots, \text{False}]$.
  * Cần tối ưu nghiệm trên miền cực lớn ($1 \dots 10^{18}$) mà không thể duyệt tuần tự.
* **KHI NÀO THẤT BẠI:**
  * Không gian tìm kiếm **không đơn điệu** (hàm dao động, có nhiều cực trị cục bộ). Lúc này chặt nhị phân sẽ bỏ sót nghiệm tối ưu toàn cục. Bắt buộc phải dùng **Ternary Search (Tìm kiếm Tam phân)** nếu hàm lồi/lõm, hoặc Quy hoạch động / Duyệt đồ thị.

---

# CÂU HỎI TRẮC NGHIỆM ĐO LƯỜNG TƯ DUY (CONCEPT QUIZ)

#### Câu 1 (Bản chất — Complexity):
Tại sao thuật toán tìm kiếm nhị phân trên không gian kích thước $N = 10^9$ chỉ cần tối đa khoảng 30 bước lặp?
* A. Vì mỗi bước chia không gian thành 10 phần.
* B. **(Đáp án đúng)** Vì mỗi bước loại bỏ chính xác $50\%$ không gian tìm kiếm, và $2^{30} \approx 1.07 \times 10^9 > 10^9$.
* C. Vì mảng số nguyên trong C++ chỉ chứa tối đa 30 phần tử âm.
* D. Do trình biên dịch C++ tối ưu hóa vòng lặp thành lệnh SIMD.
> *Giải thích:* Sau $k$ bước lặp, không gian còn lại là $N / 2^k$. Với $N = 10^9$, $2^{30} > 10^9 \implies k \approx 30$ bước là không gian thu hẹp về 1 phần tử.

---

#### Câu 2 (Điều kiện tiên quyết — Monotonicity):
Yêu cầu bắt buộc để có thể áp dụng thuật toán Tìm kiếm nhị phân là gì?
* A. Mảng phải chứa toàn số dương.
* B. Kích thước mảng phải là một lũy thừa của 2.
* C. **(Đáp án đúng)** Không gian tìm kiếm hoặc hàm kiểm tra phải có tính chất đơn điệu (Monotonicity).
* D. Tất cả các phần tử trong mảng phải đôi một khác nhau.
> *Giải thích:* Tính đơn điệu đảm bảo khi so sánh với phần tử trung điểm `mid`, ta chắc chắn biết nửa nào chứa nghiệm và nửa nào có thể loại bỏ an toàn.

---

#### Câu 3 (Cú pháp chuẩn — Bug Trap):
Biểu thức nào sau đây tính trung điểm `mid` an toàn nhất để chống tràn số trong C++?
* A. `mid = (low + high) / 2;`
* B. **(Đáp án đúng)** `mid = low + (high - low) / 2;`
* C. `mid = (low + high) >> 1;`
* D. `mid = low + high / 2;`
> *Giải thích:* Nếu $low = 1.5 \cdot 10^9$ và $high = 1.8 \cdot 10^9$, tổng $low + high = 3.3 \cdot 10^9$ vượt giới hạn $2.14 \cdot 10^9$ của `int`. Dùng `low + (high - low) / 2` phép trừ $(high - low)$ luôn không âm và nhỏ hơn $high$, không bao giờ tràn số.

---

#### Câu 4 (Hàm STL — lower_bound):
Cho mảng đã sắp xếp $A = [2, 4, 4, 4, 7, 9]$. Giá trị trả về của `lower_bound(A.begin(), A.end(), 4) - A.begin()` là gì?
* A. 0
* B. **(Đáp án đúng)** 1 (chỉ số của số 4 đầu tiên).
* C. 3 (chỉ số của số 4 cuối cùng).
* D. 4 (chỉ số của số 7).
> *Giải thích:* `lower_bound(..., X)` trả về con trỏ tới phần tử đầu tiên có giá trị $\ge X$. Số 4 đầu tiên nằm tại chỉ số 1 (0-based).

---

#### Câu 5 (Hàm STL — upper_bound):
Cho mảng đã sắp xếp $A = [2, 4, 4, 4, 7, 9]$. Giá trị trả về của `upper_bound(A.begin(), A.end(), 4) - A.begin()` là gì?
* A. 1
* B. 3
* C. **(Đáp án đúng)** 4 (chỉ số của số 7, phần tử đầu tiên $> 4$).
* D. 5
> *Giải thích:* `upper_bound(..., X)` trả về con trỏ tới phần tử đầu tiên có giá trị nghiêm ngặt $> X$. Phần tử đầu tiên $> 4$ là số 7 tại chỉ số 4.

---

#### Câu 6 (Đếm số lần xuất hiện — Counting):
Để đếm số lần xuất hiện của giá trị $X$ trong một vector $A$ gồm $N$ phần tử đã sắp xếp tăng dần trong thời gian $\mathcal{O}(\log N)$, ta dùng biểu thức nào?
* A. `upper_bound(A.begin(), A.end(), X) - A.begin()`
* B. `count(A.begin(), A.end(), X)`
* C. **(Đáp án đúng)** `upper_bound(A.begin(), A.end(), X) - lower_bound(A.begin(), A.end(), X)`
* D. `lower_bound(A.begin(), A.end(), X) - A.begin()`
> *Giải thích:* Hiệu vị trí của phần tử đầu tiên $> X$ và phần tử đầu tiên $\ge X$ chính là số lượng phần tử có giá trị đúng bằng $X$. Hàm `count` duyệt tuần tự $\mathcal{O}(N)$ sẽ bị TLE.

---

#### Câu 7 (Binary Search on Answer — Logic):
Trong bài toán *"Tìm chiều cao cắt $H$ lớn nhất sao cho tổng lượng gỗ thu được $\ge M$"*, tính chất đơn điệu của hàm kiểm tra `check(H)` thể hiện như thế nào?
* A. Chiều cao $H$ càng tăng thì lượng gỗ thu được càng tăng.
* B. **(Đáp án đúng)** Chiều cao $H$ càng tăng thì lượng gỗ thu được càng giảm (hàm giảm đơn điệu).
* C. Lượng gỗ thu được luôn không đổi với mọi chiều cao $H$.
* D. Hàm lượng gỗ biến thiên ngẫu nhiên theo $H$.
> *Giải thích:* Khi nâng máy cắt lên cao ($H$ tăng), phần ngọn cây bị cắt sẽ ngắn đi, do đó tổng lượng gỗ thu được chắc chắn giảm dần. Đây là hàm đơn điệu giảm.

---

#### Câu 8 (Binary Search on Answer — Search Space):
Nếu bài toán yêu cầu tìm giá trị $X$ nhỏ nhất thỏa mãn `check(X) == true`, sau khi kiểm tra tại `mid` thấy `check(mid) == true`, ta cần cập nhật bước tiếp theo như thế nào?
* A. `low = mid + 1;`
* B. **(Đáp án đúng)** `ans = mid; high = mid - 1;` (Ghi nhận `mid` là một đáp án hợp lệ và tiếp tục tìm giá trị nhỏ hơn ở nửa trái).
* C. `ans = mid; return ans;`
* D. `high = mid + 1;`
> *Giải thích:* Vì đề bài yêu cầu tìm $X$ **nhỏ nhất**, một giá trị `mid` thỏa mãn có thể chưa phải là nhỏ nhất $\implies$ ghi nhận `ans = mid` rồi thu hẹp không gian tìm kiếm sang bên trái `high = mid - 1`.

---

#### Câu 9 (Chặt nhị phân số thực — Real Numbers):
Tại sao khi chặt nhị phân trên tập số thực, ta nên dùng vòng lặp `for (int iter = 0; iter < 100; ++iter)` thay vì `while (high - low > 1e-7)`?
* A. Để chương trình chạy nhanh hơn gấp 100 lần.
* B. **(Đáp án đúng)** Để tránh nguy cơ lặp vô tận do sai số làm tròn số thực (Floating-point round-off error) khiến hiệu `high - low` không bao giờ nhỏ hơn epsilon.
* C. Vì số thực trong C++ chỉ biểu diễn được tối đa 100 chữ số thập phân.
* D. Do tiêu chuẩn thi đấu Olympic cấm dùng vòng lặp `while`.
> *Giải thích:* Với kiểu `double`, khi `high` và `low` rất gần nhau, phép trừ `high - low` có thể bị kẹt do giới hạn bit mantissa. Lặp 100 lần đảm bảo chia đôi khoảng cách $2^{100}$ lần, đạt độ chính xác cực cao mà không bao giờ bị kẹt vòng lặp.

---

#### Câu 10 (Ranh giới thất bại — Failure Boundary):
Trường hợp nào sau đây **KHÔNG THỂ** giải bằng thuật toán Tìm kiếm nhị phân một cách trực tiếp?
* A. Tìm căn bậc hai của số nguyên lớn $N \le 10^{18}$.
* B. Tìm phần tử nhỏ nhất lớn hơn $X$ trong mảng đã sắp xếp.
* C. **(Đáp án đúng)** Tìm giá trị $X$ để hàm số đa thức bậc 4 có 3 điểm cực trị $f(X)$ đạt giá trị lớn nhất trên đoạn $[-1000, 1000]$.
* D. Chia mảng thành $K$ đoạn con liên tiếp sao cho tổng đoạn lớn nhất là nhỏ nhất.
> *Giải thích:* Hàm đa thức bậc 4 có 3 điểm cực trị không có tính chất đơn điệu trên toàn đoạn $[-1000, 1000]$ (đổi chiều tăng/giảm nhiều lần), do đó Binary Search không thể loại bỏ an toàn một nửa không gian. Lưu ý: Thuật toán Tìm kiếm Tam phân (Ternary Search) cũng chỉ áp dụng được cho hàm **đơn đỉnh (unimodal)** có đúng 1 cực trị duy nhất, không áp dụng trực tiếp cho hàm đa cực trị như đa thức bậc 4 này.

---

#### Câu 11 (Mảng xoay vòng — Rotated Array):
Cho mảng gồm các phần tử đôi một phân biệt đã sắp xếp nhưng bị xoay vòng tại một vị trí $P$ (ví dụ: $[4, 5, 6, 7, 0, 1, 2]$). Khi xét phần tử trung điểm $A[mid]$, tính chất cốt lõi nào cho phép ta tiếp tục tìm kiếm nhị phân?
* A. Cả hai nửa trái và phải đều đã được sắp xếp tăng dần.
* B. **(Đáp án đúng)** Ít nhất một trong hai nửa $[low \dots mid]$ hoặc $[mid \dots high]$ chắc chắn là một dãy tăng dần đơn điệu bình thường.
* C. Phần tử nhỏ nhất luôn nằm ở chính giữa mảng.
* D. Mảng luôn có số lượng phần tử là số lẻ.
> *Giải thích:* Điểm gãy (Pivot) chỉ nằm ở 1 trong 2 nửa. Do đó, nửa còn lại luôn là một mảng tăng dần hoàn hảo, ta có thể kiểm tra xem $X$ có thuộc khoảng giá trị của nửa đó không để thu hẹp không gian. (Lưu ý: Nếu mảng chứa các **phần tử trùng lặp** thỏa $A[low] == A[mid] == A[high]$, ta không thể xác định nửa nào được sắp xếp, thuật toán buộc phải co $low++, high--$ và có thể suy biến về $\mathcal{O}(N)$).

---

#### Câu 12 (Ma trận 2D đã sắp xếp — 2D Matrix Binary Search):
Cho ma trận $N \times M$ gồm các số nguyên tăng dần từ trái sang phải trên từng hàng và phần tử đầu mỗi hàng luôn lớn hơn phần tử cuối hàng trước. Để tìm kiếm phần tử $X$ trong $\mathcal{O}(\log(N \times M))$, ta ánh xạ chỉ số 1D $mid$ sang tọa độ ô $(r, c)$ bằng công thức nào?
* A. $r = mid \bmod M, c = mid / M$
* B. **(Đáp án đúng)** $r = mid / M, c = mid \bmod M$ (với chỉ số 0-based).
* C. $r = mid / N, c = mid \bmod N$
* D. $r = mid \times M, c = mid + M$
> *Giải thích:* Coi ma trận $N \times M$ như một mảng 1D độ dài $N \times M$. Chỉ số dòng là $r = \lfloor mid / M \rfloor$ và chỉ số cột là $c = mid \bmod M$.

---

#### Câu 13 (Đỉnh dãy núi — Mountain Array Peak):
Trong một mảng dạng đỉnh núi (tăng dần rồi giảm dần: $A_0 < A_1 < \dots < A_p > A_{p+1} > \dots > A_{N-1}$), điều kiện nào tại vị trí `mid` cho biết đỉnh núi nằm ở bên phải `mid`?
* A. $A[mid] > A[mid + 1]$
* B. **(Đáp án đúng)** $A[mid] < A[mid + 1]$ (đang ở sườn dốc đi lên, đỉnh núi chắc chắn nằm bên phải $\implies low = mid + 1$).
* C. $A[mid] == A[mid + 1]$
* D. $A[mid] < A[mid - 1]$
> *Giải thích:* Nếu $A[mid] < A[mid+1]$, dãy đang có xu hướng tăng tại `mid`, do đó đỉnh núi chưa đạt được và nằm về phía bên phải.

---

#### Câu 14 (Trung vị hai mảng đã sắp xếp — Advanced Partition):
Thuật toán tìm phần tử trung vị của hai mảng đã sắp xếp $A$ (kích thước $N$) và $B$ (kích thước $M$) trong thời gian tối ưu $\mathcal{O}(\log(\min(N, M)))$ dựa trên việc chặt nhị phân đối tượng nào?
* A. Chặt nhị phân giá trị của phần tử trung vị từ $-10^9 \dots 10^9$.
* B. **(Đáp án đúng)** Chặt nhị phân vị trí vách ngăn (cut partition) trên mảng có kích thước nhỏ hơn để chia tổng hai mảng thành 2 nửa bằng nhau.
* C. Sắp xếp lại toàn bộ mảng gộp trong $\mathcal{O}((N+M)\log(N+M))$.
* D. Duyệt tuần tự 2 con trỏ qua cả 2 mảng.
> *Giải thích:* Bằng cách chặt nhị phân số lượng phần tử lấy từ mảng nhỏ hơn $i \in [0, N]$, số lượng phần tử lấy từ mảng lớn hơn được cố định $j = (N + M + 1)/2 - i$. Ta kiểm tra điều kiện vách ngăn hợp lệ trong $\mathcal{O}(1) \implies$ Tổng thời gian $\mathcal{O}(\log(\min(N, M)))$.

---

# DANH SÁCH BÀI TẬP THỰC HÀNH

| STT | Mã Bài | Tên Bài Toán | Cấp Độ | Ràng Buộc Dữ Liệu | Mục Tiêu Rèn Luyện |
|:---:|:---:|---|:---:|---|---|
| 01 | `CPPB-BS-01` | **Tìm Kiếm Phần Tử Trên Mảng Đã Sắp Xếp** | `P0` | $N, Q \le 10^5$ | Cài đặt Binary Search cơ bản |
| 02 | `CPPB-BS-02` | **Tìm Vị Trí Xuất Hiện Đầu Tiên & Cuối Cùng** | `P1` | $N, Q \le 10^5$ | Bản chất `lower_bound` / `upper_bound` |
| 03 | `CPPB-BS-03` | **Đếm Số Phần Tử Trong Đoạn $[L, R]$** | `P1` | $N, Q \le 10^5$ | Hiệu hai con trỏ nhị phân `upper - lower` |
| 04 | `CPPB-BS-04` | **Tìm Căn Bậc Hai Số Nguyên Lớn** | `P2` | $N \le 10^{18}$ | Binary Search trên tập số nguyên 64-bit |
| 05 | `CPPB-BS-05` | **Tìm Phần Tử Nhỏ Nhất Lớn Hơn X** | `P2` | $N, Q \le 10^5$ | Chặn trên nghiêm ngặt |
| 06 | `CPPB-BS-06` | **Chia Kẹo Cho Học Sinh Đạt Chuẩn** | `P3` | $N \le 10^5, K \le 10^{14}$ | Chặt nhị phân kết quả (Check chia đều) |
| 07 | `CPPB-BS-07` | **Cắt Gỗ Xây Dựng (Woodcutting / EKO)** | `P2` | $N \le 10^5, M \le 10^{14}$ | Bài toán kinh điển tìm độ cao máy cắt |
| 08 | `CPPB-BS-08` | **Đặt Trạm Phát Sóng Cách Nhau Xa Nhất (Aggressive Cows)** | `P3` | $N \le 10^5, C \le N$ | Tối đại hóa khoảng cách nhỏ nhất |
| 09 | `CPPB-BS-09` | **Chia Mảng Thành K Đoạn Có Tổng Max Nhỏ Nhất** | `P3` | $N \le 10^5, K \le N$ | Tối thiểu hóa tổng đoạn con lớn nhất |
| 10 | `CPPB-BS-10` | **Vận Chuyển Hàng Hóa Qua Phà Trong D Ngày** | `P3` | $N \le 10^5, D \le 10^5$ | Chặt nhị phân tải trọng thuyền |
| 11 | `CPPB-BS-11` | **Tìm Nghiệm Thực Của Phương Trình Đơn Điệu** | `P4` | Sai số $10^{-7}$ | Chặt nhị phân số thực với số lần lặp cố định |
| 12 | `CPPB-BS-12` | **Phần Tử Thứ K Của Hai Mảng Đã Sắp Xếp** | `P4` | $N, M \le 10^5$ | Chặt nhị phân số lượng phần tử $\le X$ |
| 13 | `CPPB-BS-13` | **Tìm Đoạn Con Có Trung Bình Lớn Nhất Độ Dài $\ge K$** | `P5` | $N \le 10^5, K \le N$ | Chặt nhị phân trung bình + Mảng tiền tố |
| 14 | `CPPB-BS-14` | **Tối Ưu Hóa Tuyến Đường Vận Tải Đa Điểm** | `P5` | $N \le 2 \cdot 10^5$ | Chặt nhị phân kết hợp cấu trúc đơn điệu |
| 15 | `CPPB-BS-15` | **Tìm Kiếm Trên Mảng Sắp Xếp Bị Xoay Vòng (Rotated Array)** | `P3` | $N \le 10^5$ | Phân đoạn đơn điệu trong mảng xoay |
| 16 | `CPPB-BS-16` | **Tìm Kiếm Trên Ma Trận 2D Đã Sắp Xếp (Matrix Search)** | `P2` | $N, M \le 1000$ | Chuyển tọa độ $1D \leftrightarrow 2D$ trong nhị phân |
| 17 | `CPPB-BS-17` | **Tìm Đỉnh Của Dãy Núi (Peak in Mountain Array)** | `P3` | $N \le 10^5$ | Chặt nhị phân theo đạo hàm / độ dốc |
| 18 | `CPPB-BS-18` | **Trung Vị Của Hai Mảng Đã Sắp Xếp (Median of Two Sorted)** | `P5` | $N, M \le 10^5$ | Phân chia vách ngăn nhị phân tối ưu $\mathcal{O}(\log(\min(N, M)))$ |
