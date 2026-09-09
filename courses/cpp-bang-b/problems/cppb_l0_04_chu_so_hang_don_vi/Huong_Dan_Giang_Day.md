# Hướng Dẫn Giảng Dạy: Chữ Số Hàng Đơn Vị & Hàng Chục
Chuyên đề: **Chương 01 — Bài 01: Biến, Kiểu Dữ Liệu, Toán Tử & Nhập Xuất An Toàn**

---

## 1. Mục Tiêu Học Tập & Chuẩn Đầu Ra
- Thành thạo toán tử chia lấy phần dư `%` và chia lấy phần nguyên `/`.
- Nắm vững kỹ thuật trích xuất các chữ số tận cùng của một số nguyên hệ thập phân.

---

## 2. Phân Tích Đề Bài & Bản Chất Toán Học
- Chữ số hàng đơn vị của $N$ luôn là $N \% 10$.
- Muốn lấy chữ số hàng chục: Ta thực hiện phép chia nguyên $N / 10$ để gọt bỏ chữ số hàng đơn vị, khi đó chữ số hàng chục cũ trở thành chữ số hàng đơn vị mới, ta chỉ cần lấy $(N / 10) \% 10$.

---

## 3. Câu Hỏi Gợi Mở Dẫn Dắt
- Muốn lấy chữ số cuối cùng của số 12345 ta làm phép toán gì
- Sau khi bỏ chữ số cuối, số còn lại là gì Làm sao để lấy tiếp chữ số đứng ngay trước nó

---

## 4. Chiến Lược Tối Ưu & Bất Biến Thuật Toán
- Đọc số $N$.
- Áp dụng công thức: `don_vi = n % 10`, `hang_chuc = (n / 10) % 10`.
- In theo đúng thứ tự: hàng chục rồi đến hàng đơn vị.

---

## 5. Mô Phỏng Từng Bước Trên Sample

| Giá trị $N$ | `n % 10` (Hàng đơn vị) | `n / 10` | `(n / 10) % 10` (Hàng chục) | Output |
|:---:|:---:|:---:|:---:|:---:|
| `357` | `7` | `35` | `5` | `5 7` |
| `80` | `0` | `8` | `8` | `8 0` |

---

## 6. Phân Tích Độ Phức Tạp
- Thời gian: $\mathcal{O}(1)$.
- Không gian: $\mathcal{O}(1)$.

---

## 7. Các Bẫy Lỗi Lập Trình Kinh Điển
- In nhầm thứ tự hàng đơn vị trước hàng chục sau.
- Nhầm lẫn giữa phép chia nguyên `/` và phép chia dư `%`.

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

int don_vi = n % 10;
int hang_chuc = (n / 10) % 10;

cout << hang_chuc << ' ' << don_vi << '\n';
return 0;
}
```

---

## 9. Bài Toán Mở Rộng & Chuyển Giao
- Trích xuất chữ số hàng trăm: `(n / 100) % 10`.
- Tách toàn bộ các chữ số của một số nguyên bằng vòng lặp `while (n > 0)`.
