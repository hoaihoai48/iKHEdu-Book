# Hướng Dẫn Giảng Dạy: Đua Xe Mê Cung Đổi Hướng Ít Nhất (0-1 BFS State)

Chuyên đề: **Cấu Trúc Dữ Liệu Hàng Đợi (Queue, Deque) & Monotonic Deque**

---

## 1. Ý tưởng & Phân tích thuật toán

- **Bản chất bài toán:** Cho bản đồ mê cung $N  × M$ và vị trí $S, D$. Hãy lập trình tìm số lần đổi hướng ít nhất để robot đi từ $S$ tới $D$. Nếu không có đường đi, in ra `-1`.

- **Phương pháp tiếp cận & Chiến lược tối ưu:**
- **Nguyên lý Hàng đợi chuẩn (Queue):** Vào trước Ra trước (FIFO), là cấu trúc nền tảng phục vụ duyệt đồ thị theo chiều rộng (BFS).
- **Hàng đợi hai đầu (Deque) & Monotonic Deque:**
  * Hỗ trợ thêm/xoá ở cả hai đầu trong $\mathcal{O}(1)$.
  * Khi trượt cửa sổ kích thước $K$, lưu chỉ số phần tử trong deque sao cho giá trị tương ứng luôn đơn điệu.
  * Loại bỏ phần tử trượt ra khỏi cửa sổ ở đầu trước (`pop_front()`) và loại bỏ phần tử kém tối ưu ở đầu sau (`pop_back()`).
- **Độ phức tạp:** Thời gian $\mathcal{O}(N)$, không gian phụ trợ $\mathcal{O}(K)$.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table)
Mẫu thử (Sample 1): Đầu vào: `3 3 S.. .#. ..E` $\implies$ Đầu ra kỳ vọng: `1`.

| Bước | Thao tác thực hiện | Dữ liệu biến đổi & Trạng thái | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Khởi tạo & Đọc dữ liệu | Nạp Input: `3 3 S.. .#. ..E` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Chạy thuật toán từng bước | Phân tích mẫu: Với mê cung $3 × 3$ không vật cản từ góc $(1,1)$ tới $(3,3)$: Robot chỉ cần đi thẳng hết hàng 1 sang phải, sau đó rẽ lái 1 lần duy nhất... | Cập nhật các biến / mảng trạng thái |
| 3 | Xuất kết quả chuẩn | Đối chiếu trạng thái cuối cùng | Output chuẩn: `1` |

*Giải thích chi tiết:* Với mê cung $3 × 3$ không vật cản từ góc $(1,1)$ tới $(3,3)$:
Robot chỉ cần đi thẳng hết hàng 1 sang phải, sau đó rẽ lái 1 lần duy nhất để đi thẳng xuống dưới tới đích. Số lần đổi hướng ít nhất là 1.

---

## 3. Lưu ý & Bẫy lỗi thường gặp
* Lưu giá trị thay vì lưu chỉ số vị trí (index) trong Deque: Phải lưu index để kiểm tra điều kiện phần tử đã trượt ra khỏi cửa sổ $i - K$ hay chưa (`dq.front() <= i - K`).
* Quên kiểm tra `!dq.empty()` trước khi truy xuất `dq.front()` hoặc `dq.back()` gây crash chương trình.
* Không khởi tạo kết quả cho $K-1$ vị trí đầu tiên trước khi bắt đầu ghi nhận đáp án từ vị trí thứ $K$.

---

## 4. Lời giải tham khảo
```cpp
#include <bits/stdc++.h>
using namespace std;

const int INF = 1e9;
const int dr[] = {-1, 1, 0, 0};
const int dc[] = {0, 0, -1, 1};

struct State {
    int r, c, dir;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;
    if (n <= 0 || m <= 0) return 0;

    vector<string> grid(n);
    int sr = -1, sc = -1, er = -1, ec = -1;

    for (int r = 0; r < n; ++r) {
        cin >> grid[r];
        for (int c = 0; c < m; ++c) {
            if (grid[r][c] == 'S') { sr = r; sc = c; }
            if (grid[r][c] == 'E') { er = r; ec = c; }
        }
    }

    vector<vector<vector<int>>> dist(n, vector<vector<int>>(m, vector<int>(4, INF)));
    deque<State> dq;

    for (int d = 0; d < 4; ++d) {
        dist[sr][sc][d] = 0;
        dq.push_back({sr, sc, d});
    }

    while (!dq.empty()) {
        auto [r, c, dir] = dq.front();
        dq.pop_front();

        for (int nd = 0; nd < 4; ++nd) {
            int nr = r + dr[nd];
            int nc = c + dc[nd];
            int cost = (nd == dir ? 0 : 1);

            if (nr >= 0 && nr < n && nc >= 0 && nc < m && grid[nr][nc] != '#') {
                if (dist[r][c][dir] + cost < dist[nr][nc][nd]) {
                    dist[nr][nc][nd] = dist[r][c][dir] + cost;
                    if (cost == 0) {
                        dq.push_front({nr, nc, nd});
                    } else {
                        dq.push_back({nr, nc, nd});
                    }
                }
            }
        }
    }

    int ans = INF;
    for (int d = 0; d < 4; ++d) ans = min(ans, dist[er][ec][d]);

    if (ans == INF) cout << -1 << "\n";
    else cout << ans << "\n";
    return 0;
}
```
