# Hướng Dẫn Giảng Dạy

## 1. Ý tưởng & Phân tích thuật toán
- Bản chất: đo độ an toàn mật khẩu bằng cách đếm riêng chữ hoa và chữ thường, bỏ qua dấu cách.
- Quy trình với biến thật (`s`, `hoa`, `thuong`, `ch`):
  - Đọc `s = "Lap Trinh Python"`, khởi động `hoa = 0`, `thuong = 0`.
  - Duyệt từng `ch`: `L` hoa thành 1, `a`, `p` thường thành 2, dấu cách bỏ qua, `T` hoa thành 2, `P` hoa thành 3... hết chuỗi được `hoa = 3` (`L`, `T`, `P`), `thuong = 11`.
  - In `3 11`.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: Lap Trinh Python)
| Bước | Lệnh chạy | Giá trị trong máy | Ghi chú |
|---|---|---|---|
| 1 | `s = câu trả lời` | `s = "Lap Trinh Python"` | 16 ký tự cả 2 cách |
| 2 | duyệt `Lap` | `hoa = 1`, `thuong = 2` | L hoa, a p thường |
| 3 | duyệt hết chuỗi | `hoa = 3`, `thuong = 11` | thêm T, P và 9 thường |
| 4 | `nói (...)` | màn hình hiện `3 11` | khớp Output mẫu |

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- Bẫy 1: dùng hai nhánh `if` độc lập kèm `else` nên đếm sai. Đoạn sai:
```text
s = câu trả lời
hoa = 0
thuong = 0
for ch in s:
    if ch.isupper():
        hoa = hoa + 1
    if ch.islower():
        thuong = thuong + 1
    else:
        thuong = thuong + 1
nói (str(hoa) + ' ' + str(thuong))

```
Với mẫu trên dấu cách và chữ hoa cũng bị cộng vào `thuong`, in ra số lớn hơn `11`, đáp án đúng là `3 11`. Cách sửa: dùng `if ... elif ...` như lời giải.
- Bẫy 2: in hai số trên hai dòng. Đoạn sai:
```text
s = câu trả lời
hoa = 0
thuong = 0
for ch in s:
    if ch.isupper():
        hoa = hoa + 1
    elif ch.islower():
        thuong = thuong + 1
nói (hoa)
nói (thuong)

```
Với mẫu trên in `3` rồi `11` xuống hai dòng, đáp án đúng là một dòng `3 11`. Cách sửa: in chung `nói (str(hoa) + ' ' + str(thuong))`.

---

## 4. Lời giải tham khảo & Kịch bản Khối lệnh Scratch 3.0

### 4.1. Khối lệnh đồ họa trực quan (Visual Scratch Blocks)

![Khối lệnh Scratch 3.0 giải mẫu](solution_blocks_vi.png)

> 💡 **Kịch bản thực hiện từng bước:**
> - khi bấm vào cờ xanh
> - hỏi [Nhập s:] và đợi
> - đặt [s] thành (câu trả lời)
> - đặt [hoa] thành (0)
> - đặt [thuong] thành (0)
> - đặt [vi_tri] thành 1
> - lặp lại (kích thước của s) lần:
> -   đặt [ch] thành phần tử thứ (vi_tri)
> -   nếu <điều kiện> thì:
> -     đặt [hoa] thành (hoa + 1)
> -   nếu không thì:
> -     nếu <điều kiện> thì:
> -       đặt [thuong] thành (thuong + 1)
> -   thay đổi [vi_tri] một lượng 1
> - nói (str(...) +   + str(...))
