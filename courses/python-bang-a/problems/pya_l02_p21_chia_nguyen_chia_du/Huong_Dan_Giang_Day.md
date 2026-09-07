# Hướng Dẫn Giảng Dạy: Chia Nguyên Và Chia Dư
Chuyên đề: **Tính Toán Cơ Bản & Nền Tảng Python**

---

## 1. Ý tưởng & Phân tích thuật toán

- Bản chất là in đồng thời thương và dư: với `a = 17`, `b = 5` thì `17 // 5 = 3` và `17 % 5 = 2`.
- Quy trình trong lời giải: đọc một dòng `a, b` rồi in một dòng `print(a // b, a % b)` cho ra `3 2`.
- Xử lý biên: `b = a` (ví dụ `7 7`) cho `1 0`; `b = 1` thì dư luôn `0`; `a = 10^9, b = 10^9` cho `1 0`.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 17 5 (một dòng))

| Bước | Diễn giải | Giá trị |
|------|-----------|---------|
| 1 | Đọc một dòng, tách `a` và `b` | `a = 17`, `b = 5` |
| 2 | Tính `a // b` | `17 // 5 = 3` |
| 3 | Tính `a % b` | `17 % 5 = 2` |
| 4 | In một dòng | `3 2` |

---

## 3. Lưu ý & Bẫy lỗi thường gặp

**Bẫy 1: Dùng chia thực `/` cho thương.**

```python
print(a / b, a % b)
```

Với số liệu mẫu trên, đoạn này cho `17 5` in ra `3.4 2` thay vì `3 2`.

Cách sửa: dùng `a // b`.

**Bẫy 2: Hoán đổi `b // a`.**

```python
print(b // a, b % a)
```

Với số liệu mẫu trên, đoạn này cho `17 5` cho `0 5` thay vì `3 2`.

Cách sửa: số bị chia `a` đứng trước.

---

## 4. Lời giải tham khảo

```python
a, b = map(int, input().split())
print(a // b, a % b)
```
