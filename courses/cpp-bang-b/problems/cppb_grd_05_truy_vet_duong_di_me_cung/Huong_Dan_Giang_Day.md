# Hướng Dẫn Giảng Dạy: Truy Vết Đường Đi Mê Cung (L, R, U, D)

Chuyên đề: **Đồ Thị Lưới 2 Chiều & Thuật Toán Loang (2D Grid & Flood Fill)**

---

## 1. Ý tưởng & Phân tích thuật toán

- **Bản chất bài toán:** Cho bản đồ mê cung $N  × M$ với điểm xuất phát `S` và đích `E`. Hãy lập trình tìm đường đi ngắn nhất và in ra chuỗi các bước di chuyển tương ứng.

- **Phương pháp tiếp cận & Chiến lược tối ưu:**
- **Mô hình hoá ma trận:** Coi mỗi ô $(r, c)$ trên lưới là một đỉnh của đồ thị, các cạnh nối đến 4 ô kề cạnh (hoặc 8 ô kề góc).
- **Kỹ thuật mảng hướng di chuyển:** Sử dụng 2 mảng phụ trợ `int dx[] = {-1, 1, 0, 0}` và `int dy[] = {0, 0, -1, 1}` để duyệt các ô lân cận tinh gọn, tránh trùng lặp mã nguồn.
- **Kỹ thuật Flood Fill:** Đánh dấu ô đã thăm ngay khi đẩy vào hàng đợi `queue` (hoặc biến đổi trực tiếp giá trị ô ma trận) để tránh việc một ô bị đẩy vào queue nhiều lần gây quá tải bộ nhớ.
- **Độ phức tạp:** Thời gian $\mathcal{O}(N \times M)$, bộ nhớ $\mathcal{O}(N \times M)$.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table)
Mẫu thử (Sample 1): Đầu vào: `5 8 ######## #.A#...# #.##.#B# #......# ########` $\implies$ Đầu ra kỳ vọng: `YES 9 LDDRRRRRU`.

| Bước | Thao tác thực hiện | Dữ liệu biến đổi & Trạng thái | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Khởi tạo & Đọc dữ liệu | Nạp Input: `5 8 ######## #.A#...# #.##.#B# #......# #####` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Chạy thuật toán từng bước | Phân tích mẫu: Với lộ trình đi từ $(0, 0)$ sang phải rồi xuống dưới: Chuỗi lệnh điều hướng tương ứng là: "RRD" hoặc "DRR" có độ dài 3 bước. | Cập nhật các biến / mảng trạng thái |
| 3 | Xuất kết quả chuẩn | Đối chiếu trạng thái cuối cùng | Output chuẩn: `YES 9 LDDRRRRRU` |

*Giải thích chi tiết:* Với lộ trình đi từ $(0, 0)$ sang phải rồi xuống dưới:
Chuỗi lệnh điều hướng tương ứng là: "RRD" hoặc "DRR" có độ dài 3 bước.

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
const char dir_char[] = {'U', 'D', 'L', 'R'};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<string> grid(n);
    int sr = -1, sc = -1, er = -1, ec = -1;

    for (int r = 0; r < n; ++r) {
        cin >> grid[r];
        for (int c = 0; c < m; ++c) {
            if (grid[r][c] == 'A' || grid[r][c] == 'S') { sr = r; sc = c; }
            if (grid[r][c] == 'B' || grid[r][c] == 'E') { er = r; ec = c; }
        }
    }

    vector<vector<int>> dist(n, vector<int>(m, -1));
    vector<vector<int>> prev_dir(n, vector<int>(m, -1));
    queue<pair<int, int>> q;

    dist[sr][sc] = 0;
    q.push({sr, sc});

    while (!q.empty()) {
        auto [r, c] = q.front();
        q.pop();

        if (r == er && c == ec) break;

        for (int d = 0; d < 4; ++d) {
            int nr = r + dr[d];
            int nc = c + dc[d];
            if (nr >= 0 && nr < n && nc >= 0 && nc < m && grid[nr][nc] != '#' && dist[nr][nc] == -1) {
                dist[nr][nc] = dist[r][c] + 1;
                prev_dir[nr][nc] = d;
                q.push({nr, nc});
            }
        }
    }

    if (dist[er][ec] == -1) {
        cout << "NO\n";
        return 0;
    }

    cout << "YES\n" << dist[er][ec] << "\n";
    string path = "";
    int curr_r = er, curr_c = ec;

    while (curr_r != sr || curr_c != sc) {
        int d = prev_dir[curr_r][curr_c];
        path += dir_char[d];
        curr_r -= dr[d];
        curr_c -= dc[d];
    }
    reverse(path.begin(), path.end());
    cout << path << "\n";
    return 0;
}
```
