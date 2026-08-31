# HƯỚNG DẪN GIẢNG DẠY: ĐUA XE MÊ CUNG ĐỔI HƯỚNG ÍT NHẤT (0-1 BFS STATE)

## 1. Mục Tiêu Học Tập & Chuẩn Đầu Ra (Learning Objectives)
* Hiểu rõ bản chất bài toán và cách nhận diện trạng thái quy hoạch động / cấu trúc dữ liệu.
* Rèn luyện kỹ năng xây dựng công thức truy hồi và xác định trường hợp cơ sở (Base Case).
* Nắm vững kỹ thuật tối ưu hóa không gian bộ nhớ và thời gian thực thi.

## 2. Phân Tích Đề Bài & Bản Chất Toán Học (Edge Cases)
* **Bản chất:** Phân rã bài toán lớn thành các bài toán con tối ưu lồng nhau (Optimal Substructure & Overlapping Subproblems).
* **Trường hợp biên:**
  * $N = 1$ hoặc giá trị biên nhỏ nhất.
  * Mảng không có phần tử thỏa mãn hoặc các phần tử bằng nhau.
  * Giá trị tích lũy vượt quá $2^31-1$ cần dùng `long long`.

## 3. Câu Hỏi Gợi Mở Dẫn Dắt (Socratic Method)
1. Nếu giải bài toán bằng đệ quy ngây thơ, ta có bị tính lặp lại các trạng thái trùng nhau không?
2. Trạng thái $dp[i]$ cần lưu trữ thông tin gì nhỏ nhất để đủ quyết định các bước tiếp theo?
3. Thứ tự tính toán các trạng thái nên đi từ đâu đến đâu để đảm bảo trạng thái trước đã sẵn sàng?

## 4. Chiến Lược Tối Ưu & Bất Biến Thuật Toán (Invariant)
* **Trạng thái:** Định nghĩa rõ ràng ý nghĩa của bảng phương án $dp$.
* **Công thức chuyển trạng thái:** Thiết lập mối liên hệ giữa bài toán con và bài toán lớn hơn.
* **Bất biến:** Tại mọi bước $i$, $dp[i]$ luôn chứa kết quả tối ưu của tiền tố kích thước $i$.

## 5. Mô Phỏng Từng Bước Trên Sample (Dry Run Table)
Mô phỏng chi tiết các bước cập nhật trạng thái trên dữ liệu mẫu:
* Dữ liệu vào: `3 3 S.. .#. ..E`
* Kết quả tính toán: `1`

## 6. Phân Tích Độ Phức Tạp Thời Gian & Không Gian
* **Thời gian (Time Complexity):** $\mathcal{O}(N)$ hoặc $\mathcal{O}(N \log N)$ đảm bảo chạy dưới $1.0\text{s}$ với $N = 10^5$.
* **Không gian (Space Complexity):** $\mathcal{O}(N)$ hoặc $\mathcal{O}(1)$ tối ưu bộ nhớ dưới $256\text{MB}$.

## 7. Các Bẫy Lỗi Lập Trình Kinh Điển (Bug Traps)
* Quên khởi tạo giá trị cơ sở hoặc khởi tạo sai giá trị cực trị (`INF` / `-INF`).
* Tràn số nguyên 32-bit khi cộng dồn kết quả hoặc nhân giá trị.
* Chỉ số mảng 0-based và 1-based bị lệch $1$ đơn vị.

## 8. Mã Nguồn Tham Chiếu C++ Chuẩn Thi Đấu
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

## 9. Bài Toán Mở Rộng & Chuyển Giao (Transfer & Extensions)
* Mở rộng bài toán khi có thêm ràng buộc hoặc kết hợp cấu trúc dữ liệu Segment Tree / Fenwick Tree để tăng tốc truy vấn.
