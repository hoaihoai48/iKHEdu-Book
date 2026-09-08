# Hướng Dẫn Giảng Dạy: Diện Tích Hình Chữ Nhật
Chuyên đề: **Chương 00: Ôn tập nền tảng C++**

---

## 1. Mục Tiêu Học Tập & Chuẩn Đầu Ra
- Áp dụng công thức toán học vào code C++.
- Phân biệt phép nhân và phép cộng trong biểu thức.

---

## 2. Phân Tích Đề Bài & Bản Chất Toán Học
- Chu vi: $P = 2(a + b)$. Diện tích: $S = a \times b$.
- Với $a, b \le 10^4$: $S \le 10^8$ (vẫn trong giới hạn `int`).

---

## 3. Câu Hỏi Gợi Mở Dẫn Dắt
- Công thức chu vi và diện tích HCN là gì?
- Nếu $a = b$ thì hình gì?

---

## 4. Chiến Lược Tối Ưu & Bất Biến
- Đọc → Tính → In. $\mathcal{O}(1)$.

---

## 5. Mô Phỏng Từng Bước Trên Sample

| Bước | Thao tác | Giá trị | Kết quả |
|---|---|---|---|
| 1 | Đọc $a, b$ | $5, 3$ | — |
| 2 | $P = 2(5+3) = 16$ | $16$ | — |
| 3 | $S = 5 \times 3 = 15$ | $15$ | In `16 15` |

---

## 6. Phân Tích Độ Phức Tạp
- $\mathcal{O}(1)$ thời gian và không gian.

---

## 7. Các Bẫy Lỗi Lập Trình Kinh Điển
- **Bẫy 1:** Nhầm công thức chu vi thiếu nhân $2$.
- **Bẫy 2:** In sai thứ tự (chu vi trước, diện tích sau).

---

## 8. Mã Nguồn Tham Chiếu
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int a, b;
    if (!(cin >> a >> b)) return 0;

    cout << 2 * (a + b) << ' ' << a * b << '\n';
    return 0;
}
```

---

## 9. Bài Toán Mở Rộng & Chuyển Giao
- Tính chu vi/diện tích tam giác, hình tròn.
- Nếu $a, b$ rất lớn, cần dùng kiểu dữ liệu nào?
