# Hướng Dẫn Giảng Dạy: Tích Hai Tổng
Chuyên đề: **Tính Toán Cơ Bản & Nền Tảng Python**

---

## 1. Ý tưởng & Phân tích thuật toán

- Bản chất là nhân hai ngoặc: với `a = 5, b = 3, c = 10, d = 6` thì `(5 + 3) * (10 - 6) = 8 * 4 = 32`.
- Quy trình trong lời giải: đọc một dòng `a, b, c, d` rồi in `(a + b) * (c - d)`; ngoặc buộc tính tổng và hiệu trước.
- Xử lý biên: `a + b = 0` thì đáp số `0`; `c - d = 0` thì đáp số `0`; số âm vẫn đúng (ví dụ `-5 3 10 6` cho `-8`).

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 5 3 10 6 (một dòng))

| Bước | Diễn giải | Giá trị |
|------|-----------|---------|
| 1 | Đọc một dòng, tách bốn biến | `a = 5`, `b = 3`, `c = 10`, `d = 6` |
| 2 | Tính `a + b` | `8` |
| 3 | Tính `c - d` | `4` |
| 4 | Nhân và in `8 * 4` | `32` |

---

## 3. Lưu ý & Bẫy lỗi thường gặp

**Bẫy 1: Bỏ ngoặc: `a + b * c - d`.**

```python
print(a + b * c - d)
```

Với số liệu mẫu trên, đoạn này cho `5 3 10 6` cho `29` thay vì `32` vì nhân làm trước.

Cách sửa: giữ ngoặc `(a + b) * (c - d)`.

**Bẫy 2: Nhầm dấu `c + d` thay vì `c - d`.**

```python
print((a + b) * (c + d))
```

Với số liệu mẫu trên, đoạn này cho `5 3 10 6` cho `128` thay vì `32`.

Cách sửa: ngoặc sau là `(c - d)`.

---

## 4. Lời giải tham khảo

```python
a, b, c, d = map(int, input().split())
print((a + b) * (c - d))
```
