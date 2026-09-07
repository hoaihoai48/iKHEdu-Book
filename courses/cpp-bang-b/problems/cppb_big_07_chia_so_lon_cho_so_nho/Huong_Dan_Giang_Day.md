# Hướng Dẫn Giảng Dạy: Chia Số Lớn Cho Số Nhỏ (Lấy Thương)
Chuyên đề: **Bài 09: Xử lý số nguyên lớn (BigInt)**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho số nguyên lớn A và số nguyên nhỏ b (1 <= b <= 10^9). Hãy tìm phần nguyên thương số floor(A / b).

- **Phương pháp tiếp cận — Xử lý số nguyên lớn (BigInt):**
  - Biểu diễn số lớn bằng chuỗi ký tự `string` hoặc mảng các chữ số `vector<int>` đảo ngược.
  - Mô phỏng các phép tính cộng, trừ, nhân, chia bằng thuật toán đặt tính từng cột như tiểu học.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 1000 3)
| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `1000 3` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | 1000 chia cho 3 được phần nguyên thương là 333.... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `333` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* 1000 chia cho 3 được phần nguyên thương là 333.

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

string divSmall(string a, long long b) {
    string res = "";
    long long cur = 0;

    for (char c : a) {
        cur = cur * 10 + (c - '0');
        res.push_back((cur / b) + '0');
        cur %= b;
    }

    int pos = 0;
    while (pos + 1 < (int)res.size() && res[pos] == '0') pos++;
    return res.substr(pos);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string a;
    long long b;
    if (!(cin >> a >> b)) return 0;

    cout << divSmall(a, b) << "\n";
    return 0;
}
```
