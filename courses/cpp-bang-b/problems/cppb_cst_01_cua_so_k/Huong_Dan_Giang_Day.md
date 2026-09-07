# Hướng Dẫn Giảng Dạy: Tổng Cửa Sổ Cố Định K
Chuyên đề: **Bài 03: Kỹ thuật cửa sổ trượt**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho dãy N số nguyên và số nguyên dương K (K <= N). Hãy tìm đoạn con gồm K phần tử liên tiếp có tổng lớn nhất. In ra tổng lớn nhất và chỉ số bắt đầu (1-indexed) của đoạn con đó. Nếu có nhiều đoạn cùng đạt tổng lớn nhất, in ra chỉ số bắt đầu nhỏ nhất.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 7 3 2 1 5 1 3 2 4)
| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `7 3 2 1 5 1 3 2 4` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | Các cửa sổ độ dài K = 3 gồm: [2, 1, 5] (tổng 8), [1, 5, 1] (tổng 7), [5, 1, 3] (tổng 9 tại vị trí 3), [1, 3, 2] (tổng 6)... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `9 3` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* Các cửa sổ độ dài K = 3 gồm: [2, 1, 5] (tổng 8), [1, 5, 1] (tổng 7), [5, 1, 3] (tổng 9 tại vị trí 3), [1, 3, 2] (tổng 6), [3, 2, 4] (tổng 9 tại vị trí 5). Tổng lớn nhất là 9, đạt được sớm nhất tại vị trí bắt đầu 3. Kết quả in ra: 9 3.

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

    cout << max_sum << "\n";
    return 0;
}
```
