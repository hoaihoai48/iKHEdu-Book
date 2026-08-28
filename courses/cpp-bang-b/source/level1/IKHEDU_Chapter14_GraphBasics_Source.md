# TÀI LIỆU GỐC — CHƯƠNG 14: LÝ THUYẾT ĐỒ THỊ CƠ BẢN (GRAPH BASICS)

## Bản đồ chương

| Trường | Nội dung |
|---|---|
| Mục tiêu | Nắm vững cách mô hình hóa mạng lưới dữ liệu thành đỉnh (Vertices) và cạnh (Edges); biểu diễn đồ thị bằng Danh sách kề (`vector<vector<int>>`); cài đặt 2 thuật toán duyệt kinh điển: DFS (Duyệt theo chiều sâu) và BFS (Duyệt theo chiều rộng); giải bài toán loang trên lưới (Flood Fill) |
| Kiến thức cần có | Mảng 2D (`vector<vector<int>>`), đệ quy, cấu trúc hàng đợi `queue` |
| Phạm vi | Biểu diễn đồ thị (Danh sách kề), Duyệt theo chiều sâu (DFS), Duyệt theo chiều rộng (BFS), Đếm thành phần liên thông, Tìm đường đi ngắn nhất không trọng số, Loang trên lưới ô vuông (Flood Fill) |
| Số bài | 4 bài học lý thuyết & ví dụ mẫu + 1 bài luyện tập phân tầng |
| Tổng bài tập | 12 bài tập tự chứa (Tầng A: 4 bài, Tầng B: 4 bài, Tầng C: 4 bài) |

### Learning outcomes

Sau chương này, em có thể:
1. Biểu diễn đồ thị vô hướng/có hướng $N$ đỉnh $M$ cạnh bằng danh sách kề `vector<vector<int>> adj` tối ưu bộ nhớ $\mathcal{O}(N + M)$ — `LO-01`.
2. Cài đặt DFS để duyệt và đếm số lượng thành phần liên thông của đồ thị — `LO-02`.
3. Cài đặt BFS bằng `queue` để tìm đường đi ngắn nhất (số cạnh ít nhất) giữa hai đỉnh trong $\mathcal{O}(N + M)$ — `LO-03`.
4. Áp dụng thuật toán Flood Fill giải các bài toán loang diện tích trên ma trận ô vuông — `LO-04`.

### Câu hỏi trung tâm của chương

> **Làm thế nào để tìm đường đi ngắn nhất trong một mê cung hoặc kiểm tra xem hai máy tính có thể kết nối với nhau không?**

---

### Bài 14.1 — Biểu diễn đồ thị và Danh sách kề

#### 1. Khái niệm & Cấu trúc Danh sách kề
- Dùng `vector<vector<int>> adj(n + 1)` biểu diễn đồ thị với bộ nhớ $\mathcal{O}(N + M)$.

---

#### 2. Bài toán mẫu có hướng dẫn

> **Bài toán mẫu 14.1: Mạng Lưới Tuyến Xe Být Thủ Đô Hà Nội**  
> **Bối cảnh:** Sở Giao thông Vận tải Hà Nội quản lý $N$ trạm trung chuyển và $M$ tuyến đường hai chiều kết nối trực tiếp giữa các trạm.  
> **Nhiệm vụ:** Hãy in ra bậc kết nối và danh sách các trạm kề của từng trạm trung chuyển.  
> **Input:** `3 2` \ `1 2` \ `2 3` $\implies$ **Output:** `Dinh 1: bac 1, ke voi 2`...

