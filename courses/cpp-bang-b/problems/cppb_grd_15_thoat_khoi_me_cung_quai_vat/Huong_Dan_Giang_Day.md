# Hướng Dẫn Giảng Dạy: Thoát Khỏi Mê Cung Quái Vật (Monsters Maze)

Chuyên đề: **Đồ Thị Lưới 2 Chiều & Thuật Toán Loang (2D Grid & Flood Fill)**

---

## 1. Ý tưởng & Phân tích thuật toán

- **Bản chất bài toán:** Cho bản đồ mê cung. Hãy lập trình kiểm tra xem người thám hiểm có thể thoát thân thành công ra mép biên hay không. Nếu có in ra `YES` kèm số bước, ngược lại in ra `NO`.

- **Phương pháp tiếp cận & Chiến lược tối ưu:**
- **Mô hình hoá ma trận:** Coi mỗi ô $(r, c)$ trên lưới là một đỉnh của đồ thị, các cạnh nối đến 4 ô kề cạnh (hoặc 8 ô kề góc).
- **Kỹ thuật mảng hướng di chuyển:** Sử dụng 2 mảng phụ trợ `int dx[] = {-1, 1, 0, 0}` và `int dy[] = {0, 0, -1, 1}` để duyệt các ô lân cận tinh gọn, tránh trùng lặp mã nguồn.
- **Kỹ thuật Flood Fill:** Đánh dấu ô đã thăm ngay khi đẩy vào hàng đợi `queue` (hoặc biến đổi trực tiếp giá trị ô ma trận) để tránh việc một ô bị đẩy vào queue nhiều lần gây quá tải bộ nhớ.
- **Độ phức tạp:** Thời gian $\mathcal{O}(N \times M)$, bộ nhớ $\mathcal{O}(N \times M)$.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table)
Mẫu thử (Sample 1): Đầu vào: `5 8 ######## #M..A..# #.#.M#.# #M#..#..# #.######` $\implies$ Đầu ra kỳ vọng: `YES`.

| Bước | Thao tác thực hiện | Dữ liệu biến đổi & Trạng thái | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Khởi tạo & Đọc dữ liệu | Nạp Input: `5 8 ######## #M..A..# #.#.M#.# #M#..#..# #.##` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Chạy thuật toán từng bước | Phân tích mẫu: Người thám hiểm chọn lộ trình nhanh nhất hướng về phía mép biên phía đông, đến được biên an toàn sau 2 bước trước khi bất kỳ quái vật n... | Cập nhật các biến / mảng trạng thái |
| 3 | Xuất kết quả chuẩn | Đối chiếu trạng thái cuối cùng | Output chuẩn: `YES` |

*Giải thích chi tiết:* Người thám hiểm chọn lộ trình nhanh nhất hướng về phía mép biên phía đông, đến được biên an toàn sau 2 bước trước khi bất kỳ quái vật nào kịp tiếp cận. Kết quả in ra YES.

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

const int INF = 1e9;
const int dr[] = {-1, 1, 0, 0};
const int dc[] = {0, 0, -1, 1};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<string> grid(n);
    queue<pair<int, int>> mq;
    vector<vector<int>> monster_dist(n, vector<int>(m, INF));
    int ar = -1, ac = -1;

    for (int r = 0; r < n; ++r) {
        cin >> grid[r];
        for (int c = 0; c < m; ++c) {
            if (grid[r][c] == 'M') {
                monster_dist[r][c] = 0;
                mq.push({r, c});
            } else if (grid[r][c] == 'A') {
                ar = r; ac = c;
            }
        }
    }

    while (!mq.empty()) {
        auto [r, c] = mq.front();
        mq.pop();

        for (int d = 0; d < 4; ++d) {
            int nr = r + dr[d];
            int nc = c + dc[d];
            if (nr >= 0 && nr < n && nc >= 0 && nc < m && grid[nr][nc] != '#' && monster_dist[nr][nc] == INF) {
                monster_dist[nr][nc] = monster_dist[r][c] + 1;
                mq.push({nr, nc});
            }
        }
    }

    vector<vector<int>> player_dist(n, vector<int>(m, -1));
    queue<pair<int, int>> pq;

    player_dist[ar][ac] = 0;
    pq.push({ar, ac});

    while (!pq.empty()) {
        auto [r, c] = pq.front();
        pq.pop();

        if (r == 0 || r == n - 1 || c == 0 || c == m - 1) {
            cout << "YES\n";
            return 0;
        }

        for (int d = 0; d < 4; ++d) {
            int nr = r + dr[d];
            int nc = c + dc[d];
            if (nr >= 0 && nr < n && nc >= 0 && nc < m && grid[nr][nc] != '#' && player_dist[nr][nc] == -1) {
                if (player_dist[r][c] + 1 < monster_dist[nr][nc]) {
                    player_dist[nr][nc] = player_dist[r][c] + 1;
                    pq.push({nr, nc});
                }
            }
        }
    }

    cout << "NO\n";
    return 0;
}
```
