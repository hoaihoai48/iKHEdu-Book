# Hướng Dẫn Giảng Dạy: Tổng dãy siêu lớn không lặp
Chuyên đề: **Vòng Lặp for & Chiếc Thước Đo range()**

---

## 1. Ý tưởng & Phân tích thuật toán
- Bản chất: tổng 1 + 2 + ... + N bằng công thức ghép cặp của Gauss: `S = N * (N + 1) // 2`. Với N tới 1 000 000 000 mà dùng vòng lặp `for` thì phải lặp 1 tỉ lần, chạy quá thời gian quy định, nên bắt buộc dùng công thức tính thẳng.
- Quy trình trong lời giải: đọc `n = int(input())`, rồi tính `n * (n + 1) // 2` và in ra. Dấu `//` là chia lấy phần nguyên, giữ kết quả luôn là số nguyên.
- Xử lý biên: với N nhỏ nhất là 1 thì `1 * 2 // 2 = 1`; với N lớn nhất 1 000 000 000 thì `1000000000 * 1000000001 // 2 = 500000000500000000`, Python tính số nguyên lớn chính xác.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 1000000000)
| Lượt | Giá trị của `n` | Biểu thức tính | Kết quả in ra |
|---|---|---|---|
| 1 | 1000000000 | 1000000000 * 1000000001 // 2 | 500000000500000000 |

Chương trình chỉ tính một phép nhân, một phép cộng và một phép chia nguyên rồi in ra `500000000500000000`, khớp với kết quả mẫu.

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- Bẫy 1 — dùng vòng lặp cộng dồn:
```python
n = int(input())
s = 0
for i in range(1, n + 1):
    s = s + i
print(s)
```
Với mẫu `1000000000` chương trình lặp 1 tỉ lần nên chạy quá thời gian quy định, không ra kết quả kịp. Cách sửa: thay cả vòng lặp bằng `print(n * (n + 1) // 2)`.
- Bẫy 2 — dùng chia `/` thay vì `//`:
```python
n = int(input())
print(n * (n + 1) / 2)
```
Với mẫu `1000000000` sẽ in ra `5e+17` (dạng số thực, mất chính xác). Cách sửa: dùng `//` để chia lấy phần nguyên.

---

## 4. Lời giải tham khảo
```python
n = int(input())
print(n * (n + 1) // 2)
```
