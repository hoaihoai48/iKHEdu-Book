# Hướng Dẫn Giảng Dạy: Đổi chữ hoa thành thường & ngược lại
Chuyên đề: **Duyệt Chuỗi & Biến Đổi Ký Tự Thần Kỳ**

---

## 1. Ý tưởng & Phân tích thuật toán
- Bản chất: lật trạng thái từng chữ cái, chữ khác (số, dấu câu, cách) giữ nguyên.
- Quy trình với biến thật (`s`, `kq`, `ch`):
  - Đọc `s = "Hello World 123"`, khởi động `kq = ''`.
  - Duyệt từng `ch`: `H` hoa thành `h`, `e` thường thành `E`, `l` thành `L`... dấu cách giữ nguyên, `1`, `2`, `3` giữ nguyên.
  - Được `kq = "hELLO wORLD 123"` rồi in ra.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: Hello World 123)
| Bước | Lệnh chạy | Giá trị trong máy | Ghi chú |
|---|---|---|---|
| 1 | `s = input()` | `s = "Hello World 123"` | 15 ký tự |
| 2 | duyệt `Hello` | `kq = "hELLO"` | H lật xuống, còn lại lật lên |
| 3 | duyệt ` World 123` | `kq = "hELLO wORLD 123"` | cách và số giữ nguyên |
| 4 | `print(kq)` | màn hình hiện `hELLO wORLD 123` | khớp Output mẫu |

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- Bẫy 1: đổi một chiều thành chữ thường hết bằng `lower()`. Đoạn sai:
```python
s = input()
print(s.lower())
```
Với mẫu trên in ra `hello world 123`, đáp án đúng là `hELLO wORLD 123`. Cách sửa: lật hai chiều như lời giải.
- Bẫy 2: quên nhánh giữ nguyên nên số và dấu câu bị đưa qua `upper()`. Đoạn sai:
```python
s = input()
kq = ''
for ch in s:
    if ch.isupper():
        kq = kq + ch.lower()
    else:
        kq = kq + ch.upper()
print(kq)
```
Với mẫu `Hello World 123` thì số và cách trùng cờ không lỗi, nhưng với câu có ký tự đặc biệt dễ phát sinh kết quả sai khó lường. Cách sửa chắc chắn: giữ nhánh `else: kq = kq + ch` như lời giải để số và dấu câu không bao giờ đổi.

---

## 4. Lời giải tham khảo
```python
s = input()
kq = ''
for ch in s:
    if ch.isupper():
        kq = kq + ch.lower()
    elif ch.islower():
        kq = kq + ch.upper()
    else:
        kq = kq + ch
print(kq)
```
