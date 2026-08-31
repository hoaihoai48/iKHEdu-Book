# Hướng Dẫn Giảng Dạy: Mê Cung (Rat in a Maze): Tìm Mọi Đường Đi
Chuyên đề: **Thuật Toán Quay Lui & Nhánh Cận (Backtracking & Branch and Bound)**

**Phân loại chuyên đề:** `Core Foundation`

---

## 1. Mục Tiêu Học Tập & Chuẩn Đầu Ra (Learning Objectives)
* **Kỹ năng cốt lõi:** Nắm vững và làm chủ kỹ thuật: Mê Cung (Rat in a Maze): Tìm Mọi Đường Đi.
* **Tư duy thuật toán:** Rèn luyện phản xạ xây dựng cây không gian trạng thái theo chuẩn mực `Choose` $\to$ `Explore` $\to$ `Unchoose` và phân biệt rõ ràng giữa Cắt tỉa ràng buộc (Feasibility Pruning) và Cắt tỉa tối ưu (Optimality Pruning).
* **Chuẩn code thi đấu:** Cài đặt C++ chuẩn thi đấu (Fast I/O, Safe Input, 0 `std::`, hoàn tác an toàn).

---

## 2. Phân Tích Đề Bài & Bản Chất Toán Học
* **Dữ liệu đầu vào:** - Dòng 1: Số nguyên dương $N$ ($2 \le N \le 8$).
- $N$ dòng tiếp theo: Mỗi dòng gồm $N$ số nguyên `0` hoặc `1`.
* **Yêu cầu cốt lõi:** Cho mê cung $N \times N$ gồm các ô `1` (đi được) và `0` (tường đá). Con chuột xuất phát từ ô $(0, 0)$ cần đi tới ô $(N-1, N-1)$. Mỗi bước chỉ được đi sang các ô kề cạnh (Down `D`, Left `L`, Right `R`, Up `U`). Hãy in ra tất cả các đường đi hợp lệ theo thứ tự từ điển (`D < L < R < U`). Nếu không có đường đi, in `-1`.
* **Phân tích trường hợp biên:** Đảm bảo hàm dừng đúng khi chạm đáy cây trạng thái và hoàn tác đầy đủ cho các nhánh tiếp theo.

---

## 3. Câu Hỏi Gợi Mở Dẫn Dắt (Socratic Method)
1. Tại mỗi bước của quá trình quay lui, ta có những lựa chọn nào và điều kiện hợp lệ là gì?
2. Sau khi gọi đệ quy đi sâu, trạng thái nào bắt buộc phải được hoàn tác (Unchoose)?
3. Ta có thể thiết lập hàm đánh giá (Bound) như thế nào để cắt tỉa sớm các nhánh không thể tối ưu?

---

## 4. Chiến Lược Tối Ưu & Bất Biến Thuật Toán (Invariant)
* **State Consistency Invariant:** Trạng thái hệ thống trước và sau mỗi lời gọi đệ quy nhánh con phải hoàn toàn bất biến (nhờ bước Unchoose).
* **Pruning Safety:** Cận dưới/Cận trên phải luôn bảo đảm tính đúng đắn toán học để không bao giờ cắt bỏ nghiệm tối ưu toàn cục.

---

## 5. Mô Phỏng Từng Bước Trên Sample (Dry Run Table)
### Dữ liệu Sample:
* **Input:**
```text
4
1 0 0 0
1 1 0 1
0 1 0 0
1 1 1 1
```
* **Output:**
```text
DDRDRR
DRDDRR
```
* **Phân tích thực thi:** Có 2 đường đi từ (0,0) đến (3,3): DDRDRR và DRDDRR.

---

## 6. Phân Tích Độ Phức Tạp Thời Gian & Không Gian
* **Thời gian thực thi (Time Complexity):** $\mathcal{O}(4^{N^2})$ (Loose upper bound)
* **Bộ nhớ ngăn xếp (Call Stack Space):** $\Theta(N^2)$ (Độ sâu tối đa: $N^2$)
* **Bộ nhớ phụ trợ (Auxiliary Memory):** $\Theta(N^2)$
* **Ghi chú phân tích:** Đánh dấu visited[][] và hoàn tác khi backtrack.

---

## 7. Các Bẫy Lỗi Lập Trình Kinh Điển (Bug Traps)
1. **Quên bước hoàn tác (Unchoose):** Làm rò rỉ trạng thái giữa các nhánh gây thiếu nghiệm.
2. **Hàm Bound sai:** Cắt tỉa nhầm nghiệm tối ưu trong các bài toán Branch & Bound.

---

## 8. Mã Nguồn Tham Chiếu C++ Chuẩn Thi Đấu
```cpp
#include <bits/stdc++.h>
using namespace std;

int n;
int a[10][10];
bool visited[10][10];
vector<string> paths;
string cur = "";

int dx[] = {1, 0, 0, -1};
int dy[] = {0, -1, 1, 0};
char step_char[] = {'D', 'L', 'R', 'U'};

void backtrack(int x, int y) {
    if (x == n - 1 && y == n - 1) {
        paths.push_back(cur);
        return;
    }
    for (int i = 0; i < 4; ++i) {
        int nx = x + dx[i], ny = y + dy[i];
        if (nx >= 0 && nx < n && ny >= 0 && ny < n && a[nx][ny] == 1 && !visited[nx][ny]) {
            visited[nx][ny] = true;
            cur.push_back(step_char[i]);
            backtrack(nx, ny);
            cur.pop_back();
            visited[nx][ny] = false;
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    if (!(cin >> n)) return 0;
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < n; ++j) cin >> a[i][j];

    if (a[0][0] == 1) {
        visited[0][0] = true;
        backtrack(0, 0);
    }
    if (paths.empty()) {
        cout << -1 << "\n";
    } else {
        for (const string &s : paths) cout << s << "\n";
    }
    return 0;
}
```

---

## 9. Bài Toán Mở Rộng & Chuyển Giao (Transfer & Extensions)
* Nhận diện hiện tượng trùng lặp trạng thái trên đồ thị có hướng không chu trình (DAG) để chuẩn bị bước chuyển mình mang tính quyết định sang **Module 05: Quy Hoạch Động (Dynamic Programming)**.
