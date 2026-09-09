# Hướng Dẫn Giảng Dạy: Cập Nhật Cộng Hình Chữ Nhật (Mảng Hiệu 2D)
Chuyên đề: **Bài 04: Mảng tiền tố & mảng hiệu**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho ma trận N x M ban đầu toàn số 0. Thực hiện Q thao tác cộng giá trị X vào hình chữ nhật từ (r1, c1) đến (r2, c2). Hãy in ra ma trận kết quả sau Q thao tác bằng Mảng hiệu 2D.

- **Phương pháp tiếp cận — Mảng tiền tố & Mảng hiệu:**
- Dựng mảng cộng dồn `pref[i] = pref[i-1] + a[i]`. Khi đó tổng đoạn $[L, R]$ được tính tức thì bằng `pref[R] - pref[L-1]` trong $\mathcal{O}(1)$.
- Với các thao tác cộng dồn đoạn, sử dụng mảng hiệu `diff[L] += V, diff[R+1] -= V` rồi cộng dồn để phục hồi mảng.

---

## 2. Bảng chạy tay trên số liệu mẫu| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `3 3 1 1 1 2 2 5` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | Thao tác cộng 5 vào hình chữ nhật từ (1, 1) đến (2, 2) làm cho 4 ô ở góc trên bên trái đều có giá trị 5, các ô còn lại g... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `5 5 0 5 5 0 0 0 0` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* Thao tác cộng 5 vào hình chữ nhật từ (1, 1) đến (2, 2) làm cho 4 ô ở góc trên bên trái đều có giá trị 5, các ô còn lại giữ nguyên giá trị 0.

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

int n, m, q;
if (!(cin >> n >> m >> q)) return 0;

vector<vector<long long>> d(n + 2, vector<long long>(m + 2, 0));

while (q--) {
int x1, y1, x2, y2;
long long v;
cin >> x1 >> y1 >> x2 >> y2 >> v;
d[x1][y1] += v;
d[x1][y2 + 1] -= v;
d[x2 + 1][y1] -= v;
d[x2 + 1][y2 + 1] += v;
}

for (int i = 1; i <= n; ++i) {
for (int j = 1; j <= m; ++j) {
d[i][j] = d[i - 1][j] + d[i][j - 1] - d[i - 1][j - 1] + d[i][j];
cout << d[i][j] << (j == m "" : " ");
}
cout << "\n";
}

return 0;
}
```
