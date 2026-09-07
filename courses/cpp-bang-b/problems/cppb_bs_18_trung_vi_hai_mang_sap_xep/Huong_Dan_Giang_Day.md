# Hướng Dẫn Giảng Dạy: Trung Vị Của Hai Mảng Đã Sắp Xếp (Median of Two Sorted)
Chuyên đề: **Bài 05: Thuật toán tìm kiếm nhị phân**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho hai mảng đã sắp xếp A (kích thước N) và B (kích thước M). Hãy tìm giá trị trung vị của mảng hợp nhất với độ chính xác 1 chữ số thập phân.

- **Phương pháp tiếp cận — Tìm kiếm nhị phân (Binary Search):**
  - Nhận diện tính đơn điệu của hàm mục tiêu hoặc không gian tìm kiếm.
  - Thu hẹp không gian nghiệm $[L, R]$ qua điểm giữa $mid = L + (R - L) / 2$. Độ phức tạp thời gian đạt $\mathcal{O}(\log N)$ hoặc $\mathcal{O}(N \log(\text{range}))$.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 2 2 1 3 2 4)
| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `2 2 1 3 2 4` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | Mảng hợp nhất: [1, 2, 3, 4] có 4 phần tử. Hai phần tử ở giữa là 2 và 3. Giá trị trung vị là (2 + 3) / 2 = 2.5. Kết quả i... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `2.5` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* Mảng hợp nhất: [1, 2, 3, 4] có 4 phần tử. Hai phần tử ở giữa là 2 và 3. Giá trị trung vị là (2 + 3) / 2 = 2.5. Kết quả in ra: 2.5.

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- **Bẫy 1 — Tràn số nguyên:** Khi tính toán tổng, tích hoặc lũy thừa lớn hơn $2 \cdot 10^9$, bắt buộc phải sử dụng kiểu dữ liệu `long long` (64-bit) để tránh tràn số âm.
- **Bẫy 2 — Chỉ số mảng & Giới hạn biên:** Chú ý giữa đánh chỉ số 0-based (`0 .. N-1`) và 1-based (`1 .. N`). Kiểm tra kỹ trường hợp $N = 1$ hoặc giá trị biên tối đa của đề bài.
- **Bẫy 3 — Tối ưu thời gian I/O:** Luôn sử dụng `ios::sync_with_stdio(false); cin.tie(nullptr);` ở đầu hàm `main()` để đọc ghi nhanh, tránh bị TLE khi số lượng testcase lớn.

---

## 4. Lời giải tham khảo
```cpp
#include <bits/stdc++.h>
using namespace std;

double findMedianSortedArrays(vector<long long>& a, vector<long long>& b) {
    if (a.size() > b.size()) return findMedianSortedArrays(b, a);

    int n = (int)a.size();
    int m = (int)b.size();
    int low = 0, high = n;

    const long long INF = 2e18;

    while (low <= high) {
        int i = low + (high - low) / 2;
        int j = (n + m + 1) / 2 - i;

        long long maxLeftA = (i == 0) ? -INF : a[i - 1];
        long long minRightA = (i == n) ? INF : a[i];

        long long maxLeftB = (j == 0) ? -INF : b[j - 1];
        long long minRightB = (j == m) ? INF : b[j];

        if (maxLeftA <= minRightB && maxLeftB <= minRightA) {
            if ((n + m) % 2 == 1) {
                return (double)max(maxLeftA, maxLeftB);
            } else {
                return (max(maxLeftA, maxLeftB) + min(minRightA, minRightB)) / 2.0;
            }
        } else if (maxLeftA > minRightB) {
            high = i - 1;
        } else {
            low = i + 1;
        }
    }
    return 0.0;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<long long> a(n), b(m);
    for (int i = 0; i < n; ++i) cin >> a[i];
    for (int i = 0; i < m; ++i) cin >> b[i];

    double median = findMedianSortedArrays(a, b);
    cout << fixed << setprecision(1) << median << "\n";

    return 0;
}
```
