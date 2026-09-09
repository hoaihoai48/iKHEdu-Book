# Hướng Dẫn Giảng Dạy: Sinh Tất Cả Hoán Vị 1..N
Chuyên đề: **Bài 12: Thuật toán quay lui & nhánh cận**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho số nguyên dương $N$. Hãy áp dụng thuật toán Quay lui với kỹ thuật đánh dấu mảng `visited[]` để sinh và in ra tất cả các hoán vị của tập hợp $\{1, 2, \dots, N\}$ theo đúng thứ tự từ điển tăng dần.

- **Phương pháp tiếp cận — Quay lui & Nhánh cận (Backtracking):**
- Xây dựng không gian trạng thái dạng cây tìm kiếm.
- Thử từng khả năng, nếu vi phạm điều kiện ràng buộc thì tỉa nhánh sớm (nhánh cận) để giảm số trạng thái cần duyệt.

---

## 2. Bảng chạy tay trên số liệu mẫu| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `3` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | Tập $\{1, 2, 3\}$ có đúng $3! = 6$ hoán vị khác nhau. Hoán vị đầu tiên theo thứ tự từ điển là `1 2 3` và hoán vị cuối cù... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `1 2 3 1 3 2 2 1 3 2 3 1 3 1 2 3 2 1` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* Tập $\{1, 2, 3\}$ có đúng $3! = 6$ hoán vị khác nhau. Hoán vị đầu tiên theo thứ tự từ điển là `1 2 3` và hoán vị cuối cùng là `3 2 1`.

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
vector<int> cur;
vector<bool> visited;

void backtrack(int step) {
if (step > n) {
for (int i = 0; i < n; ++i) cout << cur[i] << (i + 1 == n "" : " ");
cout << "\n";
return;
}
for (int val = 1; val <= n; ++val) {
if (!visited[val]) {
visited[val] = true;
cur.push_back(val);
backtrack(step + 1);
cur.pop_back();
visited[val] = false;
}
}
}

int main() {
ios::sync_with_stdio(false);
cin.tie(nullptr);
if (!(cin >> n)) return 0;
visited.assign(n + 1, false);
backtrack(1);
return 0;
}
```
