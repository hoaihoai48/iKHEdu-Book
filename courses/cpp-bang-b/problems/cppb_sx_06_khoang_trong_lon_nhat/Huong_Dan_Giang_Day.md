# Hướng Dẫn Giảng Dạy: Khoảng Trống Lớn Nhất Trên Trục Tọa Độ
Chuyên đề: **Bài 01: Thuật toán sắp xếp**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho danh sách tọa độ của $N$ chướng ngại vật. Hãy tìm và in ra khoảng cách lớn nhất giữa hai chướng ngại vật liên tiếp sau khi sắp xếp vị trí của chúng theo thứ tự tăng dần trên trục tọa độ.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 5 10 3 25 8 12)
| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `5 10 3 25 8 12` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | Tọa độ các chướng ngại vật ban đầu là: $10, 3, 25, 8, 12$. Sau khi sắp xếp tăng dần theo chiều dọc hành lang: $3, 8, 10,... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `13` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* Tọa độ các chướng ngại vật ban đầu là: $10, 3, 25, 8, 12$.
Sau khi sắp xếp tăng dần theo chiều dọc hành lang:
$3, 8, 10, 12, 25$.
Khoảng cách giữa các chướng ngại vật liên tiếp lần lượt là:

- $8 - 3 = 5$
- $10 - 8 = 2$
- $12 - 10 = 2$
- $25 - 12 = 13$

Khoảng trống lớn nhất giữa hai chướng ngại vật liên tiếp là $13$ (giữa vị trí $12$ và $25$).

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

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    sort(a.begin(), a.end());

    long long max_gap = 0;
    for (int i = 0; i < n - 1; ++i) {
        max_gap = max(max_gap, a[i + 1] - a[i]);
    }

    cout << max_gap << "\n";
    return 0;
}
```
