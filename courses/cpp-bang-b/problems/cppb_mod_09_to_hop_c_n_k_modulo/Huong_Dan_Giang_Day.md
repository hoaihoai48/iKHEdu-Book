# Hướng Dẫn Giảng Dạy: Tính Số Tổ Hợp C(N, K) mod M
Chuyên đề: **Bài 08: Đồng dư thức, lũy thừa nhị phân & nghịch đảo modulo**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho Q truy vấn, mỗi truy vấn chứa 2 số N và K. Hãy tính C(N, K) mod (10^9 + 7) bằng phương pháp tiền xử lý giai thừa và nghịch đảo giai thừa.

- **Phương pháp tiếp cận — Đại số Modular & Lũy thừa nhị phân:**
- Áp dụng các tính chất $(A + B) \pmod M$, $(A \times B) \pmod M$ ở mọi bước tính.
- Lũy thừa nhị phân tính $A^B \pmod M$ trong $\mathcal{O}(\log B)$ và nghịch đảo modulo qua định lý Fermat nhỏ.

---

## 2. Bảng chạy tay trên số liệu mẫu| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `2 5 2 10 3` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | - C(5, 2) = 5! / (2! * 3!) = 10. - C(10, 3) = 10! / (3! * 7!) = 120.... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `10 120` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* - C(5, 2) = 5! / (2! * 3!) = 10.

- C(10, 3) = 10! / (3! * 7!) = 120.

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
const long long MOD = 1000000007;

vector<long long> fact(MAXN + 1);
vector<long long> invFact(MAXN + 1);

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

void precompute() {
fact[0] = 1;
for (int i = 1; i <= MAXN; ++i) fact[i] = (fact[i - 1] * i) % MOD;
invFact[MAXN] = powerMod(fact[MAXN], MOD - 2);
for (int i = MAXN; i >= 1; --i) invFact[i - 1] = (invFact[i] * i) % MOD;
}

int main() {
ios::sync_with_stdio(false);
cin.tie(nullptr);

precompute();

int q;
if (!(cin >> q)) return 0;

while (q--) {
int n, k;
cin >> n >> k;
if (k < 0 || k > n) cout << 0 << "\n";
else cout << fact[n] * invFact[k] % MOD * invFact[n - k] % MOD << "\n";
}
return 0;
}
```
