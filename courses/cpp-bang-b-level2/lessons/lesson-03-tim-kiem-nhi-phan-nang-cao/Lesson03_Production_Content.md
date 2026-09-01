# Chuyên đề 03: Tìm kiếm nhị phân nâng cao

## 1. Khái niệm & bản chất của tìm kiếm nhị phân trong không gian nghiệm

Tìm kiếm nhị phân (Binary Search) không chỉ giới hạn ở việc tìm kiếm một phần tử trên mảng đã sắp xếp trong $\mathcal{O}(\log N)$, mà ở cấp độ thi đấu nâng cao, nó là một **phương pháp tối ưu hóa tổng quát trên không gian hàm đơn điệu**:
* **Chặt nhị phân kết quả (Binary Search on Answer):** Chuyển đổi một bài toán tối ưu hóa khó ("Tìm giá trị $X$ nhỏ nhất/lớn nhất thỏa mãn điều kiện...") thành một chuỗi các bài toán kiểm tra tính khả thi dễ dàng ("Với giá trị $X$ cho trước, có thể đạt được mục tiêu hay không?") thông qua một hàm kiểm tra đơn điệu `check(X)`.
* **Tìm kiếm nhị phân trên số thực (Real Binary Search):** Tìm nghiệm của phương trình hoặc hàm số liên tục với độ chính xác tuyệt đối $\epsilon = 10^{-7}$.
* **Tìm kiếm tam phân (Ternary Search):** Tìm điểm cực trị (cực đại/cực tiểu) của hàm số đơn phong (unimodal function) trong $\mathcal{O}(\log N)$.

---

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

---

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

---

![Chặt nhị phân tập số thực](assets/l03_binary_search_real_visual.svg)

## 4. Chặt nhị phân số thực

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

---

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

---

## 6. Ranh giới áp dụng: Khi nào chặt nhị phân mảng vs Chặt nhị phân kết quả?

| Đặc Điểm | Binary Search trên Mảng | Binary Search trên Đáp Án (Answer) |
|---|---|---|
| **Đối tượng tìm kiếm** | Vị trí / phần tử trong mảng tĩnh | Giá trị mục tiêu $X$ trong không gian nghiệm $[L, R]$ |
| **Yêu cầu bắt buộc** | Mảng đã được sắp xếp | Hàm kiểm tra $\text{check}(X)$ có tính đơn điệu |
| **Độ phức tạp** | $\mathcal{O}(\log N)$ | $\mathcal{O}(\text{Time}(\text{check}) \times \log(\text{Range}))$ |
| **Dấu hiệu đề bài** | "Tìm vị trí đầu tiên $\ge K$" | "Tìm giá trị lớn nhất / nhỏ nhất sao cho..." |

---

## Câu hỏi trắc nghiệm củng cố khái niệm

#### Câu 1 (Bản chất tính đơn điệu — Monotonicity):
Điều kiện cốt lõi để áp dụng phương pháp Chặt nhị phân kết quả là gì?
- **A.** Mảng đầu vào phải có ít hơn $10^5$ phần tử.
- **B.** **[Đáp án đúng]** Hàm kiểm tra tính khả thi $\text{check}(X)$ phải có tính đơn điệu (chuyển trạng thái 1 chiều từ True sang False hoặc ngược lại).
- **C.** Tất cả các số trong đề bài phải là số nguyên tố.
- **D.** Không gian tìm kiếm phải là số nguyên dương.

> *Giải thích:* Tính đơn điệu cho phép loại bỏ một nửa không gian nghiệm sau mỗi bước kiểm tra.

#### Câu 2 (Bẫy tràn số — Overflow):
Tại sao nên tính `mid = low + (high - low) / 2` thay vì `mid = (low + high) / 2`?
- **A.** Vì chạy nhanh hơn trên CPU.
- **B.** **[Đáp án đúng]** Để tránh tràn số khi `low + high` vượt quá giá trị cực đại của kiểu dữ liệu.
- **C.** Vì cú pháp C++ bắt buộc.
- **D.** Để `mid` luôn là số chẵn.

> *Giải thích:* Nếu `low, high = 1.5 \cdot 10^9`, tổng của chúng là $3 \cdot 10^9$ gây tràn số nguyên 32-bit (`int`).

#### Câu 3 (Cận ban đầu — Bounds):
Trong bài toán chia mảng $N$ phần tử thành $K$ đoạn liên tiếp sao cho tổng đoạn lớn nhất là nhỏ nhất, cận dưới `low` và cận trên `high` ban đầu nên chọn là gì?
- **A.** `low = 0, high = 10^9`
- **B.** **[Đáp án đúng]** `low = max(a[i]), high = sum(a[i])`
- **C.** `low = min(a[i]), high = max(a[i])`
- **D.** `low = 1, high = N`

> *Giải thích:* Tổng đoạn nhỏ nhất không thể bé hơn phần tử lớn nhất trong mảng (`max(a)`), và lớn nhất không thể vượt quá tổng toàn bộ mảng (`sum(a)`).

#### Câu 4 (Chặt nhị phân số thực — Real BS):
Tại sao khi chặt nhị phân trên số thực, người ta thường dùng vòng lặp cố định `for (int iter = 0; iter < 100; ++iter)`?
- **A.** Vì số thực không thể so sánh bằng dấu `<`.
- **B.** **[Đáp án đúng]** Để tránh vòng lặp vô tận do sai số làm tròn số thực dấu phẩy động và luôn đạt độ chính xác cực cao ($2^{-100}$).
- **C.** Vì 100 là giới hạn của ngôn ngữ C++.
- **D.** Để tiết kiệm bộ nhớ RAM.

