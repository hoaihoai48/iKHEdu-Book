# Chuyên đề 19: Lý thuyết đồ thị cơ bản: Duyệt BFS & DFS

## 1. Bản chất đồ thị & các phương pháp biểu diễn

Đồ thị $G = (V, E)$ là cấu trúc toán học biểu diễn tập hợp các đỉnh (Vertices — $V$) và các cạnh nối giữa chúng (Edges — $E$). Đồ thị có thể là vô hướng (Undirected) hoặc có hướng (Directed), có trọng số hoặc không có trọng số.

![Biểu diễn Đồ thị: Ma trận kề vs Danh sách kề](/Users/vu/Developer/ikhEdu_lessons/courses/cpp-bang-b/lessons/lesson-19-ly-thuyet-do-thi-bfs-dfs/assets/graph_representations_vi.svg)

### 1.1. Ma trận kề (adjacency matrix)
* Mảng 2 chiều `int adj[N][N]`: `adj[u][v] = 1` nếu có cạnh nối giữa $u$ và $v$.
* **Ưu điểm:** Kiểm tra cạnh $(u, v)$ trong $\mathcal{O}(1)$.
* **Nhược điểm:** Tốn $\mathcal{O}(N^2)$ bộ nhớ. Khi $N = 10^5$, ma trận cần $40\text{GB}$ RAM $\implies$ Sập bộ nhớ ngay lập tức (MLE). Chỉ dùng khi $N \le 1000$.

### 1.2. Danh sách kề (adjacency list — Chuẩn mực thi đấu)
* Sử dụng mảng các vector `vector<int> adj[N + 1]`: `adj[u]` chứa toàn bộ các đỉnh kề trực tiếp với $u$.

* **Bộ nhớ:** Đúng $\mathcal{O}(V + E)$, cực kỳ tiết kiệm và tối ưu cho đồ thị thưa trong lập trình thi đấu ($N, M \le 2 \cdot 10^5$).
* **Duyệt đỉnh kề:** `for (int v : adj[u])` tốn thời gian tỷ lệ thuận với bậc của đỉnh $\mathcal{O}(\text{deg}(u))$.

## 2. Hai chiến lược duyệt đồ thị kinh điển: BFS vs DFS

![So sánh BFS vs DFS](/Users/vu/Developer/ikhEdu_lessons/courses/cpp-bang-b/lessons/lesson-19-ly-thuyet-do-thi-bfs-dfs/assets/bfs_vs_dfs_traversal_vi.svg)

### 2.1. Tìm kiếm theo chiều rộng (breadth-first search — BFS)
* Sử dụng **Hàng đợi (Queue)**, lan tỏa theo từng tầng bán kính $d = 0, 1, 2, \dots$ tính từ đỉnh nguồn $S$.
* **Đặc tính vàng:** Tìm đường đi có ít cạnh nhất (ngắn nhất) trên đồ thị không trọng số.

### 2.2. Tìm kiếm theo chiều sâu (depth-first search — DFS)
* Sử dụng **Đệ quy (hoặc Stack)**, đi sâu hết mức có thể trên một nhánh cho đến khi gặp ngõ cụt thì quay lui (Backtracking).
* **Đặc tính vàng:** Cực kỳ hiệu quả để đếm thành phần liên thông, phát hiện chu trình, kiểm tra tính liên thông, định hướng cây DFS.

## 3. Ứng dụng: Đếm số thành phần liên thông & kiểm tra chu trình

![Đếm số thành phần liên thông](/Users/vu/Developer/ikhEdu_lessons/courses/cpp-bang-b/lessons/lesson-19-ly-thuyet-do-thi-bfs-dfs/assets/connected_components_vi.svg)

* **Thuật toán đếm thành phần liên thông:** Duyệt qua mọi đỉnh $i \in [1, N]$. Nếu đỉnh $i$ chưa được thăm (`!visited[i]`), tăng biến đếm số thành phần liên thông `components++` và gọi `DFS(i)` để loang thăm toàn bộ các đỉnh thuộc cùng thành phần.
* **Phát hiện chu trình trên đồ thị vô hướng bằng DFS:** Khi duyệt từ $u$ sang đỉnh kề $v$, nếu $v$ đã được thăm (`visited[v] == true`) và $v \ne parent[u]$, ta khẳng định đồ thị **CÓ CHU TRÌNH**!

## 4. Các bẫy lỗi lập trình kinh điển (bug traps)

