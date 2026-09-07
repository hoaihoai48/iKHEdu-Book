# Hướng Dẫn Giảng Dạy: Mảnh vườn chữ nhật
Chuyên đề: **Toán Học & Hình Học Đời Thường**

---

## 1. Ý tưởng & Phân tích thuật toán
- Bản chất mảnh vườn chữ nhật: chu vi `(a + b) * 2` và diện tích `a * b`, cả hai tính từ dài `a` và rộng `b`.
- Quy trình trong lời giải: đọc `a` dòng 1 và `b` dòng 2, đặt `chu_vi = (a + b) * 2` và `dien_tich = a * b`; với mẫu `a = 10` và `b = 6` thì chu vi `(10 + 6) * 2 = 32` và diện tích `10 * 6 = 60`.
- Xử lý biên: đề cho `b` không vượt quá `a` và cả hai tới 10000, chu vi lớn nhất là 40000, diện tích lớn nhất là 100000000.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 10\n6)
Với số mẫu dòng 1 là `10` và dòng 2 là `6`, chương trình phải in ra `32 60`.

| Bước | Hành động | Giá trị biến | Kết quả |
|---|---|---|---|
| 1 | Đọc `a` | `a = 10` | dài 10 |
| 2 | Đọc `b` | `b = 6` | rộng 6 |
| 3 | Tính `(a + b) * 2` | `(10 + 6) * 2 = 32` | chu vi 32 |
| 4 | Tính `a * b` | `10 * 6 = 60` | diện tích 60, xuất `32 60` khớp mẫu |

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- Bẫy 1 — thiếu ngoặc: viết `a + b * 2` thì với mẫu ra `10 + 12 = 22` thay vì `32`; cách sửa là `(a + b) * 2`.
- Bẫy 2 — đọc hai số một dòng: viết `a, b = map(int, input().split())` thì với mẫu mỗi số một dòng sẽ bị lỗi; cách sửa là đọc hai lần riêng.
- Bẫy 3 — in hai dòng: dùng hai lệnh in thì với mẫu ra hai dòng thay vì một dòng `32 60`; cách sửa là `print(chu_vi, dien_tich)`.

---

## 4. Lời giải tham khảo
```python
a = int(input())
b = int(input())
chu_vi = (a + b) * 2
dien_tich = a * b
print(chu_vi, dien_tich)
```
