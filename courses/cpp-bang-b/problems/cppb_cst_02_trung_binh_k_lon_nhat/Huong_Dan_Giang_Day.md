# Hướng Dẫn Giảng Dạy: Giá Trị Trung Bình Lớn Nhất Của Đoạn K
Chuyên đề: **Bài 03: Kỹ thuật cửa sổ trượt**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho dãy gồm N số nguyên và số nguyên K (K <= N). Hãy tìm giá trị trung bình lớn nhất của một đoạn con gồm K phần tử liên tiếp, làm tròn đến đúng 3 chữ số thập phân.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 4 4 1 12 -5 -6)
| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `4 4 1 12 -5 -6` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | Với N = 4 và K = 4, chỉ có duy nhất 1 đoạn con gồm 4 phần tử: [1, 12, -5, -6]. Tổng của đoạn là 1 + 12 - 5 - 6 = 2. Giá ... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `0.500` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* Với N = 4 và K = 4, chỉ có duy nhất 1 đoạn con gồm 4 phần tử: [1, 12, -5, -6]. Tổng của đoạn là 1 + 12 - 5 - 6 = 2. Giá trị trung bình là 2 / 4 = 0.500. Kết quả in ra: 0.500.

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
    cout << fixed << setprecision(3) << ans << "\n";
    return 0;
}
```
