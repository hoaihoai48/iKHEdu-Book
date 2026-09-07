# Hướng Dẫn Giảng Dạy: Chuẩn hóa khoảng trắng
Chuyên đề: **Tách Từ & Mật Mã Thay Thế**

---

## 1. Ý tưởng & Phân tích thuật toán
- Bản chất: dọn thiệp của bạn Na sao cho đầu cuối sạch cách thừa, giữa các từ đúng một dấu cách.
- Quy trình:
  - Đọc câu vào biến `s`. Với số liệu mẫu, `s = "  Python rat la tuyet "` (dư cách đầu cuối và giữa `rat` với `la` có 2 cách).
  - Gọi `s.split()` được `['Python', 'rat', 'la', 'tuyet']`, mọi cách thừa tự mất.
  - Nối lại bằng `" ".join(...)` được `Python rat la tuyet` rồi in ra.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: Python rat la tuyet (thừa cách hai đầu))
| Bước | Lệnh chạy | Giá trị trong máy | Ghi chú |
|---|---|---|---|
| 1 | `s = input()` | `s = "  Python rat la tuyet "` | cách thừa nhiều chỗ |
| 2 | `s.split()` | `['Python', 'rat', 'la', 'tuyet']` | sạch cách thừa |
| 3 | `" ".join(...)` rồi in | màn hình hiện `Python rat la tuyet` | khớp Output mẫu |

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- Bẫy 1: chỉ gọt hai đầu bằng `strip()`. Đoạn sai:
```python
s = input()
print(s.strip())
```
Với mẫu trên giữa `rat` và `la` vẫn còn 2 dấu cách, đáp án đúng là `Python rat la tuyet` đều một cách. Cách sửa: dùng `" ".join(s.split())`.
- Bẫy 2: nối không có dấu cách `"".join(s.split())`. Đoạn sai:
```python
s = input()
print("".join(s.split()))
```
Với mẫu trên in ra `Pythonratlatuyet` dính liền, đáp án đúng là `Python rat la tuyet`. Cách sửa: nối bằng `" ".join(...)`.

---

## 4. Lời giải tham khảo
```python
s = input()
print(" ".join(s.split()))
```