> *Giải thích:* Sai số epsilon có thể khiến điều kiện `high - low > EPS` không bao giờ kết thúc nếu EPS quá nhỏ so với độ chuẩn của kiểu `double`.

#### Câu 5 (Ternary Search — Function):
Tìm kiếm tam phân (Ternary Search) được áp dụng khi hàm số có tính chất nào?
- **A.** Hàm số tăng ngặt trên toàn miền.
- **B.** **[Đáp án đúng]** Hàm số đơn phong (Unimodal — chỉ có đúng 1 điểm cực đại hoặc 1 điểm cực tiểu).
- **C.** Hàm số tuần hoàn hình sin.
- **D.** Hàm số ngẫu nhiên.

> *Giải thích:* Hàm đơn phong tăng liên tục rồi giảm liên tục (hoặc ngược lại), cho phép chia 3 đoạn để thu hẹp cực trị.

---

## Ma trận bài tập thực hành (P0 → P5)

| STT | Mã Bài | Tên Bài Toán | Cấp Độ | Ràng Buộc Dữ Liệu | Mục Tiêu Rèn Luyện |
|:---:|:---:|---|:---:|---|---|
| 01 | `CPPB2-L03-01` | **Chặt Nhị Phân Cắt Gỗ (EKO)** | `P0` | $N \le 10^6, H_i \le 10^9, M \le 10^{18}$ | BS trên đáp án cơ bản tìm Max |
| 02 | `CPPB2-L03-02` | **Chia Bánh Pizza Đều Nhau** | `P0` | $N \le 10^5, K \le 10^9$ | BS trên đáp án số thực tìm kích thước bánh |
| 03 | `CPPB2-L03-03` | **Chuồng Bò Xa Nhau Nhất (Aggressive Cows)** | `P1` | $N \le 10^5, C \le N, X_i \le 10^9$ | Sắp xếp + BS khoảng cách cực đại |
| 04 | `CPPB2-L03-04` | **Phân Chia Công Việc Thợ Sơn (Painter's Partition)** | `P1` | $N \le 10^5, K \le N, T_i \le 10^9$ | BS tìm Min của Max tổng đoạn |
| 05 | `CPPB2-L03-05` | **Đoàn Tàu Vận Chuyển Hàng Hóa** | `P2` | $N, M \le 10^5, W_i \le 10^9$ | Tham lam kiểm tra tính khả thi trong $\text{check}(X)$ |
| 06 | `CPPB2-L03-06` | **Khoảng Cách Dây Cáp Nhỏ Nhất** | `P2` | $N \le 10^5$, tọa độ thực | Chặt nhị phân số thực độ chính xác $10^{-6}$ |
| 07 | `CPPB2-L03-07` | **Trung Bình Cộng Đoạn Con Lớn Nhất $\ge K$** | `P2` | $N \le 10^5, K \le N, A_i \le 10^6$ | BS số thực kết hợp Mảng tiền tố trừ $mid$ |
| 08 | `CPPB2-L03-08` | **Tối Ưu Hóa Chi Phí Lắp Trạm Phát Sóng** | `P3` | $N \le 10^5$, tọa độ $\le 10^9$ | Tìm kiếm tam phân (Ternary Search) cực tiểu chi phí |
| 09 | `CPPB2-L03-09` | **Tìm Phần Tử Nhỏ Thứ K Trong Bảng Nhân $N \times N$** | `P3` | $N \le 10^5, K \le N^2$ | BS trên giá trị, hàm check đếm $\mathcal{O}(N)$ |
| 10 | `CPPB2-L03-10` | **Khoảng Cách Giữa Hai Phần Tử Trong Dãy Xoay Vòng** | `P3` | $N \le 2 \times 10^5, A_i \le 10^9$ | BS trên mảng bị xoay vòng (Rotated Array) |
| 11 | `CPPB2-L03-11` | **Tìm Nghiệm Thực Của Phương Trình Phi Tuyến** | `P4` | $f(x) = 0$, độ chính xác $10^{-8}$ | Chặt nhị phân số thực trên hàm đơn điệu ngặt |
| 12 | `CPPB2-L03-12` | **Đếm Số Cặp $(A_i, B_j)$ Có Tổng Trong Khoảng $[L, R]$** | `P4` | $N, M \le 10^5, \vert A_i \vert \le 10^9$ | `lower_bound` và `upper_bound` đếm số lượng |
| 13 | `CPPB2-L03-13` | **Phần Tử Nhỏ Thứ K Của Hợp Hai Mảng Đã Sắp Xếp** | `P4` | $N, M \le 10^6, K \le N + M$ | Chặt nhị phân trong $\mathcal{O}(\log(\min(N, M)))$ |
| 14 | `CPPB2-L03-14` | **Tối Ưu Phân Đoạn Trọng Số Ma Trận 2D** | `P5` | $N, M \le 1000, K \le 10^5$ | BS trên đáp án kết hợp 2D Prefix Sum & Greedy |
| 15 | `CPPB2-L03-15` | **Chặt Nhị Phân Song Song (Parallel Binary Search)** | `P5` | $N, M, Q \le 10^5$ | Kỹ thuật chặt nhị phân đồng thời cho $Q$ truy vấn |
| 16 | `CPPB2-L03-16` | **Khoảng Cách Cực Trị Trên Đa Giác Lồi** | `P5` | $N \le 10^5$ đỉnh lồi | Ternary Search trên cấu trúc đa giác |
