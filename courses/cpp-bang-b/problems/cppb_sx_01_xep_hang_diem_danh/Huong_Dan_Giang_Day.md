# Hướng Dẫn Giảng Dạy: Xếp Hàng Điểm Danh
Chuyên đề: **Bài 01: Thuật toán sắp xếp**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho danh sách chiều cao của $N$ bạn học sinh. Hãy in ra danh sách chiều cao sau khi đã xếp hàng theo thứ tự tăng dần.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 5 1550 1420 1680 1500 160)
| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `5 1550 1420 1680 1500 1600` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | Chiều cao ban đầu của 5 bạn học sinh lần lượt là: $1550, 1420, 1680, 1500, 1600$ (đơn vị: mm). Sau khi sắp xếp theo thứ ... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `1420 1500 1550 1600 1680` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* Chiều cao ban đầu của 5 bạn học sinh lần lượt là: $1550, 1420, 1680, 1500, 1600$ (đơn vị: mm).
Sau khi sắp xếp theo thứ tự chiều cao tăng dần từ thấp đến cao, thứ tự đứng vào hàng chuẩn xác sẽ là:
$1420 \le 1500 \le 1550 \le 1600 \le 1680$.

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

    vector<int> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    sort(a.begin(), a.end());

    for (int i = 0; i < n; ++i) {
        cout << a[i] << (i == n - 1 ? "" : " ");
    }
    cout << "\n";
    return 0;
}
```
