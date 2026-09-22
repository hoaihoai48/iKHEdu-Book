# Hướng Dẫn Giảng Dạy

## 1. Ý tưởng & Phân tích thuật toán

- Bản chất của bài này là liệt kê các số chia hết cho 3 hoặc chia hết cho 5 theo thứ tự tăng dần: 3, 5, 6, 9, 10, 12, 15, ... và lấy `N` số đầu.
- Quy trình từng bước với đúng tên biến trong lời giải:
  - Bước 1: `n = int(câu trả lời)` đọc số lượng cần lấy. Với mẫu, `n = 6`.
  - Bước 2: đặt `res = []` đựng kết quả và `num = 1` là số đang xét.
  - Bước 3: lặp `while len(res) < n`, mỗi lần kiểm tra `if (num mod 3) == 0 or (num mod 5) == 0` thì thêm `str(num)` vào `res`, rồi tăng `num` thêm 1.
  - Bước 4: in `" ".join(res)`.
- Giá trị biên cụ thể: với mẫu `n = 6` thì `num` xét tới 12 là đủ 6 số; đề bài cho `N` tới 10000 nên vòng lặp xét tới số khoảng hơn hai vạn.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 6)

| `num` | `(num mod 3) == 0` | `(num mod 5) == 0` | Có thêm vào `res` không | `res` sau bước này |
|---|---|---|---|---|
| 1 | sai | sai | không | [] |
| 2 | sai | sai | không | [] |
| 3 | đúng | sai | có | [`3`] |
| 4 | sai | sai | không | [`3`] |
| 5 | sai | đúng | có | [`3`, `5`] |
| 6 | đúng | sai | có | [`3`, `5`, `6`] |
| 7 | sai | sai | không | [`3`, `5`, `6`] |
| 8 | sai | sai | không | [`3`, `5`, `6`] |
| 9 | đúng | sai | có | [`3`, `5`, `6`, `9`] |
| 10 | sai | đúng | có | [`3`, `5`, `6`, `9`, `10`] |
| 11 | sai | sai | không | [`3`, `5`, `6`, `9`, `10`] |
| 12 | đúng | sai | có | [`3`, `5`, `6`, `9`, `10`, `12`] |

- Đủ 6 số thì dừng, in ra `3 5 6 9 10 12`, trùng kết quả mẫu.

---

## 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1: dùng `and` thay vì `or`, chỉ giữ số vừa chia hết cho 3 vừa chia hết cho 5. Với mẫu `n = 6` sẽ ra `15 30 45 60 75 90`, là kết quả sai. Cách sửa: dùng `or`.
```text
n = câu trả lời
res = []
num = 1
while len(res) < n:
    if (num mod 3) == 0 and (num mod 5) == 0:
        res.append(str(num))
    num += 1
nói (" ".join(res))

```
- Bẫy 2: quên tăng `num` trong vòng lặp, chương trình chạy mãi không dừng ở `num = 1`. Cách sửa: cuối mỗi lần lặp phải `num += 1`.
```text
n = câu trả lời
res = []
num = 1
while len(res) < n:
    if (num mod 3) == 0 or (num mod 5) == 0:
        res.append(str(num))
nói (" ".join(res))

```
- Bẫy 3: thêm `num` (số nguyên) vào `res` rồi `" ".join(res)` sẽ báo lỗi vì `join` cần chuỗi. Với mẫu sẽ dừng vì lỗi trước khi in. Cách sửa: thêm `str(num)`.
```text
n = câu trả lời
res = []
num = 1
while len(res) < n:
    if (num mod 3) == 0 or (num mod 5) == 0:
        res.append(num)
    num += 1
nói (" ".join(res))

```

---

## 4. Lời giải tham khảo & Kịch bản Khối lệnh Scratch 3.0

### 4.1. Khối lệnh đồ họa trực quan (Visual Scratch Blocks)

![Khối lệnh Scratch 3.0 giải mẫu](solution_blocks_vi.png)

> 💡 **Kịch bản thực hiện từng bước:**
> - khi bấm vào cờ xanh
> - hỏi [Nhập n:] và đợi
> - đặt [n] thành (câu trả lời)
> - xóa tất cả của [res]
> - đặt [num] thành (1)
> - lặp lại cho đến khi không còn <độ dài của res < n>:
> -   nếu <điều kiện> thì:
> -     thêm (str(...)) vào [res]
> -   thay đổi [num] một lượng (1)
> - nói (res)
