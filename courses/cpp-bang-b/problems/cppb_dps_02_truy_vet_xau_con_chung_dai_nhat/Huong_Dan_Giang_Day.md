# Hướng Dẫn Giảng Dạy: Truy Vết Xâu Con Chung Dài Nhất

Chuyên đề: **Quy Hoạch Động Trên Chuỗi (String DP: LCS & Edit Distance)**

---

## 1. Ý tưởng & Phân tích thuật toán

- **Bản chất bài toán:** Cho hai chuỗi ký tự $S$ và $T$. Hãy lập trình tìm và in ra xâu con chung dài nhất của hai chuỗi. Nếu có nhiều xâu con chung cùng đạt độ dài lớn nhất, in ra một xâu bất kỳ thỏa mãn.

- **Phương pháp tiếp cận & Chiến lược tối ưu:**
- **Mô hình trạng thái xâu:** Gọi $dp[i][j]$ là đáp số tối ưu khi so khớp tiền tố độ dài $i$ của xâu $S$ và tiền tố độ dài $j$ của xâu $T$.
- **Công thức chuyển trạng thái tiêu biểu:**
* *Xâu con chung dài nhất (LCS):* Nếu $S[i-1] == T[j-1]$ thì $dp[i][j] = dp[i-1][j-1] + 1$; ngược lại $dp[i][j] = \max(dp[i-1][j], dp[i][j-1])$.
* *Khoảng cách chỉnh sửa (Edit Distance):* Lấy giá trị nhỏ nhất giữa 3 thao tác: Chèn ($dp[i][j-1] + 1$), Xoá ($dp[i-1][j] + 1$), Thay thế ($dp[i-1][j-1] + (S[i-1] \neq T[j-1])$).
- **Độ phức tạp:** Thời gian $\mathcal{O}(|S| \times |T|)$, bộ nhớ $\mathcal{O}(|S| \times |T|)$ hoặc $\mathcal{O}(\min(|S|, |T|))$ khi nén 2 hàng.

---

## 2. Bảng chạy tay trên số liệu mẫuMẫu thử (Sample 1): Đầu vào: `ABCBDAB BDCAB` $\implies$ Đầu ra kỳ vọng: `4 BDAB`.

| Bước | Thao tác thực hiện | Dữ liệu biến đổi & Trạng thái | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Khởi tạo & Đọc dữ liệu | Nạp Input: `ABCBDAB BDCAB` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Chạy thuật toán từng bước | Phân tích mẫu: Với hai xâu $S = \text{"ABCBDAB"}$ và $T = \text{"BDCAB"}$: Xâu con chung dài nhất đồng thời xuất hiện trong cả hai xâu là $\text{"BCAB... | Cập nhật các biến / mảng trạng thái |
| 3 | Xuất kết quả chuẩn | Đối chiếu trạng thái cuối cùng | Output chuẩn: `4 BDAB` |

*Giải thích chi tiết:* Với hai xâu $S = \text{"ABCBDAB"}$ và $T = \text{"BDCAB"}$:
Xâu con chung dài nhất đồng thời xuất hiện trong cả hai xâu là $\text{"BCAB"}$ với độ dài là 4. Kết quả in ra chuỗi BCAB.

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
vector<vector<int>> dp(n + 1, vector<int>(m + 1, 0));

for (int i = 1; i <= n; ++i) {
for (int j = 1; j <= m; ++j) {
if (s[i - 1] == t[j - 1]) {
dp[i][j] = dp[i - 1][j - 1] + 1;
} else {
dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
}
}
}

// Truy vết
string lcs = "";
int i = n, j = m;
while (i > 0 && j > 0) {
if (s[i - 1] == t[j - 1]) {
lcs += s[i - 1];
--i; --j;
} else if (dp[i - 1][j] >= dp[i][j - 1]) {
--i;
} else {
--j;
}
}
reverse(lcs.begin(), lcs.end());

cout << dp[n][m] << "\n";
cout << lcs << "\n";
return 0;
}
```
