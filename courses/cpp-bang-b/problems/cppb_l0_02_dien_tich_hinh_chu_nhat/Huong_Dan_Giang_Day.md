# Hướng Dẫn Giảng Dạy: Diện Tích & Chu Vi Hình Chữ Nhật
Chuyên đề: **Chương 01 — Bài 01: Biến, Kiểu Dữ Liệu, Toán Tử & Nhập Xuất An Toàn**

---

## 1. Mục Tiêu Học Tập & Chuẩn Đầu Ra
- Nắm vững công thức chu vi và diện tích hình học cơ bản.
- Hiểu rõ hiện tượng tràn số khi thực hiện phép nhân hai số lớn.
- Bắt buộc dùng `long long` cho biến diện tích vì $a \times b$ có thể lên tới $10^{18}$.

---

## 2. Phân Tích Đề Bài & Bản Chất Toán Học
- Chu vi $P = 2 \times (a + b)$. Khi $a, b \le 10^9$, $P \le 4 \times 10^9$ (vượt quá kiểu `int` có dấu).
- Diện tích $S = a \times b$. Khi $a, b = 10^9$, $S = 10^{18}$, bắt buộc phải dùng kiểu số nguyên 64-bit `long long` (chứa được tới xấp xỉ $9 \times 10^{18}$).

---

## 3. Câu Hỏi Gợi Mở Dẫn Dắt
- Nếu khai báo `int a, b; long long s = a * b;` thì kết quả có bị sai không (Gợi ý: Phép nhân $a \times b$ xảy ra trên miền `int` trước rồi mới gán sang `s`).
- Làm thế nào để đảm bảo an toàn tuyệt đối ngay từ khâu khai báo

---

## 4. Chiến Lược Tối Ưu & Bất Biến Thuật Toán
- Khai báo cả $a$ và $b$ dưới kiểu `long long`.
- Tính $P = 2 \times (a + b)$ và $S = a \times b$. In ra theo định dạng yêu cầu.

---

## 5. Mô Phỏng Từng Bước Trên Sample

| Biến $a$ | Biến $b$ | Chu vi $2 \times (a + b)$ | Diện tích $a \times b$ | Output |
|:---:|:---:|:---:|:---:|:---:|
| `4` | `7` | `2 * (4 + 7) = 22` | `4 * 7 = 28` | `22 28` |

---

## 6. Phân Tích Độ Phức Tạp
- Thời gian: $\mathcal{O}(1)$.
- Không gian: $\mathcal{O}(1)$.

---

## 7. Các Bẫy Lỗi Lập Trình Kinh Điển
- Khai báo $a, b$ là `int`. Khi $a = 10^6, b = 10^6$, diện tích $a \times b = 10^{12}$ sẽ bị tràn số sinh ra số âm ngẫu nhiên.
- In ngược thứ tự: in diện tích trước chu vi sau.

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

long long perimeter = 2 * (a + b);
long long area = a * b;

cout << perimeter << ' ' << area << '\n';
return 0;
}
```

---

## 9. Bài Toán Mở Rộng & Chuyển Giao
- Tính diện tích tam giác với công thức Heron hoặc đường cao.
- Mở rộng tính chu vi diện tích hình tròn có số thực $\pi$.
