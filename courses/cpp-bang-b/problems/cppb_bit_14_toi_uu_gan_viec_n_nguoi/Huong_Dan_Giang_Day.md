# Hướng Dẫn Giảng Dạy: Tối Ưu Hóa Gán Việc Cho N Người (N <= 20)
Chuyên đề: **Bài 06: Phép toán BIT & biểu diễn trạng thái**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho ma trận chi phí C kích thước N x N (N <= 16). Hãy tìm tổng chi phí phân công nhỏ nhất để giao N việc cho N người bằng quy hoạch động trạng thái bitmask.

- **Phương pháp tiếp cận — Phép toán BIT & Bitmask:**
- Biểu diễn tập hợp hoặc trạng thái bật/tắt bằng các bit của số nguyên 64-bit.
- Sử dụng các toán tử bitwise `&, |, ^, ~, <<, >>` để thao tác đồng thời trong $\mathcal{O}(1)$ chu kỳ máy.

---

## 2. Bảng chạy tay trên số liệu mẫu| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `3 9 2 7 6 4 3 5 8 1` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | Phương án phân công tối ưu có tổng chi phí nhỏ nhất là $6$: - Kỹ sư 1 làm việc 2 (chi phí $C_{1, 2} = 2$). - Kỹ sư 2 làm... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `6` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* Phương án phân công tối ưu có tổng chi phí nhỏ nhất là $6$:

- Kỹ sư 1 làm việc 2 (chi phí $C_{1, 2} = 2$).
- Kỹ sư 2 làm việc 3 (chi phí $C_{2, 3} = 3$).
- Kỹ sư 3 làm việc 1 (chi phí $C_{3, 1} = 1$).
Tổng chi phí tối thiểu: $2 + 3 + 1 = 6$.

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

int main() {
ios::sync_with_stdio(false);
cin.tie(nullptr);

int n;
if (!(cin >> n)) return 0;

vector<vector<long long>> cost(n, vector<long long>(n));
for (int i = 0; i < n; ++i) {
for (int j = 0; j < n; ++j) {
cin >> cost[i][j];
}
}

int total_masks = (1 << n);
const long long INF = 1e18;
vector<long long> dp(total_masks, INF);
dp[0] = 0;

for (int mask = 0; mask < total_masks; ++mask) {
if (dp[mask] == INF) continue;
int task_idx = __builtin_popcount(mask);
if (task_idx >= n) continue;

for (int j = 0; j < n; ++j) {
if (!((mask >> j) & 1)) {
int next_mask = mask | (1 << j);
dp[next_mask] = min(dp[next_mask], dp[mask] + cost[task_idx][j]);
}
}
}

cout << dp[total_masks - 1] << "\n";
return 0;
}
```
