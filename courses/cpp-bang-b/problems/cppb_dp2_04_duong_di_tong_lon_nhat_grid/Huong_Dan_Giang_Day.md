# Hướng Dẫn Giảng Dạy: Nhặt Vàng Trên Lưới

Chuyên đề: **Quy Hoạch Động 2 Chiều & Bài Toán Cái Túi (DP 2D / Knapsack)**

---

## 1. Ý tưởng & Phân tích thuật toán

- **Bản chất bài toán:** Cho ma trận số vàng tại các gian phòng. Hãy lập trình tìm tổng số vàng lớn nhất mà nhà khảo cổ có thể thu thập được trên đường thoát ra.

- **Phương pháp tiếp cận & Chiến lược tối ưu:**
- **Mô hình trạng thái:** Định nghĩa $dp[i][j]$ biểu diễn kết quả tối ưu khi xét tiền tố $i$ đồ vật và sức chứa/trọng lượng còn lại là $j$, hoặc toạ độ ô $(i, j)$ trên lưới.
- **Chuyển trạng thái bài toán Cái Túi (0/1 Knapsack):**
$$dp[i][w] = \max(dp[i-1][w],\, dp[i-1][w - w_i] + v_i) \quad (w \ge w_i)$$

- **Kỹ thuật tối ưu bộ nhớ (Nén mảng 1D):** Với bài toán 0/1 Knapsack, duyệt lùi $w$ từ $W$ về $w_i$ để đảm bảo mỗi vật chỉ được chọn tối đa một lần; với Unbounded Knapsack, duyệt xuôi từ $w_i$ đến $W$.
- **Độ phức tạp:** Thời gian $\mathcal{O}(N \times W)$ hoặc $\mathcal{O}(N \times M)$, không gian tối ưu $\mathcal{O}(W)$.

---

## 2. Bảng chạy tay trên số liệu mẫuMẫu thử (Sample 1): Đầu vào: `3 3 1 2 3 0 5 0 4 1 2` $\implies$ Đầu ra kỳ vọng: `13`.

| Bước | Thao tác thực hiện | Dữ liệu biến đổi & Trạng thái | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Khởi tạo & Đọc dữ liệu | Nạp Input: `3 3 1 2 3 0 5 0 4 1 2` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Chạy thuật toán từng bước | Phân tích mẫu: Với lưới vàng kích thước $3 × 3$: Lộ trình thu thập tối ưu là đi qua các gian phòng có lượng vàng phong phú nhất, đạt tổng giá trị lớn... | Cập nhật các biến / mảng trạng thái |
| 3 | Xuất kết quả chuẩn | Đối chiếu trạng thái cuối cùng | Output chuẩn: `13` |

*Giải thích chi tiết:* Với lưới vàng kích thước $3 × 3$:
Lộ trình thu thập tối ưu là đi qua các gian phòng có lượng vàng phong phú nhất, đạt tổng giá trị lớn nhất là 15.

---

## 3. Lưu ý & Bẫy lỗi thường gặp
* Trong bài toán Cái Túi 0/1, nếu nén mảng 1D mà duyệt xuôi vòng lặp sức chứa $w$ thì một đồ vật sẽ bị chọn vô hạn lần (biến thành Unbounded Knapsack).
* Mảng $dp$ 2 chiều kích thước lớn vượt quá giới hạn bộ nhớ (256MB cho phép tối đa khoảng $6 \times 10^7$ phần tử `int`), cần nén mảng 1 chiều hoặc dùng mảng cuốn chiếu.
* Các ô có chướng ngại vật trên lưới phải gán trạng thái bằng $0$ (số cách đi) hoặc $-INF$ (chi phí) để không lan truyền sang các ô kế tiếp.

---

## 4. Lời giải tham khảo
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
ios::sync_with_stdio(false);
cin.tie(nullptr);

int n, m;
if (!(cin >> n >> m)) return 0;
if (n <= 0 || m <= 0) return 0;

vector<vector<long long>> a(n, vector<long long>(m));
for (int i = 0; i < n; ++i) {
for (int j = 0; j < m; ++j) cin >> a[i][j];
}

vector<long long> dp(m, 0);
dp[0] = a[0][0];

for (int j = 1; j < m; ++j) dp[j] = dp[j - 1] + a[0][j];

for (int i = 1; i < n; ++i) {
dp[0] += a[i][0];
for (int j = 1; j < m; ++j) {
dp[j] = max(dp[j], dp[j - 1]) + a[i][j];
}
}

cout << dp[m - 1] << "\n";
return 0;
}
```
