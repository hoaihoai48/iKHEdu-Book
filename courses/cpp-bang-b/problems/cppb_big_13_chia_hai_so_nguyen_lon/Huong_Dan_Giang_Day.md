# Hướng Dẫn Giảng Dạy: Chia Hai Số Nguyên Lớn (A / B)
Chuyên đề: **Bài 09: Xử lý số nguyên lớn (BigInt)**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho 2 số nguyên dương lớn A và B. Hãy tìm phần nguyên thương số floor(A / B).

- **Phương pháp tiếp cận — Xử lý số nguyên lớn (BigInt):**
  - Biểu diễn số lớn bằng chuỗi ký tự `string` hoặc mảng các chữ số `vector<int>` đảo ngược.
  - Mô phỏng các phép tính cộng, trừ, nhân, chia bằng thuật toán đặt tính từng cột như tiểu học.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 100 3)
| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `100 3` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | 100 / 3 = 33 (dư 1). Phần nguyên thương là 33.... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `33` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* 100 / 3 = 33 (dư 1). Phần nguyên thương là 33.

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

bool isLess(const string &a, const string &b) {
    if (a.size() != b.size()) return a.size() < b.size();
    return a < b;
}

string subBig(string a, string b) {
    reverse(a.begin(), a.end());
    reverse(b.begin(), b.end());
    string res = "";
    int borrow = 0;
    for (int i = 0; i < (int)a.size(); ++i) {
        int diff = (a[i] - '0') - borrow;
        if (i < (int)b.size()) diff -= (b[i] - '0');
        if (diff < 0) { diff += 10; borrow = 1; }
        else borrow = 0;
        res.push_back(diff + '0');
    }
    while (res.size() > 1 && res.back() == '0') res.pop_back();
    reverse(res.begin(), res.end());
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string a, b;
    if (!(cin >> a >> b)) return 0;

    if (isLess(a, b)) {
        cout << "0\n";
        return 0;
    }

    string cur = "";
    string res = "";

    for (char c : a) {
        cur.push_back(c);
        while (cur.size() > 1 && cur[0] == '0') cur.erase(cur.begin());
        int digit = 0;
        while (!isLess(cur, b)) {
            cur = subBig(cur, b);
            digit++;
        }
        res.push_back(digit + '0');
    }

    int pos = 0;
    while (pos + 1 < (int)res.size() && res[pos] == '0') pos++;
    cout << res.substr(pos) << "\n";
    return 0;
}
```
