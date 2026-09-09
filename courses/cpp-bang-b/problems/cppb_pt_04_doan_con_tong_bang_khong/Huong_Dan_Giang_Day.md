# Hướng Dẫn Giảng Dạy: Đoạn Con Có Tổng Bằng 0
Chuyên đề: **Bài 04: Mảng tiền tố & mảng hiệu**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho mảng gồm N số nguyên. Hãy kiểm tra xem có tồn tại ít nhất một đoạn con liên tiếp có tổng đúng bằng 0 hay không. Nếu có in ra YES, ngược lại in ra NO.

- **Phương pháp tiếp cận — Mảng tiền tố & Mảng hiệu:**
- Dựng mảng cộng dồn `pref[i] = pref[i-1] + a[i]`. Khi đó tổng đoạn $[L, R]$ được tính tức thì bằng `pref[R] - pref[L-1]` trong $\mathcal{O}(1)$.
- Với các thao tác cộng dồn đoạn, sử dụng mảng hiệu `diff[L] += V, diff[R+1] -= V` rồi cộng dồn để phục hồi mảng.

---

## 2. Bảng chạy tay trên số liệu mẫu| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `5 4 2 -3 1 6` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | Đoạn con [2, -3, 1] từ vị trí 2 đến vị trí 4 có tổng là 2 + (-3) + 1 = 0. Do đó in ra YES.... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `YES` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* Đoạn con [2, -3, 1] từ vị trí 2 đến vị trí 4 có tổng là 2 + (-3) + 1 = 0. Do đó in ra YES.

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

int n;
if (!(cin >> n)) return 0;

vector<long long> p(n + 1, 0);
for (int i = 1; i <= n; ++i) {
long long x;
cin >> x;
p[i] = p[i - 1] + x;
}

sort(p.begin(), p.end());

for (int i = 1; i <= n; ++i) {
if (p[i] == p[i - 1]) {
cout << "YES\n";
return 0;
}
}

cout << "NO\n";
return 0;
}
```
