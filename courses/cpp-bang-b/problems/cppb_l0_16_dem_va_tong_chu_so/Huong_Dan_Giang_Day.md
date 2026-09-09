# Hướng Dẫn Giảng Dạy: Đếm Chữ Số & Tổng Chữ Số Của Số Nguyên
Chuyên đề: **Chương 01 — Bài 02: Cấu Trúc Rẽ Nhánh & Cấu Trúc Vòng Lặp**

---

## 1. Mục Tiêu Học Tập & Chuẩn Đầu Ras
- Thành thạo vòng lặp `while (n > 0)` để trích xuất từng chữ số bằng `% 10` và `/= 10`.
- Xử lý trọn vẹn trường hợp biên đặc biệt $N = 0$.
- Phối hợp cùng lúc 2 mẫu tích lũy: mẫu Đếm (`count_digits++`) và mẫu Tổng (`sum_digits += n % 10`).

---

## 2. Phân Tích Đề Bài & Bản Chất Toán Học
- Với số nguyên $N > 0$:
- Chữ số cuối cùng là $N \% 10$.
- Sau khi lấy chữ số cuối, ta bỏ nó đi bằng phép chia nguyên $N = N / 10$.
- Quá trình này lặp lại cho đến khi $N = 0$.
- Số lần lặp chính là số lượng chữ số của $N$.
- **Edge case:** Khi $N = 0$, nếu chạy trực tiếp vào `while (n > 0)` thì vòng lặp không chạy lần nào, dẫn đến đếm ra 0 chữ số (sai). Vì vậy cần kiểm tra riêng trường hợp $N = 0$.

---

## 3. Câu Hỏi Gợi Mở Dẫn Dắt
- Khi nào vòng lặp rút trích chữ số sẽ dừng lại (Khi $N$ giảm về bằng 0).
- Nếu người dùng nhập vào số 0 thì vòng lặp `while (n > 0)` có chạy không Ta xử lý thế nào

---

## 4. Chiến Lược Tối Ưu & Bất Biến Thuật Toán
- Đọc $N$ kiểu `long long`.
- Nếu $N = 0$, in `1 0` và thoát ngay.
- Khởi tạo `count_digits = 0`, `sum_digits = 0`.
- Dùng vòng lặp `while (n > 0)` cập nhật biến đếm và biến tổng.

---

## 5. Mô Phỏng Từng Bước Trên Sample ($N = 12345$)

| Bước | Giá trị $N$ | `n % 10` | `sum_digits` | `count_digits` | `n /= 10` mới |
|:---:|:---:|:---:|:---:|:---:|:---:|
| Ban đầu | `12345` | — | `0` | `0` | — |
| Lần 1 | `12345` | 5 | 5 | 1 | `1234` |
| Lần 2 | `1234` | 4 | 9 | 2 | `123` |
| Lần 3 | `123` | 3 | 12 | 3 | `12` |
| Lần 4 | `12` | 2 | 14 | 4 | `1` |
| Lần 5 | `1` | 1 | 15 | 5 | `0` (Dừng) |

---

## 6. Phân Tích Độ Phức Tạp
- Thời gian: $\mathcal{O}(\log_{10} N)$ (với $N \le 10^{18}$, số bước lặp tối đa là 19 vòng lặp, chạy trong $0.000001\text{s}$).
- Không gian: $\mathcal{O}(1)$.

---

## 7. Các Bẫy Lỗi Lập Trình Kinh Điển
- Bẫy $N = 0$ (cho ra 0 chữ số thay vì 1 chữ số).
- Dùng kiểu `int` cho biến $N$ dẫn đến tràn số khi $N > 2 \times 10^9$.

---

## 8. Mã Nguồn Tham Chiếu
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
ios::sync_with_stdio(false);
cin.tie(nullptr);

long long n;
if (!(cin >> n)) return 0;

if (n == 0) {
cout << "1 0\n";
return 0;
}

int count_digits = 0;
long long sum_digits = 0;

while (n > 0) {
sum_digits += n % 10;
count_digits++;
n /= 10;
}

cout << count_digits << ' ' << sum_digits << '\n';
return 0;
}
```

---

## 9. Bài Toán Mở Rộng & Chuyển Giao
- Tìm chữ số đầu tiên của số nguyên $N$.
- Kiểm tra số siêu nguyên tố hoặc số đối xứng số học.