1. **Bẫy thêm cạnh đồ thị vô hướng chỉ thêm 1 chiều:**
* Với đồ thị vô hướng, cạnh giữa $u$ và $v$ phải thêm cả 2 chiều: `adj[u].push_back(v); adj[v].push_back(u);`. Quên thêm chiều thứ hai làm đồ thị biến thành đồ thị có hướng sai hoàn toàn.
2. **Bẫy tràn ngăn xếp đệ quy (Stack Overflow) khi DFS đồ thị sâu:**
* Nếu đồ thị là một đường thẳng $N = 2 \cdot 10^5$ đỉnh, hàm đệ quy `DFS` sẽ gọi sâu $2 \cdot 10^5$ tầng, vượt quá giới hạn ngăn xếp (Call Stack) của một số hệ điều hành và gây Runtime Error.
3. **Bẫy cạnh lặp và khuyên (Multiple Edges & Self-loops):**
* Đề bài có thể cho nhiều cạnh nối giữa cùng một cặp đỉnh $(u, v)$ hoặc cạnh tự nối $u \to u$. Cần kiểm tra hoặc xử lý cẩn thận nếu thuật toán yêu cầu tính toán bậc hoặc trọng số tối thiểu.

## 5. Mẫu cài đặt chuẩn thi đấu (competitive templates)

### Mẫu 1: DFS đếm số thành phần liên thông và tìm kích thước từng thành phần

> ⚠️ **Lưu ý về Stack Overflow:** Hàm DFS đệ quy dưới đây có thể gây tràn ngăn xếp hệ thống (Segmentation Fault) khi đồ thị có dạng đường thẳng $N = 2 \times 10^5$ đỉnh (độ sâu đệ quy lên tới $N$ tầng). Trong thi đấu thực tế, nên dùng **DFS bằng `std::stack` tường minh** hoặc thiết lập `ulimit -s unlimited` (Linux) trước khi chạy. Mẫu đệ quy được giữ lại ở đây vì tính trực quan sư phạm.

```cpp
#include <bits/stdc++.h>
using namespace std;

int n, m;
vector<vector<int>> adj;

vector<bool> visited;

int dfs(int u) {
    visited[u] = true;
    int comp_size = 1;
    for (int v : adj[u]) {
        if (!visited[v]) {
            comp_size += dfs(v);
        }
    }
    return comp_size;
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

    int component_count = 0;
    vector<int> component_sizes;

    for (int i = 1; i <= n; ++i) {
        if (!visited[i]) {
            component_count++;
            int sz = dfs(i);
            component_sizes.push_back(sz);
        }
    }

    cout << component_count << "\n";
    for (int i = 0; i < (int)component_sizes.size(); ++i) {
        cout << component_sizes[i] << (i + 1 == (int)component_sizes.size() ? "" : " ");
    }
    cout << "\n";

    return 0;
}
```

### Mẫu 2: Phát hiện chu trình trên đồ thị vô hướng bằng DFS

```cpp
#include <bits/stdc++.h>
using namespace std;

int n, m;
vector<vector<int>> adj;

vector<bool> visited;

bool has_cycle = false;

void dfs_cycle(int u, int p) {
    visited[u] = true;
    for (int v : adj[u]) {
        if (!visited[v]) {
            dfs_cycle(v, u);
        } else if (v != p) {
            has_cycle = true; // Gặp lại đỉnh đã thăm khác cha -> Chu trình!

        }
    }
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

    for (int i = 1; i <= n; ++i) {
        if (!visited[i]) {
            dfs_cycle(i, 0);
        }
    }

    if (has_cycle) {
        cout << "YES\n";
    } else {
        cout << "NO\n";
    }

    return 0;
}
```

## Câu hỏi trắc nghiệm củng cố khái niệm

#### Câu 1 (Bộ nhớ của Danh sách kề):

Với đồ thị gồm $V$ đỉnh và $E$ cạnh, danh sách kề `vector<int> adj[V + 1]` chiếm dung lượng bộ nhớ là bao nhiêu?

- **A.** $\mathcal{O}(V^2)$

- **B.** **[Đáp án đúng]** $\mathcal{O}(V + E)$

- **C.** $\mathcal{O}(E^2)$

- **D.** $\mathcal{O}(V \cdot E)$

> *Giải thích:* Mỗi đỉnh lưu một vector chứa các cạnh kề. Tổng số phần tử trong toàn bộ các vector đúng bằng $2E$ (vô hướng) hoặc $E$ (có hướng) $\implies \mathcal{O}(V + E)$.

#### Câu 2 (Độ phức tạp thời gian duyệt toàn bộ đồ thị):

