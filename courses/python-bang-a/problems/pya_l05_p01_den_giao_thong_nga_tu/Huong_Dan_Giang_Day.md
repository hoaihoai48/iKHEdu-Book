# Hướng Dẫn Giảng Dạy: Đèn giao thông ngã tư
Chuyên đề: **Lựa Chọn Nhiều Hướng (if - elif - else)**

---

## 1. Ý tưởng & Phân tích thuật toán
- Bản chất của bài này là tra bảng màu đèn: `den` sau khi viết hoa mà là `D` thì `DUNG LAI`, là `V` thì `DI CHAM`, là `X` thì `DUOC DI`.
- Cách làm của lời giải mẫu: đọc `den = input().strip().upper()` rồi rẽ ba nhánh, mỗi nhánh còn nhận thêm cách viết chữ đầy đủ (`DO`, `VANG`, `XANH`). Với mẫu `do`: viết hoa thành `DO`, rơi vào nhánh một nên in `DUNG LAI`.
- Xử lý biên: input chỉ quanh quẩn `D, V, X` và các cách viết `do, vang, xanh` chữ thường. Thầy cô cho thử `XANH` (in `DUOC DI`) và `v` (in `DI CHAM`).

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: do)
Sample 1 với input mẫu: `do`.
| Bước | Việc làm | Giá trị của `den` | In ra |
|---|---|---|---|
| 1 | Đọc input, cắt khoảng trắng, viết hoa | `den = 'DO'` | — |
| 2 | Kiểm tra `den == 'D' or den == 'DO'`? `DO == DO` đúng | rẽ nhánh một | — |
| 3 | In theo nhánh | — | `DUNG LAI` |

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- Bẫy 1 — quên viết hoa: bạn nhỏ viết `den = input().strip()` rồi so với `'D'`. Với mẫu `do` chữ thường sẽ không khớp nhánh nào, không in gì. Cách sửa: thêm `.upper()` như lời giải mẫu.
- Bẫy 2 — so bằng `in` sai cách: bạn nhỏ viết `if den in 'DO'` rồi tưởng đúng. Với `den = 'O'` cũng lọt vào nhánh, sai. Cách sửa: so bằng `==` từng giá trị như lời giải mẫu.
- Bẫy 3 — in sai chữ: bạn nhỏ in `DUNG LAI ` thừa khoảng trắng cuối. Với mẫu `do`, chương trình kiểm tra sẽ báo kết quả sai. Cách sửa: chép đúng `DUNG LAI`, `DI CHAM`, `DUOC DI`.

---

## 4. Lời giải tham khảo
```python
den = input().strip().upper()
if den == "D" or den == "DO":
    print("DUNG LAI")
elif den == "V" or den == "VANG":
    print("DI CHAM")
elif den == "X" or den == "XANH":
    print("DUOC DI")
```
