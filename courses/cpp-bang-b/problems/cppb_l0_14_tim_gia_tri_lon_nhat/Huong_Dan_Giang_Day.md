# Hướng Dẫn Giảng Dạy: Tìm Giá Trị Lớn Nhất
Chuyên đề: **Chương 00: Ôn tập nền tảng C++**

---

## 1. Mục Tiêu Học Tập & Chuẩn Đầu Ra
- Mẫu tích lũy tìm max.

---

## 2. Phân Tích Đề Bài & Bản Chất Toán Học
- Duyệt mảng, so sánh với max hiện tại bằng `max()`.

---

## 3. Câu Hỏi Gợi Mở Dẫn Dắt
- Khởi tạo `mx` bằng gì? ($a[0]$ hay $-\infty$?)
- Nếu dãy toàn số âm thì sao?

---

## 4. Chiến Lược Tối Ưu & Bất Biến
- Bất biến: sau bước $i$, `mx` chứa max của $a[0..i]$. $\mathcal{O}(N)$.

---

## 5. Mô Phỏng Từng Bước Trên Sample

| $i$ | $a_i$ | $mx$ |
|---|---|---|
| 0 | 3 | 3 |
| 1 | 1 | 3 |
| 2 | 4 | 4 |
| 3 | 1 | 4 |
| 4 | 5 | 5 |

---

## 6. Phân Tích Độ Phức Tạp
- $\mathcal{O}(N)$.

---

## 7. Các Bẫy Lỗi Lập Trình Kinh Điển
- **Bẫy 1:** Khởi tạo `mx = 0` → sai nếu dãy toàn số âm.
- **Bẫy 2:** Dùng `if (x > mx)` thay vì `max()` cũng đúng nhưng dài hơn.

---

## 8. Mã Nguồn Tham Chiếu
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    int mx;
    cin >> mx;
    for (int i = 1; i < n; i++) {
        int x;
        cin >> x;
        mx = max(mx, x);
    }
    cout << mx << '\n';
    return 0;
}
```

---

## 9. Bài Toán Mở Rộng & Chuyển Giao
- Tìm max lẫn min cùng lúc.
- Tìm max lần 2 (second maximum).
