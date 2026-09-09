# Hướng Dẫn Giảng Dạy: Phân Phối Tài Nguyên Không Gian Tuyến Tính
Chuyên đề: **Bài 04: Mảng tiền tố & mảng hiệu**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho dãy số N phần tử ban đầu toàn số 0. Thực hiện Q thao tác cộng vào đoạn [L, R] một dãy cấp số cộng với số hạng đầu V và công sai D. Hãy in ra mảng kết quả cuối cùng.

- **Phương pháp tiếp cận — Mảng tiền tố & Mảng hiệu:**
- Dựng mảng cộng dồn `pref[i] = pref[i-1] + a[i]`. Khi đó tổng đoạn $[L, R]$ được tính tức thì bằng `pref[R] - pref[L-1]` trong $\mathcal{O}(1)$.
- Với các thao tác cộng dồn đoạn, sử dụng mảng hiệu `diff[L] += V, diff[R+1] -= V` rồi cộng dồn để phục hồi mảng.

---

## 2. Bảng chạy tay trên số liệu mẫu| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `5 1 2 4 1 2` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | Thao tác trên đoạn [2, 4] với V = 1, D = 2: vị trí 2 nhận 1; vị trí 3 nhận 1 + 2 = 3; vị trí 4 nhận 1 + 2*2 = 5. Kết quả... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `0 1 3 5 0` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* Thao tác trên đoạn [2, 4] với V = 1, D = 2: vị trí 2 nhận 1; vị trí 3 nhận 1 + 2 = 3; vị trí 4 nhận 1 + 2*2 = 5. Kết quả in ra: 0 1 3 5 0.

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

int n, q;
if (!(cin >> n >> q)) return 0;

vector<long long> d2(n + 3, 0);

while (q--) {
long long l, r, s, d;
cin >> l >> r >> s >> d;
d2[l] += s;
d2[l + 1] += (d - s);
d2[r + 1] -= (s + (r - l + 1) * d);
d2[r + 2] += (s + (r - l) * d);
}

// Lần 1: Khôi phục mảng hiệu bậc 1
vector<long long> d1(n + 2, 0);
for (int i = 1; i <= n + 1; ++i) {
d1[i] = d1[i - 1] + d2[i];
}

// Lần 2: Khôi phục mảng giá trị gốc
vector<long long> a(n + 1, 0);
for (int i = 1; i <= n; ++i) {
a[i] = a[i - 1] + d1[i];
cout << a[i] << (i == n "" : " ");
}
cout << "\n";

return 0;
}
```
