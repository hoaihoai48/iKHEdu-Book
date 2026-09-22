# Hướng Dẫn Giảng Dạy

## 1. Ý tưởng & Phân tích thuật toán
- Bản chất: nguyên âm gồm 5 chữ `A, E, I, O, U` tính cả hoa lẫn thường; đi đếm từng chữ trong chuỗi `s`.
- Quy trình với biến thật (`s`, `dem`, `ch`):
  - Đọc `s = "EDUCATION"` (9 chữ cái).
  - Khởi động `dem = 0`, duyệt từng `ch`: `E` đếm, `D` bỏ, `U` đếm, `C` bỏ, `A` đếm, `T` bỏ, `I` đếm, `O` đếm, `N` bỏ.
  - `dem` tăng 5 lần thành 5 rồi in ra 5.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: EDUCATION)
| Bước | Lệnh chạy | Giá trị trong máy | Ghi chú |
|---|---|---|---|
| 1 | `s = câu trả lời` | `s = "EDUCATION"` | 9 chữ cái |
| 2 | duyệt E, D, U, C, A | `dem` từ 0 thành 3 | E, U, A là nguyên âm |
| 3 | duyệt T, I, O, N | `dem` từ 3 thành 5 | thêm I, O |
| 4 | `nói (dem)` | màn hình hiện `5` | khớp Output mẫu |

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- Bẫy 1: chỉ kiểm tra nguyên âm thường nên sót chữ hoa. Đoạn sai:
```text
s = câu trả lời
dem = 0
for ch in s:
    if ch in 'aeiou':
        dem = dem + 1
nói (dem)

```
Với mẫu `EDUCATION` toàn chữ hoa nên `dem` vẫn là `0`, đáp án đúng là `5`. Cách sửa: kiểm tra cả hai dạng `'AEIOUaeiou'`.
- Bẫy 2: in `dem` bên trong vòng lặp. Đoạn sai:
```text
s = câu trả lời
dem = 0
for ch in s:
    if ch in 'AEIOUaeiou':
        dem = dem + 1
    nói (dem)

```
Với mẫu trên in ra 9 dòng `1, 1, 2, 2, 3...`, đáp án đúng chỉ là một dòng `5`. Cách sửa: đưa `nói (dem)` ra ngoài vòng lặp.

---

## 4. Lời giải tham khảo & Kịch bản Khối lệnh Scratch 3.0

### 4.1. Khối lệnh đồ họa trực quan (Visual Scratch Blocks)

![Khối lệnh Scratch 3.0 giải mẫu](solution_blocks_vi.png)

> 💡 **Kịch bản thực hiện từng bước:**
> - khi bấm vào cờ xanh
> - hỏi [Nhập s:] và đợi
> - đặt [s] thành (câu trả lời)
> - đặt [dem] thành (0)
> - đặt [vi_tri] thành 1
> - lặp lại (kích thước của s) lần:
> -   đặt [ch] thành phần tử thứ (vi_tri)
> -   nếu <ch = AEIOUaeiou> thì:
> -     đặt [dem] thành (dem + 1)
> -   thay đổi [vi_tri] một lượng 1
> - nói (dem)