Thuật toán BFS và DFS khi duyệt qua toàn bộ đồ thị biểu diễn bằng danh sách kề có độ phức tạp thời gian là:

- **A.** $\mathcal{O}(V \cdot E)$

- **B.** **[Đáp án đúng]** $\mathcal{O}(V + E)$

- **C.** $\mathcal{O}(V^2)$

- **D.** $\mathcal{O}(E \log V)$

> *Giải thích:* Mỗi đỉnh được thăm đúng 1 lần ($\mathcal{O}(V)$) và mỗi cạnh được duyệt qua tối đa 2 lần ($\mathcal{O}(E)$) $\implies$ Tổng thời gian $\mathcal{O}(V + E)$.

#### Câu 3 (Điều kiện phát hiện chu trình đồ thị vô hướng):

Trong hàm `DFS(u, p)` với $p$ là đỉnh cha trực tiếp của $u$, dấu hiệu nào khẳng định có chu trình?

- **A.** Gặp một đỉnh kề $v$ chưa được thăm.

- **B.** **[Đáp án đúng]** Gặp đỉnh kề $v$ đã được thăm ($visited[v] = true$) và $v \ne p$.

- **C.** Đỉnh $u$ có bậc lớn hơn 2.

- **D.** Khi DFS kết thúc mà còn đỉnh chưa thăm.

> *Giải thích:* Nếu đi tới một đỉnh đã thăm mà không phải quay ngược lại đỉnh vừa sinh ra mình, ta vừa đi vòng qua một chu trình khép kín.

#### Câu 4 (Tìm đường đi ngắn nhất không trọng số):

Để tìm đường đi qua ít cạnh nhất từ đỉnh $S$ đến đỉnh $T$, thuật toán nào luôn đảm bảo tìm ra kết quả tối ưu đầu tiên?

- **A.** DFS.

- **B.** **[Đáp án đúng]** BFS (Duyệt theo chiều rộng).

- **C.** Tìm kiếm nhị phân.

- **D.** Quy hoạch động 1D.

> *Giải thích:* BFS lan tỏa theo từng tầng khoảng cách tăng dần ($0, 1, 2...$), nên lần đầu tiên chạm tới $T$ chắc chắn là đường đi ngắn nhất.

#### Câu 5 (Bậc của đỉnh trong đồ thị vô hướng):

Tổng bậc của toàn bộ các đỉnh trong đồ thị vô hướng $G = (V, E)$ luôn bằng:

- **A.** $E$

- **B.** **[Đáp án đúng]** $2E$ (Định lý Bắt tay — Handshaking Lemma).

- **C.** $V$

- **D.** $V + E$

> *Giải thích:* Mỗi cạnh nối giữa 2 đỉnh đóng góp đúng 1 bậc vào đỉnh $u$ và 1 bậc vào đỉnh $v \implies \sum \text{deg}(v) = 2E$.

#### Câu 6 (Kiểm tra đồ thị liên thông):

Đồ thị vô hướng $G$ gồm $N$ đỉnh là liên thông khi và chỉ khi:

- **A.** Số cạnh $M \ge N$.

- **B.** **[Đáp án đúng]** Sau khi gọi `DFS(1)` (hoặc `BFS(1)`), toàn bộ $N$ đỉnh đều có $visited[i] = true$ (số thành phần liên thông đúng bằng 1).

- **C.** Đồ thị không có chu trình.

- **D.** Mọi đỉnh đều có bậc chẵn.

> *Giải thích:* Liên thông nghĩa là từ một đỉnh bất kỳ có thể đi tới mọi đỉnh còn lại trong đồ thị.

#### Câu 7 (Thứ tự duyệt Topo trên DAG):

Thuật toán Sắp xếp Tô-pô (Topological Sort) chỉ áp dụng được trên loại đồ thị nào?

- **A.** Đồ thị vô hướng bất kỳ.

- **B.** **[Đáp án đúng]** Đồ thị có hướng không có chu trình (Directed Acyclic Graph — DAG).

- **C.** Đồ thị có chu trình âm.

- **D.** Cây nhị phân hoàn hảo.

> *Giải thích:* Tô-pô sắp xếp các đỉnh theo thứ tự tiên quyết, nếu có chu trình thì sẽ xảy ra mâu thuẫn phụ thuộc vòng tròn.

#### Câu 8 (Đồ thị đầy đủ $K_N$):

Đồ thị đơn vô hướng đầy đủ gồm $N$ đỉnh có chính xác bao nhiêu cạnh?

- **A.** $N(N - 1)$

