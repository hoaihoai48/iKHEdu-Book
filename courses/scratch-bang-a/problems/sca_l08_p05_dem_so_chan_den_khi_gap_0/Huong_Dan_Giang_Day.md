# Hướng Dẫn Giảng Dạy

## 1. Ý tưởng & Phân tích thuật toán
- Bản chất: vừa đọc tới số 0 thì dừng (như bài đếm số lượng), vừa chỉ đếm những số chia hết cho 2 (`(x mod 2) == 0`). Số 0 dừng vòng lặp không được đếm.
- Quy trình trong lời giải: đặt `count = 0`; `while True` đọc `x`; nếu `x == 0` thì `break`; nếu `(x mod 2) == 0` thì tăng `count`; cuối cùng in `count`.
- Xử lý biên: nếu nhập ngay số 0 thì kết quả là 0; dãy mẫu 4, 7, 8, 12 cho 3 số chẵn.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 4 / 7 / 8 / 12 / 0)
| Lần đọc | Giá trị của `x` | Kiểm tra | `count` sau bước |
|---|---|---|---|
| đầu | — | — | 0 |
| 1 | 4 | chẵn, đếm | 1 |
| 2 | 7 | lẻ, bỏ qua | 1 |
| 3 | 8 | chẵn, đếm | 2 |
| 4 | 12 | chẵn, đếm | 3 |
| 5 | 0 | dừng | 3 |

In ra `3` (các số 4, 8, 12), khớp với kết quả mẫu.

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- Bẫy 1 — kiểm tra chẵn trước khi kiểm tra 0:
```text
count = 0
while True:
    x = câu trả lời
    if (x mod 2) == 0:
        count = count + 1
    if x == 0:
        break
nói (count)

```
Với mẫu `4 / 7 / 8 / 12 / 0` sẽ đếm luôn số 0 (0 chia hết cho 2) nên in ra `4` thay vì `3`. Cách sửa: kiểm tra `if x == 0: break` trước.
- Bẫy 2 — đếm số lẻ:
```text
count = 0
while True:
    x = câu trả lời
    if x == 0:
        break
    if (x mod 2) == 1:
        count = count + 1
nói (count)

```
Với mẫu sẽ in ra `1` (chỉ có số 7) thay vì `3`. Cách sửa: điều kiện đúng là `(x mod 2) == 0`.

---

## 4. Lời giải tham khảo & Kịch bản Khối lệnh Scratch 3.0

### 4.1. Khối lệnh đồ họa trực quan (Visual Scratch Blocks)

![Khối lệnh Scratch 3.0 giải mẫu](solution_blocks_vi.png)

> 💡 **Kịch bản thực hiện từng bước:**
> - khi bấm vào cờ xanh
> - đặt [count] thành (0)
> - lặp lại cho đến khi không còn <điều kiện>:
> -   hỏi [Nhập x:] và đợi
> -   đặt [x] thành (câu trả lời)
> -   nếu <x = 0> thì:
> -     dừng kịch bản này
> -   nếu <x mod 2 = 0> thì:
> -     đặt [count] thành (count + 1)
> - nói (count)
