# Hướng Dẫn Giảng Dạy: Tính Tổng Hai Số
Chuyên đề: **Chương 00: Ôn tập nền tảng C++**

---

## 1. Mục Tiêu Học Tập & Chuẩn Đầu Ra
- Khai báo biến kiểu `long long` để tránh tràn số.
- Sử dụng `cin` đọc dữ liệu, `cout` in kết quả.
- Nhận biết khi nào cần dùng `long long` thay vì `int`.

---

## 2. Phân Tích Đề Bài & Bản Chất Toán Học
- **Bản chất:** Tính tổng hai số nguyên.
- **Edge case:** $a$ và $b$ có thể âm, tổng có thể vượt giới hạn `int` ($2 \times 10^9 > 2^{31} - 1$).
- **Giới hạn:** $|a|, |b| \le 10^9$ nên tổng có thể đạt $2 \times 10^9$, cần `long long`.

---

## 3. Câu Hỏi Gợi Mở Dẫn Dắt
- Khi $a = 10^9$ và $b = 10^9$, tổng bằng bao nhiêu? Kiểu `int` chứa được không?
- Nếu cả hai số đều âm thì sao?

---

## 4. Chiến Lược Tối Ưu & Bất Biến
- Đọc hai số → cộng → in. Độ phức tạp $\mathcal{O}(1)$.
- Bất biến: dùng `long long` để kết quả luôn chính xác.

---

## 5. Mô Phỏng Từng Bước Trên Sample

| Bước | Thao tác | Giá trị biến | Kết quả |
|---|---|---|---|
| 1 | Đọc $a, b$ | $a = 3, b = 5$ | — |
| 2 | Tính $a + b$ | $3 + 5 = 8$ | In ra $8$ |

---

## 6. Phân Tích Độ Phức Tạp
- Thời gian: $\mathcal{O}(1)$.
- Không gian: $\mathcal{O}(1)$.

---

## 7. Các Bẫy Lỗi Lập Trình Kinh Điển
- **Bẫy 1 — Tràn int:** $10^9 + 10^9 = 2 \times 10^9 > 2^{31}-1$. Phải dùng `long long`.
- **Bẫy 2 — Quên Fast I/O:** Luôn dùng `ios::sync_with_stdio(false); cin.tie(nullptr);`.

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

    cout << a + b << '\n';
    return 0;
}
```

---

## 9. Bài Toán Mở Rộng & Chuyển Giao
- Tính tổng 3 số, tính hiệu, tính trung bình.
- Tính tổng $N$ số (dẫn sang vòng lặp và mảng).
