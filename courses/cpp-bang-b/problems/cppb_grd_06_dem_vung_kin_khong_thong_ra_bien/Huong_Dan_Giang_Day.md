# HƯỚNG DẪN GIẢNG DẠY: ĐẾM SỐ Ô VÙNG KÍN KHÔNG THÔNG RA BIÊN

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
* Dữ liệu vào: `4 4 1111 1001 1101 1111`
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

const int dr[] = {-1, 1, 0, 0};
const int dc[] = {0, 0, -1, 1};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;
    vector<string> grid(n);
    for (int i = 0; i < n; ++i) cin >> grid[i];

    queue<pair<int, int>> q;

    for (int r = 0; r < n; ++r) {
        if (grid[r][0] == '0') { grid[r][0] = '1'; q.push({r, 0}); }
        if (grid[r][m - 1] == '0') { grid[r][m - 1] = '1'; q.push({r, m - 1}); }
    }
    for (int c = 0; c < m; ++c) {
        if (grid[0][c] == '0') { grid[0][c] = '1'; q.push({0, c}); }
        if (grid[n - 1][c] == '0') { grid[n - 1][c] = '1'; q.push({n - 1, c}); }
    }

    while (!q.empty()) {
        auto [r, c] = q.front();
        q.pop();

        for (int d = 0; d < 4; ++d) {
            int nr = r + dr[d];
            int nc = c + dc[d];
            if (nr >= 0 && nr < n && nc >= 0 && nc < m && grid[nr][nc] == '0') {
                grid[nr][nc] = '1';
                q.push({nr, nc});
            }
        }
    }

    int closed_zeros = 0;
    for (int r = 0; r < n; ++r) {
        for (int c = 0; c < m; ++c) {
            if (grid[r][c] == '0') closed_zeros++;
        }
    }

    cout << closed_zeros << "\n";
    return 0;
}
```

## 9. Bài Toán Mở Rộng & Chuyển Giao (Transfer & Extensions)
* Mở rộng bài toán khi có thêm ràng buộc hoặc kết hợp cấu trúc dữ liệu Segment Tree / Fenwick Tree để tăng tốc truy vấn.
