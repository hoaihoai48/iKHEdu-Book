# Hướng Dẫn Giảng Dạy: Số Fibonacci Lớn Thứ N
Chuyên đề: **Xử Lý Số Nguyên Lớn (Big Integer Arithmetic)**

> [!NOTE]
> **Phân loại chuyên đề:** `Core Foundation` (Kiến thức nền tảng bắt buộc)

---

## 1. Mục Tiêu Học Tập & Chuẩn Đầu Ra (Learning Objectives)
* **Kỹ năng cốt lõi:** Nắm vững và làm chủ kỹ thuật giải quyết bài toán: Số Fibonacci Lớn Thứ N.
* **Tư duy thuật toán:** Rèn luyện phản xạ mô phỏng đặt tính số học trên chuỗi ký tự (`string`) hoặc mảng (`vector<int>`), quản lý biến nhớ `carry` và `borrow`.
* **Chuẩn code thi đấu:** Cài đặt code C++ chuẩn thi đấu (Fast I/O, Safe Input, không tiền tố thừa, xóa sạch số 0 vô nghĩa ở đầu).

---

## 2. Phân Tích Đề Bài & Bản Chất Toán Học
* **Dữ liệu đầu vào:** - Một dòng duy nhất chứa số nguyên $N$ ($0 \le N \le 1000$).
* **Yêu cầu cốt lõi:** Cho số nguyên $N$. Hãy in ra giá trị chính xác của số Fibonacci thứ $N$ ($F_0 = 0, F_1 = 1, F_2 = 1, \dots$).
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
10
```
* **Output:**
```text
55
```
* **Phân tích quá trình thực thi:**
  F(10) = 55.

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

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    if (n == 0) { cout << "0
"; return 0; }
    if (n == 1) { cout << "1
"; return 0; }

    string f0 = "0", f1 = "1", f2 = "";
    for (int i = 2; i <= n; ++i) {
        f2 = addBig(f0, f1);
        f0 = f1;
        f1 = f2;
    }

    cout << f1 << "
";
    return 0;
}
```

---

## 9. Bài Toán Mở Rộng & Chuyển Giao (Transfer & Extensions)
* **Mở rộng 1:** Áp dụng kỹ thuật nén Base $10^9$ để tăng tốc độ gấp hàng chục lần.
* **Mở rộng 2:** Tích hợp số lớn vào các thuật toán quy hoạch động đếm số cách (DP đếm).
