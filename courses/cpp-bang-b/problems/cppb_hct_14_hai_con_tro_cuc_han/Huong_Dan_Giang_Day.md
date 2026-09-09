# Hướng Dẫn Giảng Dạy: Cặp Số Tối Ưu Với Chênh Lệch Cực Hạn
Chuyên đề: **Bài 02: Kỹ thuật hai con trỏ**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho 2 dãy số nguyên A gồm N phần tử và B gồm M phần tử. Hãy tìm một phần tử A[i] và một phần tử B[j] sao cho độ chênh lệch |A[i] - B[j]| là nhỏ nhất có thể.

---

## 2. Bảng chạy tay trên số liệu mẫu| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `3 3 1 5 10 2 8 14` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | Dãy A = [1, 5, 10] và dãy B = [2, 8, 14]. So sánh các cặp phần tử: chọn A[0] = 1 và B[0] = 2 cho độ chênh lệch |1 - 2| =... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `1` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* Dãy A = [1, 5, 10] và dãy B = [2, 8, 14]. So sánh các cặp phần tử: chọn A[0] = 1 và B[0] = 2 cho độ chênh lệch |1 - 2| = 1. Đây là mức chênh lệch nhỏ nhất có thể đạt được giữa hai dãy.

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

int n, m;
if (!(cin >> n >> m)) return 0;

vector<long long> a(n), b(m);
for (int i = 0; i < n; ++i) cin >> a[i];
for (int i = 0; i < m; ++i) cin >> b[i];

sort(a.begin(), a.end());
sort(b.begin(), b.end());

int i = 0, j = 0;
long long min_diff = abs(a[0] - b[0]);

while (i < n && j < m) {
min_diff = min(min_diff, abs(a[i] - b[j]));
if (a[i] == b[j]) break;
else if (a[i] < b[j]) ++i;
else ++j;
}

cout << min_diff << "\n";
return 0;
}
```
