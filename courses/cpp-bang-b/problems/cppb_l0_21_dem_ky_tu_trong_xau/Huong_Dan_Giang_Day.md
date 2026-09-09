# Hướng Dẫn Giảng Dạy: Đếm Số Lần Xuất Hiện Của Ký Tự Trong Xâu
Chuyên đề: **Chương 01 — Bài 03: Mảng 1 Chiều, Vector, Xâu Ký Tự & Tổ Chức Hàm**

---

## 1. Mục Tiêu Học Tập & Chuẩn Đầu Ra
- Làm quen với kiểu dữ liệu xâu ký tự `string` trong C++.
- Sử dụng cú pháp vòng lặp duyệt từng ký tự `for (char x : s)`.
- Phân biệt kiểu dữ liệu ký tự đơn `char` (dấu nháy đơn `'a'`) và xâu ký tự `string` (dấu nháy kép `"banana"`).

---

## 2. Phân Tích Đề Bài & Bản Chất Toán Học
- Duyệt qua từng ký tự của xâu từ trái sang phải, so sánh `x == c`. Nếu bằng nhau thì tăng biến đếm.

---

## 3. Câu Hỏi Gợi Mở Dẫn Dắt
- Trong C++, chuỗi ký tự được lưu bằng kiểu dữ liệu nào
- Ký tự `C` được biểu diễn bằng dấu nháy đơn hay nháy kép

---

## 4. Chiến Lược Tối Ưu & Bất Biến Thuật Toán
- Đọc xâu `s` và ký tự `c`.
- Dùng vòng lặp duyệt qua xâu trong thời gian $\mathcal{O}(|S|)$.

---

## 5. Mô Phỏng Từng Bước Trên Sample (`banana`, `a`)

| Ký tự $x$ | `b` | `a` | `n` | `a` | `n` | `a` |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `x == 'a'` | Sai | Đúng | Sai | Đúng | Sai | Đúng |
| `count_c` | 0 | 1 | 1 | 2 | 2 | 3 |

---

## 6. Phân Tích Độ Phức Tạp
- Thời gian: $\mathcal{O}(|S|)$.
- Không gian: $\mathcal{O}(1)$ phụ trội.

---

## 7. Các Bẫy Lỗi Lập Trình Kinh Điển
- Nhầm dấu nháy đơn `'c'` và nháy kép `"c"`.
- Không phân biệt chữ hoa và chữ thường (`'A'` khác `'a'`).

---

## 8. Mã Nguồn Tham Chiếu
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
ios::sync_with_stdio(false);
cin.tie(nullptr);

string s;
char c;
if (!(cin >> s >> c)) return 0;

int count_c = 0;
for (char x : s) {
if (x == c) {
count_c++;
}
}

cout << count_c << '\n';
return 0;
}
```

---

## 9. Bài Toán Mở Rộng & Chuyển Giao
- Đếm số lượng chữ số, chữ cái hoa, chữ cái thường trong một xâu.
