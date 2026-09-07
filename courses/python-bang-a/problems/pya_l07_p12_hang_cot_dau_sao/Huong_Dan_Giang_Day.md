# Hướng Dẫn Giảng Dạy: Hàng cột dấu sao
Chuyên đề: **Vòng Lặp for & Chiếc Thước Đo range()**

---

## 1. Ý tưởng & Phân tích thuật toán
- Bản chất: hình chữ nhật đặc kích thước R hàng, C cột. Mỗi hàng là chuỗi `'*' * c` dài đúng C ký tự, lặp lại R lần.
- Quy trình trong lời giải: đọc `r` rồi đọc `c`, vòng lặp `for i in range(r)` in `print('*' * c)` mỗi lượt một hàng.
- Xử lý biên: với R = 1, C = 1 thì chỉ in một dấu `*`; với R = 50, C = 50 thì in 50 hàng, mỗi hàng 50 dấu sao.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 3 / 5)
| Lượt lặp | `i` trong `range(3)` | `'*' * 5` | Dòng in ra |
|---|---|---|---|
| 1 | 0 | `*****` | ***** |
| 2 | 1 | `*****` | ***** |
| 3 | 2 | `*****` | ***** |

Ba hàng giống nhau ghép thành hình chữ nhật 3x5, khớp với kết quả mẫu.

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- Bẫy 1 — đọc cả hai số trên một dòng:
```python
r, c = map(int, input().split())
for i in range(r):
    print('*' * c)
```
Với mẫu nhập `3` rồi xuống dòng `5`, lệnh tách một dòng sẽ thiếu số và lỗi. Cách sửa: đọc riêng `r = int(input())` rồi `c = int(input())` như lời giải.
- Bẫy 2 — nhầm số hàng với số cột:
```python
r = int(input())
c = int(input())
for i in range(c):
    print('*' * r)
```
Với mẫu `3 / 5` sẽ in 5 hàng mỗi hàng 3 sao, cho kết quả sai kích thước. Cách sửa: lặp `range(r)` và nhân `'*' * c`.

---

## 4. Lời giải tham khảo
```python
r = int(input())
c = int(input())
for i in range(r):
    print('*' * c)
```
