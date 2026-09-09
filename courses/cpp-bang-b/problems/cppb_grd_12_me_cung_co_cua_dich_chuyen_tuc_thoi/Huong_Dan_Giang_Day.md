# Hướng Dẫn Giảng Dạy: Cổng Dịch Chuyển Tức Thời (Teleport Maze)

Chuyên đề: **Đồ Thị Lưới 2 Chiều & Thuật Toán Loang (2D Grid & Flood Fill)**

---

## 1. Ý tưởng & Phân tích thuật toán

- **Bản chất bài toán:** Cho bản đồ mê cung và danh sách các cặp cổng dịch chuyển. Hãy lập trình tìm số bước ít nhất để đến đích.

- **Phương pháp tiếp cận & Chiến lược tối ưu:**
- **Mô hình hoá ma trận:** Coi mỗi ô $(r, c)$ trên lưới là một đỉnh của đồ thị, các cạnh nối đến 4 ô kề cạnh (hoặc 8 ô kề góc).
- **Kỹ thuật mảng hướng di chuyển:** Sử dụng 2 mảng phụ trợ `int dx[] = {-1, 1, 0, 0}` và `int dy[] = {0, 0, -1, 1}` để duyệt các ô lân cận tinh gọn, tránh trùng lặp mã nguồn.
- **Kỹ thuật Flood Fill:** Đánh dấu ô đã thăm ngay khi đẩy vào hàng đợi `queue` (hoặc biến đổi trực tiếp giá trị ô ma trận) để tránh việc một ô bị đẩy vào queue nhiều lần gây quá tải bộ nhớ.
- **Độ phức tạp:** Thời gian $\mathcal{O}(N \times M)$, bộ nhớ $\mathcal{O}(N \times M)$.

---

## 2. Bảng chạy tay trên số liệu mẫuMẫu thử (Sample 1): Đầu vào: `3 3 ..A .## A..` $\implies$ Đầu ra kỳ vọng: `2`.

| Bước | Thao tác thực hiện | Dữ liệu biến đổi & Trạng thái | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Khởi tạo & Đọc dữ liệu | Nạp Input: `3 3 ..A .## A..` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Chạy thuật toán từng bước | Phân tích mẫu: Nhờ sử dụng cổng dịch chuyển tức thời, người chơi rút ngắn được quãng đường vòng qua tường đá, thời gian đến đích giảm xuống còn 3 bước. | Cập nhật các biến / mảng trạng thái |
| 3 | Xuất kết quả chuẩn | Đối chiếu trạng thái cuối cùng | Output chuẩn: `2` |

*Giải thích chi tiết:* Nhờ sử dụng cổng dịch chuyển tức thời, người chơi rút ngắn được quãng đường vòng qua tường đá, thời gian đến đích giảm xuống còn 3 bước.

---

## 3. Lưu ý & Bẫy lỗi thường gặp
* Quên kiểm tra toạ độ nằm ngoài biên giới ma trận ($r < 1$ hoặc $r > N$ hoặc $c < 1$ hoặc $c > M$) trước khi truy cập ô `grid[r][c]`, dẫn đến lỗi `Segmentation Fault`.
* Chỉ đánh dấu `visited = true` khi lấy phần tử ra khỏi queue (`pop()`) thay vì khi đẩy vào (`push()`): Đây là lỗi kinh điển khiến cùng một ô bị đẩy vào hàng đợi hàng nghìn lần, dẫn đến `Memory Limit Exceeded` (MLE) hoặc `Time Limit Exceeded` (TLE).
* Không đọc đúng các dòng ký tự liền nhau của ma trận: Khi các ký tự viết liền không có dấu cách, phải đọc từng chuỗi `string` rồi truy cập ký tự `s[c]`.

---

## 4. Lời giải tham khảo
```cpp
#include <bits/stdc++.h>
using namespace std;

const int dr[] = {-1, 1, 0, 0};
const int dc[] = {0, 0, -1, 1};

int main() {
ios::sync_with_stdio(false);
cin.tie(nullptr);

int n, m;
if (!(cin >> n >> m)) return 0;

vector<string> grid(n);
vector<vector<pair<int, int>>> teleports(26);

for (int r = 0; r < n; ++r) {
cin >> grid[r];
for (int c = 0; c < m; ++c) {
if (isupper(grid[r][c])) {
teleports[grid[r][c] - 'A'].push_back({r, c});
}
}
}

vector<vector<int>> dist(n, vector<int>(m, -1));
vector<bool> teleport_used(26, false);
queue<pair<int, int>> q;

dist[0][0] = 0;
q.push({0, 0});

while (!q.empty()) {
auto [r, c] = q.front();
q.pop();

if (r == n - 1 && c == m - 1) {
cout << dist[r][c] << "\n";
return 0;
}

// Dịch chuyển tức thời
if (isupper(grid[r][c])) {
int ch = grid[r][c] - 'A';
if (!teleport_used[ch]) {
teleport_used[ch] = true;
for (auto [tr, tc] : teleports[ch]) {
if (dist[tr][tc] == -1) {
dist[tr][tc] = dist[r][c];
q.push({tr, tc});
}
}
}
}

for (int d = 0; d < 4; ++d) {
int nr = r + dr[d];
int nc = c + dc[d];
if (nr >= 0 && nr < n && nc >= 0 && nc < m && grid[nr][nc] != '#' && dist[nr][nc] == -1) {
dist[nr][nc] = dist[r][c] + 1;
q.push({nr, nc});
}
}
}

cout << dist[n - 1][m - 1] << "\n";
return 0;
}
```
