# Hướng Dẫn Giảng Dạy: Số Có Đúng 3 Ước Số
Chuyên đề: **Bài 07: Lý thuyết số & số nguyên tố**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho số nguyên dương N. Hãy đếm số lượng số nguyên dương <= N có đúng 3 ước số nguyên dương.

- **Phương pháp tiếp cận — Lý thuyết số & Số nguyên tố:**
- Tận dụng sàng nguyên tố Eratosthenes cho các truy vấn tiền xử lý $\mathcal{O}(N \log \log N)$ hoặc kiểm tra căn bậc hai $\mathcal{O}(\sqrt{N})$.
- Phân tích thừa số nguyên tố và tính chất ước số để tối ưu hóa bài toán.

---

## 2. Bảng chạy tay trên số liệu mẫu| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `50` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | Các số có đúng 3 ước số <= 50 là bình phương các số nguyên tố: 2^2=4, 3^2=9, 5^2=25, 7^2=49. Tổng cộng có 4 số.... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `4` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* Các số có đúng 3 ước số <= 50 là bình phương các số nguyên tố: 2^2=4, 3^2=9, 5^2=25, 7^2=49. Tổng cộng có 4 số.

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

int lim = sqrt(n);
vector<bool> is_prime(lim + 1, true);
is_prime[0] = is_prime[1] = false;
for (int i = 2; 1LL * i * i <= lim; ++i) {
if (is_prime[i]) {
for (int j = i * i; j <= lim; j += i) is_prime[j] = false;
}
}

int count_3div = 0;
for (int i = 2; i <= lim; ++i) {
if (is_prime[i] && 1LL * i * i <= n) count_3div++;
}

cout << count_3div << "\n";
return 0;
}
```
