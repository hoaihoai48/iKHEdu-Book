# Hướng Dẫn Giảng Dạy: Tính Tổng Cấp Số Nhân Đồng Dư
Chuyên đề: **Bài 08: Đồng dư thức, lũy thừa nhị phân & nghịch đảo modulo**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho A, N và M = 10^9 + 7. Hãy tính tổng S = 1 + A + A^2 + ... + A^N mod M.

- **Phương pháp tiếp cận — Đại số Modular & Lũy thừa nhị phân:**
- Áp dụng các tính chất $(A + B) \pmod M$, $(A \times B) \pmod M$ ở mọi bước tính.
- Lũy thừa nhị phân tính $A^B \pmod M$ trong $\mathcal{O}(\log B)$ và nghịch đảo modulo qua định lý Fermat nhỏ.

---

## 2. Bảng chạy tay trên số liệu mẫu| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `2 3` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | S = 1 + 2 + 2^2 + 2^3 = 1 + 2 + 4 + 8 = 15. Kết quả in ra: 15.... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `15` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* S = 1 + 2 + 2^2 + 2^3 = 1 + 2 + 4 + 8 = 15. Kết quả in ra: 15.

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

long long powerMod(long long a, long long b) {
long long ans = 1;
a %= MOD;
while (b > 0) {
if (b & 1) ans = (ans * a) % MOD;
a = (a * a) % MOD;
b >>= 1;
}
return ans;
}

long long sumGeo(long long a, long long k) {
if (k == 0) return 0;
if (k == 1) return 1;
if (k % 2 == 0) {
long long half = sumGeo(a, k / 2);
return half * (1 + powerMod(a, k / 2)) % MOD;
} else {
return (1 + a * sumGeo(a, k - 1)) % MOD;
}
}

int main() {
ios::sync_with_stdio(false);
cin.tie(nullptr);

long long a, n;
if (!(cin >> a >> n)) return 0;

cout << sumGeo(a, n + 1) << "\n";
return 0;
}
```
