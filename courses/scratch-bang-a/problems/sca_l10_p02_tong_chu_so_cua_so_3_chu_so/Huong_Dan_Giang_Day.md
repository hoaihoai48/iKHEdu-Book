# Hướng Dẫn Giảng Dạy

## 1. Ý tưởng & Phân tích thuật toán

- Bản chất của bài này là gọt từng chữ số từ phải sang trái bằng phép chia lấy dư rồi cộng dồn vào giỏ tổng.
- Quy trình từng bước với đúng tên biến trong lời giải:
  - Bước 1: `n = câu trả lời` đọc số. Với mẫu, `n = 358`.
  - Bước 2: đặt `tong = 0`.
  - Bước 3: lặp `while n > 0`, mỗi lần cộng `(n mod 10)` (chữ số cuối) vào `tong` rồi gọt `n = làm tròn xuống của (n / 10)`.
  - Bước 4: in `tong`.
- Giá trị biên cụ thể: số nhỏ nhất 100 có tổng `1 + 0 + 0 = 1`, số lớn nhất 999 có tổng `9 + 9 + 9 = 27`.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 358)

| Lần lặp | `n` trước | Chữ số `(n mod 10)` | `tong` trước | `tong` sau | `n` sau (`làm tròn xuống của (n / 10)`) |
|---|---|---|---|---|---|
| Khởi đầu | 358 | — | 0 | 0 | 358 |
| 1 | 358 | 8 | 0 | 8 | 35 |
| 2 | 35 | 5 | 8 | 13 | 3 |
| 3 | 3 | 3 | 13 | 16 | 0 |

- Vòng lặp dừng vì `n = 0`, in ra `16`, trùng kết quả mẫu (`3 + 5 + 8 = 16`).

---

## 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1: quên gọt `n` trong vòng lặp, `n` mãi bằng 358 nên lặp vô tận. Cách sửa: cuối mỗi lần lặp phải `n = làm tròn xuống của (n / 10)`.
```text
n = câu trả lời
tong = 0
while n > 0:
    tong = tong + (n mod 10)
nói (tong)

```
- Bẫy 2: đặt `tong = 1` thay vì `tong = 0`, tổng dư 1. Với mẫu sẽ ra `17`, là kết quả sai. Cách sửa: khởi đầu `tong = 0`.
```text
n = câu trả lời
tong = 1
while n > 0:
    tong = tong + (n mod 10)
    n = làm tròn xuống của (n / 10)
nói (tong)

```
- Bẫy 3: cộng cả số `n` thay vì chữ số cuối, viết `tong = tong + n`. Với mẫu lần đầu `tong = 358`, kết quả sai hẳn. Cách sửa: chỉ cộng `(n mod 10)`.
```text
n = câu trả lời
tong = 0
while n > 0:
    tong = tong + n
    n = làm tròn xuống của (n / 10)
nói (tong)

```

---

## 4. Lời giải tham khảo & Kịch bản Khối lệnh Scratch 3.0

### 4.1. Khối lệnh đồ họa trực quan (Visual Scratch Blocks)

![Khối lệnh Scratch 3.0 giải mẫu](solution_blocks_vi.png)

> 💡 **Kịch bản thực hiện từng bước:**
> - khi bấm vào cờ xanh
> - hỏi [Nhập n:] và đợi
> - đặt [n] thành (câu trả lời)
> - đặt [tong] thành (0)
> - lặp lại cho đến khi <n = 0>:
> -   đặt [tong] thành (tong + n mod 10)
> -   đặt [n] thành (n chia nguyên 10)
> - nói (tong)
