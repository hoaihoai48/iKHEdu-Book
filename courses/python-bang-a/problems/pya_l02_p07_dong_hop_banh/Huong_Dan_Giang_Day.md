# Hướng Dẫn Giảng Dạy: Đóng Hộp Bánh
Chuyên đề: **Tính Toán Cơ Bản & Nền Tảng Python**

---

## 1. Ý tưởng & Phân tích thuật toán

- Bản chất là đóng hộp 6 chiếc: với `m = 50` thì số hộp đầy `50 // 6 = 8`, bánh lẻ `50 % 6 = 2`.
- Quy trình trong lời giải: đọc `m` rồi in một dòng `print(m // 6, m % 6)` cho ra `8 2`.
- Xử lý biên: `m = 1` cho `0 1`; `m = 6` cho `1 0`; `m = 10^6` cho `166666 4`.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 50)

| Bước | Diễn giải | Giá trị |
|------|-----------|---------|
| 1 | Đọc một dòng, biến `m` nhận giá trị | `m = 50` |
| 2 | Tính số hộp `m // 6` | `50 // 6 = 8` |
| 3 | Tính bánh lẻ `m % 6` | `50 % 6 = 2` |
| 4 | In một dòng hai số | `8 2` |

---

## 3. Lưu ý & Bẫy lỗi thường gặp

**Bẫy 1: In hai số xuống hai dòng.**

```python
print(m // 6)
print(m % 6)
```

Với số liệu mẫu trên, đoạn này cho `50` in ra `8` rồi `2` xuống hai dòng thay vì `8 2` một dòng.

Cách sửa: in chung một lệnh `print(m // 6, m % 6)`.

**Bẫy 2: Nhầm số bánh mỗi hộp thành `5`.**

```python
print(m // 5, m % 5)
```

Với số liệu mẫu trên, đoạn này cho `50` in ra `10 0` thay vì `8 2`.

Cách sửa: mỗi hộp đúng `6` chiếc.

---

## 4. Lời giải tham khảo

```python
m = int(input())
print(m // 6, m % 6)
```
