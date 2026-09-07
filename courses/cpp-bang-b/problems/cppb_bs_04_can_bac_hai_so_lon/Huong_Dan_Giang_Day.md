# Hướng Dẫn Giảng Dạy: Tìm Căn Bậc Hai Số Nguyên Lớn
Chuyên đề: **Bài 05: Thuật toán tìm kiếm nhị phân**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho số nguyên dương N (1 <= N <= 10^18). Hãy tìm số nguyên dương X lớn nhất thỏa mãn X^2 <= N bằng tìm kiếm nhị phân trên tập kết quả.

- **Phương pháp tiếp cận — Tìm kiếm nhị phân (Binary Search):**
  - Nhận diện tính đơn điệu của hàm mục tiêu hoặc không gian tìm kiếm.
  - Thu hẹp không gian nghiệm $[L, R]$ qua điểm giữa $mid = L + (R - L) / 2$. Độ phức tạp thời gian đạt $\mathcal{O}(\log N)$ hoặc $\mathcal{O}(N \log(\text{range}))$.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 17)
| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `17` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | 4^2 = 16 <= 17, trong khi 5^2 = 25 > 17. Số nguyên lớn nhất có bình phương <= 17 là 4.... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `4` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* 4^2 = 16 <= 17, trong khi 5^2 = 25 > 17. Số nguyên lớn nhất có bình phương <= 17 là 4.

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

void solve() {
    long long n;
    cin >> n;
    long long low = 1, high = 1000000000LL, ans = 1;
    while (low <= high) {
        long long mid = low + (high - low) / 2;
        if (mid <= n / mid) {
            ans = mid;
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }
    cout << ans << "\n";
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    if (!(cin >> t)) return 0;
    while (t--) {
        solve();
    }
    return 0;
}
```
