# Hướng Dẫn Giảng Dạy: Người Du Lịch (TSP) Nhánh Cận
Chuyên đề: **Bài 12: Thuật toán quay lui & nhánh cận**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho số lượng thành phố $N$ và ma trận chi phí vận tải $C$ kích thước $N \times N$, trong đó $C_{i, j}$ là chi phí bay từ thành phố $i$ đến thành phố $j$. Hãy áp dụng thuật toán Nhánh Cận (Branch and Bound) với hàm cận dưới dựa trên cạnh có chi phí nhỏ nhất toàn đồ thị để tìm chu trình di chuyển có tổng chi phí thấp nhất.

- **Phương pháp tiếp cận — Quay lui & Nhánh cận (Backtracking):**
  - Xây dựng không gian trạng thái dạng cây tìm kiếm.
  - Thử từng khả năng, nếu vi phạm điều kiện ràng buộc thì tỉa nhánh sớm (nhánh cận) để giảm số trạng thái cần duyệt.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 4 0 10 15 20 10 0 35 25 1)
| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `4 0 10 15 20 10 0 35 25 15 35 0 30 ` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | Lộ trình tối ưu xuất phát từ thành phố 1 là: $1 \to 2 \to 4 \to 3 \to 1$. Tổng chi phí của hành trình là: $C_{1, 2} + C_... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `80` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* Lộ trình tối ưu xuất phát từ thành phố 1 là: $1 \to 2 \to 4 \to 3 \to 1$. Tổng chi phí của hành trình là: $C_{1, 2} + C_{2, 4} + C_{4, 3} + C_{3, 1} = 10 + 25 + 30 + 15 = 80$.

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- **Bẫy 1 — Tràn số nguyên:** Khi tính toán tổng, tích hoặc lũy thừa lớn hơn $2 \cdot 10^9$, bắt buộc phải sử dụng kiểu dữ liệu `long long` (64-bit) để tránh tràn số âm.
- **Bẫy 2 — Chỉ số mảng & Giới hạn biên:** Chú ý giữa đánh chỉ số 0-based (`0 .. N-1`) và 1-based (`1 .. N`). Kiểm tra kỹ trường hợp $N = 1$ hoặc giá trị biên tối đa của đề bài.
- **Bẫy 3 — Tối ưu thời gian I/O:** Luôn sử dụng `ios::sync_with_stdio(false); cin.tie(nullptr);` ở đầu hàm `main()` để đọc ghi nhanh, tránh bị TLE khi số lượng testcase lớn.

---

## 4. Lời giải tham khảo
```cpp
#include <bits/stdc++.h>
using namespace std;

int n;
long long c[15][15];
bool visited[15];
long long min_edge = 1e9;
long long best_cost = 1e18;

void branchAndBound(int u, int count, long long current_cost) {
    // Optimality Pruning
    if (current_cost + (n - count + 1) * min_edge >= best_cost) return;

    if (count == n) {
        best_cost = min(best_cost, current_cost + c[u][1]);
        return;
    }

    for (int v = 2; v <= n; ++v) {
        if (!visited[v]) {
            visited[v] = true;
            branchAndBound(v, count + 1, current_cost + c[u][v]);
            visited[v] = false;
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    if (!(cin >> n)) return 0;
    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= n; ++j) {
            cin >> c[i][j];
            if (i != j) min_edge = min(min_edge, c[i][j]);
        }
    }
    memset(visited, false, sizeof(visited));
    visited[1] = true;
    branchAndBound(1, 1, 0);
    cout << best_cost << "\n";
    return 0;
}
```
