# Hướng Dẫn Giảng Dạy: Tối Ưu Hóa Túi Đồ Hỗn Hợp (Hybrid Knapsack)

Chuyên đề: **Quy Hoạch Động 2 Chiều & Bài Toán Cái Túi (DP 2D / Knapsack)**

---

## 1. Ý tưởng & Phân tích thuật toán

- **Bản chất bài toán:** Cho danh sách $N$ loại hàng với đặc tính số lượng của từng loại và tải trọng khoang bay $W$. Hãy lập trình tìm tổng giá trị cứu trợ lớn nhất có thể vận chuyển.

- **Phương pháp tiếp cận & Chiến lược tối ưu:**
- **Mô hình trạng thái:** Định nghĩa $dp[i][j]$ biểu diễn kết quả tối ưu khi xét tiền tố $i$ đồ vật và sức chứa/trọng lượng còn lại là $j$, hoặc toạ độ ô $(i, j)$ trên lưới.
- **Chuyển trạng thái bài toán Cái Túi (0/1 Knapsack):**
$$dp[i][w] = \max(dp[i-1][w],\, dp[i-1][w - w_i] + v_i) \quad (w \ge w_i)$$

- **Kỹ thuật tối ưu bộ nhớ (Nén mảng 1D):** Với bài toán 0/1 Knapsack, duyệt lùi $w$ từ $W$ về $w_i$ để đảm bảo mỗi vật chỉ được chọn tối đa một lần; với Unbounded Knapsack, duyệt xuôi từ $w_i$ đến $W$.
- **Độ phức tạp:** Thời gian $\mathcal{O}(N \times W)$ hoặc $\mathcal{O}(N \times M)$, không gian tối ưu $\mathcal{O}(W)$.

---

## 2. Bảng chạy tay trên số liệu mẫuMẫu thử (Sample 1): Đầu vào: `3 10 1 4 20 2 3 15 1 5 30` $\implies$ Đầu ra kỳ vọng: `50`.

| Bước | Thao tác thực hiện | Dữ liệu biến đổi & Trạng thái | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Khởi tạo & Đọc dữ liệu | Nạp Input: `3 10 1 4 20 2 3 15 1 5 30` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Chạy thuật toán từng bước | Phân tích mẫu: Với khoang máy bay có tải trọng $W = 15$ và danh mục hàng cứu trợ hỗn hợp: Sự kết hợp tối ưu giữa các mặt hàng giới hạn và hàng không g... | Cập nhật các biến / mảng trạng thái |
| 3 | Xuất kết quả chuẩn | Đối chiếu trạng thái cuối cùng | Output chuẩn: `50` |

*Giải thích chi tiết:* Với khoang máy bay có tải trọng $W = 15$ và danh mục hàng cứu trợ hỗn hợp:
Sự kết hợp tối ưu giữa các mặt hàng giới hạn và hàng không giới hạn đem lại tổng giá trị lớn nhất là 32.

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

vector<long long> dp(w + 1, 0);

for (int i = 0; i < n; ++i) {
int type;
long long weight, val;
cin >> type >> weight >> val;

if (type == 1) { // 0/1 Knapsack: duyệt ngược
for (int j = w; j >= weight; --j) {
dp[j] = max(dp[j], dp[j - weight] + val);
}
} else { // Unbounded Knapsack: duyệt xuôi
for (int j = weight; j <= w; ++j) {
dp[j] = max(dp[j], dp[j - weight] + val);
}
}
}

long long ans = 0;
for (int j = 0; j <= w; ++j) ans = max(ans, dp[j]);
cout << ans << "\n";
return 0;
}
```
