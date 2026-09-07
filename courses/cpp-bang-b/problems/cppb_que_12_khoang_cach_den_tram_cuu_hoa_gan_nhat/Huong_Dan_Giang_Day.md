# Hướng Dẫn Giảng Dạy: Khoảng Cách Đến Trạm Cứu Hỏa Gần Nhất (Multi-Source BFS)

Chuyên đề: **Cấu Trúc Dữ Liệu Hàng Đợi (Queue, Deque) & Monotonic Deque**

---

## 1. Ý tưởng & Phân tích thuật toán

- **Bản chất bài toán:** Cho bản đồ thành phố và danh sách vị trí các trạm cứu hỏa. Hãy lập trình tính khoảng cách ngắn nhất từ từng khu dân cư đến trạm cứu hỏa gần nhất.

- **Phương pháp tiếp cận & Chiến lược tối ưu:**
- **Nguyên lý Hàng đợi chuẩn (Queue):** Vào trước Ra trước (FIFO), là cấu trúc nền tảng phục vụ duyệt đồ thị theo chiều rộng (BFS).
- **Hàng đợi hai đầu (Deque) & Monotonic Deque:**
  * Hỗ trợ thêm/xoá ở cả hai đầu trong $\mathcal{O}(1)$.
  * Khi trượt cửa sổ kích thước $K$, lưu chỉ số phần tử trong deque sao cho giá trị tương ứng luôn đơn điệu.
  * Loại bỏ phần tử trượt ra khỏi cửa sổ ở đầu trước (`pop_front()`) và loại bỏ phần tử kém tối ưu ở đầu sau (`pop_back()`).
- **Độ phức tạp:** Thời gian $\mathcal{O}(N)$, không gian phụ trợ $\mathcal{O}(K)$.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table)
Mẫu thử (Sample 1): Đầu vào: `4 3 2 1 4 1 2 2 3 3 4` $\implies$ Đầu ra kỳ vọng: `0 1 1 0`.

| Bước | Thao tác thực hiện | Dữ liệu biến đổi & Trạng thái | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Khởi tạo & Đọc dữ liệu | Nạp Input: `4 3 2 1 4 1 2 2 3 3 4` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Chạy thuật toán từng bước | Phân tích mẫu: Với 4 khu dân cư nối liên tiếp 1 - 2 - 3 - 4 và trạm cứu hỏa đặt tại khu 2: - Khu 1: cách trạm cứu hỏa 1 bước. - Khu 2: có sẵn trạm cứu... | Cập nhật các biến / mảng trạng thái |
| 3 | Xuất kết quả chuẩn | Đối chiếu trạng thái cuối cùng | Output chuẩn: `0 1 1 0` |

*Giải thích chi tiết:* Với 4 khu dân cư nối liên tiếp 1 - 2 - 3 - 4 và trạm cứu hỏa đặt tại khu 2:
- Khu 1: cách trạm cứu hỏa 1 bước.
- Khu 2: có sẵn trạm cứu hỏa $\to$ khoảng cách 0.
- Khu 3: cách trạm cứu hỏa 1 bước.
- Khu 4: cách trạm cứu hỏa 2 bước.
Kết quả in ra: 1 0 1 2.

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

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, k;
    if (!(cin >> n >> m >> k)) return 0;
    if (n <= 0) return 0;

    vector<int> dist(n + 1, -1);
    queue<int> q;

    for (int i = 0; i < k; ++i) {
        int st;
        cin >> st;
        dist[st] = 0;
        q.push(st);
    }

    vector<vector<int>> adj(n + 1);
    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

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

    for (int i = 1; i <= n; ++i) {
        cout << dist[i] << (i == n ? "" : " ");
    }
    cout << "\n";
    return 0;
}
```
