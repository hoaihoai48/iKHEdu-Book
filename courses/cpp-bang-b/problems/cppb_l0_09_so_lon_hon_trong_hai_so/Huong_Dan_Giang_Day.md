# Hướng Dẫn Giảng Dạy: Tìm Số Lớn Hơn Trong Hai Số
Chuyên đề: **Chương 01 — Bài 02: Cấu Trúc Rẽ Nhánh & Cấu Trúc Vòng Lặp**

---

## 1. Mục Tiêu Học Tập & Chuẩn Đầu Ra
- Làm quen với cấu trúc rẽ nhánh cơ bản `if`, `else if`, `else`.
- Hiểu và sử dụng các toán tử so sánh `>`, `<`, `==`.
- Rèn luyện kỹ năng xử lý trường hợp đặc biệt (hai số bằng nhau).

---

## 2. Phân Tích Đề Bài & Bản Chất Toán Học
- Có 3 trường hợp độc lập loại trừ nhau (trichotomy property): $a > b$, $a < b$, hoặc $a = b$.
- Cấu trúc `if - else if - else` đảm bảo chỉ có đúng một nhánh được thực thi.

---

## 3. Câu Hỏi Gợi Mở Dẫn Dắt
- Khi so sánh hai số bất kỳ, có bao nhiêu trường hợp có thể xảy ra
- Trong C++, toán tử so sánh bằng được viết như thế nào (Chú ý `==` chứ không phải `=`).

---

## 4. Chiến Lược Tối Ưu & Bất Biến Thuật Toán
- Đọc $a, b$. Dùng cấu trúc rẽ nhánh 3 trường hợp để in kết quả tương ứng.

---

## 5. Mô Phỏng Từng Bước Trên Sample

| $a$ | $b$ | Điều kiện thỏa mãn | In ra màn hình |
|:---:|:---:|:---:|:---:|
| `7` | `12` | `b > a` (12 > 7) | `12` |
| `9` | `9` | `a == b` (9 == 9) | `BANG NHAU` |

---

## 6. Phân Tích Độ Phức Tạp
- Thời gian: $\mathcal{O}(1)$.
- Không gian: $\mathcal{O}(1)$.

---

## 7. Các Bẫy Lỗi Lập Trình Kinh Điển
- Viết nhầm `if (a = b)` thay vì `if (a == b)`.
- Thiếu dấu ngoặc nhọn hoặc in sai chính tả chuỗi `BANG NHAU`.

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

if (a > b) {
cout << a << '\n';
} else if (b > a) {
cout << b << '\n';
} else {
cout << "BANG NHAU\n";
}

return 0;
}
```

---

## 9. Bài Toán Mở Rộng & Chuyển Giao
- Tìm số lớn nhất trong ba số $a, b, c$.
