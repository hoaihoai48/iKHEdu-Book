# Hướng Dẫn Giảng Dạy: Kiểm Tra Năm Nhuận
Chuyên đề: **Chương 00: Ôn tập nền tảng C++**

---

## 1. Mục Tiêu Học Tập & Chuẩn Đầu Ra
- Xử lý điều kiện phức hợp với `&&` (và) và `||` (hoặc).

---

## 2. Phân Tích Đề Bài & Bản Chất Toán Học
- Năm nhuận: $(Y \% 4 = 0 \text{ AND } Y \% 100 \ne 0)$ OR $(Y \% 400 = 0)$.

---

## 3. Câu Hỏi Gợi Mở Dẫn Dắt
- Năm 2000 có phải năm nhuận không? Năm 1900?
- Tại sao cần 3 điều kiện chứ không phải chỉ chia hết cho 4?

---

## 4. Chiến Lược Tối Ưu & Bất Biến
- Kiểm tra trực tiếp. $\mathcal{O}(1)$.

---

## 5. Mô Phỏng Từng Bước Trên Sample

| Year | $\% 4$ | $\% 100$ | $\% 400$ | Kết quả |
|---|---|---|---|---|
| $2024$ | $= 0$ | $\ne 0$ | — | YES |
| $1900$ | $= 0$ | $= 0$ | $\ne 0$ | NO |
| $2000$ | $= 0$ | $= 0$ | $= 0$ | YES |

---

## 6. Phân Tích Độ Phức Tạp
- $\mathcal{O}(1)$.

---

## 7. Các Bẫy Lỗi Lập Trình Kinh Điển
- **Bẫy 1:** Quên điều kiện `% 100 != 0`.
- **Bẫy 2:** Thiếu ngoặc khi kết hợp `&&` và `||`.

---

## 8. Mã Nguồn Tham Chiếu
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int y;
    if (!(cin >> y)) return 0;

    if ((y % 4 == 0 && y % 100 != 0) || y % 400 == 0) {
        cout << "YES" << '\n';
    } else {
        cout << "NO" << '\n';
    }
    return 0;
}
```

---

## 9. Bài Toán Mở Rộng & Chuyển Giao
- Tính số ngày trong tháng 2 của năm $Y$.
- Đếm số năm nhuận trong khoảng $[A, B]$.
