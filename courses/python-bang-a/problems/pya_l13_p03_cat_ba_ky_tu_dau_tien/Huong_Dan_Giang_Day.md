# Hướng Dẫn Giảng Dạy: Cắt ba ký tự đầu tiên
Chuyên đề: **Chỉ Số Indexing & Nghệ Thuật Cắt Lát (Slicing)**

---

## 1. Ý tưởng & Phân tích thuật toán
- Bản chất: lấy 3 chữ cái đầu tiên của chuỗi `s`.
- Quy trình:
  - Đọc chuỗi vào biến `s`. Với số liệu mẫu, `s = "VIETNAM"` (độ dài 7).
  - Cắt lát `s[:3]` nghĩa là lấy các vị trí 0, 1, 2, tức là `V`, `I`, `E`.
  - In ra `VIE` bằng `print(s[:3])`.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: VIETNAM)
| Bước | Lệnh chạy | Giá trị trong máy | Ghi chú |
|---|---|---|---|
| 1 | `s = input()` | `s = "VIETNAM"` | vị trí 0 là V, 1 là I, 2 là E |
| 2 | `s[:3]` | `"VIE"` | lấy đúng 3 ký tự đầu |
| 3 | `print(s[:3])` | màn hình hiện `VIE` | khớp Output mẫu |

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- Bẫy 1: cắt thiếu thành `s[:2]`. Đoạn sai:
```python
s = input()
print(s[:2])
```
Với mẫu `VIETNAM` chỉ in ra `VI`, thiếu chữ `E`, đáp án đúng là `VIE`. Cách sửa: dùng `s[:3]`.
- Bẫy 2: in ký tự ở vị trí 3 là `print(s[3])`. Đoạn sai:
```python
s = input()
print(s[3])
```
Với mẫu `VIETNAM` in ra `T` (vị trí 3), đáp án đúng là `VIE`. Cách sửa: dùng lát cắt `s[:3]`.

---

## 4. Lời giải tham khảo
```python
s = input()
print(s[:3])
```
