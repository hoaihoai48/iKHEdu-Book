# Hướng Dẫn Giảng Dạy: Sinh Dãy Ngoặc Hợp Lệ Độ Dài 2N
Chuyên đề: **Bài 12: Thuật toán quay lui & nhánh cận**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho số nguyên dương $N$. Hãy áp dụng thuật toán Quay lui có kỹ thuật cắt tỉa điều kiện hợp lệ (`open < N` và `close < open`) để sinh và in ra tất cả các dãy ngoặc đúng gồm $N$ cặp ngoặc tròn `()` theo thứ tự từ điển (`(` đứng trước `)`).

- **Phương pháp tiếp cận — Quay lui & Nhánh cận (Backtracking):**
- Xây dựng không gian trạng thái dạng cây tìm kiếm.
- Thử từng khả năng, nếu vi phạm điều kiện ràng buộc thì tỉa nhánh sớm (nhánh cận) để giảm số trạng thái cần duyệt.

---

## 2. Bảng chạy tay trên số liệu mẫu| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `3` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | Với $N = 3$ cặp ngoặc (độ dài 6 ký tự), số lượng dãy ngoặc hợp lệ chính là số Catalan $C_3 = \frac{1}{4} \binom{6}{3} = ... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `((())) (()()) (())() ()(()) ()()()` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* Với $N = 3$ cặp ngoặc (độ dài 6 ký tự), số lượng dãy ngoặc hợp lệ chính là số Catalan $C_3 = \frac{1}{4} \binom{6}{3} = 5$. Các cấu hình hợp lệ được liệt kê theo thứ tự từ điển chuẩn mực.

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

int n;
string cur = "";

void backtrack(int open_cnt, int close_cnt) {
if (open_cnt == n && close_cnt == n) {
cout << cur << "\n";
return;
}
if (open_cnt < n) {
cur.push_back('(');
backtrack(open_cnt + 1, close_cnt);
cur.pop_back();
}
if (close_cnt < open_cnt) {
cur.push_back(')');
backtrack(open_cnt, close_cnt + 1);
cur.pop_back();
}
}

int main() {
ios::sync_with_stdio(false);
cin.tie(nullptr);
if (!(cin >> n)) return 0;
backtrack(0, 0);
return 0;
}
```
