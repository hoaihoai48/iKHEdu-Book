# Hướng Dẫn Giảng Dạy: Số Lớn Hơn Trong Hai Số
Chuyên đề: **Chương 00: Ôn tập nền tảng C++**

---

## 1. Mục Tiêu Học Tập & Chuẩn Đầu Ra
- Sử dụng câu lệnh `if/else` hoặc hàm `max()`.

---

## 2. Phân Tích Đề Bài & Bản Chất Toán Học
- Trả về $\max(a, b)$. C++ có sẵn hàm `max(a, b)`.

---

## 3. Câu Hỏi Gợi Mở Dẫn Dắt
- Viết bằng `if/else` thì cần bao nhiêu nhánh?
- Có cách nào ngắn hơn không?

---

## 4. Chiến Lược Tối Ưu & Bất Biến
- Dùng `max(a, b)`. $\mathcal{O}(1)$.

---

## 5. Mô Phỏng Từng Bước Trên Sample

| Bước | Thao tác | Giá trị | Kết quả |
|---|---|---|---|
| 1 | Đọc $a, b$ | $3, 7$ | — |
| 2 | $\max(3, 7) = 7$ | $7$ | In $7$ |

---

## 6. Phân Tích Độ Phức Tạp
- $\mathcal{O}(1)$.

---

## 7. Các Bẫy Lỗi Lập Trình Kinh Điển
- **Bẫy 1:** Nếu viết `if/else`, quên xử lý trường hợp $a = b$.
- **Bẫy 2:** Nhầm `=` (gán) với `==` (so sánh) trong điều kiện `if`.

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

    cout << max(a, b) << '\n';
    return 0;
}
```

---

## 9. Bài Toán Mở Rộng & Chuyển Giao
- Tìm max trong 3 số, 4 số.
- Tìm max trong mảng $N$ phần tử.
