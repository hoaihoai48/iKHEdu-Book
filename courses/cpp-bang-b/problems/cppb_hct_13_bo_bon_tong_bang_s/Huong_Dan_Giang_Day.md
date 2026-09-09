# Hướng Dẫn Giảng Dạy: Bộ Bốn Số Có Tổng Bằng S (4-Sum)
Chuyên đề: **Bài 02: Kỹ thuật hai con trỏ**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho mảng gồm N số nguyên và số nguyên S. Hãy tìm 4 phần tử ở 4 vị trí phân biệt có tổng đúng bằng S. Nếu có nhiều bộ, in ra một bộ theo thứ tự tăng dần. Nếu không tồn tại, in ra -1.

---

## 2. Bảng chạy tay trên số liệu mẫu| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `6 20 2 7 5 1 8 4` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | Sắp xếp mảng tăng dần: [1, 2, 4, 5, 7, 8] và S = 20. Bộ bốn số gồm các phần tử 1, 4, 7, 8 có tổng là 1 + 4 + 7 + 8 = 20 ... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `1 4 7 8` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* Sắp xếp mảng tăng dần: [1, 2, 4, 5, 7, 8] và S = 20. Bộ bốn số gồm các phần tử 1, 4, 7, 8 có tổng là 1 + 4 + 7 + 8 = 20 đúng bằng S. Kết quả in ra: 1 4 7 8.

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

for (int i = 0; i < n - 3; ++i) {
for (int j = i + 1; j < n - 2; ++j) {
long long target = s - a[i] - a[j];
int l = j + 1, r = n - 1;
while (l < r) {
long long sum = a[l] + a[r];
if (sum == target) {
cout << a[i] << " " << a[j] << " " << a[l] << " " << a[r] << "\n";
return 0;
} else if (sum < target) {
++l;
} else {
--r;
}
}
}
}

cout << -1 << "\n";
return 0;
}
```
