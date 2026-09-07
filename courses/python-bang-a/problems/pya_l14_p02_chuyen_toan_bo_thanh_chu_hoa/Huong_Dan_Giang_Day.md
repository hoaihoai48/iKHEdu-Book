# Hướng Dẫn Giảng Dạy: Chuyển toàn bộ thành chữ hoa
Chuyên đề: **Duyệt Chuỗi & Biến Đổi Ký Tự Thần Kỳ**

---

## 1. Ý tưởng & Phân tích thuật toán
- Bản chất: biến mọi chữ cái trong chuỗi `s` thành chữ in hoa.
- Quy trình:
  - Đọc cả dòng vào biến `s`. Với số liệu mẫu, `s = "ikhedu vietnam"`.
  - Gọi `s.upper()` để đổi toàn bộ chữ thường thành chữ hoa, dấu cách giữ nguyên.
  - In ra `IKHEDU VIETNAM` bằng `print(s.upper())`.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: ikhedu vietnam)
| Bước | Lệnh chạy | Giá trị trong máy | Ghi chú |
|---|---|---|---|
| 1 | `s = input()` | `s = "ikhedu vietnam"` | 14 ký tự cả dấu cách |
| 2 | `s.upper()` | `"IKHEDU VIETNAM"` | từng chữ đều hóa in hoa |
| 3 | `print(s.upper())` | màn hình hiện `IKHEDU VIETNAM` | khớp Output mẫu |

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- Bẫy 1: gọi `s.upper()` mà quên `print`. Đoạn sai:
```python
s = input()
s.upper()
```
Với mẫu `ikhedu vietnam`, màn hình không in gì cả, đáp án đúng là `IKHEDU VIETNAM`. Cách sửa: bọc lệnh in `print(s.upper())`.
- Bẫy 2: dùng `s.lower()` ngược yêu cầu. Đoạn sai:
```python
s = input()
print(s.lower())
```
Với mẫu trên vẫn in ra `ikhedu vietnam` chữ thường, đáp án đúng là `IKHEDU VIETNAM`. Cách sửa: dùng `s.upper()`.

---

## 4. Lời giải tham khảo
```python
s = input()
print(s.upper())
```
