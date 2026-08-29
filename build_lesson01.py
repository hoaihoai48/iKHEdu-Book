import random
from generate_module01_all_problems import build_problem

LESSON01_PROBLEMS = [
    # 1. IKH-0101
    {
        "id": "IKH-0101",
        "slug": "cpp1_01_xep_hang_diem_danh",
        "title": "Xếp Hàng Điểm Danh",
        "statement": """# Xếp Hàng Điểm Danh

## Bối cảnh
Trong buổi học thể dục đầu năm, thầy giáo muốn xếp hàng $N$ bạn học sinh theo thứ tự chiều cao từ thấp đến cao để chuẩn bị cho bài tập đồng diễn.

## Nhiệm vụ
Cho danh sách chiều cao của $N$ bạn học sinh. Hãy in ra danh sách chiều cao sau khi đã xếp hàng theo thứ tự tăng dần.

## Input
- Dòng 1: Chứa số nguyên dương $N$ ($1 \\le N \\le 1000$).
- Dòng 2: Chứa $N$ số nguyên dương $A_1, A_2, \\dots, A_N$ ($1 \\le A_i \\le 10^6$).

## Output
- In ra trên một dòng gồm $N$ số nguyên biểu diễn chiều cao sau khi sắp xếp tăng dần, cách nhau bởi khoảng trắng.

## Sample 1
### Input
```text
5
1550 1420 1680 1500 1600
```
### Output
```text
1420 1500 1550 1600 1680
```

## Ràng buộc
- $100\\%$ số test có $1 \\le N \\le 1000, 1 \\le A_i \\le 10^6$.
- Thời gian: $1.0\\text{s}$, Bộ nhớ: $256\\text{MB}$.
""",
        "guide": """# Hướng Dẫn Giảng Dạy: Xếp Hàng Điểm Danh
- Sử dụng `std::sort(a.begin(), a.end())`.
- Độ phức tạp: $\\mathcal{O}(N \\log N)$.
""",
        "solution_cpp": """#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    sort(a.begin(), a.end());

    for (int i = 0; i < n; ++i) {
        cout << a[i] << (i == n - 1 ? "" : " ");
    }
    cout << "\\n";
    return 0;
}
""",
        "gen_tests": lambda: [
            {"n": 5, "arr": [1550, 1420, 1680, 1500, 1600]},
            {"n": 1, "arr": [1500]},
            {"n": 2, "arr": [1700, 1600]},
            {"n": 10, "arr": [random.randint(1000, 2000) for _ in range(10)]},
            {"n": 50, "arr": [1500] * 50},
            {"n": 100, "arr": [random.randint(1, 10**6) for _ in range(100)]},
            {"n": 200, "arr": list(range(200, 0, -1))},
            {"n": 500, "arr": [random.randint(1, 10**6) for _ in range(500)]},
            {"n": 1000, "arr": list(range(1000, 0, -1))},
            {"n": 1000, "arr": list(range(1, 1001))},
            {"n": 1000, "arr": [random.randint(1, 10**6) for _ in range(1000)]},
            {"n": 1000, "arr": [random.randint(1, 10**6) for _ in range(1000)]},
            {"n": 1000, "arr": [10**6] * 1000},
            {"n": 1000, "arr": [1] * 1000},
            {"n": 1000, "arr": [random.randint(1, 10) for _ in range(1000)]},
            {"n": 1000, "arr": [random.randint(1, 10**6) for _ in range(1000)]},
            {"n": 1000, "arr": [random.randint(1, 10**6) for _ in range(1000)]},
            {"n": 1000, "arr": [random.randint(1, 10**6) for _ in range(1000)]},
            {"n": 1000, "arr": [random.randint(1, 10**6) for _ in range(1000)]},
            {"n": 1000, "arr": [random.randint(1, 10**6) for _ in range(1000)]},
        ],
        "format_inp": lambda t: f"{t['n']}\n" + " ".join(map(str, t['arr'])) + "\n"
    },

    # 2. IKH-0102
    {
        "id": "IKH-0102",
        "slug": "cpp1_01_khoang_cach_nho_nhat",
        "title": "Khoảng Cách Nhỏ Nhất",
        "statement": """# Khoảng Cách Nhỏ Nhất

## Bối cảnh
Cho tập hợp gồm $N$ số nguyên. Hãy tìm khoảng cách nhỏ nhất giữa hai số bất kỳ trong tập hợp đó.

## Input
- Dòng 1: Số nguyên dương $N$ ($2 \\le N \\le 10^5$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \\dots, A_N$ ($1 \\le A_i \\le 10^9$).

## Output
- In ra khoảng cách nhỏ nhất giữa hai phần tử bất kỳ.

## Sample 1
### Input
```text
5
8 3 14 6 10
```
### Output
```text
2
```

## Ràng buộc
- $40\\%$ số test có $N \\le 1000$.
- $60\\%$ số test có $N \\le 10^5$.
- Thời gian: $1.0\\text{s}$, Bộ nhớ: $256\\text{MB}$.
""",
        "guide": """# Hướng Dẫn Giảng Dạy: Khoảng Cách Nhỏ Nhất
- Sắp xếp tăng dần $\\mathcal{O}(N \\log N)$, sau đó duyệt qua $N-1$ cặp kề nhau: $\\min(A_{i+1} - A_i)$.
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

    long long ans = a[1] - a[0];
    for (int i = 1; i < n - 1; ++i) {
        ans = min(ans, a[i + 1] - a[i]);
    }

    cout << ans << "\\n";
    return 0;
}
""",
        "gen_tests": lambda: [
            {"n": 5, "arr": [8, 3, 14, 6, 10]},
            {"n": 2, "arr": [10, 20]},
            {"n": 2, "arr": [10**9, 1]},
            {"n": 3, "arr": [5, 5, 10]},
            {"n": 10, "arr": [random.randint(1, 100) for _ in range(10)]},
            {"n": 100, "arr": [random.randint(1, 10**9) for _ in range(100)]},
            {"n": 500, "arr": [i * 7 for i in range(500)]},
            {"n": 1000, "arr": [random.randint(1, 10**9) for _ in range(1000)]},
            {"n": 5000, "arr": [random.randint(1, 10**9) for _ in range(5000)]},
            {"n": 20000, "arr": [random.randint(1, 10**9) for _ in range(20000)]},
            {"n": 50000, "arr": [random.randint(1, 10**9) for _ in range(50000)]},
            {"n": 100000, "arr": [i * 10 for i in range(100000)]},
            {"n": 100000, "arr": [random.randint(1, 10**9) for _ in range(100000)]},
            {"n": 100000, "arr": [random.randint(1, 10**9) for _ in range(100000)]},
            {"n": 100000, "arr": [10**9] * 100000},
            {"n": 100000, "arr": [random.randint(1, 500) for _ in range(100000)]},
            {"n": 100000, "arr": [random.randint(1, 10**9) for _ in range(100000)]},
            {"n": 100000, "arr": [random.randint(1, 10**9) for _ in range(100000)]},
            {"n": 100000, "arr": [random.randint(1, 10**9) for _ in range(100000)]},
            {"n": 100000, "arr": [random.randint(1, 10**9) for _ in range(100000)]},
        ],
        "format_inp": lambda t: f"{t['n']}\n" + " ".join(map(str, t['arr'])) + "\n"
    },

    # 3. IKH-0103
    {
        "id": "IKH-0103",
        "slug": "cpp1_01_tri_tuyet_doi",
        "title": "Sắp Xếp Theo Trị Tuyệt Đối",
        "statement": """# Sắp Xếp Theo Trị Tuyệt Đối

## Bối cảnh
Cho một dãy gồm $N$ số nguyên. Hãy sắp xếp các phần tử theo giá trị tuyệt đối tăng dần. Nếu hai phần tử có cùng giá trị tuyệt đối, số âm phải đứng trước số dương.

## Input
- Dòng 1: Số nguyên dương $N$ ($1 \\le N \\le 10^5$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \\dots, A_N$ ($-10^9 \\le A_i \\le 10^9$).

## Output
- In ra dãy số sau khi sắp xếp, cách nhau bởi một khoảng trắng.

## Sample 1
### Input
```text
5
5 -8 2 -3 8
```
### Output
```text
2 -3 5 -8 8
```

## Ràng buộc
- $40\\%$ số test có $N \\le 1000$.
- $60\\%$ số test có $N \\le 10^5$.
- Thời gian: $1.0\\text{s}$, Bộ nhớ: $256\\text{MB}$.
""",
        "guide": """# Hướng Dẫn Giảng Dạy: Sắp Xếp Theo Trị Tuyệt Đối
- Custom Comparator: So sánh `abs(u) < abs(v)`, khi bằng nhau thì `u < v`.
""",
        "solution_cpp": """#include <bits/stdc++.h>
using namespace std;

bool cmp(long long u, long long v) {
    if (abs(u) != abs(v)) return abs(u) < abs(v);
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
    cout << "\\n";
    return 0;
}
""",
        "gen_tests": lambda: [
            {"n": 5, "arr": [5, -8, 2, -3, 8]},
            {"n": 1, "arr": [-10]},
            {"n": 2, "arr": [5, -5]},
            {"n": 10, "arr": [random.randint(-100, 100) for _ in range(10)]},
            {"n": 100, "arr": [random.randint(-1000, 1000) for _ in range(100)]},
            {"n": 500, "arr": [random.randint(-10**9, 10**9) for _ in range(500)]},
            {"n": 1000, "arr": [random.randint(-10**9, 10**9) for _ in range(1000)]},
            {"n": 5000, "arr": [random.randint(-10**9, 10**9) for _ in range(5000)]},
            {"n": 20000, "arr": [random.randint(-10**9, 10**9) for _ in range(20000)]},
            {"n": 50000, "arr": [random.randint(-10**9, 10**9) for _ in range(50000)]},
            {"n": 100000, "arr": [random.randint(-10**9, 10**9) for _ in range(100000)]},
            {"n": 100000, "arr": [-10**9, 10**9] * 50000},
            {"n": 100000, "arr": [random.randint(-50, 50) for _ in range(100000)]},
            {"n": 100000, "arr": [random.randint(-10**9, 10**9) for _ in range(100000)]},
            {"n": 100000, "arr": [random.randint(-10**9, 10**9) for _ in range(100000)]},
            {"n": 100000, "arr": [random.randint(-10**9, 10**9) for _ in range(100000)]},
            {"n": 100000, "arr": [0] * 100000},
            {"n": 100000, "arr": [random.randint(-10**9, 10**9) for _ in range(100000)]},
            {"n": 100000, "arr": [random.randint(-10**9, 10**9) for _ in range(100000)]},
            {"n": 100000, "arr": [random.randint(-10**9, 10**9) for _ in range(100000)]},
        ],
        "format_inp": lambda t: f"{t['n']}\n" + " ".join(map(str, t['arr'])) + "\n"
    },

    # 4. IKH-0104
    {
        "id": "IKH-0104",
        "slug": "cpp1_01_dem_gia_tri_phan_biet",
        "title": "Đếm Giá Trị Phân Biệt",
        "statement": """# Đếm Giá Trị Phân Biệt

## Bối cảnh
Cho dãy số nguyên gồm $N$ phần tử. Hãy đếm xem trong dãy có bao nhiêu giá trị phân biệt.

## Input
- Dòng 1: Số nguyên dương $N$ ($1 \\le N \\le 2 \\cdot 10^5$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \\dots, A_N$ ($-10^9 \\le A_i \\le 10^9$).

## Output
- In ra một số nguyên duy nhất là số lượng giá trị phân biệt.

## Sample 1
### Input
```text
6
2 3 2 1 3 5
```
### Output
```text
4
```

## Ràng buộc
- $40\\%$ số test có $N \\le 1000$.
- $60\\%$ số test có $N \\le 2 \\cdot 10^5$.
- Thời gian: $1.0\\text{s}$, Bộ nhớ: $256\\text{MB}$.
""",
        "guide": """# Hướng Dẫn Giảng Dạy: Đếm Giá Trị Phân Biệt
- Sắp xếp tăng dần $\\mathcal{O}(N \\log N)$.
- Đếm số lần $A_i \\neq A_{i-1}$ cộng thêm 1.
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

    int cnt = 1;
    for (int i = 1; i < n; ++i) {
        if (a[i] != a[i - 1]) ++cnt;
    }

    cout << cnt << "\\n";
    return 0;
}
""",
        "gen_tests": lambda: [
            {"n": 6, "arr": [2, 3, 2, 1, 3, 5]},
            {"n": 1, "arr": [100]},
            {"n": 5, "arr": [1, 1, 1, 1, 1]},
            {"n": 20, "arr": [random.randint(-10, 10) for _ in range(20)]},
            {"n": 100, "arr": [random.randint(-1000, 1000) for _ in range(100)]},
            {"n": 500, "arr": [random.randint(-10**9, 10**9) for _ in range(500)]},
            {"n": 1000, "arr": [random.randint(1, 50) for _ in range(1000)]},
            {"n": 5000, "arr": [random.randint(-10**9, 10**9) for _ in range(5000)]},
            {"n": 20000, "arr": [random.randint(-10**9, 10**9) for _ in range(20000)]},
            {"n": 50000, "arr": [random.randint(-10**9, 10**9) for _ in range(50000)]},
            {"n": 100000, "arr": [random.randint(1, 100) for _ in range(100000)]},
            {"n": 100000, "arr": list(range(-50000, 50000))},
            {"n": 200000, "arr": [random.randint(-10**9, 10**9) for _ in range(200000)]},
            {"n": 200000, "arr": [7] * 200000},
            {"n": 200000, "arr": [random.randint(1, 10) for _ in range(200000)]},
            {"n": 200000, "arr": [random.randint(-10**9, 10**9) for _ in range(200000)]},
            {"n": 200000, "arr": [random.randint(-10**9, 10**9) for _ in range(200000)]},
            {"n": 200000, "arr": [random.randint(-10**9, 10**9) for _ in range(200000)]},
            {"n": 200000, "arr": [random.randint(-10**9, 10**9) for _ in range(200000)]},
            {"n": 200000, "arr": [random.randint(-10**9, 10**9) for _ in range(200000)]},
        ],
        "format_inp": lambda t: f"{t['n']}\n" + " ".join(map(str, t['arr'])) + "\n"
    },

    # 5. IKH-0105
    {
        "id": "IKH-0105",
        "slug": "cpp1_01_hai_tram_kiem_soat",
        "title": "Hai Trạm Kiểm Soát Gần Nhau Nhất",
        "statement": """# Hai Trạm Kiểm Soát Gần Nhau Nhất

## Bối cảnh
Trên một tuyến quốc lộ thẳng tắp, có $N$ trạm kiểm soát tự động tại tọa độ $X_1, X_2, \\dots, X_N$ ($0 \\le X_i \\le 10^{12}$). Hãy tìm khoảng cách ngắn nhất giữa hai trạm bất kỳ.

## Input
- Dòng 1: Số nguyên dương $N$ ($2 \\le N \\le 10^5$).
- Dòng 2: $N$ số nguyên không âm $X_1, X_2, \\dots, X_N$ ($0 \\le X_i \\le 10^{12}$).

## Output
- In ra khoảng cách ngắn nhất giữa hai trạm.

## Sample 1
### Input
```text
6
1500 300 2800 800 1200 3150
```
### Output
```text
300
```

## Ràng buộc
- $40\\%$ số test có $N \\le 1000$.
- $60\\%$ số test có $N \\le 10^5, X_i \\le 10^{12}$.
- Thời gian: $1.0\\text{s}$, Bộ nhớ: $256\\text{MB}$.
""",
        "guide": """# Hướng Dẫn Giảng Dạy: Hai Trạm Kiểm Soát
- Dùng kiểu `long long` cho tọa độ $10^{12}$. Sắp xếp và xét hiệu cặp kề.
""",
        "solution_cpp": """#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> x(n);
    for (int i = 0; i < n; ++i) cin >> x[i];

    sort(x.begin(), x.end());

    long long min_dist = x[1] - x[0];
    for (int i = 1; i < n - 1; ++i) {
        min_dist = min(min_dist, x[i + 1] - x[i]);
    }

    cout << min_dist << "\\n";
    return 0;
}
""",
        "gen_tests": lambda: [
            {"n": 6, "arr": [1500, 300, 2800, 800, 1200, 3150]},
            {"n": 2, "arr": [0, 10**12]},
            {"n": 2, "arr": [10**12, 10**12]},
            {"n": 5, "arr": [100, 200, 300, 400, 500]},
            {"n": 20, "arr": [random.randint(0, 10**6) for _ in range(20)]},
            {"n": 100, "arr": [random.randint(0, 10**12) for _ in range(100)]},
            {"n": 500, "arr": [random.randint(0, 10**12) for _ in range(500)]},
            {"n": 1000, "arr": [random.randint(0, 10**12) for _ in range(1000)]},
            {"n": 5000, "arr": [random.randint(0, 10**12) for _ in range(5000)]},
            {"n": 20000, "arr": [random.randint(0, 10**12) for _ in range(20000)]},
            {"n": 50000, "arr": [random.randint(0, 10**12) for _ in range(50000)]},
            {"n": 100000, "arr": [i * 10**6 for i in range(100000)]},
            {"n": 100000, "arr": [random.randint(0, 10**12) for _ in range(100000)]},
            {"n": 100000, "arr": [random.randint(0, 10**12) for _ in range(100000)]},
            {"n": 100000, "arr": [10**12] * 100000},
            {"n": 100000, "arr": [random.randint(0, 10**5) for _ in range(100000)]},
            {"n": 100000, "arr": [random.randint(0, 10**12) for _ in range(100000)]},
            {"n": 100000, "arr": [random.randint(0, 10**12) for _ in range(100000)]},
            {"n": 100000, "arr": [random.randint(0, 10**12) for _ in range(100000)]},
            {"n": 100000, "arr": [random.randint(0, 10**12) for _ in range(100000)]},
        ],
        "format_inp": lambda t: f"{t['n']}\n" + " ".join(map(str, t['arr'])) + "\n"
    },

    # 6. IKH-0106
    {
        "id": "IKH-0106",
        "slug": "cpp1_01_khoang_trong_lon_nhat",
        "title": "Khoảng Trống Lớn Nhất Trên Trục Tọa Độ",
        "statement": """# Khoảng Trống Lớn Nhất Trên Trục Tọa Độ

## Bối cảnh
Cho $N$ chướng ngại vật tại các vị trí $A_1, A_2, \\dots, A_N$ ($-10^{18} \\le A_i \\le 10^{18}$). Hãy tìm khoảng cách lớn nhất giữa hai chướng ngại vật liên tiếp sau khi sắp xếp.

## Input
- Dòng 1: Số nguyên dương $N$ ($2 \\le N \\le 10^5$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \\dots, A_N$ ($-10^{18} \\le A_i \\le 10^{18}$).

## Output
- In ra khoảng cách lớn nhất giữa hai chướng ngại vật liên tiếp.

## Sample 1
### Input
```text
5
10 3 25 8 12
```
### Output
```text
13
```

## Ràng buộc
- $40\\%$ số test có $N \\le 1000, \\vert A_i \\vert \\le 10^9$.
- $60\\%$ số test có $N \\le 10^5, \\vert A_i \\vert \\le 10^{18}$.
- Thời gian: $1.0\\text{s}$, Bộ nhớ: $256\\text{MB}$.
""",
        "guide": """# Hướng Dẫn Giảng Dạy: Khoảng Trống Lớn Nhất
- Sắp xếp tăng dần $\\mathcal{O}(N \\log N)$, lấy $\\max(A_{i+1} - A_i)$ với kiểu dữ liệu `long long`.
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

    long long max_gap = 0;
    for (int i = 0; i < n - 1; ++i) {
        max_gap = max(max_gap, a[i + 1] - a[i]);
    }

    cout << max_gap << "\\n";
    return 0;
}
""",
        "gen_tests": lambda: [
            {"n": 5, "arr": [10, 3, 25, 8, 12]},
            {"n": 2, "arr": [-10**18, 10**18]},
            {"n": 2, "arr": [5, 5]},
            {"n": 10, "arr": [random.randint(-100, 100) for _ in range(10)]},
            {"n": 100, "arr": [random.randint(-10**9, 10**9) for _ in range(100)]},
            {"n": 500, "arr": [random.randint(-10**18, 10**18) for _ in range(500)]},
            {"n": 1000, "arr": [random.randint(-10**9, 10**9) for _ in range(1000)]},
            {"n": 5000, "arr": [random.randint(-10**18, 10**18) for _ in range(5000)]},
            {"n": 20000, "arr": [random.randint(-10**18, 10**18) for _ in range(20000)]},
            {"n": 50000, "arr": [random.randint(-10**18, 10**18) for _ in range(50000)]},
            {"n": 100000, "arr": [random.randint(-10**18, 10**18) for _ in range(100000)]},
            {"n": 100000, "arr": [random.randint(-10**18, 10**18) for _ in range(100000)]},
            {"n": 100000, "arr": [random.randint(-10**18, 10**18) for _ in range(100000)]},
            {"n": 100000, "arr": [0] * 100000},
            {"n": 100000, "arr": [random.randint(-10**9, 10**9) for _ in range(100000)]},
            {"n": 100000, "arr": [random.randint(-10**18, 10**18) for _ in range(100000)]},
            {"n": 100000, "arr": [random.randint(-10**18, 10**18) for _ in range(100000)]},
            {"n": 100000, "arr": [random.randint(-10**18, 10**18) for _ in range(100000)]},
            {"n": 100000, "arr": [random.randint(-10**18, 10**18) for _ in range(100000)]},
            {"n": 100000, "arr": [random.randint(-10**18, 10**18) for _ in range(100000)]},
        ],
        "format_inp": lambda t: f"{t['n']}\n" + " ".join(map(str, t['arr'])) + "\n"
    },

    # 7. IKH-0107
    {
        "id": "IKH-0107",
        "slug": "cpp1_01_sap_xep_tong_chu_so",
        "title": "Sắp Xếp Theo Tổng Chữ Số",
        "statement": """# Sắp Xếp Theo Tổng Chữ Số

## Bối cảnh
Cho $N$ số nguyên dương. Hãy sắp xếp dãy số theo **tổng các chữ số tăng dần**. Nếu hai số có cùng tổng chữ số, số có giá trị nhỏ hơn sẽ đứng trước.

## Input
- Dòng 1: Số nguyên dương $N$ ($1 \\le N \\le 10^5$).
- Dòng 2: $N$ số nguyên dương $A_1, A_2, \\dots, A_N$ ($1 \\le A_i \\le 10^9$).

## Output
- In ra dãy số sau khi sắp xếp, cách nhau bởi khoảng trắng.

## Sample 1
### Input
```text
5
13 20 4 103 11
```
### Output
```text
11 20 4 13 103
```

## Ràng buộc
- $100\\%$ số test có $1 \\le N \\le 10^5, 1 \\le A_i \\le 10^9$.
- Thời gian: $1.0\\text{s}$, Bộ nhớ: $256\\text{MB}$.
""",
        "guide": """# Hướng Dẫn Giảng Dạy: Sắp Xếp Theo Tổng Chữ Số
- Viết hàm `sum_digits(x)` tính tổng chữ số.
- Comparator so sánh tổng chữ số, nếu hòa thì so sánh giá trị số.
""",
        "solution_cpp": """#include <bits/stdc++.h>
using namespace std;

long long sum_digits(long long x) {
    long long s = 0;
    while (x > 0) {
        s += x % 10;
        x /= 10;
    }
    return s;
}

bool cmp(long long a, long long b) {
    long long sa = sum_digits(a);
    long long sb = sum_digits(b);
    if (sa != sb) return sa < sb;
    return a < b;
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
    cout << "\\n";
    return 0;
}
""",
        "gen_tests": lambda: [
            {"n": 5, "arr": [13, 20, 4, 103, 11]},
            {"n": 1, "arr": [999999999]},
            {"n": 10, "arr": [random.randint(1, 1000) for _ in range(10)]},
            {"n": 100, "arr": [random.randint(1, 10**9) for _ in range(100)]},
            {"n": 500, "arr": [random.randint(1, 10**9) for _ in range(500)]},
            {"n": 1000, "arr": [random.randint(1, 10**9) for _ in range(1000)]},
            {"n": 5000, "arr": [random.randint(1, 10**9) for _ in range(5000)]},
            {"n": 20000, "arr": [random.randint(1, 10**9) for _ in range(20000)]},
            {"n": 50000, "arr": [random.randint(1, 10**9) for _ in range(50000)]},
            {"n": 100000, "arr": [random.randint(1, 10**9) for _ in range(100000)]},
            {"n": 100000, "arr": [10**9] * 100000},
            {"n": 100000, "arr": [random.randint(1, 9) for _ in range(100000)]},
            {"n": 100000, "arr": [random.randint(1, 10**9) for _ in range(100000)]},
            {"n": 100000, "arr": [random.randint(1, 10**9) for _ in range(100000)]},
            {"n": 100000, "arr": [random.randint(1, 10**9) for _ in range(100000)]},
            {"n": 100000, "arr": [random.randint(1, 10**9) for _ in range(100000)]},
            {"n": 100000, "arr": [random.randint(1, 10**9) for _ in range(100000)]},
            {"n": 100000, "arr": [random.randint(1, 10**9) for _ in range(100000)]},
            {"n": 100000, "arr": [random.randint(1, 10**9) for _ in range(100000)]},
            {"n": 100000, "arr": [random.randint(1, 10**9) for _ in range(100000)]},
        ],
        "format_inp": lambda t: f"{t['n']}\n" + " ".join(map(str, t['arr'])) + "\n"
    },

    # 8. IKH-0108
    {
        "id": "IKH-0108",
        "slug": "cpp1_01_gom_cum_chenh_lech_k",
        "title": "Gom Cụm Chênh Lệch Không Quá K",
        "statement": """# Gom Cụm Chênh Lệch Không Quá K

## Bối cảnh
Cho $N$ học sinh với điểm số $A_1, A_2, \\dots, A_N$. Giáo viên muốn chia các bạn học sinh thành các nhóm sao cho trong mỗi nhóm, chênh lệch điểm số giữa bạn cao nhất và bạn thấp nhất không vượt quá $K$.

## Nhiệm vụ
Hãy tìm số lượng nhóm ít nhất để phân chia toàn bộ $N$ học sinh.

## Input
- Dòng 1: Chứa 2 số nguyên dương $N$ và $K$ ($1 \\le N \\le 2 \\cdot 10^5, 0 \\le K \\le 10^9$).
- Dòng 2: $N$ số nguyên dương $A_1, A_2, \\dots, A_N$ ($1 \\le A_i \\le 10^9$).

## Output
- In ra số lượng nhóm ít nhất cần chia.

## Sample 1
### Input
```text
6 3
1 10 3 4 12 15
```
### Output
```text
3
```

## Ràng buộc
- $100\\%$ số test có $N \\le 2 \\cdot 10^5, K \\le 10^9, A_i \\le 10^9$.
- Thời gian: $1.0\\text{s}$, Bộ nhớ: $256\\text{MB}$.
""",
        "guide": """# Hướng Dẫn Giảng Dạy: Gom Cụm Điểm Số
- Sắp xếp tăng dần $\\mathcal{O}(N \\log N)$.
- Duyệt tham lam: Gán phần tử đầu nhóm là $A[start]$. Mở rộng cho đến khi $A[i] - A[start] > K$ thì tạo nhóm mới.
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

    int groups = 1;
    long long min_val = a[0];

    for (int i = 1; i < n; ++i) {
        if (a[i] - min_val > k) {
            ++groups;
            min_val = a[i];
        }
    }

    cout << groups << "\\n";
    return 0;
}
""",
        "gen_tests": lambda: [
            {"n": 6, "k": 3, "arr": [1, 10, 3, 4, 12, 15]},
            {"n": 1, "k": 10, "arr": [5]},
            {"n": 5, "k": 0, "arr": [1, 2, 3, 4, 5]},
            {"n": 5, "k": 100, "arr": [1, 2, 3, 4, 5]},
            {"n": 10, "k": 5, "arr": [random.randint(1, 30) for _ in range(10)]},
            {"n": 100, "k": 20, "arr": [random.randint(1, 1000) for _ in range(100)]},
            {"n": 500, "k": 50, "arr": [random.randint(1, 10**6) for _ in range(500)]},
            {"n": 1000, "k": 1000, "arr": [random.randint(1, 10**9) for _ in range(1000)]},
            {"n": 5000, "k": 50000, "arr": [random.randint(1, 10**9) for _ in range(5000)]},
            {"n": 20000, "k": 10**6, "arr": [random.randint(1, 10**9) for _ in range(20000)]},
            {"n": 50000, "k": 10**7, "arr": [random.randint(1, 10**9) for _ in range(50000)]},
            {"n": 100000, "k": 10**8, "arr": [random.randint(1, 10**9) for _ in range(100000)]},
            {"n": 200000, "k": 10**9, "arr": [random.randint(1, 10**9) for _ in range(200000)]},
            {"n": 200000, "k": 0, "arr": [random.randint(1, 10) for _ in range(200000)]},
            {"n": 200000, "k": 10, "arr": [1] * 200000},
            {"n": 200000, "k": 100, "arr": [random.randint(1, 10**9) for _ in range(200000)]},
            {"n": 200000, "k": 1000, "arr": [random.randint(1, 10**9) for _ in range(200000)]},
            {"n": 200000, "k": 50000, "arr": [random.randint(1, 10**9) for _ in range(200000)]},
            {"n": 200000, "k": 123456, "arr": [random.randint(1, 10**9) for _ in range(200000)]},
            {"n": 200000, "k": 987654, "arr": [random.randint(1, 10**9) for _ in range(200000)]},
        ],
        "format_inp": lambda t: f"{t['n']} {t['k']}\n" + " ".join(map(str, t['arr'])) + "\n"
    },

    # 9. IKH-0109
    {
        "id": "IKH-0109",
        "slug": "cpp1_01_phan_tu_xuat_hien_nhieu_nhat",
        "title": "Tìm Phần Tử Xuất Hiện Nhiều Nhất",
        "statement": """# Tìm Phần Tử Xuất Hiện Nhiều Nhất

## Bối cảnh
Cho một dãy gồm $N$ số nguyên. Hãy tìm phần tử có số lần xuất hiện nhiều nhất trong dãy. Nếu có nhiều phần tử có cùng số lần xuất hiện cực đại, in ra phần tử có giá trị nhỏ nhất.

## Input
- Dòng 1: Số nguyên dương $N$ ($1 \\le N \\le 2 \\cdot 10^5$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \\dots, A_N$ ($-10^9 \\le A_i \\le 10^9$).

## Output
- In ra hai số nguyên: giá trị của phần tử xuất hiện nhiều nhất và số lần xuất hiện của nó.

## Sample 1
### Input
```text
7
3 5 2 3 5 3 2
```
### Output
```text
3 3
```

## Ràng buộc
- $100\\%$ số test có $N \\le 2 \\cdot 10^5, \\vert A_i \\vert \\le 10^9$.
- Thời gian: $1.0\\text{s}$, Bộ nhớ: $256\\text{MB}$.
""",
        "guide": """# Hướng Dẫn Giảng Dạy: Phần Tử Xuất Hiện Nhiều Nhất
- Sắp xếp tăng dần $\\mathcal{O}(N \\log N)$.
- Duyệt qua từng khối các phần tử bằng nhau liên tiếp để đếm tần suất.
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

    long long best_val = a[0];
    int max_freq = 1;

    long long cur_val = a[0];
    int cur_freq = 1;

    for (int i = 1; i < n; ++i) {
        if (a[i] == cur_val) {
            ++cur_freq;
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

    cout << best_val << " " << max_freq << "\\n";
    return 0;
}
""",
        "gen_tests": lambda: [
            {"n": 7, "arr": [3, 5, 2, 3, 5, 3, 2]},
            {"n": 1, "arr": [100]},
            {"n": 4, "arr": [1, 2, 3, 4]},
            {"n": 5, "arr": [2, 2, 1, 1, 3]},
            {"n": 10, "arr": [random.randint(1, 5) for _ in range(10)]},
            {"n": 100, "arr": [random.randint(1, 20) for _ in range(100)]},
            {"n": 500, "arr": [random.randint(-50, 50) for _ in range(500)]},
            {"n": 1000, "arr": [random.randint(-100, 100) for _ in range(1000)]},
            {"n": 5000, "arr": [random.randint(1, 1000) for _ in range(5000)]},
            {"n": 20000, "arr": [random.randint(-10**9, 10**9) for _ in range(20000)]},
            {"n": 50000, "arr": [random.randint(-10**9, 10**9) for _ in range(50000)]},
            {"n": 100000, "arr": [5] * 100000},
            {"n": 200000, "arr": [random.randint(1, 1000) for _ in range(200000)]},
            {"n": 200000, "arr": [random.randint(1, 10) for _ in range(200000)]},
            {"n": 200000, "arr": [random.randint(-10**9, 10**9) for _ in range(200000)]},
            {"n": 200000, "arr": [random.randint(-10**9, 10**9) for _ in range(200000)]},
            {"n": 200000, "arr": [random.randint(-10**9, 10**9) for _ in range(200000)]},
            {"n": 200000, "arr": [random.randint(-10**9, 10**9) for _ in range(200000)]},
            {"n": 200000, "arr": [random.randint(-10**9, 10**9) for _ in range(200000)]},
            {"n": 200000, "arr": [random.randint(-10**9, 10**9) for _ in range(200000)]},
        ],
        "format_inp": lambda t: f"{t['n']}\n" + " ".join(map(str, t['arr'])) + "\n"
    },

    # 10. IKH-0110
    {
        "id": "IKH-0110",
        "slug": "cpp1_01_sap_xep_luu_vi_tri",
        "title": "Sắp Xếp Lưu Vị Trí Ban Đầu",
        "statement": """# Sắp Xếp Lưu Vị Trí Ban Đầu

## Bối cảnh
Cho một dãy gồm $N$ số nguyên $A_1, A_2, \\dots, A_N$. Hãy sắp xếp các phần tử theo thứ tự tăng dần, đồng thời in ra vị trí ban đầu (chỉ số 1-indexed) của mỗi phần tử trong mảng gốc. Nếu hai phần tử có cùng giá trị, phần tử xuất hiện trước trong mảng gốc sẽ đứng trước.

## Input
- Dòng 1: Số nguyên dương $N$ ($1 \\le N \\le 10^5$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \\dots, A_N$ ($-10^9 \\le A_i \\le 10^9$).

## Output
- In ra $N$ dòng, mỗi dòng gồm 2 số nguyên biểu diễn giá trị phần tử và chỉ số ban đầu của nó.

## Sample 1
### Input
```text
5
40 10 20 10 30
```
### Output
```text
10 2
10 4
20 3
30 5
40 1
```

## Ràng buộc
- $100\\%$ số test có $N \\le 10^5, \\vert A_i \\vert \\le 10^9$.
- Thời gian: $1.0\\text{s}$, Bộ nhớ: $256\\text{MB}$.
""",
        "guide": """# Hướng Dẫn Giảng Dạy: Lưu Vị Trí Ban Đầu
- Sử dụng `vector<pair<long long, int>>` lưu `{giá_trị, chỉ_số_gốc}`.
- Sắp xếp tăng dần.
""",
        "solution_cpp": """#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<pair<long long, int>> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i].first;
        a[i].second = i + 1;
    }

    sort(a.begin(), a.end());

    for (int i = 0; i < n; ++i) {
        cout << a[i].first << " " << a[i].second << "\\n";
    }
    return 0;
}
""",
        "gen_tests": lambda: [
            {"n": 5, "arr": [40, 10, 20, 10, 30]},
            {"n": 1, "arr": [5]},
            {"n": 3, "arr": [10, 10, 10]},
            {"n": 10, "arr": [random.randint(1, 20) for _ in range(10)]},
            {"n": 100, "arr": [random.randint(-1000, 1000) for _ in range(100)]},
            {"n": 500, "arr": [random.randint(-10**9, 10**9) for _ in range(500)]},
            {"n": 1000, "arr": [random.randint(-10**9, 10**9) for _ in range(1000)]},
            {"n": 5000, "arr": [random.randint(-10**9, 10**9) for _ in range(5000)]},
            {"n": 20000, "arr": [random.randint(-10**9, 10**9) for _ in range(20000)]},
            {"n": 50000, "arr": [random.randint(-10**9, 10**9) for _ in range(50000)]},
            {"n": 100000, "arr": list(range(100000, 0, -1))},
            {"n": 100000, "arr": [random.randint(-10**9, 10**9) for _ in range(100000)]},
            {"n": 100000, "arr": [random.randint(-10**9, 10**9) for _ in range(100000)]},
            {"n": 100000, "arr": [random.randint(-10**9, 10**9) for _ in range(100000)]},
            {"n": 100000, "arr": [0] * 100000},
            {"n": 100000, "arr": [random.randint(1, 5) for _ in range(100000)]},
            {"n": 100000, "arr": [random.randint(-10**9, 10**9) for _ in range(100000)]},
            {"n": 100000, "arr": [random.randint(-10**9, 10**9) for _ in range(100000)]},
            {"n": 100000, "arr": [random.randint(-10**9, 10**9) for _ in range(100000)]},
            {"n": 100000, "arr": [random.randint(-10**9, 10**9) for _ in range(100000)]},
        ],
        "format_inp": lambda t: f"{t['n']}\n" + " ".join(map(str, t['arr'])) + "\n"
    },

    # 11. IKH-0111
    {
        "id": "IKH-0111",
        "slug": "cpp1_01_ghep_so_lon_nhat",
        "title": "Ghép Chuỗi Tạo Số Lớn Nhất",
        "statement": """# Ghép Chuỗi Tạo Số Lớn Nhất

## Bối cảnh
Cho $N$ số nguyên không âm biểu diễn dưới dạng chuỗi ký tự. Hãy ghép toàn bộ $N$ số này lại với nhau theo thứ tự nào đó để tạo thành số có giá trị lớn nhất.

## Input
- Dòng 1: Số nguyên dương $N$ ($1 \\le N \\le 10^4$).
- Dòng 2: $N$ chuỗi số $S_1, S_2, \\dots, S_N$ (độ dài mỗi chuỗi không quá 10 ký tự).

## Output
- In ra chuỗi số lớn nhất tạo được. Nếu kết quả gồm toàn số 0, in ra `0`.

## Sample 1
### Input
```text
4
3 30 34 5
```
### Output
```text
534330
```

## Ràng buộc
- $100\\%$ số test có $N \\le 10^4$.
- Thời gian: $1.0\\text{s}$, Bộ nhớ: $256\\text{MB}$.
""",
        "guide": """# Hướng Dẫn Giảng Dạy: Ghép Số Lớn Nhất
- Comparator: `bool cmp(string a, string b) { return a + b > b + a; }`.
- Xử lý biên: Nếu phần tử đầu tiên là `"0"`, in ra `"0"`.
""",
        "solution_cpp": """#include <bits/stdc++.h>
using namespace std;

bool cmp(const string &a, const string &b) {
    return a + b > b + a;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<string> s(n);
    for (int i = 0; i < n; ++i) cin >> s[i];

    sort(s.begin(), s.end(), cmp);

    if (s[0] == "0") {
        cout << 0 << "\\n";
        return 0;
    }

    for (int i = 0; i < n; ++i) {
        cout << s[i];
    }
    cout << "\\n";
    return 0;
}
""",
        "gen_tests": lambda: [
            {"n": 4, "arr": ["3", "30", "34", "5"]},
            {"n": 2, "arr": ["0", "0"]},
            {"n": 5, "arr": ["9", "99", "999", "9999", "8"]},
            {"n": 10, "arr": [str(random.randint(1, 999)) for _ in range(10)]},
            {"n": 50, "arr": [str(random.randint(0, 10000)) for _ in range(50)]},
            {"n": 100, "arr": [str(random.randint(0, 10**9)) for _ in range(100)]},
            {"n": 500, "arr": [str(random.randint(1, 10**9)) for _ in range(500)]},
            {"n": 1000, "arr": [str(random.randint(1, 10**9)) for _ in range(1000)]},
            {"n": 2000, "arr": [str(random.randint(0, 10**9)) for _ in range(2000)]},
            {"n": 5000, "arr": [str(random.randint(1, 10**9)) for _ in range(5000)]},
            {"n": 10000, "arr": ["0"] * 10000},
            {"n": 10000, "arr": ["9"] * 10000},
            {"n": 10000, "arr": [str(random.randint(1, 9)) for _ in range(10000)]},
            {"n": 10000, "arr": [str(random.randint(10, 99)) for _ in range(10000)]},
            {"n": 10000, "arr": [str(random.randint(100, 999)) for _ in range(10000)]},
            {"n": 10000, "arr": [str(random.randint(1, 10**9)) for _ in range(10000)]},
            {"n": 10000, "arr": [str(random.randint(1, 10**9)) for _ in range(10000)]},
            {"n": 10000, "arr": [str(random.randint(1, 10**9)) for _ in range(10000)]},
            {"n": 10000, "arr": [str(random.randint(1, 10**9)) for _ in range(10000)]},
            {"n": 10000, "arr": [str(random.randint(1, 10**9)) for _ in range(10000)]},
        ],
        "format_inp": lambda t: f"{t['n']}\n" + " ".join(t['arr']) + "\n"
    },

    # 12. IKH-0112
    {
        "id": "IKH-0112",
        "slug": "cpp1_01_bang_diem_hoc_sinh",
        "title": "Bảng Điểm Học Sinh Đa Trường",
        "statement": """# Bảng Điểm Học Sinh Đa Trường

## Bối cảnh
Cho danh sách $N$ học sinh tham gia kỳ thi. Mỗi học sinh có mã số $ID$, điểm thi Toán và điểm thi Tin. Hãy sắp xếp danh sách học sinh theo các quy tắc sau:
1. Tổng điểm (Toán + Tin) giảm dần.
2. Nếu bằng tổng điểm, điểm Tin học cao hơn đứng trước.
3. Nếu vẫn bằng nhau, mã số $ID$ nhỏ hơn đứng trước.

## Input
- Dòng 1: Số nguyên dương $N$ ($1 \\le N \\le 10^5$).
- $N$ dòng tiếp theo: Mỗi dòng gồm 3 số nguyên $ID, Math, Info$ ($1 \\le ID \\le 10^9, 0 \\le Math, Info \\le 100$).

## Output
- In ra danh sách học sinh sau khi sắp xếp, mỗi học sinh gồm 3 số $ID, Math, Info$ trên một dòng.

## Sample 1
### Input
```text
3
101 8 9
102 9 8
103 10 10
```
### Output
```text
103 10 10
101 8 9
102 9 8
```

## Ràng buộc
- $100\\%$ số test có $N \\le 10^5$.
- Thời gian: $1.0\\text{s}$, Bộ nhớ: $256\\text{MB}$.
""",
        "guide": """# Hướng Dẫn Giảng Dạy: Bảng Điểm Học Sinh
- Struct/Vector đa trường. Comparator so sánh 3 cấp độ.
""",
        "solution_cpp": """#include <bits/stdc++.h>
using namespace std;

struct Student {
    long long id;
    int math, info;
};

bool cmp(const Student &a, const Student &b) {
    int total_a = a.math + a.info;
    int total_b = b.math + b.info;
    if (total_a != total_b) return total_a > total_b;
    if (a.info != b.info) return a.info > b.info;
    return a.id < b.id;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<Student> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i].id >> a[i].math >> a[i].info;
    }

    sort(a.begin(), a.end(), cmp);

    for (int i = 0; i < n; ++i) {
        cout << a[i].id << " " << a[i].math << " " << a[i].info << "\\n";
    }
    return 0;
}
""",
        "gen_tests": lambda: [
            {"n": 3, "arr": [[101, 8, 9], [102, 9, 8], [103, 10, 10]]},
            {"n": 1, "arr": [[1, 10, 10]]},
            {"n": 5, "arr": [[i, random.randint(0, 100), random.randint(0, 100)] for i in range(1, 6)]},
            {"n": 10, "arr": [[i, 50, 50] for i in range(10, 0, -1)]},
            {"n": 100, "arr": [[random.randint(1, 10**6), random.randint(0, 100), random.randint(0, 100)] for _ in range(100)]},
            {"n": 500, "arr": [[random.randint(1, 10**9), random.randint(0, 100), random.randint(0, 100)] for _ in range(500)]},
            {"n": 1000, "arr": [[random.randint(1, 10**9), random.randint(0, 100), random.randint(0, 100)] for _ in range(1000)]},
            {"n": 5000, "arr": [[random.randint(1, 10**9), random.randint(0, 100), random.randint(0, 100)] for _ in range(5000)]},
            {"n": 20000, "arr": [[random.randint(1, 10**9), random.randint(0, 100), random.randint(0, 100)] for _ in range(20000)]},
            {"n": 50000, "arr": [[random.randint(1, 10**9), random.randint(0, 100), random.randint(0, 100)] for _ in range(50000)]},
            {"n": 100000, "arr": [[i, 100, 100] for i in range(1, 100001)]},
            {"n": 100000, "arr": [[random.randint(1, 10**9), random.randint(0, 100), random.randint(0, 100)] for _ in range(100000)]},
            {"n": 100000, "arr": [[random.randint(1, 10**9), random.randint(0, 100), random.randint(0, 100)] for _ in range(100000)]},
            {"n": 100000, "arr": [[random.randint(1, 10**9), random.randint(0, 100), random.randint(0, 100)] for _ in range(100000)]},
            {"n": 100000, "arr": [[random.randint(1, 10**9), random.randint(0, 100), random.randint(0, 100)] for _ in range(100000)]},
            {"n": 100000, "arr": [[random.randint(1, 10**9), random.randint(0, 100), random.randint(0, 100)] for _ in range(100000)]},
            {"n": 100000, "arr": [[random.randint(1, 10**9), random.randint(0, 100), random.randint(0, 100)] for _ in range(100000)]},
            {"n": 100000, "arr": [[random.randint(1, 10**9), random.randint(0, 100), random.randint(0, 100)] for _ in range(100000)]},
            {"n": 100000, "arr": [[random.randint(1, 10**9), random.randint(0, 100), random.randint(0, 100)] for _ in range(100000)]},
            {"n": 100000, "arr": [[random.randint(1, 10**9), random.randint(0, 100), random.randint(0, 100)] for _ in range(100000)]},
        ],
        "format_inp": lambda t: f"{t['n']}\n" + "\n".join(f"{x[0]} {x[1]} {x[2]}" for x in t['arr']) + "\n"
    },

    # 13. IKH-0113
    {
        "id": "IKH-0113",
        "slug": "cpp1_01_bang_xep_hang_the_thao",
        "title": "Bảng Xếp Hạng Giải Đấu Thể Thao",
        "statement": """# Bảng Xếp Hạng Giải Đấu Thể Thao

## Bối cảnh
Cho kết quả của $N$ đội bóng gồm: Mã đội $ID$, Điểm số $Points$, Hiệu số bàn thắng $GoalDiff$, Số bàn thắng ghi được $Goals$. Hãy xếp hạng các đội theo thứ tự:
1. Điểm số giảm dần.
2. Hiệu số bàn thắng giảm dần.
3. Số bàn thắng ghi được giảm dần.
4. Mã đội $ID$ tăng dần.

## Input
- Dòng 1: Số nguyên dương $N$ ($1 \\le N \\le 10^5$).
- $N$ dòng tiếp theo: Mỗi dòng gồm 4 số nguyên $ID, Points, GoalDiff, Goals$.

## Output
- In ra danh sách mã đội $ID$ sau khi đã sắp xếp thứ hạng, cách nhau bởi khoảng trắng.

## Sample 1
### Input
```text
3
1 10 5 12
2 10 5 15
3 12 2 8
```
### Output
```text
3 2 1
```

## Ràng buộc
- $100\\%$ số test có $N \\le 10^5$.
- Thời gian: $1.0\\text{s}$, Bộ nhớ: $256\\text{MB}$.
""",
        "guide": """# Hướng Dẫn Giảng Dạy: Bảng Xếp Hạng Thể Thao
- Sắp xếp 4 tiêu chí rõ ràng, tránh sai sót toán tử so sánh.
""",
        "solution_cpp": """#include <bits/stdc++.h>
using namespace std;

struct Team {
    long long id;
    int pts, diff, goals;
};

bool cmp(const Team &a, const Team &b) {
    if (a.pts != b.pts) return a.pts > b.pts;
    if (a.diff != b.diff) return a.diff > b.diff;
    if (a.goals != b.goals) return a.goals > b.goals;
    return a.id < b.id;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<Team> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i].id >> a[i].pts >> a[i].diff >> a[i].goals;
    }

    sort(a.begin(), a.end(), cmp);

    for (int i = 0; i < n; ++i) {
        cout << a[i].id << (i == n - 1 ? "" : " ");
    }
    cout << "\\n";
    return 0;
}
""",
        "gen_tests": lambda: [
            {"n": 3, "arr": [[1, 10, 5, 12], [2, 10, 5, 15], [3, 12, 2, 8]]},
            {"n": 1, "arr": [[10, 50, 20, 30]]},
            {"n": 10, "arr": [[i, random.randint(0, 30), random.randint(-20, 20), random.randint(0, 40)] for i in range(1, 11)]},
            {"n": 100, "arr": [[i, random.randint(0, 100), random.randint(-50, 50), random.randint(0, 100)] for i in range(1, 101)]},
            {"n": 1000, "arr": [[i, random.randint(0, 100), random.randint(-50, 50), random.randint(0, 100)] for i in range(1, 1001)]},
            {"n": 5000, "arr": [[i, random.randint(0, 100), random.randint(-50, 50), random.randint(0, 100)] for i in range(1, 5001)]},
            {"n": 20000, "arr": [[i, random.randint(0, 100), random.randint(-50, 50), random.randint(0, 100)] for i in range(1, 20001)]},
            {"n": 50000, "arr": [[i, random.randint(0, 100), random.randint(-50, 50), random.randint(0, 100)] for i in range(1, 50001)]},
            {"n": 100000, "arr": [[i, 50, 10, 20] for i in range(100000, 0, -1)]},
            {"n": 100000, "arr": [[i, random.randint(0, 100), random.randint(-50, 50), random.randint(0, 100)] for i in range(1, 100001)]},
            {"n": 100000, "arr": [[i, random.randint(0, 100), random.randint(-50, 50), random.randint(0, 100)] for i in range(1, 100001)]},
            {"n": 100000, "arr": [[i, random.randint(0, 100), random.randint(-50, 50), random.randint(0, 100)] for i in range(1, 100001)]},
            {"n": 100000, "arr": [[i, random.randint(0, 100), random.randint(-50, 50), random.randint(0, 100)] for i in range(1, 100001)]},
            {"n": 100000, "arr": [[i, random.randint(0, 100), random.randint(-50, 50), random.randint(0, 100)] for i in range(1, 100001)]},
            {"n": 100000, "arr": [[i, random.randint(0, 100), random.randint(-50, 50), random.randint(0, 100)] for i in range(1, 100001)]},
            {"n": 100000, "arr": [[i, random.randint(0, 100), random.randint(-50, 50), random.randint(0, 100)] for i in range(1, 100001)]},
            {"n": 100000, "arr": [[i, random.randint(0, 100), random.randint(-50, 50), random.randint(0, 100)] for i in range(1, 100001)]},
            {"n": 100000, "arr": [[i, random.randint(0, 100), random.randint(-50, 50), random.randint(0, 100)] for i in range(1, 100001)]},
            {"n": 100000, "arr": [[i, random.randint(0, 100), random.randint(-50, 50), random.randint(0, 100)] for i in range(1, 100001)]},
            {"n": 100000, "arr": [[i, random.randint(0, 100), random.randint(-50, 50), random.randint(0, 100)] for i in range(1, 100001)]},
        ],
        "format_inp": lambda t: f"{t['n']}\n" + "\n".join(f"{x[0]} {x[1]} {x[2]} {x[3]}" for x in t['arr']) + "\n"
    },

    # 14. IKH-0114
    {
        "id": "IKH-0114",
        "slug": "cpp1_01_khac_phuc_strict_weak_ordering",
        "title": "Sắp Xếp Đoạn Thẳng Không Giao Lỗi",
        "statement": """# Sắp Xếp Đoạn Thẳng Không Giao Lỗi

## Bối cảnh
Cho $N$ đoạn thẳng $[L_i, R_i]$ trên trục số. Hãy sắp xếp các đoạn thẳng theo tiêu chí:
1. Tọa độ đầu mút $L_i$ tăng dần.
2. Nếu cùng $L_i$, tọa độ $R_i$ giảm dần.
3. Nếu trùng cả $L_i$ và $R_i$, giữ nguyên thứ tự ban đầu (sắp xếp ổn định).

## Input
- Dòng 1: Số nguyên dương $N$ ($1 \\le N \\le 2 \\cdot 10^5$).
- $N$ dòng tiếp theo: Mỗi dòng gồm 2 số nguyên $L_i, R_i$ ($-10^9 \\le L_i \\le R_i \\le 10^9$).

## Output
- In ra $N$ dòng, mỗi dòng gồm 2 số $L_i, R_i$ sau khi sắp xếp.

## Sample 1
### Input
```text
3
2 8
1 5
2 10
```
### Output
```text
1 5
2 10
2 8
```

## Ràng buộc
- $100\\%$ số test có $N \\le 2 \\cdot 10^5$.
- Thời gian: $1.0\\text{s}$, Bộ nhớ: $256\\text{MB}$.
""",
        "guide": """# Hướng Dẫn Giảng Dạy: Strict Weak Ordering Trên Đoạn Thẳng
- Sử dụng `std::stable_sort` kết hợp Comparator chuẩn `<` và `>`. Tuyệt đối không dùng `<=` khi so sánh hai phần tử bằng nhau.
""",
        "solution_cpp": """#include <bits/stdc++.h>
using namespace std;

struct Segment {
    long long l, r;
};

bool cmp(const Segment &a, const Segment &b) {
    if (a.l != b.l) return a.l < b.l;
    return a.r > b.r;
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

    stable_sort(a.begin(), a.end(), cmp);

    for (int i = 0; i < n; ++i) {
        cout << a[i].l << " " << a[i].r << "\\n";
    }
    return 0;
}
""",
        "gen_tests": lambda: [
            {"n": 3, "arr": [[2, 8], [1, 5], [2, 10]]},
            {"n": 1, "arr": [[0, 100]]},
            {"n": 5, "arr": [[random.randint(1, 10), random.randint(10, 20)] for _ in range(5)]},
            {"n": 10, "arr": [[5, 10] for _ in range(10)]},
            {"n": 100, "arr": [[random.randint(-1000, 1000), random.randint(1000, 2000)] for _ in range(100)]},
            {"n": 1000, "arr": [[random.randint(-10**9, 10**9), random.randint(-10**9, 10**9)] for _ in range(1000)]},
            {"n": 5000, "arr": [[random.randint(-10**9, 10**9), random.randint(-10**9, 10**9)] for _ in range(5000)]},
            {"n": 20000, "arr": [[random.randint(-10**9, 10**9), random.randint(-10**9, 10**9)] for _ in range(20000)]},
            {"n": 50000, "arr": [[random.randint(-10**9, 10**9), random.randint(-10**9, 10**9)] for _ in range(50000)]},
            {"n": 100000, "arr": [[random.randint(-10**9, 10**9), random.randint(-10**9, 10**9)] for _ in range(100000)]},
            {"n": 200000, "arr": [[1, 2] for _ in range(200000)]},
            {"n": 200000, "arr": [[random.randint(-10**9, 10**9), random.randint(-10**9, 10**9)] for _ in range(200000)]},
            {"n": 200000, "arr": [[random.randint(-10**9, 10**9), random.randint(-10**9, 10**9)] for _ in range(200000)]},
            {"n": 200000, "arr": [[random.randint(-10**9, 10**9), random.randint(-10**9, 10**9)] for _ in range(200000)]},
            {"n": 200000, "arr": [[random.randint(-10**9, 10**9), random.randint(-10**9, 10**9)] for _ in range(200000)]},
            {"n": 200000, "arr": [[random.randint(-10**9, 10**9), random.randint(-10**9, 10**9)] for _ in range(200000)]},
            {"n": 200000, "arr": [[random.randint(-10**9, 10**9), random.randint(-10**9, 10**9)] for _ in range(200000)]},
            {"n": 200000, "arr": [[random.randint(-10**9, 10**9), random.randint(-10**9, 10**9)] for _ in range(200000)]},
            {"n": 200000, "arr": [[random.randint(-10**9, 10**9), random.randint(-10**9, 10**9)] for _ in range(200000)]},
            {"n": 200000, "arr": [[random.randint(-10**9, 10**9), random.randint(-10**9, 10**9)] for _ in range(200000)]},
        ],
        "format_inp": lambda t: f"{t['n']}\n" + "\n".join(f"{min(x[0], x[1])} {max(x[0], x[1])}" for x in t['arr']) + "\n"
    }
]

if __name__ == "__main__":
    print(f"Building {len(LESSON01_PROBLEMS)} problems for Lesson 01...")
    for p in LESSON01_PROBLEMS:
        build_problem(p)
    print("🎉 Done Lesson 01!")
