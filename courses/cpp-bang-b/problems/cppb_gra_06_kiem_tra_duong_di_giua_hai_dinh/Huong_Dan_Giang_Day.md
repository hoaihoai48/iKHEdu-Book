# Hướng Dẫn Giảng Dạy: Kiểm Tra Đường Đi Giữa Hai Đỉnh

Chuyên đề: **Lý Thuyết Đồ Thị Cơ Bản (Graph: BFS, DFS & Thành Phần Liên Thông)**

---

## 1. Ý tưởng & Phân tích thuật toán

- **Bản chất bài toán:** Cho đồ thị vô hướng $N$ đỉnh $M$ cạnh và hai đỉnh $S, D$. Hãy lập trình kiểm tra xem có tồn tại đường đi giữa $S$ và $D$ hay không. Nếu có in ra `YES`, ngược lại in ra `NO`.

- **Phương pháp tiếp cận & Chiến lược tối ưu:**
- **Biểu diễn đồ thị:** Sử dụng danh sách kề `vector<vector<int>> adj(N + 1)` để tối ưu bộ nhớ $\mathcal{O}(N + M)$ và duyệt cạnh nhanh chóng.
- **Thuật toán duyệt đồ thị:**
* *Tìm kiếm theo chiều rộng (BFS):* Sử dụng hàng đợi `queue`, đảm bảo tìm đường đi ngắn nhất trên đồ thị không trọng số.
* *Tìm kiếm theo chiều sâu (DFS):* Duyệt nhánh sâu nhất bằng đệ quy hoặc stack, thích hợp tìm thành phần liên thông, chu trình và sắp xếp tô-pô.
- **Mảng đánh dấu:** Sử dụng mảng `visited[]` để đảm bảo mỗi đỉnh và cạnh chỉ được xét một số lần hằng số, độ phức tạp đạt $\mathcal{O}(N + M)$.

---

## 2. Bảng chạy tay trên số liệu mẫuMẫu thử (Sample 1): Đầu vào: `4 2 1 4 1 2 2 3` $\implies$ Đầu ra kỳ vọng: `NO`.

| Bước | Thao tác thực hiện | Dữ liệu biến đổi & Trạng thái | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Khởi tạo & Đọc dữ liệu | Nạp Input: `4 2 1 4 1 2 2 3` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Chạy thuật toán từng bước | Phân tích mẫu: Với đồ thị có các cạnh (1, 2), (2, 3) và đỉnh 4 cô lập: - Kiểm tra giữa 1 và 3: Tồn tại đường đi $1 × o 2 × o 3$, in ra YES. - Nếu ki... | Cập nhật các biến / mảng trạng thái |
| 3 | Xuất kết quả chuẩn | Đối chiếu trạng thái cuối cùng | Output chuẩn: `NO` |

*Giải thích chi tiết:* Với đồ thị có các cạnh (1, 2), (2, 3) và đỉnh 4 cô lập:

- Kiểm tra giữa 1 và 3: Tồn tại đường đi $1 × o 2 × o 3$, in ra YES.
- Nếu kiểm tra giữa 1 và 4: Không có đường đi, in ra NO.

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

int n, m, s, t;
vector<vector<int>> adj;
vector<bool> visited;

void dfs(int u) {
visited[u] = true;
for (int v : adj[u]) {
if (!visited[v]) dfs(v);
}
}

int main() {
ios::sync_with_stdio(false);
cin.tie(nullptr);

if (!(cin >> n >> m >> s >> t)) return 0;
if (n <= 0) return 0;

adj.assign(n + 1, vector<int>());
visited.assign(n + 1, false);

for (int i = 0; i < m; ++i) {
int u, v;
cin >> u >> v;
adj[u].push_back(v);
adj[v].push_back(u);
}

dfs(s);

if (visited[t]) cout << "YES\n";
else cout << "NO\n";
return 0;
}
```
