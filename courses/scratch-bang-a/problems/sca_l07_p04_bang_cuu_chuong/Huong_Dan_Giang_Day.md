# Hướng Dẫn Giảng Dạy

## 1. Ý tưởng & Phân tích thuật toán
- Bản chất: in 10 dòng bảng nhân của số K, dòng thứ `i` có dạng `K x i = K*i`. Vòng lặp cho `i` chạy từ 1 tới 10.
- Quy trình trong lời giải: đọc `n`, vòng lặp `for i in range(1, 11)`, mỗi lượt `nói (f"{n} x {i} = {n * i}")` tự tính tích `n * i`.
- Xử lý biên: với K nhỏ nhất là 1 thì dòng cuối là `1 x 10 = 10`; với K lớn nhất là 9 thì dòng cuối là `9 x 10 = 90`.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 5)
| Lượt lặp | Giá trị của `i` | Tích `5 * i` | Dòng in ra |
|---|---|---|---|
| 1 | 1 | 5 | 5 x 1 = 5 |
| 2 | 2 | 10 | 5 x 2 = 10 |
| 3 | 3 | 15 | 5 x 3 = 15 |
| 4 | 4 | 20 | 5 x 4 = 20 |
| 5 | 5 | 25 | 5 x 5 = 25 |
| 6 | 6 | 30 | 5 x 6 = 30 |
| 7 | 7 | 35 | 5 x 7 = 35 |
| 8 | 8 | 40 | 5 x 8 = 40 |
| 9 | 9 | 45 | 5 x 9 = 45 |
| 10 | 10 | 50 | 5 x 10 = 50 |

Đủ 10 dòng như kết quả mẫu.

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- Bẫy 1 — dùng `range(1, 10)`:
```text
n = câu trả lời
for i in range(1, 10):
    nói (f"{n} x {i} = {n * i}")

```
Với mẫu `5` chỉ in 9 dòng, thiếu dòng `5 x 10 = 50`. Cách sửa: dùng `range(1, 11)`.
- Bẫy 2 — sai định dạng khoảng trắng:
```text
n = câu trả lời
for i in range(1, 11):
    nói (f"{n}x{i}={n * i}")

```
Với mẫu `5` dòng đầu thành `5x1=5` thay vì `5 x 1 = 5`, chương trình kiểm tra báo kết quả sai. Cách sửa: giữ đúng mẫu `f"{n} x {i} = {n * i}"`.

---

## 4. Lời giải tham khảo & Kịch bản Khối lệnh Scratch 3.0

### 4.1. Khối lệnh đồ họa trực quan (Visual Scratch Blocks)

![Khối lệnh Scratch 3.0 giải mẫu](solution_blocks_vi.png)

> 💡 **Kịch bản thực hiện từng bước:**
> - khi bấm vào cờ xanh
> - hỏi [Nhập n:] và đợi
> - đặt [n] thành (câu trả lời)
> - đặt [i] thành (1)
> - lặp lại (11 - 1) lần:
> -   nói (giá trị)
> -   thay đổi [i] một lượng 1
