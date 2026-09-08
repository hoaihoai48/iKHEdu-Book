# Hướng Dẫn Giảng Dạy: Truy Vết Món Đồ Cái Túi 0/1

Chuyên đề: **Quy Hoạch Động 2 Chiều & Bài Toán Cái Túi (DP 2D / Knapsack)**

---

## 1. Ý tưởng & Phân tích thuật toán

- **Bản chất bài toán:** Cho $N$ đồ vật (mỗi vật có khối lượng $w_i$, giá trị $v_i$) và sức chứa ba lô $W$. Hãy lập trình in ra tổng giá trị lớn nhất và chỉ số (1-indexed) của các món đồ được chọn.

- **Phương pháp tiếp cận & Chiến lược tối ưu:**
- **Mô hình trạng thái:** Định nghĩa $dp[i][j]$ biểu diễn kết quả tối ưu khi xét tiền tố $i$ đồ vật và sức chứa/trọng lượng còn lại là $j$, hoặc toạ độ ô $(i, j)$ trên lưới.
- **Chuyển trạng thái bài toán Cái Túi (0/1 Knapsack):**
  $$dp[i][w] = \max(dp[i-1][w],\, dp[i-1][w - w_i] + v_i) \quad (w \ge w_i)$$

- **Kỹ thuật tối ưu bộ nhớ (Nén mảng 1D):** Với bài toán 0/1 Knapsack, duyệt lùi $w$ từ $W$ về $w_i$ để đảm bảo mỗi vật chỉ được chọn tối đa một lần; với Unbounded Knapsack, duyệt xuôi từ $w_i$ đến $W$.
- **Độ phức tạp:** Thời gian $\mathcal{O}(N \times W)$ hoặc $\mathcal{O}(N \times M)$, không gian tối ưu $\mathcal{O}(W)$.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table)
Mẫu thử (Sample 1): Đầu vào: `3 4 1 15 3 20 4 30` $\implies$ Đầu ra kỳ vọng: `35 2 1 2`.

| Bước | Thao tác thực hiện | Dữ liệu biến đổi & Trạng thái | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Khởi tạo & Đọc dữ liệu | Nạp Input: `3 4 1 15 3 20 4 30` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Chạy thuật toán từng bước | Phân tích mẫu: Với $N = 3, W = 4$ và các đồ vật $[(2, 3), (1, 2), (3, 4)]$: Chọn món đồ 1 (nặng 2, giá trị 3) và món đồ 2 (nặng 1, giá trị 2). Tổng kh... | Cập nhật các biến / mảng trạng thái |
| 3 | Xuất kết quả chuẩn | Đối chiếu trạng thái cuối cùng | Output chuẩn: `35 2 1 2` |

*Giải thích chi tiết:* Với $N = 3, W = 4$ và các đồ vật $[(2, 3), (1, 2), (3, 4)]$:
Chọn món đồ 1 (nặng 2, giá trị 3) và món đồ 2 (nặng 1, giá trị 2). Tổng khối lượng là $2 + 1 = 3 \le 4$, tổng giá trị là $3 + 2 = 5$. Danh sách món đồ chọn là 1 và 2.

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

    int n, w;
    if (!(cin >> n >> w)) return 0;
    if (n <= 0 || w <= 0) return 0;

    vector<long long> weight(n + 1), val(n + 1);
    for (int i = 1; i <= n; ++i) {
        cin >> weight[i] >> val[i];
    }

    vector<vector<long long>> dp(n + 1, vector<long long>(w + 1, 0));

    for (int i = 1; i <= n; ++i) {
        for (int j = 0; j <= w; ++j) {
            dp[i][j] = dp[i - 1][j];
            if (j >= weight[i]) {
                dp[i][j] = max(dp[i][j], dp[i - 1][j - weight[i]] + val[i]);
            }
        }
    }

    // Truy vết các món đồ được chọn
    vector<int> chosen;
    int curr_w = w;
    for (int i = n; i >= 1; --i) {
        if (curr_w >= weight[i] && dp[i][curr_w] == dp[i - 1][curr_w - weight[i]] + val[i]) {
            chosen.push_back(i);
            curr_w -= weight[i];
        }
    }
    reverse(chosen.begin(), chosen.end());

    cout << dp[n][w] << "\n";
    cout << chosen.size() << "\n";
    for (int i = 0; i < (int)chosen.size(); ++i) {
        cout << chosen[i] << (i + 1 == (int)chosen.size() ? "" : " ");
    }
    cout << "\n";
    return 0;
}
```
