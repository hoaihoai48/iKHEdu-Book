# Hướng Dẫn Giảng Dạy: Chia Kẹo Công Bằng
Chuyên đề: **Chương 00: Ôn tập nền tảng C++**

---

## 1. Mục Tiêu Học Tập & Chuẩn Đầu Ra
- Phân biệt phép chia nguyên `/` và phép lấy dư `%`.
- Hiểu mối quan hệ: $M = (M / N) \times N + (M \% N)$.

---

## 2. Phân Tích Đề Bài & Bản Chất Toán Học
- Mỗi bạn nhận: $M / N$ (chia nguyên). Số dư: $M \% N$.

---

## 3. Câu Hỏi Gợi Mở Dẫn Dắt
- `17 / 5` và `17 % 5` cho kết quả gì?
- Nếu $M$ chia hết cho $N$ thì số dư bằng bao nhiêu?

---

## 4. Chiến Lược Tối Ưu & Bất Biến
- $\mathcal{O}(1)$. Công thức chuẩn: phần nguyên = $M/N$, phần dư = $M\%N$.

---

## 5. Mô Phỏng Từng Bước Trên Sample

| Bước | Thao tác | Giá trị | Kết quả |
|---|---|---|---|
| 1 | Đọc $M, N$ | $17, 5$ | — |
| 2 | $17 / 5 = 3$ | $3$ | — |
| 3 | $17 \% 5 = 2$ | $2$ | In `3 2` |

---

## 6. Phân Tích Độ Phức Tạp
- $\mathcal{O}(1)$.

---

## 7. Các Bẫy Lỗi Lập Trình Kinh Điển
- **Bẫy 1:** Với $M$ lớn ($10^9$), cần dùng `long long` để tránh tràn.

---

## 8. Mã Nguồn Tham Chiếu
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long m, n;
    if (!(cin >> m >> n)) return 0;

    cout << m / n << ' ' << m % n << '\n';
    return 0;
}
```

---

## 9. Bài Toán Mở Rộng & Chuyển Giao
- Chia kẹo nhưng cô lấy dư, trả về tổng kẹo cô có.
- Chia kẹo cho nhiều nhóm với số lượng khác nhau.
