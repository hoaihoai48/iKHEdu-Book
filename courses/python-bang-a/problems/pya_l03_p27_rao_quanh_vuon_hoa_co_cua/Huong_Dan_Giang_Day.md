# Hướng Dẫn Giảng Dạy: Rào quanh vườn hoa có cửa
Chuyên đề: **Toán Học & Hình Học Đời Thường**

---

## 1. Ý tưởng & Phân tích thuật toán
- Bản chất tiền rào: chu vi vườn `(a + b) * 2` trừ cửa `c` rồi nhân đơn giá 15 nghìn một mét.
- Quy trình trong lời giải: đọc `a`, `b`, `c` mỗi biến một dòng, rồi in `((a + b) * 2 - c) * 15`; với mẫu `a = 12`, `b = 8`, `c = 2` thì chu vi `(12 + 8) * 2 = 40`, rào `40 - 2 = 38`, tiền `38 * 15 = 570`.
- Xử lý biên: `a` và `b` tới 10000, `c` nhỏ hơn chu vi nên độ dài rào luôn dương.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 12\n8\n2)
Với số mẫu ba dòng `12`, `8`, `2`, chương trình phải in ra `570`.

| Bước | Hành động | Giá trị biến | Kết quả |
|---|---|---|---|
| 1 | Đọc `a`, `b`, `c` | `a = 12`, `b = 8`, `c = 2` | đủ ba số |
| 2 | Tính `(a + b) * 2` | `(12 + 8) * 2 = 40` | chu vi 40 |
| 3 | Tính `(40 - 2) * 15` | `38 * 15 = 570` | khớp kết quả mẫu `570` |

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- Bẫy 1 — quên trừ cửa: viết `print((a + b) * 2 * 15)` thì với mẫu ra `600` thay vì `570`; cách sửa là trừ `c` trước khi nhân 15.
- Bẫy 2 — quên nhân đơn giá: viết `print((a + b) * 2 - c)` thì với mẫu ra `38` thay vì `570`; cách sửa là nhân thêm 15.
- Bẫy 3 — đọc ba số một dòng: viết `a, b, c = map(int, input().split())` thì với mẫu mỗi số một dòng sẽ bị lỗi; cách sửa là đọc ba lần riêng.

---

## 4. Lời giải tham khảo
```python
a = int(input())
b = int(input())
c = int(input())
print(((a + b) * 2 - c) * 15)
```
