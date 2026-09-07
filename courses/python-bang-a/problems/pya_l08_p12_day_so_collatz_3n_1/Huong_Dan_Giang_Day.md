# Hướng Dẫn Giảng Dạy: Dãy số Collatz (3n + 1)
Chuyên đề: **Vòng Lặp while & Người Lính Canh**

---

## 1. Ý tưởng & Phân tích thuật toán
- Bản chất: luật biến hình Collatz: số chẵn thì chia đôi (`n = n // 2`), số lẻ thì nhân ba cộng một (`n = 3 * n + 1`). Biến `count` đếm mỗi lần biến hình cho tới khi n thành 1.
- Quy trình trong lời giải: đọc `n`, đặt `count = 0`; chừng nào `n != 1` thì xét chẵn lẻ để biến đổi rồi tăng `count`; cuối cùng in `count`.
- Xử lý biên: với N nhỏ nhất là 1 thì không biến hình lần nào nên in `0`; với N tới 100 000 vòng lặp vẫn kết thúc và cho kết quả đúng.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 6)
| Bước | `n` đầu bước | Chẵn hay lẻ? | `n` sau bước | `count` |
|---|---|---|---|---|
| đầu | 6 | — | — | 0 |
| 1 | 6 | chẵn, 6 // 2 | 3 | 1 |
| 2 | 3 | lẻ, 3*3+1 | 10 | 2 |
| 3 | 10 | chẵn | 5 | 3 |
| 4 | 5 | lẻ | 16 | 4 |
| 5 | 16 | chẵn | 8 | 5 |
| 6 | 8 | chẵn | 4 | 6 |
| 7 | 4 | chẵn | 2 | 7 |
| 8 | 2 | chẵn | 1 | 8, dừng |

In ra `8`, khớp với kết quả mẫu.

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- Bẫy 1 — quên tăng `count` ở nhánh lẻ:
```python
n = int(input())
count = 0
while n != 1:
    if n % 2 == 0:
        n = n // 2
        count = count + 1
    else:
        n = 3 * n + 1
print(count)
```
Với mẫu `6` sẽ in ra `5` thay vì `8` vì 3 bước lẻ không được đếm. Cách sửa: đặt `count = count + 1` chung cho cả hai nhánh.
- Bẫy 2 — dùng `/` khi chia đôi:
```python
n = int(input())
count = 0
while n != 1:
    if n % 2 == 0:
        n = n / 2
    else:
        n = 3 * n + 1
    count = count + 1
print(count)
```
Với mẫu `6` thì n thành số thực 3.0, 10.0... dễ sai ở phép chia hết tiếp theo. Cách sửa: dùng `n = n // 2`.

---

## 4. Lời giải tham khảo
```python
n = int(input())
count = 0
while n != 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1
    count = count + 1
print(count)
```
