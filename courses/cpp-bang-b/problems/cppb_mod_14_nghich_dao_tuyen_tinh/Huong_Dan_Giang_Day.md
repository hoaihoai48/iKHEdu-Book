# Hướng Dẫn Giảng Dạy: Nghịch Đảo Tuyến Tính 1..N Trong O(N)
Chuyên đề: **Bài 08: Đồng dư thức, lũy thừa nhị phân & nghịch đảo modulo**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho số nguyên N và M = 10^9 + 7. Hãy tính và in ra nghịch đảo modulo của tất cả các số từ 1 đến N theo modulo M trong thời gian O(N).

- **Phương pháp tiếp cận — Đại số Modular & Lũy thừa nhị phân:**
- Áp dụng các tính chất $(A + B) \pmod M$, $(A \times B) \pmod M$ ở mọi bước tính.
- Lũy thừa nhị phân tính $A^B \pmod M$ trong $\mathcal{O}(\log B)$ và nghịch đảo modulo qua định lý Fermat nhỏ.

---

## 2. Bảng chạy tay trên số liệu mẫu| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `3` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | - inv(1) = 1. - inv(2) = 500000004 (vì 2 * 500000004 = 1 mod M). - inv(3) = 333333336 (vì 3 * 333333336 = 1000000008 = 1... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `1 500000004 333333336` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* - inv(1) = 1.

- inv(2) = 500000004 (vì 2 * 500000004 = 1 mod M).
- inv(3) = 333333336 (vì 3 * 333333336 = 1000000008 = 1 mod M).

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

int main() {
ios::sync_with_stdio(false);
cin.tie(nullptr);

int n;
if (!(cin >> n)) return 0;

vector<long long> inv(n + 1);
inv[1] = 1;
long long sum_inv = 1;

for (int i = 2; i <= n; ++i) {
inv[i] = (MOD - (MOD / i) * inv[MOD % i] % MOD) % MOD;
sum_inv = (sum_inv + inv[i]) % MOD;
}

cout << sum_inv << "\n";
return 0;
}
```
