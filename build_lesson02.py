import random
from generate_module01_all_problems import build_problem

LESSON02_PROBLEMS = [
    # 1. IKH-0201
    {
        "id": "IKH-0201",
        "slug": "cpp1_02_mo_phong_hai_con_tro",
        "title": "Mô Phỏng Hai Con Trỏ Đối Đầu",
        "statement": """# Mô Phỏng Hai Con Trỏ Đối Đầu

## Bối cảnh
Cho mảng $N$ số nguyên đã sắp xếp tăng dần và một số nguyên $S$. Hãy kiểm tra xem trong mảng có tồn tại cặp chỉ số $(i, j)$ với $i < j$ sao cho $A_i + A_j = S$ hay không. Nếu có, in ra `YES`, ngược lại in ra `NO`.

## Input
- Dòng 1: Chứa 2 số nguyên $N$ và $S$ ($2 \\le N \\le 10^5, -10^{18} \\le S \\le 10^{18}$).
- Dòng 2: Chứa $N$ số nguyên đã sắp xếp tăng dần $A_1 \\le A_2 \\le \\dots \\le A_N$ ($-10^9 \\le A_i \\le 10^9$).

## Output
- In ra `YES` nếu tồn tại cặp số có tổng bằng $S$, ngược lại in ra `NO`.

## Sample 1
### Input
```text
5 20
2 5 8 12 19
```
### Output
```text
YES
```

## Ràng buộc
- $40\\%$ số test có $N \\le 1000$.
- $60\\%$ số test có $N \\le 10^5$.
- Thời gian: $1.0\\text{s}$, Bộ nhớ: $256\\text{MB}$.
""",
        "guide": """# Hướng Dẫn Giảng Dạy: Mô Phỏng Hai Con Trỏ Đối Đầu
- Đặt $L = 0, R = N - 1$. Độ phức tạp: $\\mathcal{O}(N)$.
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

    int l = 0, r = n - 1;
    bool found = false;

    while (l < r) {
        long long sum = a[l] + a[r];
        if (sum == s) {
            found = true;
            break;
        } else if (sum < s) {
            ++l;
        } else {
            --r;
        }
    }

    if (found) cout << "YES\\n";
    else cout << "NO\\n";
    return 0;
}
""",
        "gen_tests": lambda: [
            {"n": 5, "s": 20, "arr": [2, 5, 8, 12, 19]},
            {"n": 5, "s": 100, "arr": [2, 5, 8, 12, 19]},
            {"n": 2, "s": 10, "arr": [3, 7]},
            {"n": 10, "s": 50, "arr": sorted([random.randint(1, 40) for _ in range(10)])},
            {"n": 100, "s": 500, "arr": sorted([random.randint(-200, 400) for _ in range(100)])},
            {"n": 1000, "s": 10**6, "arr": sorted([random.randint(1, 10**6) for _ in range(1000)])},
            {"n": 5000, "s": 123456, "arr": sorted([random.randint(1, 10**9) for _ in range(5000)])},
            {"n": 20000, "s": 10**9, "arr": sorted([random.randint(-10**9, 10**9) for _ in range(20000)])},
            {"n": 50000, "s": 999999, "arr": sorted([random.randint(-10**9, 10**9) for _ in range(50000)])},
            {"n": 100000, "s": 200000, "arr": list(range(1, 100001))},
            {"n": 100000, "s": 10**9, "arr": sorted([random.randint(-10**9, 10**9) for _ in range(100000)])},
            {"n": 100000, "s": 0, "arr": sorted([random.randint(-10**9, 10**9) for _ in range(100000)])},
            {"n": 100000, "s": 10**18, "arr": sorted([random.randint(1, 10**9) for _ in range(100000)])},
            {"n": 100000, "s": 14, "arr": [7] * 100000},
            {"n": 100000, "s": 15, "arr": [7] * 100000},
            {"n": 100000, "s": 12345678, "arr": sorted([random.randint(-10**9, 10**9) for _ in range(100000)])},
            {"n": 100000, "s": -500, "arr": sorted([random.randint(-10**9, 10**9) for _ in range(100000)])},
            {"n": 100000, "s": 88888888, "arr": sorted([random.randint(-10**9, 10**9) for _ in range(100000)])},
            {"n": 100000, "s": 12345, "arr": sorted([random.randint(-10**9, 10**9) for _ in range(100000)])},
            {"n": 100000, "s": -99999, "arr": sorted([random.randint(-10**9, 10**9) for _ in range(100000)])},
        ],
        "format_inp": lambda t: f"{t['n']} {t['s']}\n" + " ".join(map(str, t['arr'])) + "\n"
    },

    # 2. IKH-0202
    {
        "id": "IKH-0202",
        "slug": "cpp1_02_tong_hai_so",
        "title": "Cặp Số Có Tổng Bằng S (Two Sum)",
        "statement": """# Cặp Số Có Tổng Bằng S (Two Sum)

## Bối cảnh
Cho một mảng gồm $N$ số nguyên và một số nguyên $S$. Hãy tìm hai phần tử ở hai vị trí khác nhau trong mảng có tổng đúng bằng $S$. Nếu có nhiều cặp thỏa mãn, in ra một cặp bất kỳ theo thứ tự tăng dần. Nếu không tồn tại, in ra `-1`.

## Input
- Dòng 1: Chứa 2 số nguyên $N$ và $S$ ($2 \\le N \\le 10^5, -10^{18} \\le S \\le 10^{18}$).
- Dòng 2: Chứa $N$ số nguyên $A_1, A_2, \\dots, A_N$ ($-10^9 \\le A_i \\le 10^9$).

## Output
- In ra 2 số nguyên là giá trị của 2 phần tử tìm được theo thứ tự tăng dần, hoặc `-1` nếu không có nghiệm.

## Sample 1
### Input
```text
5 20
19 2 8 12 5
```
### Output
```text
8 12
```

## Ràng buộc
- $40\\%$ số test có $N \\le 1000$.
- $60\\%$ số test có $N \\le 10^5$.
- Thời gian: $1.0\\text{s}$, Bộ nhớ: $256\\text{MB}$.
""",
        "guide": """# Hướng Dẫn Giảng Dạy: Two Sum
- Sắp xếp tăng dần $\\mathcal{O}(N \\log N)$, sau đó duyệt bằng Hai con trỏ $\\mathcal{O}(N)$.
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

    sort(a.begin(), a.end());

    int l = 0, r = n - 1;
    bool found = false;

    while (l < r) {
        long long sum = a[l] + a[r];
        if (sum == s) {
            cout << a[l] << " " << a[r] << "\\n";
            found = true;
            break;
        } else if (sum < s) {
            ++l;
        } else {
            --r;
        }
    }

    if (!found) cout << -1 << "\\n";
    return 0;
}
""",
        "gen_tests": lambda: [
            {"n": 5, "s": 20, "arr": [19, 2, 8, 12, 5]},
            {"n": 5, "s": 100, "arr": [19, 2, 8, 12, 5]},
            {"n": 2, "s": 15, "arr": [10, 5]},
            {"n": 10, "s": 30, "arr": [random.randint(1, 30) for _ in range(10)]},
            {"n": 100, "s": 50, "arr": [random.randint(-100, 100) for _ in range(100)]},
            {"n": 500, "s": 1000, "arr": [random.randint(-500, 1500) for _ in range(500)]},
            {"n": 1000, "s": 10**6, "arr": [random.randint(1, 10**6) for _ in range(1000)]},
            {"n": 5000, "s": 0, "arr": [random.randint(-10**5, 10**5) for _ in range(5000)]},
            {"n": 20000, "s": 500000, "arr": [random.randint(-10**9, 10**9) for _ in range(20000)]},
            {"n": 50000, "s": 10**9, "arr": [random.randint(-10**9, 10**9) for _ in range(50000)]},
            {"n": 100000, "s": 199999, "arr": list(range(100000, 0, -1))},
            {"n": 100000, "s": 10**9, "arr": [random.randint(-10**9, 10**9) for _ in range(100000)]},
            {"n": 100000, "s": 0, "arr": [random.randint(-10**9, 10**9) for _ in range(100000)]},
            {"n": 100000, "s": 20, "arr": [10] * 100000},
            {"n": 100000, "s": 25, "arr": [10] * 100000},
            {"n": 100000, "s": 123456, "arr": [random.randint(-10**9, 10**9) for _ in range(100000)]},
            {"n": 100000, "s": -987654, "arr": [random.randint(-10**9, 10**9) for _ in range(100000)]},
            {"n": 100000, "s": 7777777, "arr": [random.randint(-10**9, 10**9) for _ in range(100000)]},
            {"n": 100000, "s": 10**18, "arr": [random.randint(-10**9, 10**9) for _ in range(100000)]},
            {"n": 100000, "s": -10**18, "arr": [random.randint(-10**9, 10**9) for _ in range(100000)]},
        ],
        "format_inp": lambda t: f"{t['n']} {t['s']}\n" + " ".join(map(str, t['arr'])) + "\n"
    },

    # 3. IKH-0203
    {
        "id": "IKH-0203",
        "slug": "cpp1_02_dem_cap_tong_be_hon_s",
        "title": "Đếm Cặp Có Tổng Không Quá S",
        "statement": """# Đếm Cặp Có Tổng Không Quá S

## Bối cảnh
Cho mảng gồm $N$ số nguyên và một số nguyên $S$. Hãy đếm số lượng cặp chỉ số $(i, j)$ với $1 \\le i < j \\le N$ thỏa mãn:
$$A_i + A_j \\le S$$

## Input
- Dòng 1: Chứa 2 số nguyên $N$ và $S$ ($2 \\le N \\le 2 \\cdot 10^5, -10^{18} \\le S \\le 10^{18}$).
- Dòng 2: Chứa $N$ số nguyên $A_1, A_2, \\dots, A_N$ ($-10^9 \\le A_i \\le 10^9$).

## Output
- In ra một số nguyên duy nhất là số lượng cặp thỏa mãn.

## Sample 1
### Input
```text
5 8
2 5 1 4 3
```
### Output
```text
8
```

## Ràng buộc
- $100\\%$ số test có $N \\le 2 \\cdot 10^5$.
- Thời gian: $1.0\\text{s}$, Bộ nhớ: $256\\text{MB}$.
""",
        "guide": """# Hướng Dẫn Giảng Dạy: Đếm Cặp Tổng <= S
- Khi $A[L] + A[R] \\le S \\implies$ cộng $R - L$ vào kết quả, $++L$. Ngược lại $--R$.
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

    sort(a.begin(), a.end());

    int l = 0, r = n - 1;
    long long count = 0;

    while (l < r) {
        if (a[l] + a[r] <= s) {
            count += (r - l);
            ++l;
        } else {
            --r;
        }
    }

    cout << count << "\\n";
    return 0;
}
""",
        "gen_tests": lambda: [
            {"n": 5, "s": 8, "arr": [2, 5, 1, 4, 3]},
            {"n": 2, "s": 5, "arr": [2, 3]},
            {"n": 10, "s": 20, "arr": [random.randint(1, 20) for _ in range(10)]},
            {"n": 100, "s": 50, "arr": [random.randint(-50, 50) for _ in range(100)]},
            {"n": 500, "s": 1000, "arr": [random.randint(1, 1000) for _ in range(500)]},
            {"n": 1000, "s": 0, "arr": [random.randint(-1000, 1000) for _ in range(1000)]},
            {"n": 5000, "s": 10**6, "arr": [random.randint(1, 10**6) for _ in range(500)]},
            {"n": 20000, "s": 10**9, "arr": [random.randint(-10**9, 10**9) for _ in range(20000)]},
            {"n": 50000, "s": 500000, "arr": [random.randint(-10**9, 10**9) for _ in range(50000)]},
            {"n": 100000, "s": 100000, "arr": list(range(1, 100001))},
            {"n": 100000, "s": 2 * 10**9, "arr": [random.randint(1, 10**9) for _ in range(100000)]},
            {"n": 200000, "s": 10**9, "arr": [random.randint(-10**9, 10**9) for _ in range(200000)]},
            {"n": 200000, "s": 0, "arr": [random.randint(-10**9, 10**9) for _ in range(200000)]},
            {"n": 200000, "s": 20, "arr": [10] * 200000},
            {"n": 200000, "s": 19, "arr": [10] * 200000},
            {"n": 200000, "s": 123456789, "arr": [random.randint(-10**9, 10**9) for _ in range(200000)]},
            {"n": 200000, "s": -500000, "arr": [random.randint(-10**9, 10**9) for _ in range(200000)]},
            {"n": 200000, "s": 10**18, "arr": [random.randint(-10**9, 10**9) for _ in range(200000)]},
            {"n": 200000, "s": -10**18, "arr": [random.randint(-10**9, 10**9) for _ in range(200000)]},
            {"n": 200000, "s": 999999999, "arr": [random.randint(-10**9, 10**9) for _ in range(200000)]},
        ],
        "format_inp": lambda t: f"{t['n']} {t['s']}\n" + " ".join(map(str, t['arr'])) + "\n"
    },

    # 4. IKH-0204 (Đếm số cặp có tổng >= S)
    {
        "id": "IKH-0204",
        "slug": "cpp1_02_dem_cap_tong_lon_hon_s",
        "title": "Đếm Cặp Có Tổng Lớn Hơn Hoặc Bằng S",
        "statement": """# Đếm Cặp Có Tổng Lớn Hơn Hoặc Bằng S

## Bối cảnh
Cho mảng gồm $N$ số nguyên và một số nguyên $S$. Hãy đếm số lượng cặp chỉ số $(i, j)$ với $1 \\le i < j \\le N$ thỏa mãn:
$$A_i + A_j \\ge S$$

## Input
- Dòng 1: Chứa 2 số nguyên $N$ và $S$ ($2 \\le N \\le 2 \\cdot 10^5, -10^{18} \\le S \\le 10^{18}$).
- Dòng 2: Chứa $N$ số nguyên $A_1, A_2, \\dots, A_N$ ($-10^9 \\le A_i \\le 10^9$).

## Output
- In ra một số nguyên duy nhất là số lượng cặp thỏa mãn.

## Sample 1
### Input
```text
5 8
2 5 1 4 3
```
### Output
```text
2
```
### Giải thích
Sắp xếp mảng: $[1, 2, 3, 4, 5]$. Các cặp có tổng $\\ge 8$ là: $(3, 5)$ (tổng 8), $(4, 5)$ (tổng 9). Tổng cộng có 2 cặp.

## Ràng buộc
- $100\\%$ số test có $N \\le 2 \\cdot 10^5$.
- Thời gian: $1.0\\text{s}$, Bộ nhớ: $256\\text{MB}$.
""",
        "guide": """# Hướng Dẫn Giảng Dạy: Đếm Cặp Tổng >= S
- Khi $A[L] + A[R] \\ge S \\implies$ với cố định $R$, mọi phần tử từ $L$ đến $R-1$ đều thỏa $\\implies$ cộng $R - L$, sau đó $--R$. Ngược lại $++L$.
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

    sort(a.begin(), a.end());

    int l = 0, r = n - 1;
    long long count = 0;

    while (l < r) {
        if (a[l] + a[r] >= s) {
            count += (r - l);
            --r;
        } else {
            ++l;
        }
    }

    cout << count << "\\n";
    return 0;
}
""",
        "gen_tests": lambda: [
            {"n": 5, "s": 8, "arr": [2, 5, 1, 4, 3]},
            {"n": 2, "s": 5, "arr": [2, 3]},
            {"n": 10, "s": 20, "arr": [random.randint(1, 20) for _ in range(10)]},
            {"n": 100, "s": 50, "arr": [random.randint(-50, 50) for _ in range(100)]},
            {"n": 500, "s": 1000, "arr": [random.randint(1, 1000) for _ in range(500)]},
            {"n": 1000, "s": 0, "arr": [random.randint(-1000, 1000) for _ in range(1000)]},
            {"n": 5000, "s": 10**6, "arr": [random.randint(1, 10**6) for _ in range(5000)]},
            {"n": 20000, "s": 10**9, "arr": [random.randint(-10**9, 10**9) for _ in range(20000)]},
            {"n": 50000, "s": 500000, "arr": [random.randint(-10**9, 10**9) for _ in range(50000)]},
            {"n": 100000, "s": 100000, "arr": list(range(1, 100001))},
            {"n": 100000, "s": 2 * 10**9, "arr": [random.randint(1, 10**9) for _ in range(100000)]},
            {"n": 200000, "s": 10**9, "arr": [random.randint(-10**9, 10**9) for _ in range(200000)]},
            {"n": 200000, "s": 0, "arr": [random.randint(-10**9, 10**9) for _ in range(200000)]},
            {"n": 200000, "s": 20, "arr": [10] * 200000},
            {"n": 200000, "s": 21, "arr": [10] * 200000},
            {"n": 200000, "s": 123456789, "arr": [random.randint(-10**9, 10**9) for _ in range(200000)]},
            {"n": 200000, "s": -500000, "arr": [random.randint(-10**9, 10**9) for _ in range(200000)]},
            {"n": 200000, "s": 10**18, "arr": [random.randint(-10**9, 10**9) for _ in range(200000)]},
            {"n": 200000, "s": -10**18, "arr": [random.randint(-10**9, 10**9) for _ in range(200000)]},
            {"n": 200000, "s": 999999999, "arr": [random.randint(-10**9, 10**9) for _ in range(200000)]},
        ],
        "format_inp": lambda t: f"{t['n']} {t['s']}\n" + " ".join(map(str, t['arr'])) + "\n"
    },

    # 5. IKH-0205
    {
        "id": "IKH-0205",
        "slug": "cpp1_02_thuyen_cuu_ho",
        "title": "Ghép Thuyền Cứu Hộ Tối Ưu",
        "statement": """# Ghép Thuyền Cứu Hộ Tối Ưu

## Bối cảnh
Có $N$ người cần qua sông bằng thuyền cứu hộ. Mỗi người thứ $i$ có cân nặng $W_i$. Mỗi chiếc thuyền chở tối đa **2 người** và tổng cân nặng không vượt quá $C$. Hãy tìm số thuyền ít nhất.

## Input
- Dòng 1: 2 số nguyên $N$ và $C$ ($1 \\le N \\le 10^5, 1 \\le C \\le 10^9$).
- Dòng 2: $N$ số nguyên $W_1, W_2, \\dots, W_N$ ($1 \\le W_i \\le C$).

## Output
- In ra một số nguyên duy nhất là số thuyền ít nhất cần dùng.

## Sample 1
### Input
```text
4 50
30 20 40 50
```
### Output
```text
3
```

## Ràng buộc
- $100\\%$ số test có $N \\le 10^5, C \\le 10^9$.
- Thời gian: $1.0\\text{s}$, Bộ nhớ: $256\\text{MB}$.
""",
        "guide": """# Hướng Dẫn Giảng Dạy: Ghép Thuyền Cứu Hộ
- Sắp xếp tăng dần. Nếu $W[L] + W[R] \\le C \\implies ++L, --R$. Ngược lại $--R$. Tăng `boats`.
""",
        "solution_cpp": """#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long c;
    if (!(cin >> n >> c)) return 0;

    vector<long long> w(n);
    for (int i = 0; i < n; ++i) cin >> w[i];

    sort(w.begin(), w.end());

    int l = 0, r = n - 1;
    int boats = 0;

    while (l <= r) {
        if (l == r) {
            ++boats;
            break;
        }
        if (w[l] + w[r] <= c) {
            ++l;
            --r;
        } else {
            --r;
        }
        ++boats;
    }

    cout << boats << "\\n";
    return 0;
}
""",
        "gen_tests": lambda: [
            {"n": 4, "c": 50, "arr": [30, 20, 40, 50]},
            {"n": 1, "c": 100, "arr": [50]},
            {"n": 2, "c": 100, "arr": [50, 50]},
            {"n": 10, "c": 100, "arr": [random.randint(10, 100) for _ in range(10)]},
            {"n": 100, "c": 1000, "arr": [random.randint(50, 1000) for _ in range(100)]},
            {"n": 500, "c": 5000, "arr": [random.randint(100, 5000) for _ in range(500)]},
            {"n": 1000, "c": 10**6, "arr": [random.randint(1, 10**6) for _ in range(1000)]},
            {"n": 5000, "c": 10**9, "arr": [random.randint(1, 10**9) for _ in range(5000)]},
            {"n": 20000, "c": 10**9, "arr": [random.randint(1, 10**9) for _ in range(20000)]},
            {"n": 50000, "c": 10**9, "arr": [random.randint(1, 10**9) for _ in range(50000)]},
            {"n": 100000, "c": 100, "arr": [50] * 100000},
            {"n": 100000, "c": 100, "arr": [60] * 100000},
            {"n": 100000, "c": 10**9, "arr": [random.randint(1, 10**9) for _ in range(100000)]},
            {"n": 100000, "c": 10**9, "arr": [random.randint(1, 10**9) for _ in range(100000)]},
            {"n": 100000, "c": 10**9, "arr": [random.randint(1, 10**9) for _ in range(100000)]},
            {"n": 100000, "c": 10**9, "arr": [random.randint(1, 10**9) for _ in range(100000)]},
            {"n": 100000, "c": 10**9, "arr": [random.randint(1, 10**9) for _ in range(100000)]},
            {"n": 100000, "c": 10**9, "arr": [random.randint(1, 10**9) for _ in range(100000)]},
            {"n": 100000, "c": 10**9, "arr": [random.randint(1, 10**9) for _ in range(100000)]},
            {"n": 100000, "c": 10**9, "arr": [random.randint(1, 10**9) for _ in range(100000)]},
        ],
        "format_inp": lambda t: f"{t['n']} {t['c']}\n" + " ".join(map(str, t['arr'])) + "\n"
    },

    # 6. IKH-0206
    {
        "id": "IKH-0206",
        "slug": "cpp1_02_van_chuyen_hang_hoa",
        "title": "Vận Chuyển Thùng Hàng Cực Đại",
        "statement": """# Vận Chuyển Thùng Hàng Cực Đại

## Bối cảnh
Một đội xe chuyên dụng cần chở $N$ kiện hàng $W_1, W_2, \\dots, W_N$ ($W_i \\le 10^{12}$) ra bến cảng. Mỗi xe chở tối đa **2 kiện hàng** và tổng khối lượng không vượt quá tải trọng $C$ ($C \\le 10^{12}$). Hãy tính số chuyến xe tối thiểu.

## Input
- Dòng 1: 2 số nguyên dương $N$ và $C$ ($1 \\le N \\le 10^5, 1 \\le C \\le 10^{12}$).
- Dòng 2: $N$ số nguyên dương $W_1, W_2, \\dots, W_N$ ($1 \\le W_i \\le C$).

## Output
- In ra số chuyến xe ít nhất.

## Sample 1
### Input
```text
5 10
3 5 8 2 7
```
### Output
```text
3
```

## Ràng buộc
- $100\\%$ số test có $N \\le 10^5, C \\le 10^{12}$.
- Thời gian: $1.0\\text{s}$, Bộ nhớ: $256\\text{MB}$.
""",
        "guide": """# Hướng Dẫn Giảng Dạy: Vận Chuyển Thùng Hàng
- Hai con trỏ với kiểu `long long` cho tải trọng $10^{12}$.
""",
        "solution_cpp": """#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long c;
    if (!(cin >> n >> c)) return 0;

    vector<long long> w(n);
    for (int i = 0; i < n; ++i) cin >> w[i];

    sort(w.begin(), w.end());

    int l = 0, r = n - 1;
    int trips = 0;

    while (l <= r) {
        if (l == r) {
            ++trips;
            break;
        }
        if (w[l] + w[r] <= c) {
            ++l;
            --r;
        } else {
            --r;
        }
        ++trips;
    }

    cout << trips << "\\n";
    return 0;
}
""",
        "gen_tests": lambda: [
            {"n": 5, "c": 10, "arr": [3, 5, 8, 2, 7]},
            {"n": 1, "c": 10**12, "arr": [5 * 10**11]},
            {"n": 2, "c": 10**12, "arr": [5 * 10**11, 5 * 10**11]},
            {"n": 10, "c": 1000, "arr": [random.randint(100, 1000) for _ in range(10)]},
            {"n": 100, "c": 10**6, "arr": [random.randint(1, 10**6) for _ in range(100)]},
            {"n": 1000, "c": 10**12, "arr": [random.randint(1, 10**12) for _ in range(1000)]},
            {"n": 5000, "c": 10**12, "arr": [random.randint(1, 10**12) for _ in range(5000)]},
            {"n": 20000, "c": 10**12, "arr": [random.randint(1, 10**12) for _ in range(20000)]},
            {"n": 50000, "c": 10**12, "arr": [random.randint(1, 10**12) for _ in range(50000)]},
            {"n": 100000, "c": 10**12, "arr": [random.randint(1, 10**12) for _ in range(100000)]},
            {"n": 100000, "c": 10**12, "arr": [random.randint(1, 10**12) for _ in range(100000)]},
            {"n": 100000, "c": 10**12, "arr": [random.randint(1, 10**12) for _ in range(100000)]},
            {"n": 100000, "c": 10**12, "arr": [random.randint(1, 10**12) for _ in range(100000)]},
            {"n": 100000, "c": 10**12, "arr": [random.randint(1, 10**12) for _ in range(100000)]},
            {"n": 100000, "c": 10**12, "arr": [random.randint(1, 10**12) for _ in range(100000)]},
            {"n": 100000, "c": 10**12, "arr": [random.randint(1, 10**12) for _ in range(100000)]},
            {"n": 100000, "c": 10**12, "arr": [random.randint(1, 10**12) for _ in range(100000)]},
            {"n": 100000, "c": 10**12, "arr": [random.randint(1, 10**12) for _ in range(100000)]},
            {"n": 100000, "c": 10**12, "arr": [random.randint(1, 10**12) for _ in range(100000)]},
            {"n": 100000, "c": 10**12, "arr": [random.randint(1, 10**12) for _ in range(100000)]},
        ],
        "format_inp": lambda t: f"{t['n']} {t['c']}\n" + " ".join(map(str, t['arr'])) + "\n"
    },

    # 7. IKH-0207 (HW P1: Tìm cặp có tổng gần S nhất)
    {
        "id": "IKH-0207",
        "slug": "cpp1_02_tong_gan_s_nhat",
        "title": "Tìm Cặp Có Tổng Gần S Nhất",
        "statement": """# Tìm Cặp Có Tổng Gần S Nhất

## Bối cảnh
Cho mảng gồm $N$ số nguyên và một số nguyên $S$. Hãy tìm một cặp số $(A_i, A_j)$ với $i < j$ sao cho tổng $A_i + A_j$ có độ chênh lệch $|(A_i + A_j) - S|$ là nhỏ nhất có thể. Nếu có nhiều cặp, in ra cặp có tổng nhỏ hơn.

## Input
- Dòng 1: Chứa 2 số nguyên $N$ và $S$ ($2 \\le N \\le 10^5, -10^{18} \\le S \\le 10^{18}$).
- Dòng 2: Chứa $N$ số nguyên $A_1, A_2, \\dots, A_N$ ($-10^9 \\le A_i \\le 10^9$).

## Output
- In ra 2 số nguyên biểu diễn cặp số tìm được theo thứ tự tăng dần.

## Sample 1
### Input
```text
5 20
2 8 13 4 25
```
### Output
```text
4 13
```
### Giải thích
Sắp xếp: $[2, 4, 8, 13, 25]$. Cặp $(4, 13)$ có tổng là 17 (chênh lệch với 20 là 3, nhỏ nhất).

## Ràng buộc
- $100\\%$ số test có $N \\le 10^5$.
- Thời gian: $1.0\\text{s}$, Bộ nhớ: $256\\text{MB}$.
""",
        "guide": """# Hướng Dẫn Giảng Dạy: Tổng Gần S Nhất
- Sắp xếp tăng dần. Duyệt $L, R$ và liên tục cập nhật tổng có chênh lệch $\\min$.
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

    sort(a.begin(), a.end());

    int l = 0, r = n - 1;
    long long best_diff = -1;
    long long ans_l = a[0], ans_r = a[1];

    while (l < r) {
        long long cur_sum = a[l] + a[r];
        long long cur_diff = abs(cur_sum - s);

        if (best_diff == -1 || cur_diff < best_diff || (cur_diff == best_diff && cur_sum < ans_l + ans_r)) {
            best_diff = cur_diff;
            ans_l = a[l];
            ans_r = a[r];
        }

        if (cur_sum == s) break;
        else if (cur_sum < s) ++l;
        else --r;
    }

    cout << ans_l << " " << ans_r << "\\n";
    return 0;
}
""",
        "gen_tests": lambda: [
            {"n": 5, "s": 20, "arr": [2, 8, 13, 4, 25]},
            {"n": 2, "s": 10, "arr": [3, 6]},
            {"n": 10, "s": 50, "arr": [random.randint(-50, 50) for _ in range(10)]},
            {"n": 100, "s": 100, "arr": [random.randint(-1000, 1000) for _ in range(100)]},
            {"n": 1000, "s": 10**6, "arr": [random.randint(-10**9, 10**9) for _ in range(1000)]},
            {"n": 5000, "s": 0, "arr": [random.randint(-10**9, 10**9) for _ in range(5000)]},
            {"n": 20000, "s": 10**9, "arr": [random.randint(-10**9, 10**9) for _ in range(20000)]},
            {"n": 50000, "s": -10**9, "arr": [random.randint(-10**9, 10**9) for _ in range(50000)]},
            {"n": 100000, "s": 123456, "arr": [random.randint(-10**9, 10**9) for _ in range(100000)]},
            {"n": 100000, "s": 10**18, "arr": [random.randint(-10**9, 10**9) for _ in range(100000)]},
            {"n": 100000, "s": 0, "arr": [random.randint(-10**9, 10**9) for _ in range(100000)]},
            {"n": 100000, "s": 20, "arr": [10] * 100000},
            {"n": 100000, "s": 987654321, "arr": [random.randint(-10**9, 10**9) for _ in range(100000)]},
            {"n": 100000, "s": -500000, "arr": [random.randint(-10**9, 10**9) for _ in range(100000)]},
            {"n": 100000, "s": 10**9, "arr": [random.randint(-10**9, 10**9) for _ in range(100000)]},
            {"n": 100000, "s": -10**9, "arr": [random.randint(-10**9, 10**9) for _ in range(100000)]},
            {"n": 100000, "s": 7777777, "arr": [random.randint(-10**9, 10**9) for _ in range(100000)]},
            {"n": 100000, "s": 8888888, "arr": [random.randint(-10**9, 10**9) for _ in range(100000)]},
            {"n": 100000, "s": 9999999, "arr": [random.randint(-10**9, 10**9) for _ in range(100000)]},
            {"n": 100000, "s": 1111111, "arr": [random.randint(-10**9, 10**9) for _ in range(100000)]},
        ],
        "format_inp": lambda t: f"{t['n']} {t['s']}\n" + " ".join(map(str, t['arr'])) + "\n"
    },

    # 8. IKH-0208 (HW P2: Tìm cặp có hiệu đúng bằng K)
    {
        "id": "IKH-0208",
        "slug": "cpp1_02_hieu_hai_so_bang_k",
        "title": "Tìm Cặp Có Hiệu Đúng Bằng K",
        "statement": """# Tìm Cặp Có Hiệu Đúng Bằng K

## Bối cảnh
Cho mảng gồm $N$ số nguyên và số nguyên không âm $K$. Hãy kiểm tra xem có tồn tại cặp chỉ số $(i, j)$ với $i \\neq j$ sao cho $A_j - A_i = K$ hay không. Nếu có in ra `YES`, ngược lại in ra `NO`.

## Input
- Dòng 1: Chứa 2 số nguyên $N$ và $K$ ($2 \\le N \\le 10^5, 0 \\le K \\le 10^{18}$).
- Dòng 2: Chứa $N$ số nguyên $A_1, A_2, \\dots, A_N$ ($-10^9 \\le A_i \\le 10^9$).

## Output
- In ra `YES` hoặc `NO`.

## Sample 1
### Input
```text
5 3
1 8 5 3 2
```
### Output
```text
YES
```
### Giải thích
Cặp $(5, 8)$ hoặc $(2, 5)$ có hiệu $8 - 5 = 3 = K$.

## Ràng buộc
- $100\\%$ số test có $N \\le 10^5$.
- Thời gian: $1.0\\text{s}$, Bộ nhớ: $256\\text{MB}$.
""",
        "guide": """# Hướng Dẫn Giảng Dạy: Hiệu Hai Số Bằng K
- Sắp xếp tăng dần. Dùng hai con trỏ cùng chiều $L = 0, R = 1$. Khi $A[R] - A[L] < K \\implies ++R$. Khi $> K \\implies ++L$.
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

    sort(a.begin(), a.end());

    int l = 0, r = 1;
    bool found = false;

    while (r < n) {
        if (l == r) {
            ++r;
            continue;
        }
        long long diff = a[r] - a[l];
        if (diff == k) {
            found = true;
            break;
        } else if (diff < k) {
            ++r;
        } else {
            ++l;
        }
    }

    if (found) cout << "YES\\n";
    else cout << "NO\\n";
    return 0;
}
""",
        "gen_tests": lambda: [
            {"n": 5, "k": 3, "arr": [1, 8, 5, 3, 2]},
            {"n": 2, "k": 0, "arr": [5, 5]},
            {"n": 2, "k": 1, "arr": [5, 5]},
            {"n": 10, "k": 5, "arr": [random.randint(1, 30) for _ in range(10)]},
            {"n": 100, "k": 20, "arr": [random.randint(-100, 100) for _ in range(100)]},
            {"n": 1000, "k": 500, "arr": [random.randint(-10**9, 10**9) for _ in range(1000)]},
            {"n": 5000, "k": 1000, "arr": [random.randint(-10**9, 10**9) for _ in range(5000)]},
            {"n": 20000, "k": 10**6, "arr": [random.randint(-10**9, 10**9) for _ in range(20000)]},
            {"n": 50000, "k": 0, "arr": [random.randint(-10**9, 10**9) for _ in range(50000)]},
            {"n": 100000, "k": 10**9, "arr": [random.randint(-10**9, 10**9) for _ in range(100000)]},
            {"n": 100000, "k": 1, "arr": list(range(1, 100001))},
            {"n": 100000, "k": 100000, "arr": list(range(1, 100001))},
            {"n": 100000, "k": 10**18, "arr": [random.randint(-10**9, 10**9) for _ in range(100000)]},
            {"n": 100000, "k": 123456, "arr": [random.randint(-10**9, 10**9) for _ in range(100000)]},
            {"n": 100000, "k": 999999, "arr": [random.randint(-10**9, 10**9) for _ in range(100000)]},
            {"n": 100000, "k": 0, "arr": [random.randint(1, 10) for _ in range(100000)]},
            {"n": 100000, "k": 5, "arr": [random.randint(1, 100) for _ in range(100000)]},
            {"n": 100000, "k": 50, "arr": [random.randint(1, 100) for _ in range(100000)]},
            {"n": 100000, "k": 1000, "arr": [random.randint(-10**9, 10**9) for _ in range(100000)]},
            {"n": 100000, "k": 2000, "arr": [random.randint(-10**9, 10**9) for _ in range(100000)]},
        ],
        "format_inp": lambda t: f"{t['n']} {t['k']}\n" + " ".join(map(str, t['arr'])) + "\n"
    },

    # 9. IKH-0209 (HW P3: 3-Sum)
    {
        "id": "IKH-0209",
        "slug": "cpp1_02_bo_ba_tong_bang_s",
        "title": "Bộ Ba Số Có Tổng Bằng S (3-Sum)",
        "statement": """# Bộ Ba Số Có Tổng Bằng S (3-Sum)

## Bối cảnh
Cho mảng gồm $N$ số nguyên và một số nguyên $S$. Hãy tìm 3 phần tử ở 3 vị trí phân biệt trong mảng có tổng đúng bằng $S$. Nếu có nhiều bộ, in ra một bộ bất kỳ theo thứ tự tăng dần. Nếu không tồn tại, in ra `-1`.

## Input
- Dòng 1: Chứa 2 số nguyên $N$ và $S$ ($3 \\le N \\le 3000, -10^{18} \\le S \\le 10^{18}$).
- Dòng 2: Chứa $N$ số nguyên $A_1, A_2, \\dots, A_N$ ($-10^9 \\le A_i \\le 10^9$).

## Output
- In ra 3 số nguyên theo thứ tự tăng dần, hoặc `-1`.

## Sample 1
### Input
```text
6 15
2 7 5 1 8 4
```
### Output
```text
2 5 8
```

## Ràng buộc
- $100\\%$ số test có $N \\le 3000$.
- Thời gian: $1.0\\text{s}$, Bộ nhớ: $256\\text{MB}$.
""",
        "guide": """# Hướng Dẫn Giảng Dạy: 3-Sum
- Sắp xếp tăng dần. Cố định phần tử $i$, dùng Two Pointers trên $[i+1 \dots N-1]$ tìm tổng $S - A[i]$.
- Độ phức tạp: $\\mathcal{O}(N^2)$.
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

    sort(a.begin(), a.end());

    for (int i = 0; i < n - 2; ++i) {
        long long target = s - a[i];
        int l = i + 1, r = n - 1;
        while (l < r) {
            long long sum = a[l] + a[r];
            if (sum == target) {
                cout << a[i] << " " << a[l] << " " << a[r] << "\\n";
                return 0;
            } else if (sum < target) {
                ++l;
            } else {
                --r;
            }
        }
    }

    cout << -1 << "\\n";
    return 0;
}
""",
        "gen_tests": lambda: [
            {"n": 6, "s": 15, "arr": [2, 7, 5, 1, 8, 4]},
            {"n": 3, "s": 6, "arr": [1, 2, 3]},
            {"n": 3, "s": 10, "arr": [1, 2, 3]},
            {"n": 10, "s": 30, "arr": [random.randint(1, 20) for _ in range(10)]},
            {"n": 50, "s": 50, "arr": [random.randint(-50, 50) for _ in range(50)]},
            {"n": 100, "s": 0, "arr": [random.randint(-100, 100) for _ in range(100)]},
            {"n": 300, "s": 1000, "arr": [random.randint(-1000, 1000) for _ in range(300)]},
            {"n": 500, "s": 10**6, "arr": [random.randint(-10**9, 10**9) for _ in range(500)]},
            {"n": 1000, "s": 0, "arr": [random.randint(-10**9, 10**9) for _ in range(1000)]},
            {"n": 1500, "s": 123456, "arr": [random.randint(-10**9, 10**9) for _ in range(1500)]},
            {"n": 2000, "s": 10**9, "arr": [random.randint(-10**9, 10**9) for _ in range(2000)]},
            {"n": 2500, "s": -10**9, "arr": [random.randint(-10**9, 10**9) for _ in range(2500)]},
            {"n": 3000, "s": 10**18, "arr": [random.randint(-10**9, 10**9) for _ in range(3000)]},
            {"n": 3000, "s": 30, "arr": [10] * 3000},
            {"n": 3000, "s": 0, "arr": [random.randint(-10**9, 10**9) for _ in range(3000)]},
            {"n": 3000, "s": 999999, "arr": [random.randint(-10**9, 10**9) for _ in range(3000)]},
            {"n": 3000, "s": -999999, "arr": [random.randint(-10**9, 10**9) for _ in range(3000)]},
            {"n": 3000, "s": 12345678, "arr": [random.randint(-10**9, 10**9) for _ in range(3000)]},
            {"n": 3000, "s": -12345678, "arr": [random.randint(-10**9, 10**9) for _ in range(3000)]},
            {"n": 3000, "s": 7777777, "arr": [random.randint(-10**9, 10**9) for _ in range(3000)]},
        ],
        "format_inp": lambda t: f"{t['n']} {t['s']}\n" + " ".join(map(str, t['arr'])) + "\n"
    },

    # 10. IKH-0210 (HW P3: Đếm số tam giác)
    {
        "id": "IKH-0210",
        "slug": "cpp1_02_dem_so_tam_giac",
        "title": "Đếm Số Tam Giác Có Thể Tạo Thành",
        "statement": """# Đếm Số Tam Giác Có Thể Tạo Thành

## Bối cảnh
Cho $N$ đoạn que với độ dài $A_1, A_2, \\dots, A_N$. Hãy đếm số lượng bộ 3 que có thể ghép lại thành một tam giác không suy biến (tổng 2 cạnh bất kỳ lớn hơn cạnh còn lại).

## Input
- Dòng 1: Số nguyên dương $N$ ($3 \\le N \\le 3000$).
- Dòng 2: $N$ số nguyên dương $A_1, A_2, \\dots, A_N$ ($1 \\le A_i \\le 10^9$).

## Output
- In ra một số nguyên duy nhất là số lượng tam giác tạo được.

## Sample 1
### Input
```text
4
4 6 3 7
```
### Output
```text
3
```
### Giải thích
Các bộ 3 tạo tam giác: $(3, 4, 6), (3, 6, 7), (4, 6, 7)$.

## Ràng buộc
- $100\\%$ số test có $N \\le 3000, 1 \\le A_i \\le 10^9$.
- Thời gian: $1.0\\text{s}$, Bộ nhớ: $256\\text{MB}$.
""",
        "guide": """# Hướng Dẫn Giảng Dạy: Đếm Tam Giác
- Sắp xếp tăng dần. Cố định cạnh lớn nhất $k$ từ $N-1$ về $2$.
- Dùng Two Pointers $L = 0, R = k - 1$. Khi $A[L] + A[R] > A[k] \\implies$ có $R - L$ cặp, sau đó $--R$. Ngược lại $++L$.
- Độ phức tạp: $\\mathcal{O}(N^2)$.
""",
        "solution_cpp": """#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    sort(a.begin(), a.end());

    long long count = 0;

    for (int k = n - 1; k >= 2; --k) {
        int l = 0, r = k - 1;
        while (l < r) {
            if (a[l] + a[r] > a[k]) {
                count += (r - l);
                --r;
            } else {
                ++l;
            }
        }
    }

    cout << count << "\\n";
    return 0;
}
""",
        "gen_tests": lambda: [
            {"n": 4, "arr": [4, 6, 3, 7]},
            {"n": 3, "arr": [1, 2, 3]},
            {"n": 3, "arr": [3, 4, 5]},
            {"n": 10, "arr": [random.randint(1, 50) for _ in range(10)]},
            {"n": 50, "arr": [random.randint(1, 1000) for _ in range(50)]},
            {"n": 100, "arr": [random.randint(1, 10**6) for _ in range(100)]},
            {"n": 300, "arr": [random.randint(1, 10**9) for _ in range(300)]},
            {"n": 500, "arr": [random.randint(1, 10**9) for _ in range(500)]},
            {"n": 1000, "arr": [random.randint(1, 10**9) for _ in range(1000)]},
            {"n": 1500, "arr": [random.randint(1, 10**9) for _ in range(1500)]},
            {"n": 2000, "arr": [random.randint(1, 10**9) for _ in range(2000)]},
            {"n": 2500, "arr": [random.randint(1, 10**9) for _ in range(2500)]},
            {"n": 3000, "arr": [10] * 3000},
            {"n": 3000, "arr": list(range(1, 3001))},
            {"n": 3000, "arr": [random.randint(1, 10**9) for _ in range(3000)]},
            {"n": 3000, "arr": [random.randint(1, 10**9) for _ in range(3000)]},
            {"n": 3000, "arr": [random.randint(1, 10**9) for _ in range(3000)]},
            {"n": 3000, "arr": [random.randint(1, 10**9) for _ in range(3000)]},
            {"n": 3000, "arr": [random.randint(1, 10**9) for _ in range(3000)]},
            {"n": 3000, "arr": [random.randint(1, 10**9) for _ in range(3000)]},
        ],
        "format_inp": lambda t: f"{t['n']}\n" + " ".join(map(str, t['arr'])) + "\n"
    },

    # 11. IKH-0211 (HW P4: Đếm cặp tổng S trên mảng trùng lặp)
    {
        "id": "IKH-0211",
        "slug": "cpp1_02_dem_cap_trung_lap",
        "title": "Đếm Cặp Tổng S Trên Mảng Trùng Lặp",
        "statement": """# Đếm Cặp Tổng S Trên Mảng Trùng Lặp

## Bối cảnh
Cho mảng gồm $N$ số nguyên có thể chứa nhiều phần tử trùng lặp và số nguyên $S$. Hãy đếm số lượng cặp chỉ số $(i, j)$ với $1 \\le i < j \\le N$ sao cho $A_i + A_j = S$.

## Input
- Dòng 1: 2 số nguyên $N$ và $S$ ($2 \\le N \\le 2 \\cdot 10^5, -10^{18} \\le S \\le 10^{18}$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \\dots, A_N$ ($-10^9 \\le A_i \\le 10^9$).

## Output
- In ra một số nguyên duy nhất là số lượng cặp chỉ số thỏa mãn.

## Sample 1
### Input
```text
6 6
3 3 3 3 3 3
```
### Output
```text
15
```

## Ràng buộc
- $100\\%$ số test có $N \\le 2 \\cdot 10^5$.
- Thời gian: $1.0\\text{s}$, Bộ nhớ: $256\\text{MB}$.
""",
        "guide": """# Hướng Dẫn Giảng Dạy: Đếm Cặp Trùng Lặp
- Sắp xếp tăng dần. Dùng Two Pointers đếm số lượng phần tử bằng $A[L]$ ($c_1$) và $A[R]$ ($c_2$):
  - Nếu $A[L] == A[R] \\implies$ cộng $c_1(c_1-1)/2$.
  - Nếu $A[L] \\neq A[R] \\implies$ cộng $c_1 \\times c_2$.
- Độ phức tạp: $\\mathcal{O}(N \\log N)$.
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

    sort(a.begin(), a.end());

    int l = 0, r = n - 1;
    long long ans = 0;

    while (l < r) {
        long long sum = a[l] + a[r];
        if (sum == s) {
            if (a[l] == a[r]) {
                long long cnt = r - l + 1;
                ans += cnt * (cnt - 1) / 2;
                break;
            } else {
                long long c1 = 1, c2 = 1;
                while (l + 1 < r && a[l + 1] == a[l]) { ++c1; ++l; }
                while (r - 1 > l && a[r - 1] == a[r]) { ++c2; --r; }
                ans += c1 * c2;
                ++l;
                --r;
            }
        } else if (sum < s) {
            ++l;
        } else {
            --r;
        }
    }

    cout << ans << "\\n";
    return 0;
}
""",
        "gen_tests": lambda: [
            {"n": 6, "s": 6, "arr": [3, 3, 3, 3, 3, 3]},
            {"n": 2, "s": 10, "arr": [5, 5]},
            {"n": 5, "s": 10, "arr": [2, 8, 2, 8, 5]},
            {"n": 10, "s": 10, "arr": [random.randint(1, 10) for _ in range(10)]},
            {"n": 100, "s": 20, "arr": [random.randint(1, 20) for _ in range(100)]},
            {"n": 1000, "s": 50, "arr": [random.randint(1, 50) for _ in range(1000)]},
            {"n": 5000, "s": 100, "arr": [random.randint(1, 100) for _ in range(5000)]},
            {"n": 20000, "s": 1000, "arr": [random.randint(1, 1000) for _ in range(20000)]},
            {"n": 50000, "s": 10**6, "arr": [random.randint(-10**6, 10**6) for _ in range(50000)]},
            {"n": 100000, "s": 0, "arr": [random.randint(-10**5, 10**5) for _ in range(100000)]},
            {"n": 200000, "s": 10, "arr": [5] * 200000},
            {"n": 200000, "s": 200001, "arr": list(range(1, 200001))},
            {"n": 200000, "s": 10**9, "arr": [random.randint(-10**9, 10**9) for _ in range(200000)]},
            {"n": 200000, "s": 0, "arr": [random.randint(-10**9, 10**9) for _ in range(200000)]},
            {"n": 200000, "s": 123456789, "arr": [random.randint(-10**9, 10**9) for _ in range(200000)]},
            {"n": 200000, "s": -500000, "arr": [random.randint(-10**9, 10**9) for _ in range(200000)]},
            {"n": 200000, "s": 10**18, "arr": [random.randint(-10**9, 10**9) for _ in range(200000)]},
            {"n": 200000, "s": -10**18, "arr": [random.randint(-10**9, 10**9) for _ in range(200000)]},
            {"n": 200000, "s": 7777777, "arr": [random.randint(-10**9, 10**9) for _ in range(200000)]},
            {"n": 200000, "s": 8888888, "arr": [random.randint(-10**9, 10**9) for _ in range(200000)]},
        ],
        "format_inp": lambda t: f"{t['n']} {t['s']}\n" + " ".join(map(str, t['arr'])) + "\n"
    },

    # 12. IKH-0212 (HW P4: Ghép cặp trẻ em và bánh quy)
    {
        "id": "IKH-0212",
        "slug": "cpp1_02_ghep_tre_em_banh_quy",
        "title": "Ghép Cặp Trẻ Em Và Bánh Quy",
        "statement": """# Ghép Cặp Trẻ Em Và Bánh Quy

## Bối cảnh
Có $N$ đứa trẻ và $M$ chiếc bánh quy. Đứa trẻ thứ $i$ có mức độ thèm ăn $G_i$ (chỉ hài lòng nếu nhận được bánh có kích thước $\\ge G_i$). Chiếc bánh thứ $j$ có kích thước $S_j$. Mỗi đứa trẻ nhận tối đa 1 bánh và mỗi bánh chỉ phát cho 1 trẻ. Hãy tính số lượng đứa trẻ tối đa có thể được thỏa mãn.

## Input
- Dòng 1: 2 số nguyên $N$ và $M$ ($1 \\le N, M \\le 10^5$).
- Dòng 2: $N$ số nguyên $G_1, G_2, \\dots, G_N$ ($1 \\le G_i \\le 10^9$).
- Dòng 3: $M$ số nguyên $S_1, S_2, \\dots, S_M$ ($1 \\le S_j \\le 10^9$).

## Output
- In ra số lượng đứa trẻ tối đa được thỏa mãn.

## Sample 1
### Input
```text
3 2
1 2 3
1 1
```
### Output
```text
1
```

## Ràng buộc
- $100\\%$ số test có $N, M \\le 10^5$.
- Thời gian: $1.0\\text{s}$, Bộ nhớ: $256\\text{MB}$.
""",
        "guide": """# Hướng Dẫn Giảng Dạy: Trẻ Em Và Bánh Quy
- Sắp xếp cả 2 mảng tăng dần. Dùng Hai con trỏ ghép bánh nhỏ nhất vừa đủ thỏa mãn đứa trẻ nhỏ nhất.
""",
        "solution_cpp": """#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<long long> g(n), s(m);
    for (int i = 0; i < n; ++i) cin >> g[i];
    for (int i = 0; i < m; ++i) cin >> s[i];

    sort(g.begin(), g.end());
    sort(s.begin(), s.end());

    int i = 0, j = 0;
    int satisfied = 0;

    while (i < n && j < m) {
        if (s[j] >= g[i]) {
            ++satisfied;
            ++i;
            ++j;
        } else {
            ++j;
        }
    }

    cout << satisfied << "\\n";
    return 0;
}
""",
        "gen_tests": lambda: [
            {"n": 3, "m": 2, "g": [1, 2, 3], "s": [1, 1]},
            {"n": 2, "m": 3, "g": [1, 2], "s": [1, 2, 3]},
            {"n": 1, "m": 1, "g": [5], "s": [4]},
            {"n": 10, "m": 10, "g": [random.randint(1, 20) for _ in range(10)], "s": [random.randint(1, 20) for _ in range(10)]},
            {"n": 100, "m": 80, "g": [random.randint(1, 1000) for _ in range(100)], "s": [random.randint(1, 1000) for _ in range(80)]},
            {"n": 1000, "m": 1000, "g": [random.randint(1, 10**6) for _ in range(1000)], "s": [random.randint(1, 10**6) for _ in range(1000)]},
            {"n": 5000, "m": 5000, "g": [random.randint(1, 10**9) for _ in range(5000)], "s": [random.randint(1, 10**9) for _ in range(5000)]},
            {"n": 20000, "m": 20000, "g": [random.randint(1, 10**9) for _ in range(20000)], "s": [random.randint(1, 10**9) for _ in range(20000)]},
            {"n": 50000, "m": 50000, "g": [random.randint(1, 10**9) for _ in range(50000)], "s": [random.randint(1, 10**9) for _ in range(50000)]},
            {"n": 100000, "m": 100000, "g": [10] * 100000, "s": [10] * 100000},
            {"n": 100000, "m": 100000, "g": [10] * 100000, "s": [9] * 100000},
            {"n": 100000, "m": 100000, "g": list(range(1, 100001)), "s": list(range(1, 100001))},
            {"n": 100000, "m": 50000, "g": [random.randint(1, 10**9) for _ in range(100000)], "s": [random.randint(1, 10**9) for _ in range(50000)]},
            {"n": 50000, "m": 100000, "g": [random.randint(1, 10**9) for _ in range(50000)], "s": [random.randint(1, 10**9) for _ in range(100000)]},
            {"n": 100000, "m": 100000, "g": [random.randint(1, 10**9) for _ in range(100000)], "s": [random.randint(1, 10**9) for _ in range(100000)]},
            {"n": 100000, "m": 100000, "g": [random.randint(1, 10**9) for _ in range(100000)], "s": [random.randint(1, 10**9) for _ in range(100000)]},
            {"n": 100000, "m": 100000, "g": [random.randint(1, 10**9) for _ in range(100000)], "s": [random.randint(1, 10**9) for _ in range(100000)]},
            {"n": 100000, "m": 100000, "g": [random.randint(1, 10**9) for _ in range(100000)], "s": [random.randint(1, 10**9) for _ in range(100000)]},
            {"n": 100000, "m": 100000, "g": [random.randint(1, 10**9) for _ in range(100000)], "s": [random.randint(1, 10**9) for _ in range(100000)]},
            {"n": 100000, "m": 100000, "g": [random.randint(1, 10**9) for _ in range(100000)], "s": [random.randint(1, 10**9) for _ in range(100000)]},
        ],
        "format_inp": lambda t: f"{t['n']} {t['m']}\n" + " ".join(map(str, t['g'])) + "\n" + " ".join(map(str, t['s'])) + "\n"
    },

    # 13. IKH-0213 (HW P5: 4-Sum)
    {
        "id": "IKH-0213",
        "slug": "cpp1_02_bo_bon_tong_bang_s",
        "title": "Bộ Bốn Số Có Tổng Bằng S (4-Sum)",
        "statement": """# Bộ Bốn Số Có Tổng Bằng S (4-Sum)

## Bối cảnh
Cho mảng gồm $N$ số nguyên và số nguyên $S$. Hãy tìm 4 phần tử ở 4 vị trí phân biệt có tổng đúng bằng $S$. Nếu có nhiều bộ, in ra một bộ theo thứ tự tăng dần. Nếu không tồn tại, in ra `-1`.

## Input
- Dòng 1: 2 số nguyên $N$ và $S$ ($4 \\le N \\le 1000, -10^{18} \\le S \\le 10^{18}$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \\dots, A_N$ ($-10^9 \\le A_i \\le 10^9$).

## Output
- In ra 4 số nguyên tăng dần hoặc `-1`.

## Sample 1
### Input
```text
6 20
2 7 5 1 8 4
```
### Output
```text
1 4 7 8
```

## Ràng buộc
- $100\\%$ số test có $N \\le 1000$.
- Thời gian: $1.0\\text{s}$, Bộ nhớ: $256\\text{MB}$.
""",
        "guide": """# Hướng Dẫn Giảng Dạy: 4-Sum
- Sắp xếp tăng dần. Dùng 2 vòng lặp lồng nhau cố định $i, j$ và Two Pointers trên $[j+1 \dots N-1]$.
- Độ phức tạp: $\\mathcal{O}(N^3)$.
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

    sort(a.begin(), a.end());

    for (int i = 0; i < n - 3; ++i) {
        for (int j = i + 1; j < n - 2; ++j) {
            long long target = s - a[i] - a[j];
            int l = j + 1, r = n - 1;
            while (l < r) {
                long long sum = a[l] + a[r];
                if (sum == target) {
                    cout << a[i] << " " << a[j] << " " << a[l] << " " << a[r] << "\\n";
                    return 0;
                } else if (sum < target) {
                    ++l;
                } else {
                    --r;
                }
            }
        }
    }

    cout << -1 << "\\n";
    return 0;
}
""",
        "gen_tests": lambda: [
            {"n": 6, "s": 20, "arr": [2, 7, 5, 1, 8, 4]},
            {"n": 4, "s": 10, "arr": [1, 2, 3, 4]},
            {"n": 4, "s": 15, "arr": [1, 2, 3, 4]},
            {"n": 10, "s": 40, "arr": [random.randint(1, 20) for _ in range(10)]},
            {"n": 50, "s": 100, "arr": [random.randint(-100, 100) for _ in range(50)]},
            {"n": 100, "s": 0, "arr": [random.randint(-1000, 1000) for _ in range(100)]},
            {"n": 200, "s": 10**6, "arr": [random.randint(-10**9, 10**9) for _ in range(200)]},
            {"n": 400, "s": 0, "arr": [random.randint(-10**9, 10**9) for _ in range(400)]},
            {"n": 600, "s": 123456, "arr": [random.randint(-10**9, 10**9) for _ in range(600)]},
            {"n": 800, "s": -999999, "arr": [random.randint(-10**9, 10**9) for _ in range(800)]},
            {"n": 1000, "s": 40, "arr": [10] * 1000},
            {"n": 1000, "s": 10**18, "arr": [random.randint(-10**9, 10**9) for _ in range(1000)]},
            {"n": 1000, "s": -10**18, "arr": [random.randint(-10**9, 10**9) for _ in range(1000)]},
            {"n": 1000, "s": 0, "arr": [random.randint(-10**9, 10**9) for _ in range(1000)]},
            {"n": 1000, "s": 12345678, "arr": [random.randint(-10**9, 10**9) for _ in range(1000)]},
            {"n": 1000, "s": -12345678, "arr": [random.randint(-10**9, 10**9) for _ in range(1000)]},
            {"n": 1000, "s": 7777777, "arr": [random.randint(-10**9, 10**9) for _ in range(1000)]},
            {"n": 1000, "s": 8888888, "arr": [random.randint(-10**9, 10**9) for _ in range(1000)]},
            {"n": 1000, "s": 9999999, "arr": [random.randint(-10**9, 10**9) for _ in range(1000)]},
            {"n": 1000, "s": 1111111, "arr": [random.randint(-10**9, 10**9) for _ in range(1000)]},
        ],
        "format_inp": lambda t: f"{t['n']} {t['s']}\n" + " ".join(map(str, t['arr'])) + "\n"
    },

    # 14. IKH-0214 (HW P5: Hai con trỏ đa điều kiện)
    {
        "id": "IKH-0214",
        "slug": "cpp1_02_hai_con_tro_cuc_han",
        "title": "Cặp Số Tối Ưu Với Chênh Lệch Cực Hạn",
        "statement": """# Cặp Số Tối Ưu Với Chênh Lệch Cực Hạn

## Bối cảnh
Cho 2 dãy số nguyên $A$ gồm $N$ phần tử và $B$ gồm $M$ phần tử. Hãy tìm một phần tử $A_i$ và một phần tử $B_j$ sao cho độ chênh lệch $|A_i - B_j|$ là nhỏ nhất có thể.

## Input
- Dòng 1: 2 số nguyên $N$ và $M$ ($1 \\le N, M \\le 2 \\cdot 10^5$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \\dots, A_N$ ($-10^{18} \\le A_i \\le 10^{18}$).
- Dòng 3: $M$ số nguyên $B_1, B_2, \\dots, B_M$ ($-10^{18} \\le B_j \\le 10^{18}$).

## Output
- In ra một số nguyên duy nhất là giá trị chênh lệch nhỏ nhất $|A_i - B_j|$.

## Sample 1
### Input
```text
3 3
1 5 10
2 8 14
```
### Output
```text
1
```
### Giải thích
Chọn $A_1 = 1, B_1 = 2$ có chênh lệch $|1 - 2| = 1$.

## Ràng buộc
- $100\\%$ số test có $N, M \\le 2 \\cdot 10^5$.
- Thời gian: $1.0\\text{s}$, Bộ nhớ: $256\\text{MB}$.
""",
        "guide": """# Hướng Dẫn Giảng Dạy: Chênh Lệch Nhỏ Nhất Giữa 2 Mảng
- Sắp xếp cả 2 mảng tăng dần. Dùng Hai con trỏ $i, j$:
  - Nếu $A[i] < B[j] \\implies ++i$.
  - Nếu $A[i] > B[j] \\implies ++j$.
  - Nếu $A[i] == B[j] \\implies$ chênh lệch bằng 0.
- Độ phức tạp: $\\mathcal{O}(N \\log N + M \\log M)$.
""",
        "solution_cpp": """#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<long long> a(n), b(m);
    for (int i = 0; i < n; ++i) cin >> a[i];
    for (int i = 0; i < m; ++i) cin >> b[i];

    sort(a.begin(), a.end());
    sort(b.begin(), b.end());

    int i = 0, j = 0;
    long long min_diff = abs(a[0] - b[0]);

    while (i < n && j < m) {
        min_diff = min(min_diff, abs(a[i] - b[j]));
        if (a[i] == b[j]) break;
        else if (a[i] < b[j]) ++i;
        else ++j;
    }

    cout << min_diff << "\\n";
    return 0;
}
""",
        "gen_tests": lambda: [
            {"n": 3, "m": 3, "a": [1, 5, 10], "b": [2, 8, 14]},
            {"n": 1, "m": 1, "a": [10**18], "b": [-10**18]},
            {"n": 2, "m": 2, "a": [5, 10], "b": [5, 10]},
            {"n": 10, "m": 10, "a": [random.randint(-50, 50) for _ in range(10)], "b": [random.randint(-50, 50) for _ in range(10)]},
            {"n": 100, "m": 100, "a": [random.randint(-1000, 1000) for _ in range(100)], "b": [random.randint(-1000, 1000) for _ in range(100)]},
            {"n": 1000, "m": 1000, "a": [random.randint(-10**9, 10**9) for _ in range(1000)], "b": [random.randint(-10**9, 10**9) for _ in range(1000)]},
            {"n": 5000, "m": 5000, "a": [random.randint(-10**18, 10**18) for _ in range(5000)], "b": [random.randint(-10**18, 10**18) for _ in range(5000)]},
            {"n": 20000, "m": 20000, "a": [random.randint(-10**18, 10**18) for _ in range(20000)], "b": [random.randint(-10**18, 10**18) for _ in range(20000)]},
            {"n": 50000, "m": 50000, "a": [random.randint(-10**18, 10**18) for _ in range(50000)], "b": [random.randint(-10**18, 10**18) for _ in range(50000)]},
            {"n": 100000, "m": 100000, "a": [0] * 100000, "b": [0] * 100000},
            {"n": 100000, "m": 100000, "a": list(range(1, 100001)), "b": list(range(100001, 200001))},
            {"n": 200000, "m": 200000, "a": [random.randint(-10**18, 10**18) for _ in range(200000)], "b": [random.randint(-10**18, 10**18) for _ in range(200000)]},
            {"n": 200000, "m": 200000, "a": [random.randint(-10**18, 10**18) for _ in range(200000)], "b": [random.randint(-10**18, 10**18) for _ in range(200000)]},
            {"n": 200000, "m": 200000, "a": [random.randint(-10**18, 10**18) for _ in range(200000)], "b": [random.randint(-10**18, 10**18) for _ in range(200000)]},
            {"n": 200000, "m": 200000, "a": [random.randint(-10**18, 10**18) for _ in range(200000)], "b": [random.randint(-10**18, 10**18) for _ in range(200000)]},
            {"n": 200000, "m": 200000, "a": [random.randint(-10**18, 10**18) for _ in range(200000)], "b": [random.randint(-10**18, 10**18) for _ in range(200000)]},
            {"n": 200000, "m": 200000, "a": [random.randint(-10**18, 10**18) for _ in range(200000)], "b": [random.randint(-10**18, 10**18) for _ in range(200000)]},
            {"n": 200000, "m": 200000, "a": [random.randint(-10**18, 10**18) for _ in range(200000)], "b": [random.randint(-10**18, 10**18) for _ in range(200000)]},
            {"n": 200000, "m": 200000, "a": [random.randint(-10**18, 10**18) for _ in range(200000)], "b": [random.randint(-10**18, 10**18) for _ in range(200000)]},
            {"n": 200000, "m": 200000, "a": [random.randint(-10**18, 10**18) for _ in range(200000)], "b": [random.randint(-10**18, 10**18) for _ in range(200000)]},
        ],
        "format_inp": lambda t: f"{t['n']} {t['m']}\n" + " ".join(map(str, t['a'])) + "\n" + " ".join(map(str, t['b'])) + "\n"
    }
]

if __name__ == "__main__":
    print(f"Building {len(LESSON02_PROBLEMS)} problems for Lesson 02...")
    for p in LESSON02_PROBLEMS:
        build_problem(p)
    print("🎉 Done Lesson 02!")
