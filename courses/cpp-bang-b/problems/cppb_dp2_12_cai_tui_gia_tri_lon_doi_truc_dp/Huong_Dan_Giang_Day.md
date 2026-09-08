# Hướng Dẫn Giảng Dạy: Cái Túi Khối Lượng Cực Đại W <= 10^9 (Đổi Trục DP)

Chuyên đề: **Quy Hoạch Động 2 Chiều & Bài Toán Cái Túi (DP 2D / Knapsack)**

---

## 1. Ý tưởng & Phân tích thuật toán

- **Bản chất bài toán:** Cho $N$ mẫu vật ($w_i, v_i$) và tải trọng $W \le 10^9$. Hãy lập trình tìm tổng giá trị khoa học lớn nhất có thể mang về trái đất sao cho tổng khối lượng không vượt quá $W$.

- **Phương pháp tiếp cận & Chiến lược tối ưu:**
- **Mô hình trạng thái:** Định nghĩa $dp[i][j]$ biểu diễn kết quả tối ưu khi xét tiền tố $i$ đồ vật và sức chứa/trọng lượng còn lại là $j$, hoặc toạ độ ô $(i, j)$ trên lưới.
- **Chuyển trạng thái bài toán Cái Túi (0/1 Knapsack):**
  $$dp[i][w] = \max(dp[i-1][w],\, dp[i-1][w - w_i] + v_i) \quad (w \ge w_i)$$

- **Kỹ thuật tối ưu bộ nhớ (Nén mảng 1D):** Với bài toán 0/1 Knapsack, duyệt lùi $w$ từ $W$ về $w_i$ để đảm bảo mỗi vật chỉ được chọn tối đa một lần; với Unbounded Knapsack, duyệt xuôi từ $w_i$ đến $W$.
- **Độ phức tạp:** Thời gian $\mathcal{O}(N \times W)$ hoặc $\mathcal{O}(N \times M)$, không gian tối ưu $\mathcal{O}(W)$.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table)
Mẫu thử (Sample 1): Đầu vào: `3 8 3 30 4 50 5 60` $\implies$ Đầu ra kỳ vọng: `90`.

| Bước | Thao tác thực hiện | Dữ liệu biến đổi & Trạng thái | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Khởi tạo & Đọc dữ liệu | Nạp Input: `3 8 3 30 4 50 5 60` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Chạy thuật toán từng bước | Phân tích mẫu: Với $N = 3, W = 10$ và các mẫu vật $[(3, 30), (4, 50), (5, 60)]$: Chọn mẫu vật 1 và mẫu vật 3 với tổng khối lượng $3 + 5 = 8 \le 10$, đ... | Cập nhật các biến / mảng trạng thái |
| 3 | Xuất kết quả chuẩn | Đối chiếu trạng thái cuối cùng | Output chuẩn: `90` |

*Giải thích chi tiết:* Với $N = 3, W = 10$ và các mẫu vật $[(3, 30), (4, 50), (5, 60)]$:
Chọn mẫu vật 1 và mẫu vật 3 với tổng khối lượng $3 + 5 = 8 \le 10$, đạt tổng giá trị là $30 + 60 = 90$.

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

const long long INF = 1e18;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long w;
    if (!(cin >> n >> w)) return 0;
    if (n <= 0 || w <= 0) return 0;

    vector<long long> weight(n), val(n);
    int max_v = 0;
    for (int i = 0; i < n; ++i) {
        cin >> weight[i] >> val[i];
        max_v += val[i];
    }

    // Đổi trục: dp[v] = khối lượng nhỏ nhất để đạt được tổng giá trị v
    vector<long long> dp(max_v + 1, INF);
    dp[0] = 0;

    for (int i = 0; i < n; ++i) {
        for (int v = max_v; v >= val[i]; --v) {
            if (dp[v - val[i]] != INF) {
                dp[v] = min(dp[v], dp[v - val[i]] + weight[i]);
            }
        }
    }

    long long ans = 0;
    for (int v = max_v; v >= 0; --v) {
        if (dp[v] <= w) {
            ans = v;
            break;
        }
    }

    cout << ans << "\n";
    return 0;
}
```
