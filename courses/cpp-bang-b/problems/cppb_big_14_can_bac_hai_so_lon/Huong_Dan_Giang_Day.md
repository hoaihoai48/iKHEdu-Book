# Hướng Dẫn Giảng Dạy: Căn Bậc Hai Số Nguyên Lớn
Chuyên đề: **Xử Lý Số Nguyên Lớn (Big Integer Arithmetic)**

**Phân loại chuyên đề:** `Advanced Challenge` (Kiến thức mở rộng chuyên sâu)

---

## 1. Mục Tiêu Học Tập & Chuẩn Đầu Ra (Learning Objectives)
* **Kỹ năng cốt lõi:** Nắm vững và làm chủ kỹ thuật giải quyết bài toán: Căn Bậc Hai Số Nguyên Lớn.
* **Tư duy thuật toán:** Rèn luyện phản xạ mô phỏng đặt tính số học trên chuỗi ký tự (`string`) hoặc mảng (`vector<int>`), quản lý biến nhớ `carry` và `borrow`.
* **Chuẩn code thi đấu:** Cài đặt code C++ chuẩn thi đấu (Fast I/O, Safe Input, không tiền tố thừa, xóa sạch số 0 vô nghĩa ở đầu).

---

## 2. Phân Tích Đề Bài & Bản Chất Toán Học
* **Dữ liệu đầu vào:** - Một dòng duy nhất chứa chuỗi ký tự số $A$ ($1 \le |A| \le 1000$).
* **Yêu cầu cốt lõi:** Cho số nguyên dương lớn $A$. Hãy tìm phần nguyên căn bậc hai $\lfloor \sqrt{A} \rfloor$.
* **Trường hợp biên (Edge Cases):**
  * Giá trị bằng $0$ (cần in `"0"`, tránh chuỗi rỗng `""`).
  * Phép trừ dẫn đến số âm hoặc các số 0 ở đầu (`leading zeros`).
  * Biến nhớ `carry` ở chữ số cuối cùng.

---

## 3. Câu Hỏi Dẫn Dắt Tư Duy (Socratic Method)
1. Ta nên duyệt chuỗi từ trái sang phải hay đảo ngược chuỗi để hàng đơn vị ở `index = 0`?
2. Trong phép nhân hai số lớn $A$ và $B$, kích thước tối đa của mảng kết quả là bao nhiêu?
3. Khi nào cần xóa các số 0 vô nghĩa ở đầu kết quả?

---

## 4. Chiến Lược Tối Ưu & Bất Biến Thuật Toán (Invariant)
### 4.1. Chiến lược thực thi:
- Đảo ngược chuỗi để thao tác `push_back()` đạt $\mathcal{O}(1)$.
- Mô phỏng đúng quy tắc đặt tính toán học tiểu học.

### 4.2. Bất biến toán học (Invariant):
> Chữ số hàng $k$ của kết quả luôn được xác định bởi tổng các tích chữ số có tổng chỉ số bằng $k$ cộng dồn với biến nhớ.

---

## 5. Mô Phỏng Từng Bước Trên Sample (Dry Run)
### Dữ liệu Sample:
* **Input:**
```text
100
```
* **Output:**
```text
10
```
* **Phân tích quá trình thực thi:**
  sqrt(100) = 10.

---

## 6. Phân Tích Độ Phức Tạp Thời Gian & Không Gian
- **Thời gian (Time Complexity):** $\mathcal{O}(L)$ cho phép cộng/trừ/chia nhỏ, $\mathcal{O}(L_A \times L_B)$ cho phép nhân lớn.
- **Không gian (Space Complexity):** $\mathcal{O}(L)$ bộ nhớ lưu trữ chuỗi kết quả.

---

## 7. Các Bẫy Lỗi Lập Trình Kinh Điển (Bug Traps)
1. Quên xử lý `carry` còn lại sau vòng lặp.
2. In ra các số 0 vô nghĩa (ví dụ `007` thay vì `7`).
3. Phép nhân số lớn với 0 trả về chuỗi rỗng thay vì `"0"`.

---

## 8. Mã Nguồn Tham Chiếu C++ Chuẩn Thi Đấu
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

    cout << ans << "
";
    return 0;
}
```

---

## 9. Bài Toán Mở Rộng & Chuyển Giao (Transfer & Extensions)
* **Mở rộng 1:** Áp dụng kỹ thuật nén Base $10^9$ để tăng tốc độ gấp hàng chục lần.
* **Mở rộng 2:** Tích hợp số lớn vào các thuật toán quy hoạch động đếm số cách (DP đếm).
