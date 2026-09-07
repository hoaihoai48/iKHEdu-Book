# Hướng Dẫn Giảng Dạy: Thuật Toán Euclid Tính GCD & LCM Bằng Đệ Quy
Chuyên đề: **Bài 10: Thuật toán đệ quy & cây gọi hàm**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho 2 số nguyên dương A, B. Hãy tính ước chung lớn nhất gcd(A, B) và bội chung nhỏ nhất lcm(A, B) bằng hàm đệ quy Euclid.

- **Phương pháp tiếp cận — Thuật toán đệ quy & Cây gọi hàm:**
  - Xác định trường hợp cơ sở (Base Case) để chặn đệ quy vô hạn.
  - Thiết lập công thức truy hồi và theo dõi luồng thực thi trên cây gọi hàm.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 24 36)
| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `24 36` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | gcd(24, 36) = 12 và lcm(24, 36) = (24 * 36) / 12 = 72.... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `12 72` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* gcd(24, 36) = 12 và lcm(24, 36) = (24 * 36) / 12 = 72.

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

long long gcdRec(long long a, long long b) {
    if (b == 0) return a;
    return gcdRec(b, a % b);
}

void print128(__int128 n) {
    if (n == 0) { cout << 0; return; }
    string s = "";
    while (n > 0) {
        s.push_back(char('0' + (n % 10)));
        n /= 10;
    }
    reverse(s.begin(), s.end());
    cout << s;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    long long a, b;
    if (!(cin >> a >> b)) return 0;
    long long g = gcdRec(a, b);
    __int128 lcm = ((__int128)a / g) * b;
    cout << g << " ";
    print128(lcm);
    cout << "\n";
    return 0;
}
```
