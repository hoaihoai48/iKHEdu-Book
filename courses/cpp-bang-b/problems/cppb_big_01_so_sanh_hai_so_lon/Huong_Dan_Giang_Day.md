# Hướng Dẫn Giảng Dạy: So Sánh Hai Số Nguyên Lớn
Chuyên đề: **Bài 09: Xử lý số nguyên lớn (BigInt)**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho 2 số nguyên dương lớn A và B. Hãy so sánh A và B, in ra '>' nếu A > B, '<' nếu A < B, '=' nếu A = B.

- **Phương pháp tiếp cận — Xử lý số nguyên lớn (BigInt):**
  - Biểu diễn số lớn bằng chuỗi ký tự `string` hoặc mảng các chữ số `vector<int>` đảo ngược.
  - Mô phỏng các phép tính cộng, trừ, nhân, chia bằng thuật toán đặt tính từng cột như tiểu học.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 123456789 98765432)
| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `123456789 98765432` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | Số A có 9 chữ số trong khi số B chỉ có 8 chữ số. Do đó A > B. Kết quả in ra: `>`.... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `>` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* Số A có 9 chữ số trong khi số B chỉ có 8 chữ số. Do đó A > B. Kết quả in ra: `>`.

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

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string a, b;
    if (!(cin >> a >> b)) return 0;

    if (a.size() > b.size()) cout << ">\n";
    else if (a.size() < b.size()) cout << "<\n";
    else {
        if (a > b) cout << ">\n";
        else if (a < b) cout << "<\n";
        else cout << "=\n";
    }
    return 0;
}
```
