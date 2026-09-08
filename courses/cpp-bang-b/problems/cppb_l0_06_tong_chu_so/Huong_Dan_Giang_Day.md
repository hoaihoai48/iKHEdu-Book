# Hướng Dẫn Giảng Dạy: Tổng Các Chữ Số
Chuyên đề: **Chương 00: Ôn tập nền tảng C++**

---

## 1. Mục Tiêu Học Tập & Chuẩn Đầu Ra
- Kết hợp vòng lặp `while` với `%` và `/` để tách từng chữ số.
- Mẫu tích lũy tổng.

---

## 2. Phân Tích Đề Bài & Bản Chất Toán Học
- Lặp: lấy chữ số cuối ($N \% 10$), cộng vào tổng, bỏ chữ số cuối ($N /= 10$).
- Dừng khi $N = 0$.

---

## 3. Câu Hỏi Gợi Mở Dẫn Dắt
- Làm sao lấy chữ số cuối? Làm sao bỏ chữ số cuối?
- Khi nào vòng lặp dừng?

---

## 4. Chiến Lược Tối Ưu & Bất Biến
- Bất biến: mỗi vòng lặp, $N$ giảm 1 chữ số, $\text{sum}$ tăng thêm chữ số cuối.
- $\mathcal{O}(\log_{10} N)$ = tối đa 10 vòng.

---

## 5. Mô Phỏng Từng Bước Trên Sample

| Bước | $N$ | $N \% 10$ | $\text{sum}$ | $N$ sau |
|---|---|---|---|---|
| 1 | $1234$ | $4$ | $4$ | $123$ |
| 2 | $123$ | $3$ | $7$ | $12$ |
| 3 | $12$ | $2$ | $9$ | $1$ |
| 4 | $1$ | $1$ | $10$ | $0$ |

Kết quả: $10$.

---

## 6. Phân Tích Độ Phức Tạp
- $\mathcal{O}(\log_{10} N) \approx \mathcal{O}(10)$.

---

## 7. Các Bẫy Lỗi Lập Trình Kinh Điển
- **Bẫy 1:** Quên `n /= 10` → vòng lặp vô hạn.
- **Bẫy 2:** Dùng `n > 0` thay vì `n != 0` (đúng với $N > 0$).

---

## 8. Mã Nguồn Tham Chiếu
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    int sum = 0;
    while (n > 0) {
        sum += n % 10;
        n /= 10;
    }
    cout << sum << '\n';
    return 0;
}
```

---

## 9. Bài Toán Mở Rộng & Chuyển Giao
- Đếm số chữ số của $N$.
- Đảo ngược các chữ số (ví dụ $123 \to 321$).
- Kiểm tra số $N$ có phải số palindrome không.
