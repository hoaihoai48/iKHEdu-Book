# Hướng Dẫn Giảng Dạy: Ước chung lớn nhất & BCNN
Chuyên đề: **Ước Số, Bội Số & Số Nguyên Tố Cơ Bản**

---

## 1. Ý tưởng & Phân tích thuật toán
- Bản chất của bài này: với hai số `a = 12` và `b = 18`, tìm ước chung lớn nhất rồi suy ra bội chung nhỏ nhất theo công thức `lcm = a // gcd * b`.
- Lời giải dùng vòng lặp chia lấy dư với hai biến `x`, `y`: khởi đầu `x = 12`, `y = 18`, mỗi bước gán `x, y = y, x % y` cho tới khi `y == 0`, khi đó `x` chính là ước chung lớn nhất.
- Với `12` và `18`: `12 // 6 * 18 = 2 * 18 = 36`, nên in ra `6 36`.
- Thầy cô nhấn mạnh thứ tự in: ước chung lớn nhất in trước, bội chung nhỏ nhất in sau, cách nhau một khoảng trắng.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 12 18)
| Bước | `x` | `y` | `x % y` | Ghi chú |
| --- | --- | --- | --- | --- |
| Khởi đầu | 12 | 18 | — | `x = a = 12`, `y = b = 18` |
| 1 | 18 | 12 | 12 | `18 % 12 = 6`, gán tiếp |
| 2 | 12 | 6 | 0 | `12 % 6 = 0`, gán tiếp |
| 3 | 6 | 0 | — | `y == 0` nên dừng, `gcd = 6` |
| Tính | — | — | — | `lcm = 12 // 6 * 18 = 36` |

Kết quả in ra: `6 36`, khớp với kết quả mẫu.

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- Bẫy 1: tính bội chung nhỏ nhất bằng `a * b // gcd` khi `a`, `b` tới `10^9`. Với `12` và `18` vẫn đúng (`216 // 6 = 36`), nhưng với số lớn tích `a * b` phình to không cần thiết. Cách viết đúng như bài giải: `a // gcd * b` (chia trước, nhân sau).
- Bẫy 2: dùng hàm `round` hoặc phép chia `/` rồi ép kiểu để tìm ước chung. Sai mẫu:
```python
gcd = int(12 / 18)
print(gcd, 12 * 18 // gcd)
```
chạy sẽ lỗi chia cho 0. Sửa lại: dùng vòng lặp chia lấy dư như bài giải.
- Bẫy 3: in ngược thứ tự `print(lcm, gcd)` cho mẫu sẽ ra `36 6`, là kết quả sai. Sửa lại: `print(gcd, lcm)`.

---

## 4. Lời giải tham khảo
```python
a, b = map(int, input().split())
x = a
y = b
while y != 0:
    x, y = y, x % y
gcd = x
lcm = a // gcd * b
print(gcd, lcm)
```
