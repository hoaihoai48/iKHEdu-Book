# Hướng Dẫn Giảng Dạy: Tập Con Có Tổng Bằng S (Subset Sum)
Chuyên đề: **Bài 12: Thuật toán quay lui & nhánh cận**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho mảng số nguyên dương $A$ gồm $N$ phần tử và số nguyên dương $S$. Hãy sử dụng thuật toán Quay lui kết hợp cắt tỉa khả thi (dừng nhánh khi tổng tích lũy vượt quá $S$) để tìm và in ra tất cả các tập con có tổng bằng đúng $S$ theo thứ tự từ điển. Nếu không có phương án nào thỏa mãn, in ra `-1`.

- **Phương pháp tiếp cận — Quay lui & Nhánh cận (Backtracking):**
- Xây dựng không gian trạng thái dạng cây tìm kiếm.
- Thử từng khả năng, nếu vi phạm điều kiện ràng buộc thì tỉa nhánh sớm (nhánh cận) để giảm số trạng thái cần duyệt.

---

## 2. Bảng chạy tay trên số liệu mẫu| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `4 6 1 2 3 5` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | Với kho vàng gồm các thỏi $[1, 2, 3, 5]$ và mục tiêu $S = 6$, có 2 phương án chọn: - Phương án 1: Chọn các thỏi $\{1, 2,... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `1 2 3 1 5` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* Với kho vàng gồm các thỏi $[1, 2, 3, 5]$ và mục tiêu $S = 6$, có 2 phương án chọn:

- Phương án 1: Chọn các thỏi $\{1, 2, 3\}$ vì $1 + 2 + 3 = 6$.
- Phương án 2: Chọn các thỏi $\{1, 5\}$ vì $1 + 5 = 6$.

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
long long S;
vector<long long> a;
vector<long long> cur;
bool found = false;

void backtrack(int idx, long long current_sum) {
if (current_sum == S) {
found = true;
for (int i = 0; i < (int)cur.size(); ++i) cout << cur[i] << (i + 1 == (int)cur.size() "" : " ");
cout << "\n";
return;
}
if (idx >= n || current_sum > S) return;

for (int i = idx; i < n; ++i) {
if (current_sum + a[i] <= S) {
cur.push_back(a[i]);
backtrack(i + 1, current_sum + a[i]);
cur.pop_back();
}
}
}

int main() {
ios::sync_with_stdio(false);
cin.tie(nullptr);
if (!(cin >> n >> S)) return 0;
a.resize(n);
for (int i = 0; i < n; ++i) cin >> a[i];
sort(a.begin(), a.end());
backtrack(0, 0);
if (!found) cout << -1 << "\n";
return 0;
}
```
