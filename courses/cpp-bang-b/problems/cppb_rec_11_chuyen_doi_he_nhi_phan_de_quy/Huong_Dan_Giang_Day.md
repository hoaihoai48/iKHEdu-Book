# Hướng Dẫn Giảng Dạy: Chuyển Đổi Hệ Cơ Số 10 Sang Nhị Phân Bằng Đệ Quy
Chuyên đề: **Bài 10: Thuật toán đệ quy & cây gọi hàm**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho số nguyên không âm N. Hãy in ra biểu diễn nhị phân của N bằng hàm đệ quy.

- **Phương pháp tiếp cận — Thuật toán đệ quy & Cây gọi hàm:**
  - Xác định trường hợp cơ sở (Base Case) để chặn đệ quy vô hạn.
  - Thiết lập công thức truy hồi và theo dõi luồng thực thi trên cây gọi hàm.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 10)
| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `10` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | Số 10 trong hệ thập phân chuyển sang nhị phân là 1010_2.... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `1010` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* Số 10 trong hệ thập phân chuyển sang nhị phân là 1010_2.

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

void printBinaryRec(long long n) {
    if (n == 0) return;
    printBinaryRec(n / 2);
    cout << (n % 2);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    long long n;
    if (!(cin >> n)) return 0;
    if (n == 0) {
        cout << 0 << "\n";
    } else {
        printBinaryRec(n);
        cout << "\n";
    }
    return 0;
}
```
