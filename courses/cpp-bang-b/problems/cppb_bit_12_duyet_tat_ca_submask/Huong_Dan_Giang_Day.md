# Hướng Dẫn Giảng Dạy: Duyệt Tất Cả Các Tập Con Của Một Mặt Nạ Bit
Chuyên đề: **Bài 06: Phép toán BIT & biểu diễn trạng thái**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho số nguyên dương N. Hãy liệt kê tất cả các số nguyên dương s là tập con bit của N (nghĩa là (s & N) == s với s > 0) theo thứ tự giảm dần.

- **Phương pháp tiếp cận — Phép toán BIT & Bitmask:**
- Biểu diễn tập hợp hoặc trạng thái bật/tắt bằng các bit của số nguyên 64-bit.
- Sử dụng các toán tử bitwise `&, |, ^, ~, <<, >>` để thao tác đồng thời trong $\mathcal{O}(1)$ chu kỳ máy.

---

## 2. Bảng chạy tay trên số liệu mẫu| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `5` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | 5 có biểu diễn nhị phân là 101_2. Các tập con bit dương của 101_2 gồm có: 101_2 (5), 100_2 (4) và 001_2 (1). Thứ tự giảm... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `5 4 1` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* 5 có biểu diễn nhị phân là 101_2. Các tập con bit dương của 101_2 gồm có: 101_2 (5), 100_2 (4) và 001_2 (1). Thứ tự giảm dần là: 5 4 1.

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

long long n;
if (!(cin >> n)) return 0;

bool first = true;
for (long long sub = n; sub > 0; sub = (sub - 1) & n) {
if (!first) cout << " ";
cout << sub;
first = false;
}
cout << "\n";

return 0;
}
```
