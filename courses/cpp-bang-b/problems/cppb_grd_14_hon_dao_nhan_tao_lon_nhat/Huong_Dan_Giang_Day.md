# HƯỚNG DẪN GIẢNG DẠY: HÒN ĐẢO NHÂN TẠO LỚN NHẤT (MAKING A LARGE ISLAND)

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
* Dữ liệu vào: `2 2 10 01`
* Kết quả tính toán: `3`

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

## 9. Bài Toán Mở Rộng & Chuyển Giao (Transfer & Extensions)
* Mở rộng bài toán khi có thêm ràng buộc hoặc kết hợp cấu trúc dữ liệu Segment Tree / Fenwick Tree để tăng tốc truy vấn.
