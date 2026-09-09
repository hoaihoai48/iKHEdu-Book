# Hướng Dẫn Giảng Dạy: Giải Phương Trình Đồng Dư Tuyến Tính Ax = B mod M
Chuyên đề: **Bài 08: Đồng dư thức, lũy thừa nhị phân & nghịch đảo modulo**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho 3 số nguyên A, B, M. Hãy tìm nghiệm nguyên không âm nhỏ nhất X của phương trình Ax = B mod M. Nếu vô nghiệm, in ra -1.

- **Phương pháp tiếp cận — Đại số Modular & Lũy thừa nhị phân:**
- Áp dụng các tính chất $(A + B) \pmod M$, $(A \times B) \pmod M$ ở mọi bước tính.
- Lũy thừa nhị phân tính $A^B \pmod M$ trong $\mathcal{O}(\log B)$ và nghịch đảo modulo qua định lý Fermat nhỏ.

---

## 2. Bảng chạy tay trên số liệu mẫu| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `2 4 6` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | Thay X = 2: 2 * 2 = 4 = 4 mod 6. Nghiệm không âm nhỏ nhất là 2.... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `2` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* Thay X = 2: 2 * 2 = 4 = 4 mod 6. Nghiệm không âm nhỏ nhất là 2.

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

long long extGCD(long long a, long long b, long long &x, long long &y) {
if (b == 0) {
x = 1;
y = 0;
return a;
}
long long x1, y1;
long long d = extGCD(b, a % b, x1, y1);
x = y1;
y = x1 - y1 * (a / b);
return d;
}

int main() {
ios::sync_with_stdio(false);
cin.tie(nullptr);

long long a, b, m;
if (!(cin >> a >> b >> m)) return 0;

long long x, y;
long long g = extGCD(a, m, x, y);

if (b % g != 0) {
cout << -1 << "\n";
return 0;
}

x = (x % m + m) % m;
long long m_prime = m / g;
long long ans = (x * ((b / g) % m_prime)) % m_prime;
ans = (ans % m_prime + m_prime) % m_prime;

cout << ans << "\n";
return 0;
}
```
