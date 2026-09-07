# Hướng Dẫn Giảng Dạy: Tính tiền mua sơn quét tường
Chuyên đề: **Tính Toán Cơ Bản & Nền Tảng Python**

---

## 1. Ý tưởng & Phân tích thuật toán
- Bản chất tiền sơn: diện tích tường `a * h` trừ cửa sổ `x * y`, rồi nhân đơn giá `g` một mét vuông.
- Quy trình trong lời giải: đọc một dòng rồi tách thành `a, h, x, y, g`, đặt `s_son = (a * h) - (x * y)` rồi in `s_son * g`; với mẫu `6 3 2 1 50000` thì tường `6 * 3 = 18`, cửa sổ `2 * 1 = 2`, cần sơn `18 - 2 = 16`, tiền `16 * 50000 = 800000`.
- Xử lý biên: đề cho cửa sổ nhỏ hơn tường nên diện tích cần sơn luôn dương; `G` tới 100000.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 6 3 2 1 50000)
Với số mẫu một dòng `6 3 2 1 50000`, chương trình phải in ra `800000`.

| Bước | Hành động | Giá trị biến | Kết quả |
|---|---|---|---|
| 1 | Đọc `a, h, x, y, g` | `a = 6`, `h = 3`, `x = 2`, `y = 1`, `g = 50000` | đủ năm số |
| 2 | Tính `a * h` | `6 * 3 = 18` | diện tích tường 18 |
| 3 | Tính `x * y` | `2 * 1 = 2` | diện tích cửa sổ 2 |
| 4 | Tính `(18 - 2) * 50000` | `16 * 50000 = 800000` | khớp kết quả mẫu `800000` |

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- Bẫy 1 — cộng cửa sổ: viết `(a * h + x * y) * g` thì với mẫu ra `1000000` thay vì `800000`; cách sửa là lấy tường trừ cửa sổ.
- Bẫy 2 — quên nhân đơn giá: viết `print((a * h) - (x * y))` thì với mẫu ra `16` thay vì `800000`; cách sửa là nhân thêm `g`.
- Bẫy 3 — đọc năm dòng riêng: dùng năm lần `input()` thì với mẫu một dòng sẽ bị treo chờ; cách sửa là tách một dòng bằng `split()`.

---

## 4. Lời giải tham khảo
```python
a, h, x, y, g = map(int, input().split())
s_son = (a * h) - (x * y)
print(s_son * g)
```
