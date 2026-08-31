# Hướng Dẫn Giảng Dạy: Chia Hai Số Nguyên Lớn (A / B)
Chuyên đề: **Xử Lý Số Nguyên Lớn (Big Integer Arithmetic)**

**Phân loại chuyên đề:** `Advanced Challenge` (Kiến thức mở rộng chuyên sâu)

---

## 1. Mục Tiêu Học Tập & Chuẩn Đầu Ra (Learning Objectives)
* **Kỹ năng cốt lõi:** Nắm vững và làm chủ kỹ thuật giải quyết bài toán: Chia Hai Số Nguyên Lớn (A / B).
* **Tư duy thuật toán:** Rèn luyện phản xạ mô phỏng đặt tính số học trên chuỗi ký tự (`string`) hoặc mảng (`vector<int>`), quản lý biến nhớ `carry` và `borrow`.
* **Chuẩn code thi đấu:** Cài đặt code C++ chuẩn thi đấu (Fast I/O, Safe Input, không tiền tố thừa, xóa sạch số 0 vô nghĩa ở đầu).

---

## 2. Phân Tích Đề Bài & Bản Chất Toán Học
* **Dữ liệu đầu vào:** - Dòng 1: Chuỗi ký tự số $A$ ($1 \le |A| \le 1000$).
- Dòng 2: Chuỗi ký tự số $B$ ($1 \le |B| \le 1000$).
* **Yêu cầu cốt lõi:** Cho 2 số nguyên dương lớn $A$ và $B$. Hãy tìm thương nguyên $\lfloor A / B \rfloor$.
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
1000
30
```
* **Output:**
```text
33
```
* **Phân tích quá trình thực thi:**
  1000 / 30 = 33.

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
        cout << "0
";
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
    cout << res.substr(pos) << "
";
    return 0;
}
```

---

## 9. Bài Toán Mở Rộng & Chuyển Giao (Transfer & Extensions)
* **Mở rộng 1:** Áp dụng kỹ thuật nén Base $10^9$ để tăng tốc độ gấp hàng chục lần.
* **Mở rộng 2:** Tích hợp số lớn vào các thuật toán quy hoạch động đếm số cách (DP đếm).
