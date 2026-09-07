# Hướng Dẫn Giảng Dạy: Hai Chữ Số Tận Cùng
Chuyên đề: **Tính Toán Cơ Bản & Nền Tảng Python**

---

## 1. Ý tưởng & Phân tích thuật toán

- Bản chất là lấy khối 2 chữ số cuối bằng dư cho `100`: với `n = 1945` thì `1945 % 100 = 45`.
- Quy trình trong lời giải: đọc `n` rồi in `n % 100`; ví dụ `105 % 100 = 5` nên số `105` in ra `5`.
- Xử lý biên: `n = 100` cho `0`; `n = 10^9 = 1000000000` cho `0`; `n = 2026` cho `26`.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 1945)

| Bước | Diễn giải | Giá trị |
|------|-----------|---------|
| 1 | Đọc một dòng, biến `n` nhận giá trị | `n = 1945` |
| 2 | Tính `n % 100` | `1945 % 100 = 45` |
| 3 | In kết quả | `45` |

---

## 3. Lưu ý & Bẫy lỗi thường gặp

**Bẫy 1: Dùng `% 10` chỉ lấy một chữ số.**

```python
print(n % 10)
```

Với số liệu mẫu trên, đoạn này cho `1945` in ra `5` thay vì `45`.

Cách sửa: dùng `n % 100`.

**Bẫy 2: Dùng `n // 100` (lấy phần đầu).**

```python
print(n // 100)
```

Với số liệu mẫu trên, đoạn này cho `1945` in ra `19` thay vì `45`.

Cách sửa: dùng `n % 100`.

---

## 4. Lời giải tham khảo

```python
n = int(input())
print(n % 100)
```
