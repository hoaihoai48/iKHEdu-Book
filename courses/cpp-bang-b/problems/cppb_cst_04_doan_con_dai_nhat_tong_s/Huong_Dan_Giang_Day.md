# Hướng Dẫn Giảng Dạy: Đoạn Con Dài Nhất Có Tổng Không Quá S
Chuyên đề: **Bài 03: Kỹ thuật cửa sổ trượt**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho dãy gồm N số nguyên không âm và một số nguyên dương S. Hãy tìm độ dài lớn nhất của một đoạn con liên tiếp có tổng không vượt quá S.

---

## 2. Bảng chạy tay trên số liệu mẫu| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `5 10 1 2 3 4 5` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | Đoạn con [1, 2, 3, 4] có tổng 1 + 2 + 3 + 4 = 10 <= 10 và có độ dài bằng 4. Nếu xét cả 5 phần tử thì tổng là 15 > 10. Do... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `4` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* Đoạn con [1, 2, 3, 4] có tổng 1 + 2 + 3 + 4 = 10 <= 10 và có độ dài bằng 4. Nếu xét cả 5 phần tử thì tổng là 15 > 10. Do đó độ dài lớn nhất là 4.

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

int l = 0;
long long cur_sum = 0;
int max_len = 0;

for (int r = 0; r < n; ++r) {
cur_sum += a[r];
while (cur_sum > s) {
cur_sum -= a[l];
++l;
}
max_len = max(max_len, r - l + 1);
}

cout << max_len << "\n";
return 0;
}
```
