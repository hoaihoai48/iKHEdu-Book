# Hướng Dẫn Giảng Dạy: Ký tự đầu & ký tự cuối
Chuyên đề: **Chỉ Số Indexing & Nghệ Thuật Cắt Lát (Slicing)**

---

## 1. Ý tưởng & Phân tích thuật toán
- Bản chất: lấy chữ cái đầu tiên và chữ cái cuối cùng của chuỗi `s`, nối bằng một dấu cách.
- Quy trình:
  - Đọc chuỗi vào biến `s`. Với số liệu mẫu, `s = "PYTHON"`.
  - Lấy ký tự đầu `s[0]` được `P`, ký tự cuối `s[-1]` được `N`.
  - Nối thành `P + ' ' + N` rồi in ra `P N`.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: PYTHON)
| Bước | Lệnh chạy | Giá trị trong máy | Ghi chú |
|---|---|---|---|
| 1 | `s = input()` | `s = "PYTHON"` | đầu là P, cuối là N |
| 2 | `s[0] + ' ' + s[-1]` | `"P N"` | có đúng một dấu cách |
| 3 | `print(...)` | màn hình hiện `P N` | khớp Output mẫu |

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- Bẫy 1: nối trực tiếp không có dấu cách. Đoạn sai:
```python
s = input()
print(s[0] + s[-1])
```
Với mẫu `PYTHON` in ra `PN` dính nhau, đáp án đúng là `P N`. Cách sửa: chèn `' '` ở giữa.
- Bẫy 2: lấy ký tự cuối bằng `s[len(s)]`. Đoạn sai:
```python
s = input()
print(s[0] + ' ' + s[len(s)])
```
Với mẫu `PYTHON`, `len(s)` bằng 6 vượt quá vị trí cuối (5) nên chương trình báo lỗi và không in gì, đáp án đúng là `P N`. Cách sửa: dùng `s[-1]` hoặc `s[len(s) - 1]`.

---

## 4. Lời giải tham khảo
```python
s = input()
print(s[0] + ' ' + s[-1])
```
