# Hướng Dẫn Giảng Dạy: Rút thăm đến khi trúng
Chuyên đề: **Lập Trình Thuật Toán & Khối Lệnh Scratch 3.0**

---

## 1. Ý tưởng & Phân tích thuật toán
- Bản chất: đọc liên tục không biết trước số lượng, dừng ngay khi bốc trúng lá phiếu số 7. Vòng lặp `while True` đọc từng `x` và `break` khi gặp 7.
- Quy trình trong lời giải: `while True` đọc `x`; nếu `x == 7` (lời giải còn chấp nhận thêm 77 cho chắc) thì `break`; sau vòng lặp in đúng một dòng `DA TRUNG THUONG!`.
- Xử lý biên: nếu lá đầu tiên đã là 7 thì in ngay; dãy mẫu 10, 25, 7 thì dừng ở lá thứ ba.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 10 / 25 / 7)
| Lần đọc | Giá trị của `x` | `x == 7`? | Hành động |
|---|---|---|---|
| 1 | 10 | không | đọc tiếp |
| 2 | 25 | không | đọc tiếp |
| 3 | 7 | có | dừng vòng lặp |

Sau vòng lặp in ra `DA TRUNG THUONG!`, khớp với kết quả mẫu.

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- Bẫy 1 — in thông báo trong vòng lặp:
```text
while True:
    x = int(câu trả lời.strip())
    if x == 7:
        print("DA TRUNG THUONG!")
print("DA TRUNG THUONG!")
```
Với mẫu `10 / 25 / 7` vòng lặp không dừng nên chương trình treo luôn. Cách sửa: dùng `break` khi gặp 7 và chỉ in một lần sau vòng lặp.
- Bẫy 2 — sai chữ in (thường hoặc có dấu):
```text
while True:
    x = int(câu trả lời.strip())
    if x == 7:
        break
print("Da trung thuong!")
```
Với mẫu `10 / 25 / 7` sẽ in `Da trung thuong!` khác chữ mẫu nên chương trình kiểm tra báo kết quả sai. Cách sửa: in đúng chữ in hoa `DA TRUNG THUONG!`.

---

## 4. Lời giải tham khảo & Kịch bản Khối lệnh Scratch 3.0

### 4.1. Khối lệnh đồ họa trực quan (Visual Scratch Blocks)

![Khối lệnh Scratch 3.0 giải mẫu](solution_blocks_vi.png)

> 💡 **Kịch bản thực hiện từng bước:**
> - khi bấm vào cờ xanh
> - hỏi [Nhập x:] và đợi
> - đặt [x] thành (câu trả lời)
> - đặt [dem] thành (0)
> - lặp lại cho đến khi <n = 0>:
> -   thay đổi [dem] một lượng (1)
> -   đặt [n] thành (làm tròn xuống của n / 10)
> - nói (dem)
