# Hướng Dẫn Giảng Dạy: Đổi Tiền Giới Hạn Số Lượng (Bounded Knapsack)

Chuyên đề: **Quy Hoạch Động 2 Chiều & Bài Toán Cái Túi (DP 2D / Knapsack)**

---

## 1. Ý tưởng & Phân tích thuật toán

- **Bản chất bài toán:** Cho danh sách $N$ mệnh giá kèm số lượng tờ tiền tương ứng và số tiền cần rút $S$. Hãy lập trình tìm số lượng tờ tiền ít nhất để chi trả đúng số tiền $S$. Nếu khay tiền không thể đáp ứng, in ra `-1`.

- **Phương pháp tiếp cận & Chiến lược tối ưu:**
- **Mô hình trạng thái:** Định nghĩa $dp[i][j]$ biểu diễn kết quả tối ưu khi xét tiền tố $i$ đồ vật và sức chứa/trọng lượng còn lại là $j$, hoặc toạ độ ô $(i, j)$ trên lưới.
- **Chuyển trạng thái bài toán Cái Túi (0/1 Knapsack):**
  $$dp[i][w] = \max(dp[i-1][w],\, dp[i-1][w - w_i] + v_i) \quad (w \ge w_i)$$
- **Kỹ thuật tối ưu bộ nhớ (Nén mảng 1D):** Với bài toán 0/1 Knapsack, duyệt lùi $w$ từ $W$ về $w_i$ để đảm bảo mỗi vật chỉ được chọn tối đa một lần; với Unbounded Knapsack, duyệt xuôi từ $w_i$ đến $W$.
- **Độ phức tạp:** Thời gian $\mathcal{O}(N \times W)$ hoặc $\mathcal{O}(N \times M)$, không gian tối ưu $\mathcal{O}(W)$.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table)
Mẫu thử (Sample 1): Đầu vào: `3 11 1 2 5 2 6 1` $\implies$ Đầu ra kỳ vọng: `2`.

| Bước | Thao tác thực hiện | Dữ liệu biến đổi & Trạng thái | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Khởi tạo & Đọc dữ liệu | Nạp Input: `3 11 1 2 5 2 6 1` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Chạy thuật toán từng bước | Phân tích mẫu: Với số tiền cần rút $S = 10$ và các mệnh giá: 5 đồng (có 1 tờ), 2 đồng (có 3 tờ): Chọn 1 tờ 5 đồng và 2 tờ 2 đồng ($5 + 2  × 2 = 9 < 10... | Cập nhật các biến / mảng trạng thái |
| 3 | Xuất kết quả chuẩn | Đối chiếu trạng thái cuối cùng | Output chuẩn: `2` |

*Giải thích chi tiết:* Với số tiền cần rút $S = 10$ và các mệnh giá: 5 đồng (có 1 tờ), 2 đồng (có 3 tờ):
Chọn 1 tờ 5 đồng và 2 tờ 2 đồng ($5 + 2  × 2 = 9 < 10$).
Phương án đổi đúng là dùng 5 tờ 2 đồng (nhưng chỉ có 3 tờ nên không được).
Nếu có thêm mệnh giá 1 đồng (2 tờ): Dùng 1 tờ 5, 2 tờ 2 và 1 tờ 1, tổng cộng 4 tờ tiền.

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

const int INF = 1e9;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, s;
    if (!(cin >> n >> s)) return 0;
    if (n <= 0 || s < 0) return 0;

    vector<int> dp(s + 1, INF);
    dp[0] = 0;

    for (int i = 0; i < n; ++i) {
        int v, c;
        cin >> v >> c;
        // Phân rã nhị phân số lượng c thành 1, 2, 4, ...
        int k = 1;
        while (c > 0) {
            int take = min(k, c);
            int weight = take * v;
            int coins = take;

            for (int j = s; j >= weight; --j) {
                if (dp[j - weight] != INF) {
                    dp[j] = min(dp[j], dp[j - weight] + coins);
                }
            }

            c -= take;
            k *= 2;
        }
    }

    if (dp[s] == INF) cout << -1 << "\n";
    else cout << dp[s] << "\n";
    return 0;
}
```
