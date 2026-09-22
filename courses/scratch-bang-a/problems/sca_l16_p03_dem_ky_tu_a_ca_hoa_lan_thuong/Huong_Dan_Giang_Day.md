# Hướng Dẫn Giảng Dạy

## 1. Ý tưởng & Phân tích thuật toán
- Bản chất: đếm mọi chữ `A` lẫn `a` trong chuỗi `s`, không phân biệt hoa thường.
- Quy trình với biến thật (`s`, `dem`, `ch`):
  - Đọc `s = "An va Ba hoc bai"`.
  - Khởi động `dem = 0`, duyệt từng `ch`, gặp `A` ở đầu `An` đếm 1, gặp `a` trong `va` đếm 2, `a` trong `Ba` đếm 3, `a` trong `bai` đếm 4.
  - In ra 4.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: An va Ba hoc bai)
| Bước | Lệnh chạy | Giá trị trong máy | Ghi chú |
|---|---|---|---|
| 1 | `s = câu trả lời` | `s = "An va Ba hoc bai"` | 16 ký tự cả cách |
| 2 | duyệt `An` | `dem = 1` | chữ A hoa đầu câu |
| 3 | duyệt `va`, `Ba`, `bai` | `dem = 4` | thêm 3 chữ a thường |
| 4 | `nói (dem)` | màn hình hiện `4` | khớp Output mẫu |

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- Bẫy 1: chỉ đếm chữ thường `if ch == 'a'`. Đoạn sai:
```text
s = câu trả lời
dem = 0
for ch in s:
    if ch == 'a':
        dem = dem + 1
nói (dem)

```
Với mẫu trên sót chữ `A` hoa nên chỉ in ra `3`, đáp án đúng là `4`. Cách sửa: kiểm tra cả hai `if ch == 'a' or ch == 'A'`.
- Bẫy 2: đếm nhầm cả từ chứa `a` bằng `split`. Đoạn sai:
```text
s = câu trả lời
nói (len([w for w in s.split() if 'a' in w.lower()]))

```
Với mẫu trên có 4 từ chứa `a` (`An`, `va`, `Ba`, `bai`) nên trùng cờ ra `4`, nhưng câu như `aaa bb` sẽ ra `1` thay vì `3`. Cách sửa: duyệt từng ký tự `for ch in s`.

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
> -   nếu <điều kiện> thì:
> -     đặt [dem] thành (dem + 1)
> -   thay đổi [vi_tri] một lượng 1
> - nói (dem)
