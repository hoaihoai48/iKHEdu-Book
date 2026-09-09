# Hướng Dẫn Giảng Dạy: Đếm Số Lượng & Tính Tổng Các Ước Số
Chuyên đề: **Bài 07: Lý thuyết số & số nguyên tố**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho số nguyên dương N. Hãy tính số lượng ước số nguyên dương d(N) và tổng tất cả các ước số nguyên dương của N.

- **Phương pháp tiếp cận — Lý thuyết số & Số nguyên tố:**
- Tận dụng sàng nguyên tố Eratosthenes cho các truy vấn tiền xử lý $\mathcal{O}(N \log \log N)$ hoặc kiểm tra căn bậc hai $\mathcal{O}(\sqrt{N})$.
- Phân tích thừa số nguyên tố và tính chất ước số để tối ưu hóa bài toán.

---

## 2. Bảng chạy tay trên số liệu mẫu| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `12` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | Các ước số của 12 là {1, 2, 3, 4, 6, 12}, tổng cộng có 6 ước. Tổng các ước là 1 + 2 + 3 + 4 + 6 + 12 = 28. Kết quả in ra... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `6 28` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* Các ước số của 12 là {1, 2, 3, 4, 6, 12}, tổng cộng có 6 ước. Tổng các ước là 1 + 2 + 3 + 4 + 6 + 12 = 28. Kết quả in ra: 6 28.

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

long long count_div = 1;
long long sum_div = 1;

for (long long i = 2; i * i <= n; ++i) {
if (n % i == 0) {
int a = 0;
long long p_pow = 1;
long long cur_sum = 1;
while (n % i == 0) {
a++;
n /= i;
p_pow *= i;
cur_sum += p_pow;
}
count_div *= (a + 1);
sum_div *= cur_sum;
}
}
if (n > 1) {
count_div *= 2;
sum_div *= (1 + n);
}

cout << count_div << " " << sum_div << "\n";
return 0;
}
```
