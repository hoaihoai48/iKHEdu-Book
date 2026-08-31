# Hướng Dẫn Giảng Dạy: Nghịch Đảo Modulo Bằng Euclid Mở Rộng
Chuyên đề: **Đồng Dư Thức & Lũy Thừa Nhị Phân (Modular Arithmetic)**

**Phân loại chuyên đề:** `Core Foundation` (Kiến thức nền tảng bắt buộc)

---

## 1. Mục Tiêu Học Tập & Chuẩn Đầu Ra (Learning Objectives)
* **Kỹ năng cốt lõi:** Nắm vững và làm chủ kỹ thuật giải quyết bài toán: Nghịch Đảo Modulo Bằng Euclid Mở Rộng.
* **Tư duy thuật toán:** Rèn luyện phản xạ phân tích tính chất đồng dư, áp dụng lũy thừa nhị phân $\mathcal{O}(\log N)$, nghịch đảo modulo và tránh tràn số.
* **Chuẩn code thi đấu:** Cài đặt code C++ chuẩn thi đấu (Fast I/O, Safe Input, không tiền tố thừa, quản lý số dư âm chặt chẽ).

---

## 2. Phân Tích Đề Bài & Bản Chất Toán Học
* **Dữ liệu đầu vào:** - Một dòng duy nhất chứa 2 số nguyên $A, M$ ($1 \le A, M \le 10^9, \gcd(A, M) = 1$).
* **Yêu cầu cốt lõi:** Cho hai số nguyên dương $A, M$ với $\gcd(A, M) = 1$. Hãy tìm nghịch đảo modulo $A^{-1} \pmod M$ bằng thuật toán Euclid mở rộng.
* **Trường hợp biên (Edge Cases):**
  * Giá trị $A, B = 0$ hoặc $B = 1$.
  * Số dư âm trong phép trừ.
  * Phép nhân tràn số 32-bit (bắt buộc dùng `long long` hoặc ép kiểu).

---

## 3. Câu Hỏi Dẫn Dắt Tư Duy (Socratic Method)
1. Bài toán có thể chia để trị số mũ $B$ thành $\lfloor B / 2 \rfloor$ không?
2. Có xuất hiện phép chia trên vành Modulo không? Nếu có, modulo $M$ có phải số nguyên tố không?
3. Trong phép trừ, ta cần làm gì để số dư không bao giờ bị âm trong C++?

---

## 4. Chiến Lược Tối Ưu & Bất Biến Thuật Toán (Invariant)
### 4.1. Chiến lược thực thi:
- Triển khai Lũy thừa nhị phân lặp hoặc tiền xử lý mảng giai thừa / nghịch đảo.
- Áp dụng các định lý số học (Fermat nhỏ, Euclid mở rộng).

### 4.2. Bất biến toán học (Invariant):
> Mọi phép toán biến đổi đều bảo toàn tính chất đồng dư trên vành $\mathbb{Z}_M$.

---

## 5. Mô Phỏng Từng Bước Trên Sample (Dry Run)
### Dữ liệu Sample:
* **Input:**
```text
3 7
```
* **Output:**
```text
5
```
* **Phân tích quá trình thực thi:**
  3 * 5 = 15 = 1 mod 7.

---

## 6. Phân Tích Độ Phức Tạp Thời Gian & Không Gian
- **Thời gian (Time Complexity):** Thuật toán chạy trong $\mathcal{O}(\log B)$ hoặc $\mathcal{O}(1)$ mỗi truy vấn sau tiền xử lý.
- **Không gian (Space Complexity):** $\mathcal{O}(1)$ hoặc $\mathcal{O}(N)$ bộ nhớ phụ trợ.

---

## 7. Các Bẫy Lỗi Lập Trình Kinh Điển (Bug Traps)
1. Tràn số khi nhân hai số $\approx 10^9$ (bắt buộc dùng `(1LL * a * b) % M`).
2. Quên cộng $M$ trong phép trừ: `(a - b + M) % M`.
3. Chia trực tiếp `(A / B) % M` gây sai bản chất toán học.

---

## 8. Mã Nguồn Tham Chiếu C++ Chuẩn Thi Đấu
```cpp
#include <bits/stdc++.h>
using namespace std;

long long extGCD(long long a, long long b, long long &x, long long &y) {
    if (b == 0) {
        x = 1;
        y = 0;
        return a;
    }
    long long x1, y1;
    long long d = extGCD(b, a % b, x1, y1);
    x = y1;
    y = x1 - y1 * (a / b);
    return d;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long a, m;
    if (!(cin >> a >> m)) return 0;

    long long x, y;
    extGCD(a, m, x, y);
    x = (x % m + m) % m;

    cout << x << "
";
    return 0;
}
```

---

## 9. Bài Toán Mở Rộng & Chuyển Giao (Transfer & Extensions)
* **Mở rộng 1:** Áp dụng vào các bài toán quy hoạch động đếm đường đi, đếm dãy ngoặc đúng (Catalan).
* **Mở rộng 2:** Tích hợp Lũy thừa nhị phân vào phép nhân ma trận trên đồ thị.
