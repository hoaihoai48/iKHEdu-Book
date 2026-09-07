# Hướng Dẫn Giảng Dạy: Tổng số chẵn trong đoạn
Chuyên đề: **Vòng Lặp for & Chiếc Thước Đo range()**

---

## 1. Ý tưởng & Phân tích thuật toán
- Bản chất: trong đoạn từ A tới B chỉ cộng những số chia hết cho 2 (`i % 2 == 0`). Các số lẻ bị bỏ qua.
- Quy trình trong lời giải: đọc `a` rồi đọc `b`, đặt `s = 0`, vòng lặp cho `i` chạy từ `a` tới `b` (kể cả `b` nhờ `range(a, b + 1)`), nếu `i % 2 == 0` thì `s += i`, cuối cùng in `s`.
- Xử lý biên: đoạn nhỏ nhất A = B = 1 thì không có số chẵn nào nên tổng là 0; đoạn tới 10 000 thì vòng lặp duyệt tối đa 10 000 số.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 3 / 8)
| Lượt lặp | Giá trị của `i` | `i % 2 == 0`? | Giá trị mới của `s` |
|---|---|---|---|
| đầu | — | — | 0 |
| 1 | 3 | không | 0 |
| 2 | 4 | có, cộng 4 | 4 |
| 3 | 5 | không | 4 |
| 4 | 6 | có, cộng 6 | 10 |
| 5 | 7 | không | 10 |
| 6 | 8 | có, cộng 8 | 18 |

In ra `18` (vì `4 + 6 + 8 = 18`), khớp với kết quả mẫu.

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- Bẫy 1 — quên cộng 1 ở điểm dừng:
```python
a = int(input())
b = int(input())
s = 0
for i in range(a, b):
    if i % 2 == 0:
        s += i
print(s)
```
Với mẫu `3 / 8` chỉ xét tới 7 nên in ra `10` thay vì `18`. Cách sửa: dùng `range(a, b + 1)`.
- Bẫy 2 — kiểm tra số lẻ thay vì số chẵn:
```python
a = int(input())
b = int(input())
s = 0
for i in range(a, b + 1):
    if i % 2 == 1:
        s += i
print(s)
```
Với mẫu `3 / 8` sẽ cộng 3 + 5 + 7 = `15` thay vì `18`. Cách sửa: điều kiện đúng là `i % 2 == 0`.

---

## 4. Lời giải tham khảo
```python
a = int(input())
b = int(input())
s = 0
for i in range(a, b + 1):
    if i % 2 == 0:
        s += i
print(s)
```
