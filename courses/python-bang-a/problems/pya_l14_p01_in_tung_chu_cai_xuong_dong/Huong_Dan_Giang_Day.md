# Hướng Dẫn Giảng Dạy: In từng chữ cái xuống dòng
Chuyên đề: **Duyệt Chuỗi & Biến Đổi Ký Tự Thần Kỳ**

---

## 1. Ý tưởng & Phân tích thuật toán
- Bản chất: đi thăm từng chữ cái trong từ `s`, mỗi chữ nằm một dòng riêng.
- Quy trình:
  - Đọc từ vào biến `s`. Với số liệu mẫu, `s = "CAT"`.
  - Lặp `for ch in s`: lượt 1 `ch = "C"`, lượt 2 `ch = "A"`, lượt 3 `ch = "T"`.
  - Mỗi lượt `print(ch)` xuống dòng một lần nên được 3 dòng `C`, `A`, `T`.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: CAT)
| Bước | Lệnh chạy | Giá trị trong máy | Ghi chú |
|---|---|---|---|
| 1 | `s = input()` | `s = "CAT"` | 3 chữ cái |
| 2 | lượt 1 `ch = "C"` | in dòng 1 `C` | chữ đầu |
| 3 | lượt 2 `ch = "A"` | in dòng 2 `A` | chữ giữa |
| 4 | lượt 3 `ch = "T"` | in dòng 3 `T` | khớp Output mẫu |

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- Bẫy 1: in cả từ một lần `print(s)`. Đoạn sai:
```python
s = input()
print(s)
```
Với mẫu `CAT` chỉ in một dòng `CAT`, đáp án đúng là 3 dòng `C`, `A`, `T`. Cách sửa: dùng vòng lặp `for ch in s: print(ch)`.
- Bẫy 2: in các chữ trên cùng một dòng bằng `end`. Đoạn sai:
```python
s = input()
for ch in s:
    print(ch, end='')
```
Với mẫu `CAT` in ra `CAT` trên một dòng, đáp án đúng là mỗi chữ một dòng. Cách sửa: để `print(ch)` xuống dòng tự nhiên.

---

## 4. Lời giải tham khảo
```python
s = input()
for ch in s:
    print(ch)
```
