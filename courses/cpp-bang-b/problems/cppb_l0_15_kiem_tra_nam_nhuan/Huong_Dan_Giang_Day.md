# Hướng Dẫn Giảng Dạy: Kiểm Tra Năm Nhuận & Số Ngày Trong Tháng
Chuyên đề: **Chương 01 — Bài 02: Cấu Trúc Rẽ Nhánh & Cấu Trúc Vòng Lặp**

---

## 1. Mục Tiêu Học Tập & Chuẩn Đầu Ra
- Phối hợp thành thạo các toán tử logic `||` (HOẶC) và `&&` (VÀ) với thứ tự ưu tiên dấu ngoặc.
- Rèn luyện kỹ năng lưu biểu thức điều kiện phức tạp vào một biến kiểu `bool` giúp mã nguồn sáng rõ.

---

## 2. Phân Tích Đề Bài & Bản Chất Toán Học
- Biểu thức logic chuẩn xác cho năm nhuận:
$$\text{is\_leap} = (Y \% 400 == 0) \lor (Y \% 4 == 0 \land Y \% 100 \ne 0)$$

- Năm 1900, 2100 chia hết cho 4 nhưng chia hết cho 100 và không chia hết cho 400 nên KHÔNG phải năm nhuận.
- Năm 2000, 2400 chia hết cho 400 nên LÀ năm nhuận.

---

## 3. Câu Hỏi Gợi Mở Dẫn Dắt
- Năm 1900 chia hết cho 4, vậy nó có phải năm nhuận không Tại sao
- Để gom nhóm điều kiện "chia hết cho 4 và không chia hết cho 100", ta dùng cặp ngoặc tròn như thế nào

---

## 4. Chiến Lược Tối Ưu & Bất Biến Thuật Toán
- Đọc $Y$.
- Tính biến cờ `bool is_leap = (y % 400 == 0) || (y % 4 == 0 && y % 100 != 0);`.
- Rẽ nhánh in kết quả tương ứng.

---

## 5. Mô Phỏng Từng Bước Trên Sample

| Năm $Y$ | `y % 400 == 0` | `y % 4 == 0` | `y % 100 != 0` | Biến `is_leap` | Output |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `2024` | Sai | Đúng | Đúng | Đúng | `NHUAN 29` |
| `1900` | Sai | Đúng | Sai (vì 1900 % 100 == 0) | Sai | `KHONG NHUAN 28` |
| `2000` | Đúng | Đúng | Sai | Đúng | `NHUAN 29` |

---

## 6. Phân Tích Độ Phức Tạp
- Thời gian: $\mathcal{O}(1)$.
- Không gian: $\mathcal{O}(1)$.

---

## 7. Các Bẫy Lỗi Lập Trình Kinh Điển
- Viết điều kiện đơn giản `y % 4 == 0` (bị sai ở các năm tròn thế kỷ như 1900, 2100).
- Thiếu dấu ngoặc phân tách giữa `||` và `&&`.

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

bool is_leap = (y % 400 == 0) || (y % 4 == 0 && y % 100 != 0);

if (is_leap) {
cout << "NHUAN 29\n";
} else {
cout << "KHONG NHUAN 28\n";
}

return 0;
}
```

---

## 9. Bài Toán Mở Rộng & Chuyển Giao
- Nhập tháng $M$ và năm $Y$, in ra chính xác số ngày của tháng $M$ trong năm $Y$.
