# Hướng Dẫn Giảng Dạy: Chữ Số Hàng Đơn Vị
Chuyên đề: **Chương 00: Ôn tập nền tảng C++**

---

## 1. Mục Tiêu Học Tập & Chuẩn Đầu Ra
- Hiểu toán tử `%` (modulo / phần dư) và ứng dụng tách chữ số.

---

## 2. Phân Tích Đề Bài & Bản Chất Toán Học
- Chữ số cuối = $N \% 10$. Luôn đúng với mọi $N > 0$.

---

## 3. Câu Hỏi Gợi Mở Dẫn Dắt
- `2024 % 10` bằng bao nhiêu? `2024 / 10` bằng bao nhiêu?
- Làm sao lấy chữ số hàng chục?

---

## 4. Chiến Lược Tối Ưu & Bất Biến
- $N \% 10$ luôn trả về chữ số cuối. $\mathcal{O}(1)$.

---

## 5. Mô Phỏng Từng Bước Trên Sample

| Bước | Thao tác | Giá trị | Kết quả |
|---|---|---|---|
| 1 | Đọc $N$ | $2024$ | — |
| 2 | $2024 \% 10 = 4$ | $4$ | In ra $4$ |

---

## 6. Phân Tích Độ Phức Tạp
- $\mathcal{O}(1)$.

---

## 7. Các Bẫy Lỗi Lập Trình Kinh Điển
- **Bẫy 1:** Nhầm `%` với `/`. `2024 / 10 = 202` (bỏ chữ số cuối), `2024 % 10 = 4` (lấy chữ số cuối).

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

    cout << n % 10 << '\n';
    return 0;
}
```

---

## 9. Bài Toán Mở Rộng & Chuyển Giao
- Tách tất cả chữ số (dùng vòng lặp `while`).
- Tính tổng các chữ số của $N$.
