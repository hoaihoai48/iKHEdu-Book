# Hướng Dẫn Giảng Dạy

## 1. Ý tưởng & Phân tích thuật toán
- Bản chất: giúp bạn An nhặt hết các chữ số theo đúng thứ tự, nếu không có số nào thì báo `KHONG CO`.
- Quy trình với biến thật (`s`, `kq`, `ch`):
  - Đọc `s = "Toi sinh nam 2014 vao thang 08"`, khởi động `kq = ''`.
  - Duyệt từng `ch`, gặp số thì nối vào `kq`: nhặt `2, 0, 1, 4` thành `2014`, rồi `0, 8` thành `201408`.
  - `kq` khác rỗng nên in `201408`.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: Toi sinh nam 2014 vao thang 08)
| Bước | Lệnh chạy | Giá trị trong máy | Ghi chú |
|---|---|---|---|
| 1 | `s = câu trả lời` | cả câu mẫu dài | lẫn 6 chữ số |
| 2 | duyệt tới `2014` | `kq = "2014"` | chữ bỏ qua, số giữ lại |
| 3 | duyệt tới `08` | `kq = "201408"` | nối tiếp theo thứ tự |
| 4 | `kq != ''` nên in `kq` | màn hình hiện `201408` | khớp Output mẫu |

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- Bẫy 1: in `kq` mà quên trường hợp không có số. Đoạn sai:
```text
s = câu trả lời
kq = ''
for ch in s:
    if ch.isdigit():
        kq = kq + ch
nói (kq)

```
Với câu không có số nào sẽ in ra dòng trắng, đáp án đúng phải là `KHONG CO`. Cách sửa: kiểm tra `if kq == '': nói ('KHONG CO')`.
- Bẫy 2: nối số bằng phép cộng số học. Đoạn sai:
```text
s = câu trả lời
kq = 0
for ch in s:
    if ch.isdigit():
        kq = kq * 10 + int(ch)
nói (kq)

```
Với mẫu trên số 0 ở đầu `08` bị nuốt mất, in ra `20148`, đáp án đúng là `201408`. Cách sửa: nối chuỗi `kq = kq + ch`.

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
> -     đặt [kq] thành (kq + ch)
> -   thay đổi [vi_tri] một lượng 1
> - nếu <kq = > thì:
> -   nói (KHONG CO)
> - nếu không thì:
> -   nói (kq)
