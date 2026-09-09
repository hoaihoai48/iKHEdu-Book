# Hướng Dẫn Giảng Dạy: Hòn Đảo Nhân Tạo Lớn Nhất (Making A Large Island)

Chuyên đề: **Đồ Thị Lưới 2 Chiều & Thuật Toán Loang (2D Grid & Flood Fill)**

---

## 1. Ý tưởng & Phân tích thuật toán

- **Bản chất bài toán:** Cho ma trận nhị phân $N × M$. Hãy lập trình tìm diện tích lớn nhất của một hòn đảo sau khi chuyển đổi tối đa một ô `0` thành `1`.

- **Phương pháp tiếp cận & Chiến lược tối ưu:**
- **Mô hình hoá ma trận:** Coi mỗi ô $(r, c)$ trên lưới là một đỉnh của đồ thị, các cạnh nối đến 4 ô kề cạnh (hoặc 8 ô kề góc).
- **Kỹ thuật mảng hướng di chuyển:** Sử dụng 2 mảng phụ trợ `int dx[] = {-1, 1, 0, 0}` và `int dy[] = {0, 0, -1, 1}` để duyệt các ô lân cận tinh gọn, tránh trùng lặp mã nguồn.
- **Kỹ thuật Flood Fill:** Đánh dấu ô đã thăm ngay khi đẩy vào hàng đợi `queue` (hoặc biến đổi trực tiếp giá trị ô ma trận) để tránh việc một ô bị đẩy vào queue nhiều lần gây quá tải bộ nhớ.
- **Độ phức tạp:** Thời gian $\mathcal{O}(N \times M)$, bộ nhớ $\mathcal{O}(N \times M)$.

---

## 2. Bảng chạy tay trên số liệu mẫuMẫu thử (Sample 1): Đầu vào: `2 2 10 01` $\implies$ Đầu ra kỳ vọng: `3`.

| Bước | Thao tác thực hiện | Dữ liệu biến đổi & Trạng thái | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Khởi tạo & Đọc dữ liệu | Nạp Input: `2 2 10 01` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Chạy thuật toán từng bước | Phân tích mẫu: Với hai hòn đảo nhỏ diện tích 2 và 3 nằm cách nhau đúng một ô nước biển '0': Khi chuyển ô nước đó thành ô đất '1', hai hòn đảo sẽ được ... | Cập nhật các biến / mảng trạng thái |
| 3 | Xuất kết quả chuẩn | Đối chiếu trạng thái cuối cùng | Output chuẩn: `3` |

*Giải thích chi tiết:* Với hai hòn đảo nhỏ diện tích 2 và 3 nằm cách nhau đúng một ô nước biển '0':
Khi chuyển ô nước đó thành ô đất '1', hai hòn đảo sẽ được nối liền thành một hòn đảo duy nhất có diện tích $2 + 3 + 1 = 6$. Diện tích lớn nhất đạt được là 6.

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

int n, m;
vector<string> grid;
vector<vector<int>> island_id;
vector<int> island_size;

const int dr[] = {-1, 1, 0, 0};
const int dc[] = {0, 0, -1, 1};

int main() {
ios::sync_with_stdio(false);
cin.tie(nullptr);

if (!(cin >> n >> m)) return 0;
grid.resize(n);
for (int i = 0; i < n; ++i) cin >> grid[i];

island_id.assign(n, vector<int>(m, 0));
island_size.push_back(0); // id 0 unused
int current_id = 1;
int max_area = 0;

for (int r = 0; r < n; ++r) {
for (int c = 0; c < m; ++c) {
if (grid[r][c] == '1' && island_id[r][c] == 0) {
int sz = 0;
island_id[r][c] = current_id;
queue<pair<int, int>> q;
q.push({r, c});

while (!q.empty()) {
auto [cr, cc] = q.front();
q.pop();
sz++;

for (int d = 0; d < 4; ++d) {
int nr = cr + dr[d];
int nc = cc + dc[d];
if (nr >= 0 && nr < n && nc >= 0 && nc < m && grid[nr][nc] == '1' && island_id[nr][nc] == 0) {
island_id[nr][nc] = current_id;
q.push({nr, nc});
}
}
}

island_size.push_back(sz);
max_area = max(max_area, sz);
current_id++;
}
}
}

for (int r = 0; r < n; ++r) {
for (int c = 0; c < m; ++c) {
if (grid[r][c] == '0') {
unordered_set<int> neighbor_ids;
for (int d = 0; d < 4; ++d) {
int nr = r + dr[d];
int nc = c + dc[d];
if (nr >= 0 && nr < n && nc >= 0 && nc < m && island_id[nr][nc] > 0) {
neighbor_ids.insert(island_id[nr][nc]);
}
}
int combined_sz = 1;
for (int id : neighbor_ids) combined_sz += island_size[id];
max_area = max(max_area, combined_sz);
}
}
}

cout << max_area << "\n";
return 0;
}
```
