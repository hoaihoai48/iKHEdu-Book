# Hướng Dẫn Giảng Dạy: Tính tổng các chữ số trong chuỗi
Chuyên đề: **Duyệt Chuỗi & Biến Đổi Ký Tự Thần Kỳ**

---

## 1. Ý tưởng & Phân tích thuật toán
- Bản chất: nhặt từng ký tự là số trong chuỗi `s` rồi cộng dồn vào `tong`.
- Quy trình với biến thật (`s`, `tong`, `ch`):
  - Đọc `s = "A1B2C3D4"`.
  - Khởi động `tong = 0`, duyệt từng `ch`: gặp `1` cộng thành 1, `2` thành 3, `3` thành 6, `4` thành 10; các chữ `A, B, C, D` bỏ qua.
  - In ra 10 (đúng là 1 + 2 + 3 + 4).

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: A1B2C3D4)
| Bước | Lệnh chạy | Giá trị trong máy | Ghi chú |
|---|---|---|---|
| 1 | `s = input()` | `s = "A1B2C3D4"` | 4 chữ và 4 số |
| 2 | duyệt `1`, `2` | `tong` từ 0 thành 3 | A, B bị bỏ qua |
| 3 | duyệt `3`, `4` | `tong` từ 3 thành 10 | C, D bị bỏ qua |
| 4 | `print(tong)` | màn hình hiện `10` | khớp Output mẫu |

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- Bẫy 1: cộng trực tiếp ký tự mà quên đổi sang số. Đoạn sai:
```python
s = input()
tong = 0
for ch in s:
    if ch.isdigit():
        tong = tong + ch
print(tong)
```
Với mẫu trên chương trình báo lỗi vì không cộng số với chữ được, đáp án đúng là `10`. Cách sửa: đổi sang số `tong = tong + int(ch)`.
- Bẫy 2: đếm số lượng chữ số thay vì cộng giá trị. Đoạn sai:
```python
s = input()
tong = 0
for ch in s:
    if ch.isdigit():
        tong = tong + 1
print(tong)
```
Với mẫu trên in ra `4` (có 4 chữ số), đáp án đúng là `10`. Cách sửa: cộng giá trị `int(ch)`.

---

## 4. Lời giải tham khảo
```python
s = input()
tong = 0
for ch in s:
    if ch.isdigit():
        tong = tong + int(ch)
print(tong)
```
