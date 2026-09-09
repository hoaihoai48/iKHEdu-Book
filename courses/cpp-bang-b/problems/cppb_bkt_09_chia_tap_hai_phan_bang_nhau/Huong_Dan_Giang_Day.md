# Hướng Dẫn Giảng Dạy: Chia Tập Thành 2 Phần Có Tổng Bằng Nhau
Chuyên đề: **Bài 12: Thuật toán quay lui & nhánh cận**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho mảng số nguyên dương $A$ gồm $N$ phần tử. Hãy xác định xem có thể chia toàn bộ $N$ phần tử thành hai tập con rời nhau sao cho tổng giá trị của hai tập con bằng nhau hay không. Nếu có thể chia được in `YES`, ngược lại in `NO`.

- **Phương pháp tiếp cận — Quay lui & Nhánh cận (Backtracking):**
- Xây dựng không gian trạng thái dạng cây tìm kiếm.
- Thử từng khả năng, nếu vi phạm điều kiện ràng buộc thì tỉa nhánh sớm (nhánh cận) để giảm số trạng thái cần duyệt.

---

## 2. Bảng chạy tay trên số liệu mẫu| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `4 1 5 11 5` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | Tổng khối lượng của tất cả các thùng là $1 + 5 + 11 + 5 = 22$. Nửa tổng là 11. Ta có thể chia thành 2 phần: tập thứ nhất... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `YES` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* Tổng khối lượng của tất cả các thùng là $1 + 5 + 11 + 5 = 22$. Nửa tổng là 11. Ta có thể chia thành 2 phần: tập thứ nhất gồm $\{1, 5, 5\}$ có tổng bằng 11 và tập thứ hai gồm $\{11\}$ có tổng bằng 11. Do đó đáp án là `YES`.

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
long long target;
vector<long long> a;
bool possible = false;

void backtrack(int idx, long long cur_sum) {
if (possible) return;
if (cur_sum == target) {
possible = true;
return;
}
if (idx >= n || cur_sum > target) return;

for (int i = idx; i < n; ++i) {
if (cur_sum + a[i] <= target) {
backtrack(i + 1, cur_sum + a[i]);
if (possible) return;
}
}
}

int main() {
ios::sync_with_stdio(false);
cin.tie(nullptr);
if (!(cin >> n)) return 0;
a.resize(n);
long long total = 0;
for (int i = 0; i < n; ++i) {
cin >> a[i];
total += a[i];
}
if (total % 2 != 0) {
cout << "NO\n";
return 0;
}
target = total / 2;
sort(a.rbegin(), a.rend());
backtrack(0, 0);
cout << (possible "YES\n" : "NO\n");
return 0;
}
```
