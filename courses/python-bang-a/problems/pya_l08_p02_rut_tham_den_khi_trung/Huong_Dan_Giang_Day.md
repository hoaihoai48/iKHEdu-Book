# Hướng Dẫn Giảng Dạy: Rút thăm đến khi trúng
Chuyên đề: **Vòng Lặp while & Người Lính Canh**

---

## 1. Ý tưởng & Phân tích thuật toán
- Bản chất: đọc liên tục không biết trước số lượng, dừng ngay khi bốc trúng lá phiếu số 7. Vòng lặp `while True` đọc từng `x` và `break` khi gặp 7.
- Quy trình trong lời giải: `while True` đọc `x`; nếu `x == 7` (lời giải còn chấp nhận thêm 77 cho chắc) thì `break`; sau vòng lặp in đúng một dòng `DA TRUNG THUONG!`.
- Xử lý biên: nếu lá đầu tiên đã là 7 thì in ngay; dãy mẫu 10, 25, 7 thì dừng ở lá thứ ba.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 10 / 25 / 7)
| Lần đọc | Giá trị của `x` | `x == 7`? | Hành động |
|---|---|---|---|
| 1 | 10 | không | đọc tiếp |
| 2 | 25 | không | đọc tiếp |
| 3 | 7 | có | dừng vòng lặp |

Sau vòng lặp in ra `DA TRUNG THUONG!`, khớp với kết quả mẫu.

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- Bẫy 1 — in thông báo trong vòng lặp:
```python
while True:
    x = int(input().strip())
    if x == 7:
        print("DA TRUNG THUONG!")
print("DA TRUNG THUONG!")
```
Với mẫu `10 / 25 / 7` vòng lặp không dừng nên chương trình treo luôn. Cách sửa: dùng `break` khi gặp 7 và chỉ in một lần sau vòng lặp.
- Bẫy 2 — sai chữ in (thường hoặc có dấu):
```python
while True:
    x = int(input().strip())
    if x == 7:
        break
print("Da trung thuong!")
```
Với mẫu `10 / 25 / 7` sẽ in `Da trung thuong!` khác chữ mẫu nên chương trình kiểm tra báo kết quả sai. Cách sửa: in đúng chữ in hoa `DA TRUNG THUONG!`.

---

## 4. Lời giải tham khảo
```python
while True:
    try:
        x = int(input().strip())
        if x == 7 or x == 77:
            break
    except:
        break
print("DA TRUNG THUONG!")
```
