# Hướng Dẫn Giảng Dạy: Kiểm Tra Ba Cạnh Tam Giác
Chuyên đề: **Chương 01 — Bài 02: Cấu Trúc Rẽ Nhánh & Cấu Trúc Vòng Lặp**

---

## 1. Mục Tiêu Học Tập & Chuẩn Đầu Ra
- Áp dụng toán tử logic `&&` (VÀ) để kết hợp đồng thời nhiều điều kiện.
- Nắm vững bất đẳng thức tam giác trong hình học phẳng.
- Phòng tránh tràn số khi cộng hai số $10^9$ bằng cách sử dụng kiểu `long long`.

---

## 2. Phân Tích Đề Bài & Bản Chất Toán Học
- Định lý bất đẳng thức tam giác: Ba đoạn thẳng độ dài dương $a, b, c$ tạo thành tam giác khi và chỉ khi tổng độ dài hai cạnh bất kỳ luôn lớn hơn độ dài cạnh còn lại:
$$\begin{cases} a + b > c \\ a + c > b \\ b + c > a \end{cases}$$

- Khi $a, b \le 10^9$, tổng $a + b$ có thể lên tới $2 \times 10^9$, nếu dùng `int` có nguy cơ tràn số khi cộng, do đó cần dùng `long long`.

---

## 3. Câu Hỏi Gợi Mở Dẫn Dắt
- Để ba đoạn thẳng ghép thành tam giác, điều kiện về tổng hai cạnh bất kỳ phải như thế nào so với cạnh thứ ba
- Trong C++, làm sao để biểu diễn việc cả 3 điều kiện đều phải đồng thời xảy ra (Toán tử `&&`).

---

## 4. Chiến Lược Tối Ưu & Bất Biến Thuật Toán
- Đọc $a, b, c$ kiểu `long long`.
- Kiểm tra `(a + b > c && a + c > b && b + c > a)`. In `YES` hoặc `NO`.

---

## 5. Mô Phỏng Từng Bước Trên Sample

| $a, b, c$ | $a+b > c$ | $a+c > b$ | $b+c > a$ | Kết luận logic | Kết quả in |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `3 4 5` | `7 > 5` (Đúng) | `8 > 4` (Đúng) | `9 > 3` (Đúng) | Đúng cả 3 | `YES` |
| `1 2 5` | `3 > 5` (Sai) | — | — | Sai ít nhất 1 | `NO` |

---

## 6. Phân Tích Độ Phức Tạp
- Thời gian: $\mathcal{O}(1)$.
- Không gian: $\mathcal{O}(1)$.

---

## 7. Các Bẫy Lỗi Lập Trình Kinh Điển
- Dùng toán tử `||` thay vì `&&`.
- Viết điều kiện $\ge$ thay vì $>$ (trường hợp suy biến $a + b = c$ tạo thành một đoạn thẳng chứ không phải tam giác).

---

## 8. Mã Nguồn Tham Chiếu
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
ios::sync_with_stdio(false);
cin.tie(nullptr);

long long a, b, c;
if (!(cin >> a >> b >> c)) return 0;

if (a + b > c && a + c > b && b + c > a) {
cout << "YES\n";
} else {
cout << "NO\n";
}

return 0;
}
```

---

## 9. Bài Toán Mở Rộng & Chuyển Giao
- Phân loại tam giác: tam giác đều ($a=b=c$), tam giác cân ($a=b \lor b=c \lor c=a$), tam giác vuông (Định lý Pytago $a^2 + b^2 = c^2$).
