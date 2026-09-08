# Hướng Dẫn Giảng Dạy: Trung Bình Ba Số
Chuyên đề: **Chương 00: Ôn tập nền tảng C++**

---

## 1. Mục Tiêu Học Tập & Chuẩn Đầu Ra
- Sử dụng kiểu `double` cho số thực.
- Kỹ thuật ép kiểu `1.0 * sum / n` để giữ phần thập phân.
- Định dạng output với `fixed` và `setprecision`.

---

## 2. Phân Tích Đề Bài & Bản Chất Toán Học
- Trung bình: $\text{avg} = (a + b + c) / 3$.
- Nếu chia `int / int`, C++ sẽ cho kết quả chia nguyên (mất phần thập phân).

---

## 3. Câu Hỏi Gợi Mở Dẫn Dắt
- Nếu viết `(a + b + c) / 3` với $a, b, c$ kiểu `int`, kết quả sẽ ra sao?
- Làm sao để giữ phần thập phân?

---

## 4. Chiến Lược Tối Ưu & Bất Biến
- Nhân $1.0$ trước khi chia để ép sang `double`. $\mathcal{O}(1)$.

---

## 5. Mô Phỏng Từng Bước Trên Sample

| Bước | Thao tác | Giá trị | Kết quả |
|---|---|---|---|
| 1 | Đọc $a, b, c$ | $7, 8, 9$ | — |
| 2 | $\text{sum} = 7+8+9 = 24$ | $24$ | — |
| 3 | $\text{avg} = 1.0 \times 24 / 3 = 8.0$ | $8.0$ | In `8.00` |

---

## 6. Phân Tích Độ Phức Tạp
- $\mathcal{O}(1)$ thời gian và không gian.

---

## 7. Các Bẫy Lỗi Lập Trình Kinh Điển
- **Bẫy 1 — Chia nguyên:** `(7+8+9)/3` cho `8` thay vì `8.00`. Phải nhân `1.0` trước.
- **Bẫy 2 — Thiếu setprecision:** Không in đủ 2 chữ số thập phân.

---

## 8. Mã Nguồn Tham Chiếu
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int a, b, c;
    if (!(cin >> a >> b >> c)) return 0;

    double avg = 1.0 * (a + b + c) / 3;
    cout << fixed << setprecision(2) << avg << '\n';
    return 0;
}
```

---

## 9. Bài Toán Mở Rộng & Chuyển Giao
- Tính trung bình có trọng số.
- Tính trung bình N số (dùng vòng lặp).
