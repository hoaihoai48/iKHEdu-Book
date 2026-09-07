# Hướng Dẫn Giảng Dạy: Trọng Tâm Của Cây (Tree Centroid)

Chuyên đề: **Đồ Thị Lưới 2 Chiều & Thuật Toán Loang (2D Grid & Flood Fill)**

---

## 1. Ý tưởng & Phân tích thuật toán

- **Bản chất bài toán:** Cho đồ thị cây $N$ đỉnh. Hãy lập trình tìm đỉnh trọng tâm của cây. Nếu có nhiều đỉnh trọng tâm, in ra đỉnh có số hiệu nhỏ nhất.

- **Phương pháp tiếp cận & Chiến lược tối ưu:**
- **Mô hình hoá ma trận:** Coi mỗi ô $(r, c)$ trên lưới là một đỉnh của đồ thị, các cạnh nối đến 4 ô kề cạnh (hoặc 8 ô kề góc).
- **Kỹ thuật mảng hướng di chuyển:** Sử dụng 2 mảng phụ trợ `int dx[] = {-1, 1, 0, 0}` và `int dy[] = {0, 0, -1, 1}` để duyệt các ô lân cận tinh gọn, tránh trùng lặp mã nguồn.
- **Kỹ thuật Flood Fill:** Đánh dấu ô đã thăm ngay khi đẩy vào hàng đợi `queue` (hoặc biến đổi trực tiếp giá trị ô ma trận) để tránh việc một ô bị đẩy vào queue nhiều lần gây quá tải bộ nhớ.
- **Độ phức tạp:** Thời gian $\mathcal{O}(N \times M)$, bộ nhớ $\mathcal{O}(N \times M)$.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table)
Mẫu thử (Sample 1): Đầu vào: `5 1 2 2 3 3 4 3 5` $\implies$ Đầu ra kỳ vọng: `3`.

| Bước | Thao tác thực hiện | Dữ liệu biến đổi & Trạng thái | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Khởi tạo & Đọc dữ liệu | Nạp Input: `5 1 2 2 3 3 4 3 5` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Chạy thuật toán từng bước | Phân tích mẫu: Với cây 5 đỉnh có đỉnh 1 nối với các đỉnh 2, 3, 4, 5 (cấu trúc hình sao): Nếu chọn đỉnh 1 làm trọng tâm, các nhánh còn lại đều chỉ có k... | Cập nhật các biến / mảng trạng thái |
| 3 | Xuất kết quả chuẩn | Đối chiếu trạng thái cuối cùng | Output chuẩn: `3` |

*Giải thích chi tiết:* Với cây 5 đỉnh có đỉnh 1 nối với các đỉnh 2, 3, 4, 5 (cấu trúc hình sao):
Nếu chọn đỉnh 1 làm trọng tâm, các nhánh còn lại đều chỉ có kích thước là 1. Đỉnh trọng tâm duy nhất là đỉnh 1.

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

int n;
vector<vector<int>> adj;
vector<int> sz;
int centroid_node = -1;

void dfs(int u, int p) {
    sz[u] = 1;
    bool is_centroid = true;

    for (int v : adj[u]) {
        if (v != p) {
            dfs(v, u);
            sz[u] += sz[v];
            if (sz[v] > n / 2) is_centroid = false;
        }
    }

    if (n - sz[u] > n / 2) is_centroid = false;
    if (is_centroid && centroid_node == -1) centroid_node = u;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    if (!(cin >> n)) return 0;
    if (n <= 0) return 0;

    adj.assign(n + 1, vector<int>());
    sz.assign(n + 1, 0);

    for (int i = 0; i < n - 1; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    dfs(1, 0);
    cout << centroid_node << "\n";
    return 0;
}
```
