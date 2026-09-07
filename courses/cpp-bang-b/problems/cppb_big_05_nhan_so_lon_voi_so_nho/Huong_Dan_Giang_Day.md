# Hướng Dẫn Giảng Dạy: Nhân Số Lớn Với Số Nhỏ
Chuyên đề: **Bài 09: Xử lý số nguyên lớn (BigInt)**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho số nguyên lớn A và số nguyên nhỏ b (0 <= b <= 10^9). Hãy tính tích A * b.

- **Phương pháp tiếp cận — Xử lý số nguyên lớn (BigInt):**
  - Biểu diễn số lớn bằng chuỗi ký tự `string` hoặc mảng các chữ số `vector<int>` đảo ngược.
  - Mô phỏng các phép tính cộng, trừ, nhân, chia bằng thuật toán đặt tính từng cột như tiểu học.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 123456789 5)
| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `123456789 5` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | 123456789 * 5 = 617283945.... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `617283945` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* 123456789 * 5 = 617283945.

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

string mulSmall(string a, long long b) {
    if (a == "0" || b == 0) return "0";

    reverse(a.begin(), a.end());
    string res = "";
    long long carry = 0;

    for (int i = 0; i < (int)a.size() || carry; ++i) {
        long long prod = carry;
        if (i < (int)a.size()) prod += 1LL * (a[i] - '0') * b;
        res.push_back((prod % 10) + '0');
        carry = prod / 10;
    }

    while (res.size() > 1 && res.back() == '0') res.pop_back();
    reverse(res.begin(), res.end());
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string a;
    long long b;
    if (!(cin >> a >> b)) return 0;

    cout << mulSmall(a, b) << "\n";
    return 0;
}
```
