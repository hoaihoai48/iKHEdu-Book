# Hướng Dẫn Giảng Dạy: Vận Chuyển Hàng Hóa Qua Phà Trong D Ngày
Chuyên đề: **Bài 05: Thuật toán tìm kiếm nhị phân**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho trọng lượng N kiện hàng và số ngày D. Tìm tải trọng nhỏ nhất của phà để chở hết hàng trong D ngày.

- **Phương pháp tiếp cận — Tìm kiếm nhị phân (Binary Search):**
  - Nhận diện tính đơn điệu của hàm mục tiêu hoặc không gian tìm kiếm.
  - Thu hẹp không gian nghiệm $[L, R]$ qua điểm giữa $mid = L + (R - L) / 2$. Độ phức tạp thời gian đạt $\mathcal{O}(\log N)$ hoặc $\mathcal{O}(N \log(\text{range}))$.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 10 5 1 2 3 4 5 6 7 8 9 10)
| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `10 5 1 2 3 4 5 6 7 8 9 10` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | Với tải trọng 15: - Ngày 1: chở [1, 2, 3, 4, 5] (tổng 15) - Ngày 2: chở [6, 7] (tổng 13) - Ngày 3: chở [8] (tổng 8) - Ng... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `15` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* Với tải trọng 15:
- Ngày 1: chở [1, 2, 3, 4, 5] (tổng 15)
- Ngày 2: chở [6, 7] (tổng 13)
- Ngày 3: chở [8] (tổng 8)
- Ngày 4: chở [9] (tổng 9)
- Ngày 5: chở [10] (tổng 10)
Tổng cộng 5 ngày chở hết 10 kiện hàng. Tải trọng nhỏ nhất là 15.

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

bool check(long long cap, const vector<long long>& w, int d) {
    int days = 1;
    long long current_weight = 0;
    for (long long x : w) {
        if (current_weight + x > cap) {
            days++;
            current_weight = x;
        } else {
            current_weight += x;
        }
    }
    return days <= d;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, d;
    if (!(cin >> n >> d)) return 0;

    vector<long long> w(n);
    long long max_w = 0, sum_w = 0;
    for (int i = 0; i < n; ++i) {
        cin >> w[i];
        max_w = max(max_w, w[i]);
        sum_w += w[i];
    }

    long long low = max_w, high = sum_w, ans = sum_w;
    while (low <= high) {
        long long mid = low + (high - low) / 2;
        if (check(mid, w, d)) {
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
