# Hướng Dẫn Giảng Dạy: Xếp Loại Học Lực
Chuyên đề: **Chương 00: Ôn tập nền tảng C++**

---

## 1. Mục Tiêu Học Tập & Chuẩn Đầu Ra
- Sử dụng `if / else if / else` nhiều nhánh.
- Đọc số thực bằng `cin`.

---

## 2. Phân Tích Đề Bài & Bản Chất Toán Học
- 4 khoảng giá trị: $[8, 10]$, $[6.5, 8)$, $[5, 6.5)$, $[0, 5)$.

---

## 3. Câu Hỏi Gợi Mở Dẫn Dắt
- Nếu $D = 8.0$, xếp loại gì? (`>=` hay `>` quan trọng!)
- Thứ tự kiểm tra `if/else if` có ảnh hưởng không?

---

## 4. Chiến Lược Tối Ưu & Bất Biến
- Kiểm tra từ ngưỡng cao → thấp. $\mathcal{O}(1)$.

---

## 5. Mô Phỏng Từng Bước Trên Sample

| Bước | Thao tác | Điều kiện | Kết quả |
|---|---|---|---|
| 1 | Đọc $D = 8.5$ | — | — |
| 2 | $8.5 \ge 8.0$? | Đúng | In "Gioi" |

---

## 6. Phân Tích Độ Phức Tạp
- $\mathcal{O}(1)$.

---

## 7. Các Bẫy Lỗi Lập Trình Kinh Điển
- **Bẫy 1:** Nhầm `>=` với `>` ở ngưỡng (ví dụ $D = 8.0$ phải là "Gioi").
- **Bẫy 2:** Kiểm tra sai thứ tự (nếu kiểm tra $\ge 5.0$ trước $\ge 8.0$).

---

## 8. Mã Nguồn Tham Chiếu
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    double d;
    if (!(cin >> d)) return 0;

    if (d >= 8.0) cout << "Gioi" << '\n';
    else if (d >= 6.5) cout << "Kha" << '\n';
    else if (d >= 5.0) cout << "Trung binh" << '\n';
    else cout << "Yeu" << '\n';
    return 0;
}
```

---

## 9. Bài Toán Mở Rộng & Chuyển Giao
- Thêm loại "Xuất sắc" cho $D \ge 9.0$.
- Xếp loại cho cả lớp (dùng vòng lặp).
