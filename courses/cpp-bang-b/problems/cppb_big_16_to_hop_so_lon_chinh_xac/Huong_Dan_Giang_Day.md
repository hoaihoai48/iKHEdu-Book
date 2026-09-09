# Hướng Dẫn Giảng Dạy: Số Lớn Cực Hạn: Tổ Hợp C(N, K) Chính Xác
Chuyên đề: **Bài 09: Xử lý số nguyên lớn (BigInt)**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho 2 số nguyên N và K. Hãy tính giá trị chính xác tuyệt đối của C(N, K) = N! / (K! * (N - K)!).

- **Phương pháp tiếp cận — Xử lý số nguyên lớn (BigInt):**
- Biểu diễn số lớn bằng chuỗi ký tự `string` hoặc mảng các chữ số `vector<int>` đảo ngược.
- Mô phỏng các phép tính cộng, trừ, nhân, chia bằng thuật toán đặt tính từng cột như tiểu học.

---

## 2. Bảng chạy tay trên số liệu mẫu| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `5 2` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | C(5, 2) = 10.... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `10` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* C(5, 2) = 10.

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

string addBig(string a, string b) {
reverse(a.begin(), a.end());
reverse(b.begin(), b.end());
string res = "";
int carry = 0;
int n = max(a.size(), b.size());
for (int i = 0; i < n || carry; ++i) {
int sum = carry;
if (i < (int)a.size()) sum += a[i] - '0';
if (i < (int)b.size()) sum += b[i] - '0';
res.push_back((sum % 10) + '0');
carry = sum / 10;
}
reverse(res.begin(), res.end());
return res;
}

int main() {
ios::sync_with_stdio(false);
cin.tie(nullptr);

int n, k;
if (!(cin >> n >> k)) return 0;

vector<vector<string>> c(n + 1, vector<string>(k + 1, "0"));
for (int i = 0; i <= n; ++i) {
c[i][0] = "1";
for (int j = 1; j <= min(i, k); ++j) {
if (j == i) c[i][j] = "1";
else c[i][j] = addBig(c[i - 1][j - 1], c[i - 1][j]);
}
}

cout << c[n][k] << "\n";
return 0;
}
```
