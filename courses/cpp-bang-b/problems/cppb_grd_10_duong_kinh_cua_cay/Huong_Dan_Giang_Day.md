# Hướng Dẫn Giảng Dạy: Đường Kính Của Cây (Tree Diameter)

Chuyên đề: **Đồ Thị Lưới 2 Chiều & Thuật Toán Loang (2D Grid & Flood Fill)**

---

## 1. Ý tưởng & Phân tích thuật toán

- **Bản chất bài toán:** Cho cấu trúc cây gồm $N$ đỉnh. Hãy lập trình tìm đường kính (khoảng cách lớn nhất giữa hai đỉnh) của cây.

- **Phương pháp tiếp cận & Chiến lược tối ưu:**
- **Mô hình hoá ma trận:** Coi mỗi ô $(r, c)$ trên lưới là một đỉnh của đồ thị, các cạnh nối đến 4 ô kề cạnh (hoặc 8 ô kề góc).
- **Kỹ thuật mảng hướng di chuyển:** Sử dụng 2 mảng phụ trợ `int dx[] = {-1, 1, 0, 0}` và `int dy[] = {0, 0, -1, 1}` để duyệt các ô lân cận tinh gọn, tránh trùng lặp mã nguồn.
- **Kỹ thuật Flood Fill:** Đánh dấu ô đã thăm ngay khi đẩy vào hàng đợi `queue` (hoặc biến đổi trực tiếp giá trị ô ma trận) để tránh việc một ô bị đẩy vào queue nhiều lần gây quá tải bộ nhớ.
- **Độ phức tạp:** Thời gian $\mathcal{O}(N \times M)$, bộ nhớ $\mathcal{O}(N \times M)$.

---

## 2. Bảng chạy tay trên số liệu mẫuMẫu thử (Sample 1): Đầu vào: `5 1 2 1 3 3 4 3 5` $\implies$ Đầu ra kỳ vọng: `3`.

| Bước | Thao tác thực hiện | Dữ liệu biến đổi & Trạng thái | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Khởi tạo & Đọc dữ liệu | Nạp Input: `5 1 2 1 3 3 4 3 5` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Chạy thuật toán từng bước | Phân tích mẫu: Với cây gồm 5 đỉnh có các cạnh (1, 2), (1, 3), (2, 4), (4, 5): Hành trình dài nhất nối giữa đỉnh 3 và đỉnh 5 qua các cạnh: $3 - 1 - 2 -... | Cập nhật các biến / mảng trạng thái |
| 3 | Xuất kết quả chuẩn | Đối chiếu trạng thái cuối cùng | Output chuẩn: `3` |

*Giải thích chi tiết:* Với cây gồm 5 đỉnh có các cạnh (1, 2), (1, 3), (2, 4), (4, 5):
Hành trình dài nhất nối giữa đỉnh 3 và đỉnh 5 qua các cạnh: $3 - 1 - 2 - 4 - 5$, gồm đúng 4 cạnh. Đường kính của cây là 4.

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

int n;
vector<vector<int>> adj;

pair<int, int> bfs(int start) {
vector<int> dist(n + 1, -1);
queue<int> q;
dist[start] = 0;
q.push(start);

int furthest_node = start;
int max_d = 0;

while (!q.empty()) {
int u = q.front();
q.pop();

if (dist[u] > max_d) {
max_d = dist[u];
furthest_node = u;
}

for (int v : adj[u]) {
if (dist[v] == -1) {
dist[v] = dist[u] + 1;
q.push(v);
}
}
}
return {furthest_node, max_d};
}

int main() {
ios::sync_with_stdio(false);
cin.tie(nullptr);

if (!(cin >> n)) return 0;
if (n <= 1) { cout << 0 << "\n"; return 0; }

adj.assign(n + 1, vector<int>());
for (int i = 0; i < n - 1; ++i) {
int u, v;
cin >> u >> v;
adj[u].push_back(v);
adj[v].push_back(u);
}

auto [u, d1] = bfs(1);
auto [v, diameter] = bfs(u);

cout << diameter << "\n";
return 0;
}
```
