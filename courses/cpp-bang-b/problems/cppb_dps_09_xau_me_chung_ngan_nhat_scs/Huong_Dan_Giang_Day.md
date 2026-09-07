# Hướng Dẫn Giảng Dạy: Xâu Mẹ Chung Ngắn Nhất (Shortest Common Supersequence)

Chuyên đề: **Quy Hoạch Động Trên Chuỗi (String DP: LCS & Edit Distance)**

---

## 1. Ý tưởng & Phân tích thuật toán

- **Bản chất bài toán:** Cho hai chuỗi ký tự $S$ và $T$. Hãy lập trình tìm độ dài ngắn nhất của một chuỗi chứa cả $S$ và $T$ dưới dạng các chuỗi con.

- **Phương pháp tiếp cận & Chiến lược tối ưu:**
- **Mô hình trạng thái xâu:** Gọi $dp[i][j]$ là đáp số tối ưu khi so khớp tiền tố độ dài $i$ của xâu $S$ và tiền tố độ dài $j$ của xâu $T$.
- **Công thức chuyển trạng thái tiêu biểu:**
  * *Xâu con chung dài nhất (LCS):* Nếu $S[i-1] == T[j-1]$ thì $dp[i][j] = dp[i-1][j-1] + 1$; ngược lại $dp[i][j] = \max(dp[i-1][j], dp[i][j-1])$.
  * *Khoảng cách chỉnh sửa (Edit Distance):* Lấy giá trị nhỏ nhất giữa 3 thao tác: Chèn ($dp[i][j-1] + 1$), Xoá ($dp[i-1][j] + 1$), Thay thế ($dp[i-1][j-1] + (S[i-1] \neq T[j-1])$).
- **Độ phức tạp:** Thời gian $\mathcal{O}(|S| \times |T|)$, bộ nhớ $\mathcal{O}(|S| \times |T|)$ hoặc $\mathcal{O}(\min(|S|, |T|))$ khi nén 2 hàng.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table)
Mẫu thử (Sample 1): Đầu vào: `abac cab` $\implies$ Đầu ra kỳ vọng: `5`.

| Bước | Thao tác thực hiện | Dữ liệu biến đổi & Trạng thái | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Khởi tạo & Đọc dữ liệu | Nạp Input: `abac cab` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Chạy thuật toán từng bước | Phân tích mẫu: Với hai chuỗi $S = \text{"abac"}$ và $T = \text{"cab"}$: Xâu mẹ chung ngắn nhất chứa cả hai chuỗi là $\text{"cabac"}$ có độ dài đúng bằ... | Cập nhật các biến / mảng trạng thái |
| 3 | Xuất kết quả chuẩn | Đối chiếu trạng thái cuối cùng | Output chuẩn: `5` |

*Giải thích chi tiết:* Với hai chuỗi $S = \text{"abac"}$ và $T = \text{"cab"}$:
Xâu mẹ chung ngắn nhất chứa cả hai chuỗi là $\text{"cabac"}$ có độ dài đúng bằng 5 (chứa "cab" ở tiền tố và "abac" ở hậu tố).

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

    string s, t;
    if (!(cin >> s >> t)) return 0;

    int n = s.size(), m = t.size();
    vector<int> prev_row(m + 1, 0), curr_row(m + 1, 0);

    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= m; ++j) {
            if (s[i - 1] == t[j - 1]) {
                curr_row[j] = prev_row[j - 1] + 1;
            } else {
                curr_row[j] = max(prev_row[j], curr_row[j - 1]);
            }
        }
        prev_row = curr_row;
    }

    int lcs = prev_row[m];
    int scs_len = n + m - lcs;
    cout << scs_len << "\n";
    return 0;
}
```
