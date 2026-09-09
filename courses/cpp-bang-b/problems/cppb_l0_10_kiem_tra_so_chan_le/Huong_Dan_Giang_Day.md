# Hướng Dẫn Giảng Dạy: Kiểm Tra Số Chẵn Lẻ
Chuyên đề: **Chương 01 — Bài 02: Cấu Trúc Rẽ Nhánh & Cấu Trúc Vòng Lặp**

---

## 1. Mục Tiêu Học Tập & Chuẩn Đầu Ra
- Áp dụng toán tử chia dư `% 2` kết hợp với cấu trúc `if - else`.
- Xử lý đúng số âm: trong C++, số âm lẻ `% 2` có thể ra `-1`, nhưng điều kiện `n % 2 == 0` luôn đúng cho mọi số chẵn (dương, âm và số 0).

---

## 2. Phân Tích Đề Bài & Bản Chất Toán Học
- Số chẵn là số có dạng $2k$ ($k \in \mathbb{Z}$). Số chẵn luôn có phần dư bằng $0$ khi chia cho $2$.
- Viết điều kiện `if (n % 2 == 0)` là phương pháp an toàn nhất cho cả số âm lẫn số dương.

---

## 3. Câu Hỏi Gợi Mở Dẫn Dắt
- Số 0 là số chẵn hay số lẻ ($0 \% 2 == 0$ nên là số chẵn).
- Nếu viết `if (n % 2 == 1)` thì với số âm như `-7` điều kiện có đúng không (Không, vì `-7 % 2` bằng `-1`).

---

## 4. Chiến Lược Tối Ưu & Bất Biến Thuật Toán
- Đọc $N$ kiểu `long long`.
- Kiểm tra `n % 2 == 0`. In `CHAN` nếu đúng, ngược lại in `LE`.

---

## 5. Mô Phỏng Từng Bước Trên Sample

| $N$ | `n % 2` | So sánh với 0 | Kết quả in |
|:---:|:---:|:---:|:---:|
| `8` | `0` | `0 == 0` (Đúng) | `CHAN` |
| `-7` | `-1` | `-1 == 0` (Sai) | `LE` |

---

## 6. Phân Tích Độ Phức Tạp
- Thời gian: $\mathcal{O}(1)$.
- Không gian: $\mathcal{O}(1)$.

---

## 7. Các Bẫy Lỗi Lập Trình Kinh Điển
- Bẫy số âm khi dùng `n % 2 == 1` để kiểm tra số lẻ.
- Dùng `int` khi $N$ lên tới $10^{18}$.

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

if (n % 2 == 0) {
cout << "CHAN\n";
} else {
cout << "LE\n";
}

return 0;
}
```

---

## 9. Bài Toán Mở Rộng & Chuyển Giao
- Kiểm tra tính chia hết cho 3, 5, 10.
- Kiểm tra số có chữ số tận cùng là chữ số chẵn.
