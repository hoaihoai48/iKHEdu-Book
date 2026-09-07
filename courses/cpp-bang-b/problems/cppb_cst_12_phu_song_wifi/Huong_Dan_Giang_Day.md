# Hướng Dẫn Giảng Dạy: Phủ Sóng Trạm Phát Sóng Wifi Đô Thị
Chuyên đề: **Bài 03: Kỹ thuật cửa sổ trượt**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho danh sách tọa độ của N căn nhà đã sắp xếp tăng dần và số nguyên R. Hãy tìm số lượng căn nhà nhiều nhất nằm gọn trong một đoạn có độ dài không vượt quá 2R.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 5 3 1 3 5 8 10)
| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `5 3 1 3 5 8 10` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | Với bán kính R = 3, đường kính phủ sóng tối đa là 2R = 6. Xét đoạn từ nhà tọa độ 1 đến nhà tọa độ 5: độ dài khoảng cách ... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `3` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* Với bán kính R = 3, đường kính phủ sóng tối đa là 2R = 6. Xét đoạn từ nhà tọa độ 1 đến nhà tọa độ 5: độ dài khoảng cách là 5 - 1 = 4 <= 6, phủ sóng được 3 căn nhà tại các tọa độ {1, 3, 5}. Tương tự, đoạn {3, 5, 8} có 8 - 3 = 5 <= 6 cũng phủ được 3 nhà. Số lượng nhà tối đa phủ được là 3.

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
    long long r;
    if (!(cin >> n >> r)) return 0;

    vector<long long> x(n);
    for (int i = 0; i < n; ++i) cin >> x[i];

    int i = 0;
    int count = 0;

    while (i < n) {
        ++count;
        long long loc = x[i];
        while (i < n && x[i] - loc <= r) ++i;
        long long tower = x[i - 1];
        while (i < n && x[i] - tower <= r) ++i;
    }

    cout << count << "\n";
    return 0;
}
```
