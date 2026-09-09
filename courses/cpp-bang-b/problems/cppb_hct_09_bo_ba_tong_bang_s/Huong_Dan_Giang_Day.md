# Hướng Dẫn Giảng Dạy: Bộ Ba Số Có Tổng Bằng S (3-Sum)
Chuyên đề: **Bài 02: Kỹ thuật hai con trỏ**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho mảng gồm N số nguyên và một số nguyên S. Hãy tìm 3 phần tử ở 3 vị trí phân biệt trong mảng có tổng đúng bằng S. Nếu có nhiều bộ, in ra một bộ bất kỳ theo thứ tự tăng dần. Nếu không tồn tại, in ra -1.

---

## 2. Bảng chạy tay trên số liệu mẫu| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `6 15 2 7 5 1 8 4` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | Sắp xếp mảng tăng dần: [1, 2, 4, 5, 7, 8] với mục tiêu S = 15. Cố định phần tử đầu tiên là 2, ta cần tìm hai phần tử còn... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `2 5 8` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* Sắp xếp mảng tăng dần: [1, 2, 4, 5, 7, 8] với mục tiêu S = 15. Cố định phần tử đầu tiên là 2, ta cần tìm hai phần tử còn lại có tổng là 15 - 2 = 13. Sử dụng hai con trỏ trên đoạn còn lại [4, 5, 7, 8], ta tìm được cặp (5, 8) có 5 + 8 = 13. Do đó bộ ba số tìm được là 2, 5, 8 thỏa mãn 2 + 5 + 8 = 15. Kết quả in ra: 2 5 8.

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

for (int i = 0; i < n - 2; ++i) {
long long target = s - a[i];
int l = i + 1, r = n - 1;
while (l < r) {
long long sum = a[l] + a[r];
if (sum == target) {
cout << a[i] << " " << a[l] << " " << a[r] << "\n";
return 0;
} else if (sum < target) {
++l;
} else {
--r;
}
}
}

cout << -1 << "\n";
return 0;
}
```
