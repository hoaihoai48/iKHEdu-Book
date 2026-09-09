# Hướng Dẫn Giảng Dạy: Kiểm Tra Chuỗi Palindrome Bằng Đệ Quy
Chuyên đề: **Bài 10: Thuật toán đệ quy & cây gọi hàm**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho xâu ký tự S gồm các chữ cái in thường. Hãy viết hàm đệ quy isPalindrome(S, L, R) kiểm tra xâu S có phải là Palindrome không. In YES nếu đúng, ngược lại in NO.

- **Phương pháp tiếp cận — Thuật toán đệ quy & Cây gọi hàm:**
- Xác định trường hợp cơ sở (Base Case) để chặn đệ quy vô hạn.
- Thiết lập công thức truy hồi và theo dõi luồng thực thi trên cây gọi hàm.

---

## 2. Bảng chạy tay trên số liệu mẫu| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `radar` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | Xâu 'radar' đọc xuôi hay đọc ngược đều là 'radar' nên là xâu Palindrome -> in YES.... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `YES` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* Xâu 'radar' đọc xuôi hay đọc ngược đều là 'radar' nên là xâu Palindrome -> in YES.

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

bool isPalindromeRec(const string &s, int l, int r) {
if (l >= r) return true;
if (s[l] != s[r]) return false;
return isPalindromeRec(s, l + 1, r - 1);
}

int main() {
ios::sync_with_stdio(false);
cin.tie(nullptr);
string s;
if (!(cin >> s)) return 0;
if (isPalindromeRec(s, 0, (int)s.size() - 1)) {
cout << "YES\n";
} else {
cout << "NO\n";
}
return 0;
}
```
