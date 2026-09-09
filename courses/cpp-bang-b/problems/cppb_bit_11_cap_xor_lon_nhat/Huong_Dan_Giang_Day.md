# Hướng Dẫn Giảng Dạy: Tìm Cặp Có XOR Lớn Nhất Trong Mảng
Chuyên đề: **Bài 06: Phép toán BIT & biểu diễn trạng thái**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho mảng N số nguyên không âm. Hãy tìm giá trị lớn nhất của biểu thức A[i] ^ A[j] với 1 <= i < j <= N.

- **Phương pháp tiếp cận — Phép toán BIT & Bitmask:**
- Biểu diễn tập hợp hoặc trạng thái bật/tắt bằng các bit của số nguyên 64-bit.
- Sử dụng các toán tử bitwise `&, |, ^, ~, <<, >>` để thao tác đồng thời trong $\mathcal{O}(1)$ chu kỳ máy.

---

## 2. Bảng chạy tay trên số liệu mẫu| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `4 3 10 5 25` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | Cặp (5, 25) có 5 ^ 25 = 00101_2 ^ 11001_2 = 11100_2 = 28. Đây là giá trị XOR lớn nhất giữa 2 phần tử bất kỳ trong mảng.... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `28` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* Cặp (5, 25) có 5 ^ 25 = 00101_2 ^ 11001_2 = 11100_2 = 28. Đây là giá trị XOR lớn nhất giữa 2 phần tử bất kỳ trong mảng.

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
if (!(cin >> n)) return 0;

vector<long long> a(n);
for (int i = 0; i < n; ++i) {
cin >> a[i];
}

long long max_xor = 0;
long long mask = 0;

for (int bit = 30; bit >= 0; --bit) {
mask |= (1LL << bit);
vector<long long> prefixes;
prefixes.reserve(n);
for (long long x : a) {
prefixes.push_back(x & mask);
}
sort(prefixes.begin(), prefixes.end());
prefixes.erase(unique(prefixes.begin(), prefixes.end()), prefixes.end());

long long candidate = max_xor | (1LL << bit);
bool found = false;

for (long long p : prefixes) {
long long target = p ^ candidate;
if (binary_search(prefixes.begin(), prefixes.end(), target)) {
found = true;
break;
}
}

if (found) {
max_xor = candidate;
}
}

cout << max_xor << "\n";
return 0;
}
```
