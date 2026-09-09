# Hướng Dẫn Giảng Dạy: Trừ Hai Số Lớn Tổng Quát (Có Thể Âm)
Chuyên đề: **Bài 09: Xử lý số nguyên lớn (BigInt)**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho 2 số nguyên dương lớn A và B. Hãy tính hiệu A - B (in dấu '-' phía trước nếu kết quả mang giá trị âm).

- **Phương pháp tiếp cận — Xử lý số nguyên lớn (BigInt):**
- Biểu diễn số lớn bằng chuỗi ký tự `string` hoặc mảng các chữ số `vector<int>` đảo ngược.
- Mô phỏng các phép tính cộng, trừ, nhân, chia bằng thuật toán đặt tính từng cột như tiểu học.

---

## 2. Bảng chạy tay trên số liệu mẫu| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `1 1000` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | 1 - 1000 = -999. Kết quả in ra: -999.... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `-999` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* 1 - 1000 = -999. Kết quả in ra: -999.

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

bool isLess(const string &a, const string &b) {
if (a.size() != b.size()) return a.size() < b.size();
return a < b;
}

string subBig(string a, string b) {
reverse(a.begin(), a.end());
reverse(b.begin(), b.end());

string res = "";
int borrow = 0;

for (int i = 0; i < (int)a.size(); ++i) {
int diff = (a[i] - '0') - borrow;
if (i < (int)b.size()) diff -= (b[i] - '0');
if (diff < 0) {
diff += 10;
borrow = 1;
} else {
borrow = 0;
}
res.push_back(diff + '0');
}

while (res.size() > 1 && res.back() == '0') res.pop_back();
reverse(res.begin(), res.end());
return res;
}

int main() {
ios::sync_with_stdio(false);
cin.tie(nullptr);

string a, b;
if (!(cin >> a >> b)) return 0;

if (a == b) {
cout << "0\n";
} else if (isLess(a, b)) {
cout << "-" << subBig(b, a) << "\n";
} else {
cout << subBig(a, b) << "\n";
}
return 0;
}
```
