# Hướng Dẫn Giảng Dạy: Kiểm Tra Số Có Phải Lũy Thừa Của 2
Chuyên đề: **Bài 06: Phép toán BIT & biểu diễn trạng thái**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho số nguyên dương N (1 <= N <= 10^18). Kiểm tra N có phải là lũy thừa của 2 không. In YES nếu đúng, ngược lại in NO.

- **Phương pháp tiếp cận — Phép toán BIT & Bitmask:**
  - Biểu diễn tập hợp hoặc trạng thái bật/tắt bằng các bit của số nguyên 64-bit.
  - Sử dụng các toán tử bitwise `&, |, ^, ~, <<, >>` để thao tác đồng thời trong $\mathcal{O}(1)$ chu kỳ máy.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 16)
| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `16` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | 16 = 2^4 là một lũy thừa của 2. Phép toán bit: (16 & 15) = 0. Do đó in YES.... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `YES` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* 16 = 2^4 là một lũy thừa của 2. Phép toán bit: (16 & 15) = 0. Do đó in YES.

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

void solve() {
    unsigned long long n;
    cin >> n;
    if (n > 0 && (n & (n - 1)) == 0) {
        cout << "YES\n";
    } else {
        cout << "NO\n";
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    if (!(cin >> t)) return 0;
    while (t--) {
        solve();
    }
    return 0;
}
```
