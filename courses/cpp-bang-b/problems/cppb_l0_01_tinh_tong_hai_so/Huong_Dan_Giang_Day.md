# Hướng Dẫn Giảng Dạy: Tính Tổng Hai Số
Chuyên đề: **Chương 01 — Bài 01: Biến, Kiểu Dữ Liệu, Toán Tử & Nhập Xuất An Toàn**

---

## 1. Mục Tiêu Học Tập & Chuẩn Đầu Ra
- Khai báo và sử dụng biến số nguyên.
- Biết cách đọc dữ liệu bằng `cin` và xuất dữ liệu bằng `cout`.
- Rèn luyện phản xạ sử dụng `long long` khi tổng hai số có thể vượt quá $2 \times 10^9$.

---

## 2. Phân Tích Đề Bài & Bản Chất Toán Học
- **Bản chất:** Tính tổng số học cơ bản $S = a + b$.
- **Edge cases:** Các số có thể mang dấu âm (ví dụ: $-10^9 + (-10^9) = -2 \times 10^9$). Nếu dùng `int` 32-bit có dấu, giá trị lớn nhất là $2^{31} - 1 \approx 2.14 \times 10^9$, khi cộng hai số lớn dễ tiệm cận ngưỡng tràn số (Overflow).

---

## 3. Câu Hỏi Gợi Mở Dẫn Dắt
- Trong C++, khi cần lưu số nguyên có giá trị lên tới hàng tỷ, kiểu dữ liệu `int` có an toàn không
- Lệnh nào giúp đọc lần lượt hai số cách nhau bởi dấu cách từ bàn phím

---

## 4. Chiến Lược Tối Ưu & Bất Biến Thuật Toán
- Đọc trực tiếp $a, b$, tính tổng và xuất ra màn hình.
- **Bất biến:** Mọi phép toán cộng đều thực hiện trên miền giá trị `long long`. Độ phức tạp thời gian $\mathcal{O}(1)$, bộ nhớ $\mathcal{O}(1)$.

---

## 5. Mô Phỏng Từng Bước Trên Sample

| Bước | Biến $a$ | Biến $b$ | Biểu thức $a + b$ | Kết quả in |
|:---:|:---:|:---:|:---:|:---:|
| 1 | `3` | `5` | `3 + 5 = 8` | `8` |

---

## 6. Phân Tích Độ Phức Tạp
- Thời gian: $\mathcal{O}(1)$ (chỉ gồm 1 phép đọc, 1 phép cộng, 1 phép in).
- Không gian bộ nhớ: $\mathcal{O}(1)$ (chỉ sử dụng 2 ô nhớ kiểu `long long`).

---

## 7. Các Bẫy Lỗi Lập Trình Kinh Điển
- **Bẫy 1:** Dùng `int` thay vì `long long` khi test đạt cực đại $a = 10^9, b = 10^9$.
- **Bẫy 2:** Quên ngắt dòng `\n` hoặc viết nhầm toán tử `>>` của `cin` thành `<<`.

---

## 8. Mã Nguồn Tham Chiếu
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
ios::sync_with_stdio(false);
cin.tie(nullptr);

long long a, b;
if (!(cin >> a >> b)) return 0;

cout << a + b << '\n';
return 0;
}
```

---

## 9. Bài Toán Mở Rộng & Chuyển Giao
- Tính hiệu $a - b$ và tích $a \times b$ (lưu ý tích hai số $10^9$ chắc chắn tràn `long long` nếu không kiểm soát).
- Mở rộng tính tổng của một dãy nhiều số nguyên.
