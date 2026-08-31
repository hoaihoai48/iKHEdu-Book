# HƯỚNG DẪN GIẢNG DẠY: HÌNH VUÔNG TOÀN 1 LỚN NHẤT (MAXIMAL SQUARE)

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
* Dữ liệu vào: `4 5 10100 10111 11111 10010`
* Kết quả tính toán: `4`

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

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;
    if (n <= 0 || m <= 0) return 0;

    vector<string> grid(n);
    for (int i = 0; i < n; ++i) cin >> grid[i];

    vector<vector<int>> dp(n, vector<int>(m, 0));
    int max_side = 0;

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            if (grid[i][j] == '1') {
                if (i == 0 || j == 0) {
                    dp[i][j] = 1;
                } else {
                    dp[i][j] = min({dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]}) + 1;
                }
                max_side = max(max_side, dp[i][j]);
            }
        }
    }

    cout << max_side * max_side << "\n";
    return 0;
}
```

## 9. Bài Toán Mở Rộng & Chuyển Giao (Transfer & Extensions)
* Mở rộng bài toán khi có thêm ràng buộc hoặc kết hợp cấu trúc dữ liệu Segment Tree / Fenwick Tree để tăng tốc truy vấn.
