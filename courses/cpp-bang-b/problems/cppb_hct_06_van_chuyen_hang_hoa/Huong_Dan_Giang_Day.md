# Hướng Dẫn Giảng Dạy: Vận Chuyển Thùng Hàng Cực Đại
Chuyên đề: **Bài 02: Kỹ thuật hai con trỏ**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho khối lượng N kiện hàng và tải trọng C của xe đầu kéo. Mỗi chuyến xe chở tối đa 2 kiện hàng và tổng khối lượng không quá C. Hãy tính số chuyến xe ít nhất cần dùng để vận chuyển toàn bộ N kiện hàng.

---

## 2. Bảng chạy tay trên số liệu mẫu| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `5 10 3 5 8 2 7` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | Sắp xếp khối lượng 5 kiện hàng tăng dần: [2, 3, 5, 7, 8] với tải trọng C = 10. Chiến thuật ghép con trỏ hai đầu: kiện nặ... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `3` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* Sắp xếp khối lượng 5 kiện hàng tăng dần: [2, 3, 5, 7, 8] với tải trọng C = 10. Chiến thuật ghép con trỏ hai đầu: kiện nặng nhất 8 ghép với nhẹ nhất 2 (8 + 2 = 10 <= 10 -> Chuyến 1); kiện nặng tiếp theo 7 ghép với nhẹ tiếp theo 3 (7 + 3 = 10 <= 10 -> Chuyến 2); kiện còn lại 5 đi riêng một xe (Chuyến 3). Tổng cộng cần 3 chuyến xe.

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
long long c;
if (!(cin >> n >> c)) return 0;

vector<long long> w(n);
for (int i = 0; i < n; ++i) cin >> w[i];

sort(w.begin(), w.end());

int l = 0, r = n - 1;
int trips = 0;

while (l <= r) {
if (l == r) {
++trips;
break;
}
if (w[l] + w[r] <= c) {
++l;
--r;
} else {
--r;
}
++trips;
}

cout << trips << "\n";
return 0;
}
```
