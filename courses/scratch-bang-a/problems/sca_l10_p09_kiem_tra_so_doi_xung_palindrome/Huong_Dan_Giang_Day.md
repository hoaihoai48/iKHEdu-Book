# Hướng Dẫn Giảng Dạy

## 1. Ý tưởng & Phân tích thuật toán

- Bản chất của bài này là số đối xứng đọc xuôi hay đọc ngược đều giống nhau, nên chỉ cần đảo ngược số rồi so với số gốc.
- Quy trình từng bước với đúng tên biến trong lời giải:
  - Bước 1: `n = int(câu trả lời)` đọc số. Với mẫu, `n = 12321`.
  - Bước 2: giữ lại `orig = n` (số gốc) và đặt `rev = 0` (số đảo đang xây).
  - Bước 3: lặp `while n > 0`, mỗi lần đắp `rev = rev * 10 + (n mod 10)` rồi gọt `n = làm tròn xuống của (n / 10)`.
  - Bước 4: nếu `rev == orig` thì in `YES`, ngược lại in `NO`.
- Giá trị biên cụ thể: với mẫu `12321` đảo thành `12321` nên bằng nhau, in `YES`; số có 1 chữ số như 5 đảo vẫn là 5 nên luôn là số đối xứng.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 12321)

| Lần lặp | `n` trước | Chữ số `(n mod 10)` | `rev` trước | `rev` sau | `n` sau |
|---|---|---|---|---|---|
| Khởi đầu | 12321 | — | 0 | 0 | 12321 |
| 1 | 12321 | 1 | 0 | 1 | 1232 |
| 2 | 1232 | 2 | 1 | 12 | 123 |
| 3 | 123 | 3 | 12 | 123 | 12 |
| 4 | 12 | 2 | 123 | 1232 | 1 |
| 5 | 1 | 1 | 1232 | 12321 | 0 |

- Vòng lặp dừng, so sánh `rev = 12321` với `orig = 12321` bằng nhau nên in `YES`, trùng kết quả mẫu.

---

## 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1: quên giữ số gốc, so sánh `rev == n` sau khi `n` đã bị gọt về 0. Với mẫu sẽ so `12321 == 0` sai nên in `NO`, là kết quả sai. Cách sửa: lưu `orig = n` trước vòng lặp.
```text
n = câu trả lời
rev = 0
while n > 0:
    rev = rev * 10 + (n mod 10)
    n = làm tròn xuống của (n / 10)
if rev == n:
    nói ("YES")
else:
    nói ("NO")

```
- Bẫy 2: quên nhân `rev` với 10, viết `rev = rev + (n mod 10)`. Với mẫu `rev` thành `1 + 2 + 3 + 2 + 1 = 9`, so với `12321` sai nên in `NO`, là kết quả sai. Cách sửa: viết đủ `rev = rev * 10 + (n mod 10)`.
```text
n = câu trả lời
orig = n
rev = 0
while n > 0:
    rev = rev + (n mod 10)
    n = làm tròn xuống của (n / 10)
if rev == orig:
    nói ("YES")
else:
    nói ("NO")

```
- Bẫy 3: in chữ thường `yes`/`no`. Với mẫu sẽ in `yes`, là kết quả sai vì đề bài yêu cầu in hoa `YES`. Cách sửa: in đúng `YES` và `NO`.
```text
n = câu trả lời
orig = n
rev = 0
while n > 0:
    rev = rev * 10 + (n mod 10)
    n = làm tròn xuống của (n / 10)
if rev == orig:
    nói ("yes")
else:
    nói ("no")

```

---

## 4. Lời giải tham khảo & Kịch bản Khối lệnh Scratch 3.0

### 4.1. Khối lệnh đồ họa trực quan (Visual Scratch Blocks)

![Khối lệnh Scratch 3.0 giải mẫu](solution_blocks_vi.png)

> 💡 **Kịch bản thực hiện từng bước:**
> - khi bấm vào cờ xanh
> - hỏi [Nhập n:] và đợi
> - đặt [n] thành (câu trả lời)
> - đặt [orig] thành (n)
> - đặt [rev] thành (0)
> - lặp lại cho đến khi <n = 0>:
> -   đặt [rev] thành (rev * 10 + n mod 10)
> -   đặt [n] thành (n chia nguyên 10)
> - nếu <rev = orig> thì:
> -   nói (YES)
> - nếu không thì:
> -   nói (NO)
