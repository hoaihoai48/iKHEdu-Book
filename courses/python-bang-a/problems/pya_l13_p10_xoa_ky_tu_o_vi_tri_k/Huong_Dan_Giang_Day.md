# Hướng Dẫn Giảng Dạy: Xóa ký tự ở vị trí K
Chuyên đề: **Chỉ Số Indexing & Nghệ Thuật Cắt Lát (Slicing)**

---

## 1. Ý tưởng & Phân tích thuật toán
- Bản chất: chuỗi không xóa trực tiếp được nên ghép hai lát cắt bỏ qua vị trí `K`.
- Quy trình:
  - Đọc chuỗi vào `s` và số vào `k`. Với số liệu mẫu, `s = "PYTHON"`, `k = 2` (chữ `T`).
  - Lát trái `s[:2]` là `PY`, lát phải `s[3:]` là `HON` (bỏ qua vị trí 2).
  - Nối `PY + HON` thành `PYHON` rồi in ra.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: PYTHON và 2)
| Bước | Lệnh chạy | Giá trị trong máy | Ghi chú |
|---|---|---|---|
| 1 | `s = input()` | `s = "PYTHON"` | P(0) Y(1) T(2) H(3) O(4) N(5) |
| 2 | `k = int(input())` | `k = 2` | cần xóa chữ T |
| 3 | `s[:k] + s[k + 1:]` | `"PY" + "HON" = "PYHON"` | bỏ đúng vị trí 2 |
| 4 | `print(...)` | màn hình hiện `PYHON` | khớp Output mẫu |

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- Bẫy 1: quên `+ 1` nên không xóa gì `s[:k] + s[k:]`. Đoạn sai:
```python
s = input()
k = int(input())
print(s[:k] + s[k:])
```
Với mẫu `PYTHON` và `2` in ra nguyên `PYTHON`, đáp án đúng là `PYHON`. Cách sửa: lát phải bắt đầu từ `k + 1`.
- Bẫy 2: chỉ in lát trái `print(s[:k])`. Đoạn sai:
```python
s = input()
k = int(input())
print(s[:k])
```
Với mẫu trên chỉ in ra `PY`, thiếu hẳn `HON`, đáp án đúng là `PYHON`. Cách sửa: nối thêm `s[k + 1:]`.

---

## 4. Lời giải tham khảo
```python
s = input()
k = int(input())
print(s[:k] + s[k + 1:])
```
