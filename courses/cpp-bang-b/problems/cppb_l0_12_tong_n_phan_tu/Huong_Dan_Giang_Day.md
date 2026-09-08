# Hướng Dẫn Giảng Dạy: Tổng N Phần Tử
Chuyên đề: **Chương 00: Ôn tập nền tảng C++**

---

## 1. Mục Tiêu Học Tập & Chuẩn Đầu Ra
- Đọc mảng $N$ phần tử.
- Tính tổng bằng vòng lặp.

---

## 2. Phân Tích Đề Bài & Bản Chất Toán Học
- $\text{sum} = \sum a_i$. Tổng có thể đến $10^{14}$ → cần `long long`.

---

## 3. Câu Hỏi Gợi Mở Dẫn Dắt
- Biến `sum` nên khởi tạo bao nhiêu?
- Kiểu `int` có đủ cho tổng không?

---

## 4. Chiến Lược Tối Ưu & Bất Biến
- Duyệt 1 lần, cộng dồn. $\mathcal{O}(N)$.

---

## 5. Mô Phỏng Từng Bước Trên Sample

| $i$ | $a_i$ | $\text{sum}$ |
|---|---|---|
| 0 | 1 | 1 |
| 1 | 2 | 3 |
| 2 | 3 | 6 |
| 3 | 4 | 10 |
| 4 | 5 | 15 |

---

## 6. Phân Tích Độ Phức Tạp
- $\mathcal{O}(N)$.

---

## 7. Các Bẫy Lỗi Lập Trình Kinh Điển
- **Bẫy 1 — Tràn int:** $10^5 \times 10^9 = 10^{14}$ vượt `int`.
- **Bẫy 2:** Quên khởi tạo `sum = 0`.

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

    long long sum = 0;
    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        sum += x;
    }
    cout << sum << '\n';
    return 0;
}
```

---

## 9. Bài Toán Mở Rộng & Chuyển Giao
- Tính trung bình $N$ phần tử.
- Tính tổng có điều kiện (chỉ cộng số dương).
