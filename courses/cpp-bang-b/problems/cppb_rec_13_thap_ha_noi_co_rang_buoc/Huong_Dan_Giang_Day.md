# Hướng Dẫn Giảng Dạy: Tháp Hà Nội Có Ràng Buộc Nước Đi
Chuyên đề: **Bài 10: Thuật toán đệ quy & cây gọi hàm**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho N đĩa trên cọc A với quy tắc chuyển qua cọc trung gian B. Hãy tính số bước di chuyển tối thiểu và in ra danh sách các bước đi để chuyển hết N đĩa từ A sang C.

- **Phương pháp tiếp cận — Thuật toán đệ quy & Cây gọi hàm:**
  - Xác định trường hợp cơ sở (Base Case) để chặn đệ quy vô hạn.
  - Thiết lập công thức truy hồi và theo dõi luồng thực thi trên cây gọi hàm.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 1)
| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `1` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | Với 1 đĩa không được đi trực tiếp A -> C nên phải đi qua B: A -> B rồi B -> C. Tổng cộng 2 bước.... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `2 A -> B B -> C` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* Với 1 đĩa không được đi trực tiếp A -> C nên phải đi qua B: A -> B rồi B -> C. Tổng cộng 2 bước.

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

void moveAtoB(int n, char a, char b, char c);
void moveBtoC(int n, char b, char c, char a);

void solveConstrainedHanoi(int n, char from, char to, char aux) {
    if (n == 0) return;
    // Chuyển n-1 đĩa from -> to
    solveConstrainedHanoi(n - 1, from, to, aux);
    // Chuyển đĩa n: from -> aux
    cout << from << " -> " << aux << "\n";
    // Chuyển n-1 đĩa to -> from
    solveConstrainedHanoi(n - 1, to, from, aux);
    // Chuyển đĩa n: aux -> to
    cout << aux << " -> " << to << "\n";
    // Chuyển n-1 đĩa from -> to
    solveConstrainedHanoi(n - 1, from, to, aux);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    long long total_steps = 1;
    for (int i = 0; i < n; ++i) total_steps *= 3;
    total_steps -= 1;
    cout << total_steps << "\n";
    solveConstrainedHanoi(n, 'A', 'C', 'B');
    return 0;
}
```
