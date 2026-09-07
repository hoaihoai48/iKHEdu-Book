# Hướng Dẫn Giảng Dạy: Mật mã thay thế hoán vị (anagram)
Chuyên đề: **Tách Từ & Mật Mã Thay Thế**

---

## 1. Ý tưởng & Phân tích thuật toán
- Bản chất: hai từ là hoán vị của nhau khi chúng gồm đúng cùng một bộ chữ cái, chỉ khác thứ tự xếp.
- Quy trình:
  - Đọc hai từ vào `s1` và `s2`. Với số liệu mẫu, `s1 = "listen"`, `s2 = "silent"`.
  - Sắp xếp chữ cái hai từ bằng `sorted(...)`: cả hai đều thành `['e', 'i', 'l', 'n', 's', 't']`.
  - Hai danh sách bằng nhau nên in `YES` (ngược lại in `NO`).

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: listen và silent)
| Bước | Lệnh chạy | Giá trị trong máy | Ghi chú |
|---|---|---|---|
| 1 | `s1 = input().strip()` | `s1 = "listen"` | từ thứ nhất |
| 2 | `s2 = input().strip()` | `s2 = "silent"` | từ thứ hai |
| 3 | `sorted(s1)` và `sorted(s2)` | cùng `['e', 'i', 'l', 'n', 's', 't']` | cùng bộ chữ cái |
| 4 | so sánh bằng nhau | đúng nên `print("YES")` | khớp Output mẫu |

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- Bẫy 1: so trực tiếp `s1 == s2` mà không sắp xếp. Đoạn sai:
```python
s1 = input().strip()
s2 = input().strip()
if s1 == s2:
    print("YES")
else:
    print("NO")
```
Với mẫu `listen` và `silent` in ra `NO`, đáp án đúng là `YES`. Cách sửa: so `sorted(s1) == sorted(s2)`.
- Bẫy 2: so độ dài thay vì so chữ cái. Đoạn sai:
```python
s1 = input().strip()
s2 = input().strip()
if len(s1) == len(s2):
    print("YES")
else:
    print("NO")
```
Với hai từ dài bằng nhau nhưng khác chữ (ví dụ `abc` và `xyz`) vẫn in `YES` là kết quả sai. Cách sửa: so `sorted(s1) == sorted(s2)`.

---

## 4. Lời giải tham khảo
```python
s1 = input().strip()
s2 = input().strip()
if sorted(s1) == sorted(s2):
    print("YES")
else:
    print("NO")
```
