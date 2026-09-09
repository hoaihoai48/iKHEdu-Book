# Hướng Dẫn Giảng Dạy: Số Gần Nguyên Tố (Almost Prime)
Chuyên đề: **Bài 07: Lý thuyết số & số nguyên tố**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho số nguyên dương N. Hãy đếm số lượng số nguyên trong đoạn [1, N] có đúng 2 ước số nguyên tố phân biệt.

- **Phương pháp tiếp cận — Lý thuyết số & Số nguyên tố:**
- Tận dụng sàng nguyên tố Eratosthenes cho các truy vấn tiền xử lý $\mathcal{O}(N \log \log N)$ hoặc kiểm tra căn bậc hai $\mathcal{O}(\sqrt{N})$.
- Phân tích thừa số nguyên tố và tính chất ước số để tối ưu hóa bài toán.

---

## 2. Bảng chạy tay trên số liệu mẫu| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `10` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | Trong đoạn [1, 10], các số có đúng 2 ước nguyên tố phân biệt là: 6 (ước 2, 3) và 10 (ước 2, 5). Tổng cộng có 2 số.... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `2` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* Trong đoạn [1, 10], các số có đúng 2 ước nguyên tố phân biệt là: 6 (ước 2, 3) và 10 (ước 2, 5). Tổng cộng có 2 số.

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

vector<int> prime_count(n + 1, 0);
for (int i = 2; i <= n; ++i) {
if (prime_count[i] == 0) { // i là số nguyên tố
for (int j = i; j <= n; j += i) {
prime_count[j]++;
}
}
}

int ans = 0;
for (int i = 1; i <= n; ++i) {
if (prime_count[i] == 2) ans++;
}

cout << ans << "\n";
return 0;
}
```
