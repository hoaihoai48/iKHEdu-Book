# Hướng Dẫn Giảng Dạy: Sắp Xếp Theo Tổng Chữ Số
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
```