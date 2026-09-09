# Hướng Dẫn Giảng Dạy: Đoạn Con Có Độ Chênh Lệch Max - Min Không Quá K
Chuyên đề: **Bài 03: Kỹ thuật cửa sổ trượt**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho mảng gồm N số nguyên và số nguyên không âm K. Hãy tìm độ dài lớn nhất của đoạn con liên tiếp sao cho chênh lệch giữa phần tử lớn nhất và phần tử nhỏ nhất trong đoạn không vượt quá K: max(đoạn) - min(đoạn) <= K.

---

## 2. Bảng chạy tay trên số liệu mẫu| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `6 2 1 3 6 7 9 4` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | Với dung sai K = 2, các đoạn con liên tiếp có chênh lệch max - min <= 2 là [1, 3] (3 - 1 = 2) hoặc [6, 7] (7 - 6 = 1). Đ... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `2` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* Với dung sai K = 2, các đoạn con liên tiếp có chênh lệch max - min <= 2 là [1, 3] (3 - 1 = 2) hoặc [6, 7] (7 - 6 = 1). Độ dài lớn nhất của đoạn con hợp lệ là 2.

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
long long k;
if (!(cin >> n >> k)) return 0;

vector<long long> a(n);
for (int i = 0; i < n; ++i) cin >> a[i];

int max_len = 0;

for (int l = 0; l < n; ++l) {
long long cur_min = a[l], cur_max = a[l];
for (int r = l; r < n; ++r) {
cur_min = min(cur_min, a[r]);
cur_max = max(cur_max, a[r]);
if (cur_max - cur_min <= k) {
max_len = max(max_len, r - l + 1);
} else {
break;
}
}
}

cout << max_len << "\n";
return 0;
}
```
