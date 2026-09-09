# Hướng Dẫn Giảng Dạy: Mê Cung (Rat in a Maze): Tìm Mọi Đường Đi
Chuyên đề: **Bài 12: Thuật toán quay lui & nhánh cận**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho bản đồ mê cung $N \times N$. Giả sử mỗi bước robot chỉ di chuyển sang các ô kề cạnh chưa từng ghé qua theo các hướng: Xuống dưới (`D`), Sang trái (`L`), Sang phải (`R`), Lên trên (`U`). Hãy áp dụng thuật toán Quay lui để tìm và in ra tất cả các chuỗi di chuyển hợp lệ theo thứ tự từ điển (`D < L < R < U`). Nếu ô xuất phát bị chặn hoặc không có đường đi nào, in ra `-1`.

- **Phương pháp tiếp cận — Quay lui & Nhánh cận (Backtracking):**
- Xây dựng không gian trạng thái dạng cây tìm kiếm.
- Thử từng khả năng, nếu vi phạm điều kiện ràng buộc thì tỉa nhánh sớm (nhánh cận) để giảm số trạng thái cần duyệt.

---

## 2. Bảng chạy tay trên số liệu mẫu| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `4 1 0 0 0 1 1 0 1 0 1 0 0 1 1 1 1` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | Robot xuất phát tại $(0,0)$ và đích đến là $(3,3)$. Có 2 tuyến đường hợp lệ không qua ô 0: - Tuyến 1: Đi xuống $\to$ xuố... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `DDRDRR DRDDRR` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* Robot xuất phát tại $(0,0)$ và đích đến là $(3,3)$. Có 2 tuyến đường hợp lệ không qua ô 0:

- Tuyến 1: Đi xuống $\to$ xuống $\to$ phải $\to$ xuống $\to$ phải $\to$ phải (`DDRDRR`).
- Tuyến 2: Đi xuống $\to$ phải $\to$ xuống $\to$ xuống $\to$ phải $\to$ phải (`DRDDRR`).

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
int a[10][10];
bool visited[10][10];
vector<string> paths;
string cur = "";

int dx[] = {1, 0, 0, -1};
int dy[] = {0, -1, 1, 0};
char step_char[] = {'D', 'L', 'R', 'U'};

void backtrack(int x, int y) {
if (x == n - 1 && y == n - 1) {
paths.push_back(cur);
return;
}
for (int i = 0; i < 4; ++i) {
int nx = x + dx[i], ny = y + dy[i];
if (nx >= 0 && nx < n && ny >= 0 && ny < n && a[nx][ny] == 1 && !visited[nx][ny]) {
visited[nx][ny] = true;
cur.push_back(step_char[i]);
backtrack(nx, ny);
cur.pop_back();
visited[nx][ny] = false;
}
}
}

int main() {
ios::sync_with_stdio(false);
cin.tie(nullptr);
if (!(cin >> n)) return 0;
for (int i = 0; i < n; ++i)
for (int j = 0; j < n; ++j) cin >> a[i][j];

if (a[0][0] == 1) {
visited[0][0] = true;
backtrack(0, 0);
}
if (paths.empty()) {
cout << -1 << "\n";
} else {
for (const string &s : paths) cout << s << "\n";
}
return 0;
}
```
