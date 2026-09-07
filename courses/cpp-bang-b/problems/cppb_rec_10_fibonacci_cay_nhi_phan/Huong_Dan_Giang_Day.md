# Hướng Dẫn Giảng Dạy: Dãy Fibonacci Đệ Quy & Khảo Sát Cây Gọi Hàm
Chuyên đề: **Bài 10: Thuật toán đệ quy & cây gọi hàm**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho số nguyên N (0 <= N <= 30). Hãy tính giá trị F_N và đếm tổng số lần gọi hàm fibonacci() trong toàn bộ quá trình thực thi.

- **Phương pháp tiếp cận — Thuật toán đệ quy & Cây gọi hàm:**
  - Xác định trường hợp cơ sở (Base Case) để chặn đệ quy vô hạn.
  - Thiết lập công thức truy hồi và theo dõi luồng thực thi trên cây gọi hàm.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 4)
| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `4` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | F(4) = 3. Cây gọi hàm fib(4) gồm 9 lần gọi hàm: fib(4) gọi fib(3) và fib(2); fib(3) gọi fib(2) và fib(1); v.v. Tổng số l... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `3 9` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* F(4) = 3. Cây gọi hàm fib(4) gồm 9 lần gọi hàm: fib(4) gọi fib(3) và fib(2); fib(3) gọi fib(2) và fib(1); v.v. Tổng số lần gọi là 9.

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

long long call_count = 0;

long long fibRec(int n) {
    call_count++;
    if (n <= 0) return 0;
    if (n == 1) return 1;
    return fibRec(n - 1) + fibRec(n - 2);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    long long val = fibRec(n);
    cout << val << " " << call_count << "\n";
    return 0;
}
```
