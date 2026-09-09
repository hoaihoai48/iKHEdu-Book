# Hướng Dẫn Giảng Dạy: Duyệt Toàn Bộ 2^N Tập Con Bằng Mặt Nạ Bit
Chuyên đề: **Bài 06: Phép toán BIT & biểu diễn trạng thái**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho tập hợp gồm N số nguyên. Hãy in ra tổng các phần tử của tất cả 2^N tập con theo thứ tự mặt nạ bit tăng dần từ 0 đến 2^N - 1.

- **Phương pháp tiếp cận — Phép toán BIT & Bitmask:**
- Biểu diễn tập hợp hoặc trạng thái bật/tắt bằng các bit của số nguyên 64-bit.
- Sử dụng các toán tử bitwise `&, |, ^, ~, <<, >>` để thao tác đồng thời trong $\mathcal{O}(1)$ chu kỳ máy.

---

## 2. Bảng chạy tay trên số liệu mẫu| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `2 3 5` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | - Mask 0 (00_2): tập rỗng -> tổng 0. - Mask 1 (01_2): tập {A[0]} = {3} -> tổng 3. - Mask 2 (10_2): tập {A[1]} = {5} -> t... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `0 3 5 8` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* - Mask 0 (00_2): tập rỗng -> tổng 0.

- Mask 1 (01_2): tập {A[0]} = {3} -> tổng 3.
- Mask 2 (10_2): tập {A[1]} = {5} -> tổng 5.
- Mask 3 (11_2): tập {A[0], A[1]} = {3, 5} -> tổng 8.

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
for (int i = 0; i < n; ++i) {
cin >> a[i];
}

int total_masks = (1 << n);
for (int mask = 0; mask < total_masks; ++mask) {
bool first = true;
for (int i = 0; i < n; ++i) {
if ((mask >> i) & 1) {
if (!first) cout << " ";
cout << a[i];
first = false;
}
}
cout << "\n";
}

return 0;
}
```