#### Cài đặt C++
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<vector<int>> adj(n + 1);
    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    for (int u = 1; u <= n; u++) {
        cout << "Dinh " << u << ": bac " << adj[u].size() << ", ke voi";
        for (int v : adj[u]) cout << " " << v;
        cout << "\n";
    }

    return 0;
}
```

---

#### 3. Bài tập thực hành Bài 14.1

##### Bài 14.1.1 — Tìm Đỉnh Có Bậc Lớn Nhất Trong Mạng Lưới
- **Bối cảnh:** Cho đồ thị vô hướng $N$ đỉnh $M$ cạnh. Tìm đỉnh có số lượng liên kết nhiều nhất và bậc của đỉnh đó.
- **Input:** `4 3` \ `1 2` \ `2 3` \ `2 4` $\implies$ **Output:** `2 3` (đỉnh 2 có bậc 3).

##### Bài 14.1.2 — Đếm Số Cạnh Của Đồ Thị Có Hướng
- **Bối cảnh:** Nhập ma trận kề $N \times N$. Hãy in ra số lượng cạnh có hướng của đồ thị.
- **Input:** `3` \ `0 1 0` \ `0 0 1` \ `1 0 0` $\implies$ **Output:** `3`

---

### Bài 14.2 — Duyệt theo chiều sâu (DFS) và Đếm thành phần liên thông

#### 1. Khái niệm & Thuật toán
- DFS và mảng đánh dấu `visited` để đếm số thành phần liên thông.

---

#### 2. Bài toán mẫu có hướng dẫn

> **Bài toán mẫu 14.2: Quy Hoạch Mạng Cáp Quang Độc Lập FPT Telecom**  
> **Bối cảnh:** FPT Telecom rà soát $N$ máy chủ và $M$ tuyến cáp kết nối để xác định số lượng mạng con độc lập (thành phần liên thông).  
> **Input:** `4 2` \ `1 2` \ `3 4` $\implies$ **Output:** `2` (nhóm {1, 2} và nhóm {3, 4}).

#### Cài đặt C++
```cpp
#include <bits/stdc++.h>
using namespace std;

