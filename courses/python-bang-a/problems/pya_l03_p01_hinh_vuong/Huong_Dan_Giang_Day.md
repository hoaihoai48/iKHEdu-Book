# Hướng Dẫn Giảng Dạy: Chu vi và diện tích hình vuông
Chuyên đề: **Tính Toán Cơ Bản & Nền Tảng Python**

---

## 1. Ý tưởng & Phân tích thuật toán
- Bản chất hình học: hình vuông cạnh `a` có chu vi `4 * a` và diện tích `a * a`, cả hai đều tính từ cùng một số đọc vào.
- Quy trình trong lời giải: đọc biến `a` bằng `int(input())`, rồi in `4 * a` và `a * a` trên cùng một dòng; với mẫu `a = 6` thì chu vi `4 * 6 = 24` và diện tích `6 * 6 = 36`.
- Xử lý biên: `A` nhỏ nhất là 1 cho ra `4 1`, `A` lớn nhất là 10000 cho ra `40000 100000000`, đều là số nguyên vừa khít.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 6)
Với số mẫu `6`, chương trình phải in ra `24 36`.

| Bước | Hành động | Giá trị biến | Kết quả |
|---|---|---|---|
| 1 | Đọc `a = int(input())` | `a = 6` | cạnh bằng 6 |
| 2 | Tính `4 * a` | `4 * 6 = 24` | chu vi 24 |
| 3 | Tính `a * a` | `6 * 6 = 36` | diện tích 36 |
| 4 | In kết quả | xuất `24 36` | khớp kết quả mẫu `24 36` |

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- Bẫy 1 — nhầm công thức chu vi: viết `print(2 * a, a * a)` thì với mẫu in ra `12 36` thay vì `24 36`; cách sửa là nhân chu vi với 4.
- Bẫy 2 — in mỗi thứ một dòng: dùng hai lệnh in riêng thì với mẫu ra hai dòng thay vì một dòng `24 36`; cách sửa là in một lần `print(4 * a, a * a)`.
- Bẫy 3 — quên đổi kiểu: viết `a = input()` thì `4 * a` với mẫu lặp chuỗi cho ra kết quả lạ thay vì `24 36`; cách sửa là bọc `int(input())`.

---

## 4. Lời giải tham khảo
```python
a = int(input())
print(4 * a, a * a)
```
