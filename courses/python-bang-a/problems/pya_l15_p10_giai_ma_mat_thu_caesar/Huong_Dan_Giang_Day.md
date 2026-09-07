# Hướng Dẫn Giảng Dạy: Giải mã mật thư Caesar
Chuyên đề: **Tách Từ & Mật Mã Thay Thế**

---

## 1. Ý tưởng & Phân tích thuật toán
- Bản chất: ngược với mã hóa, kéo mỗi chữ cái lùi lại `K` nấc để tìm thư gốc, hết `A` thì vòng lại `Z`.
- Quy trình với biến thật (`s`, `k`, `res`, `ch`):
  - Đọc bản mật mã `s = "DEFABC"`, `k = 3`.
  - Với từng `ch`, tính `chr((ord(ch) - ord('A') - k) % 26 + ord('A'))`: `D` về `A`, `E` về `B`, `F` về `C`, `A` về `X`, `B` về `Y`, `C` về `Z`.
  - Nối lại được `ABCXYZ` rồi in ra.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: DEFABC và 3)
| Bước | Lệnh chạy | Giá trị trong máy | Ghi chú |
|---|---|---|---|
| 1 | `s`, `k` | `s = "DEFABC"`, `k = 3` | bản mật mã và bước nhảy |
| 2 | `D, E, F` trừ 3 | `A, B, C` | lùi thẳng |
| 3 | `A, B, C` trừ 3 | `X, Y, Z` | vòng lại cuối bảng |
| 4 | `print("".join(res))` | màn hình hiện `ABCXYZ` | khớp Output mẫu |

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- Bẫy 1: dùng công thức mã hóa (cộng `k`) thay vì giải mã. Đoạn sai:
```python
s = input().strip()
k = int(input().strip())
res = []
for ch in s:
    if 'A' <= ch <= 'Z':
        res.append(chr((ord(ch) - ord('A') + k) % 26 + ord('A')))
    else:
        res.append(ch)
print("".join(res))
```
Với mẫu `DEFABC` và `3` in ra `GHIDEF` (mã hóa hai lần), đáp án đúng là `ABCXYZ`. Cách sửa: trừ `k` như lời giải.
- Bẫy 2: trừ trực tiếp `chr(ord(ch) - k)` nên `A, B, C` văng khỏi bảng chữ. Đoạn sai khiến ba chữ cuối thành ký tự lạ thay vì `XYZ`. Cách sửa: vòng lại bằng `% 26` như lời giải.

---

## 4. Lời giải tham khảo
```python
s = input().strip()
k = int(input().strip())
res = []
for ch in s:
    if 'A' <= ch <= 'Z':
        res.append(chr((ord(ch) - ord('A') - k) % 26 + ord('A')))
    else:
        res.append(ch)
print("".join(res))
```
