# Hướng Dẫn Giảng Dạy: Tổng Chữ Số Của Số Có Ba Chữ Số
Chuyên đề: **Chương 01 — Bài 01: Biến, Kiểu Dữ Liệu, Toán Tử & Nhập Xuất An Toàn**

---

## 1. Mục Tiêu Học Tập & Chuẩn Đầu Ra
- Áp dụng thành thạo phép chia lấy phần nguyên `/` và chia lấy phần dư `%` để tách rời các chữ số hàng trăm, hàng chục, hàng đơn vị.
- Rèn luyện kỹ năng kết hợp các biểu thức toán học trong cùng một chương trình.

---

## 2. Phân Tích Đề Bài & Bản Chất Toán Học
- Với số có 3 chữ số $N = \overline{abc}$:
- Chữ số hàng trăm $a = N / 100$.
- Chữ số hàng chục $b = (N / 10) \% 10$.
- Chữ số hàng đơn vị $c = N \% 10$.
- Tổng các chữ số cần tìm là $S = a + b + c$.

---

## 3. Câu Hỏi Gợi Mở Dẫn Dắt
- Số 357 chia cho 100 được phần nguyên bằng bao nhiêu
- Làm sao để lấy được chữ số ở giữa (hàng chục)

---

## 4. Chiến Lược Tối Ưu & Bất Biến Thuật Toán
- Đọc số nguyên $N$.
- Tách từng biến `tram`, `chuc`, `don_vi` theo công thức toán học.
- In ra tổng `tram + chuc + don_vi`. Độ phức tạp $\mathcal{O}(1)$.

---

## 5. Mô Phỏng Từng Bước Trên Sample

| Số $N$ | Hàng trăm `n / 100` | Hàng chục `(n / 10) % 10` | Hàng đơn vị `n % 10` | Tổng chữ số |
|:---:|:---:|:---:|:---:|:---:|
| `357` | `3` | `5` | `7` | `3 + 5 + 7 = 15` |
| `505` | `5` | `0` | `5` | `5 + 0 + 5 = 10` |

---

## 6. Phân Tích Độ Phức Tạp
- Thời gian: $\mathcal{O}(1)$.
- Không gian: $\mathcal{O}(1)$.

---

## 7. Các Bẫy Lỗi Lập Trình Kinh Điển
- Nhầm công thức hàng chục thành `n % 100` (kết quả là số có 2 chữ số chứ không phải 1 chữ số).
- Quên rằng đề bài cố định $100 \le N \le 999$ nên có thể giải trực tiếp bằng công thức mà chưa cần vòng lặp.

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

int tram = n / 100;
int chuc = (n / 10) % 10;
int don_vi = n % 10;

cout << tram + chuc + don_vi << '\n';
return 0;
}
```

---

## 9. Bài Toán Mở Rộng & Chuyển Giao
- Mở rộng tính tổng chữ số của số có 4 chữ số hoặc số có độ dài bất kỳ bằng vòng lặp (sẽ học ở Bài 02).
