# Hướng Dẫn Giảng Dạy: Số Fibonacci Lớn Thứ N
Chuyên đề: **Bài 09: Xử lý số nguyên lớn (BigInt)**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho số nguyên N (0 <= N <= 1000). Hãy in ra giá trị chính xác của F(N) (với F(0) = 0, F(1) = 1, F(N) = F(N-1) + F(N-2)).

- **Phương pháp tiếp cận — Xử lý số nguyên lớn (BigInt):**
- Biểu diễn số lớn bằng chuỗi ký tự `string` hoặc mảng các chữ số `vector<int>` đảo ngược.
- Mô phỏng các phép tính cộng, trừ, nhân, chia bằng thuật toán đặt tính từng cột như tiểu học.

---

## 2. Bảng chạy tay trên số liệu mẫu| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `10` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | Dãy Fibonacci: F(0)=0, F(1)=1, ..., F(10)=55. Kết quả in ra: 55.... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `55` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* Dãy Fibonacci: F(0)=0, F(1)=1, ..., F(10)=55. Kết quả in ra: 55.

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

int n;
if (!(cin >> n)) return 0;

if (n == 0) { cout << "0\n"; return 0; }
if (n == 1) { cout << "1\n"; return 0; }

string f0 = "0", f1 = "1", f2 = "";
for (int i = 2; i <= n; ++i) {
f2 = addBig(f0, f1);
f0 = f1;
f1 = f2;
}

cout << f1 << "\n";
return 0;
}
```
