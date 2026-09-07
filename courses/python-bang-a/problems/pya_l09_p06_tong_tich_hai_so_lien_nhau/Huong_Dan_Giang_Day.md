# Hướng Dẫn Giảng Dạy: Tổng tích hai số liền nhau
Chuyên đề: **Quy Luật Dãy Số & Tam Giác Số Kỳ Ảo**

---

## 1. Ý tưởng & Phân tích thuật toán

- Bản chất của bài này là cộng dồn từng cụm `i * (i + 1)` với `i` chạy từ 1 tới `N`: `S = 1*2 + 2*3 + ... + N*(N+1)`.
- Quy trình từng bước với đúng tên biến trong lời giải:
  - Bước 1: `n = int(input().strip())` đọc `N`. Với mẫu, `n = 3`.
  - Bước 2: đặt `s = 0` làm giỏ đựng tổng.
  - Bước 3: vòng lặp `for i in range(1, n + 1)` cho `i` lần lượt là 1, 2, 3; mỗi lần cộng `i * (i + 1)` vào `s`.
  - Bước 4: `print(s)` in tổng cuối.
- Giá trị biên cụ thể: khi `n = 1` thì tổng chỉ có một cụm `1*2 = 2`; đề bài cho `N` tới 100000 nên vòng lặp chạy nhiều nhất 100000 lần.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 3)

| Lần lặp | `i` | Cụm `i * (i + 1)` | `s` trước khi cộng | `s` sau khi cộng |
|---|---|---|---|---|
| Khởi đầu | — | — | 0 | 0 |
| 1 | 1 | `1 * 2 = 2` | 0 | 2 |
| 2 | 2 | `2 * 3 = 6` | 2 | 8 |
| 3 | 3 | `3 * 4 = 12` | 8 | 20 |

- Lệnh `print(s)` in ra `20`, trùng kết quả mẫu (`2 + 6 + 12 = 20`).

---

## 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1: viết cụm sai thành `i * i`, bỏ mất `+ 1`. Với mẫu `n = 3` sẽ tính `1 + 4 + 9 = 14`, là kết quả sai. Cách sửa: viết đủ `i * (i + 1)`.
```python
n = int(input().strip())
s = 0
for i in range(1, n + 1):
    s += i * i
print(s)
```
- Bẫy 2: vòng lặp dừng sớm ở `range(1, n)`, bỏ mất cụm cuối. Với mẫu `n = 3` chỉ cộng `2 + 6 = 8`, là kết quả sai. Cách sửa: dùng `range(1, n + 1)`.
```python
n = int(input().strip())
s = 0
for i in range(1, n):
    s += i * (i + 1)
print(s)
```
- Bẫy 3: quên đặt `s = 0` trước vòng lặp mà đặt `s = 1`, tổng sẽ dư 1. Với mẫu sẽ ra `21`, là kết quả sai. Cách sửa: khởi đầu `s = 0`.
```python
n = int(input().strip())
s = 1
for i in range(1, n + 1):
    s += i * (i + 1)
print(s)
```

---

## 4. Lời giải tham khảo

```python
n = int(input().strip())
s = 0
for i in range(1, n + 1):
    s += i * (i + 1)
print(s)
```
