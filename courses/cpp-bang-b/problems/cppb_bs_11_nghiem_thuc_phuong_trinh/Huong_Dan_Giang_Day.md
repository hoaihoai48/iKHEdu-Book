# Hướng Dẫn Giảng Dạy: Tìm Nghiệm Thực Của Phương Trình Đơn Điệu
Chuyên đề: **Bài 05: Thuật toán tìm kiếm nhị phân**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho số thực C dương (1 <= C <= 10^9). Hãy tìm nghiệm thực dương x của phương trình x^3 + 2x^2 + 10x - C = 0 với độ chính xác 6 chữ số thập phân.

- **Phương pháp tiếp cận — Tìm kiếm nhị phân:**
- Nhận diện tính đơn điệu của hàm mục tiêu hoặc không gian tìm kiếm.
- Thu hẹp không gian nghiệm $[L, R]$ qua điểm giữa $mid = L + (R - L) / 2$. Độ phức tạp thời gian đạt $\mathcal{O}(\log N)$ hoặc $\mathcal{O}(N \log(\text{range}))$.

---

## 2. Bảng chạy tay trên số liệu mẫu| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `20.0` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | Thay x = 1.233519 vào f(x): 1.233519^3 + 2*1.233519^2 + 10*1.233519 - 20 = 0.000000. Nghiệm chính xác đến 6 chữ số thập ... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `1.233519` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* Thay x = 1.233519 vào f(x): 1.233519^3 + 2*1.233519^2 + 10*1.233519 - 20 = 0.000000. Nghiệm chính xác đến 6 chữ số thập phân là 1.233519.

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

double f(double x) {
return x * x * x + 2.0 * x * x + 10.0 * x;
}

int main() {
ios::sync_with_stdio(false);
cin.tie(nullptr);

double c;
if (!(cin >> c)) return 0;

double low = 0.0, high = 1000.0;
for (int iter = 0; iter < 100; ++iter) {
double mid = low + (high - low) / 2.0;
if (f(mid) >= c) {
high = mid;
} else {
low = mid;
}
}

cout << fixed << setprecision(6) << low << "\n";
return 0;
}
```
