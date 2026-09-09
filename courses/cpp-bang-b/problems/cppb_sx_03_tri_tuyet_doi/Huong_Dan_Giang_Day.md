# Hướng Dẫn Giảng Dạy: Sắp Xếp Theo Trị Tuyệt Đối
Chuyên đề: **Bài 01: Thuật toán sắp xếp**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho một dãy gồm $N$ số nguyên $A_1, A_2, \dots, A_N$. Hãy sắp xếp các phần tử theo giá trị tuyệt đối tăng dần. Nếu hai phần tử có cùng giá trị tuyệt đối, phần tử mang dấu âm phải đứng trước phần tử mang dấu dương.

---

## 2. Bảng chạy tay trên số liệu mẫu| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `5 5 -8 2 -3 8` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | Xét dãy số ban đầu: $5, -8, 2, -3, 8$. - Giá trị tuyệt đối của các phần tử lần lượt là: $|5| = 5$, $|-8| = 8$, $|2| = 2$... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `2 -3 5 -8 8` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* Xét dãy số ban đầu: $5, -8, 2, -3, 8$.

- Giá trị tuyệt đối của các phần tử lần lượt là: $|5| = 5$, $|-8| = 8$, $|2| = 2$, $|-3| = 3$, $|8| = 8$.
- Sắp xếp theo thứ tự độ lớn tăng dần:
- $|2| = 2 \implies 2$ đứng đầu.
- $|-3| = 3 \implies -3$ đứng tiếp theo.
- $|5| = 5 \implies 5$ đứng tiếp theo.
- Với hai phần tử có độ lớn bằng nhau là $-8$ và $8$ (cùng có trị tuyệt đối là $8$): theo quy tắc ưu tiên, số âm $-8$ phải đứng trước số dương $8$.
Kết quả thu được: `2 -3 5 -8 8`.

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

bool cmp(long long u, long long v) {
if (abs(u) != abs(v)) return abs(u) < abs(v);
return u < v;
}

int main() {
ios::sync_with_stdio(false);
cin.tie(nullptr);

int n;
if (!(cin >> n)) return 0;

vector<long long> a(n);
for (int i = 0; i < n; ++i) cin >> a[i];

sort(a.begin(), a.end(), cmp);

for (int i = 0; i < n; ++i) {
cout << a[i] << (i == n - 1 "" : " ");
}
cout << "\n";
return 0;
}
```
