# Hướng Dẫn Giảng Dạy: Đếm Số Lượng Số Chẵn Trong Đoạn
Chuyên đề: **Bài 04: Mảng tiền tố & mảng hiệu**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho dãy gồm N số nguyên. Hãy trả lời Q truy vấn [L, R], mỗi truy vấn yêu cầu đếm xem có bao nhiêu số chẵn trong đoạn từ vị trí L đến R.

- **Phương pháp tiếp cận — Mảng tiền tố & Mảng hiệu:**
- Dựng mảng cộng dồn `pref[i] = pref[i-1] + a[i]`. Khi đó tổng đoạn $[L, R]$ được tính tức thì bằng `pref[R] - pref[L-1]` trong $\mathcal{O}(1)$.
- Với các thao tác cộng dồn đoạn, sử dụng mảng hiệu `diff[L] += V, diff[R+1] -= V` rồi cộng dồn để phục hồi mảng.

---

## 2. Bảng chạy tay trên số liệu mẫu| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `6 3 2 3 4 6 7 8 1 4 2 5 1 6` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | Mảng nhị phân đánh dấu số chẵn: [1, 0, 1, 1, 0, 1]. Mảng tiền tố đếm số chẵn: [0, 1, 1, 2, 3, 3, 4]. - Đoạn [1, 4]: gồm ... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `3 2 4` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* Mảng nhị phân đánh dấu số chẵn: [1, 0, 1, 1, 0, 1]. Mảng tiền tố đếm số chẵn: [0, 1, 1, 2, 3, 3, 4].

- Đoạn [1, 4]: gồm {2, 3, 4, 6} có 3 số chẵn.
- Đoạn [2, 5]: gồm {3, 4, 6, 7} có 2 số chẵn.
- Đoạn [1, 6]: có 4 số chẵn.

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

vector<int> p(n + 1, 0);
for (int i = 1; i <= n; ++i) {
long long x;
cin >> x;
p[i] = p[i - 1] + (abs(x) % 2 == 0 1 : 0);
}

while (q--) {
int l, r;
cin >> l >> r;
cout << p[r] - p[l - 1] << "\n";
}

return 0;
}
```
