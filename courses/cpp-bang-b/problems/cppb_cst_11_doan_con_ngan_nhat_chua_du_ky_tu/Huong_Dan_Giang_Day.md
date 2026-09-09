# Hướng Dẫn Giảng Dạy: Đoạn Con Ngắn Nhất Chứa Đủ Mọi Ký Tự Của Tập Hợp
Chuyên đề: **Bài 03: Kỹ thuật cửa sổ trượt**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho chuỗi S gồm các chữ cái in thường và chuỗi mẫu T gồm M ký tự phân biệt. Hãy tìm độ dài nhỏ nhất của một đoạn con liên tiếp trong S chứa đầy đủ toàn bộ các ký tự của chuỗi T. Nếu không tồn tại, in ra -1.

---

## 2. Bảng chạy tay trên số liệu mẫu| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `adobecodebanc abc` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | Chuỗi T = 'abc' yêu cầu phải có đủ 3 ký tự 'a', 'b', 'c'. Đoạn con ngắn nhất trong S chứa đủ cả 3 ký tự này là 'banc' ở ... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `4` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* Chuỗi T = 'abc' yêu cầu phải có đủ 3 ký tự 'a', 'b', 'c'. Đoạn con ngắn nhất trong S chứa đủ cả 3 ký tự này là 'banc' ở cuối chuỗi S, có độ dài bằng 4. Kết quả in ra: 4.

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

string s, t;
cin >> s >> t;

vector<int> need(26, 0);
for (char c : t) need[c - 'a'] = 1;

vector<int> have(26, 0);
int matched = 0;
int l = 0, min_len = n + 1;

for (int r = 0; r < n; ++r) {
int c = s[r] - 'a';
if (need[c]) {
if (have[c] == 0) ++matched;
++have[c];
}

while (matched == m) {
min_len = min(min_len, r - l + 1);
int lc = s[l] - 'a';
if (need[lc]) {
--have[lc];
if (have[lc] == 0) --matched;
}
++l;
}
}

if (min_len > n) cout << -1 << "\n";
else cout << min_len << "\n";
return 0;
}
```
