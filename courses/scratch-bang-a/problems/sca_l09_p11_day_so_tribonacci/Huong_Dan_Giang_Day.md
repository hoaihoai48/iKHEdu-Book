# Hướng Dẫn Giảng Dạy

## 1. Ý tưởng & Phân tích thuật toán

- Bản chất của bài này giống dãy Fibonacci nhưng mỗi số bằng tổng ba số liền trước: `T1 = 1, T2 = 1, T3 = 2`, từ số thứ 4 trở đi `Tn = T(n-1) + T(n-2) + T(n-3)`.
- Quy trình từng bước với đúng tên biến trong lời giải:
  - Bước 1: `n = int(câu trả lời)` đọc vị trí cần tìm. Với mẫu, `n = 5`.
  - Bước 2: đặt `a, b, c = 1, 1, 2` tượng trưng cho `T1, T2, T3`.
  - Bước 3: vì `n = 5` lớn hơn 3 nên lặp `n - 3 = 2` lần, mỗi lần trượt `a, b, c = b, c, a + b + c`.
  - Bước 4: in `c`.
- Giá trị biên cụ thể: khi `n = 1` hoặc `n = 2` in `1`, khi `n = 3` in `2`; đề bài giới hạn `1 <= N <= 35` nên không lo số quá lớn.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 5)

| Lần lặp | `a` trước | `b` trước | `c` trước | Tổng `a + b + c` | Bộ ba sau lặp |
|---|---|---|---|---|---|
| Khởi đầu | 1 | 1 | 2 | — | (1, 1, 2) |
| 1 | 1 | 1 | 2 | `1 + 1 + 2 = 4` | (1, 2, 4) |
| 2 | 1 | 2 | 4 | `1 + 2 + 4 = 7` | (2, 4, 7) |

- Sau 2 lần lặp thì `c = 7`, lệnh `nói (c)` in ra `7`, trùng kết quả mẫu. Dãy viết ra là 1, 1, 2, 4, 7 nên số thứ 5 đúng là 7.

---

## 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1: lặp đúng `n` lần thay vì `n - 3` lần. Với mẫu `n = 5` sẽ lặp 5 lần và `c` vượt xa 7, là kết quả sai. Cách sửa: dùng `range(n - 3)`.
```text
n = câu trả lời
a, b, c = 1, 1, 2
if n == 1 or n == 2:
    nói (1)
elif n == 3:
    nói (2)
else:
    for _ in range(n):
        a, b, c = b, c, a + b + c
    nói (c)

```
- Bẫy 2: quên xử lý riêng `n = 1, 2, 3` mà cho chạy vòng lặp ngay. Với `n = 1` thì `range(-2)` rỗng và in `c = 2`, là kết quả sai (đáp án đúng là 1). Cách sửa: rẽ nhánh như lời giải.
```text
n = câu trả lời
a, b, c = 1, 1, 2
for _ in range(n - 3):
    a, b, c = b, c, a + b + c
nói (c)

```
- Bẫy 3: công thức thiếu một số hạng, viết `a, b, c = b, c, b + c`. Với mẫu lần lặp 1 cho `c = 3` thay vì 4, kết quả cuối sai. Cách sửa: cộng đủ ba số `a + b + c`.
```text
n = câu trả lời
a, b, c = 1, 1, 2
if n == 1 or n == 2:
    nói (1)
elif n == 3:
    nói (2)
else:
    for _ in range(n - 3):
        a, b, c = b, c, b + c
    nói (c)

```

---

## 4. Lời giải tham khảo & Kịch bản Khối lệnh Scratch 3.0

### 4.1. Khối lệnh đồ họa trực quan (Visual Scratch Blocks)

![Khối lệnh Scratch 3.0 giải mẫu](solution_blocks_vi.png)

> 💡 **Kịch bản thực hiện từng bước:**
> - khi bấm vào cờ xanh
> - hỏi [Nhập n:] và đợi
> - đặt [n] thành (câu trả lời)
> - đặt [a] thành (1)
> - đặt [b] thành (1)
> - đặt [c] thành (2)
> - nếu <điều kiện> thì:
> -   nói (1)
> - nếu không thì:
> -   nếu <n = 3> thì:
> -     nói (2)
> -   nếu không thì:
> -     đặt [_] thành (0)
> -     lặp lại (n - 3) lần:
> -       đặt [a] thành (b)
> -       đặt [b] thành (c)
> -       đặt [c] thành (a + b + c)
> -       thay đổi [_] một lượng 1
> -     nói (c)
