# Hướng Dẫn Giảng Dạy: Nhập số đến khi gặp số 0
Chuyên đề: **Vòng Lặp while & Người Lính Canh**

---

## 1. Ý tưởng & Phân tích thuật toán
- Bản chất: không biết trước có bao nhiêu số, cứ đọc tới khi gặp số 0 thì dừng. Số 0 chỉ là lính gác báo dừng, không được đếm.
- Quy trình trong lời giải: đặt `count = 0`; `while True` đọc từng `x`; nếu `x == 0` thì `break`; ngược lại `count = count + 1`; cuối cùng in `count`.
- Xử lý biên: nếu nhập ngay số 0 đầu tiên thì kết quả là 0; dãy mẫu có 3 số trước số 0 nên kết quả là 3.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 5 / 12 / 8 / 0)
| Lần đọc | Giá trị của `x` | `x == 0`? | `count` sau bước |
|---|---|---|---|
| đầu | — | — | 0 |
| 1 | 5 | không | 1 |
| 2 | 12 | không | 2 |
| 3 | 8 | không | 3 |
| 4 | 0 | có, dừng | 3 |

In ra `3` vì có 3 số 5, 12, 8 trước số 0, khớp với kết quả mẫu.

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- Bẫy 1 — đếm luôn số 0:
```python
count = 0
while True:
    x = int(input())
    count = count + 1
    if x == 0:
        break
print(count)
```
Với mẫu `5 / 12 / 8 / 0` sẽ in ra `4` thay vì `3`. Cách sửa: kiểm tra `if x == 0: break` trước rồi mới tăng `count`.
- Bẫy 2 — dừng khi gặp số âm:
```python
count = 0
while True:
    x = int(input())
    if x <= 0:
        break
    count = count + 1
print(count)
```
Với dãy có số âm hợp lệ thì chương trình dừng sớm và đếm thiếu. Cách sửa: chỉ dừng khi `x == 0`.

---

## 4. Lời giải tham khảo
```python
count = 0
while True:
    x = int(input())
    if x == 0:
        break
    count = count + 1
print(count)
```
