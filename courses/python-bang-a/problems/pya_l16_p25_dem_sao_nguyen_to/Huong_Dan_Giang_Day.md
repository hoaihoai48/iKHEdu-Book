# Hướng Dẫn Giảng Dạy: Đếm sao nguyên tố
Chuyên đề: **Chiếc Hộp Thần Kỳ list & Thao Tác Cơ Bản**

---

## 1. Ý tưởng & Phân tích thuật toán

- Bản chất của bài này là sàng lọc các số từ 1 đến `N`, gạch bỏ dần các bội số để còn lại đúng các số nguyên tố.
- Với số mẫu `N = 10`: các số nguyên tố là `2`, `3`, `5`, `7` nên đáp án là `4` (số `1` không phải số nguyên tố).
- Quy trình trong lời giải với các biến `n`, `is_p`, `i`, `j`:
  - Đọc `n = 10`; vì `n >= 2` nên dựng bảng `is_p` dài 11 ô, đánh dấu `is_p[0]` và `is_p[1]` là sai.
  - Với `i = 2`: gạch các bội `4`, `6`, `8`, `10`. Với `i = 3`: gạch `9` (các bội `6` đã gạch rồi).
  - Đếm các ô còn đúng: `2`, `3`, `5`, `7` được `4` rồi in ra.
- Giá trị biên cụ thể: `N = 1` thì không có số nguyên tố nào nên in `0`; `N = 10^6` thì bảng dài một triệu lẻ một ô vẫn vừa bộ nhớ.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 10)

| Bước | Thao tác | Giá trị |
|------|----------|---------|
| 1 | Đọc `n` | `n = 10` (lớn hơn 1 nên làm tiếp) |
| 2 | Dựng `is_p`, gạch `0`, `1` | còn đúng: 2, 3, 4, 5, 6, 7, 8, 9, 10 |
| 3 | `i = 2`, gạch bội từ `4` | gạch 4, 6, 8, 10; còn đúng: 2, 3, 5, 7, 9 |
| 4 | `i = 3`, gạch bội từ `9` | gạch 9; còn đúng: 2, 3, 5, 7 |
| 5 | `i = 4` hết vòng (`4 * 4 > 10`) | dừng |
| 6 | Đếm và in | màn hình hiện `4` |

Kết quả cuối cùng khớp với đáp án mẫu: `4`.

---

## 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — coi số 1 là số nguyên tố:
```python
n = int(input())
if n < 2:
    print(0)
else:
    is_p = [True] * (n + 1)
    is_p[0] = False
    i = 2
    while i * i <= n:
        if is_p[i]:
            j = i * i
            while j <= n:
                is_p[j] = False
                j += i
        i += 1
    print(sum(is_p))
```
Với mẫu `10` thì đếm cả số `1` nên in ra `5`, không khớp đáp án mẫu `4`. Cách sửa: gạch thêm `is_p[1] = False`.
- Bẫy 2 — gạch bội từ `2 * i` bằng bước 1:
```python
n = int(input())
if n < 2:
    print(0)
else:
    is_p = [True] * (n + 1)
    is_p[0] = False
    is_p[1] = False
    i = 2
    while i * i <= n:
        if is_p[i]:
            j = 2 * i
            while j <= n:
                is_p[j] = False
                j += 1
        i += 1
    print(sum(is_p))
```
Với mẫu `10`, khi `i = 2` thì gạch `4` xong tăng `j` từng 1 nên gạch luôn cả `5`, `7` là các số nguyên tố, in ra `2` sai. Cách sửa: gạch đúng bội bằng bước nhảy `j += i` bắt đầu từ `i * i`.
- Bẫy 3 — thử chia từng số tới `N`:
```python
n = int(input())
c = 0
for v in range(2, n + 1):
    ngto = True
    for u in range(2, v):
        if v % u == 0:
            ngto = False
    if ngto:
        c += 1
print(c)
```
Với mẫu `10` vẫn ra `4`, nhưng với `N = 10^6` thì số phép chia quá lớn, chạy rất lâu. Cách sửa: dùng bảng sàng gạch bội như lời giải.

---

## 4. Lời giải tham khảo

```python
n = int(input())
if n < 2:
    print(0)
else:
    is_p = [True] * (n + 1)
    is_p[0] = False
    is_p[1] = False
    i = 2
    while i * i <= n:
        if is_p[i]:
            j = i * i
            while j <= n:
                is_p[j] = False
                j += i
        i += 1
    print(sum(is_p))
```
