# Hướng Dẫn Giảng Dạy: Chia Tập Chênh Lệch Nhỏ Nhất (Minimum Subset Sum Difference)

Chuyên đề: **Quy Hoạch Động 2 Chiều & Bài Toán Cái Túi (DP 2D / Knapsack)**

---

## 1. Ý tưởng & Phân tích thuật toán

- **Bản chất bài toán:** Cho danh sách điểm kỹ năng của $N$ tuyển thủ. Hãy lập trình tìm độ chênh lệch nhỏ nhất giữa tổng điểm của hai đội.

- **Phương pháp tiếp cận & Chiến lược tối ưu:**
- **Mô hình trạng thái:** Định nghĩa $dp[i][j]$ biểu diễn kết quả tối ưu khi xét tiền tố $i$ đồ vật và sức chứa/trọng lượng còn lại là $j$, hoặc toạ độ ô $(i, j)$ trên lưới.
- **Chuyển trạng thái bài toán Cái Túi (0/1 Knapsack):**
$$dp[i][w] = \max(dp[i-1][w],\, dp[i-1][w - w_i] + v_i) \quad (w \ge w_i)$$

- **Kỹ thuật tối ưu bộ nhớ (Nén mảng 1D):** Với bài toán 0/1 Knapsack, duyệt lùi $w$ từ $W$ về $w_i$ để đảm bảo mỗi vật chỉ được chọn tối đa một lần; với Unbounded Knapsack, duyệt xuôi từ $w_i$ đến $W$.
- **Độ phức tạp:** Thời gian $\mathcal{O}(N \times W)$ hoặc $\mathcal{O}(N \times M)$, không gian tối ưu $\mathcal{O}(W)$.

---

## 2. Bảng chạy tay trên số liệu mẫuMẫu thử (Sample 1): Đầu vào: `4 1 6 11 5` $\implies$ Đầu ra kỳ vọng: `1`.

| Bước | Thao tác thực hiện | Dữ liệu biến đổi & Trạng thái | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Khởi tạo & Đọc dữ liệu | Nạp Input: `4 1 6 11 5` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Chạy thuật toán từng bước | Phân tích mẫu: Với tập hợp kỹ năng $[1, 6, 11, 5]$: Tổng toàn bộ kỹ năng là $1 + 6 + 11 + 5 = 23$. Ta chia thành hai đội với các tuyển thủ $\{1, 11\}$... | Cập nhật các biến / mảng trạng thái |
| 3 | Xuất kết quả chuẩn | Đối chiếu trạng thái cuối cùng | Output chuẩn: `1` |

*Giải thích chi tiết:* Với tập hợp kỹ năng $[1, 6, 11, 5]$:
Tổng toàn bộ kỹ năng là $1 + 6 + 11 + 5 = 23$. Ta chia thành hai đội với các tuyển thủ $\{1, 11\}$ (tổng kỹ năng 12) và $\{6, 5\}$ (tổng kỹ năng 11). Độ chênh lệch giữa hai đội là $|12 - 11| = 1$. Đây là mức chênh lệch nhỏ nhất.

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

int n;
if (!(cin >> n)) return 0;
if (n <= 0) return 0;

vector<int> a(n);
int total_sum = 0;
for (int i = 0; i < n; ++i) {
cin >> a[i];
total_sum += a[i];
}

int half = total_sum / 2;
vector<bool> dp(half + 1, false);
dp[0] = true;

for (int x : a) {
for (int j = half; j >= x; --j) {
if (dp[j - x]) dp[j] = true;
}
}

int best_s1 = 0;
for (int j = half; j >= 0; --j) {
if (dp[j]) {
best_s1 = j;
break;
}
}

int min_diff = total_sum - 2 * best_s1;
cout << min_diff << "\n";
return 0;
}
```
