# Hướng Dẫn Giảng Dạy: Rút trích tên miền email
Chuyên đề: **Chỉ Số Indexing & Nghệ Thuật Cắt Lát (Slicing)**

---

## 1. Ý tưởng & Phân tích thuật toán
- Bản chất: phần tên miền là đoạn đứng sau ký tự `@` trong chuỗi `s`.
- Quy trình:
  - Đọc địa chỉ vào biến `s`. Với số liệu mẫu, `s = "hocsinh@ikhedu.vn"`, ký tự `@` nằm ở vị trí 7.
  - Tìm vị trí `@` bằng `s.index('@')` được 7, cộng 1 thành 8 là điểm bắt đầu của tên miền.
  - Cắt `s[8:]` được `ikhedu.vn` rồi in ra.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: hocsinh@ikhedu.vn)
| Bước | Lệnh chạy | Giá trị trong máy | Ghi chú |
|---|---|---|---|
| 1 | `s = input()` | `s = "hocsinh@ikhedu.vn"` | `@` ở vị trí 7 |
| 2 | `s.index('@') + 1` | `8` | điểm bắt đầu tên miền |
| 3 | `s[8:]` rồi in | màn hình hiện `ikhedu.vn` | khớp Output mẫu |

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- Bẫy 1: quên cộng 1 nên lấy dính cả `@`. Đoạn sai:
```python
s = input()
print(s[s.index('@'):])
```
Với mẫu `hocsinh@ikhedu.vn` in ra `@ikhedu.vn`, đáp án đúng là `ikhedu.vn`. Cách sửa: cộng 1 `s[s.index('@') + 1:]`.
- Bẫy 2: tách rồi lấy nhầm nửa đầu `s.split('@')[0]`. Đoạn sai:
```python
s = input()
print(s.split('@')[0])
```
Với mẫu `hocsinh@ikhedu.vn` in ra `hocsinh`, đáp án đúng là `ikhedu.vn`. Cách sửa: lấy nửa sau `s.split('@')[1]`.

---

## 4. Lời giải tham khảo
```python
s = input()
print(s[s.index('@') + 1:])
```
