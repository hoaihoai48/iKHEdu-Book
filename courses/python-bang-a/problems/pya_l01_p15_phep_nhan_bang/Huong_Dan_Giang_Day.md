# Hướng Dẫn Giảng Dạy: In bảng phép nhân cơ bản
Chuyên đề: **Tính Toán Cơ Bản & Nền Tảng Python**

---

## 1. Ý tưởng & Phân tích thuật toán
- Bản chất của bài này là trình bày phép nhân theo đúng khung `A x B = C`: với mẫu `A = 7` và `B = 9` thì `C = 63`, in ra `7 x 9 = 63`. Thầy cô nhắc chữ `x` ở đây là chữ cái, không phải dấu nhân.
- Quy trình gồm ba bước với hai biến `a` và `b` trong lời giải: đọc `7` vào `a` và `9` vào `b` bằng `int(input())`, rồi tính `a * b` tức `63` và dùng chuỗi `f"{a} x {b} = {a * b}"` để đặt ba con số vào đúng vị trí trong khung.
- Xử lý biên: ràng buộc cho `A, B` từ 1 tới 100. Thầy cô cho các con thử cặp biên `1` và `1` cho ra `1 x 1 = 1`, cặp `100` và `100` cho ra `100 x 100 = 10000`.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 7 và 9)
| Bước | Lệnh chạy | Giá trị biến | Màn hình hiện ra |
|------|-----------|--------------|------------------|
| 1 | `a = int(input())` với dòng 1 gõ `7` | `a = 7` | (chưa in gì) |
| 2 | `b = int(input())` với dòng 2 gõ `9` | `b = 9` | (chưa in gì) |
| 3 | `print(f"{a} x {b} = {a * b}")` tức ghép `7`, `9`, `63` vào khung | `a = 7`, `b = 9` | `7 x 9 = 63` |
| 4 | Kết thúc chương trình | — | Kết quả cuối cùng: `7 x 9 = 63`. |

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- Bẫy 1: chỉ in kết quả `print(a * b)` thì với mẫu `7` và `9` màn hình hiện `63` thay vì `7 x 9 = 63`. Cách sửa: in cả khung bằng `print(f"{a} x {b} = {a * b}")`.
- Bẫy 2: dùng dấu `*` trong khung, viết `f"{a} * {b} = {a * b}"` thì với mẫu màn hình hiện `7 * 9 = 63` thay vì `7 x 9 = 63`. Cách sửa: trong khung hiển thị dùng chữ `x` thường.
- Bẫy 3: quên dấu cách quanh chữ `x` và dấu `=`, in ra `7x9=63` dính liền nên bị tính là kết quả sai. Cách sửa: giữ đúng mẫu `{a} x {b} = {kết quả}` với dấu cách hai bên.

---

## 4. Lời giải tham khảo
```python
a = int(input())
b = int(input())
print(f"{a} x {b} = {a * b}")
```
