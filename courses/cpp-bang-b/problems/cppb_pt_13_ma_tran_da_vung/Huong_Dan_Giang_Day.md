# Hướng Dẫn Giảng Dạy: Truy Vấn Ma Trận Đa Vùng Cực Đại
Chuyên đề: **Bài 04: Mảng tiền tố & mảng hiệu**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho một ma trận N x M. Mỗi truy vấn cung cấp tọa độ của hai hình chữ nhật rời nhau, hãy tính tổng giá trị của tất cả các phần tử thuộc về cả hai hình chữ nhật đó.

- **Phương pháp tiếp cận — Mảng tiền tố & Mảng hiệu:**
- Dựng mảng cộng dồn `pref[i] = pref[i-1] + a[i]`. Khi đó tổng đoạn $[L, R]$ được tính tức thì bằng `pref[R] - pref[L-1]` trong $\mathcal{O}(1)$.
- Với các thao tác cộng dồn đoạn, sử dụng mảng hiệu `diff[L] += V, diff[R+1] -= V` rồi cộng dồn để phục hồi mảng.

---

## 2. Bảng chạy tay trên số liệu mẫu| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `3 3 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 2` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | Hình chữ nhật 1 là ô (1, 1) có giá trị 1. Hình chữ nhật 2 là vùng từ (2, 2) đến (3, 3) gồm 4 ô giá trị 1 (tổng bằng 4). ... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `5` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* Hình chữ nhật 1 là ô (1, 1) có giá trị 1. Hình chữ nhật 2 là vùng từ (2, 2) đến (3, 3) gồm 4 ô giá trị 1 (tổng bằng 4). Tổng hai vùng là 1 + 4 = 5.

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

vector<vector<long long>> p(n + 1, vector<long long>(m + 1, 0));
for (int i = 1; i <= n; ++i) {
for (int j = 1; j <= m; ++j) {
long long val;
cin >> val;
p[i][j] = p[i - 1][j] + p[i][j - 1] - p[i - 1][j - 1] + val;
}
}

auto query = [&](int x1, int y1, int x2, int y2) -> long long {
return p[x2][y2] - p[x1 - 1][y2] - p[x2][y1 - 1] + p[x1 - 1][y1 - 1];
};

while (q--) {
int x1, y1, x2, y2, u1, v1, u2, v2;
cin >> x1 >> y1 >> x2 >> y2 >> u1 >> v1 >> u2 >> v2;
cout << query(x1, y1, x2, y2) + query(u1, v1, u2, v2) << "\n";
}

return 0;
}
```
