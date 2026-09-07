# Hướng Dẫn Giảng Dạy: Tổng Các Chữ Số Của N!
Chuyên đề: **Bài 09: Xử lý số nguyên lớn (BigInt)**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho số nguyên N (1 <= N <= 1000). Hãy tính tổng tất cả các chữ số của N!.

- **Phương pháp tiếp cận — Xử lý số nguyên lớn (BigInt):**
  - Biểu diễn số lớn bằng chuỗi ký tự `string` hoặc mảng các chữ số `vector<int>` đảo ngược.
  - Mô phỏng các phép tính cộng, trừ, nhân, chia bằng thuật toán đặt tính từng cột như tiểu học.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 10)
| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `10` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | 10! = 3628800. Tổng các chữ số là: 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `27` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* 10! = 3628800. Tổng các chữ số là: 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

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

string mulSmall(string a, int b) {
    reverse(a.begin(), a.end());
    string res = "";
    int carry = 0;
    for (int i = 0; i < (int)a.size() || carry; ++i) {
        int prod = carry;
        if (i < (int)a.size()) prod += (a[i] - '0') * b;
        res.push_back((prod % 10) + '0');
        carry = prod / 10;
    }
    reverse(res.begin(), res.end());
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    string fact = "1";
    for (int i = 2; i <= n; ++i) {
        fact = mulSmall(fact, i);
    }

    long long sum_digits = 0;
    for (char c : fact) {
        sum_digits += (c - '0');
    }

    cout << sum_digits << "\n";
    return 0;
}
```
