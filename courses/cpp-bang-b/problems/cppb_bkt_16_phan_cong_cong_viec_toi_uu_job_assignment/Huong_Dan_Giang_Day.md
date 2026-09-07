# Hướng Dẫn Giảng Dạy: Phân Công Công Việc Tối Ưu (Job Assignment B&B)
Chuyên đề: **Bài 12: Thuật toán quay lui & nhánh cận**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho số lượng $N$ và ma trận chi phí phân công $C_{N \times N}$. Hãy áp dụng thuật toán Nhánh Cận (Branch and Bound) với hàm cận dưới tối ưu để tìm một phương án phân công toàn diện sao cho tổng chi phí hoàn thành tất cả các công việc là nhỏ nhất có thể.

- **Phương pháp tiếp cận — Quay lui & Nhánh cận (Backtracking):**
  - Xây dựng không gian trạng thái dạng cây tìm kiếm.
  - Thử từng khả năng, nếu vi phạm điều kiện ràng buộc thì tỉa nhánh sớm (nhánh cận) để giảm số trạng thái cần duyệt.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 4 9 2 7 8 6 4 3 7 5 8 1 8)
| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `4 9 2 7 8 6 4 3 7 5 8 1 8 7 6 9 4` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | Phương án phân công tối ưu nhất là: - Kỹ sư 1 làm việc 2 (chi phí $C_{1, 2} = 2$). - Kỹ sư 2 làm việc 1 (chi phí $C_{2, ... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `13` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* Phương án phân công tối ưu nhất là:
- Kỹ sư 1 làm việc 2 (chi phí $C_{1, 2} = 2$).
- Kỹ sư 2 làm việc 1 (chi phí $C_{2, 1} = 6$).
- Kỹ sư 3 làm việc 3 (chi phí $C_{3, 3} = 1$).
- Kỹ sư 4 làm việc 4 (chi phí $C_{4, 4} = 4$).
Tổng chi phí nhỏ nhất đạt được là $2 + 6 + 1 + 4 = 13$.

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
bool job_assigned[15];
long long min_row[15];
long long best_cost = 1e18;

void branchAndBound(int worker, long long current_cost) {
    // Optimality Pruning
    long long bound = current_cost;
    for (int w = worker; w <= n; ++w) bound += min_row[w];
    if (bound >= best_cost) return;

    if (worker > n) {
        best_cost = min(best_cost, current_cost);
        return;
    }

    for (int job = 1; job <= n; ++job) {
        if (!job_assigned[job]) {
            job_assigned[job] = true;
            branchAndBound(worker + 1, current_cost + c[worker][job]);
            job_assigned[job] = false;
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    if (!(cin >> n)) return 0;
    for (int i = 1; i <= n; ++i) {
        min_row[i] = 1e9;
        for (int j = 1; j <= n; ++j) {
            cin >> c[i][j];
            min_row[i] = min(min_row[i], c[i][j]);
        }
    }
    memset(job_assigned, false, sizeof(job_assigned));
    branchAndBound(1, 0);
    cout << best_cost << "\n";
    return 0;
}
```
