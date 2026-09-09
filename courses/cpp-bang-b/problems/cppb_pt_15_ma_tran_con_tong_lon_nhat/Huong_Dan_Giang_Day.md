# Hướng Dẫn Giảng Dạy: Tìm Ma Trận Con Có Tổng Lớn Nhất (Max Submatrix Sum)
Chuyên đề: **Bài 04: Mảng tiền tố & mảng hiệu**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho ma trận số nguyên A kích thước N x M. Hãy tìm một ma trận con chữ nhật có tổng các phần tử là lớn nhất.

- **Phương pháp tiếp cận — Mảng tiền tố & Mảng hiệu:**
- Dựng mảng cộng dồn `pref[i] = pref[i-1] + a[i]`. Khi đó tổng đoạn $[L, R]$ được tính tức thì bằng `pref[R] - pref[L-1]` trong $\mathcal{O}(1)$.
- Với các thao tác cộng dồn đoạn, sử dụng mảng hiệu `diff[L] += V, diff[R+1] -= V` rồi cộng dồn để phục hồi mảng.

---

## 2. Bảng chạy tay trên số liệu mẫu| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `3 3 1 2 -1 -8 -9 -2 3 4 5` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | Ma trận con ở hàng 3 gồm các phần tử [3, 4, 5] có tổng 3 + 4 + 5 = 12. Đây là ma trận con có tổng lớn nhất trong bảng.... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `12` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* Ma trận con ở hàng 3 gồm các phần tử [3, 4, 5] có tổng 3 + 4 + 5 = 12. Đây là ma trận con có tổng lớn nhất trong bảng.

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

int n, m;
if (!(cin >> n >> m)) return 0;

vector<vector<long long>> a(n + 1, vector<long long>(m + 1));
vector<vector<long long>> p(n + 1, vector<long long>(m + 1, 0));

for (int i = 1; i <= n; ++i) {
for (int j = 1; j <= m; ++j) {
cin >> a[i][j];
p[i][j] = p[i - 1][j] + a[i][j]; // Tiền tố theo cột
}
}

long long max_sum = -4e18;

for (int r1 = 1; r1 <= n; ++r1) {
for (int r2 = r1; r2 <= n; ++r2) {
long long current_kadane = 0;
for (int c = 1; c <= m; ++c) {
long long val = p[r2][c] - p[r1 - 1][c];
current_kadane = max(val, current_kadane + val);
max_sum = max(max_sum, current_kadane);
}
}
}

cout << max_sum << "\n";
return 0;
}
```
