# Hướng Dẫn Giảng Dạy: Đảo ngược tên riêng
Chuyên đề: **Chỉ Số Indexing & Nghệ Thuật Cắt Lát (Slicing)**

---

## 1. Ý tưởng & Phân tích thuật toán
- Bản chất: đọc ngược toàn bộ chuỗi `s` để tạo biệt danh bí mật.
- Quy trình:
  - Đọc chuỗi vào biến `s`. Với số liệu mẫu, `s = "DORAEMON"` (độ dài 8).
  - Dùng lát cắt bước nhảy âm `s[::-1]` để lật ngược thứ tự ký tự.
  - In ra `NOMEAROD` bằng `print(s[::-1])`.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: DORAEMON)
| Bước | Lệnh chạy | Giá trị trong máy | Ghi chú |
|---|---|---|---|
| 1 | `s = input()` | `s = "DORAEMON"` | D-O-R-A-E-M-O-N |
| 2 | `s[::-1]` | `"NOMEAROD"` | đọc ngược từng chữ cái |
| 3 | `print(s[::-1])` | màn hình hiện `NOMEAROD` | khớp Output mẫu |

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- Bẫy 1: quên dấu trừ, viết `s[::1]`. Đoạn sai:
```python
s = input()
print(s[::1])
```
Với mẫu `DORAEMON` in ra nguyên `DORAEMON`, đáp án đúng là `NOMEAROD`. Cách sửa: viết đủ `s[::-1]`.
- Bẫy 2: dùng `reversed(s)` rồi in trực tiếp. Đoạn sai:
```python
s = input()
print(reversed(s))
```
Với mẫu `DORAEMON` màn hình hiện dòng mô tả vật lạ thay vì `NOMEAROD`. Cách sửa: dùng `print(s[::-1])`.

---

## 4. Lời giải tham khảo
```python
s = input()
print(s[::-1])
```
