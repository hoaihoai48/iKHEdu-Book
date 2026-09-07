# Hướng Dẫn Giảng Dạy: Đếm số từ trong câu
Chuyên đề: **Tách Từ & Mật Mã Thay Thế**

---

## 1. Ý tưởng & Phân tích thuật toán
- Bản chất: từ là các cụm chữ cách nhau bởi dấu cách; `split()` tự bỏ hết cách thừa.
- Quy trình:
  - Đọc cả dòng vào biến `s`. Với số liệu mẫu, `s = "  Chuc mung nam moi "` (dư cách đầu và cuối).
  - Gọi `s.split()` được danh sách 4 từ `['Chuc', 'mung', 'nam', 'moi']`.
  - In `len(words)` được 4.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: Chuc mung nam moi (thừa cách hai đầu))
| Bước | Lệnh chạy | Giá trị trong máy | Ghi chú |
|---|---|---|---|
| 1 | `s = input()` | `s = "  Chuc mung nam moi "` | dư cách hai đầu |
| 2 | `words = s.split()` | `['Chuc', 'mung', 'nam', 'moi']` | cách thừa tự biến mất |
| 3 | `print(len(words))` | màn hình hiện `4` | khớp Output mẫu |

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- Bẫy 1: đếm dấu cách cộng 1 nên sai khi dư cách. Đoạn sai:
```python
s = input()
print(s.count(' ') + 1)
```
Với mẫu `  Chuc mung nam moi ` có 6 dấu cách nên in ra `7`, đáp án đúng là `4`. Cách sửa: dùng `len(s.split())`.
- Bẫy 2: tách bằng `s.split(' ')` giữ lại chuỗi rỗng. Đoạn sai:
```python
s = input()
words = s.split(' ')
print(len(words))
```
Với mẫu trên danh sách lẫn chuỗi rỗng nên in ra số lớn hơn `4`. Cách sửa: dùng `s.split()` không truyền gì.

---

## 4. Lời giải tham khảo
```python
s = input()
words = s.split()
print(len(words))
```
