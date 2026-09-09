# Hướng Dẫn Giảng Dạy: Chia Kẹo Trung Thu
Chuyên đề: **Chương 01 — Bài 01: Biến, Kiểu Dữ Liệu, Toán Tử & Nhập Xuất An Toàn**

---

## 1. Mục Tiêu Học Tập & Chuẩn Đầu Ra
- Áp dụng ý nghĩa thực tế của phép chia nguyên `/` (thương số) và phép chia dư `%` (phần dư).
- Nhận thức về điều kiện dữ liệu lên tới $10^9$ cần dùng kiểu `long long`.

---

## 2. Phân Tích Đề Bài & Bản Chất Toán Học
- Định lý chia có dư: Với mọi số nguyên dương $N, K$, luôn tồn tại duy nhất cặp số $q, r$ sao cho:
$$N = q \times K + r \quad (0 \le r < K)$$

- Trong đó $q = N / K$ là số kẹo mỗi bạn nhận được, $r = N \% K$ là số kẹo dư.

---

## 3. Câu Hỏi Gợi Mở Dẫn Dắt
- Khi chia đều cho $K$ bạn, số kẹo dư tối đa có thể là bao nhiêu (Luôn nhỏ hơn $K$).
- Phép toán nào trong C++ cho ta thương số và phép toán nào cho ta số dư

---

## 4. Chiến Lược Tối Ưu & Bất Biến Thuật Toán
- Đọc $N, K$ kiểu `long long`.
- Tính `each = n / k` và `rem = n % k`. In ra kết quả.

---

## 5. Mô Phỏng Từng Bước Trên Sample

| Tổng số kẹo $N$ | Số học sinh $K$ | Thương $N / K$ | Số dư $N \% K$ | Kết quả |
|:---:|:---:|:---:|:---:|:---:|
| `23` | `5` | `4` | `3` | `4 3` |
| `30` | `6` | `5` | `0` | `5 0` |

---

## 6. Phân Tích Độ Phức Tạp
- Thời gian: $\mathcal{O}(1)$.
- Không gian: $\mathcal{O}(1)$.

---

## 7. Các Bẫy Lỗi Lập Trình Kinh Điển
- Chia cho 0 (trong bài này đề bài cho $K \ge 1$, nhưng cần luôn cảnh báo học sinh không bao giờ chia cho số 0).
- Nhầm thứ tự in: in số dư trước thương số sau.

---

## 8. Mã Nguồn Tham Chiếu
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
ios::sync_with_stdio(false);
cin.tie(nullptr);

long long n, k;
if (!(cin >> n >> k)) return 0;

long long each = n / k;
long long rem = n % k;

cout << each << ' ' << rem << '\n';
return 0;
}
```

---

## 9. Bài Toán Mở Rộng & Chuyển Giao
- Bài toán tìm số chuyến xe tối thiểu để chở hết $N$ người biết mỗi xe chở tối đa $K$ người (công thức làm tròn lên: `(n + k - 1) / k`).
