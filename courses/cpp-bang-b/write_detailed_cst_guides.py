#!/usr/bin/env python3
"""
Viết lại chuyên sâu cho Bài 03: Cửa sổ trượt (cst_01 -> cst_14).
"""

from pathlib import Path

BASE_DIR = Path(__file__).parent / "problems"

guides = {
    "cppb_cst_01_cua_so_k": r"""# Hướng Dẫn Giảng Dạy: Tổng Cửa Sổ Cố Định K
Chuyên đề: **Kỹ Thuật Cửa Sổ Trượt (Sliding Window)**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho dãy số nguyên $A$ gồm $N$ phần tử và số nguyên dương $K \le N$. Tìm tổng lớn nhất của một đoạn con liên tiếp gồm đúng $K$ phần tử.
- **Kỹ thuật Cửa sổ trượt cố định (Fixed-size Sliding Window):**
  - Nếu tính tổng từng đoạn $K$ phần tử bằng vòng for con, độ phức tạp là $\mathcal{O}(N \cdot K)$ (với $N = 10^5, K = 5 \cdot 10^4$ sẽ tốn tới $5 \cdot 10^9$ phép tính $\implies$ TLE).
  - Nhận xét then chốt: Khi cửa sổ trượt từ đoạn $[i - K \dots i - 1]$ sang đoạn kế tiếp $[i - K + 1 \dots i]$, ta chỉ cần:
    $$\text{sum\_mới} = \text{sum\_cũ} - A_{i - K} + A_i$$
    Tức là: **bớt đi phần tử vừa trượt ra khỏi cửa sổ bên trái, và cộng thêm phần tử mới bước vào cửa sổ bên phải**.
  - Mỗi bước trượt chỉ tốn $\mathcal{O}(1)$ phép tính.
  - Tổng độ phức tạp: $\mathcal{O}(N)$ thời gian, $\mathcal{O}(1)$ bộ nhớ phụ trợ.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: K = 3)
Mẫu thử: $N = 6, K = 3$, mảng `a = [2, 1, 5, 1, 3, 2]`.

| Bước | Cửa sổ trượt | Thao tác cập nhật tổng | Giá trị tổng | `max_sum` |
|---|---|---|---|---|
| 1 | `[2, 1, 5]` | Tính $K$ phần tử đầu: $2 + 1 + 5 = 8$ | `cur = 8` | `max_sum = 8` |
| 2 | Trượt sang `[1, 5, 1]` | Bớt $a[0]=2$, thêm $a[3]=1 \implies 8 - 2 + 1 = 7$ | `cur = 7` | $\max(8, 7) = 8$ |
| 3 | Trượt sang `[5, 1, 3]` | Bớt $a[1]=1$, thêm $a[4]=3 \implies 7 - 1 + 3 = 9$ | `cur = 9` | $\max(8, 9) = 9$ |
| 4 | Trượt sang `[1, 3, 2]` | Bớt $a[2]=5$, thêm $a[5]=2 \implies 9 - 5 + 2 = 6$ | `cur = 6` | $\max(9, 6) = 9$ |

Kết quả: Tổng lớn nhất của cửa sổ độ dài 3 là `9` (đoạn $[5, 1, 3]$).

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- **Bẫy 1 — Tràn số khi cộng dồn:** $K$ phần tử mỗi phần tử có thể lên tới $10^9$, tổng $K$ phần tử có thể đạt $10^{14}$. Biến `cur_sum` và `max_sum` bắt buộc phải là `long long`.
- **Bẫy 2 — Khởi tạo giá trị `max_sum`:** Nếu các phần tử có thể là số âm, không được khởi tạo `max_sum = 0` mà phải khởi tạo bằng tổng của chính cửa sổ $K$ phần tử đầu tiên.

---

## 4. Lời giải tham khảo
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k) || k > n) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    long long cur_sum = 0;
    for (int i = 0; i < k; ++i) {
        cur_sum += a[i];
    }

    long long max_sum = cur_sum;
    for (int i = k; i < n; ++i) {
        cur_sum += a[i] - a[i - k];
        max_sum = max(max_sum, cur_sum);
    }

    cout << max_sum << "\n";
    return 0;
}
```""",

    "cppb_cst_03_doan_con_ngan_nhat_tong_s": r"""# Hướng Dẫn Giảng Dạy: Đoạn Con Ngắn Nhất Có Tổng Đạt S
Chuyên đề: **Kỹ Thuật Cửa Sổ Trượt (Sliding Window)**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho dãy số nguyên dương $A$ và số nguyên dương $S$. Tìm độ dài nhỏ nhất của một đoạn con liên tiếp có tổng các phần tử $\ge S$. Nếu không tồn tại đoạn nào, in `0`.
- **Kỹ thuật Cửa sổ trượt biến thiên (Variable-size Sliding Window):**
  - Vì tất cả các phần tử $A_i$ đều là số nguyên dương ($A_i > 0$), mảng có tính chất đơn điệu: khi mở rộng cửa sổ sang phải thì tổng luôn tăng, khi thu hẹp cửa sổ bên trái thì tổng luôn giảm.
  - Sử dụng 2 con trỏ $L = 0, R = 0$ và biến tích lũy `cur_sum = 0`:
    1. Mở rộng biên phải $R$: Cộng `cur_sum += a[R]`.
    2. Trong khi `cur_sum >= S`: Ta đã tìm thấy một đoạn hợp lệ có độ dài $R - L + 1$. Cập nhật `min_len = min(min_len, R - L + 1)`. Sau đó thử thu hẹp biên trái bằng cách trừ `cur_sum -= a[L]` và tăng `L++` để tìm đoạn ngắn hơn.
  - Mỗi phần tử đi vào cửa sổ qua $R$ đúng 1 lần và ra khỏi cửa sổ qua $L$ tối đa 1 lần $\implies$ Tổng số thao tác con trỏ không quá $2N$. Độ phức tạp thời gian: $\mathcal{O}(N)$.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: S = 7)
Mẫu thử: $N = 6, S = 7$, mảng `a = [2, 3, 1, 2, 4, 3]`.

| Bước | Con trỏ $R$ | Thêm $a[R]$ | `cur_sum` | `cur_sum >= 7`? | Thu hẹp con trỏ $L$ & Cập nhật `min_len` |
|---|---|---|---|---|---|
| 1 | $R=0$ | $+2$ | 2 | Chưa | $L=0$ |
| 2 | $R=1$ | $+3$ | 5 | Chưa | $L=0$ |
| 3 | $R=2$ | $+1$ | 6 | Chưa | $L=0$ |
| 4 | $R=3$ | $+2$ | 8 | $8 \ge 7$ | Đoạn $[2, 3, 1, 2]$ dài 4. `min_len = 4`. Trừ $a[0]=2 \implies cur = 6, L=1$. |
| 5 | $R=4$ | $+4$ | 10 | $10 \ge 7$ | Đoạn $[3, 1, 2, 4]$ dài 4. Trừ $a[1]=3 \implies cur=7, L=2$.<br>Lại có $7 \ge 7 \implies$ đoạn $[1, 2, 4]$ dài 3. `min_len = 3`. Trừ $a[2]=1 \implies cur=6, L=3$. |
| 6 | $R=5$ | $+3$ | 9 | $9 \ge 7$ | Đoạn $[2, 4, 3]$ dài 3. Trừ $a[3]=2 \implies cur=7, L=4$.<br>Lại có $7 \ge 7 \implies$ đoạn $[4, 3]$ dài 2! `min_len = 2`. Trừ $a[4]=4 \implies cur=3, L=5$. |

Kết quả: Đoạn ngắn nhất có độ dài `2` (chính là đoạn $[4, 3]$).

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- **Bẫy 1 — Mảng có số âm hoặc số 0:** Thuật toán 2 con trỏ chỉ áp dụng được khi các phần tử đều dương ($A_i > 0$). Nếu có số âm, tính đơn điệu bị phá vỡ, phải dùng Mảng tiền tố + Binary Search / Deque.
- **Bẫy 2 — Không có đoạn nào thỏa mãn:** Khởi tạo `min_len = N + 1`. Nếu kết thúc vòng lặp mà `min_len > N` thì in `0`.

---

## 4. Lời giải tham khảo
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long s;
    if (!(cin >> n >> s)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    int l = 0;
    long long cur_sum = 0;
    int min_len = n + 1;

    for (int r = 0; r < n; ++r) {
        cur_sum += a[r];
        while (cur_sum >= s) {
            min_len = min(min_len, r - l + 1);
            cur_sum -= a[l];
            l++;
        }
    }

    if (min_len > n) {
        cout << 0 << "\n";
    } else {
        cout << min_len << "\n";
    }

    return 0;
}
```""",

    "cppb_cst_04_doan_con_dai_nhat_tong_s": r"""# Hướng Dẫn Giảng Dạy: Đoạn Con Dài Nhất Có Tổng Không Quá S
Chuyên đề: **Kỹ Thuật Cửa Sổ Trượt (Sliding Window)**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho dãy số nguyên không âm $A$ và số nguyên $S$. Tìm độ dài lớn nhất của một đoạn con liên tiếp có tổng không vượt quá $S$ ($\sum \le S$).
- **Phương pháp tiếp cận:**
  - Mở rộng con trỏ $R$ từ $0$ đến $N - 1$, cộng $A_R$ vào `cur_sum`.
  - Nếu `cur_sum > S`: Cửa sổ vi phạm điều kiện, ta co con trỏ $L$ lại bằng cách trừ $A_L$ và tăng $L++$ cho đến khi `cur_sum <= S`.
  - Tại mỗi bước sau khi co hợp lệ, cập nhật `max_len = max(max_len, R - L + 1)`.
  - Độ phức tạp thời gian: $\mathcal{O}(N)$.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: S = 8)
Mẫu thử: $N = 5, S = 8$, mảng `a = [3, 1, 2, 7, 4]`.

| Bước | $R$ | Nạp $a[R]$ | `cur_sum` | Co con trỏ $L$ | Đoạn hợp lệ | `max_len` |
|---|---|---|---|---|---|---|
| 1 | 0 | +3 | 3 | Không | $[3]$ | $\max(0, 1) = 1$ |
| 2 | 1 | +1 | 4 | Không | $[3, 1]$ | $\max(1, 2) = 2$ |
| 3 | 2 | +2 | 6 | Không | $[3, 1, 2]$ | $\max(2, 3) = 3$ |
| 4 | 3 | +7 | 13 | $>8 \implies$ trừ 3 ($L=1$), trừ 1 ($L=2$), trừ 2 ($L=3$) $\implies cur = 7$ | $[7]$ | $\max(3, 1) = 3$ |
| 5 | 4 | +4 | 11 | $>8 \implies$ trừ 7 ($L=4$) $\implies cur = 4$ | $[4]$ | $\max(3, 1) = 3$ |

Độ dài lớn nhất tìm được là `3` (đoạn $[3, 1, 2]$).

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- **Số 0 trong mảng:** Nếu mảng chứa số 0, việc cộng thêm 0 không làm tăng tổng nhưng vẫn làm tăng độ dài đoạn con, code vẫn chạy hoàn toàn chính xác.
- **Tất cả các số $> S$:** Kết quả sẽ là 0.

---

## 4. Lời giải tham khảo
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long s;
    if (!(cin >> n >> s)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    int l = 0;
    long long cur_sum = 0;
    int max_len = 0;

    for (int r = 0; r < n; ++r) {
        cur_sum += a[r];
        while (cur_sum > s && l <= r) {
            cur_sum -= a[l];
            l++;
        }
        if (cur_sum <= s) {
            max_len = max(max_len, r - l + 1);
        }
    }

    cout << max_len << "\n";
    return 0;
}
```""",

    "cppb_cst_05_lat_bit_k_so_khong": r"""# Hướng Dẫn Giảng Dạy: Đoạn Con Chứa Tối Đa K Số 0 (Lật Bit)
Chuyên đề: **Kỹ Thuật Cửa Sổ Trượt (Sliding Window)**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho dãy nhị phân chỉ gồm các số 0 và 1. Bạn được phép đổi chỗ tối đa $K$ số 0 thành số 1. Tìm độ dài lớn nhất của một đoạn con toàn số 1 liên tiếp sau khi thực hiện thao tác.
- **Quy đổi về bài toán Cửa sổ trượt:**
  - Thay vì thực hiện "lật bit", bài toán tương đương trực tiếp với: **"Tìm đoạn con dài nhất chứa tối đa $K$ số 0"**.
  - Dùng 2 con trỏ $L$ và $R$, duy trì biến `zero_count` đếm số lượng số 0 hiện có trong cửa sổ $[L \dots R]$:
    - Khi duyệt $R$: nếu $A_R == 0$ thì tăng `zero_count++`.
    - Trong khi `zero_count > K`: cửa sổ chứa quá nhiều số 0, ta co $L$ lại: nếu $A_L == 0$ thì giảm `zero_count--`, tăng $L++$.
    - Cập nhật `max_len = max(max_len, R - L + 1)`.
  - Độ phức tạp: $\mathcal{O}(N)$ thời gian, $\mathcal{O}(1)$ bộ nhớ.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: K = 2)
Mẫu thử: `a = [1, 1, 0, 0, 1, 1, 1, 0, 1]`, $K = 2$.

| Bước | $R$ | Phần tử $a[R]$ | `zero_count` | Trạng thái cửa sổ $[L \dots R]$ | Độ dài đoạn | `max_len` |
|---|---|---|---|---|---|---|
| 1-2 | 0, 1 | 1, 1 | 0 | $[1, 1]$ | 2 | 2 |
| 3 | 2 | 0 | 1 | $[1, 1, 0]$ | 3 | 3 |
| 4 | 3 | 0 | 2 | $[1, 1, 0, 0]$ | 4 | 4 |
| 5-7| 4-6 | 1, 1, 1 | 2 | $[1, 1, 0, 0, 1, 1, 1]$ | 7 | 7 |
| 8 | 7 | 0 | 3 ($>2$) | Co $L$ từ 0 đến 3 (bỏ số 0 đầu tiên tại $a[2]$) $\implies L=3, zeros=2$ | 5 | 7 |
| 9 | 8 | 1 | 2 | $[0, 1, 1, 1, 0, 1]$ | 6 | 7 |

Đoạn con dài nhất chứa tối đa 2 số 0 có độ dài là `7`.

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- **Trường hợp $K \ge$ số lượng số 0 trong cả mảng:** Đáp số chính là $N$ (toàn bộ mảng chuyển thành 1).
- **Trường hợp $K = 0$:** Bài toán trở thành tìm đoạn các số 1 liên tiếp dài nhất.

---

## 4. Lời giải tham khảo
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

    int l = 0;
    int zeros = 0;
    int max_len = 0;

    for (int r = 0; r < n; ++r) {
        if (a[r] == 0) zeros++;

        while (zeros > k) {
            if (a[l] == 0) zeros--;
            l++;
        }

        max_len = max(max_len, r - l + 1);
    }

    cout << max_len << "\n";
    return 0;
}
```""",

    "cppb_cst_08_dem_doan_con_tong_be_hon_s": r"""# Hướng Dẫn Giảng Dạy: Đếm Số Lượng Đoạn Con Có Tổng Không Quá S
Chuyên đề: **Kỹ Thuật Cửa Sổ Trượt (Sliding Window)**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho dãy số nguyên dương $A$ và số nguyên $S$. Đếm số lượng đoạn con liên tiếp có tổng không vượt quá $S$.
- **Kỹ thuật Đếm đoạn con bằng Sliding Window:**
  - Nhận xét then chốt: Với mỗi vị trí kết thúc $R$, nếu đoạn con dài nhất kết thúc tại $R$ thỏa mãn tổng $\le S$ bắt đầu từ $L$ (tức đoạn $[L \dots R]$ có tổng $\le S$), thì **tất cả các đoạn con kết thúc tại $R$ bắt đầu từ $L, L+1, \dots, R$ đều có tổng $\le S$** (do các phần tử đều dương).
  - Số lượng đoạn con hợp lệ kết thúc tại $R$ đúng bằng: **$R - L + 1$ đoạn!**
  - Do đó, ta chỉ cần duy trì cửa sổ trượt $[L \dots R]$ có tổng $\le S$. Với mỗi $R$, sau khi co $L$ hợp lệ, ta cộng dồn `ans += (R - L + 1)`.
  - Độ phức tạp thời gian: $\mathcal{O}(N)$.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: S = 6)
Mẫu thử: `a = [1, 2, 3, 4]`, $S = 6$.

| Bước | $R$ | Phần tử $a[R]$ | Co $L$ sao cho `sum <= 6` | Đoạn $[L \dots R]$ | Số đoạn kết thúc tại $R$ | `ans` cộng dồn |
|---|---|---|---|---|---|---|
| 1 | 0 | 1 | $L=0, sum=1$ | $[1]$ | $0 - 0 + 1 = 1$ (đoạn $[1]$) | 1 |
| 2 | 1 | 2 | $L=0, sum=3$ | $[1, 2]$ | $1 - 0 + 1 = 2$ (đoạn $[2], [1, 2]$) | $1 + 2 = 3$ |
| 3 | 2 | 3 | $L=0, sum=6$ | $[1, 2, 3]$ | $2 - 0 + 1 = 3$ (đoạn $[3], [2, 3], [1, 2, 3]$) | $3 + 3 = 6$ |
| 4 | 3 | 4 | $sum=10 > 6 \implies$ bớt 1 ($L=1$), bớt 2 ($L=2$) $\implies sum=7 > 6 \implies$ bớt 3 ($L=3$) $\implies sum=4 \le 6$ | $[4]$ | $3 - 3 + 1 = 1$ (đoạn $[4]$) | $6 + 1 = 7$ |

Tổng số đoạn con thỏa mãn: `7` đoạn.

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- **Tràn số `long long`:** Tổng số đoạn con tối đa là $N(N + 1) / 2 \approx 5 \cdot 10^9$ khi $N = 10^5$. Bắt buộc phải khai báo `long long ans = 0`.

---

## 4. Lời giải tham khảo
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long s;
    if (!(cin >> n >> s)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    long long ans = 0;
    long long cur_sum = 0;
    int l = 0;

    for (int r = 0; r < n; ++r) {
        cur_sum += a[r];
        while (cur_sum > s && l <= r) {
            cur_sum -= a[l];
            l++;
        }
        if (cur_sum <= s) {
            ans += (r - l + 1);
        }
    }

    cout << ans << "\n";
    return 0;
}
```""",

    "cppb_cst_10_doan_con_k_ky_tu_khac_nhau": r"""# Hướng Dẫn Giảng Dạy: Đoạn Con Dài Nhất Chứa Tối Đa K Ký Tự Khác Nhau
Chuyên đề: **Kỹ Thuật Cửa Sổ Trượt (Sliding Window)**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho chuỗi ký tự $S$ và số nguyên $K$. Tìm độ dài lớn nhất của một chuỗi con liên tiếp chứa tối đa $K$ ký tự phân biệt khác nhau.
- **Phương pháp tiếp cận — Mảng đếm tần số trong cửa sổ:**
  - Vì bảng chữ cái chỉ có 256 ký tự ASCII (hoặc 26 chữ cái thường), ta dùng mảng `freq[256]` để đếm số lần xuất hiện của từng ký tự trong cửa sổ $[L \dots R]$.
  - Duy trì biến `distinct_count` là số lượng ký tự có tần số $> 0$.
  - Khi mở rộng $R$: nếu `freq[S[R]] == 0` thì `distinct_count++`, sau đó `freq[S[R]]++`.
  - Trong khi `distinct_count > K`: ta co $L$ lại: `freq[S[L]]--`, nếu `freq[S[L]] == 0` thì giảm `distinct_count--`, sau đó `L++`.
  - Cập nhật `max_len = max(max_len, R - L + 1)`.
  - Độ phức tạp: $\mathcal{O}(N)$ thời gian, $\mathcal{O}(1)$ bộ nhớ.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: K = 2)
Mẫu thử: Chuỗi `s = "eceba"`, $K = 2$.

| Bước | $R$ | Ký tự $S[R]$ | Cửa sổ $[L \dots R]$ | Số ký tự khác nhau | Cập nhật `max_len` |
|---|---|---|---|---|---|
| 1 | 0 | 'e' | `"e"` | 1 | $\max(0, 1) = 1$ |
| 2 | 1 | 'c' | `"ec"` | 2 | $\max(1, 2) = 2$ |
| 3 | 2 | 'e' | `"ece"` | 2 (vẫn chỉ có 'e' và 'c') | $\max(2, 3) = 3$ |
| 4 | 3 | 'b' | `"eceb"` $\implies$ có 3 ký tự {'e', 'c', 'b'} | Co $L$: bỏ 'e' ($L=1$, vẫn còn 'e' ở vị trí 2), bỏ 'c' ($L=2$, hết 'c' $\implies$ còn 2 ký tự {'e', 'b'}) | Cửa sổ mới `"eb"` dài 2 |
| 5 | 4 | 'a' | `"eba"` $\implies$ có 3 ký tự | Co $L$: bỏ 'e' ($L=3$, hết 'e') $\implies$ còn 2 ký tự {'b', 'a'} | Cửa sổ mới `"ba"` dài 2 |

Độ dài lớn nhất là `3` (chuỗi con `"ece"`).

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- **Bẫy $K = 0$:** Nếu $K = 0$, không thể chọn ký tự nào $\implies$ in `0`.
- **Ký tự ASCII mở rộng:** Khai báo mảng tần số kích thước `256` kiểu `int` để an toàn với mọi ký tự.

---

## 4. Lời giải tham khảo
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int k;
    string s;
    if (!(cin >> k >> s)) return 0;
    if (k <= 0) { cout << 0 << "\n"; return 0; }

    int n = s.size();
    vector<int> freq(256, 0);
    int distinct = 0;
    int l = 0;
    int max_len = 0;

    for (int r = 0; r < n; ++r) {
        if (freq[(unsigned char)s[r]] == 0) {
            distinct++;
        }
        freq[(unsigned char)s[r]]++;

        while (distinct > k) {
            freq[(unsigned char)s[l]]--;
            if (freq[(unsigned char)s[l]] == 0) {
                distinct--;
            }
            l++;
        }

        max_len = max(max_len, r - l + 1);
    }

    cout << max_len << "\n";
    return 0;
}
```"""
}

for code, content in guides.items():
    p_dir = BASE_DIR / code
    if p_dir.exists():
        (p_dir / "Huong_Dan_Giang_Day.md").write_text(content, encoding="utf-8")
        print(f"✅ Đã cập nhật chuyên sâu: {code}")
