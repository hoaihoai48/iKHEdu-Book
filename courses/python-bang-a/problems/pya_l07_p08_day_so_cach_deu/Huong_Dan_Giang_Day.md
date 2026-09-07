# Hướng Dẫn Giảng Dạy: Dãy số cách đều
Chuyên đề: **Vòng Lặp for & Chiếc Thước Đo range()**

---

## 1. Ý tưởng & Phân tích thuật toán
- Bản chất: dãy cộng với số hạng đầu `a`, công sai `d`. Số hạng thứ `i` (đếm từ 0) là `a + i * d`.
- Quy trình trong lời giải: đọc `a`, `d`, `n`; vòng lặp cho `i` chạy `range(n)`, mỗi lượt in `a + i * d`; nếu chưa phải số cuối (`i < n - 1`) thì in thêm một dấu cách, cuối cùng xuống dòng.
- Xử lý biên: với n nhỏ nhất là 1 thì chỉ in mỗi `a`; mỗi giá trị a, d, n đều không vượt quá 100.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 2 / 3 / 5)
| Lượt lặp | Giá trị của `i` | Tính `2 + i * 3` | Phần in ra |
|---|---|---|---|
| 1 | 0 | 2 | `2 ` |
| 2 | 1 | 5 | `5 ` |
| 3 | 2 | 8 | `8 ` |
| 4 | 3 | 11 | `11 ` |
| 5 | 4 | 14 | `14` + xuống dòng |

Một dòng duy nhất `2 5 8 11 14`, khớp với kết quả mẫu.

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- Bẫy 1 — công thức thiếu `a`:
```python
a = int(input())
d = int(input())
n = int(input())
for i in range(n):
    print(a + d, end='')
```
Với mẫu `2 / 3 / 5` sẽ in toàn số `5` lặp lại. Cách sửa: công thức đúng là `a + i * d`.
- Bẫy 2 — mỗi số một dòng:
```python
a = int(input())
d = int(input())
n = int(input())
for i in range(n):
    print(a + i * d)
```
Với mẫu `2 / 3 / 5` sẽ in 5 dòng thay vì một dòng `2 5 8 11 14`. Cách sửa: in với `end=''` và chèn dấu cách giữa các số như lời giải.

---

## 4. Lời giải tham khảo
```python
a = int(input())
d = int(input())
n = int(input())
for i in range(n):
    print(a + i * d, end='')
    if i < n - 1:
        print(' ', end='')
print()
```
