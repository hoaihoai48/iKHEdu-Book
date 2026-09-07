# Hướng Dẫn Giảng Dạy: Xâu Con Chung Của Ba Chuỗi (LCS 3 Strings)

Chuyên đề: **Quy Hoạch Động Trên Chuỗi (String DP: LCS & Edit Distance)**

---

## 1. Ý tưởng & Phân tích thuật toán

- **Bản chất bài toán:** Cho ba chuỗi ký tự $S_1, S_2$ và $S_3$. Hãy lập trình tính độ dài chuỗi con chung dài nhất của cả ba chuỗi.

- **Phương pháp tiếp cận & Chiến lược tối ưu:**
- **Mô hình trạng thái xâu:** Gọi $dp[i][j]$ là đáp số tối ưu khi so khớp tiền tố độ dài $i$ của xâu $S$ và tiền tố độ dài $j$ của xâu $T$.
- **Công thức chuyển trạng thái tiêu biểu:**
  * *Xâu con chung dài nhất (LCS):* Nếu $S[i-1] == T[j-1]$ thì $dp[i][j] = dp[i-1][j-1] + 1$; ngược lại $dp[i][j] = \max(dp[i-1][j], dp[i][j-1])$.
  * *Khoảng cách chỉnh sửa (Edit Distance):* Lấy giá trị nhỏ nhất giữa 3 thao tác: Chèn ($dp[i][j-1] + 1$), Xoá ($dp[i-1][j] + 1$), Thay thế ($dp[i-1][j-1] + (S[i-1] \neq T[j-1])$).
- **Độ phức tạp:** Thời gian $\mathcal{O}(|S| \times |T|)$, bộ nhớ $\mathcal{O}(|S| \times |T|)$ hoặc $\mathcal{O}(\min(|S|, |T|))$ khi nén 2 hàng.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table)
Mẫu thử (Sample 1): Đầu vào: `geeks geek geekfor` $\implies$ Đầu ra kỳ vọng: `4`.

| Bước | Thao tác thực hiện | Dữ liệu biến đổi & Trạng thái | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Khởi tạo & Đọc dữ liệu | Nạp Input: `geeks geek geekfor` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Chạy thuật toán từng bước | Phân tích mẫu: Với 3 chuỗi ký tự: $S_1 = \text{"geeks"}$, $S_2 = \text{"geeksfor"}$, $S_3 = \text{"geeksforgeeks"}$: Chuỗi con chung dài nhất xuất hiệ... | Cập nhật các biến / mảng trạng thái |
| 3 | Xuất kết quả chuẩn | Đối chiếu trạng thái cuối cùng | Output chuẩn: `4` |

*Giải thích chi tiết:* Với 3 chuỗi ký tự:
$S_1 = \text{"geeks"}$, $S_2 = \text{"geeksfor"}$, $S_3 = \text{"geeksforgeeks"}$:
Chuỗi con chung dài nhất xuất hiện trong cả 3 chuỗi là $\text{"geeks"}$ với độ dài bằng 5.

---

## 3. Lưu ý & Bẫy lỗi thường gặp
* Quên khởi tạo hàng 0 và cột 0 của bảng $dp$: Trong Edit Distance, $dp[i][0] = i$ (xoá $i$ ký tự) và $dp[0][j] = j$ (chèn $j$ ký tự).
* Nhầm lẫn giữa chỉ số xâu 0-based trong C++ (`S[i-1]`) và kích thước tiền tố 1-based trong bảng $dp$ ($dp[i][j]$).
* Truy vết ngược không xử lý đúng thứ tự ký tự: Cần lưu các ký tự vào chuỗi rồi đảo ngược `reverse()` trước khi in ra kết quả.

---

## 4. Lời giải tham khảo
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s1, s2, s3;
    if (!(cin >> s1 >> s2 >> s3)) return 0;

    int n1 = s1.size(), n2 = s2.size(), n3 = s3.size();
    vector<vector<vector<int>>> dp(n1 + 1, vector<vector<int>>(n2 + 1, vector<int>(n3 + 1, 0)));

    for (int i = 1; i <= n1; ++i) {
        for (int j = 1; j <= n2; ++j) {
            for (int k = 1; k <= n3; ++k) {
                if (s1[i - 1] == s2[j - 1] && s2[j - 1] == s3[k - 1]) {
                    dp[i][j][k] = dp[i - 1][j - 1][k - 1] + 1;
                } else {
                    dp[i][j][k] = max({dp[i - 1][j][k], dp[i][j - 1][k], dp[i][j][k - 1]});
                }
            }
        }
    }

    cout << dp[n1][n2][n3] << "\n";
    return 0;
}
```
