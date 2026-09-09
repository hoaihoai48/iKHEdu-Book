# Hướng Dẫn Giảng Dạy: Điểm Trung Bình Ba Môn
Chuyên đề: **Chương 01 — Bài 01: Biến, Kiểu Dữ Liệu, Toán Tử & Nhập Xuất An Toàn**

---

## 1. Mục Tiêu Học Tập & Chuẩn Đầu Ra
- Làm quen với kiểu dữ liệu số thực `double`.
- Nắm vững cú pháp định dạng số thập phân: `cout << fixed << setprecision(k)`.
- Nhận biết bẫy phép chia nguyên giữa hai số nguyên (`sum / 3`).

---

## 2. Phân Tích Đề Bài & Bản Chất Toán Học
- Công thức trung bình: $\text{avg} = \frac{a + b + c}{3}$.
- Phép chia trong C++: Nếu tử số và mẫu số đều là số nguyên, máy tính sẽ thực hiện phép chia lấy phần nguyên (bỏ qua toàn bộ phần thập phân). Do đó, cần ép kiểu số thực bằng cách nhân `1.0` hoặc chia cho `3.0`.

---

## 3. Câu Hỏi Gợi Mở Dẫn Dắt
- Nếu $a = 7, b = 8, c = 8$, tổng là 23. Trong C++, kết quả của `23 / 3` bằng bao nhiêu (Bằng 7 chứ không phải 7.666...).
- Làm thế nào để máy tính hiểu ta muốn lấy kết quả dưới dạng số thực

---

## 4. Chiến Lược Tối Ưu & Bất Biến Thuật Toán
- Đọc 3 số, tính `avg = (a + b + c) / 3.0`.
- Sử dụng cặp cờ `fixed` và `setprecision(2)` trong thư viện chuẩn để in ra đúng 2 chữ số sau dấu chấm.

---

## 5. Mô Phỏng Từng Bước Trên Sample

| Dữ liệu $a, b, c$ | Tổng $a+b+c$ | Phép chia thực | Định dạng `setprecision(2)` |
|:---:|:---:|:---:|:---:|
| `8 7 9` | `24` | `24 / 3.0 = 8.0` | `8.00` |
| `7 8 8` | `23` | `23 / 3.0 = 7.6666...` | `7.67` |

---

## 6. Phân Tích Độ Phức Tạp
- Thời gian: $\mathcal{O}(1)$.
- Không gian: $\mathcal{O}(1)$.

---

## 7. Các Bẫy Lỗi Lập Trình Kinh Điển
- Viết `int sum = a + b + c; double avg = sum / 3;` (sai vì `sum / 3` đã bị mất phần thập phân trước khi gán cho `avg`).
- Quên thêm `fixed`, chỉ dùng `setprecision(2)` sẽ khiến máy in 2 chữ số có nghĩa thay vì 2 chữ số sau dấu phẩy.

---

## 8. Mã Nguồn Tham Chiếu
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
ios::sync_with_stdio(false);
cin.tie(nullptr);

double a, b, c;
if (!(cin >> a >> b >> c)) return 0;

double avg = (a + b + c) / 3.0;

cout << fixed << setprecision(2) << avg << '\n';
return 0;
}
```

---

## 9. Bài Toán Mở Rộng & Chuyển Giao
- Tính điểm trung bình có hệ số (Toán nhân 2, Văn nhân 2, Ngoại ngữ nhân 1).
- Tính điểm trung bình của một mảng gồm $N$ môn học.
