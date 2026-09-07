# Hướng Dẫn Giảng Dạy: Bài Toán Tháp Hà Nội (Tower of Hanoi)
Chuyên đề: **Bài 10: Thuật toán đệ quy & cây gọi hàm**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho N đĩa đặt trên cọc A. Hãy in ra số bước chuyển tối thiểu và danh sách các bước di chuyển đĩa từ cọc này sang cọc khác để chuyển hết N đĩa từ cọc A sang cọc C (dùng cọc B làm trung gian).

- **Phương pháp tiếp cận — Thuật toán đệ quy & Cây gọi hàm:**
  - Xác định trường hợp cơ sở (Base Case) để chặn đệ quy vô hạn.
  - Thiết lập công thức truy hồi và theo dõi luồng thực thi trên cây gọi hàm.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 2)
| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `2` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | Với N = 2 cần 2^2 - 1 = 3 bước: chuyển đĩa 1 từ A sang B; chuyển đĩa 2 từ A sang C; chuyển đĩa 1 từ B sang C.... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `3 A -> B A -> C B -> C` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* Với N = 2 cần 2^2 - 1 = 3 bước: chuyển đĩa 1 từ A sang B; chuyển đĩa 2 từ A sang C; chuyển đĩa 1 từ B sang C.

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

void solveHanoi(int n, char from, char to, char aux) {
    if (n == 0) return;
    solveHanoi(n - 1, from, aux, to);
    cout << from << " -> " << to << "\n";
    solveHanoi(n - 1, aux, to, from);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    cout << (1 << n) - 1 << "\n";
    solveHanoi(n, 'A', 'C', 'B');
    return 0;
}
```
