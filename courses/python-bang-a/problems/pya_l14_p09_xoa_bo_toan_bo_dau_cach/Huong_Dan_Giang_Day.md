# Hướng Dẫn Giảng Dạy: Xóa bỏ toàn bộ dấu cách
Chuyên đề: **Duyệt Chuỗi & Biến Đổi Ký Tự Thần Kỳ**

---

## 1. Ý tưởng & Phân tích thuật toán
- Bản chất: xóa sạch mọi dấu cách để chuỗi viết liền hoàn toàn.
- Quy trình:
  - Đọc cả dòng vào biến `s`. Với số liệu mẫu, `s = "Lap Trinh Python Bang A"` (4 dấu cách).
  - Gọi `s.replace(' ', '')` để thay mỗi dấu cách bằng chuỗi rỗng.
  - In ra `LapTrinhPythonBangA`.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: Lap Trinh Python Bang A)
| Bước | Lệnh chạy | Giá trị trong máy | Ghi chú |
|---|---|---|---|
| 1 | `s = input()` | `s = "Lap Trinh Python Bang A"` | 4 dấu cách |
| 2 | `s.replace(' ', '')` | `"LapTrinhPythonBangA"` | các từ dính liền nhau |
| 3 | `print(...)` | màn hình hiện `LapTrinhPythonBangA` | khớp Output mẫu |

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- Bẫy 1: thay bằng một dấu cách nên không xóa gì `s.replace('  ', ' ')`. Đoạn sai:
```python
s = input()
print(s.replace('  ', ' '))
```
Với mẫu `Lap Trinh Python Bang A` (toàn dấu cách đơn) in ra nguyên văn, đáp án đúng là `LapTrinhPythonBangA`. Cách sửa: thay bằng chuỗi rỗng `s.replace(' ', '')`.
- Bẫy 2: dùng `strip()` chỉ gọt hai đầu. Đoạn sai:
```python
s = input()
print(s.strip())
```
Với mẫu trên vẫn còn 3 dấu cách giữa các từ, in ra `Lap Trinh Python Bang A`, đáp án đúng là `LapTrinhPythonBangA`. Cách sửa: dùng `s.replace(' ', '')`.

---

## 4. Lời giải tham khảo
```python
s = input()
print(s.replace(' ', ''))
```
