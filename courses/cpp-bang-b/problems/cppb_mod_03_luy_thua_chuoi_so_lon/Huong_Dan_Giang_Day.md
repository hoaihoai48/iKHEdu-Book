# Hướng Dẫn Giảng Dạy: Lũy Thừa Chuỗi Số Lớn
Chuyên đề: **Bài 08: Đồng dư thức, lũy thừa nhị phân & nghịch đảo modulo**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho số nguyên A và số nguyên B rất lớn biểu diễn dưới dạng chuỗi ký tự. Hãy tính A^B mod (10^9 + 7).

- **Phương pháp tiếp cận — Đại số Modular & Lũy thừa nhị phân:**
  - Áp dụng các tính chất $(A + B) \pmod M$, $(A \times B) \pmod M$ ở mọi bước tính.
  - Lũy thừa nhị phân tính $A^B \pmod M$ trong $\mathcal{O}(\log B)$ và nghịch đảo modulo qua định lý Fermat nhỏ.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 2 10)
| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `2 10` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | 2^10 = 1024. Khi lấy dư cho 10^9 + 7 ta được: 1024 mod (10^9 + 7) = 1024.... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `1024` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* 2^10 = 1024. Khi lấy dư cho 10^9 + 7 ta được: 1024 mod (10^9 + 7) = 1024.

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

long long powerMod(long long a, long long b, long long m) {
    long long ans = 1;
    a %= m;
    while (b > 0) {
        if (b & 1) ans = (ans * a) % m;
        a = (a * a) % m;
        b >>= 1;
    }
    return ans;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long a;
    string b_str;
    if (!(cin >> a >> b_str)) return 0;

    if (a % MOD == 0) {
        cout << 0 << "\n";
        return 0;
    }

    long long rem_b = 0;
    for (char c : b_str) {
        rem_b = (rem_b * 10 + (c - '0')) % (MOD - 1);
    }

    cout << powerMod(a, rem_b, MOD) << "\n";
    return 0;
}
```
