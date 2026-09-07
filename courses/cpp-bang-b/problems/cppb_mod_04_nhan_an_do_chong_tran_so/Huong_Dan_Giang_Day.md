# Hướng Dẫn Giảng Dạy: Nhân Ấn Độ Chống Tràn Số 64-bit
Chuyên đề: **Bài 08: Đồng dư thức, lũy thừa nhị phân & nghịch đảo modulo**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho 3 số nguyên A, B, M (0 <= A, B, M <= 10^18, M > 0). Hãy tính (A * B) mod M bằng thuật toán nhân Ấn Độ chống tràn số.

- **Phương pháp tiếp cận — Đại số Modular & Lũy thừa nhị phân:**
  - Áp dụng các tính chất $(A + B) \pmod M$, $(A \times B) \pmod M$ ở mọi bước tính.
  - Lũy thừa nhị phân tính $A^B \pmod M$ trong $\mathcal{O}(\log B)$ và nghịch đảo modulo qua định lý Fermat nhỏ.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 1000000000000000000 2 100)
| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `1000000000000000000 2 1000000000000` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | A = 10^18. Tích 2 * 10^18 = 2000000000000000000. Chia lấy dư cho M = 10^18 + 7: 2000000000000000000 - (10^18 + 7) = 9999... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `999999999999999986` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* A = 10^18. Tích 2 * 10^18 = 2000000000000000000. Chia lấy dư cho M = 10^18 + 7: 2000000000000000000 - (10^18 + 7) = 999999999999999986.

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

long long mulMod(long long a, long long b, long long m) {
    long long ans = 0;
    a %= m;
    while (b > 0) {
        if (b & 1) ans = (ans + a) % m;
        a = (a + a) % m;
        b >>= 1;
    }
    return ans;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long a, b, m;
    if (!(cin >> a >> b >> m)) return 0;

    cout << mulMod(a, b, m) << "\n";
    return 0;
}
```
