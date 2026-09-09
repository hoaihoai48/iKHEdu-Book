# Hướng Dẫn Giảng Dạy: Truy Vấn Tổng Đoạn Con 1D
Chuyên đề: **Bài 04: Mảng tiền tố & mảng hiệu**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho dãy số nguyên gồm N phần tử. Với mỗi truy vấn [L, R] (1 <= L <= R <= N), hãy tính và in ra tổng các phần tử từ chỉ số L đến chỉ số R bằng kỹ thuật Mảng tiền tố.

- **Phương pháp tiếp cận — Mảng tiền tố & Mảng hiệu:**
- Dựng mảng cộng dồn `pref[i] = pref[i-1] + a[i]`. Khi đó tổng đoạn $[L, R]$ được tính tức thì bằng `pref[R] - pref[L-1]` trong $\mathcal{O}(1)$.
- Với các thao tác cộng dồn đoạn, sử dụng mảng hiệu `diff[L] += V, diff[R+1] -= V` rồi cộng dồn để phục hồi mảng.

---

## 2. Bảng chạy tay trên số liệu mẫu| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `5 3 1 2 3 4 5 1 3 2 4 1 5` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | Mảng tiền tố Pref = [0, 1, 3, 6, 10, 15]. - Truy vấn [1, 3]: Pref[3] - Pref[0] = 6 - 0 = 6. - Truy vấn [2, 4]: Pref[4] -... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `6 9 15` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* Mảng tiền tố Pref = [0, 1, 3, 6, 10, 15].

- Truy vấn [1, 3]: Pref[3] - Pref[0] = 6 - 0 = 6.
- Truy vấn [2, 4]: Pref[4] - Pref[1] = 10 - 1 = 9.
- Truy vấn [1, 5]: Pref[5] - Pref[0] = 15 - 0 = 15.

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

vector<long long> p(n + 1, 0);
for (int i = 1; i <= n; ++i) {
long long x;
cin >> x;
p[i] = p[i - 1] + x;
}

while (q--) {
int l, r;
cin >> l >> r;
cout << p[r] - p[l - 1] << "\n";
}

return 0;
}
```
