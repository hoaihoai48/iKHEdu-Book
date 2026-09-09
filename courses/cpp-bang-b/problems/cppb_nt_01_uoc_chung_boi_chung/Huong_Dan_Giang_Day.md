# Hướng Dẫn Giảng Dạy: Ước Chung Lớn Nhất & Bội Chung Nhỏ Nhất
Chuyên đề: **Bài 07: Lý thuyết số & số nguyên tố**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho hai số nguyên dương A và B. Hãy tìm ước chung lớn nhất gcd(A, B) và bội chung nhỏ nhất lcm(A, B).

- **Phương pháp tiếp cận — Lý thuyết số & Số nguyên tố:**
- Tận dụng sàng nguyên tố Eratosthenes cho các truy vấn tiền xử lý $\mathcal{O}(N \log \log N)$ hoặc kiểm tra căn bậc hai $\mathcal{O}(\sqrt{N})$.
- Phân tích thừa số nguyên tố và tính chất ước số để tối ưu hóa bài toán.

---

## 2. Bảng chạy tay trên số liệu mẫu| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `12 18` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | gcd(12, 18) = 6 và lcm(12, 18) = (12 * 18) / 6 = 36. Kết quả in ra: 6 36.... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `6 36` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* gcd(12, 18) = 6 và lcm(12, 18) = (12 * 18) / 6 = 36. Kết quả in ra: 6 36.

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

long long getGcd(long long a, long long b) {
while (b != 0) {
long long r = a % b;
a = b;
b = r;
}
return a;
}

int main() {
ios::sync_with_stdio(false);
cin.tie(nullptr);

long long a, b;
if (!(cin >> a >> b)) return 0;

long long g = getGcd(a, b);
long long l = (a / g) * b;

cout << g << " " << l << "\n";
return 0;
}
```