- **B.** **[Đáp án đúng]** $\frac{N(N - 1)}{2}$

- **C.** $N^2$

- **D.** $2N - 1$

> *Giải thích:* Mỗi cặp 2 đỉnh bất kỳ đều có 1 cạnh nối $\implies \binom{N}{2} = \frac{N(N-1)}{2}$.

#### Câu 9 (Độ sâu của cây DFS):

Khi DFS trên một đồ thị hình đường thẳng (Line Graph) gồm $N = 10^5$ đỉnh, ngăn xếp đệ quy sẽ đạt độ sâu tối đa là:

- **A.** $\mathcal{O}(1)$

- **B.** **[Đáp án đúng]** $\mathcal{O}(N) = 10^5$ tầng đệ quy.

- **C.** $\mathcal{O}(\log N)$

- **D.** $\mathcal{O}(\sqrt{N})$

> *Giải thích:* Nhánh đệ quy đi thẳng từ đầu mút này sang đầu mút kia mà không rẽ nhánh $\implies$ Độ sâu bằng $N$.

#### Câu 10 (Cạnh cầu trong đồ thị Bridge):

Một cạnh trong đồ thị vô hướng được gọi là Cạnh Cầu (Bridge) khi nào?

- **A.** Khi nó thuộc một chu trình.

- **B.** **[Đáp án đúng]** Khi xóa cạnh đó đi, số thành phần liên thông của đồ thị sẽ tăng lên.

- **C.** Khi trọng số của nó lớn nhất.

- **D.** Khi nó nối với đỉnh cô lập.

> *Giải thích:* Cạnh cầu là nút thắt duy nhất kết nối 2 phần của đồ thị, loại bỏ nó sẽ làm đồ thị bị chia cắt.

#### Câu 11 (Đỉnh khớp trong đồ thị Articulation Point):

Một đỉnh $u$ được gọi là Đỉnh Khớp (Cut Vertex) khi nào?

- **A.** Khi $u$ có bậc lớn hơn 3.

- **B.** **[Đáp án đúng]** Khi xóa đỉnh $u$ cùng toàn bộ các cạnh kề với nó, số thành phần liên thông của đồ thị tăng lên.

- **C.** Khi $u$ là đỉnh gốc của DFS.

- **D.** Khi $u$ không có cạnh nối.

> *Giải thích:* Đỉnh khớp là điểm chốt liên kết, loại bỏ nó sẽ làm mất tính liên thông giữa các vùng khác.

#### Câu 12 (Cây khung của đồ thị Spanning Tree):

Cây khung của một đồ thị vô hướng liên thông gồm $N$ đỉnh là:

- **A.** Một đồ thị con chứa $N$ đỉnh và $N$ cạnh.

- **B.** **[Đáp án đúng]** Một đồ thị con chứa toàn bộ $N$ đỉnh, đúng $N-1$ cạnh và không chứa chu trình.

- **C.** Đường đi ngắn nhất giữa 2 đỉnh.

- **D.** Đồ thị hai phía.

> *Giải thích:* Cây khung là cây tối thiểu kết nối toàn bộ $N$ đỉnh của đồ thị ban đầu.

#### Câu 13 (Đồ thị Euler):

Một đồ thị vô hướng liên thông có chu trình Euler (đi qua mỗi cạnh đúng 1 lần và quay về điểm xuất phát) khi và chỉ khi:

- **A.** Mọi đỉnh đều có bậc lẻ.

- **B.** **[Đáp án đúng]** Mọi đỉnh của đồ thị đều có bậc chẵn.

- **C.** Số cạnh bằng số đỉnh trừ 1.

- **D.** Có đúng 2 đỉnh bậc lẻ.

> *Giải thích:* Định lý Euler: Bậc chẵn đảm bảo mỗi khi đi vào một đỉnh bằng 1 cạnh thì luôn có 1 cạnh khác chưa dùng để đi ra.

#### Câu 14 (BFS đa nguồn Multi-source BFS):

Khi cần tìm khoảng cách ngắn nhất từ một tập hợp gồm $K$ đỉnh nguồn đến mọi đỉnh còn lại trên đồ thị, kỹ thuật chuẩn mực là:

- **A.** Chạy $K$ lần BFS độc lập tốn $\mathcal{O}(K \cdot (V + E))$.

- **B.** **[Đáp án đúng]** Đẩy toàn bộ $K$ đỉnh nguồn vào Queue ban đầu với khoảng cách bằng 0 rồi chạy đúng 1 lần BFS trong $\mathcal{O}(V + E)$.

