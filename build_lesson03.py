import random
from generate_module01_all_problems import build_problem

LESSON03_PROBLEMS = [
    # 1. IKH-0301
    {
        "id": "IKH-0301",
        "slug": "cpp1_03_cua_so_k",
        "title": "Tổng Cửa Sổ Cố Định K",
        "statement": """# Tổng Cửa Sổ Cố Định K

## Bối cảnh
Cho một dãy gồm $N$ số nguyên $A_1, A_2, \\dots, A_N$ và một số nguyên dương $K$ ($K \\le N$). Hãy tìm tổng lớn nhất của một đoạn con gồm đúng $K$ phần tử liên tiếp.

## Input
- Dòng 1: Chứa 2 số nguyên $N$ và $K$ ($1 \\le K \\le N \\le 10^5$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \\dots, A_N$ ($-10^9 \\le A_i \\le 10^9$).

## Output
- In ra một số nguyên duy nhất là tổng lớn nhất của đoạn $K$ phần tử liên tiếp.

## Sample 1
### Input
```text
6 3
2 1 5 1 3 2
```
### Output
```text
9
```
### Giải thích
Đoạn $[5, 1, 3]$ có tổng $5 + 1 + 3 = 9$ là lớn nhất.

## Ràng buộc
- $100\\%$ số test có $N \\le 10^5$.
- Thời gian: $1.0\\text{s}$, Bộ nhớ: $256\\text{MB}$.
""",
        "guide": """# Hướng Dẫn Giảng Dạy: Cửa Sổ Cố Định K
- Khởi tạo tổng $K$ phần tử đầu tiên. Trượt cửa sổ: `cur_sum += a[i] - a[i - k]`.
- Độ phức tạp: $\\mathcal{O}(N)$.
""",
        "solution_cpp": """#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    long long cur_sum = 0;
    for (int i = 0; i < k; ++i) cur_sum += a[i];

    long long max_sum = cur_sum;
    for (int i = k; i < n; ++i) {
        cur_sum += a[i] - a[i - k];
        max_sum = max(max_sum, cur_sum);
    }

    cout << max_sum << "\\n";
    return 0;
}
""",
        "gen_tests": lambda: [
            {"n": 6, "k": 3, "arr": [2, 1, 5, 1, 3, 2]},
            {"n": 1, "k": 1, "arr": [-5]},
            {"n": 5, "k": 5, "arr": [1, 2, 3, 4, 5]},
            {"n": 10, "k": 4, "arr": [random.randint(-10, 10) for _ in range(10)]},
            {"n": 100, "k": 10, "arr": [random.randint(-100, 100) for _ in range(100)]},
            {"n": 1000, "k": 50, "arr": [random.randint(-1000, 1000) for _ in range(1000)]},
            {"n": 5000, "k": 200, "arr": [random.randint(-10**6, 10**6) for _ in range(5000)]},
            {"n": 20000, "k": 1000, "arr": [random.randint(-10**9, 10**9) for _ in range(20000)]},
            {"n": 50000, "k": 5000, "arr": [random.randint(-10**9, 10**9) for _ in range(50000)]},
            {"n": 100000, "k": 1, "arr": [random.randint(-10**9, 10**9) for _ in range(100000)]},
            {"n": 100000, "k": 100000, "arr": [random.randint(-10**9, 10**9) for _ in range(100000)]},
            {"n": 100000, "k": 50000, "arr": [random.randint(-10**9, 10**9) for _ in range(100000)]},
            {"n": 100000, "k": 100, "arr": [random.randint(-10**9, 10**9) for _ in range(100000)]},
            {"n": 100000, "k": 500, "arr": [10**9] * 100000},
            {"n": 100000, "k": 500, "arr": [-10**9] * 100000},
            {"n": 100000, "k": 1234, "arr": [random.randint(-10**9, 10**9) for _ in range(100000)]},
            {"n": 100000, "k": 4321, "arr": [random.randint(-10**9, 10**9) for _ in range(100000)]},
            {"n": 100000, "k": 9999, "arr": [random.randint(-10**9, 10**9) for _ in range(100000)]},
            {"n": 100000, "k": 25000, "arr": [random.randint(-10**9, 10**9) for _ in range(100000)]},
            {"n": 100000, "k": 75000, "arr": [random.randint(-10**9, 10**9) for _ in range(100000)]},
        ],
        "format_inp": lambda t: f"{t['n']} {t['k']}\n" + " ".join(map(str, t['arr'])) + "\n"
    },

    # 2. IKH-0302
    {
        "id": "IKH-0302",
        "slug": "cpp1_03_trung_binh_k_lon_nhat",
        "title": "Giá Trị Trung Bình Lớn Nhất Của Đoạn K",
        "statement": """# Giá Trị Trung Bình Lớn Nhất Của Đoạn K

## Bối cảnh
Cho một dãy gồm $N$ số nguyên $A_1, A_2, \\dots, A_N$ và số nguyên $K$ ($K \\le N$). Hãy tìm giá trị trung bình cộng lớn nhất của một đoạn con gồm $K$ phần tử liên tiếp.

## Input
- Dòng 1: Chứa 2 số nguyên $N$ và $K$ ($1 \\le K \\le N \\le 10^5$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \\dots, A_N$ ($-10^9 \\le A_i \\le 10^9$).

## Output
- In ra một số thực duy nhất là giá trị trung bình lớn nhất, làm tròn đúng 3 chữ số thập phân sau dấu phẩy.

## Sample 1
### Input
```text
4 2
1 12 -5 6
```
### Output
```text
6.500
```
### Giải thích
Đoạn $[1, 12]$ có trung bình $(1 + 12)/2 = 6.5$.

## Ràng buộc
- $100\\%$ số test có $N \\le 10^5$.
- Thời gian: $1.0\\text{s}$, Bộ nhớ: $256\\text{MB}$.
""",
        "guide": """# Hướng Dẫn Giảng Dạy: Trung Bình Cửa Sổ K
- Tìm max tổng đoạn $K$ bằng Sliding Window, sau đó chia cho $K$ dạng `double`.
""",
        "solution_cpp": """#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    long long cur_sum = 0;
    for (int i = 0; i < k; ++i) cur_sum += a[i];

    long long max_sum = cur_sum;
    for (int i = k; i < n; ++i) {
        cur_sum += a[i] - a[i - k];
        max_sum = max(max_sum, cur_sum);
    }

    double ans = (double)max_sum / k;
    cout << fixed << setprecision(3) << ans << "\\n";
    return 0;
}
""",
        "gen_tests": lambda: [
            {"n": 4, "k": 2, "arr": [1, 12, -5, 6]},
            {"n": 1, "k": 1, "arr": [7]},
            {"n": 5, "k": 3, "arr": [10, 20, 30, 40, 50]},
            {"n": 10, "k": 4, "arr": [random.randint(-10, 10) for _ in range(10)]},
            {"n": 100, "k": 15, "arr": [random.randint(-100, 100) for _ in range(100)]},
            {"n": 1000, "k": 50, "arr": [random.randint(-1000, 1000) for _ in range(1000)]},
            {"n": 5000, "k": 200, "arr": [random.randint(-10**6, 10**6) for _ in range(5000)]},
            {"n": 20000, "k": 1000, "arr": [random.randint(-10**9, 10**9) for _ in range(20000)]},
            {"n": 50000, "k": 5000, "arr": [random.randint(-10**9, 10**9) for _ in range(50000)]},
            {"n": 100000, "k": 1, "arr": [random.randint(-10**9, 10**9) for _ in range(100000)]},
            {"n": 100000, "k": 100000, "arr": [random.randint(-10**9, 10**9) for _ in range(100000)]},
            {"n": 100000, "k": 33333, "arr": [random.randint(-10**9, 10**9) for _ in range(100000)]},
            {"n": 100000, "k": 777, "arr": [random.randint(-10**9, 10**9) for _ in range(100000)]},
            {"n": 100000, "k": 500, "arr": [10**9] * 100000},
            {"n": 100000, "k": 500, "arr": [-10**9] * 100000},
            {"n": 100000, "k": 1234, "arr": [random.randint(-10**9, 10**9) for _ in range(100000)]},
            {"n": 100000, "k": 4321, "arr": [random.randint(-10**9, 10**9) for _ in range(100000)]},
            {"n": 100000, "k": 9999, "arr": [random.randint(-10**9, 10**9) for _ in range(100000)]},
            {"n": 100000, "k": 25000, "arr": [random.randint(-10**9, 10**9) for _ in range(100000)]},
            {"n": 100000, "k": 75000, "arr": [random.randint(-10**9, 10**9) for _ in range(100000)]},
        ],
        "format_inp": lambda t: f"{t['n']} {t['k']}\n" + " ".join(map(str, t['arr'])) + "\n"
    },

    # 3. IKH-0303
    {
        "id": "IKH-0303",
        "slug": "cpp1_03_doan_con_ngan_nhat_tong_s",
        "title": "Đoạn Con Ngắn Nhất Có Tổng Đạt S",
        "statement": """# Đoạn Con Ngắn Nhất Có Tổng Đạt S

## Bối cảnh
Cho dãy gồm $N$ số nguyên **không âm** $A_1, A_2, \\dots, A_N$ và một số nguyên dương $S$. Hãy tìm độ dài nhỏ nhất của một đoạn con liên tiếp có tổng các phần tử $\\ge S$. Nếu không có đoạn con nào thỏa mãn, in ra `-1`.

## Input
- Dòng 1: Chứa 2 số nguyên $N$ và $S$ ($1 \\le N \\le 10^5, 1 \\le S \\le 10^{14}$).
- Dòng 2: $N$ số nguyên không âm $A_1, A_2, \\dots, A_N$ ($0 \\le A_i \\le 10^9$).

## Output
- In ra độ dài ngắn nhất hoặc `-1`.

## Sample 1
### Input
```text
6 7
2 3 1 2 4 3
```
### Output
```text
2
```
### Giải thích
Đoạn $[4, 3]$ có tổng là $7 \\ge 7$ với độ dài là 2.

## Ràng buộc
- $100\\%$ số test có $N \\le 10^5$.
- Thời gian: $1.0\\text{s}$, Bộ nhớ: $256\\text{MB}$.
""",
        "guide": """# Hướng Dẫn Giảng Dạy: Đoạn Con Ngắn Nhất Tổng >= S
- Sliding Window co giãn: Mở rộng $R$. Khi `cur_sum >= S` thì co $L$ và cập nhật `min_len`.
""",
        "solution_cpp": """#include <bits/stdc++.h>
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
            ++l;
        }
    }

    if (min_len > n) cout << -1 << "\\n";
    else cout << min_len << "\\n";
    return 0;
}
""",
        "gen_tests": lambda: [
            {"n": 6, "s": 7, "arr": [2, 3, 1, 2, 4, 3]},
            {"n": 1, "s": 10, "arr": [10]},
            {"n": 1, "s": 10, "arr": [5]},
            {"n": 5, "s": 15, "arr": [1, 2, 3, 4, 5]},
            {"n": 10, "s": 20, "arr": [random.randint(0, 10) for _ in range(10)]},
            {"n": 100, "s": 200, "arr": [random.randint(0, 20) for _ in range(100)]},
            {"n": 1000, "s": 5000, "arr": [random.randint(0, 100) for _ in range(1000)]},
            {"n": 5000, "s": 10**6, "arr": [random.randint(0, 1000) for _ in range(5000)]},
            {"n": 20000, "s": 10**8, "arr": [random.randint(0, 10**5) for _ in range(20000)]},
            {"n": 50000, "s": 10**10, "arr": [random.randint(0, 10**6) for _ in range(50000)]},
            {"n": 100000, "s": 100000, "arr": [1] * 100000},
            {"n": 100000, "s": 100001, "arr": [1] * 100000},
            {"n": 100000, "s": 10**14, "arr": [random.randint(0, 10**9) for _ in range(100000)]},
            {"n": 100000, "s": 10**9, "arr": [random.randint(0, 10**9) for _ in range(100000)]},
            {"n": 100000, "s": 5 * 10**13, "arr": [random.randint(0, 10**9) for _ in range(100000)]},
            {"n": 100000, "s": 123456789, "arr": [random.randint(0, 10**9) for _ in range(100000)]},
            {"n": 100000, "s": 999999999, "arr": [random.randint(0, 10**9) for _ in range(100000)]},
            {"n": 100000, "s": 777777777, "arr": [random.randint(0, 10**9) for _ in range(100000)]},
            {"n": 100000, "s": 888888888, "arr": [random.randint(0, 10**9) for _ in range(100000)]},
            {"n": 100000, "s": 1, "arr": [0] * 99999 + [1]},
        ],
        "format_inp": lambda t: f"{t['n']} {t['s']}\n" + " ".join(map(str, t['arr'])) + "\n"
    },

    # 4. IKH-0304
    {
        "id": "IKH-0304",
        "slug": "cpp1_03_doan_con_dai_nhat_tong_s",
        "title": "Đoạn Con Dài Nhất Có Tổng Không Quá S",
        "statement": """# Đoạn Con Dài Nhất Có Tổng Không Quá S

## Bối cảnh
Cho dãy gồm $N$ số nguyên **không âm** $A_1, A_2, \\dots, A_N$ và một số nguyên dương $S$. Hãy tìm độ dài lớn nhất của một đoạn con liên tiếp có tổng các phần tử $\\le S$.

## Input
- Dòng 1: Chứa 2 số nguyên $N$ và $S$ ($1 \\le N \\le 2 \\cdot 10^5, 1 \\le S \\le 10^{14}$).
- Dòng 2: $N$ số nguyên không âm $A_1, A_2, \\dots, A_N$ ($0 \\le A_i \\le 10^9$).

## Output
- In ra một số nguyên duy nhất là độ dài lớn nhất của đoạn con thỏa mãn.

## Sample 1
### Input
```text
5 7
3 1 2 1 4
```
### Output
```text
4
```
### Giải thích
Đoạn $[3, 1, 2, 1]$ có tổng là $7 \\le 7$ với độ dài là 4.

## Ràng buộc
- $100\\%$ số test có $N \\le 2 \\cdot 10^5$.
- Thời gian: $1.0\\text{s}$, Bộ nhớ: $256\\text{MB}$.
""",
        "guide": """# Hướng Dẫn Giảng Dạy: Đoạn Con Dài Nhất Tổng <= S
- Mở rộng $R$. Khi `cur_sum > S` thì co $L$. Cập nhật `max_len = max(max_len, R - L + 1)`.
""",
        "solution_cpp": """#include <bits/stdc++.h>
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
        while (cur_sum > s) {
            cur_sum -= a[l];
            ++l;
        }
        max_len = max(max_len, r - l + 1);
    }

    cout << max_len << "\\n";
    return 0;
}
""",
        "gen_tests": lambda: [
            {"n": 5, "s": 7, "arr": [3, 1, 2, 1, 4]},
            {"n": 1, "s": 5, "arr": [10]},
            {"n": 1, "s": 10, "arr": [5]},
            {"n": 5, "s": 15, "arr": [1, 2, 3, 4, 5]},
            {"n": 10, "s": 10, "arr": [random.randint(0, 5) for _ in range(10)]},
            {"n": 100, "s": 50, "arr": [random.randint(0, 10) for _ in range(100)]},
            {"n": 1000, "s": 500, "arr": [random.randint(0, 10) for _ in range(1000)]},
            {"n": 5000, "s": 10**5, "arr": [random.randint(0, 100) for _ in range(5000)]},
            {"n": 20000, "s": 10**6, "arr": [random.randint(0, 1000) for _ in range(20000)]},
            {"n": 50000, "s": 10**8, "arr": [random.randint(0, 10**5) for _ in range(50000)]},
            {"n": 100000, "s": 50000, "arr": [1] * 100000},
            {"n": 200000, "s": 0, "arr": [random.randint(1, 10) for _ in range(200000)]},
            {"n": 200000, "s": 10**14, "arr": [random.randint(0, 10**9) for _ in range(200000)]},
            {"n": 200000, "s": 10**9, "arr": [random.randint(0, 10**9) for _ in range(200000)]},
            {"n": 200000, "s": 5 * 10**13, "arr": [random.randint(0, 10**9) for _ in range(200000)]},
            {"n": 200000, "s": 123456789, "arr": [random.randint(0, 10**9) for _ in range(200000)]},
            {"n": 200000, "s": 999999999, "arr": [random.randint(0, 10**9) for _ in range(200000)]},
            {"n": 200000, "s": 777777777, "arr": [random.randint(0, 10**9) for _ in range(200000)]},
            {"n": 200000, "s": 888888888, "arr": [random.randint(0, 10**9) for _ in range(200000)]},
            {"n": 200000, "s": 1000, "arr": [1] * 200000},
        ],
        "format_inp": lambda t: f"{t['n']} {t['s']}\n" + " ".join(map(str, t['arr'])) + "\n"
    },

    # 5. IKH-0305
    {
        "id": "IKH-0305",
        "slug": "cpp1_03_lat_bit_k_so_khong",
        "title": "Đoạn Con Chứa Tối Đa K Số 0 (Lật Bit)",
        "statement": """# Đoạn Con Chứa Tối Đa K Số 0 (Lật Bit)

## Bối cảnh
Cho một mảng nhị phân $A$ gồm $N$ phần tử ($A_i \\in \\{0, 1\\}$) và số nguyên không âm $K$. Bạn được phép đổi tối đa $K$ số 0 thành số 1. Hãy tìm độ dài lớn nhất của dãy số 1 liên tiếp có thể tạo được.

## Input
- Dòng 1: Chứa 2 số nguyên $N$ và $K$ ($1 \\le N \\le 10^5, 0 \\le K \\le N$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \\dots, A_N$ ($A_i \\in \\{0, 1\\}$).

## Output
- In ra độ dài lớn nhất tìm được.

## Sample 1
### Input
```text
5 1
1 0 1 1 0
```
### Output
```text
4
```
### Giải thích
Đổi số 0 tại vị trí thứ 2 thành 1 để thu được dãy $[1, 1, 1, 1]$ dài 4.

## Ràng buộc
- $100\\%$ số test có $N \\le 10^5, K \\le N$.
- Thời gian: $1.0\\text{s}$, Bộ nhớ: $256\\text{MB}$.
""",
        "guide": """# Hướng Dẫn Giảng Dạy: Lật Bit K Số 0
- Cửa sổ trượt đếm số lượng số 0: khi `zero_count > K` thì tăng $L$ đến khi `zero_count <= K`.
""",
        "solution_cpp": """#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    vector<int> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    int l = 0;
    int zero_cnt = 0;
    int max_len = 0;

    for (int r = 0; r < n; ++r) {
        if (a[r] == 0) ++zero_cnt;

        while (zero_cnt > k) {
            if (a[l] == 0) --zero_cnt;
            ++l;
        }

        max_len = max(max_len, r - l + 1);
    }

    cout << max_len << "\\n";
    return 0;
}
""",
        "gen_tests": lambda: [
            {"n": 5, "k": 1, "arr": [1, 0, 1, 1, 0]},
            {"n": 1, "k": 0, "arr": [0]},
            {"n": 1, "k": 1, "arr": [0]},
            {"n": 10, "k": 2, "arr": [random.randint(0, 1) for _ in range(10)]},
            {"n": 100, "k": 10, "arr": [random.randint(0, 1) for _ in range(100)]},
            {"n": 1000, "k": 50, "arr": [random.randint(0, 1) for _ in range(1000)]},
            {"n": 5000, "k": 200, "arr": [random.randint(0, 1) for _ in range(5000)]},
            {"n": 20000, "k": 1000, "arr": [random.randint(0, 1) for _ in range(20000)]},
            {"n": 50000, "k": 5000, "arr": [random.randint(0, 1) for _ in range(50000)]},
            {"n": 100000, "k": 0, "arr": [random.randint(0, 1) for _ in range(100000)]},
            {"n": 100000, "k": 100000, "arr": [0] * 100000},
            {"n": 100000, "k": 100, "arr": [1] * 100000},
            {"n": 100000, "k": 500, "arr": [0] * 100000},
            {"n": 100000, "k": 25000, "arr": [random.randint(0, 1) for _ in range(100000)]},
            {"n": 100000, "k": 50000, "arr": [random.randint(0, 1) for _ in range(100000)]},
            {"n": 100000, "k": 1234, "arr": [random.randint(0, 1) for _ in range(100000)]},
            {"n": 100000, "k": 4321, "arr": [random.randint(0, 1) for _ in range(100000)]},
            {"n": 100000, "k": 9999, "arr": [random.randint(0, 1) for _ in range(100000)]},
            {"n": 100000, "k": 1, "arr": [0, 1] * 50000},
            {"n": 100000, "k": 2, "arr": [0, 1, 1] * 33333 + [0]},
        ],
        "format_inp": lambda t: f"{t['n']} {t['k']}\n" + " ".join(map(str, t['arr'])) + "\n"
    },

    # 6. IKH-0306
    {
        "id": "IKH-0306",
        "slug": "cpp1_03_camera_giao_thong",
        "title": "Giám Sát Camera Giao Thông Thông Minh",
        "statement": """# Giám Sát Camera Giao Thông Thông Minh

## Bối cảnh
Trên tuyến đường cao tốc có $N$ vị trí gắn camera. Trạng thái camera thứ $i$ được ghi nhận bởi $A_i$ ($A_i = 1$ là hoạt động tốt, $A_i = 0$ là bị hỏng). Trung tâm muốn chọn một đoạn liên tiếp gồm $K$ camera để kiểm tra định kỳ. Hãy tìm số lượng camera bị hỏng ít nhất trong bất kỳ đoạn $K$ camera liên tiếp nào.

## Input
- Dòng 1: Chứa 2 số nguyên $N$ và $K$ ($1 \\le K \\le N \\le 10^5$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \\dots, A_N$ ($A_i \\in \\{0, 1\\}$).

## Output
- In ra số camera hỏng ít nhất trong mọi cửa sổ độ dài $K$.

## Sample 1
### Input
```text
7 3
1 0 1 1 0 0 1
```
### Output
```text
0
```
### Giải thích
Đoạn từ vị trí 3 đến 5 là $[1, 1, 1]$ (sau khi xét các cửa sổ độ dài 3, đoạn $[1, 1, 0]$ có 1 hỏng, đoạn $[1, 1, 1]$... trong ví dụ là $[1, 0, 1, 1, 0, 0, 1]$ thì đoạn con $[1, 1, 0]$ có 1 hỏng, đoạn $[1, 0, 1]$ có 1 hỏng...).

## Ràng buộc
- $100\\%$ số test có $N \\le 10^5, K \\le N$.
- Thời gian: $1.0\\text{s}$, Bộ nhớ: $256\\text{MB}$.
""",
        "guide": """# Hướng Dẫn Giảng Dạy: Camera Giao Thông
- Cửa sổ cố định độ dài $K$ đếm số lượng số 0.
""",
        "solution_cpp": """#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    vector<int> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    int cur_broken = 0;
    for (int i = 0; i < k; ++i) {
        if (a[i] == 0) ++cur_broken;
    }

    int min_broken = cur_broken;
    for (int i = k; i < n; ++i) {
        if (a[i] == 0) ++cur_broken;
        if (a[i - k] == 0) --cur_broken;
        min_broken = min(min_broken, cur_broken);
    }

    cout << min_broken << "\\n";
    return 0;
}
""",
        "gen_tests": lambda: [
            {"n": 7, "k": 3, "arr": [1, 0, 1, 1, 0, 0, 1]},
            {"n": 1, "k": 1, "arr": [0]},
            {"n": 1, "k": 1, "arr": [1]},
            {"n": 10, "k": 4, "arr": [random.randint(0, 1) for _ in range(10)]},
            {"n": 100, "k": 15, "arr": [random.randint(0, 1) for _ in range(100)]},
            {"n": 1000, "k": 50, "arr": [random.randint(0, 1) for _ in range(1000)]},
            {"n": 5000, "k": 200, "arr": [random.randint(0, 1) for _ in range(5000)]},
            {"n": 20000, "k": 1000, "arr": [random.randint(0, 1) for _ in range(20000)]},
            {"n": 50000, "k": 5000, "arr": [random.randint(0, 1) for _ in range(50000)]},
            {"n": 100000, "k": 1, "arr": [random.randint(0, 1) for _ in range(100000)]},
            {"n": 100000, "k": 100000, "arr": [random.randint(0, 1) for _ in range(100000)]},
            {"n": 100000, "k": 100, "arr": [1] * 100000},
            {"n": 100000, "k": 100, "arr": [0] * 100000},
            {"n": 100000, "k": 25000, "arr": [random.randint(0, 1) for _ in range(100000)]},
            {"n": 100000, "k": 50000, "arr": [random.randint(0, 1) for _ in range(100000)]},
            {"n": 100000, "k": 1234, "arr": [random.randint(0, 1) for _ in range(100000)]},
            {"n": 100000, "k": 4321, "arr": [random.randint(0, 1) for _ in range(100000)]},
            {"n": 100000, "k": 9999, "arr": [random.randint(0, 1) for _ in range(100000)]},
            {"n": 100000, "k": 33333, "arr": [random.randint(0, 1) for _ in range(100000)]},
            {"n": 100000, "k": 77777, "arr": [random.randint(0, 1) for _ in range(100000)]},
        ],
        "format_inp": lambda t: f"{t['n']} {t['k']}\n" + " ".join(map(str, t['arr'])) + "\n"
    },

    # 7. IKH-0307 (HW P1: Min trong cửa sổ K với K nhỏ hoặc brute-force kiểm tra cửa sổ)
    {
        "id": "IKH-0307",
        "slug": "cpp1_03_min_max_cua_so_k",
        "title": "Tìm Min Trong Mọi Cửa Sổ Độ Dài K",
        "statement": """# Tìm Min Trong Mọi Cửa Sổ Độ Dài K

## Bối cảnh
Cho mảng gồm $N$ số nguyên và số nguyên $K$. Với mỗi cửa sổ gồm $K$ phần tử liên tiếp từ trái sang phải, hãy tìm giá trị nhỏ nhất trong cửa sổ đó.

## Input
- Dòng 1: Chứa 2 số nguyên $N$ và $K$ ($1 \\le K \\le N \\le 10^4$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \\dots, A_N$ ($-10^9 \\le A_i \\le 10^9$).

## Output
- In ra $N - K + 1$ số nguyên cách nhau bởi khoảng trắng là giá trị nhỏ nhất của các cửa sổ.

## Sample 1
### Input
```text
6 3
4 2 12 3 5 1
```
### Output
```text
2 2 3 1
```

## Ràng buộc
- $100\\%$ số test có $N \\le 10^4, K \\le N$.
- Thời gian: $1.0\\text{s}$, Bộ nhớ: $256\\text{MB}$.
""",
        "guide": """# Hướng Dẫn Giảng Dạy: Min Trong Cửa Sổ K
- Duyệt qua từng vị trí bắt đầu $i$, tìm min trong $[i \dots i + K - 1]$.
""",
        "solution_cpp": """#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    for (int i = 0; i <= n - k; ++i) {
        long long cur_min = a[i];
        for (int j = i + 1; j < i + k; ++j) {
            cur_min = min(cur_min, a[j]);
        }
        cout << cur_min << (i == n - k ? "" : " ");
    }
    cout << "\\n";
    return 0;
}
""",
        "gen_tests": lambda: [
            {"n": 6, "k": 3, "arr": [4, 2, 12, 3, 5, 1]},
            {"n": 1, "k": 1, "arr": [100]},
            {"n": 5, "k": 5, "arr": [5, 4, 3, 2, 1]},
            {"n": 10, "k": 3, "arr": [random.randint(-10, 10) for _ in range(10)]},
            {"n": 50, "k": 10, "arr": [random.randint(-100, 100) for _ in range(50)]},
            {"n": 100, "k": 20, "arr": [random.randint(-1000, 1000) for _ in range(100)]},
            {"n": 500, "k": 50, "arr": [random.randint(-10**6, 10**6) for _ in range(500)]},
            {"n": 1000, "k": 100, "arr": [random.randint(-10**9, 10**9) for _ in range(1000)]},
            {"n": 2000, "k": 200, "arr": [random.randint(-10**9, 10**9) for _ in range(2000)]},
            {"n": 5000, "k": 500, "arr": [random.randint(-10**9, 10**9) for _ in range(5000)]},
            {"n": 10000, "k": 1, "arr": [random.randint(-10**9, 10**9) for _ in range(10000)]},
            {"n": 10000, "k": 10000, "arr": [random.randint(-10**9, 10**9) for _ in range(10000)]},
            {"n": 10000, "k": 50, "arr": [random.randint(-10**9, 10**9) for _ in range(10000)]},
            {"n": 10000, "k": 100, "arr": [random.randint(-10**9, 10**9) for _ in range(10000)]},
            {"n": 10000, "k": 200, "arr": [random.randint(-10**9, 10**9) for _ in range(10000)]},
            {"n": 10000, "k": 500, "arr": [random.randint(-10**9, 10**9) for _ in range(10000)]},
            {"n": 10000, "k": 1000, "arr": [random.randint(-10**9, 10**9) for _ in range(10000)]},
            {"n": 10000, "k": 100, "arr": [5] * 10000},
            {"n": 10000, "k": 250, "arr": [random.randint(-10**9, 10**9) for _ in range(10000)]},
            {"n": 10000, "k": 500, "arr": [random.randint(-10**9, 10**9) for _ in range(10000)]},
        ],
        "format_inp": lambda t: f"{t['n']} {t['k']}\n" + " ".join(map(str, t['arr'])) + "\n"
    },

    # 8. IKH-0308 (HW P2: Đếm số lượng đoạn con có tổng <= S)
    {
        "id": "IKH-0308",
        "slug": "cpp1_03_dem_doan_con_tong_be_hon_s",
        "title": "Đếm Số Lượng Đoạn Con Có Tổng Không Quá S",
        "statement": """# Đếm Số Lượng Đoạn Con Có Tổng Không Quá S

## Bối cảnh
Cho mảng gồm $N$ số nguyên **không âm** $A_1, A_2, \\dots, A_N$ và số nguyên $S$. Hãy đếm số lượng đoạn con liên tiếp $[L, R]$ ($1 \\le L \\le R \\le N$) có tổng các phần tử $\\le S$.

## Input
- Dòng 1: Chứa 2 số nguyên $N$ và $S$ ($1 \\le N \\le 2 \\cdot 10^5, 0 \\le S \\le 10^{14}$).
- Dòng 2: $N$ số nguyên không âm $A_1, A_2, \\dots, A_N$ ($0 \\le A_i \\le 10^9$).

## Output
- In ra một số nguyên duy nhất là số lượng đoạn con thỏa mãn.

## Sample 1
### Input
```text
4 5
1 3 2 1
```
### Output
```text
8
```
### Giải thích
Các đoạn con có tổng $\\le 5$: $[1], [3], [2], [1], [1, 3], [3, 2], [2, 1], [1, 3, 2]$... Tổng cộng có 8 đoạn.

## Ràng buộc
- $100\\%$ số test có $N \\le 2 \\cdot 10^5$.
- Thời gian: $1.0\\text{s}$, Bộ nhớ: $256\\text{MB}$.
""",
        "guide": """# Hướng Dẫn Giảng Dạy: Đếm Đoạn Con Tổng <= S
- Khi `cur_sum <= S` kết thúc tại $R$, có đúng $R - L + 1$ đoạn con hợp lệ kết thúc tại $R$.
- Cộng $(R - L + 1)$ vào kết quả.
""",
        "solution_cpp": """#include <bits/stdc++.h>
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
    long long count = 0;

    for (int r = 0; r < n; ++r) {
        cur_sum += a[r];
        while (cur_sum > s) {
            cur_sum -= a[l];
            ++l;
        }
        count += (r - l + 1);
    }

    cout << count << "\\n";
    return 0;
}
""",
        "gen_tests": lambda: [
            {"n": 4, "s": 5, "arr": [1, 3, 2, 1]},
            {"n": 1, "s": 5, "arr": [10]},
            {"n": 1, "s": 10, "arr": [5]},
            {"n": 5, "s": 10, "arr": [1, 2, 3, 4, 5]},
            {"n": 10, "s": 15, "arr": [random.randint(0, 5) for _ in range(10)]},
            {"n": 100, "s": 50, "arr": [random.randint(0, 10) for _ in range(100)]},
            {"n": 1000, "s": 500, "arr": [random.randint(0, 10) for _ in range(1000)]},
            {"n": 5000, "s": 10**5, "arr": [random.randint(0, 100) for _ in range(5000)]},
            {"n": 20000, "s": 10**6, "arr": [random.randint(0, 1000) for _ in range(20000)]},
            {"n": 50000, "s": 10**8, "arr": [random.randint(0, 10**5) for _ in range(50000)]},
            {"n": 100000, "s": 50000, "arr": [1] * 100000},
            {"n": 200000, "s": 0, "arr": [random.randint(1, 10) for _ in range(200000)]},
            {"n": 200000, "s": 10**14, "arr": [random.randint(0, 10**9) for _ in range(200000)]},
            {"n": 200000, "s": 10**9, "arr": [random.randint(0, 10**9) for _ in range(200000)]},
            {"n": 200000, "s": 5 * 10**13, "arr": [random.randint(0, 10**9) for _ in range(200000)]},
            {"n": 200000, "s": 123456789, "arr": [random.randint(0, 10**9) for _ in range(200000)]},
            {"n": 200000, "s": 999999999, "arr": [random.randint(0, 10**9) for _ in range(200000)]},
            {"n": 200000, "s": 777777777, "arr": [random.randint(0, 10**9) for _ in range(200000)]},
            {"n": 200000, "s": 888888888, "arr": [random.randint(0, 10**9) for _ in range(200000)]},
            {"n": 200000, "s": 1000, "arr": [1] * 200000},
        ],
        "format_inp": lambda t: f"{t['n']} {t['s']}\n" + " ".join(map(str, t['arr'])) + "\n"
    },

    # 9. IKH-0309 (HW P2: Đếm số đoạn có tổng đúng bằng S trên mảng dương)
    {
        "id": "IKH-0309",
        "slug": "cpp1_03_dem_doan_con_tong_bang_s",
        "title": "Đếm Số Lượng Đoạn Con Có Tổng Đúng Bằng S",
        "statement": """# Đếm Số Lượng Đoạn Con Có Tổng Đúng Bằng S

## Bối cảnh
Cho mảng gồm $N$ số nguyên **dương** $A_1, A_2, \\dots, A_N$ ($A_i > 0$) và số nguyên dương $S$. Hãy đếm số lượng đoạn con liên tiếp có tổng đúng bằng $S$.

## Input
- Dòng 1: Chứa 2 số nguyên $N$ và $S$ ($1 \\le N \\le 2 \\cdot 10^5, 1 \\le S \\le 10^{14}$).
- Dòng 2: $N$ số nguyên dương $A_1, A_2, \\dots, A_N$ ($1 \\le A_i \\le 10^9$).

## Output
- In ra một số nguyên duy nhất là số lượng đoạn con có tổng bằng $S$.

## Sample 1
### Input
```text
5 7
2 4 1 2 7
```
### Output
```text
2
```
### Giải thích
Các đoạn con có tổng bằng 7 là: $[2, 4, 1]$ và $[7]$.

## Ràng buộc
- $100\\%$ số test có $N \\le 2 \\cdot 10^5, A_i > 0$.
- Thời gian: $1.0\\text{s}$, Bộ nhớ: $256\\text{MB}$.
""",
        "guide": """# Hướng Dẫn Giảng Dạy: Đếm Đoạn Con Tổng Bằng S (Mảng Dương)
- Vì $A_i > 0$, tổng tăng ngặt khi mở rộng $R$ và giảm ngặt khi tăng $L$.
- Duyệt Sliding Window: Khi `cur_sum == S` tăng `count`.
""",
        "solution_cpp": """#include <bits/stdc++.h>
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
    long long count = 0;

    for (int r = 0; r < n; ++r) {
        cur_sum += a[r];
        while (cur_sum > s) {
            cur_sum -= a[l];
            ++l;
        }
        if (cur_sum == s) {
            ++count;
        }
    }

    cout << count << "\\n";
    return 0;
}
""",
        "gen_tests": lambda: [
            {"n": 5, "s": 7, "arr": [2, 4, 1, 2, 7]},
            {"n": 1, "s": 10, "arr": [10]},
            {"n": 1, "s": 10, "arr": [5]},
            {"n": 5, "s": 3, "arr": [1, 2, 3, 4, 5]},
            {"n": 10, "s": 10, "arr": [random.randint(1, 5) for _ in range(10)]},
            {"n": 100, "s": 20, "arr": [random.randint(1, 10) for _ in range(100)]},
            {"n": 1000, "s": 100, "arr": [random.randint(1, 20) for _ in range(1000)]},
            {"n": 5000, "s": 1000, "arr": [random.randint(1, 50) for _ in range(5000)]},
            {"n": 20000, "s": 10000, "arr": [random.randint(1, 100) for _ in range(20000)]},
            {"n": 50000, "s": 10**6, "arr": [random.randint(1, 1000) for _ in range(50000)]},
            {"n": 100000, "s": 5, "arr": [1] * 100000},
            {"n": 200000, "s": 10**14, "arr": [random.randint(1, 10**9) for _ in range(200000)]},
            {"n": 200000, "s": 10**9, "arr": [random.randint(1, 10**9) for _ in range(200000)]},
            {"n": 200000, "s": 5 * 10**13, "arr": [random.randint(1, 10**9) for _ in range(200000)]},
            {"n": 200000, "s": 123456789, "arr": [random.randint(1, 10**9) for _ in range(200000)]},
            {"n": 200000, "s": 999999999, "arr": [random.randint(1, 10**9) for _ in range(200000)]},
            {"n": 200000, "s": 777777777, "arr": [random.randint(1, 10**9) for _ in range(200000)]},
            {"n": 200000, "s": 888888888, "arr": [random.randint(1, 10**9) for _ in range(200000)]},
            {"n": 200000, "s": 1000000, "arr": [1] * 200000},
            {"n": 200000, "s": 1, "arr": [1] * 200000},
        ],
        "format_inp": lambda t: f"{t['n']} {t['s']}\n" + " ".join(map(str, t['arr'])) + "\n"
    },

    # 10. IKH-0310 (HW P3: Đoạn con dài nhất chứa tối đa K ký tự khác nhau)
    {
        "id": "IKH-0310",
        "slug": "cpp1_03_doan_con_k_ky_tu_khac_nhau",
        "title": "Đoạn Con Dài Nhất Chứa Tối Đa K Ký Tự Khác Nhau",
        "statement": """# Đoạn Con Dài Nhất Chứa Tối Đa K Ký Tự Khác Nhau

## Bối cảnh
Cho chuỗi ký tự $S$ gồm các chữ cái tiếng Anh in thường và số nguyên dương $K$. Hãy tìm độ dài của chuỗi con liên tiếp dài nhất chứa **không quá $K$ ký tự phân biệt**.

## Input
- Dòng 1: Chứa 2 số nguyên $N$ và $K$ ($1 \\le K \\le 26, 1 \\le N \\le 10^5$).
- Dòng 2: Chuỗi ký tự $S$ có độ dài $N$.

## Output
- In ra một số nguyên duy nhất là độ dài lớn nhất tìm được.

## Sample 1
### Input
```text
7 2
ecebaaa
```
### Output
```text
4
```
### Giải thích
Chuỗi con `baaa` có độ dài 4 và chứa đúng 2 ký tự phân biệt là `b` và `a`.

## Ràng buộc
- $100\\%$ số test có $N \\le 10^5, K \\le 26$.
- Thời gian: $1.0\\text{s}$, Bộ nhớ: $256\\text{MB}$.
""",
        "guide": """# Hướng Dẫn Giảng Dạy: K Ký Tự Khác Nhau
- Sử dụng mảng đếm tần suất 26 ký tự: `int freq[26] = {0}`.
- Biến `distinct_count` lưu số ký tự có tần suất $> 0$.
- Sliding Window co giãn trong $\\mathcal{O}(N)$.
""",
        "solution_cpp": """#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    string s;
    cin >> s;

    vector<int> freq(26, 0);
    int distinct = 0;
    int l = 0, max_len = 0;

    for (int r = 0; r < n; ++r) {
        int c = s[r] - 'a';
        if (freq[c] == 0) ++distinct;
        ++freq[c];

        while (distinct > k) {
            int lc = s[l] - 'a';
            --freq[lc];
            if (freq[lc] == 0) --distinct;
            ++l;
        }

        max_len = max(max_len, r - l + 1);
    }

    cout << max_len << "\\n";
    return 0;
}
""",
        "gen_tests": lambda: [
            {"n": 7, "k": 2, "s": "ecebaaa"},
            {"n": 1, "k": 1, "s": "a"},
            {"n": 5, "k": 1, "s": "aaaaa"},
            {"n": 10, "k": 3, "s": "".join(random.choice("abcde") for _ in range(10))},
            {"n": 100, "k": 4, "s": "".join(random.choice("abcdefgh") for _ in range(100))},
            {"n": 1000, "k": 5, "s": "".join(random.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(1000))},
            {"n": 5000, "k": 10, "s": "".join(random.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(5000))},
            {"n": 20000, "k": 2, "s": "".join(random.choice("ab") for _ in range(20000))},
            {"n": 50000, "k": 15, "s": "".join(random.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(50000))},
            {"n": 100000, "k": 26, "s": "".join(random.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(100000))},
            {"n": 100000, "k": 1, "s": "z" * 100000},
            {"n": 100000, "k": 2, "s": "ab" * 50000},
            {"n": 100000, "k": 3, "s": "abc" * 33333 + "a"},
            {"n": 100000, "k": 5, "s": "".join(random.choice("abcde") for _ in range(100000))},
            {"n": 100000, "k": 8, "s": "".join(random.choice("abcdefgh") for _ in range(100000))},
            {"n": 100000, "k": 12, "s": "".join(random.choice("abcdefghijkl") for _ in range(100000))},
            {"n": 100000, "k": 20, "s": "".join(random.choice("abcdefghijklmnopqrst") for _ in range(100000))},
            {"n": 100000, "k": 26, "s": "".join(random.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(100000))},
            {"n": 100000, "k": 4, "s": "".join(random.choice("abcd") for _ in range(100000))},
            {"n": 100000, "k": 2, "s": "".join(random.choice("xy") for _ in range(100000))},
        ],
        "format_inp": lambda t: f"{t['n']} {t['k']}\n{t['s']}\n"
    },

    # 11. IKH-0311 (HW P3: Đoạn con ngắn nhất chứa đủ mọi ký tự của tập hợp)
    {
        "id": "IKH-0311",
        "slug": "cpp1_03_doan_con_ngan_nhat_chua_du_ky_tu",
        "title": "Đoạn Con Ngắn Nhất Chứa Đủ Mọi Ký Tự Của Tập Hợp",
        "statement": """# Đoạn Con Ngắn Nhất Chứa Đủ Mọi Ký Tự Của Tập Hợp

## Bối cảnh
Cho chuỗi $S$ gồm các chữ cái in thường và chuỗi mẫu $T$ gồm $M$ ký tự phân biệt. Hãy tìm độ dài ngắn nhất của một chuỗi con liên tiếp trong $S$ chứa đầy đủ tất cả các ký tự có trong $T$. Nếu không tồn tại, in ra `-1`.

## Input
- Dòng 1: Chứa 2 số nguyên $N$ và $M$ ($1 \\le M \\le 26, 1 \\le N \\le 10^5$).
- Dòng 2: Chuỗi $S$ có độ dài $N$.
- Dòng 3: Chuỗi $T$ có độ dài $M$ gồm các ký tự phân biệt.

## Output
- In ra độ dài ngắn nhất tìm được hoặc `-1`.

## Sample 1
### Input
```text
8 3
adobecod
abc
```
### Output
```text
6
```
### Giải thích
Chuỗi con `adobec` dài 6 chứa đủ `a`, `b`, `c`.

## Ràng buộc
- $100\\%$ số test có $N \\le 10^5, M \\le 26$.
- Thời gian: $1.0\\text{s}$, Bộ nhớ: $256\\text{MB}$.
""",
        "guide": """# Hướng Dẫn Giảng Dạy: Bao Phủ Tập Ký Tự
- Dùng mảng đếm tần suất `need[26]` và `have[26]`.
- Biến `matched` đếm số loại ký tự trong $T$ đã xuất hiện $\\ge 1$ lần trong cửa sổ.
- Khi `matched == M` thì co $L$ để tìm min length.
""",
        "solution_cpp": """#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    string s, t;
    cin >> s >> t;

    vector<int> need(26, 0);
    for (char c : t) need[c - 'a'] = 1;

    vector<int> have(26, 0);
    int matched = 0;
    int l = 0, min_len = n + 1;

    for (int r = 0; r < n; ++r) {
        int c = s[r] - 'a';
        if (need[c]) {
            if (have[c] == 0) ++matched;
            ++have[c];
        }

        while (matched == m) {
            min_len = min(min_len, r - l + 1);
            int lc = s[l] - 'a';
            if (need[lc]) {
                --have[lc];
                if (have[lc] == 0) --matched;
            }
            ++l;
        }
    }

    if (min_len > n) cout << -1 << "\\n";
    else cout << min_len << "\\n";
    return 0;
}
""",
        "gen_tests": lambda: [
            {"n": 8, "m": 3, "s": "adobecod", "t": "abc"},
            {"n": 1, "m": 1, "s": "a", "t": "a"},
            {"n": 1, "m": 1, "s": "a", "t": "b"},
            {"n": 10, "m": 3, "s": "abcdefghij", "t": "bdf"},
            {"n": 100, "m": 4, "s": "".join(random.choice("abcdefgh") for _ in range(100)), "t": "abcd"},
            {"n": 1000, "m": 5, "s": "".join(random.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(1000)), "t": "aeiou"},
            {"n": 5000, "m": 10, "s": "".join(random.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(5000)), "t": "abcdefghij"},
            {"n": 20000, "m": 3, "s": "".join(random.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(20000)), "t": "xyz"},
            {"n": 50000, "m": 5, "s": "".join(random.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(50000)), "t": "abcde"},
            {"n": 100000, "m": 26, "s": "".join(random.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(100000)), "t": "abcdefghijklmnopqrstuvwxyz"},
            {"n": 100000, "m": 1, "s": "z" * 100000, "t": "z"},
            {"n": 100000, "m": 2, "s": "ab" * 50000, "t": "ab"},
            {"n": 100000, "m": 3, "s": "abc" * 33333 + "a", "t": "abc"},
            {"n": 100000, "m": 5, "s": "".join(random.choice("abcde") for _ in range(100000)), "t": "abcde"},
            {"n": 100000, "m": 8, "s": "".join(random.choice("abcdefgh") for _ in range(100000)), "t": "abcdefgh"},
            {"n": 100000, "m": 12, "s": "".join(random.choice("abcdefghijkl") for _ in range(100000)), "t": "abcdefghijkl"},
            {"n": 100000, "m": 20, "s": "".join(random.choice("abcdefghijklmnopqrst") for _ in range(100000)), "t": "abcdefghijklmnopqrst"},
            {"n": 100000, "m": 4, "s": "".join(random.choice("abcd") for _ in range(100000)), "t": "abcd"},
            {"n": 100000, "m": 2, "s": "".join(random.choice("xy") for _ in range(100000)), "t": "xy"},
            {"n": 100000, "m": 3, "s": "a" * 50000 + "b" * 49999 + "c", "t": "abc"},
        ],
        "format_inp": lambda t: f"{t['n']} {t['m']}\n{t['s']}\n{t['t']}\n"
    },

    # 12. IKH-0312 (HW P4: Phủ sóng wifi)
    {
        "id": "IKH-0312",
        "slug": "cpp1_03_phu_song_wifi",
        "title": "Phủ Sóng Trạm Phát Sóng Wifi Đô Thị",
        "statement": """# Phủ Sóng Trạm Phát Sóng Wifi Đô Thị

## Bối cảnh
Dọc theo tuyến phố dài, có $N$ căn nhà tại tọa độ $X_1, X_2, \\dots, X_N$ ($X_1 < X_2 < \\dots < X_N$). Nhà mạng muốn lắp các bộ phát wifi, mỗi bộ có bán kính phủ sóng là $R$ (phủ được đoạn $[x - R, x + R]$, tức độ dài vùng phủ là $2R$). Hãy tìm số lượng bộ phát wifi ít nhất để phủ sóng toàn bộ $N$ căn nhà.

## Input
- Dòng 1: Chứa 2 số nguyên $N$ và $R$ ($1 \\le N \\le 10^5, 0 \\le R \\le 10^9$).
- Dòng 2: $N$ số nguyên tăng dần $X_1, X_2, \\dots, X_N$ ($0 \\le X_i \\le 10^{14}$).

## Output
- In ra số bộ phát wifi ít nhất.

## Sample 1
### Input
```text
6 2
1 2 3 7 8 11
```
### Output
```text
3
```
### Giải thích
- Bộ 1 đặt tại $3$: phủ $[1, 5]$ (nhà 1, 2, 3).
- Bộ 2 đặt tại $9$: phủ $[7, 11]$ (nhà 7, 8, 11 - hoặc đặt tại 8 phủ 7, 8 và đặt bộ khác...).

## Ràng buộc
- $100\\%$ số test có $N \\le 10^5$.
- Thời gian: $1.0\\text{s}$, Bộ nhớ: $256\\text{MB}$.
""",
        "guide": """# Hướng Dẫn Giảng Dạy: Phủ Sóng Wifi
- Tham lam + Hai con trỏ: Từ nhà chưa phủ đầu tiên $X[i]$, tìm nhà $X[j]$ xa nhất sao cho $X[j] - X[i] \\le R$ để đặt trạm wifi.
- Trạm tại $X[j]$ sẽ phủ đến $X[j] + R$. Tiếp tục tìm nhà đầu tiên vượt quá $X[j] + R$.
""",
        "solution_cpp": """#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long r;
    if (!(cin >> n >> r)) return 0;

    vector<long long> x(n);
    for (int i = 0; i < n; ++i) cin >> x[i];

    int i = 0;
    int count = 0;

    while (i < n) {
        ++count;
        long long loc = x[i];
        while (i < n && x[i] - loc <= r) ++i;
        long long tower = x[i - 1];
        while (i < n && x[i] - tower <= r) ++i;
    }

    cout << count << "\\n";
    return 0;
}
""",
        "gen_tests": lambda: [
            {"n": 6, "r": 2, "arr": [1, 2, 3, 7, 8, 11]},
            {"n": 1, "r": 10, "arr": [5]},
            {"n": 5, "r": 0, "arr": [1, 2, 3, 4, 5]},
            {"n": 10, "r": 5, "arr": sorted([random.randint(1, 50) for _ in range(10)])},
            {"n": 100, "r": 20, "arr": sorted([random.randint(1, 1000) for _ in range(100)])},
            {"n": 1000, "r": 100, "arr": sorted([random.randint(1, 10**6) for _ in range(1000)])},
            {"n": 5000, "r": 1000, "arr": sorted([random.randint(1, 10**9) for _ in range(5000)])},
            {"n": 20000, "r": 5000, "arr": sorted([random.randint(1, 10**12) for _ in range(20000)])},
            {"n": 50000, "r": 10000, "arr": sorted([random.randint(1, 10**14) for _ in range(50000)])},
            {"n": 100000, "r": 1, "arr": list(range(1, 100001))},
            {"n": 100000, "r": 100000, "arr": list(range(1, 100001))},
            {"n": 100000, "r": 10**9, "arr": sorted([random.randint(1, 10**14) for _ in range(100000)])},
            {"n": 100000, "r": 0, "arr": list(range(1, 100001))},
            {"n": 100000, "r": 500, "arr": sorted([random.randint(1, 10**14) for _ in range(100000)])},
            {"n": 100000, "r": 123456, "arr": sorted([random.randint(1, 10**14) for _ in range(100000)])},
            {"n": 100000, "r": 999999, "arr": sorted([random.randint(1, 10**14) for _ in range(100000)])},
            {"n": 100000, "r": 777777, "arr": sorted([random.randint(1, 10**14) for _ in range(100000)])},
            {"n": 100000, "r": 888888, "arr": sorted([random.randint(1, 10**14) for _ in range(100000)])},
            {"n": 100000, "r": 10**14, "arr": sorted([random.randint(1, 10**14) for _ in range(100000)])},
            {"n": 100000, "r": 10, "arr": [i * 10 for i in range(1, 100001)]},
        ],
        "format_inp": lambda t: f"{t['n']} {t['r']}\n" + " ".join(map(str, t['arr'])) + "\n"
    },

    # 13. IKH-0313 (HW P4: Đoạn con có độ chênh lệch Max - Min <= K với N <= 5000)
    {
        "id": "IKH-0313",
        "slug": "cpp1_03_doan_con_chenh_lech_k",
        "title": "Đoạn Con Có Độ Chênh Lệch Max - Min Không Quá K",
        "statement": """# Đoạn Con Có Độ Chênh Lệch Max - Min Không Quá K

## Bối cảnh
Cho mảng gồm $N$ số nguyên và số nguyên không âm $K$. Hãy tìm độ dài của đoạn con liên tiếp dài nhất sao cho chênh lệch giữa phần tử lớn nhất và nhỏ nhất trong đoạn đó không vượt quá $K$ (tức $\\max - \\min \\le K$).

## Input
- Dòng 1: Chứa 2 số nguyên $N$ và $K$ ($1 \\le N \\le 5000, 0 \\le K \\le 10^9$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \\dots, A_N$ ($-10^9 \\le A_i \\le 10^9$).

## Output
- In ra độ dài lớn nhất của đoạn con thỏa mãn.

## Sample 1
### Input
```text
6 3
8 2 4 7 3 9
```
### Output
```text
3
```
### Giải thích
Đoạn $[2, 4, 3]$ hoặc $[4, 7, 3]$ có chênh lệch $\\max - \\min \\le 3$ với độ dài 3.

## Ràng buộc
- $100\\%$ số test có $N \\le 5000$.
- Thời gian: $1.0\\text{s}$, Bộ nhớ: $256\\text{MB}$.
""",
        "guide": """# Hướng Dẫn Giảng Dạy: Chênh Lệch Max-Min Trong Đoạn Con
- Với $N \\le 5000$, ta có thể duyệt mở rộng $R$ từ $L$, duy trì `cur_min` và `cur_max` trong $\\mathcal{O}(N^2)$ mà không cần cấu trúc dữ liệu nâng cao.
""",
        "solution_cpp": """#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long k;
    if (!(cin >> n >> k)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    int max_len = 0;

    for (int l = 0; l < n; ++l) {
        long long cur_min = a[l], cur_max = a[l];
        for (int r = l; r < n; ++r) {
            cur_min = min(cur_min, a[r]);
            cur_max = max(cur_max, a[r]);
            if (cur_max - cur_min <= k) {
                max_len = max(max_len, r - l + 1);
            } else {
                break;
            }
        }
    }

    cout << max_len << "\\n";
    return 0;
}
""",
        "gen_tests": lambda: [
            {"n": 6, "k": 3, "arr": [8, 2, 4, 7, 3, 9]},
            {"n": 1, "k": 10, "arr": [5]},
            {"n": 5, "k": 0, "arr": [2, 2, 2, 2, 2]},
            {"n": 10, "k": 5, "arr": [random.randint(1, 20) for _ in range(10)]},
            {"n": 50, "k": 10, "arr": [random.randint(-50, 50) for _ in range(50)]},
            {"n": 100, "k": 20, "arr": [random.randint(-500, 500) for _ in range(100)]},
            {"n": 500, "k": 50, "arr": [random.randint(-10**6, 10**6) for _ in range(500)]},
            {"n": 1000, "k": 1000, "arr": [random.randint(-10**9, 10**9) for _ in range(1000)]},
            {"n": 2000, "k": 5000, "arr": [random.randint(-10**9, 10**9) for _ in range(2000)]},
            {"n": 3000, "k": 10000, "arr": [random.randint(-10**9, 10**9) for _ in range(3000)]},
            {"n": 4000, "k": 50000, "arr": [random.randint(-10**9, 10**9) for _ in range(4000)]},
            {"n": 5000, "k": 0, "arr": [10] * 5000},
            {"n": 5000, "k": 1, "arr": [random.randint(1, 2) for _ in range(5000)]},
            {"n": 5000, "k": 10**9, "arr": [random.randint(-10**9, 10**9) for _ in range(5000)]},
            {"n": 5000, "k": 123456, "arr": [random.randint(-10**9, 10**9) for _ in range(5000)]},
            {"n": 5000, "k": 999999, "arr": [random.randint(-10**9, 10**9) for _ in range(5000)]},
            {"n": 5000, "k": 777777, "arr": [random.randint(-10**9, 10**9) for _ in range(5000)]},
            {"n": 5000, "k": 888888, "arr": [random.randint(-10**9, 10**9) for _ in range(5000)]},
            {"n": 5000, "k": 100, "arr": list(range(1, 5001))},
            {"n": 5000, "k": 5000, "arr": list(range(1, 5001))},
        ],
        "format_inp": lambda t: f"{t['n']} {t['k']}\n" + " ".join(map(str, t['arr'])) + "\n"
    },

    # 14. IKH-0314 (HW P5: Tối ưu cửa sổ trượt quy mô lớn)
    {
        "id": "IKH-0314",
        "slug": "cpp1_03_cua_so_truot_cuc_han",
        "title": "Tối Ưu Cửa Sổ Trượt Tuyến Tính Khi N = 2.10⁵",
        "statement": """# Tối Ưu Cửa Sổ Trượt Tuyến Tính Khi N = 2.10⁵

## Bối cảnh
Cho mảng gồm $N$ số nguyên dương và số nguyên $S$. Hãy tìm số lượng đoạn con liên tiếp có tổng các phần tử **nằm trong đoạn $[A, B]$** (tức $A \\le \\text{tổng} \\le B$).

## Input
- Dòng 1: Chứa 3 số nguyên $N, A, B$ ($1 \\le N \\le 2 \\cdot 10^5, 1 \\le A \\le B \\le 10^{14}$).
- Dòng 2: $N$ số nguyên dương $X_1, X_2, \\dots, X_N$ ($1 \\le X_i \\le 10^9$).

## Output
- In ra một số nguyên duy nhất là số lượng đoạn con thỏa mãn.

## Sample 1
### Input
```text
4 3 6
1 2 3 4
```
### Output
```text
6
```
### Giải thích
Các đoạn con có tổng $\\in [3, 6]$: $[1, 2]$ (3), $[3]$ (3), $[4]$ (4), $[1, 2, 3]$ (6), $[2, 3]$ (5), $[2, 4]$ không liên tiếp (chỉ tính liên tiếp), $[3]$... Tổng cộng 6 đoạn con.

## Ràng buộc
- $100\\%$ số test có $N \\le 2 \\cdot 10^5$.
- Thời gian: $1.0\\text{s}$, Bộ nhớ: $256\\text{MB}$.
""",
        "guide": """# Hướng Dẫn Giảng Dạy: Đếm Đoạn Con Tổng Trong [A, B]
- Số đoạn có tổng $\\in [A, B] = (\\text{Số đoạn tổng} \\le B) - (\\text{Số đoạn tổng} \\le A - 1)$.
- Dùng hàm `count_at_most(limit)` chạy Sliding Window 2 lần trong $\\mathcal{O}(N)$.
""",
        "solution_cpp": """#include <bits/stdc++.h>
using namespace std;

long long count_at_most(const vector<long long> &x, long long limit) {
    if (limit <= 0) return 0;
    int n = x.size();
    int l = 0;
    long long cur_sum = 0;
    long long count = 0;

    for (int r = 0; r < n; ++r) {
        cur_sum += x[r];
        while (cur_sum > limit) {
            cur_sum -= x[l];
            ++l;
        }
        count += (r - l + 1);
    }
    return count;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long a, b;
    if (!(cin >> n >> a >> b)) return 0;

    vector<long long> x(n);
    for (int i = 0; i < n; ++i) cin >> x[i];

    long long ans = count_at_most(x, b) - count_at_most(x, a - 1);
    cout << ans << "\\n";
    return 0;
}
""",
        "gen_tests": lambda: [
            {"n": 4, "a": 3, "b": 6, "arr": [1, 2, 3, 4]},
            {"n": 1, "a": 5, "b": 10, "arr": [7]},
            {"n": 1, "a": 5, "b": 10, "arr": [2]},
            {"n": 5, "a": 5, "b": 15, "arr": [1, 2, 3, 4, 5]},
            {"n": 10, "a": 10, "b": 20, "arr": [random.randint(1, 10) for _ in range(10)]},
            {"n": 100, "a": 50, "b": 150, "arr": [random.randint(1, 20) for _ in range(100)]},
            {"n": 1000, "a": 500, "b": 1500, "arr": [random.randint(1, 50) for _ in range(1000)]},
            {"n": 5000, "a": 10**4, "b": 5 * 10**4, "arr": [random.randint(1, 100) for _ in range(5000)]},
            {"n": 20000, "a": 10**6, "b": 5 * 10**6, "arr": [random.randint(1, 1000) for _ in range(20000)]},
            {"n": 50000, "a": 10**8, "b": 5 * 10**8, "arr": [random.randint(1, 10**5) for _ in range(50000)]},
            {"n": 100000, "a": 1000, "b": 5000, "arr": [1] * 100000},
            {"n": 200000, "a": 1, "b": 10**14, "arr": [random.randint(1, 10**9) for _ in range(200000)]},
            {"n": 200000, "a": 10**9, "b": 2 * 10**9, "arr": [random.randint(1, 10**9) for _ in range(200000)]},
            {"n": 200000, "a": 10**13, "b": 5 * 10**13, "arr": [random.randint(1, 10**9) for _ in range(200000)]},
            {"n": 200000, "a": 123456789, "b": 987654321, "arr": [random.randint(1, 10**9) for _ in range(200000)]},
            {"n": 200000, "a": 500000, "b": 1000000, "arr": [random.randint(1, 10**9) for _ in range(200000)]},
            {"n": 200000, "a": 7777777, "b": 8888888, "arr": [random.randint(1, 10**9) for _ in range(200000)]},
            {"n": 200000, "a": 100, "b": 200, "arr": [1] * 200000},
            {"n": 200000, "a": 1, "b": 2, "arr": [1] * 200000},
            {"n": 200000, "a": 10**14, "b": 10**14, "arr": [random.randint(1, 10**9) for _ in range(200000)]},
        ],
        "format_inp": lambda t: f"{t['n']} {t['a']} {t['b']}\n" + " ".join(map(str, t['arr'])) + "\n"
    }
]

if __name__ == "__main__":
    print(f"Building {len(LESSON03_PROBLEMS)} problems for Lesson 03...")
    for p in LESSON03_PROBLEMS:
        build_problem(p)
    print("🎉 Done Lesson 03!")
