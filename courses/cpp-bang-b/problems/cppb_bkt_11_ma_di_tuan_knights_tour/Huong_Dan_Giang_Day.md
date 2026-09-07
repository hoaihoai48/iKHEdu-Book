# Hướng Dẫn Giảng Dạy: Mã Đi Tuần (Knight's Tour)
Chuyên đề: **Bài 12: Thuật toán quay lui & nhánh cận**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho kích thước bàn cờ $N$ và tọa độ xuất phát $(R, C)$ (hệ tọa độ 1-based). Hãy sử dụng thuật toán Quay lui kết hợp luật heuristic Warnsdorff (luôn ưu tiên nhảy sang ô có ít nước đi tiếp theo nhất) để tìm một hành trình mã đi tuần hoàn chỉnh. In ra ma trận $N \times N$ ghi số thứ tự các bước đi từ $1$ đến $N^2$, hoặc in `-1` nếu không tìm được hành trình.

- **Phương pháp tiếp cận — Quay lui & Nhánh cận (Backtracking):**
  - Xây dựng không gian trạng thái dạng cây tìm kiếm.
  - Thử từng khả năng, nếu vi phạm điều kiện ràng buộc thì tỉa nhánh sớm (nhánh cận) để giảm số trạng thái cần duyệt.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 5 1 1)
| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `5 1 1` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | Quân mã xuất phát từ ô $(1, 1)$ bước 1, lần lượt nhảy qua các ô theo luật mã và ghé thăm đủ 25 ô trên bàn cờ $5 \times 5... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `1 16 11 6 25 10 5 24 15 20 17 2 19 ` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* Quân mã xuất phát từ ô $(1, 1)$ bước 1, lần lượt nhảy qua các ô theo luật mã và ghé thăm đủ 25 ô trên bàn cờ $5 \times 5$ mà không ô nào bị trùng lặp.

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
int board[10][10];
int dx[] = {-2, -2, -1, -1, 1, 1, 2, 2};
int dy[] = {-1, 1, -2, 2, -2, 2, -1, 1};
bool found = false;

int countDegree(int x, int y) {
    int deg = 0;
    for (int i = 0; i < 8; ++i) {
        int nx = x + dx[i], ny = y + dy[i];
        if (nx >= 1 && nx <= n && ny >= 1 && ny <= n && board[nx][ny] == 0) deg++;
    }
    return deg;
}

void solveKnight(int x, int y, int step) {
    if (step == n * n) {
        found = true;
        return;
    }

    vector<pair<int, int>> next_moves;
    for (int i = 0; i < 8; ++i) {
        int nx = x + dx[i], ny = y + dy[i];
        if (nx >= 1 && nx <= n && ny >= 1 && ny <= n && board[nx][ny] == 0) {
            next_moves.push_back({countDegree(nx, ny), i});
        }
    }
    sort(next_moves.begin(), next_moves.end());

    for (auto &p : next_moves) {
        int idx = p.second;
        int nx = x + dx[idx], ny = y + dy[idx];
        board[nx][ny] = step + 1;
        solveKnight(nx, ny, step + 1);
        if (found) return;
        board[nx][ny] = 0;
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int r, c;
    if (!(cin >> n >> r >> c)) return 0;
    memset(board, 0, sizeof(board));
    board[r][c] = 1;
    solveKnight(r, c, 1);
    if (!found) {
        cout << -1 << "\n";
    } else {
        for (int i = 1; i <= n; ++i) {
            for (int j = 1; j <= n; ++j) {
                cout << board[i][j] << (j == n ? "" : " ");
            }
            cout << "\n";
        }
    }
    return 0;
}
```
