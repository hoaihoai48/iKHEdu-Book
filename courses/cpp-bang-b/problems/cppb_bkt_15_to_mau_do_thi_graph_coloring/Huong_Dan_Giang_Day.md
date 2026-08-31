# Hướng Dẫn Giảng Dạy: Tô Màu Đồ Thị (Graph K-Coloring)
Chuyên đề: **Thuật Toán Quay Lui & Nhánh Cận (Backtracking & Branch and Bound)**

**Phân loại chuyên đề:** `Challenge`

---

## 1. Mục Tiêu Học Tập & Chuẩn Đầu Ra (Learning Objectives)
* **Kỹ năng cốt lõi:** Nắm vững và làm chủ kỹ thuật: Tô Màu Đồ Thị (Graph K-Coloring).
* **Tư duy thuật toán:** Rèn luyện phản xạ xây dựng cây không gian trạng thái theo chuẩn mực `Choose` $\to$ `Explore` $\to$ `Unchoose` và phân biệt rõ ràng giữa Cắt tỉa ràng buộc (Feasibility Pruning) và Cắt tỉa tối ưu (Optimality Pruning).
* **Chuẩn code thi đấu:** Cài đặt C++ chuẩn thi đấu (Fast I/O, Safe Input, 0 `std::`, hoàn tác an toàn).

---

## 2. Phân Tích Đề Bài & Bản Chất Toán Học
* **Dữ liệu đầu vào:** - Dòng 1: 3 số nguyên $V, E, K$ ($1 \le V \le 12, 0 \le E \le V(V-1)/2, 1 \le K \le 4$).
- $E$ dòng tiếp theo: Mỗi dòng gồm 2 số nguyên $u, v$ mô tả một cạnh ($1 \le u, v \le V$).
* **Yêu cầu cốt lõi:** Cho đồ thị vô hướng $G = (V, E)$ gồm $V$ đỉnh và $E$ cạnh, cùng số màu $K$. Hãy kiểm tra xem có thể tô màu $V$ đỉnh bằng $K$ màu sao cho không có 2 đỉnh kề nhau có cùng màu hay không. In `YES` nếu tô được, ngược lại in `NO`.
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
4 5 3
1 2
2 3
3 4
4 1
1 3
```
* **Output:**
```text
YES
```
* **Phân tích thực thi:** Đồ thị có thể tô hợp lệ bằng 3 màu.

---

## 6. Phân Tích Độ Phức Tạp Thời Gian & Không Gian
* **Thời gian thực thi (Time Complexity):** $\mathcal{O}(K^V)$ (Pruned)
* **Bộ nhớ ngăn xếp (Call Stack Space):** $\Theta(V)$ (Độ sâu tối đa: $V$)
* **Bộ nhớ phụ trợ (Auxiliary Memory):** $\Theta(V)$
* **Ghi chú phân tích:** Kiểm tra đỉnh kề khác màu trước khi gọi đệ quy tiếp theo.

---

## 7. Các Bẫy Lỗi Lập Trình Kinh Điển (Bug Traps)
1. **Quên bước hoàn tác (Unchoose):** Làm rò rỉ trạng thái giữa các nhánh gây thiếu nghiệm.
2. **Hàm Bound sai:** Cắt tỉa nhầm nghiệm tối ưu trong các bài toán Branch & Bound.

---

## 8. Mã Nguồn Tham Chiếu C++ Chuẩn Thi Đấu
```cpp
#include <bits/stdc++.h>
using namespace std;

int V, E, K;
vector<int> adj[15];
int color[15];
bool possible = false;

bool isSafe(int u, int c) {
    for (int v : adj[u]) {
        if (color[v] == c) return false;
    }
    return true;
}

void backtrack(int u) {
    if (possible) return;
    if (u > V) {
        possible = true;
        return;
    }
    for (int c = 1; c <= K; ++c) {
        if (isSafe(u, c)) {
            color[u] = c;
            backtrack(u + 1);
            color[u] = 0;
            if (possible) return;
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    if (!(cin >> V >> E >> K)) return 0;
    for (int i = 0; i < E; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }
    memset(color, 0, sizeof(color));
    backtrack(1);
    cout << (possible ? "YES\n" : "NO\n");
    return 0;
}
```

---

## 9. Bài Toán Mở Rộng & Chuyển Giao (Transfer & Extensions)
* Nhận diện hiện tượng trùng lặp trạng thái trên đồ thị có hướng không chu trình (DAG) để chuẩn bị bước chuyển mình mang tính quyết định sang **Module 05: Quy Hoạch Động (Dynamic Programming)**.
