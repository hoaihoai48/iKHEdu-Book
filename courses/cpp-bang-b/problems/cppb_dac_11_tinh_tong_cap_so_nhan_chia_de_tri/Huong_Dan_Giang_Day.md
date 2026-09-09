# Hướng Dẫn Giảng Dạy: Tính Tổng Cấp Số Nhân D&C
Chuyên đề: **Bài 11: Kỹ thuật chia để trị**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho 3 số nguyên A, N, M. Hãy tính tổng cấp số nhân S(N) = A^0 + A^1 + ... + A^N mod M bằng chia để trị.

- **Phương pháp tiếp cận — Chia để trị:**
- Chia bài toán kích thước $N$ thành các bài toán con độc lập kích thước $N / 2$.
- Giải quyết bài toán con và gộp kết quả tối ưu.

---

## 2. Bảng chạy tay trên số liệu mẫu| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `2 3 100` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | S(3) = 1 + 2 + 4 + 8 = 15 mod 100 = 15.... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `15` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* S(3) = 1 + 2 + 4 + 8 = 15 mod 100 = 15.

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

long long powerMod(long long a, long long b, long long m) {
long long res = 1 % m;
a %= m;
while (b > 0) {
if (b & 1) res = (res * a) % m;
a = (a * a) % m;
b >>= 1;
}
return res;
}

long long sumGeoDac(long long a, long long n, long long m) {
if (n == 0) return 1 % m;
if (n % 2 == 1) {
long long k = n / 2;
long long half_sum = sumGeoDac(a, k, m);
long long mult = (1 + powerMod(a, k + 1, m)) % m;
return (half_sum * mult) % m;
} else {
long long prev = sumGeoDac(a, n - 1, m);
return (prev + powerMod(a, n, m)) % m;
}
}

int main() {
ios::sync_with_stdio(false);
cin.tie(nullptr);
long long a, n, m;
if (!(cin >> a >> n >> m)) return 0;
cout << sumGeoDac(a, n, m) << "\n";
return 0;
}
```
