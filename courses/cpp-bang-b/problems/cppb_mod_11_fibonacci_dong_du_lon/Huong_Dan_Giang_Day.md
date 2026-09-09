# Hướng Dẫn Giảng Dạy: Dãy Fibonacci Đồng Dư Lớn
Chuyên đề: **Bài 08: Đồng dư thức, lũy thừa nhị phân & nghịch đảo modulo**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho số nguyên dương N (1 <= N <= 10^18). Hãy tìm số Fibonacci thứ N (với F(1) = 1, F(2) = 1, F(3) = 2, ...) theo modulo 10^9 + 7.

- **Phương pháp tiếp cận — Đại số Modular & Lũy thừa nhị phân:**
- Áp dụng các tính chất $(A + B) \pmod M$, $(A \times B) \pmod M$ ở mọi bước tính.
- Lũy thừa nhị phân tính $A^B \pmod M$ trong $\mathcal{O}(\log B)$ và nghịch đảo modulo qua định lý Fermat nhỏ.

---

## 2. Bảng chạy tay trên số liệu mẫu| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `6` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | Dãy số Fibonacci: F(1)=1, F(2)=1, F(3)=2, F(4)=3, F(5)=5, F(6)=8. Kết quả in ra: 8.... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `8` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* Dãy số Fibonacci: F(1)=1, F(2)=1, F(3)=2, F(4)=3, F(5)=5, F(6)=8. Kết quả in ra: 8.

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

const long long MOD = 1000000007;

void multiply(long long F[2][2], long long M[2][2]) {
long long x = (F[0][0] * M[0][0] + F[0][1] * M[1][0]) % MOD;
long long y = (F[0][0] * M[0][1] + F[0][1] * M[1][1]) % MOD;
long long z = (F[1][0] * M[0][0] + F[1][0] * M[1][0]) % MOD;
long long w = (F[1][0] * M[0][1] + F[1][1] * M[1][1]) % MOD;
F[0][0] = x; F[0][1] = y;
F[1][0] = z; F[1][1] = w;
}

void powerMat(long long F[2][2], long long n) {
if (n == 0 || n == 1) return;
long long M[2][2] = {{1, 1}, {1, 0}};
powerMat(F, n / 2);
multiply(F, F);
if (n % 2 != 0) multiply(F, M);
}

long long fib(long long n) {
if (n == 0) return 0;
long long F[2][2] = {{1, 1}, {1, 0}};
powerMat(F, n - 1);
return F[0][0];
}

int main() {
ios::sync_with_stdio(false);
cin.tie(nullptr);

long long n;
if (!(cin >> n)) return 0;

cout << fib(n) << "\n";
return 0;
}
```
