# Hướng Dẫn Giảng Dạy: Tính Giai Thừa
Chuyên đề: **Chương 00: Ôn tập nền tảng C++**

---

## 1. Mục Tiêu Học Tập & Chuẩn Đầu Ra
- Mẫu tích lũy tích (nhân dồn).
- Nhận biết tràn số: $20! \approx 2.4 \times 10^{18}$, vừa khít `long long`.

---

## 2. Phân Tích Đề Bài & Bản Chất Toán Học
- $N! = \prod_{i=1}^{N} i$. Trường hợp đặc biệt: $0! = 1$.

---

## 3. Câu Hỏi Gợi Mở Dẫn Dắt
- Tại sao $0! = 1$?
- $21!$ có vượt giới hạn `long long` không?

---

## 4. Chiến Lược Tối Ưu & Bất Biến
- Khởi tạo $\text{result} = 1$, lặp nhân dồn. $\mathcal{O}(N)$.

---

## 5. Mô Phỏng Từng Bước Trên Sample

| $i$ | $\text{result}$ |
|---|---|
| 1 | 1 |
| 2 | 2 |
| 3 | 6 |
| 4 | 24 |
| 5 | 120 |

---

## 6. Phân Tích Độ Phức Tạp
- $\mathcal{O}(N)$.

---

## 7. Các Bẫy Lỗi Lập Trình Kinh Điển
- **Bẫy 1:** Khởi tạo $\text{result} = 0$ → tích luôn bằng $0$.
- **Bẫy 2:** Dùng `int` → tràn từ $13!$ trở đi.

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

    long long result = 1;
    for (int i = 1; i <= n; i++) {
        result *= i;
    }
    cout << result << '\n';
    return 0;
}
```

---

## 9. Bài Toán Mở Rộng & Chuyển Giao
- Tính giai thừa bằng đệ quy.
- $N!$ với $N > 20$ cần BigInt.
