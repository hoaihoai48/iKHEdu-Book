# Hướng Dẫn Giảng Dạy: Tìm Cặp Có Hiệu Đúng Bằng K
Chuyên đề: **Bài 02: Kỹ thuật hai con trỏ**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho mảng gồm N số nguyên và số nguyên không âm K. Hãy kiểm tra xem có tồn tại cặp chỉ số (i, j) với i != j sao cho A[j] - A[i] = K hay không. Nếu có in ra YES, ngược lại in ra NO.

---

## 2. Bảng chạy tay trên số liệu mẫu| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `5 3 1 8 5 3 2` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | Sắp xếp mảng tăng dần: [1, 2, 3, 5, 8] với K = 3. Sử dụng hai con trỏ cùng chiều: cặp số (2, 5) có hiệu 5 - 2 = 3 = K ho... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `YES` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* Sắp xếp mảng tăng dần: [1, 2, 3, 5, 8] với K = 3. Sử dụng hai con trỏ cùng chiều: cặp số (2, 5) có hiệu 5 - 2 = 3 = K hoặc cặp (5, 8) có hiệu 8 - 5 = 3 = K. Vì tồn tại ít nhất một cặp thỏa mãn nên kết quả in ra là YES.

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

sort(a.begin(), a.end());

int l = 0, r = 1;
bool found = false;

while (r < n) {
if (l == r) {
++r;
continue;
}
long long diff = a[r] - a[l];
if (diff == k) {
found = true;
break;
} else if (diff < k) {
++r;
} else {
++l;
}
}

if (found) cout << "YES\n";
else cout << "NO\n";
return 0;
}
```
