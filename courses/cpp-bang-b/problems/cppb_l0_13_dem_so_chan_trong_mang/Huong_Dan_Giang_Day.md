# Hướng Dẫn Giảng Dạy: Đếm Số Chẵn Trong Mảng
Chuyên đề: **Chương 00: Ôn tập nền tảng C++**

---

## 1. Mục Tiêu Học Tập & Chuẩn Đầu Ra
- Kết hợp vòng lặp, điều kiện, và mẫu tích lũy đếm.

---

## 2. Phân Tích Đề Bài & Bản Chất Toán Học
- Số chẵn: $x \% 2 = 0$.

---

## 3. Câu Hỏi Gợi Mở Dẫn Dắt
- Làm sao kiểm tra một số chẵn hay lẻ?
- Biến đếm nên khởi tạo bao nhiêu?

---

## 4. Chiến Lược Tối Ưu & Bất Biến
- Duyệt, kiểm tra `x % 2 == 0`, tăng đếm. $\mathcal{O}(N)$.

---

## 5. Mô Phỏng Từng Bước Trên Sample

| $i$ | $a_i$ | $a_i \% 2$ | count |
|---|---|---|---|
| 0 | 1 | 1 | 0 |
| 1 | 2 | 0 ✓ | 1 |
| 2 | 3 | 1 | 1 |
| 3 | 4 | 0 ✓ | 2 |
| 4 | 5 | 1 | 2 |
| 5 | 6 | 0 ✓ | 3 |

---

## 6. Phân Tích Độ Phức Tạp
- $\mathcal{O}(N)$.

---

## 7. Các Bẫy Lỗi Lập Trình Kinh Điển
- **Bẫy 1:** Dùng `x % 2 == 1` cho số lẻ → với số âm sẽ sai.
- **Bẫy 2:** Quên khởi tạo `count = 0`.

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

    int count = 0;
    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        if (x % 2 == 0) count++;
    }
    cout << count << '\n';
    return 0;
}
```

---

## 9. Bài Toán Mở Rộng & Chuyển Giao
- Đếm số lẻ, đếm số chia hết cho $k$.
- Tính tổng các số chẵn.
