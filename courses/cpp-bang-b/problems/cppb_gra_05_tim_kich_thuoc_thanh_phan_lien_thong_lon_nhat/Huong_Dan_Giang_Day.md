# Hướng Dẫn Giảng Dạy: Kích Thước Thành Phần Liên Thông Lớn Nhất

Chuyên đề: **Lý Thuyết Đồ Thị Cơ Bản (Graph: BFS, DFS & Thành Phần Liên Thông)**

---

## 1. Ý tưởng & Phân tích thuật toán

- **Bản chất bài toán:** Cho đồ thị vô hướng $N$ đỉnh $M$ cạnh. Hãy lập trình tìm số lượng đỉnh thuộc về thành phần liên thông có kích thước lớn nhất.

- **Phương pháp tiếp cận & Chiến lược tối ưu:**
- **Biểu diễn đồ thị:** Sử dụng danh sách kề `vector<vector<int>> adj(N + 1)` để tối ưu bộ nhớ $\mathcal{O}(N + M)$ và duyệt cạnh nhanh chóng.
- **Thuật toán duyệt đồ thị:**
* *Tìm kiếm theo chiều rộng (BFS):* Sử dụng hàng đợi `queue`, đảm bảo tìm đường đi ngắn nhất trên đồ thị không trọng số.
* *Tìm kiếm theo chiều sâu (DFS):* Duyệt nhánh sâu nhất bằng đệ quy hoặc stack, thích hợp tìm thành phần liên thông, chu trình và sắp xếp tô-pô.
- **Mảng đánh dấu:** Sử dụng mảng `visited[]` để đảm bảo mỗi đỉnh và cạnh chỉ được xét một số lần hằng số, độ phức tạp đạt $\mathcal{O}(N + M)$.

---

## 2. Bảng chạy tay trên số liệu mẫuMẫu thử (Sample 1): Đầu vào: `5 3 1 2 2 3 4 5` $\implies$ Đầu ra kỳ vọng: `3`.

| Bước | Thao tác thực hiện | Dữ liệu biến đổi & Trạng thái | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Khởi tạo & Đọc dữ liệu | Nạp Input: `5 3 1 2 2 3 4 5` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Chạy thuật toán từng bước | Phân tích mẫu: Với 5 đỉnh và các cạnh (1, 2), (2, 3), (4, 5): - Cụm 1 gồm {1, 2, 3} có 3 hòn đảo. - Cụm 2 gồm {4, 5} có 2 hòn đảo. Kích thước của thàn... | Cập nhật các biến / mảng trạng thái |
| 3 | Xuất kết quả chuẩn | Đối chiếu trạng thái cuối cùng | Output chuẩn: `3` |

*Giải thích chi tiết:* Với 5 đỉnh và các cạnh (1, 2), (2, 3), (4, 5):

- Cụm 1 gồm {1, 2, 3} có 3 hòn đảo.
- Cụm 2 gồm {4, 5} có 2 hòn đảo.
Kích thước của thành phần liên thông lớn nhất là 3.

---

## 3. Lưu ý & Bẫy lỗi thường gặp
* Với đồ thị vô hướng, quên thêm cả hai chiều cạnh: `adj[u].push_back(v); adj[v].push_back(u);`.
* Đồ thị gồm nhiều thành phần liên thông rời rạc: Bắt buộc duyệt vòng lặp `for (int i = 1; i <= N; ++i)` và gọi BFS/DFS khi `!visited[i]` để không bỏ sót các đỉnh độc lập.
* Tràn bộ nhớ Call Stack khi gọi DFS đệ quy quá sâu trên đồ thị có dạng đường thẳng ($N = 10^5$), cần tăng kích thước stack hoặc chuyển sang BFS/DFS lặp.

---

## 4. Lời giải tham khảo
```cpp
#include <bits/stdc++.h>
using namespace std;

int n, m;
vector<vector<int>> adj;
vector<bool> visited;

int dfs(int u) {
visited[u] = true;
int sz = 1;
for (int v : adj[u]) {
if (!visited[v]) sz += dfs(v);
}
return sz;
}

int main() {
ios::sync_with_stdio(false);
cin.tie(nullptr);

if (!(cin >> n >> m)) return 0;
if (n <= 0) return 0;

adj.assign(n + 1, vector<int>());
visited.assign(n + 1, false);

for (int i = 0; i < m; ++i) {
int u, v;
cin >> u >> v;
adj[u].push_back(v);
adj[v].push_back(u);
}

int max_sz = 0;
for (int i = 1; i <= n; ++i) {
if (!visited[i]) {
max_sz = max(max_sz, dfs(i));
}
}

cout << max_sz << "\n";
return 0;
}
```
