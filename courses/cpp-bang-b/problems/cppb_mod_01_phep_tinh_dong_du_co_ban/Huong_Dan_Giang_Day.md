# Hướng Dẫn Giảng Dạy: Phép Tính Đồng Dư Cơ Bản (+, -, *)
Chuyên đề: **Bài 08: Đồng dư thức, lũy thừa nhị phân & nghịch đảo modulo**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho 2 số nguyên A, B và số nguyên dương M = 10^9 + 7. Hãy tính (A + B) mod M, (A - B) mod M và (A * B) mod M sao cho kết quả luôn thuộc [0, M - 1].

- **Phương pháp tiếp cận — Đại số Modular & Lũy thừa nhị phân:**
  - Áp dụng các tính chất $(A + B) \pmod M$, $(A \times B) \pmod M$ ở mọi bước tính.
  - Lũy thừa nhị phân tính $A^B \pmod M$ trong $\mathcal{O}(\log B)$ và nghịch đảo modulo qua định lý Fermat nhỏ.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 10 15)
| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `10 15` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | Với M = 10^9 + 7: - Tổng: (10 + 15) mod M = 25. - Hiệu: (10 - 15) mod M = -5 mod M = 10^9 + 7 - 5 = 1000000002. - Tích: ... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `25 1000000002 150` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* Với M = 10^9 + 7:

- Tổng: (10 + 15) mod M = 25.
- Hiệu: (10 - 15) mod M = -5 mod M = 10^9 + 7 - 5 = 1000000002.
- Tích: (10 * 15) mod M = 150.

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

const long long MOD = 1000000007;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long a, b;
    if (!(cin >> a >> b)) return 0;

    a %= MOD;
    b %= MOD;

    long long add_res = (a + b) % MOD;
    long long sub_res = (a - b + MOD) % MOD;
    long long mul_res = (a * b) % MOD;

    cout << add_res << " " << sub_res << " " << mul_res << "\n";
    return 0;
}
```
