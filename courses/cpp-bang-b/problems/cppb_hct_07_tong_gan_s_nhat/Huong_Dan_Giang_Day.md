# Hướng Dẫn Giảng Dạy: Tìm Cặp Có Tổng Gần S Nhất
Chuyên đề: **Bài 02: Kỹ thuật hai con trỏ**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho mảng gồm N số nguyên và một số nguyên S. Hãy tìm một cặp số (A[i], A[j]) với i < j sao cho độ chênh lệch |(A[i] + A[j]) - S| là nhỏ nhất có thể. Nếu có nhiều cặp, in ra cặp có tổng nhỏ hơn theo thứ tự tăng dần.

---

## 2. Bảng chạy tay trên số liệu mẫu| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `5 20 2 8 13 4 25` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | Sắp xếp danh sách điện trở tăng dần: [2, 4, 8, 13, 25] và S = 20. Xét các cặp có tổng gần 20: cặp (8, 13) có tổng 8 + 13... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `8 13` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* Sắp xếp danh sách điện trở tăng dần: [2, 4, 8, 13, 25] và S = 20. Xét các cặp có tổng gần 20: cặp (8, 13) có tổng 8 + 13 = 21 (chênh lệch |21 - 20| = 1); cặp (4, 13) có tổng 17 (chênh lệch |17 - 20| = 3). Cặp có độ chênh lệch nhỏ nhất đạt được là (8, 13) với khoảng cách chênh lệch chỉ là 1. Kết quả in ra: 8 13.

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
long long s;
if (!(cin >> n >> s)) return 0;

vector<long long> a(n);
for (int i = 0; i < n; ++i) cin >> a[i];

sort(a.begin(), a.end());

int l = 0, r = n - 1;
long long best_diff = -1;
long long ans_l = a[0], ans_r = a[1];

while (l < r) {
long long cur_sum = a[l] + a[r];
long long cur_diff = abs(cur_sum - s);

if (best_diff == -1 || cur_diff < best_diff || (cur_diff == best_diff && cur_sum < ans_l + ans_r)) {
best_diff = cur_diff;
ans_l = a[l];
ans_r = a[r];
}

if (cur_sum == s) break;
else if (cur_sum < s) ++l;
else --r;
}

cout << ans_l << " " << ans_r << "\n";
return 0;
}
```
