# Hướng Dẫn Giảng Dạy: Tính giai thừa $N!$
Chuyên đề: **Vòng Lặp for & Chiếc Thước Đo range()**

---

## 1. Ý tưởng & Phân tích thuật toán
- Bản chất: giai thừa `N! = 1 x 2 x ... x N`. Khác với cộng dồn, ở đây biến `gt` khởi đầu bằng 1 và mỗi bước nhân thêm `i`.
- Quy trình trong lời giải: đọc `n`, đặt `gt = 1`, vòng lặp cho `i` chạy 1 tới `n`, mỗi lượt `gt = gt * i`, cuối cùng in `gt`.
- Xử lý biên: với N nhỏ nhất là 1 thì `gt = 1`; với N lớn nhất là 20 thì `20! = 2432902008176640000`, Python vẫn tính chính xác.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 5)
| Lượt lặp | Giá trị của `i` | Phép tính `gt = gt * i` | Giá trị mới của `gt` |
|---|---|---|---|
| đầu | — | `gt = 1` | 1 |
| 1 | 1 | 1 * 1 | 1 |
| 2 | 2 | 1 * 2 | 2 |
| 3 | 3 | 2 * 3 | 6 |
| 4 | 4 | 6 * 4 | 24 |
| 5 | 5 | 24 * 5 | 120 |

In ra `120`, khớp với kết quả mẫu (`1 x 2 x 3 x 4 x 5 = 120`).

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- Bẫy 1 — khởi tạo `gt = 0`:
```python
n = int(input())
gt = 0
for i in range(1, n + 1):
    gt = gt * i
print(gt)
```
Với mẫu `5` sẽ in ra `0` vì nhân với 0 luôn bằng 0. Cách sửa: khởi tạo `gt = 1`.
- Bẫy 2 — dùng cộng thay vì nhân:
```python
n = int(input())
gt = 1
for i in range(1, n + 1):
    gt = gt + i
print(gt)
```
Với mẫu `5` sẽ in ra `16` thay vì `120`. Cách sửa: dùng `gt = gt * i`.

---

## 4. Lời giải tham khảo
```python
n = int(input())
gt = 1
for i in range(1, n + 1):
    gt = gt * i
print(gt)
```
