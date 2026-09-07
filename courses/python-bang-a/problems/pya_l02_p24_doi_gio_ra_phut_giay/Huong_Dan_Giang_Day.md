# Hướng Dẫn Giảng Dạy: Đổi Giờ Ra Phút Giây
Chuyên đề: **Cỗ Máy Tính Toán & Bí Thuật Chia Dư**

---

## 1. Ý tưởng & Phân tích thuật toán

- Bản chất là đổi từng đơn vị ra giây rồi cộng: với `h = 1`, `m = 20`, `s = 15` thì `1 * 3600 + 20 * 60 + 15 = 3600 + 1200 + 15 = 4815` giây.
- Quy trình trong lời giải: đọc `h`, `m`, `s` mỗi số một dòng rồi in `h * 3600 + m * 60 + s`.
- Xử lý biên: `0 0 0` cho `0`; `23 59 59` cho `86399`; `0 1 0` cho `60`.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 1, 20, 15 (ba dòng))

| Bước | Diễn giải | Giá trị |
|------|-----------|---------|
| 1 | Đọc ba dòng vào `h`, `m`, `s` | `h = 1`, `m = 20`, `s = 15` |
| 2 | Tính `h * 3600` | `3600` |
| 3 | Tính `m * 60` rồi cộng | `3600 + 1200 = 4800` |
| 4 | Cộng `s` và in | `4800 + 15 = 4815` |

---

## 3. Lưu ý & Bẫy lỗi thường gặp

**Bẫy 1: Nhầm một giờ là `360` giây.**

```python
print(h * 360 + m * 60 + s)
```

Với số liệu mẫu trên, đoạn này cho `1 20 15` cho `1575` thay vì `4815`.

Cách sửa: một giờ là `3600` giây.

**Bẫy 2: Nhầm một phút là `100` giây.**

```python
print(h * 3600 + m * 100 + s)
```

Với số liệu mẫu trên, đoạn này cho `1 20 15` cho `5615` thay vì `4815`.

Cách sửa: một phút là `60` giây.

---

## 4. Lời giải tham khảo

```python
h = int(input())
m = int(input())
s = int(input())
print(h * 3600 + m * 60 + s)
```
