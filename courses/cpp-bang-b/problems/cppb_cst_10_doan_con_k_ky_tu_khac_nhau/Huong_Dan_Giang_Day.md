# Hướng Dẫn Giảng Dạy: Đoạn Con Dài Nhất Chứa Tối Đa K Ký Tự Khác Nhau
Chuyên đề: **Bài 03: Kỹ thuật cửa sổ trượt**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho chuỗi ký tự S gồm các chữ cái tiếng Anh in thường và số nguyên dương K. Hãy tìm độ dài lớn nhất của một chuỗi con liên tiếp chứa tối đa K ký tự khác nhau.

---

## 2. Bảng chạy tay trên số liệu mẫu| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `eceba 2` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | Chuỗi con liên tiếp dài nhất chứa tối đa 2 ký tự khác nhau là 'ece' (chỉ chứa 2 ký tự 'e' và 'c') với độ dài bằng 3. Kết... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `3` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* Chuỗi con liên tiếp dài nhất chứa tối đa 2 ký tự khác nhau là 'ece' (chỉ chứa 2 ký tự 'e' và 'c') với độ dài bằng 3. Kết quả in ra: 3.

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

string s;
cin >> s;

vector<int> freq(26, 0);
int distinct = 0;
int l = 0, max_len = 0;

for (int r = 0; r < n; ++r) {
int c = s[r] - 'a';
if (freq[c] == 0) ++distinct;
++freq[c];

while (distinct > k) {
int lc = s[l] - 'a';
--freq[lc];
if (freq[lc] == 0) --distinct;
++l;
}

max_len = max(max_len, r - l + 1);
}

cout << max_len << "\n";
return 0;
}
```
