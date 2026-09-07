# Hướng Dẫn Giảng Dạy: Mã ASCII của ký tự
Chuyên đề: **Tách Từ & Mật Mã Thay Thế**

---

## 1. Ý tưởng & Phân tích thuật toán
- Bản chất: mỗi ký tự trên máy tính tương ứng với một con số, tra bằng hàm `ord`.
- Quy trình:
  - Đọc ký tự vào biến `ch`. Với số liệu mẫu, sau `input().strip()`, `ch = "A"`.
  - Gọi `ord(ch)` được 65 vì chữ `A` in hoa mang mã 65.
  - In 65 ra màn hình.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: A)
| Bước | Lệnh chạy | Giá trị trong máy | Ghi chú |
|---|---|---|---|
| 1 | `ch = input().strip()` | `ch = "A"` | ký tự mẫu |
| 2 | `ord(ch)` | `65` | mã của chữ A in hoa |
| 3 | `print(ord(ch))` | màn hình hiện `65` | khớp Output mẫu |

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- Bẫy 1: dùng `chr` ngược lại. Đoạn sai:
```python
ch = input().strip()
print(chr(ch))
```
Với mẫu `A` chương trình báo lỗi vì `chr` cần số chứ không nhận chữ, đáp án đúng là `65`. Cách sửa: dùng `ord(ch)`.
- Bẫy 2: quên `strip()` nên dư khoảng trắng khi nhập kèm cách. Đoạn sai:
```python
ch = input()
print(ord(ch))
```
Nếu nhập `A` kèm dấu cách ở đầu, máy đọc nhầm dấu cách (mã 32) và in ra `32`, đáp án đúng là `65`. Cách sửa: đọc `ch = input().strip()`.

---

## 4. Lời giải tham khảo
```python
ch = input().strip()
print(ord(ch))
```
