# Hướng Dẫn Giảng Dạy: Phần Tử Thứ K Của Hai Mảng Đã Sắp Xếp
Chuyên đề: **Bài 05: Thuật toán tìm kiếm nhị phân**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho hai mảng số nguyên đã sắp xếp A (kích thước N) và B (kích thước M) cùng số nguyên dương K (1 <= K <= N + M). Hãy tìm giá trị của phần tử đứng ở vị trí thứ K sau khi hợp nhất hai mảng trong thời gian O(log(min(N, M))).

- **Phương pháp tiếp cận — Tìm kiếm nhị phân (Binary Search):**
  - Nhận diện tính đơn điệu của hàm mục tiêu hoặc không gian tìm kiếm.
  - Thu hẹp không gian nghiệm $[L, R]$ qua điểm giữa $mid = L + (R - L) / 2$. Độ phức tạp thời gian đạt $\mathcal{O}(\log N)$ hoặc $\mathcal{O}(N \log(\text{range}))$.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 5 4 5 2 3 6 7 9 1 4 8 10)
| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `5 4 5 2 3 6 7 9 1 4 8 10` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | Hợp nhất hai mảng có thứ tự: [1, 2, 3, 4, 6, 7, 8, 9, 10]. Phần tử đứng thứ K = 5 là số 6. Kết quả in ra: 6.... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `6` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* Hợp nhất hai mảng có thứ tự: [1, 2, 3, 4, 6, 7, 8, 9, 10]. Phần tử đứng thứ K = 5 là số 6. Kết quả in ra: 6.

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

long long count_le(long long x, const vector<long long>& a, const vector<long long>& b) {
    auto it1 = upper_bound(a.begin(), a.end(), x);
    auto it2 = upper_bound(b.begin(), b.end(), x);
    return (it1 - a.begin()) + (it2 - b.begin());
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    long long k;
    if (!(cin >> n >> m >> k)) return 0;

    vector<long long> a(n), b(m);
    for (int i = 0; i < n; ++i) cin >> a[i];
    for (int i = 0; i < m; ++i) cin >> b[i];

    long long low = -2e9, high = 2e9, ans = high;
    while (low <= high) {
        long long mid = low + (high - low) / 2;
        if (count_le(mid, a, b) >= k) {
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
