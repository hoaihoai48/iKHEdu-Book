#!/usr/bin/env python3
"""
Viết lại chuyên sâu cho hct_06 -> hct_14.
"""

from pathlib import Path

BASE_DIR = Path(__file__).parent / "problems"

guides = {
    "cppb_hct_06_van_chuyen_hang_hoa": r"""# Hướng Dẫn Giảng Dạy: Vận Chuyển Thùng Hàng Cực Đại
Chuyên đề: **Kỹ Thuật Hai Con Trỏ (Two Pointers)**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho trọng lượng của $N$ thùng hàng và tải trọng xe tải $C$. Cần chọn 2 thùng hàng phân biệt sao cho tổng trọng lượng của chúng lớn nhất nhưng không vượt quá $C$.
- **Phương pháp tiếp cận:**
  - Sắp xếp mảng tăng dần. Đặt $L = 0, R = N - 1$.
  - Khởi tạo `best_weight = -1`.
  - Tại mỗi bước:
    - Nếu $A_L + A_R \le C$: Cặp này hợp lệ! Cập nhật `best_weight = max(best_weight, a[L] + a[R])`. Sau đó, muốn tìm tổng lớn hơn, ta thử tăng `L++`.
    - Nếu $A_L + A_R > C$: Tổng vượt quá tải trọng cho phép, bắt buộc phải giảm `R--`.
  - Độ phức tạp: $\mathcal{O}(N \log N)$.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: C = 15)
Mẫu thử: $N = 5, C = 15$, trọng lượng `[3, 8, 5, 12, 7]`. Sắp xếp: `[3, 5, 7, 8, 12]`.

| Bước | $(L, R)$ | $(A_L, A_R)$ | Tổng | So với $C=15$ | Cập nhật `best_weight` |
|---|---|---|---|---|---|
| 1 | $(0, 4)$ | $(3, 12)$ | $15$ | $15 \le 15$ | `best = 15` (đạt tối đa đúng bằng $C$, có thể dừng ngay) |

Kết quả: Tổng trọng lượng lớn nhất là `15`.

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- **Bẫy 1 — Không có cặp nào $\le C$:** Nếu ngay cả 2 thùng nhẹ nhất $A_0 + A_1 > C$, in `-1`.
- **Bẫy 2 — Tối ưu hóa:** Khi tìm thấy tổng đúng bằng $C$, có thể ngắt vòng lặp ngay lập tức vì không thể có tổng nào lớn hơn $C$ mà hợp lệ.

---

## 4. Lời giải tham khảo
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long c;
    if (!(cin >> n >> c)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    sort(a.begin(), a.end());

    long long best = -1;
    int l = 0, r = n - 1;

    while (l < r) {
        long long sum = a[l] + a[r];
        if (sum <= c) {
            best = max(best, sum);
            l++;
        } else {
            r--;
        }
    }

    cout << best << "\n";
    return 0;
}
```""",

    "cppb_hct_07_tong_gan_s_nhat": r"""# Hướng Dẫn Giảng Dạy: Tìm Cặp Có Tổng Gần S Nhất
Chuyên đề: **Kỹ Thuật Hai Con Trỏ (Two Pointers)**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho dãy $N$ số nguyên và giá trị mục tiêu $S$. Tìm cặp $(A_i, A_j)$ sao cho $|(A_i + A_j) - S|$ nhỏ nhất có thể.
- **Phương pháp tiếp cận:**
  - Sắp xếp mảng tăng dần. Đặt $L = 0, R = N - 1$.
  - Duy trì khoảng cách nhỏ nhất `min_diff = abs(a[0] + a[n-1] - s)` và tổng tối ưu `best_sum`.
  - Tại mỗi bước:
    - Tính `sum = a[L] + a[R]`.
    - Nếu `abs(sum - s) < min_diff`, cập nhật `min_diff` và `best_sum`.
    - Nếu `sum == s`: Khoảng cách bằng 0, dừng ngay.
    - Nếu `sum < s`: Tăng `L++`.
    - Nếu `sum > s`: Giảm `R--`.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: S = 20)
Mẫu thử: $N = 4, S = 20$, mảng đã xếp `[2, 7, 11, 15]`.

| Bước | $(L, R)$ | $(A_L, A_R)$ | Tổng | Khoảng cách tới 20 | Cập nhật |
|---|---|---|---|---|---|
| 1 | $(0, 3)$ | $(2, 15)$ | 17 | $|17 - 20| = 3$ | `min_diff = 3, best = 17`. Do $17 < 20 \implies L=1$ |
| 2 | $(1, 3)$ | $(7, 15)$ | 22 | $|22 - 20| = 2$ | `min_diff = 2, best = 22`. Do $22 > 20 \implies R=2$ |
| 3 | $(1, 2)$ | $(7, 11)$ | 18 | $|18 - 20| = 2$ | Bằng khoảng cách 2, giữ `best = 22` hoặc theo tiêu chí đề |

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- **Bẫy tràn số khi trừ:** Tính `abs(sum - s)` cần đảm bảo `sum` và `s` là kiểu `long long`.
- **Tiêu chí phụ khi hòa khoảng cách:** Đọc kỹ đề xem nếu có 2 tổng cùng khoảng cách (ví dụ 18 và 22 cách 20 đều 2 đơn vị) thì ưu tiên tổng nhỏ hơn hay lớn hơn.

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

    sort(a.begin(), a.end());

    int l = 0, r = n - 1;
    long long best_sum = a[l] + a[r];
    long long min_diff = abs(best_sum - s);

    while (l < r) {
        long long cur_sum = a[l] + a[r];
        long long cur_diff = abs(cur_sum - s);

        if (cur_diff < min_diff) {
            min_diff = cur_diff;
            best_sum = cur_sum;
        }

        if (cur_sum == s) break;
        if (cur_sum < s) l++;
        else r--;
    }

    cout << best_sum << "\n";
    return 0;
}
```""",

    "cppb_hct_08_hieu_hai_so_bang_k": r"""# Hướng Dẫn Giảng Dạy: Tìm Cặp Có Hiệu Đúng Bằng K
Chuyên đề: **Kỹ Thuật Hai Con Trỏ (Two Pointers)**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho dãy số $A$ và số nguyên không âm $K$. Tìm cặp $(i, j)$ sao cho $A_j - A_i = K$ với $i \ne j$.
- **Kỹ thuật Hai con trỏ Cùng Chiều (Two Pointers in Same Direction):**
  - Khác với bài toán Tổng hai số (dùng con trỏ đối đầu), bài toán Hiệu hai số sử dụng **hai con trỏ cùng chiều chạy từ trái sang phải**:
  - Sắp xếp mảng tăng dần. Khởi tạo $L = 0, R = 1$.
  - Tại mỗi bước (khi $L < N$ và $R < N$):
    - Nếu $L == R$: Phải đảm bảo hai phần tử phân biệt $\implies$ tăng `R++`.
    - Tính hiệu `diff = a[R] - a[L]`:
      - Nếu `diff == K`: Tìm thấy nghiệm!
      - Nếu `diff < K`: Hiệu còn quá nhỏ, muốn hiệu tăng thì phải tăng số bị trừ $\implies$ tăng `R++`.
      - Nếu `diff > K`: Hiệu quá lớn, muốn hiệu giảm thì phải tăng số trừ $\implies$ tăng `L++`.
  - Độ phức tạp: $\mathcal{O}(N \log N)$ cho sắp xếp, $\mathcal{O}(N)$ cho duyệt vì mỗi con trỏ chỉ đi về phía trước tối đa $N$ bước.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: K = 4)
Mẫu thử: $N = 5, K = 4$, mảng đã xếp `[1, 3, 5, 8, 12]`.

| Bước | $(L, R)$ | $(A_L, A_R)$ | Hiệu $A_R - A_L$ | So với $K=4$ | Di chuyển |
|---|---|---|---|---|---|
| 1 | $(0, 1)$ | $(1, 3)$ | $3 - 1 = 2$ | $2 < 4$ | Tăng $R=2$ |
| 2 | $(0, 2)$ | $(1, 5)$ | $5 - 1 = 4$ | $4 == 4$ | Khớp! Cặp $(1, 5)$ có hiệu bằng 4 |

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- **Bẫy 1 — Trường hợp $K = 0$:** Nếu $K = 0$, đề bài yêu cầu tìm hai phần tử bằng nhau. Khi $L == R$ hiệu luôn bằng 0 nhưng đây là cùng một phần tử! Bắt buộc phải duy trì $L < R$.
- **Bẫy 2 — Dùng con trỏ đối đầu:** Học sinh thường có thói quen dùng con trỏ đối đầu cho mọi bài hai con trỏ. Cần phân biệt rõ: **Tổng hai số $\implies$ đối đầu; Hiệu hai số $\implies$ cùng chiều**.

---

## 4. Lời giải tham khảo
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long k;
    if (!(cin >> n >> k)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    sort(a.begin(), a.end());

    int l = 0, r = 1;
    bool found = false;

    while (l < n && r < n) {
        if (l == r) {
            r++;
            continue;
        }
        long long diff = a[r] - a[l];
        if (diff == k) {
            cout << a[l] << " " << a[r] << "\n";
            found = true;
            l++;
            r++;
        } else if (diff < k) {
            r++;
        } else {
            l++;
        }
    }

    if (!found) cout << "-1\n";
    return 0;
}
```""",

    "cppb_hct_09_bo_ba_tong_bang_s": r"""# Hướng Dẫn Giảng Dạy: Bộ Ba Số Có Tổng Bằng S (3-Sum)
Chuyên đề: **Kỹ Thuật Hai Con Trỏ (Two Pointers)**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho dãy $N$ số. Tìm 3 phần tử ở 3 vị trí phân biệt $i < j < k$ sao cho $A_i + A_j + A_k = S$.
- **Phương pháp tiếp cận — Cố định 1 phần tử + Hai con trỏ:**
  - Vét cạn 3 vòng lặp là $\mathcal{O}(N^3)$, không chạy được với $N = 5000$.
  - Ta giảm bài toán 3-Sum về bài toán 2-Sum:
    1. Sắp xếp mảng $A$ tăng dần.
    2. Duyệt phần tử đầu tiên $i$ từ $0$ đến $N - 3$.
    3. Với mỗi $i$, bài toán trở thành tìm 2 số trong đoạn $[i + 1 \dots N - 1]$ có tổng bằng $S - A_i$.
    4. Áp dụng kỹ thuật hai con trỏ đối đầu $L = i + 1$ và $R = N - 1$ chạy trong $\mathcal{O}(N)$.
  - Tổng độ phức tạp thời gian: $\mathcal{O}(N^2)$, chạy cực nhanh trong $< 0.1\text{s}$ với $N = 5000$.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: S = 0)
Mẫu thử: `[-1, 0, 1, 2, -1, -4]`. Sắp xếp: `[-4, -1, -1, 0, 1, 2]`.

| Bước | Cố định $i$ | Target $S - A_i$ | Hai con trỏ $(L, R)$ | Nghiệm tìm được |
|---|---|---|---|---|
| 1 | $i=0 (A_0 = -4)$ | $0 - (-4) = 4$ | $L=1, R=5$ $\implies$ max tổng là $-1 + 2 = 1 < 4$ | Không có nghiệm |
| 2 | $i=1 (A_1 = -1)$ | $0 - (-1) = 1$ | $L=2 (A_2=-1), R=5 (A_5=2) \implies -1 + 2 = 1$ | Khớp! Bộ ba: `(-1, -1, 2)` |
| 3 | — | 1 | $L=3 (A_3=0), R=4 (A_4=1) \implies 0 + 1 = 1$ | Khớp! Bộ ba: `(-1, 0, 1)` |

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- **Bẫy trùng lặp bộ ba:** Nếu đề bài yêu cầu in các bộ ba giá trị phân biệt, cần bỏ qua các giá trị trùng lặp khi tăng $i$, $L$, $R$ (`while (l < r && a[l] == a[l+1]) l++;`).
- **Bẫy tràn số:** Tổng 3 số lớn có thể vượt $2 \cdot 10^9$, dùng `long long` cho biến `sum`.

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

    sort(a.begin(), a.end());

    for (int i = 0; i < n - 2; ++i) {
        long long target = s - a[i];
        int l = i + 1, r = n - 1;

        while (l < r) {
            long long cur = a[l] + a[r];
            if (cur == target) {
                cout << a[i] << " " << a[l] << " " << a[r] << "\n";
                return 0; // Tìm thấy 1 bộ ba
            } else if (cur < target) {
                l++;
            } else {
                r--;
            }
        }
    }

    cout << "-1\n";
    return 0;
}
```""",

    "cppb_hct_10_dem_so_tam_giac": r"""# Hướng Dẫn Giảng Dạy: Đếm Số Tam Giác Có Thể Tạo Thành
Chuyên đề: **Kỹ Thuật Hai Con Trỏ (Two Pointers)**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho $N$ thanh gỗ có độ dài $A_1, A_2, \dots, A_N$. Đếm số bộ ba thanh gỗ có thể ghép thành một tam giác không suy biến.
- **Bất đẳng thức tam giác trên mảng đã sắp xếp:**
  - Ba cạnh $(a, b, c)$ tạo thành tam giác khi: $a + b > c, a + c > b, b + c > a$.
  - Nếu ta sắp xếp tăng dần $A_i \le A_j \le A_k$, ta luôn có $A_k + A_i > A_j$ và $A_k + A_j > A_i$.
  - Điều kiện duy nhất cần kiểm tra là:
    $$A_i + A_j > A_k$$
- **Thuật toán Hai con trỏ $\mathcal{O}(N^2)$:**
  - Cố định cạnh lớn nhất $k$ chạy ngược từ $N - 1$ về $2$.
  - Với mỗi $k$, đặt $L = 0$ và $R = k - 1$:
    - Nếu $A_L + A_R > A_k$: Vì mảng tăng dần nên mọi phần tử từ $L$ đến $R - 1$ khi ghép với $A_R$ đều thỏa mãn $> A_k$.
    - Do đó có đúng **$R - L$ tam giác hợp lệ**. Cộng `ans += (R - L)` và giảm `R--`.
    - Nếu $A_L + A_R \le A_k$: Tổng quá nhỏ, tăng `L++`.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1)
Mẫu thử: $N = 5$, các cạnh đã xếp `[2, 3, 4, 5, 6]`.

| Cố định $k$ | Cạnh lớn nhất $A_k$ | Hai con trỏ $(L, R)$ | $A_L + A_R > A_k$? | Số tam giác cộng dồn |
|---|---|---|---|---|
| $k=4$ | $A_4 = 6$ | $L=0, R=3 (2, 5)$ | $2 + 5 = 7 > 6$ | Cặp (3, 4, 5) với 5 $\implies$ cộng $3 - 0 = 3$. $R=2$. |
| — | $A_4 = 6$ | $L=0, R=2 (2, 4)$ | $2 + 4 = 6 \le 6$ | $L=1$. |
| — | $A_4 = 6$ | $L=1, R=2 (3, 4)$ | $3 + 4 = 7 > 6$ | Cộng $2 - 1 = 1$. $R=1 \implies$ dừng $k=4$. (Được 4 tam giác) |

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- **Bẫy tam giác suy biến:** Điều kiện là $a + b > c$ (lớn hơn nghiêm ngặt), nếu $a + b == c$ ba điểm thẳng hàng, không tạo thành tam giác.
- **Biến đếm `ans`:** Phải dùng `long long ans = 0` vì số tam giác tối đa là $\binom{N}{3} \approx 1.6 \cdot 10^{11}$ khi $N = 10^4$.

---

## 4. Lời giải tham khảo
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n) || n < 3) { cout << 0 << "\n"; return 0; }

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    sort(a.begin(), a.end());

    long long count = 0;
    for (int k = n - 1; k >= 2; --k) {
        int l = 0, r = k - 1;
        while (l < r) {
            if (a[l] + a[r] > a[k]) {
                count += (r - l);
                r--;
            } else {
                l++;
            }
        }
    }

    cout << count << "\n";
    return 0;
}
```""",

    "cppb_hct_11_dem_cap_trung_lap": r"""# Hướng Dẫn Giảng Dạy: Đếm Cặp Tổng S Trên Mảng Trùng Lặp
Chuyên đề: **Kỹ Thuật Hai Con Trỏ (Two Pointers)**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho dãy $N$ số có thể chứa nhiều giá trị trùng nhau. Đếm số cặp chỉ số $(i, j)$ với $i < j$ sao cho $A_i + A_j = S$.
- **Xử lý trùng lặp bằng đếm tần số khối:**
  - Sắp xếp mảng tăng dần. Đặt $L = 0, R = N - 1$.
  - Khi $A_L + A_R == S$:
    - **Trường hợp 1:** $A_L == A_R$. Điều này nghĩa là tất cả các phần tử từ $L$ đến $R$ đều bằng nhau. Số phần tử là $cnt = R - L + 1$. Số cặp chọn 2 từ $cnt$ là:
      $$ans += \frac{cnt \times (cnt - 1)}{2}$$
      Sau đó dừng vòng lặp ngay vì không còn phần tử nào khác.
    - **Trường hợp 2:** $A_L \ne A_R$. Đếm số lượng phần tử bằng $A_L$ liên tiếp ($cnt_L$), và số lượng phần tử bằng $A_R$ liên tiếp ($cnt_R$).
      Số cặp mới tạo thành là: $cnt_L \times cnt_R$.
      Sau đó tăng $L += cnt_L$ và giảm $R -= cnt_R$.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: S = 6)
Mẫu thử: `a = [1, 2, 2, 4, 4, 5]`, $S = 6$.

| Bước | $(L, R)$ | $(A_L, A_R)$ | Tổng | Nhánh xử lý | Số cặp cộng dồn |
|---|---|---|---|---|---|
| 1 | $(0, 5)$ | $(1, 5)$ | $1 + 5 = 6$ | $A_L \ne A_R$, có 1 số `1` và 1 số `5` | $1 \times 1 = 1$. Dịch $L=1, R=4$. |
| 2 | $(1, 4)$ | $(2, 4)$ | $2 + 4 = 6$ | $A_L \ne A_R$, có 2 số `2` và 2 số `4` | $2 \times 2 = 4$. Dịch $L=3, R=2$. |
| 3 | — | — | — | $L > R \implies$ Dừng | Tổng số cặp: $1 + 4 = 5$. |

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- **Bẫy vòng lặp vô hạn:** Khi đếm $cnt_L$ và $cnt_R$, cẩn thận kiểm tra biên $L \le R$.
- **Tràn số khi nhân:** $cnt_L \times cnt_R$ có thể lên tới $10^{10}$ nếu $N = 10^5$, bắt buộc ép kiểu `1LL * cnt_L * cnt_R`.

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

    sort(a.begin(), a.end());

    long long ans = 0;
    int l = 0, r = n - 1;

    while (l < r) {
        long long sum = a[l] + a[r];
        if (sum < s) {
            l++;
        } else if (sum > s) {
            r--;
        } else {
            if (a[l] == a[r]) {
                long long cnt = r - l + 1;
                ans += cnt * (cnt - 1) / 2;
                break;
            } else {
                long long val_l = a[l], cnt_l = 0;
                while (l <= r && a[l] == val_l) { cnt_l++; l++; }

                long long val_r = a[r], cnt_r = 0;
                while (l <= r && a[r] == val_r) { cnt_r++; r--; }

                ans += cnt_l * cnt_r;
            }
        }
    }

    cout << ans << "\n";
    return 0;
}
```""",

    "cppb_hct_12_ghep_tre_em_banh_quy": r"""# Hướng Dẫn Giảng Dạy: Ghép Cặp Trẻ Em Và Bánh Quy
Chuyên đề: **Kỹ Thuật Hai Con Trỏ (Two Pointers)**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Có $N$ đứa trẻ, đứa thứ $i$ có mức độ thèm ăn là $G_i$. Có $M$ chiếc bánh quy với kích thước $S_1, S_2, \dots, S_M$. Đứa trẻ $i$ chỉ thỏa mãn nếu được nhận chiếc bánh có kích thước $\ge G_i$. Mỗi trẻ nhận tối đa 1 bánh. Tìm số trẻ tối đa có thể làm hài lòng.
- **Chiến lược Tham lam (Greedy Matching):**
  - Sắp xếp cả hai danh sách $G$ và $S$ theo thứ tự tăng dần.
  - Sử dụng 2 con trỏ: $i$ trỏ vào trẻ em, $j$ trỏ vào bánh quy.
  - Luôn cố gắng thỏa mãn đứa trẻ dễ tính nhất trước (đứa có $G_i$ nhỏ nhất) bằng chiếc bánh nhỏ nhất có thể đáp ứng được:
    - Nếu $S_j \ge G_i$: Bánh $j$ đáp ứng được trẻ $i \implies$ cho trẻ nhận bánh, tăng $i++$ và $j++$.
    - Nếu $S_j < G_i$: Bánh quá nhỏ, không thể làm hài lòng trẻ $i$ (và cũng không thể làm hài lòng bất kỳ đứa trẻ nào phía sau) $\implies$ bỏ qua chiếc bánh này, tăng $j++$.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1)
Mẫu thử: Trẻ em `g = [1, 2, 3]`, Bánh quy `s = [1, 1]`.

| Bước | $(i, j)$ | Mức thèm $G_i$ | Kích thước bánh $S_j$ | So sánh | Kết quả ghép |
|---|---|---|---|---|---|
| 1 | $(0, 0)$ | 1 | 1 | $1 \ge 1$ (Hợp lệ) | Trẻ 1 nhận bánh 1 $\implies i=1, j=1$ |
| 2 | $(1, 1)$ | 2 | 1 | $1 < 2$ (Bánh nhỏ) | Bỏ qua bánh 1 $\implies j=2$ |
| 3 | $(1, 2)$ | — | — | Hết bánh quy ($j = M$) | Dừng. Số trẻ thỏa mãn: `1`. |

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- **Kích thước 2 mảng khác nhau:** $N$ và $M$ có thể khác nhau, điều kiện dừng là `while (i < n && j < m)`.
- **Số trẻ thỏa mãn:** Chính bằng giá trị của chỉ số $i$ sau khi kết thúc vòng lặp.

---

## 4. Lời giải tham khảo
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<long long> g(n), s(m);
    for (int i = 0; i < n; ++i) cin >> g[i];
    for (int j = 0; j < m; ++j) cin >> s[j];

    sort(g.begin(), g.end());
    sort(s.begin(), s.end());

    int i = 0, j = 0;
    while (i < n && j < m) {
        if (s[j] >= g[i]) {
            i++;
            j++;
        } else {
            j++;
        }
    }

    cout << i << "\n";
    return 0;
}
```""",

    "cppb_hct_13_bo_bon_tong_bang_s": r"""# Hướng Dẫn Giảng Dạy: Bộ Bốn Số Có Tổng Bằng S (4-Sum)
Chuyên đề: **Kỹ Thuật Hai Con Trỏ (Two Pointers)**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho dãy $N$ số nguyên và giá trị $S$. Tìm 4 phần tử phân biệt sao cho $A_a + A_b + A_c + A_d = S$.
- **Kỹ thuật Cố định 2 phần tử + Hai con trỏ:**
  - Vét cạn 4 vòng for là $\mathcal{O}(N^4)$ không khả thi.
  - Sắp xếp mảng tăng dần mất $\mathcal{O}(N \log N)$.
  - Cố định $a$ từ $0 \dots N - 4$ và $b$ từ $a + 1 \dots N - 3$.
  - Bài toán quy về tìm 2 số trong đoạn $[b + 1 \dots N - 1]$ có tổng bằng $S - A_a - A_b$.
  - Đặt hai con trỏ $L = b + 1, R = N - 1$.
  - Độ phức tạp tổng thể: $\mathcal{O}(N^3)$, xử lý mượt mà với $N \le 1000$.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: S = 0)
Mẫu thử: `[1, 0, -1, 0, -2, 2]`, $S = 0$. Sắp xếp: `[-2, -1, 0, 0, 1, 2]`.

| Bước | Cố định $(a, b)$ | Target $S - A_a - A_b$ | Hai con trỏ $(L, R)$ | Nghiệm tìm được |
|---|---|---|---|---|
| 1 | $a=0 (A_0=-2), b=1 (A_1=-1)$ | $0 - (-3) = 3$ | $L=2, R=5$ $\implies 0 + 2 = 2 < 3 \implies L=3$ | $0 + 2 = 2 < 3 \implies L=4 \implies$ Hết |
| 2 | $a=0 (A_0=-2), b=2 (A_2=0)$ | $0 - (-2) = 2$ | $L=3 (A_3=0), R=5 (A_5=2) \implies 0 + 2 = 2$ | Khớp! Bộ bốn: `(-2, 0, 0, 2)` |

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- **Tràn số khi cộng 4 số lớn:** Luôn ép kiểu `long long` khi tính tổng 4 số.
- **Biên mảng:** Vòng lặp thứ nhất $a$ chạy tới $N - 4$, vòng lặp thứ hai $b$ chạy tới $N - 3$.

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
    if (!(cin >> n >> s) || n < 4) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    sort(a.begin(), a.end());

    for (int i = 0; i < n - 3; ++i) {
        for (int j = i + 1; j < n - 2; ++j) {
            long long target = s - a[i] - a[j];
            int l = j + 1, r = n - 1;

            while (l < r) {
                long long cur = a[l] + a[r];
                if (cur == target) {
                    cout << a[i] << " " << a[j] << " " << a[l] << " " << a[r] << "\n";
                    return 0;
                } else if (cur < target) {
                    l++;
                } else {
                    r--;
                }
            }
        }
    }

    cout << "-1\n";
    return 0;
}
```""",

    "cppb_hct_14_hai_con_tro_cuc_han": r"""# Hướng Dẫn Giảng Dạy: Cặp Số Tối Ưu Với Chênh Lệch Cực Hạn
Chuyên đề: **Kỹ Thuật Hai Con Trỏ (Two Pointers)**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho hai dãy số nguyên $A$ (kích thước $N$) và $B$ (kích thước $M$). Tìm một phần tử $A_i$ và một phần tử $B_j$ sao cho chênh lệch $|A_i - B_j|$ là nhỏ nhất có thể.
- **Phương pháp tiếp cận — Hai con trỏ trên hai mảng độc lập:**
  - Sắp xếp cả hai mảng $A$ và $B$ tăng dần.
  - Đặt con trỏ $i = 0$ trên mảng $A$, con trỏ $j = 0$ trên mảng $B$.
  - Khởi tạo khoảng cách nhỏ nhất `min_diff = abs(a[0] - b[0])`.
  - Tại mỗi bước:
    - Cập nhật `min_diff = min(min_diff, abs(a[i] - b[j]))`.
    - Nếu `a[i] == b[j]`: Khoảng cách bằng 0 (tuyệt đối tối ưu), kết thúc ngay.
    - Nếu `a[i] < b[j]`: Giá trị $a[i]$ đang nhỏ hơn, muốn thu hẹp khoảng cách tới $b[j]$ thì bắt buộc phải tăng $a[i]$ $\implies$ tăng `i++`.
    - Nếu `a[i] > b[j]`: Tương tự, tăng `j++`.
  - Độ phức tạp: $\mathcal{O}(N \log N + M \log M)$ cho sắp xếp, $\mathcal{O}(N + M)$ cho bước hai con trỏ.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1)
Mẫu thử: $A = [1, 3, 15, 11, 2]$, $B = [23, 127, 235, 19, 8]$.
Sắp xếp: $A = [1, 2, 3, 11, 15]$, $B = [8, 19, 23, 127, 235]$.

| Bước | $(i, j)$ | $(A_i, B_j)$ | Khoảng cách $|A_i - B_j|$ | Cập nhật `min_diff` | Hướng dịch |
|---|---|---|---|---|---|
| 1 | $(0, 0)$ | $(1, 8)$ | $|1 - 8| = 7$ | `min_diff = 7` | $1 < 8 \implies i=1$ |
| 2 | $(1, 0)$ | $(2, 8)$ | $|2 - 8| = 6$ | `min_diff = 6` | $2 < 8 \implies i=2$ |
| 3 | $(2, 0)$ | $(3, 8)$ | $|3 - 8| = 5$ | `min_diff = 5` | $3 < 8 \implies i=3$ |
| 4 | $(3, 0)$ | $(11, 8)$ | $|11 - 8| = 3$ | `min_diff = 3` | $11 > 8 \implies j=1$ |
| 5 | $(3, 1)$ | $(11, 19)$ | $|11 - 19| = 8$ | Giữ `min_diff = 3` | $11 < 19 \implies i=4$ |
| 6 | $(4, 1)$ | $(15, 19)$ | $|15 - 19| = 4$ | Giữ `min_diff = 3` | $15 < 19 \implies$ Hết $A$ |

Khoảng cách nhỏ nhất tìm được là `3` (đạt được tại cặp $11$ và $8$).

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- **Điều kiện dừng:** Vòng lặp dừng khi một trong hai mảng đã duyệt hết: `while (i < n && j < m)`.
- **Độ lệch giá trị âm:** Công thức khoảng cách là $|A_i - B_j|$, cần dùng hàm `abs()` với kiểu `long long`.

---

## 4. Lời giải tham khảo
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<long long> a(n), b(m);
    for (int i = 0; i < n; ++i) cin >> a[i];
    for (int j = 0; j < m; ++j) cin >> b[j];

    sort(a.begin(), a.end());
    sort(b.begin(), b.end());

    int i = 0, j = 0;
    long long min_diff = abs(a[0] - b[0]);

    while (i < n && j < m) {
        long long cur = abs(a[i] - b[j]);
        min_diff = min(min_diff, cur);

        if (a[i] == b[j]) break;
        if (a[i] < b[j]) i++;
        else j++;
    }

    cout << min_diff << "\n";
    return 0;
}
```"""
}

for code, content in guides.items():
    p_dir = BASE_DIR / code
    if p_dir.exists():
        (p_dir / "Huong_Dan_Giang_Day.md").write_text(content, encoding="utf-8")
        print(f"✅ Đã cập nhật chuyên sâu: {code}")
