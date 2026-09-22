# Hướng Dẫn Giảng Dạy

## 1. Ý tưởng & Phân tích thuật toán
- Bản chất: lật trạng thái từng chữ cái, chữ khác (số, dấu câu, cách) giữ nguyên.
- Quy trình với biến thật (`s`, `kq`, `ch`):
  - Đọc `s = "Hello World 123"`, khởi động `kq = ''`.
  - Duyệt từng `ch`: `H` hoa thành `h`, `e` thường thành `E`, `l` thành `L`... dấu cách giữ nguyên, `1`, `2`, `3` giữ nguyên.
  - Được `kq = "hELLO wORLD 123"` rồi in ra.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: Hello World 123)
| Bước | Lệnh chạy | Giá trị trong máy | Ghi chú |
|---|---|---|---|
| 1 | `s = câu trả lời` | `s = "Hello World 123"` | 15 ký tự |
| 2 | duyệt `Hello` | `kq = "hELLO"` | H lật xuống, còn lại lật lên |
| 3 | duyệt ` World 123` | `kq = "hELLO wORLD 123"` | cách và số giữ nguyên |
| 4 | `nói (kq)` | màn hình hiện `hELLO wORLD 123` | khớp Output mẫu |

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- Bẫy 1: đổi một chiều thành chữ thường hết bằng `lower()`. Đoạn sai:
```text
s = câu trả lời
nói (s.lower())

```
Với mẫu trên in ra `hello world 123`, đáp án đúng là `hELLO wORLD 123`. Cách sửa: lật hai chiều như lời giải.
- Bẫy 2: quên nhánh giữ nguyên nên số và dấu câu bị đưa qua `upper()`. Đoạn sai:
```text
s = câu trả lời
kq = ''
for ch in s:
    if ch.isupper():
        kq = kq + ch.lower()
    else:
        kq = kq + ch.upper()
nói (kq)

```
Với mẫu `Hello World 123` thì số và cách trùng cờ không lỗi, nhưng với câu có ký tự đặc biệt dễ phát sinh kết quả sai khó lường. Cách sửa chắc chắn: giữ nhánh `else: kq = kq + ch` như lời giải để số và dấu câu không bao giờ đổi.

---

## 4. Lời giải tham khảo & Kịch bản Khối lệnh Scratch 3.0

### 4.1. Khối lệnh đồ họa trực quan (Visual Scratch Blocks)

![Khối lệnh Scratch 3.0 giải mẫu](solution_blocks_vi.png)

> 💡 **Kịch bản thực hiện từng bước:**
> - khi bấm vào cờ xanh
> - hỏi [Nhập s:] và đợi
> - đặt [s] thành (câu trả lời)
> - đặt [kq] thành ()
> - đặt [vi_tri] thành 1
> - lặp lại (kích thước của s) lần:
> -   đặt [ch] thành phần tử thứ (vi_tri)
> -   nếu <điều kiện> thì:
> -     đặt [kq] thành (kq + giá trị)
> -   nếu không thì:
> -     nếu <điều kiện> thì:
> -       đặt [kq] thành (kq + giá trị)
> -     nếu không thì:
> -       đặt [kq] thành (kq + ch)
> -   thay đổi [vi_tri] một lượng 1
> - nói (kq)
