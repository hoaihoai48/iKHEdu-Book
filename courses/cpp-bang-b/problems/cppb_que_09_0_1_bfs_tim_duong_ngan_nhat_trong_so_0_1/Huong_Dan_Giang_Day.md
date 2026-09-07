# Hướng Dẫn Giảng Dạy: 0-1 BFS Tìm Đường Đi Ngắn Nhất Trọng Số 0/1

Chuyên đề: **Cấu Trúc Dữ Liệu Hàng Đợi (Queue, Deque) & Monotonic Deque**

---

## 1. Ý tưởng & Phân tích thuật toán

- **Bản chất bài toán:** Cho đồ thị có hướng $N$ đỉnh $M$ cạnh với trọng số mỗi cạnh thuộc $\{0, 1\}$. Hãy lập trình tìm khoảng cách ngắn nhất từ $S$ tới $D$. Nếu không đến được, in ra `-1`.

- **Phương pháp tiếp cận & Chiến lược tối ưu:**
- **Nguyên lý Hàng đợi chuẩn (Queue):** Vào trước Ra trước (FIFO), là cấu trúc nền tảng phục vụ duyệt đồ thị theo chiều rộng (BFS).
- **Hàng đợi hai đầu (Deque) & Monotonic Deque:**
  * Hỗ trợ thêm/xoá ở cả hai đầu trong $\mathcal{O}(1)$.
  * Khi trượt cửa sổ kích thước $K$, lưu chỉ số phần tử trong deque sao cho giá trị tương ứng luôn đơn điệu.
  * Loại bỏ phần tử trượt ra khỏi cửa sổ ở đầu trước (`pop_front()`) và loại bỏ phần tử kém tối ưu ở đầu sau (`pop_back()`).
- **Độ phức tạp:** Thời gian $\mathcal{O}(N)$, không gian phụ trợ $\mathcal{O}(K)$.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table)
Mẫu thử (Sample 1): Đầu vào: `4 4 1 2 1 2 3 0 3 4 1 1 4 1` $\implies$ Đầu ra kỳ vọng: `1`.

| Bước | Thao tác thực hiện | Dữ liệu biến đổi & Trạng thái | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Khởi tạo & Đọc dữ liệu | Nạp Input: `4 4 1 2 1 2 3 0 3 4 1 1 4 1` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Chạy thuật toán từng bước | Phân tích mẫu: Với đồ thị có đường đi từ 1 tới 3 qua cạnh trọng số 1, và từ 3 tới 4 qua cạnh trọng số 0: Tổng chi phí từ 1 tới 4 là $1 + 0 = 1$ đồng. ... | Cập nhật các biến / mảng trạng thái |
| 3 | Xuất kết quả chuẩn | Đối chiếu trạng thái cuối cùng | Output chuẩn: `1` |

*Giải thích chi tiết:* Với đồ thị có đường đi từ 1 tới 3 qua cạnh trọng số 1, và từ 3 tới 4 qua cạnh trọng số 0:
Tổng chi phí từ 1 tới 4 là $1 + 0 = 1$ đồng. Đây là chi phí tối thiểu.

---

## 3. Lưu ý & Bẫy lỗi thường gặp
* Lưu giá trị thay vì lưu chỉ số vị trí (index) trong Deque: Phải lưu index để kiểm tra điều kiện phần tử đã trượt ra khỏi cửa sổ $i - K$ hay chưa (`dq.front() <= i - K`).
* Quên kiểm tra `!dq.empty()` trước khi truy xuất `dq.front()` hoặc `dq.back()` gây crash chương trình.
* Không khởi tạo kết quả cho $K-1$ vị trí đầu tiên trước khi bắt đầu ghi nhận đáp án từ vị trí thứ $K$.

---

## 4. Lời giải tham khảo
```cpp
#include <bits/stdc++.h>
using namespace std;

const int INF = 1e9;

struct Edge {
    int to, weight;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;
    if (n <= 0) return 0;

    vector<vector<Edge>> adj(n + 1);
    for (int i = 0; i < m; ++i) {
        int u, v, w;
        cin >> u >> v >> w;
        adj[u].push_back({v, w});
        adj[v].push_back({u, w});
    }

    vector<int> dist(n + 1, INF);
    deque<int> dq;

    dist[1] = 0;
    dq.push_back(1);

    while (!dq.empty()) {
        int u = dq.front();
        dq.pop_front();

        for (const auto& edge : adj[u]) {
            int v = edge.to;
            int w = edge.weight;

            if (dist[u] + w < dist[v]) {
                dist[v] = dist[u] + w;
                if (w == 0) {
                    dq.push_front(v);
                } else {
                    dq.push_back(v);
                }
            }
        }
    }

    if (dist[n] == INF) cout << -1 << "\n";
    else cout << dist[n] << "\n";
    return 0;
}
```
