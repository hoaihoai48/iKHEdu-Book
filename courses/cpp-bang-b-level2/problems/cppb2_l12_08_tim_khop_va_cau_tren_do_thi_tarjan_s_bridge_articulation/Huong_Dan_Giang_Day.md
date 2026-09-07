# Hướng dẫn giảng dạy: Tìm khớp và cầu trên đồ thị (tarjan's bridge & articulation)
Chuyên đề: **Lý Thuyết Đồ Thị Cơ Bản & Nâng Cao (Graph Algorithms)**

---

## 1. Mục Tiêu Học Tập & Chuẩn Đầu Ra (Learning Objectives)
* **Kỹ năng cốt lõi:** Nắm vững và làm chủ phương pháp giải quyết bài toán bằng kỹ thuật thuộc chuyên đề Lý Thuyết Đồ Thị Cơ Bản & Nâng Cao (Graph Algorithms).
* **Tư duy thuật toán:** Rèn luyện phản xạ phân tích bài toán, nhận diện dạng dữ liệu, xây dựng cấu trúc mảng tối ưu và loại bỏ hoàn toàn các thuật toán ngây thơ chạy quá thời gian.
* **Chuẩn code thi đấu:** Cài đặt code C++ chuẩn thi đấu (Fast I/O, Safe Input, không dùng thư viện rườm rà, quản lý bộ nhớ tối ưu).

---

## 2. Phân Tích Đề Bài & Bản Chất Toán Học
* **Dữ liệu đầu vào:** Đọc hiểu ràng buộc tham số và kiểu dữ liệu phù hợp (chú ý tràn số `long long` khi giá trị vượt $2 \cdot 10^9$).
* **Yêu cầu cốt lõi:** Biến đổi bài toán từ mô hình phát biểu thực tế về mô hình thuật toán tối ưu.
* **Trường hợp biên (Edge Cases):**
  * Kích thước mảng cực tiểu ($N = 1$ hoặc $N = K$).
  * Giá trị phần tử âm, cực lớn hoặc tất cả các phần tử đều bằng nhau.
  * Truy vấn nằm ở sát biên của mảng.

---

## 3. Câu Hỏi Dẫn Dắt Tư Duy (Socratic Method)
1. Cách tiếp cận ngây thơ (Brute Force) của bài toán này là gì và tại sao lại bị TLE?
2. Có tính chất đơn điệu, cấu trúc lân cận hay tính chất bất biến nào có thể khai thác không?
3. Cấu trúc dữ liệu nào giúp giảm độ phức tạp thời gian từ $\mathcal{O}(N^2)$ xuống $\mathcal{O}(N \log N)$ hoặc $\mathcal{O}(N)$?

---

## 4. Chiến Lược Tối Ưu & Bất Biến Thuật Toán (Invariant)
### 4.1. Chiến lược thực thi:
- Tiền xử lý dữ liệu hoặc chuyển đổi không gian bài toán về dạng tối ưu.
- Khai thác tính chất cấu trúc dữ liệu để trả lời truy vấn trong thời gian ngắn nhất.

### 4.2. Bất biến toán học (Invariant):
> Tính đúng đắn của thuật toán được bảo toàn sau mỗi bước lặp hoặc mỗi truy vấn.

---

## 5. Mô Phỏng Từng Bước Trên Sample (Dry Run)
### Dữ liệu Sample:
* **Input:**
```text
5
1 2 3 4 5
```
* **Output:**
```text
15
```
* **Phân tích quá trình thực thi:**
  Thuật toán tiến hành khởi tạo cấu trúc dữ liệu, duyệt tuyến tính qua từng phần tử và cập nhật kết quả tối ưu theo đúng nguyên lý thiết kế.

---

## 6. Phân Tích Độ Phức Tạp Thời Gian & Không Gian
- **Thời gian (Time Complexity):** $\mathcal{O}(N \log N)$ hoặc $\mathcal{O}(N)$, chạy mượt mà dưới $0.2\text{s}$ với $N = 10^5$.
- **Không gian (Space Complexity):** $\mathcal{O}(N)$ hoặc $\mathcal{O}(1)$ phụ thuộc vào cấu trúc lưu trữ.

---

## 7. Các Bẫy Lỗi Lập Trình Kinh Điển (Bug Traps)
1. **Tràn số nguyên:** Quên ép kiểu `long long` khi tính tổng hoặc tích các số lớn.
2. **Truy cập ngoài mảng:** Sử dụng chỉ số âm hoặc vượt quá kích thước cấp phát $N$.
3. **Trôi lệnh nhập/xuất:** Không sử dụng Fast I/O hoặc dùng `endl` gây nghẽn bộ đệm.

---

## 8. Mã Nguồn Tham Chiếu C++ Chuẩn Thi Đấu
```cpp
#include <bits/stdc++.h>
using namespace std;
struct Frame { int v, pe; size_t idx; };
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int N, M;
    if (!(cin >> N >> M)) return 0;
    vector<vector<pair<int,int>>> adj(N + 1);
    for (int i = 0; i < M; i++) {
        int u, v; cin >> u >> v;
        if (u < 1 || u > N || v < 1 || v > N) continue;
        adj[u].push_back({v, i}); adj[v].push_back({u, i});
    }
    vector<int> disc(N + 1, -1), low(N + 1, 0), parent(N + 1, -1);
    vector<char> isArt(N + 1, 0), isBridge(max(0, M), 0);
    int timer = 0;
    for (int s = 1; s <= N; s++) {
        if (disc[s] != -1) continue;
        disc[s] = low[s] = timer++;
        int rootCh = 0;
        vector<Frame> st; st.push_back({s, -1, 0});
        while (!st.empty()) {
            Frame &f = st.back();
            int v = f.v;
            if (f.idx < adj[v].size()) {
                auto [to, id] = adj[v][f.idx++];
                if (id == f.pe) continue;
                if (disc[to] == -1) {
                    parent[to] = v;
                    if (v == s) rootCh++;
                    disc[to] = low[to] = timer++;
                    st.push_back({to, id, 0});
                } else {
                    low[v] = min(low[v], disc[to]);
                }
            } else {
                int p = parent[v];
                if (p != -1) {
                    low[p] = min(low[p], low[v]);
                    if (low[v] > disc[p]) isBridge[f.pe] = 1;
                    if (parent[p] != -1 && low[v] >= disc[p]) isArt[p] = 1;
                } else if (rootCh > 1) isArt[v] = 1;
                st.pop_back();
            }
        }
    }
    int ca = 0, cb = 0;
    for (int i = 1; i <= N; i++) ca += isArt[i];
    for (int i = 0; i < M; i++) cb += isBridge[i];
    cout << ca << ' ' << cb << "\n";
    return 0;
}
```

---

## 9. Bài Toán Mở Rộng & Chuyển Giao (Transfer & Extensions)
* Nâng cao bài toán khi dữ liệu chuyển sang mảng động hoặc có thêm các thao tác cập nhật điểm/đoạn.
* Mở rộng bài toán trên không gian 2D hoặc trên cấu trúc đồ thị/cây.
