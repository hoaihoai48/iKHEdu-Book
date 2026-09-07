# Hướng Dẫn Giảng Dạy: Hoán đổi nửa đầu nửa sau
Chuyên đề: **Chỉ Số Indexing & Nghệ Thuật Cắt Lát (Slicing)**

---

## 1. Ý tưởng & Phân tích thuật toán
- Bản chất: đổi chỗ nửa đầu và nửa sau của chuỗi dài chẵn.
- Quy trình:
  - Đọc chuỗi vào `s`. Với số liệu mẫu, `s = "ABCDEF"` dài 6 ký tự.
  - Tính điểm giữa `n = len(s) // 2` được 3. Nửa đầu `s[:3]` là `ABC`, nửa sau `s[3:]` là `DEF`.
  - Nối ngược `DEF + ABC` thành `DEFABC` rồi in ra.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: ABCDEF)
| Bước | Lệnh chạy | Giá trị trong máy | Ghi chú |
|---|---|---|---|
| 1 | `s = input()` | `s = "ABCDEF"` | dài 6 |
| 2 | `n = len(s) // 2` | `n = 3` | `ABC` và `DEF` |
| 3 | `s[n:] + s[:n]` | `"DEFABC"` | nửa sau lên trước |
| 4 | `print(...)` | màn hình hiện `DEFABC` | khớp Output mẫu |

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- Bẫy 1: nối đúng thứ tự cũ `s[:n] + s[n:]`. Đoạn sai:
```python
s = input()
n = len(s) // 2
print(s[:n] + s[n:])
```
Với mẫu `ABCDEF` in ra nguyên `ABCDEF`, đáp án đúng là `DEFABC`. Cách sửa: đặt `s[n:]` trước.
- Bẫy 2: tính điểm giữa sai thành `n = len(s) // 2 + 1`. Đoạn sai:
```python
s = input()
n = len(s) // 2 + 1
print(s[n:] + s[:n])
```
Với mẫu `ABCDEF` (n = 4) in ra `EFABCD`, đáp án đúng là `DEFABC`. Cách sửa: giữ `n = len(s) // 2`.

---

## 4. Lời giải tham khảo
```python
s = input()
n = len(s) // 2
print(s[n:] + s[:n])
```
