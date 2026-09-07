# Hướng Dẫn Giảng Dạy: Giá Trị Biểu Thức PEMDAS
Chuyên đề: **Cỗ Máy Tính Toán & Bí Thuật Chia Dư**

---

## 1. Ý tưởng & Phân tích thuật toán

- Bản chất là thứ tự ưu tiên mũ rồi nhân rồi cộng: với `a = 2`, `b = 3`, `c = 4` thì `c ** 2 = 16`, `b * 16 = 48`, `2 + 48 = 50`.
- Quy trình trong lời giải: đọc `a`, `b`, `c` mỗi số một dòng rồi in `a + b * c ** 2`; Python tự tính `**` trước, `*` sau, `+` cuối.
- Xử lý biên: `a = b = c = 1` cho `2`; `a = b = c = 100` cho `1000100`; số nào cũng dương theo ràng buộc.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 2, 3, 4 (ba dòng))

| Bước | Diễn giải | Giá trị |
|------|-----------|---------|
| 1 | Đọc ba dòng vào `a`, `b`, `c` | `a = 2`, `b = 3`, `c = 4` |
| 2 | Tính `c ** 2` | `4 ** 2 = 16` |
| 3 | Tính `b * 16` | `3 * 16 = 48` |
| 4 | Tính `a + 48` và in | `50` |

---

## 3. Lưu ý & Bẫy lỗi thường gặp

**Bẫy 1: Thêm ngoặc sai `(a + b) * c ** 2`.**

```python
print((a + b) * c ** 2)
```

Với số liệu mẫu trên, đoạn này cho `2, 3, 4` cho `80` thay vì `50`.

Cách sửa: viết `a + b * c ** 2`.

**Bẫy 2: Viết `(a + b * c) ** 2`.**

```python
print((a + b * c) ** 2)
```

Với số liệu mẫu trên, đoạn này cho `2, 3, 4` cho `196` thay vì `50`.

Cách sửa: chỉ mũ áp vào `c`.

---

## 4. Lời giải tham khảo

```python
a = int(input())
b = int(input())
c = int(input())
print(a + b * c ** 2)
```
