# Hướng Dẫn Giảng Dạy: Tối Ưu Hóa Tuyến Đường Vận Tải Đa Điểm
Chuyên đề: **Bài 05: Thuật toán tìm kiếm nhị phân**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho mảng N số nguyên và số nguyên K. Hãy tìm giá trị cận trên tải trọng nhỏ nhất cho mỗi đoàn tàu.

- **Phương pháp tiếp cận — Tìm kiếm nhị phân (Binary Search):**
  - Nhận diện tính đơn điệu của hàm mục tiêu hoặc không gian tìm kiếm.
  - Thu hẹp không gian nghiệm $[L, R]$ qua điểm giữa $mid = L + (R - L) / 2$. Độ phức tạp thời gian đạt $\mathcal{O}(\log N)$ hoặc $\mathcal{O}(N \log(\text{range}))$.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 4 2 1 2 3 4)
| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `4 2 1 2 3 4` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | Chia thành 2 đoàn: [1, 2, 3] có tổng 6 và [4] có tổng 4. Mức tải trọng lớn nhất giữa hai đoàn là 6. Đây là mức tải trọng... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `6` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* Chia thành 2 đoàn: [1, 2, 3] có tổng 6 và [4] có tổng 4. Mức tải trọng lớn nhất giữa hai đoàn là 6. Đây là mức tải trọng trần nhỏ nhất có thể đạt được.

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

bool check(long long cap, const vector<long long>& a, int n, int m, int d) {
    int trucks = 0;
    int i = 0;
    while (i < n) {
        trucks++;
        if (trucks > m) return false;
        long long current_load = 0;
        int count_cities = 0;
        while (i < n && count_cities < d && current_load + a[i] <= cap) {
            current_load += a[i];
            count_cities++;
            i++;
        }
    }
    return trucks <= m;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, d;
    if (!(cin >> n >> m >> d)) return 0;

    vector<long long> a(n);
    long long max_val = 0, sum_val = 0;
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        max_val = max(max_val, a[i]);
        sum_val += a[i];
    }

    long long low = max_val, high = sum_val, ans = sum_val;
    while (low <= high) {
        long long mid = low + (high - low) / 2;
        if (check(mid, a, n, m, d)) {
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
