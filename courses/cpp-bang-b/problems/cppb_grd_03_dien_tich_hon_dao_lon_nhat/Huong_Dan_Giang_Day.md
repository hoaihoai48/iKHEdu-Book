# Hướng Dẫn Giảng Dạy: Diện Tích Hòn Đảo Lớn Nhất (Max Area of Island)

Chuyên đề: **Đồ Thị Lưới 2 Chiều & Thuật Toán Loang (2D Grid & Flood Fill)**

---

## 1. Ý tưởng & Phân tích thuật toán

- **Bản chất bài toán:** Cho bản đồ ma trận $N × M$. Hãy lập trình tìm diện tích (số lượng ô đất) của hòn đảo lớn nhất. Nếu bản đồ không có đảo nào, in ra `0`.

- **Phương pháp tiếp cận & Chiến lược tối ưu:**
- **Mô hình hoá ma trận:** Coi mỗi ô $(r, c)$ trên lưới là một đỉnh của đồ thị, các cạnh nối đến 4 ô kề cạnh (hoặc 8 ô kề góc).
- **Kỹ thuật mảng hướng di chuyển:** Sử dụng 2 mảng phụ trợ `int dx[] = {-1, 1, 0, 0}` và `int dy[] = {0, 0, -1, 1}` để duyệt các ô lân cận tinh gọn, tránh trùng lặp mã nguồn.
- **Kỹ thuật Flood Fill:** Đánh dấu ô đã thăm ngay khi đẩy vào hàng đợi `queue` (hoặc biến đổi trực tiếp giá trị ô ma trận) để tránh việc một ô bị đẩy vào queue nhiều lần gây quá tải bộ nhớ.
- **Độ phức tạp:** Thời gian $\mathcal{O}(N \times M)$, bộ nhớ $\mathcal{O}(N \times M)$.

---

## 2. Bảng chạy tay trên số liệu mẫuMẫu thử (Sample 1): Đầu vào: `4 5 11000 11000 00100 00011` $\implies$ Đầu ra kỳ vọng: `4`.

| Bước | Thao tác thực hiện | Dữ liệu biến đổi & Trạng thái | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Khởi tạo & Đọc dữ liệu | Nạp Input: `4 5 11000 11000 00100 00011` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Chạy thuật toán từng bước | Phân tích mẫu: Với bản đồ có cụm đảo lớn nhất gồm 5 ô đất liền kề cạnh kết nối liên tục với nhau, diện tích lớn nhất đo được là 5. | Cập nhật các biến / mảng trạng thái |
| 3 | Xuất kết quả chuẩn | Đối chiếu trạng thái cuối cùng | Output chuẩn: `4` |

*Giải thích chi tiết:* Với bản đồ có cụm đảo lớn nhất gồm 5 ô đất liền kề cạnh kết nối liên tục với nhau, diện tích lớn nhất đo được là 5.

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
if (n <= 0 || m <= 0) return 0;

vector<string> grid(n);
for (int i = 0; i < n; ++i) cin >> grid[i];

vector<vector<bool>> visited(n, vector<bool>(m, false));
int max_area = 0;

for (int r = 0; r < n; ++r) {
for (int c = 0; c < m; ++c) {
if (grid[r][c] == '1' && !visited[r][c]) {
int area = 0;
visited[r][c] = true;
queue<pair<int, int>> q;
q.push({r, c});

while (!q.empty()) {
auto [cr, cc] = q.front();
q.pop();
area++;

for (int d = 0; d < 4; ++d) {
int nr = cr + dr[d];
int nc = cc + dc[d];
if (nr >= 0 && nr < n && nc >= 0 && nc < m && grid[nr][nc] == '1' && !visited[nr][nc]) {
visited[nr][nc] = true;
q.push({nr, nc});
}
}
}
max_area = max(max_area, area);
}
}
}

cout << max_area << "\n";
return 0;
}
```
