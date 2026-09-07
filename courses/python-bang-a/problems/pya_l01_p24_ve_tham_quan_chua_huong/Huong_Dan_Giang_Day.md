# Hướng Dẫn Giảng Dạy: Vé tham quan chùa hương
Chuyên đề: **Chào Python & Chiếc Hộp Biến Số**

---

## 1. Ý tưởng & Phân tích thuật toán
- Bản chất của bài này là cộng tiền vé thuyền và vé cáp treo cho cả đoàn: đoàn `n = 10` người gồm `m = 4` trẻ em nên có `6` người lớn. Vé thuyền người lớn `a = 20`, trẻ em `b = 10`; vé cáp treo người lớn `x = 50`, trẻ em `y = 30`. Tiền thuyền là `6 * 20 + 4 * 10 = 160`, tiền cáp treo là `6 * 50 + 4 * 30 = 420`, tổng là `580`.
- Quy trình với các biến `a, b, x, y, n, m, so_tre_em, so_nguoi_lon, tong_tien` trong lời giải: đọc sáu số `20, 10, 50, 30, 10, 4` vào `a, b, x, y, n, m`, tính `so_tre_em = 4` và `so_nguoi_lon = 10 - 4 = 6`, rồi tính `tong_tien = 6 * (20 + 50) + 4 * (10 + 30) = 6 * 70 + 4 * 40 = 420 + 160 = 580` và in ra.
- Xử lý biên: ràng buộc cho vé từ 0 tới 100, đoàn `0 <= m <= n < 100`. Thầy cô cho các con thử trường hợp đặc biệt đoàn toàn trẻ em như `n = 5, m = 5` thì số người lớn là `0`, và đoàn không ai `n = 0, m = 0` thì tổng tiền là `0`.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 20, 10, 50, 30, 10 và 4)
| Bước | Lệnh chạy | Giá trị biến | Màn hình hiện ra |
|------|-----------|--------------|------------------|
| 1 | Đọc 6 dòng `20, 10, 50, 30, 10, 4` vào `a, b, x, y, n, m` | `a = 20`, `b = 10`, `x = 50`, `y = 30`, `n = 10`, `m = 4` | (chưa in gì) |
| 2 | `so_tre_em = m` | `so_tre_em = 4` | (chưa in gì) |
| 3 | `so_nguoi_lon = n - m` tức `10 - 4` | `so_nguoi_lon = 6` | (chưa in gì) |
| 4 | `tong_tien = 6 * (20 + 50) + 4 * (10 + 30)` tức `420 + 160` | `tong_tien = 580` | (chưa in gì) |
| 5 | `print(tong_tien)` | — | `580` |

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- Bẫy 1: lấy nhầm `n` làm số người lớn, viết `tong_tien = n * (a + x) + m * (b + y)` thì với mẫu cho ra `10 * 70 + 4 * 40 = 860` thay vì `580` vì đếm trùng 4 trẻ em. Cách sửa: tính `so_nguoi_lon = n - m` rồi mới nhân.
- Bẫy 2: chỉ tính một loại vé, ví dụ `tong_tien = so_nguoi_lon * a + so_tre_em * b` thì với mẫu chỉ ra `160` (tiền thuyền), thiếu `420` tiền cáp treo. Cách sửa: mỗi người phải cộng cả hai vé, viết `(a + x)` và `(b + y)`.
- Bẫy 3: đọc sai thứ tự sáu số, ví dụ đọc `n` trước `a` thì mọi biến lệch hết và tổng ra số lạ thay vì `580`. Cách sửa: đọc đúng thứ tự đề cho là `a, b, x, y, n, m` mỗi số một dòng.

---

## 4. Lời giải tham khảo
```python
a = int(input())
b = int(input())
x = int(input())
y = int(input())
n = int(input())
m = int(input())
so_tre_em = m
so_nguoi_lon = n - m
tong_tien = so_nguoi_lon * (a + x) + so_tre_em * (b + y)
print(tong_tien)
```
