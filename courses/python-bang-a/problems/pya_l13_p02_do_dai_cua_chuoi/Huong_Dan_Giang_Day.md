# Hướng Dẫn Giảng Dạy: Độ dài của chuỗi
Chuyên đề: **Chỉ Số Indexing & Nghệ Thuật Cắt Lát (Slicing)**

---

## 1. Ý tưởng & Phân tích thuật toán
- Bản chất: cần đếm xem chuỗi `s` có bao nhiêu ký tự, kể cả dấu cách.
- Quy trình:
  - Đọc cả dòng vào biến `s` bằng `input()`. Với số liệu mẫu, `s = "Python"`.
  - Gọi `len(s)` để lấy độ dài. Chuỗi `"Python"` gồm 6 chữ cái P, y, t, h, o, n nên `len(s)` bằng 6.
  - In 6 ra màn hình bằng `print(len(s))`.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: Python)
| Bước | Lệnh chạy | Giá trị trong máy | Ghi chú |
|---|---|---|---|
| 1 | `s = input()` | `s = "Python"` | đọc đúng dòng mẫu |
| 2 | `len(s)` | `6` | đếm P, y, t, h, o, n |
| 3 | `print(len(s))` | màn hình hiện `6` | khớp Output mẫu |

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- Bẫy 1: chỉ gọi `len(s)` mà quên `print`. Đoạn sai:
```python
s = input()
len(s)
```
Với mẫu `Python`, màn hình không in gì cả, trong khi đáp án đúng phải là `6`. Cách sửa: bọc lệnh in `print(len(s))`.
- Bẫy 2: tách từ bằng `s = input().split()` rồi đo `len(s)`. Đoạn sai:
```python
s = input().split()
print(len(s))
```
Với mẫu `Python` vẫn ra `6` do nhầm thành độ dài danh sách 1 từ, còn câu có dấu cách như `a b` sẽ ra `2` thay vì `3`. Cách sửa: giữ nguyên `s = input()` rồi dùng `len(s)`.

---

## 4. Lời giải tham khảo
```python
s = input()
print(len(s))
```
