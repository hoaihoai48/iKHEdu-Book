# Hướng Dẫn Giảng Dạy: Dãy số đan dấu
Chuyên đề: **Quy Luật Dãy Số & Tam Giác Số Kỳ Ảo**

---

## 1. Ý tưởng & Phân tích thuật toán

- Bản chất của bài này là tổng đan dấu `S = 1 - 2 + 3 - 4 + ...`, trong đó số lẻ cộng vào, số chẵn trừ ra.
- Mẹo quan sát: các cặp `(1 - 2), (3 - 4), ...` mỗi cặp bằng `-1`, nên khi `n` chẵn thì đáp án là `-n // 2`, khi `n` lẻ thì đáp án là `(n + 1) // 2`.
- Quy trình từng bước với đúng tên biến trong lời giải:
  - Bước 1: `n = int(input().strip())` đọc `N`. Với mẫu, `n = 5`.
  - Bước 2: kiểm tra `n % 2 == 0`. Vì 5 là số lẻ nên đi vào nhánh `else`.
  - Bước 3: in `(n + 1) // 2 = 6 // 2 = 3`.
- Giá trị biên cụ thể: khi `n = 1` đáp án là `(1 + 1) // 2 = 1`; đề bài cho `N` tới 1000000 nhưng cách này chỉ cần một phép chia.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 5)

| Bước | Việc làm | `n` | `n % 2` | Đi nhánh nào | In ra |
|---|---|---|---|---|---|
| 1 | Đọc dòng `5` | 5 | 1 | — | (chưa in) |
| 2 | Kiểm tra `n % 2 == 0` | 5 | 1 | sai, sang nhánh `else` | (chưa in) |
| 3 | Tính `(5 + 1) // 2` | 5 | 1 | nhánh lẻ | `3` |

- Kiểm tra cộng tay: `1 - 2 + 3 - 4 + 5 = 3`, trùng kết quả mẫu.

---

## 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1: nhầm công thức nhánh chẵn thành `n // 2` (thiếu dấu trừ). Với `n = 6` sẽ ra `3` thay vì `-3`, là kết quả sai. Cách sửa: nhánh chẵn in `-n // 2`.
```python
n = int(input().strip())
if n % 2 == 0:
    print(n // 2)
else:
    print((n + 1) // 2)
```
- Bẫy 2: đảo hai nhánh cho nhau. Với mẫu `n = 5` (lẻ) mà đi vào công thức chẵn `-n // 2` sẽ ra `-3`, là kết quả sai (đáp án đúng là 3). Cách sửa: số chẵn dùng `-n // 2`, số lẻ dùng `(n + 1) // 2`.
```python
n = int(input().strip())
if n % 2 == 0:
    print((n + 1) // 2)
else:
    print(-n // 2)
```
- Bẫy 3: dùng vòng lặp cộng trừ từng số từ 1 tới `N`. Với `N = 1000000` vòng lặp chạy một triệu lần rất chậm trong khi chỉ cần một phép tính theo tính chẵn lẻ. Cách sửa: dùng đúng cách rẽ nhánh theo `n % 2` như lời giải.
```python
n = int(input().strip())
s = 0
for i in range(1, n + 1):
    if i % 2 == 1:
        s = s + i
    else:
        s = s - i
print(s)
```

---

## 4. Lời giải tham khảo

```python
n = int(input().strip())
if n % 2 == 0:
    print(-n // 2)
else:
    print((n + 1) // 2)
```
