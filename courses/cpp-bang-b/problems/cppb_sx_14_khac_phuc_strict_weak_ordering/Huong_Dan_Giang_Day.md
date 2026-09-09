# Hướng Dẫn Giảng Dạy: Sắp Xếp Đoạn Thẳng Không Giao Lỗi
Chuyên đề: **Bài 01: Thuật toán sắp xếp**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho danh sách $N$ đoạn thẳng $[L_i, R_i]$ trên trục số. Hãy sắp xếp các đoạn thẳng theo các tiêu chí sau:
1. Tọa độ đầu mút bắt đầu $L_i$ tăng dần.
2. Nếu cùng tọa độ $L_i$, tọa độ mút kết thúc $R_i$ giảm dần.
3. Nếu trùng cả $L_i$ và $R_i$, giữ nguyên thứ tự ban đầu xuất hiện trong dữ liệu vào.

---

## 2. Bảng chạy tay trên số liệu mẫu| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `3 2 8 1 5 2 10` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | Danh sách 3 đoạn thẳng ban đầu là: $[2, 8]$, $[1, 5]$, $[2, 10]$. - Xét điểm đầu mút $L$: đoạn $[1, 5]$ có $L = 1$ nhỏ n... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `1 5 2 10 2 8` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* Danh sách 3 đoạn thẳng ban đầu là: $[2, 8]$, $[1, 5]$, $[2, 10]$.

- Xét điểm đầu mút $L$: đoạn $[1, 5]$ có $L = 1$ nhỏ nhất nên đứng đầu tiên.
- Hai đoạn còn lại là $[2, 8]$ và $[2, 10]$ đều có cùng $L = 2$:
- Xét điểm kết thúc $R$ giảm dần: đoạn $[2, 10]$ có $R = 10 > 8$ nên đoạn $[2, 10]$ phải đứng trước đoạn $[2, 8]$.

Thứ tự sau khi sắp xếp chuẩn là: `1 5`, tiếp đến `2 10`, và cuối cùng là `2 8`.

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

bool cmp(const vector<long long> &a, const vector<long long> &b) {
if (a[0] != b[0]) return a[0] < b[0];
return a[1] > b[1];
}

int main() {
ios::sync_with_stdio(false);
cin.tie(nullptr);

int n;
if (!(cin >> n)) return 0;

vector<vector<long long>> a(n, vector<long long>(2));
for (int i = 0; i < n; ++i) {
cin >> a[i][0] >> a[i][1];
}

stable_sort(a.begin(), a.end(), cmp);

for (int i = 0; i < n; ++i) {
cout << a[i][0] << " " << a[i][1] << "\n";
}
return 0;
}
```
