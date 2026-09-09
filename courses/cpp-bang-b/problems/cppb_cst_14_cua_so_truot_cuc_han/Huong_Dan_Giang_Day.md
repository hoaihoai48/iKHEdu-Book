# Hướng Dẫn Giảng Dạy: Tối Ưu Cửa Sổ Trượt Tuyến Tính Khi N = 2.10⁵
Chuyên đề: **Bài 03: Kỹ thuật cửa sổ trượt**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho mảng gồm N số nguyên dương và số nguyên S. Hãy tìm số lượng đoạn con liên tiếp có tổng đúng bằng S trong thời gian O(N).

---

## 2. Bảng chạy tay trên số liệu mẫu| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `5 7 2 3 2 5 2` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | Các đoạn con liên tiếp có tổng đúng bằng 7 là: [2, 3, 2] (2 + 3 + 2 = 7) và [5, 2] (5 + 2 = 7). Tổng cộng có đúng 2 đoạn... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `2` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* Các đoạn con liên tiếp có tổng đúng bằng 7 là: [2, 3, 2] (2 + 3 + 2 = 7) và [5, 2] (5 + 2 = 7). Tổng cộng có đúng 2 đoạn con thỏa mãn.

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

long long count_at_most(const vector<long long> &x, long long limit) {
if (limit <= 0) return 0;
int n = x.size();
int l = 0;
long long cur_sum = 0;
long long count = 0;

for (int r = 0; r < n; ++r) {
cur_sum += x[r];
while (cur_sum > limit) {
cur_sum -= x[l];
++l;
}
count += (r - l + 1);
}
return count;
}

int main() {
ios::sync_with_stdio(false);
cin.tie(nullptr);

int n;
long long a, b;
if (!(cin >> n >> a >> b)) return 0;

vector<long long> x(n);
for (int i = 0; i < n; ++i) cin >> x[i];

long long ans = count_at_most(x, b) - count_at_most(x, a - 1);
cout << ans << "\n";
return 0;
}
```
