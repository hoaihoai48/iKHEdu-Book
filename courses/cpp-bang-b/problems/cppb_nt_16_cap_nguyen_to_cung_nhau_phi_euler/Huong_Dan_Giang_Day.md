# Hướng Dẫn Giảng Dạy: Số Học Cực Hạn: Cặp Nguyên Tố Cùng Nhau & Phi Hàm Euler
Chuyên đề: **Bài 07: Lý thuyết số & số nguyên tố**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho số nguyên dương N. Hãy đếm số lượng cặp số nguyên (x, y) thỏa mãn 1 <= x, y <= N và gcd(x, y) = 1.

- **Phương pháp tiếp cận — Lý thuyết số & Số nguyên tố:**
- Tận dụng sàng nguyên tố Eratosthenes cho các truy vấn tiền xử lý $\mathcal{O}(N \log \log N)$ hoặc kiểm tra căn bậc hai $\mathcal{O}(\sqrt{N})$.
- Phân tích thừa số nguyên tố và tính chất ước số để tối ưu hóa bài toán.

---

## 2. Bảng chạy tay trên số liệu mẫu| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `3` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | Các cặp thỏa mãn với N = 3 gồm: (1, 1), (1, 2), (2, 1), (1, 3), (3, 1). Tổng cộng có 5 cặp.... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `5` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* Các cặp thỏa mãn với N = 3 gồm: (1, 1), (1, 2), (2, 1), (1, 3), (3, 1). Tổng cộng có 5 cặp.

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

const int MAXN = 1000000;
vector<int> phi(MAXN + 1);

void sievePhi() {
for (int i = 0; i <= MAXN; ++i) phi[i] = i;
for (int i = 2; i <= MAXN; ++i) {
if (phi[i] == i) { // i là số nguyên tố
for (int j = i; j <= MAXN; j += i) {
phi[j] -= phi[j] / i;
}
}
}
}

int main() {
ios::sync_with_stdio(false);
cin.tie(nullptr);

sievePhi();

int n;
if (!(cin >> n)) return 0;

long long sum_phi = 0;
for (int i = 1; i <= n; ++i) {
sum_phi += phi[i];
}

// Số cặp (x, y) với gcd(x, y) = 1 là 2 * sum(phi(i)) - 1 (do (1,1) tính 1 lần)
long long ans = 2 * sum_phi - 1;
cout << ans << "\n";
return 0;
}
```
