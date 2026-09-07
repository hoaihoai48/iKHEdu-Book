# Hướng Dẫn Giảng Dạy: Đổi Phút Ra Giờ Phút
Chuyên đề: **Cỗ Máy Tính Toán & Bí Thuật Chia Dư**

---

## 1. Ý tưởng & Phân tích thuật toán

- Bản chất là tách giờ và phút lẻ khỏi tổng phút: với `t = 135` thì giờ `135 // 60 = 2`, phút dư `135 % 60 = 15`.
- Quy trình trong lời giải: đọc `t` rồi in một dòng `print(t // 60, t % 60)` cho ra `2 15`.
- Xử lý biên: `t = 0` cho `0 0`; `t = 60` cho `1 0`; `t = 10000` cho `166 40`.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 135)

| Bước | Diễn giải | Giá trị |
|------|-----------|---------|
| 1 | Đọc một dòng, biến `t` nhận giá trị | `t = 135` |
| 2 | Tính giờ `t // 60` | `135 // 60 = 2` |
| 3 | Tính phút dư `t % 60` | `135 % 60 = 15` |
| 4 | In một dòng | `2 15` |

---

## 3. Lưu ý & Bẫy lỗi thường gặp

**Bẫy 1: Chia cho `100` thay vì `60`.**

```python
print(t // 100, t % 100)
```

Với số liệu mẫu trên, đoạn này cho `135` cho `1 35` thay vì `2 15`.

Cách sửa: một giờ có `60` phút.

**Bẫy 2: Dùng chia thực `/`.**

```python
print(t / 60, t % 60)
```

Với số liệu mẫu trên, đoạn này cho `135` in ra `2.25 15` thay vì `2 15`.

Cách sửa: dùng `//`.

---

## 4. Lời giải tham khảo

```python
t = int(input())
print(t // 60, t % 60)
```
