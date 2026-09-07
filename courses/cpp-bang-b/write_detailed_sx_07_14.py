#!/usr/bin/env python3
"""
Viết lại chuyên sâu, từng bước, số liệu thật cho các bài sx_07 -> sx_14.
"""

from pathlib import Path

BASE_DIR = Path(__file__).parent / "problems"

guides = {
    "cppb_sx_07_sap_xep_tong_chu_so": r"""# Hướng Dẫn Giảng Dạy: Sắp Xếp Theo Tổng Chữ Số
Chuyên đề: **Thuật Toán Sắp Xếp & Khai Thác Trật Tự (Sorting)**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho danh sách $N$ số nguyên dương. Sắp xếp lại dãy số theo quy tắc:
  1. Số nào có **tổng các chữ số** nhỏ hơn sẽ đứng trước.
  2. Nếu hai số có cùng tổng chữ số, số có **giá trị nhỏ hơn** sẽ đứng trước.
- **Phương pháp tiếp cận — Hàm tính tổng chữ số & Custom Comparator:**
  - Viết hàm phụ trợ `int sum_digits(long long n)`: Dùng vòng lặp `while (n > 0)` lấy `n % 10` cộng dồn vào tổng, sau đó `n /= 10`.
  - Định nghĩa hàm so sánh `bool cmp(long long u, long long v)`:
    ```cpp
    int su = sum_digits(u), sv = sum_digits(v);
    if (su != sv) return su < sv;
    return u < v;
    ```
  - Gọi `sort(a.begin(), a.end(), cmp)`. Độ phức tạp thời gian: $\mathcal{O}(N \log N \cdot \log_{10}(\max A))$.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 5 phần tử)
Mẫu thử: $N = 5$, mảng ban đầu `a = [15, 20, 9, 32, 11]`.

| Phần tử $x$ | Tổng chữ số $S(x)$ | Thứ tự ưu tiên sau phân tích |
|---|---|---|
| `20` | $2 + 0 = 2$ | Ưu tiên 1 (tổng chữ số nhỏ nhất là 2) |
| `11` | $1 + 1 = 2$ | Ưu tiên 2 (cùng tổng 2, nhưng $20 > 11$ nên `11` đứng trước `20`) |
| `32` | $3 + 2 = 5$ | Ưu tiên 3 (tổng 5) |
| `15` | $1 + 5 = 6$ | Ưu tiên 4 (tổng 6) |
| `9` | $9$ | Ưu tiên 5 (tổng chữ số lớn nhất là 9) |

Kết quả sau khi sắp xếp chuẩn xác: `11 20 32 15 9`.

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- **Bẫy 1 — Tính lại tổng chữ số quá nhiều lần:** Trong hàm `cmp`, việc gọi `sum_digits` liên tục trong mỗi phép so sánh vẫn chấp nhận được khi $N \le 10^5$. Tuy nhiên, để tối ưu tốc độ tối đa, có thể tiền tính tổng chữ số và lưu dưới dạng `pair<int, long long>` (tổng chữ số, giá trị gốc).
- **Bẫy 2 — Số $0$:** Nếu số có thể bằng $0$, hàm tính tổng chữ số phải xử lý đúng trường hợp này (tổng bằng 0).

---

## 4. Lời giải tham khảo
```cpp
#include <bits/stdc++.h>
using namespace std;

int sum_digits(long long n) {
    int s = 0;
    n = abs(n);
    while (n > 0) {
        s += n % 10;
        n /= 10;
    }
    return s;
}

bool cmp(long long u, long long v) {
    int su = sum_digits(u);
    int sv = sum_digits(v);
    if (su != sv) return su < sv;
    return u < v;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    sort(a.begin(), a.end(), cmp);

    for (int i = 0; i < n; ++i) {
        cout << a[i] << (i == n - 1 ? "" : " ");
    }
    cout << "\n";
    return 0;
}
```""",

    "cppb_sx_08_gom_cum_chenh_lech_k": r"""# Hướng Dẫn Giảng Dạy: Gom Cụm Chênh Lệch Không Quá K
Chuyên đề: **Thuật Toán Sắp Xếp & Khai Thác Trật Tự (Sorting)**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho danh sách $N$ số. Gom các phần tử thành ít nhóm nhất sao cho trong mỗi nhóm, chênh lệch giữa hai phần tử liên tiếp sau khi xếp trong nhóm không vượt quá $K$. Đếm số nhóm tối thiểu cần tạo.
- **Phương pháp tiếp cận — Sắp xếp rồi ngắt cụm:**
  - Sắp xếp toàn bộ mảng $A$ tăng dần.
  - Nhận xét tham lam: Khi mảng đã tăng dần, các phần tử gần nhau nhất nằm liền kề.
  - Nếu $A_{i} - A_{i-1} \le K$, phần tử $A_i$ hoàn toàn có thể nhập chung vào cụm của $A_{i-1}$.
  - Nếu $A_{i} - A_{i-1} > K$, khoảng cách vượt ngưỡng $K$, bắt buộc phải mở một nhóm mới tại $A_i$.
  - Khởi tạo số nhóm `groups = 1`. Duyệt $i$ từ $1$ đến $N - 1$, mỗi khi $A_i - A_{i-1} > K$ thì `groups++`.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: K=3)
Mẫu thử: $N = 6, K = 3$, mảng ban đầu `a = [10, 1, 12, 4, 18, 2]`.

| Bước | Lệnh chạy / Thao tác | Trạng thái | Số nhóm hiện tại |
|---|---|---|---|
| 1 | Sắp xếp mảng | `a = [1, 2, 4, 10, 12, 18]` | `groups = 1` (khởi tạo cụm 1 chứa `1`) |
| 2 | Xét $i=1$: `a[1]-a[0] = 2-1 = 1 <= 3` | Thuộc cụm 1 | `groups = 1` (cụm 1: {1, 2}) |
| 3 | Xét $i=2$: `a[2]-a[1] = 4-2 = 2 <= 3` | Thuộc cụm 1 | `groups = 1` (cụm 1: {1, 2, 4}) |
| 4 | Xét $i=3$: `a[3]-a[2] = 10-4 = 6 > 3` | Bắt đầu cụm mới! | `groups = 2` (cụm 2: {10}) |
| 5 | Xét $i=4$: `a[4]-a[3] = 12-10 = 2 <= 3`| Thuộc cụm 2 | `groups = 2` (cụm 2: {10, 12}) |
| 6 | Xét $i=5$: `a[5]-a[4] = 18-12 = 6 > 3`| Bắt đầu cụm mới! | `groups = 3` (cụm 3: {18}) |
| 7 | Kết thúc | In `3` nhóm | 3 cụm tối ưu là: {1, 2, 4}, {10, 12}, {18} |

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- **Bẫy 1 — Mảng rỗng ($N=0$):** In `0` nếu không có phần tử nào.
- **Bẫy 2 — Nhầm lẫn chênh lệch giữa $\max - \min$ của cụm với chênh lệch 2 phần tử kề:** Đọc kỹ đề bài xem yêu cầu là khoảng cách giữa 2 phần tử kề $\le K$ hay hiệu phần tử lớn nhất và nhỏ nhất của cả nhóm $\le K$.

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
    if (n <= 0) { cout << 0 << "\n"; return 0; }

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    sort(a.begin(), a.end());

    int groups = 1;
    for (int i = 1; i < n; ++i) {
        if (a[i] - a[i - 1] > k) {
            groups++;
        }
    }

    cout << groups << "\n";
    return 0;
}
```""",

    "cppb_sx_09_phan_tu_xuat_hien_nhieu_nhat": r"""# Hướng Dẫn Giảng Dạy: Tìm Phần Tử Xuất Hiện Nhiều Nhất
Chuyên đề: **Thuật Toán Sắp Xếp & Khai Thác Trật Tự (Sorting)**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho dãy số nguyên $A$. Tìm giá trị xuất hiện nhiều lần nhất trong dãy. Nếu có nhiều giá trị có cùng số lần xuất hiện cực đại, chọn giá trị nhỏ nhất.
- **Phương pháp tiếp cận:**
  - Khi chưa học `std::map` (Not Yet Boundary Chương 01), ta dùng kỹ thuật **Sắp xếp để nén đoạn bằng nhau**:
  - Sắp xếp mảng tăng dần. Tất cả các phần tử có cùng giá trị sẽ nằm liên tiếp tạo thành một đoạn $[L \dots R]$.
  - Duyệt qua mảng và đếm độ dài đoạn các phần tử bằng nhau liên tiếp `cur_count`.
  - Khi đoạn kết thúc (hoặc đến hết mảng), so sánh `cur_count` với `max_count` để cập nhật đáp số.
  - Nhờ đã sắp xếp tăng dần, nếu gặp giá trị sau có tần số chỉ ngang bằng (`cur_count == max_count`), ta không cập nhật, từ đó tự động giữ lại giá trị nhỏ hơn xuất hiện trước.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 8 phần tử)
Mẫu thử: $N = 8$, mảng ban đầu `a = [3, 1, 4, 1, 5, 1, 4, 4]`.

| Bước | Thao tác | Đoạn giá trị bằng nhau | Tần số | Cập nhật `(ans, max_count)` |
|---|---|---|---|---|
| 1 | Sắp xếp mảng | `[1, 1, 1, 3, 4, 4, 4, 5]` | — | Khởi tạo ban đầu |
| 2 | Duyệt khối số `1` | 3 số `1` liên tiếp | `count = 3` | `ans = 1, max_count = 3` |
| 3 | Duyệt khối số `3` | 1 số `3` | `count = 1` | Giữ nguyên (1 < 3) |
| 4 | Duyệt khối số `4` | 3 số `4` liên tiếp | `count = 3` | Tần số hòa (3 == 3), nhưng số 1 nhỏ hơn số 4 nên giữ nguyên `ans = 1` |
| 5 | Duyệt khối số `5` | 1 số `5` | `count = 1` | Giữ nguyên (1 < 3) |
| 6 | Kết thúc | — | — | In ra `1` với tần số `3` |

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- **Bẫy 1 — Quên cập nhật đoạn cuối cùng:** Khi vòng lặp chạy đến phần tử cuối cùng của mảng, đoạn bằng nhau kết thúc mà không có phần tử phía sau để kích hoạt điều kiện đổi giá trị. Cần xử lý đoạn cuối sau khi thoát vòng lặp.
- **Bẫy 2 — Hòa tần số:** Đề bài yêu cầu lấy số nhỏ hơn khi tần số bằng nhau. Vì mảng tăng dần, chỉ cập nhật khi `cur_count > max_count` (dấu `>` nghiêm ngặt).

---

## 4. Lời giải tham khảo
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n) || n <= 0) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    sort(a.begin(), a.end());

    long long best_val = a[0];
    int max_freq = 1;

    long long cur_val = a[0];
    int cur_freq = 1;

    for (int i = 1; i < n; ++i) {
        if (a[i] == cur_val) {
            cur_freq++;
        } else {
            if (cur_freq > max_freq) {
                max_freq = cur_freq;
                best_val = cur_val;
            }
            cur_val = a[i];
            cur_freq = 1;
        }
    }
    if (cur_freq > max_freq) {
        max_freq = cur_freq;
        best_val = cur_val;
    }

    cout << best_val << " " << max_freq << "\n";
    return 0;
}
```""",

    "cppb_sx_10_sap_xep_luu_vi_tri": r"""# Hướng Dẫn Giảng Dạy: Sắp Xếp Lưu Vị Trí Ban Đầu
Chuyên đề: **Thuật Toán Sắp Xếp & Khai Thác Trật Tự (Sorting)**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho dãy $N$ số. Sắp xếp dãy số tăng dần, đồng thời in ra chỉ số vị trí ban đầu (1-based index) của từng phần tử trong dãy gốc.
- **Phương pháp tiếp cận — Vector lồng nhau `vector<vector<long long>>`:**
  - Theo quy chuẩn dữ liệu tối giản của iKHEDU, ta ưu tiên sử dụng `vector<vector<long long>>` (mỗi phần tử là một vector 2 phần tử `[giá_trị, chỉ_số_gốc]`).
  - Cơ chế so sánh mặc định của thư viện C++ đối với vector: so sánh phần tử đầu tiên trước (`giá_trị`), nếu bằng nhau so sánh tiếp phần tử thứ hai (`chỉ_số_gốc`). Điều này hoàn toàn tự động và tự nhiên mà không cần viết comparator phức tạp!
  - Sau khi `sort(a.begin(), a.end())`, ta in ra `a[i][1]` chính là vị trí gốc ban đầu.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 5 phần tử)
Mẫu thử: $N = 5$, mảng ban đầu: giá trị `[40, 10, 50, 20, 10]` tương ứng vị trí 1-based `[1, 2, 3, 4, 5]`.

| Bước | Dữ liệu lưu trữ `[giá trị, vị trí]` | Trạng thái sau `sort` | Giải thích thứ tự |
|---|---|---|---|
| 1 | `[40, 1], [10, 2], [50, 3], [20, 4], [10, 5]` | `[10, 2]` | Giá trị nhỏ nhất là 10, ở vị trí 2 |
| 2 | — | `[10, 5]` | Cùng giá trị 10, vị trí 5 đứng sau vị trí 2 |
| 3 | — | `[20, 4]` | Giá trị tiếp theo là 20, ở vị trí 4 |
| 4 | — | `[40, 1]` | Giá trị tiếp theo là 40, ở vị trí 1 |
| 5 | — | `[50, 3]` | Giá trị lớn nhất là 50, ở vị trí 3 |

Danh sách vị trí ban đầu in ra: `2 5 4 1 3`.

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- **Bẫy 1 — 1-based index vs 0-based index:** Đề bài yêu cầu in chỉ số từ $1$ đến $N$, nếu lưu vòng lặp `i` từ 0 sẽ bị lệch 1 đơn vị. Cần lưu `i + 1`.
- **Bẫy 2 — Bằng nhau về giá trị:** Khi hai phần tử có cùng giá trị, việc ưu tiên phần tử nào xuất hiện trước trong dãy gốc đảm bảo tính ổn định (Stable Sort). Vector lồng nhau tự động so sánh chỉ số `[0] == [0] -> so sánh [1]` nên hoàn toàn đáp ứng được tiêu chí này.

---

## 4. Lời giải tham khảo
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<vector<long long>> a(n, vector<long long>(2));
    for (int i = 0; i < n; ++i) {
        cin >> a[i][0];
        a[i][1] = i + 1; // Lưu vị trí ban đầu 1-based
    }

    sort(a.begin(), a.end());

    for (int i = 0; i < n; ++i) {
        cout << a[i][1] << (i == n - 1 ? "" : " ");
    }
    cout << "\n";
    return 0;
}
```""",

    "cppb_sx_11_ghep_so_lon_nhat": r"""# Hướng Dẫn Giảng Dạy: Ghép Chuỗi Tạo Số Lớn Nhất
Chuyên đề: **Thuật Toán Sắp Xếp & Khai Thác Trật Tự (Sorting)**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho danh sách $N$ số nguyên không âm. Ghép toàn bộ các số này lại thành một số nguyên lớn nhất có thể.
- **Tại sao so sánh thông thường bị sai?**
  - Nếu so sánh theo thứ tự từ điển thông thường (`"9" > "34"` đúng, nhưng `"3" > "30"` thì `"30"` lại dài hơn `"3"`). Nếu xếp `"30"` trước `"3"` ta được `"303"`, trong khi `"3"` trước `"30"` cho `"330"` lớn hơn!
- **Tính chất bắc cầu của phép ghép (Greedy Comparator):**
  - Để quyết định giữa hai chuỗi $u$ và $v$ chuỗi nào nên đứng trước, ta so sánh trực tiếp kết quả của hai cách ghép:
    $$\text{Nếu } u + v > v + u \implies u \text{ phải đứng trước } v.$$
  - Quan hệ này thỏa mãn tính chất phản đối xứng và bắc cầu (Strict Weak Ordering), cho phép hàm `sort` định hình đúng toàn bộ dãy ghép.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 4 số)
Mẫu thử: Danh sách gồm 4 chuỗi `["3", "30", "34", "5", "9"]`.

| Cặp so sánh $(u, v)$ | Ghép $u + v$ | Ghép $v + u$ | Quyết định |
|---|---|---|---|
| `"9"` và `"5"` | `"95"` | `"59"` | `"9"` đứng trước `"5"` |
| `"34"` và `"3"` | `"343"` | `"334"` | `"34"` đứng trước `"3"` |
| `"3"` và `"30"` | `"330"` | `"303"` | `"3"` đứng trước `"30"` |

Sau khi sắp xếp: `["9", "5", "34", "3", "30"]`.
Ghép lại được số lớn nhất: `9534330`.

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- **Bẫy 1 — Toàn số 0:** Nếu input gồm các số `[0, 0, 0]`, kết quả ghép sẽ là `"000"`. Đáp số hợp lệ của bài toán khi đó chỉ là một số `"0"`. Cần kiểm tra nếu phần tử đầu tiên sau khi sắp xếp là `"0"` thì in ngay `"0"` và kết thúc.
- **Bẫy 2 — Dùng dấu `>=` trong comparator:** Viết `return u + v >= v + u;` sẽ gây lỗi vi phạm Strict Weak Ordering dẫn đến crash chương trình khi gặp hai số giống hệt nhau.

---

## 4. Lời giải tham khảo
```cpp
#include <bits/stdc++.h>
using namespace std;

bool cmp(const string &u, const string &v) {
    return u + v > v + u;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<string> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    sort(a.begin(), a.end(), cmp);

    if (a[0] == "0") {
        cout << "0\n";
        return 0;
    }

    for (int i = 0; i < n; ++i) {
        cout << a[i];
    }
    cout << "\n";
    return 0;
}
```""",

    "cppb_sx_12_bang_diem_hoc_sinh": r"""# Hướng Dẫn Giảng Dạy: Bảng Điểm Học Sinh Đa Trường
Chuyên đề: **Thuật Toán Sắp Xếp & Khai Thác Trật Tự (Sorting)**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho danh sách $N$ học sinh gồm Tên, Điểm Toán, Điểm Tin. Cần xếp hạng học sinh theo các tiêu chí ưu tiên:
  1. Tổng điểm (Toán + Tin) cao hơn xếp trước.
  2. Nếu tổng điểm bằng nhau, học sinh có điểm Tin cao hơn xếp trước.
  3. Nếu vẫn bằng nhau, xếp theo thứ tự từ điển của Tên học sinh.
- **Phương pháp tiếp cận — Struct và Comparator đa tiêu chí:**
  - Khai báo kiểu cấu trúc `Student` gồm các trường: `name` (chuỗi), `math` (số), `inf` (số), `total` (tổng điểm).
  - Viết hàm so sánh đối chiếu lần lượt từng tiêu chí:
    ```cpp
    bool cmp(const Student &a, const Student &b) {
        if (a.total != b.total) return a.total > b.total;
        if (a.inf != b.inf) return a.inf > b.inf;
        return a.name < b.name;
    }
    ```

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 3 học sinh)
Mẫu thử:
1. `An`: Toán 9, Tin 10 $\implies$ Tổng 19.
2. `Binh`: Toán 10, Tin 9 $\implies$ Tổng 19.
3. `Cuong`: Toán 10, Tin 10 $\implies$ Tổng 20.

| Xếp hạng | Học sinh | Tổng điểm | Điểm Tin | Thứ tự từ điển | Lý do xếp hạng |
|---|---|---|---|---|---|
| 1 | `Cuong` | 20 | 10 | Cuong | Tổng điểm cao nhất (20 điểm) |
| 2 | `An` | 19 | 10 | An | Cùng tổng 19, nhưng Tin 10 > Tin 9 |
| 3 | `Binh` | 19 | 9 | Binh | Cùng tổng 19, điểm Tin thấp hơn An |

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- **Bẫy 1 — So sánh chuỗi:** Khi đối chiếu tên học sinh theo thứ tự từ điển tăng dần, dùng phép so sánh `a.name < b.name` (chứ không dùng `>`).
- **Bẫy 2 — Nhập tên có khoảng trắng:** Nếu đề bài quy định tên là một từ viết liền không dấu, dùng `cin >> s.name`. Nếu tên có khoảng trắng, bắt buộc dùng `getline(cin, s.name)` và nhớ xóa bộ đệm bàn phím bằng `cin.ignore()`.

---

## 4. Lời giải tham khảo
```cpp
#include <bits/stdc++.h>
using namespace std;

struct Student {
    string name;
    int math, inf, total;
};

bool cmp(const Student &a, const Student &b) {
    if (a.total != b.total) return a.total > b.total;
    if (a.inf != b.inf) return a.inf > b.inf;
    return a.name < b.name;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<Student> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i].name >> a[i].math >> a[i].inf;
        a[i].total = a[i].math + a[i].inf;
    }

    sort(a.begin(), a.end(), cmp);

    for (int i = 0; i < n; ++i) {
        cout << a[i].name << " " << a[i].total << " " << a[i].inf << "\n";
    }
    return 0;
}
```""",

    "cppb_sx_13_bang_xep_hang_the_thao": r"""# Hướng Dẫn Giảng Dạy: Bảng Xếp Hạng Giải Đấu Thể Thao
Chuyên đề: **Thuật Toán Sắp Xếp & Khai Thác Trật Tự (Sorting)**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Xây dựng bảng xếp hạng bóng đá cho $N$ đội tuyển dựa trên các chỉ số:
  1. Số điểm (Points) giảm dần.
  2. Hiệu số bàn thắng bại (Goal Difference) giảm dần.
  3. Số bàn thắng ghi được (Goals Scored) giảm dần.
  4. Tên đội bóng theo thứ tự từ điển tăng dần.
- **Phương pháp tiếp cận:** Sử dụng `struct Team` và viết comparator chuẩn xác theo đúng thứ tự ưu tiên 4 tầng.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1)
Mẫu thử:
- Đội `A`: Điểm 6, Hiệu số +3, Bàn thắng 5
- Đội `B`: Điểm 6, Hiệu số +3, Bàn thắng 7
- Đội `C`: Điểm 7, Hiệu số +1, Bàn thắng 3

| Hạng | Đội | Điểm | Hiệu số | Bàn thắng | Phân tích xếp hạng |
|---|---|---|---|---|---|
| 1 | `C` | 7 | +1 | 3 | Điểm số cao nhất (7 điểm) |
| 2 | `B` | 6 | +3 | 7 | Cùng 6 điểm, cùng hiệu số +3, nhưng bàn thắng 7 > 5 |
| 3 | `A` | 6 | +3 | 5 | Bàn thắng ít hơn đội B |

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- **Bẫy 1 — Hiệu số có thể âm:** Hiệu số bàn thắng bại là số nguyên có dấu (ví dụ $-2, -5$), cần giữ đúng kiểu dữ liệu `int` có dấu khi trừ bàn thắng cho bàn thua.
- **Bẫy 2 — Bàn thắng đối kháng:** Tuân thủ đúng thứ tự ưu tiên đề bài quy định, không tự ý thêm bớt tiêu chí.

---

## 4. Lời giải tham khảo
```cpp
#include <bits/stdc++.h>
using namespace std;

struct Team {
    string name;
    int points;
    int diff;
    int scored;
};

bool cmp(const Team &u, const Team &v) {
    if (u.points != v.points) return u.points > v.points;
    if (u.diff != v.diff) return u.diff > v.diff;
    if (u.scored != v.scored) return u.scored > v.scored;
    return u.name < v.name;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<Team> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i].name >> a[i].points >> a[i].diff >> a[i].scored;
    }

    sort(a.begin(), a.end(), cmp);

    for (int i = 0; i < n; ++i) {
        cout << a[i].name << " " << a[i].points << " " << a[i].diff << " " << a[i].scored << "\n";
    }
    return 0;
}
```""",

    "cppb_sx_14_khac_phuc_strict_weak_ordering": r"""# Hướng Dẫn Giảng Dạy: Sắp Xếp Đoạn Thẳng Không Giao Lỗi
Chuyên đề: **Thuật Toán Sắp Xếp & Khai Thác Trật Tự (Sorting)**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho danh sách $N$ đoạn thẳng trên trục số, đoạn thứ $i$ có điểm đầu $L_i$ và điểm cuối $R_i$. Sắp xếp các đoạn thẳng theo quy tắc:
  1. Điểm đầu $L$ tăng dần.
  2. Nếu điểm đầu trùng nhau ($L_u = L_v$), sắp xếp theo điểm cuối $R$ giảm dần (đoạn dài hơn bao đoạn ngắn hơn được xếp trước).
  - Bài toán này đặc biệt nhấn mạnh vào **tiên đề Strict Weak Ordering** trong thư viện chuẩn C++.
- **Nguyên lý Strict Weak Ordering:**
  - Tiên đề toán học đòi hỏi: Với mọi phần tử $x$, biểu thức $cmp(x, x)$ **bắt buộc phải trả về `false`**.
  - Nếu lập trình viên sơ suất viết `if (u.L <= v.L)` hoặc `return u.R >= v.R;`, thì khi so sánh hai đoạn thẳng giống hệt nhau, hàm sẽ trả về `true` cho cả hai chiều $cmp(x, y)$ và $cmp(y, x)$, dẫn đến vi phạm tiên đề và gây crash chương trình khi $N$ lớn.
  - Comparator chuẩn:
    ```cpp
    bool cmp(const pair<long long, long long> &u, const pair<long long, long long> &v) {
        if (u.first != v.first) return u.first < v.first;
        return u.second > v.second; // Dấu > nghiêm ngặt, tuyệt đối không dùng >=
    }
    ```

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 4 đoạn thẳng)
Mẫu thử: 4 đoạn thẳng `[(1, 4), (2, 6), (1, 8), (2, 3)]`.

| Đoạn thẳng | Điểm $L$ | Điểm $R$ | Phân tích ưu tiên |
|---|---|---|---|
| `(1, 8)` | 1 | 8 | Cùng $L=1$, nhưng $R=8 > 4$ nên đứng trước `(1, 4)` |
| `(1, 4)` | 1 | 4 | $L=1$ |
| `(2, 6)` | 2 | 6 | Cùng $L=2$, nhưng $R=6 > 3$ nên đứng trước `(2, 3)` |
| `(2, 3)` | 2 | 3 | $L=2$ |

Thứ tự sau sắp xếp: `(1, 8), (1, 4), (2, 6), (2, 3)`.

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- **Tử huyệt lập trình — Lỗi RE / TLE bí ẩn do vi phạm Strict Weak Ordering:** Rất nhiều thí sinh khi đi thi gặp lỗi chấm bài Runtime Error mà không hiểu lý do vì test máy chấm nhỏ thì chạy đúng nhưng test lớn ($N \ge 10^4$) thì bị crash. Nguyên nhân 99% là do dùng dấu `<=` hoặc `>=` trong hàm so sánh.
- **Quy tắc vàng:** Trong hàm so sánh của `std::sort`, **chỉ được dùng dấu `<` hoặc `>` nghiêm ngặt**, tuyệt đối cấm dấu bằng `=`.

---

## 4. Lời giải tham khảo
```cpp
#include <bits/stdc++.h>
using namespace std;

struct Segment {
    long long l, r;
};

bool cmp(const Segment &u, const Segment &v) {
    if (u.l != v.l) return u.l < v.l;
    return u.r > v.r; // Nghiêm ngặt, cấm dùng >=
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<Segment> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i].l >> a[i].r;
    }

    sort(a.begin(), a.end(), cmp);

    for (int i = 0; i < n; ++i) {
        cout << a[i].l << " " << a[i].r << "\n";
    }
    return 0;
}
```"""
}

for code, content in guides.items():
    p_dir = BASE_DIR / code
    if p_dir.exists():
        (p_dir / "Huong_Dan_Giang_Day.md").write_text(content, encoding="utf-8")
        print(f"✅ Đã cập nhật chuyên sâu: {code}")
