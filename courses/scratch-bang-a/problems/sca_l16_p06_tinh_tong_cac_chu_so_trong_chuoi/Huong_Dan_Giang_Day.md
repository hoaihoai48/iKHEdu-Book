# Hướng Dẫn Giảng Dạy

## 1. Ý tưởng & Phân tích thuật toán
- Bản chất: nhặt từng ký tự là số trong chuỗi `s` rồi cộng dồn vào `tong`.
- Quy trình với biến thật (`s`, `tong`, `ch`):
  - Đọc `s = "A1B2C3D4"`.
  - Khởi động `tong = 0`, duyệt từng `ch`: gặp `1` cộng thành 1, `2` thành 3, `3` thành 6, `4` thành 10; các chữ `A, B, C, D` bỏ qua.
  - In ra 10 (đúng là 1 + 2 + 3 + 4).

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: A1B2C3D4)
| Bước | Lệnh chạy | Giá trị trong máy | Ghi chú |
|---|---|---|---|
| 1 | `s = câu trả lời` | `s = "A1B2C3D4"` | 4 chữ và 4 số |
| 2 | duyệt `1`, `2` | `tong` từ 0 thành 3 | A, B bị bỏ qua |
| 3 | duyệt `3`, `4` | `tong` từ 3 thành 10 | C, D bị bỏ qua |
| 4 | `nói (tong)` | màn hình hiện `10` | khớp Output mẫu |

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- Bẫy 1: cộng trực tiếp ký tự mà quên đổi sang số. Đoạn sai:
```text
s = câu trả lời
tong = 0
for ch in s:
    if ch.isdigit():
        tong = tong + ch
nói (tong)

```
Với mẫu trên chương trình báo lỗi vì không cộng số với chữ được, đáp án đúng là `10`. Cách sửa: đổi sang số `tong = tong + int(ch)`.
- Bẫy 2: đếm số lượng chữ số thay vì cộng giá trị. Đoạn sai:
```text
s = câu trả lời
tong = 0
for ch in s:
    if ch.isdigit():
        tong = tong + 1
nói (tong)

```
Với mẫu trên in ra `4` (có 4 chữ số), đáp án đúng là `10`. Cách sửa: cộng giá trị `int(ch)`.

---

## 4. Lời giải tham khảo & Kịch bản Khối lệnh Scratch 3.0

### 4.1. Khối lệnh đồ họa trực quan (Visual Scratch Blocks)

![Khối lệnh Scratch 3.0 giải mẫu](solution_blocks_vi.png)

> 💡 **Kịch bản thực hiện từng bước:**
> - khi bấm vào cờ xanh
> - hỏi [Nhập s:] và đợi
> - đặt [s] thành (câu trả lời)
> - đặt [tong] thành (0)
> - đặt [vi_tri] thành 1
> - lặp lại (kích thước của s) lần:
> -   đặt [ch] thành phần tử thứ (vi_tri)
> -   nếu <điều kiện> thì:
> -     đặt [tong] thành (tong + int(...))
> -   thay đổi [vi_tri] một lượng 1
> - nói (tong)
