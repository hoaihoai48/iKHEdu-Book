# Hướng Dẫn Giảng Dạy: Đếm Giá Trị Phân Biệt
Chuyên đề: **Bài 01: Thuật toán sắp xếp**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho danh sách $N$ mã số thẻ nguyên $A_1, A_2, \dots, A_N$. Hãy đếm và in ra số lượng giá trị phân biệt trong dãy số đó.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 6 2 3 2 1 3 5)
| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `6 2 3 2 1 3 5` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | Danh sách mã vé ghi nhận là: $2, 3, 2, 1, 3, 5$. Sau khi sắp xếp tăng dần: $1, 2, 2, 3, 3, 5$. Các nhóm giá trị trùng nh... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `4` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* Danh sách mã vé ghi nhận là: $2, 3, 2, 1, 3, 5$.
Sau khi sắp xếp tăng dần: $1, 2, 2, 3, 3, 5$.
Các nhóm giá trị trùng nhau được gom liền kề:
- Giá trị $1$ (xuất hiện 1 lần)
- Giá trị $2$ (xuất hiện 2 lần)
- Giá trị $3$ (xuất hiện 2 lần)
- Giá trị $5$ (xuất hiện 1 lần)
Tổng cộng có $4$ giá trị phân biệt khác nhau là $\{1, 2, 3, 5\}$. Do đó in ra kết quả là `4`.

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

    int cnt = 1;
    for (int i = 1; i < n; ++i) {
        if (a[i] != a[i - 1]) ++cnt;
    }

    cout << cnt << "\n";
    return 0;
}
```
