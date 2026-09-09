# Hướng Dẫn Giảng Dạy: Bước Nhảy Quân Mã Ngắn Nhất (Knight Moves)

Chuyên đề: **Đồ Thị Lưới 2 Chiều & Thuật Toán Loang (2D Grid & Flood Fill)**

---

## 1. Ý tưởng & Phân tích thuật toán

- **Bản chất bài toán:** Cho kích thước bàn cờ $N$ và hai tọa độ điểm xuất phát, điểm đích. Hãy lập trình tìm số bước nhảy ít nhất của quân Mã.

- **Phương pháp tiếp cận & Chiến lược tối ưu:**
- **Mô hình hoá ma trận:** Coi mỗi ô $(r, c)$ trên lưới là một đỉnh của đồ thị, các cạnh nối đến 4 ô kề cạnh (hoặc 8 ô kề góc).
- **Kỹ thuật mảng hướng di chuyển:** Sử dụng 2 mảng phụ trợ `int dx[] = {-1, 1, 0, 0}` và `int dy[] = {0, 0, -1, 1}` để duyệt các ô lân cận tinh gọn, tránh trùng lặp mã nguồn.
- **Kỹ thuật Flood Fill:** Đánh dấu ô đã thăm ngay khi đẩy vào hàng đợi `queue` (hoặc biến đổi trực tiếp giá trị ô ma trận) để tránh việc một ô bị đẩy vào queue nhiều lần gây quá tải bộ nhớ.
- **Độ phức tạp:** Thời gian $\mathcal{O}(N \times M)$, bộ nhớ $\mathcal{O}(N \times M)$.

---

## 2. Bảng chạy tay trên số liệu mẫuMẫu thử (Sample 1): Đầu vào: `8 8 0 0 7 7` $\implies$ Đầu ra kỳ vọng: `6`.

| Bước | Thao tác thực hiện | Dữ liệu biến đổi & Trạng thái | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Khởi tạo & Đọc dữ liệu | Nạp Input: `8 8 0 0 7 7` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Chạy thuật toán từng bước | Phân tích mẫu: Để đi từ ô $(1, 1)$ tới ô $(4, 5)$ trên bàn cờ vua: Quân mã thực hiện lần lượt các bước nhảy: $(1, 1) × o (2, 3) × o (4, 4) × o (2, ... | Cập nhật các biến / mảng trạng thái |
| 3 | Xuất kết quả chuẩn | Đối chiếu trạng thái cuối cùng | Output chuẩn: `6` |

*Giải thích chi tiết:* Để đi từ ô $(1, 1)$ tới ô $(4, 5)$ trên bàn cờ vua:
Quân mã thực hiện lần lượt các bước nhảy: $(1, 1) × o (2, 3) × o (4, 4) × o (2, 5) × o (4, 5)$ hoặc lộ trình tối ưu tương tự với đúng 3 bước nhảy. Kết quả là 3.

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

const int dr[] = {-2, -2, -1, -1, 1, 1, 2, 2};
const int dc[] = {-1, 1, -2, 2, -2, 2, -1, 1};

int main() {
ios::sync_with_stdio(false);
cin.tie(nullptr);

int n, m, sr, sc, er, ec;
if (!(cin >> n >> m >> sr >> sc >> er >> ec)) return 0;

vector<vector<int>> dist(n, vector<int>(m, -1));
queue<pair<int, int>> q;

dist[sr][sc] = 0;
q.push({sr, sc});

while (!q.empty()) {
auto [r, c] = q.front();
q.pop();

if (r == er && c == ec) {
cout << dist[r][c] << "\n";
return 0;
}

for (int d = 0; d < 8; ++d) {
int nr = r + dr[d];
int nc = c + dc[d];
if (nr >= 0 && nr < n && nc >= 0 && nc < m && dist[nr][nc] == -1) {
dist[nr][nc] = dist[r][c] + 1;
q.push({nr, nc});
}
}
}

cout << dist[er][ec] << "\n";
return 0;
}
```
