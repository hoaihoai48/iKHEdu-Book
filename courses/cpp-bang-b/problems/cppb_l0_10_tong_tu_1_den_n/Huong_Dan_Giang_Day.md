# Hướng Dẫn Giảng Dạy: Tổng Từ 1 Đến N
Chuyên đề: **Chương 00: Ôn tập nền tảng C++**

---

## 1. Mục Tiêu Học Tập & Chuẩn Đầu Ra
- Vòng lặp `for` cơ bản.
- Mẫu tích lũy tổng.

---

## 2. Phân Tích Đề Bài & Bản Chất Toán Học
- Vòng lặp: $\text{sum} = \sum_{i=1}^{N} i$.
- Công thức Gauss: $N(N+1)/2$ (nhưng mục đích bài là luyện vòng lặp).

---

## 3. Câu Hỏi Gợi Mở Dẫn Dắt
- Viết vòng lặp `for` từ 1 đến N ra sao?
- Khi $N = 10^6$, tổng có vượt `int` không?

---

## 4. Chiến Lược Tối Ưu & Bất Biến
- $\text{sum} = 0$, lặp $i = 1 \to N$, cộng dồn. $\mathcal{O}(N)$.

---

## 5. Mô Phỏng Từng Bước Trên Sample

| $i$ | $\text{sum}$ trước | $\text{sum}$ sau |
|---|---|---|
| 1 | 0 | 1 |
| 2 | 1 | 3 |
| 3 | 3 | 6 |
| 4 | 6 | 10 |
| 5 | 10 | 15 |

---

## 6. Phân Tích Độ Phức Tạp
- $\mathcal{O}(N)$.

---

## 7. Các Bẫy Lỗi Lập Trình Kinh Điển
- **Bẫy 1 — Tràn int:** $N = 10^6$ thì tổng $= 5 \times 10^{11}$, vượt `int`. Phải `long long`.
- **Bẫy 2:** Vòng lặp `i < n` thay vì `i <= n` → thiếu phần tử cuối.

---

## 8. Mã Nguồn Tham Chiếu
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;

    long long sum = 0;
    for (long long i = 1; i <= n; i++) {
        sum += i;
    }
    cout << sum << '\n';
    return 0;
}
```

---

## 9. Bài Toán Mở Rộng & Chuyển Giao
- Tính tổng bằng công thức $N(N+1)/2$.
- Tính tổng số chẵn / số lẻ.
