# Hướng Dẫn Giảng Dạy: Phân Tích Thừa Số Nguyên Tố
Chuyên đề: **Bài 07: Lý thuyết số & số nguyên tố**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho số nguyên dương N. Hãy phân tích N thành tích các thừa số nguyên tố theo dạng p1^e1 * p2^e2 * ... với p1 < p2 < ...

- **Phương pháp tiếp cận — Lý thuyết số & Số nguyên tố:**
- Tận dụng sàng nguyên tố Eratosthenes cho các truy vấn tiền xử lý $\mathcal{O}(N \log \log N)$ hoặc kiểm tra căn bậc hai $\mathcal{O}(\sqrt{N})$.
- Phân tích thừa số nguyên tố và tính chất ước số để tối ưu hóa bài toán.

---

## 2. Bảng chạy tay trên số liệu mẫu| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `60` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | 60 = 4 * 3 * 5 = 2^2 * 3^1 * 5^1. Kết quả in ra: `2^2 * 3^1 * 5^1`.... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `2^2 * 3^1 * 5^1` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* 60 = 4 * 3 * 5 = 2^2 * 3^1 * 5^1. Kết quả in ra: `2^2 * 3^1 * 5^1`.

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

long long n;
if (!(cin >> n)) return 0;

vector<pair<long long, int>> factors;
for (long long i = 2; i * i <= n; ++i) {
if (n % i == 0) {
int cnt = 0;
while (n % i == 0) {
cnt++;
n /= i;
}
factors.push_back({i, cnt});
}
}
if (n > 1) {
factors.push_back({n, 1});
}

for (int i = 0; i < (int)factors.size(); ++i) {
cout << factors[i].first << "^" << factors[i].second;
if (i + 1 < (int)factors.size()) cout << " * ";
}
cout << "\n";
return 0;
}
```
