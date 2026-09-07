# Hướng Dẫn Giảng Dạy: Tách Chữ Số Tận Cùng
Chuyên đề: **Cỗ Máy Tính Toán & Bí Thuật Chia Dư**

---

## 1. Ý tưởng & Phân tích thuật toán

- Bản chất là tách hai hàng thấp nhất: với `n = 857` thì hàng đơn vị `857 % 10 = 7`, hàng chục `857 // 10 % 10 = 85 % 10 = 5`.
- Quy trình trong lời giải: đọc `n`, in `n % 10` ở dòng 1 rồi in `n // 10 % 10` ở dòng 2.
- Xử lý biên: `n = 10` cho `0` rồi `1`; `n = 10^9 = 1000000000` cho `0` rồi `0`; `n = 99` cho `9` rồi `9`.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 857)

| Bước | Diễn giải | Giá trị |
|------|-----------|---------|
| 1 | Đọc một dòng, biến `n` nhận giá trị | `n = 857` |
| 2 | Tính đơn vị `n % 10` và in dòng 1 | `7` |
| 3 | Tính `n // 10 = 85` | `85` |
| 4 | Tính `85 % 10` và in dòng 2 | `5` |

---

## 3. Lưu ý & Bẫy lỗi thường gặp

**Bẫy 1: In hai số trên một dòng.**

```python
print(n % 10, n // 10 % 10)
```

Với số liệu mẫu trên, đoạn này cho `857` in ra `7 5` một dòng thay vì hai dòng `7` rồi `5`.

Cách sửa: dùng hai lệnh `print` riêng.

**Bẫy 2: Hoán đổi thứ tự hai dòng.**

```python
print(n // 10 % 10)
print(n % 10)
```

Với số liệu mẫu trên, đoạn này cho `857` in ra `5` rồi `7`, ngược yêu cầu (đơn vị trước, chục sau).

Cách sửa: in `n % 10` trước.

---

## 4. Lời giải tham khảo

```python
n = int(input())
print(n % 10)
print(n // 10 % 10)
```