void dfs(int u, const vector<vector<int>> &adj, vector<bool> &visited) {
    visited[u] = true;
    for (int v : adj[u]) {
        if (!visited[v]) dfs(v, adj, visited);
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<vector<int>> adj(n + 1);
    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    vector<bool> visited(n + 1, false);
    int connectedComponents = 0;
    for (int i = 1; i <= n; i++) {
        if (!visited[i]) {
            connectedComponents++;
            dfs(i, adj, visited);
        }
    }

    cout << connectedComponents << "\n";
    return 0;
}
```

---

#### 3. Bài tập thực hành Bài 14.2

##### Bài 14.2.1 — Kiểm Tra Tính Liên Thông Toàn Mạng
- **Bối cảnh:** Cho đồ thị $N$ đỉnh $M$ cạnh. In `YES` nếu đồ thị liên thông hoàn toàn (1 thành phần liên thông duy nhất), ngược lại in `NO`.
- **Input:** `3 2` \ `1 2` \ `2 3` $\implies$ **Output:** `YES`

##### Bài 14.2.2 — Đếm Số Đỉnh Thuộc Cùng Thành Phần Liên Thông Với S
- **Bối cảnh:** Cho đỉnh nguồn $S$. Đếm xem có bao nhiêu đỉnh có thể đi tới được từ $S$ bằng DFS.
- **Input:** `4 2 1` \ `1 2` \ `3 4` $\implies$ **Output:** `2` (gồm 1 và 2)

---

### Bài 14.3 — Duyệt theo chiều rộng (BFS) và Đường đi ngắn nhất

#### 1. Khái niệm & Thuật toán
- BFS bằng `queue` đảm bảo tìm đường đi ít cạnh nhất trên đồ thị không trọng số.

---

#### 2. Bài toán mẫu có hướng dẫn

> **Bài toán mẫu 14.3: Đường Bay Cấp Cứu Y Tế Khẩn Cấp**  
> **Bối cảnh:** Trực thăng cấp cứu từ bệnh viện dã chiến đặt tại trạm $S$. Tìm số chặng bay ít nhất từ $S$ đến tất cả các trạm cứu hộ khác trên bản đồ.  
> **Input:** `4 3 1` \ `1 2` \ `2 3` \ `1 4` $\implies$ **Output:** `0 1 2 1`.

#### Cài đặt C++
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, startNode;
    if (!(cin >> n >> m >> startNode)) return 0;

    vector<vector<int>> adj(n + 1);
    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    vector<int> dist(n + 1, -1);
    queue<int> q;

    dist[startNode] = 0;
    q.push(startNode);

    while (!q.empty()) {
        int u = q.front();
        q.pop();

        for (int v : adj[u]) {
            if (dist[v] == -1) {
                dist[v] = dist[u] + 1;
                q.push(v);
            }
        }
    }

    for (int i = 1; i <= n; i++) {
        cout << dist[i] << (i == n ? "" : " ");
    }
    cout << "\n";

    return 0;
}
```

---

#### 3. Bài tập thực hành Bài 14.3

##### Bài 14.3.1 — Tìm Khoảng Cách Giữa Hai Trạm S và T
- **Bối cảnh:** Tìm số chặng bay ít nhất từ $S$ đến $T$. Nếu không có đường, in `-1`.
- **Input:** `4 3 1 3` \ `1 2` \ `2 3` \ `1 4` $\implies$ **Output:** `2`

##### Bài 14.3.2 — Truy Vết Đường Đi Ngắn Nhất Bằng Mảng Parent
- **Bối cảnh:** In dãy các đỉnh trên đường đi ngắn nhất từ $S$ đến $T$ bằng mảng `parent`.
- **Input:** `3 2 1 3` \ `1 2` \ `2 3` $\implies$ **Output:** `1 2 3`

---

### Bài 14.4 — Duyệt đồ thị trên lưới ô vuông (Flood Fill)

#### 1. Khái niệm & Mảng 4 hướng
- Mảng di chuyển: `dr = {-1, 1, 0, 0}`, `dc = {0, 0, -1, 1}`.

---

#### 2. Bài toán mẫu có hướng dẫn

> **Bài toán mẫu 14.4: Đếm Số Quần Đảo Trên Bản Đồ Hải Dương Học**  
> **Bối cảnh:** Bản đồ vệ tinh $N \times M$ ô, `#` là đảo nổi, `.` là mặt biển. Hai ô đất kề cạnh nhau thuộc cùng một quần đảo. Đếm số lượng quần đảo độc lập.  
> **Input:** `3 3` \ `##.` \ `..#` \ `..#` $\implies$ **Output:** `2`.

#### Cài đặt C++
```cpp
#include <bits/stdc++.h>
using namespace std;

int n, m;
vector<string> grid;
int dr[] = {-1, 1, 0, 0};
int dc[] = {0, 0, -1, 1};

void dfsGrid(int r, int c) {
    grid[r][c] = '.';
    for (int k = 0; k < 4; k++) {
        int nr = r + dr[k];
        int nc = c + dc[k];
        if (nr >= 0 && nr < n && nc >= 0 && nc < m && grid[nr][nc] == '#') {
            dfsGrid(nr, nc);
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    if (!(cin >> n >> m)) return 0;

    grid.resize(n);
    for (int i = 0; i < n; i++) cin >> grid[i];

    int islands = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (grid[i][j] == '#') {
                islands++;
                dfsGrid(i, j);
            }
        }
    }

    cout << islands << "\n";
    return 0;
}
```

---

#### 3. Bài tập thực hành Bài 14.4

##### Bài 14.4.1 — Diện Tích Quần Đảo Lớn Nhất
- **Bối cảnh:** Tìm số lượng ô đất `#` thuộc về quần đảo có diện tích lớn nhất trên bản đồ.
- **Input:** `3 3` \ `##.` \ `..#` \ `..#` $\implies$ **Output:** `2`

##### Bài 14.4.2 — Đếm Số Vùng Kín Được Bao Bọc Bởi Tường
- **Bối cảnh:** Đếm số ô `0` không chạm vào viền ngoài của ma trận bằng Flood Fill loang từ viền.
- **Input:** `3 3` \ `111` \ `101` \ `111` $\implies$ **Output:** `1`

---

### Bài 14.5 — Luyện tập tổng hợp và đánh giá chương

### Đề bài 12 bài tập phân tầng tự chứa (iKHEDU Standard)

#### Tầng A — Củng cố nền tảng (Rating 1000 - 1200)

##### Bài 14.5.1 — Biểu Diễn Mạng Lưới Giao Thông Bằng Danh Sách Kề
- **Bối cảnh:** Nhập đồ thị $N$ đỉnh $M$ cạnh, in bậc kết nối của từng đỉnh.

##### Bài 14.5.2 — Kiểm Tra Khả Năng Kết Nối Đường Truyền Bằng DFS
- **Bối cảnh:** Kiểm tra xem có tồn tại đường truyền dữ liệu từ máy chủ $S$ đến máy chủ $T$ không.

##### Bài 14.5.3 — Đếm Số Nhóm Bạn Trong Mạng Xã Hội Zalo
- **Bối cảnh:** Đếm số lượng thành phần liên thông trong mạng xã hội $N$ người dùng.

##### Bài 14.5.4 — Khoảng Cách Ngắn Nhất Bằng BFS
- **Bối cảnh:** Tìm số chặng kết nối ít nhất từ đỉnh $1$ đến đỉnh $N$ trên đồ thị không trọng số.

---

#### Tầng B — Vận dụng thi đấu (Rating 1200 - 1500)

##### Bài 14.5.5 — Lối Thoát Hiểm Khỏi Mê Cung Tòa Nhà
- **Bối cảnh:** BFS tìm đường đi ngắn nhất từ vị trí xuất phát `S` đến cửa thoát hiểm `E` trên ma trận mê cung $N \times M$.

##### Bài 14.5.6 — Phân Chia Hai Đội Thi Đấu (Bipartite Graph)
- **Bối cảnh:** Kiểm tra đồ thị có phải là đồ thị 2 phía hay không bằng thuật toán tô màu 2 màu BFS/DFS.

##### Bài 14.5.7 — Phát Hiện Chu Trình Trong Hệ Thống Ống Nước
- **Bối cảnh:** Sử dụng DFS và mảng 3 trạng thái màu (0: chưa thăm, 1: đang thăm, 2: đã xong) để phát hiện chu trình trên đồ thị có hướng.

##### Bài 14.5.8 — Truy Vết Tuyến Đường Giao Hàng Tiết Kiệm
- **Bối cảnh:** In dãy các đỉnh trên lộ trình đường đi ngắn nhất từ $S$ đến $T$.

---

#### Tầng C — Chuyển giao & Nâng cao (Rating 1500 - 1800)

##### Bài 14.5.9 — Lịch Trình Sản Xuất Linh Kiện VinFast (Topological Sort)
- **Bối cảnh:** Sắp xếp thứ tự các công đoạn sản xuất trên đồ thị có hướng không chu trình (DAG) bằng thuật toán Kahn BFS (bán bậc vào `inDegree`).

##### Bài 14.5.10 — Lan Truyền Tín Hiệu Cảnh Báo Sóng Thần (Multi-Source BFS)
- **Bối cảnh:** BFS đồng thời từ nhiều nguồn phát tín hiệu cảnh báo trên bờ biển.

##### Bài 14.5.11 — Kiểm Tra Điểm Yếu Tuyến Cáp Quang Biển (Tarjan Bridge)
- **Bối cảnh:** Tìm tất cả các cạnh cầu mà nếu đứt sẽ làm tăng số thành phần liên thông của mạng lưới.

##### Bài 14.5.12 — Tối Ưu Hóa Tuyến Đường Giao Hàng Shopee (Dijkstra)
- **Bối cảnh:** Tìm đường đi ngắn nhất trên đồ thị có trọng số dương bằng Hàng đợi ưu tiên.

---

### Bẫy lỗi thường gặp & Rubric đánh giá
| Lỗi thường gặp | Cách kiểm soát |
|---|---|
| Quên thêm cạnh 2 chiều trong đồ thị vô hướng | Luôn `push_back` cho cả `u -> v` và `v -> u` |
| Quên đánh dấu `visited` khi cho đỉnh vào hàng đợi BFS | Đánh dấu `dist[v] != -1` ngay tại lúc `q.push(v)` để tránh 1 đỉnh bị đưa vào hàng đợi nhiều lần |

### Rubric hoàn thành chương
| Mức độ | Tiêu chí đánh giá |
|---|---|
| **Cơ bản (Tầng A)** | Biểu diễn danh sách kề và cài đặt DFS/BFS chính xác. |
| **Vận dụng (Tầng B)** | Giải bài toán tìm đường trong mê cung và kiểm tra đồ thị 2 phía. |
| **Thành thạo (Tầng C)** | Cài đặt Topological Sort và Multi-source BFS. |
