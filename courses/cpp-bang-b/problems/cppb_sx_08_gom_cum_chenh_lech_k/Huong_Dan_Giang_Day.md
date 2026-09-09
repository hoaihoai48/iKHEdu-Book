# Hướng Dẫn Giảng Dạy: Gom Cụm Chênh Lệch Không Quá K
Chuyên đề: **Bài 01: Thuật toán sắp xếp**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho điểm năng lực của $N$ bạn học sinh và số nguyên $K$. Hãy tìm số lượng nhóm ít nhất để phân chia toàn bộ $N$ học sinh thỏa mãn điều kiện chênh lệch tối đa giữa bạn cao nhất và bạn thấp nhất trong mỗi nhóm không quá $K$.

---

## 2. Bảng chạy tay trên số liệu mẫu| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `6 3 1 10 3 4 12 15` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | Sắp xếp điểm năng lực của 6 bạn học sinh theo thứ tự tăng dần: $1, 3, 4, 10, 12, 15$. Với $K = 3$, ta có thể gom tối ưu ... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `3` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* Sắp xếp điểm năng lực của 6 bạn học sinh theo thứ tự tăng dần:
$1, 3, 4, 10, 12, 15$.
Với $K = 3$, ta có thể gom tối ưu thành 3 nhóm như sau:

- Nhóm 1: $\{1, 3, 4\}$ (Điểm cao nhất là $4$, thấp nhất là $1$, chênh lệch $4 - 1 = 3 \le 3$).
- Nhóm 2: $\{10, 12\}$ (Điểm cao nhất là $12$, thấp nhất là $10$, chênh lệch $12 - 10 = 2 \le 3$).
- Nhóm 3: $\{15\}$ (Chỉ gồm 1 bạn, chênh lệch bằng $0 \le 3$).

Không thể chia thành ít hơn 3 nhóm mà vẫn thỏa mãn điều kiện. Vì vậy kết quả là `3`.

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
long long k;
if (!(cin >> n >> k)) return 0;

vector<long long> a(n);
for (int i = 0; i < n; ++i) cin >> a[i];

sort(a.begin(), a.end());

int groups = 1;
long long min_val = a[0];

for (int i = 1; i < n; ++i) {
if (a[i] - min_val > k) {
++groups;
min_val = a[i];
}
}

cout << groups << "\n";
return 0;
}
```
