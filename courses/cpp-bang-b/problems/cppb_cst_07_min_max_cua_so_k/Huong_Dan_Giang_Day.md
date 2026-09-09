# Hướng Dẫn Giảng Dạy: Tìm Min Trong Mọi Cửa Sổ Độ Dài K
Chuyên đề: **Bài 03: Kỹ thuật cửa sổ trượt**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho mảng gồm N số nguyên và số nguyên K. Với mỗi cửa sổ gồm K phần tử liên tiếp từ trái sang phải, hãy tìm giá trị nhỏ nhất trong cửa sổ đó.

---

## 2. Bảng chạy tay trên số liệu mẫu| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `6 3 4 2 12 3 5 1` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | Các cửa sổ độ dài K = 3 gồm: [4, 2, 12] có min = 2; [2, 12, 3] có min = 2; [12, 3, 5] có min = 3; [3, 5, 1] có min = 1. ... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `2 2 3 1` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* Các cửa sổ độ dài K = 3 gồm: [4, 2, 12] có min = 2; [2, 12, 3] có min = 2; [12, 3, 5] có min = 3; [3, 5, 1] có min = 1. Kết quả in ra lần lượt là: 2 2 3 1.

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

int n, k;
if (!(cin >> n >> k)) return 0;

vector<long long> a(n);
for (int i = 0; i < n; ++i) cin >> a[i];

for (int i = 0; i <= n - k; ++i) {
long long cur_min = a[i];
for (int j = i + 1; j < i + k; ++j) {
cur_min = min(cur_min, a[j]);
}
cout << cur_min << (i == n - k "" : " ");
}
cout << "\n";
return 0;
}
```