- **C.** Dùng thuật toán Floyd-Warshall $\mathcal{O}(V^3)$.

- **D.** Sắp xếp các đỉnh.

> *Giải thích:* Multi-source BFS lan tỏa đồng thời từ toàn bộ các nguồn, đỉnh nào gần nguồn bất kỳ nhất sẽ được thăm trước.

#### Câu 15 (Đồ thị có hướng liên thông mạnh SCC):

Một đồ thị có hướng được gọi là Liên thông mạnh (Strongly Connected) khi:

- **A.** Có ít nhất một đỉnh đi được tới mọi đỉnh.

- **B.** **[Đáp án đúng]** Giữa hai đỉnh bất kỳ $u$ và $v$, luôn tồn tại đường đi từ $u \to v$ và đường đi từ $v \to u$.

- **C.** Không có chu trình.

- **D.** Số đỉnh bằng số cạnh.

> *Giải thích:* Liên thông mạnh đòi hỏi sự thông suốt hai chiều giữa mọi cặp đỉnh trong đồ thị có hướng (thuật toán Tarjan / Kosaraju).

## Ma trận bài tập thực hành (P0 → P5)

| Mã Bài Tập | Tên Bài Toán | Mức Độ | Trọng Tâm Kiến Thức & Kỹ Năng Đồ Thị |
|---|---|:---:|---|
| `CPPB-GRA-01` | Chuyển Đổi Danh Sách Cạnh Sang Danh Sách Kề | **P0** | Xây dựng `adj[u]` và tính bậc của từng đỉnh trong $\mathcal{O}(V+E)$. |
| `CPPB-GRA-02` | Duyệt Đồ Thị Theo Chiều Sâu (DFS Traversal) | **P1** | In thứ tự các đỉnh được thăm bằng hàm đệ quy `DFS`. |
| `CPPB-GRA-03` | Duyệt Đồ Thị Theo Chiều Rộng (BFS Traversal) | **P1** | In thứ tự các đỉnh được thăm bằng hàng đợi `std::queue`. |
| `CPPB-GRA-04` | Đếm Số Thành Phần Liên Thông | **P2** | Đếm số lần gọi `DFS` trên các đỉnh chưa thăm. |
| `CPPB-GRA-05` | Tìm Kích Thước Thành Phần Liên Thông Lớn Nhất | **P2** | DFS tích lũy số lượng đỉnh trong từng vùng liên thông. |
| `CPPB-GRA-06` | Kiểm Tra Đường Đi Giữa Hai Đỉnh (Path Finding) | **P2** | DFS / BFS kiểm tra xem $T$ có đến được từ $S$. |
| `CPPB-GRA-07` | Phát Hiện Chu Trình Trên Đồ Thị Vô Hướng | **P2** | DFS phát hiện cạnh ngược nối về đỉnh đã thăm khác cha. |
| `CPPB-GRA-08` | Tìm Đường Đi Ngắn Nhất Bằng BFS | **P3** | Tính mảng `dist` và dùng mảng `parent` truy vết đường đi. |
| `CPPB-GRA-09` | Kiểm Tra Đồ Thị Cây (Tree Verification) | **P3** | Kiểm tra đồ thị liên thông và có đúng $N-1$ cạnh. |
| `CPPB-GRA-10` | Sắp Xếp Tô-pô (Topological Sort) Trên DAG | **P3** | Thuật toán Kahn dùng Bán bậc vào (In-degree) hoặc DFS hậu thứ tự. |
| `CPPB-GRA-11` | Tìm Chu Trình Độ Dài Nhỏ Nhất (Shortest Cycle) | **P3** | BFS từ từng đỉnh tìm cạnh ngược ngắn nhất. |
| `CPPB-GRA-12` | Đếm Cặp Đỉnh Không Thể Đi Tới Nhau | **P4** | Tổ hợp trên kích thước các thành phần liên thông: $\sum sz_i \times (N - sz_i) / 2$. |
| `CPPB-GRA-13` | Multi-Source BFS Lan Tỏa Virus | **P4** | Khởi tạo Queue với toàn bộ các ổ dịch, lan tỏa theo thời gian. |
| `CPPB-GRA-14` | Tìm Cạnh Cầu Trên Đồ Thị (Bridge Finding) | **P4** | Thuật toán Tarjan cơ bản với mảng `num` và `low`. |
| `CPPB-GRA-15` | Mạng Lưới Giao Thông Tối Ưu Olympic (Mastery) | **P5** | Bài toán đồ thị tổng hợp kết hợp liên thông và đường đi tối ưu. |
