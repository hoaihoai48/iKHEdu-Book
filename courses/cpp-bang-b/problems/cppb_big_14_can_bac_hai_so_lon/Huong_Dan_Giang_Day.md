# Hướng Dẫn Giảng Dạy: Căn Bậc Hai Số Nguyên Lớn
Chuyên đề: **Bài 09: Xử lý số nguyên lớn (BigInt)**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho số nguyên dương lớn A (có tới 1000 chữ số). Hãy tìm phần nguyên căn bậc hai floor(sqrt(A)).

- **Phương pháp tiếp cận — Xử lý số nguyên lớn (BigInt):**
  - Biểu diễn số lớn bằng chuỗi ký tự `string` hoặc mảng các chữ số `vector<int>` đảo ngược.
  - Mô phỏng các phép tính cộng, trừ, nhân, chia bằng thuật toán đặt tính từng cột như tiểu học.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 17)
| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `17` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | sqrt(17) = 4.123... Phần nguyên là 4.... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `4` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* sqrt(17) = 4.123... Phần nguyên là 4.

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

string mulBig(string a, string b) {
    if (a == "0" || b == "0") return "0";
    reverse(a.begin(), a.end());
    reverse(b.begin(), b.end());
    int n = a.size(), m = b.size();
    vector<int> c(n + m, 0);
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            c[i + j] += (a[i] - '0') * (b[j] - '0');
        }
    }
    int carry = 0;
    string res = "";
    for (int i = 0; i < n + m || carry; ++i) {
        if (i < (int)c.size()) carry += c[i];
        res.push_back((carry % 10) + '0');
        carry /= 10;
    }
    while (res.size() > 1 && res.back() == '0') res.pop_back();
    reverse(res.begin(), res.end());
    return res;
}

string addBig(string a, string b) {
    reverse(a.begin(), a.end());
    reverse(b.begin(), b.end());
    string res = "";
    int carry = 0;
    int n = max(a.size(), b.size());
    for (int i = 0; i < n || carry; ++i) {
        int sum = carry;
        if (i < (int)a.size()) sum += a[i] - '0';
        if (i < (int)b.size()) sum += b[i] - '0';
        res.push_back((sum % 10) + '0');
        carry = sum / 10;
    }
    reverse(res.begin(), res.end());
    return res;
}

string div2(string a) {
    string res = "";
    int cur = 0;
    for (char c : a) {
        cur = cur * 10 + (c - '0');
        res.push_back((cur / 2) + '0');
        cur %= 2;
    }
    int pos = 0;
    while (pos + 1 < (int)res.size() && res[pos] == '0') pos++;
    return res.substr(pos);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string a;
    if (!(cin >> a)) return 0;

    int target_len = (a.size() + 1) / 2;
    string low = "1";
    string high = string(target_len + 1, '9');
    string ans = "1";

    while (!isLess(high, low)) {
        string mid = div2(addBig(low, high));
        string sq = mulBig(mid, mid);
        if (!isLess(a, sq)) {
            ans = mid;
            low = addBig(mid, "1");
        } else {
            // high = mid - 1
            // vi low, high chi dung cho binary search chuoi
            int borrow = 1;
            for (int i = (int)mid.size() - 1; i >= 0; --i) {
                if (mid[i] >= '1') { mid[i]--; break; }
                else mid[i] = '9';
            }
            while (mid.size() > 1 && mid[0] == '0') mid.erase(mid.begin());
            high = mid;
        }
    }

    cout << ans << "\n";
    return 0;
}
```
