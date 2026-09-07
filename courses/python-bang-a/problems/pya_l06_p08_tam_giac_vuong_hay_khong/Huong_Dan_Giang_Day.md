# Hướng Dẫn Giảng Dạy: Tam giác vuông hay không?
Chuyên đề: **Liên Minh Điều Kiện (and - or - not)**

---

## 1. Ý tưởng & Phân tích thuật toán
- Bản chất của bài này là kiểm tra đẳng thức bình phương ba cạnh: `a * a + b * b == c * c` hoặc `a * a + c * c == b * b` hoặc `b * b + c * c == a * a`, đúng một vế là vuông.
- Cách làm của lời giải mẫu: đọc `a, b, c` linh hoạt cả hai kiểu input rồi kiểm tra cả ba vế nối bằng `or`. Với mẫu `3, 4, 5`: `3*3 + 4*4 = 25`, `5*5 = 25`, vế một đúng nên in `VUONG`.
- Xử lý biên: ràng buộc `1 <= a, b, c <= 10^4`, bình phương lên tới `10^8` vẫn vừa số nguyên. Thầy cô cho thử `a = 3, b = 4, c = 6` (`9 + 16 = 25` khác `36`, cả ba vế sai, in `KHONG VUONG`).

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 3 rồi 4 rồi 5)
Sample 1 với input mẫu: `3` rồi `4` rồi `5`.
| Bước | Việc làm | Giá trị các biến | In ra |
|---|---|---|---|
| 1 | Đọc các số | `a = 3, b = 4, c = 5` | — |
| 2 | Tính `3*3 + 4*4 = 25`, `5*5 = 25`; `25 == 25` đúng | cả cụm `or` đúng | — |
| 3 | In kết quả | — | `VUONG` |

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- Bẫy 1 — chỉ kiểm tra một vế: bạn nhỏ viết `if a * a + b * b == c * c`. Với `a = 5, b = 3, c = 4` (cạnh huyền nằm ở `a`) sẽ in `KHONG VUONG`, sai. Cách sửa: giữ đủ ba vế nối bằng `or`.
- Bẫy 2 — dùng căn bậc hai: bạn nhỏ tính `c == (a*a + b*b) ** 0.5` rồi so số thực. Với số lớn dễ lệch dấu chấm động. Cách sửa: so bình phương nguyên như lời giải mẫu.
- Bẫy 3 — quên số mũ: bạn nhỏ viết `a + b == c`. Với mẫu `3, 4, 5` thì `7 == 5` sai nên in `KHONG VUONG`, sai. Cách sửa: nhân mỗi cạnh với chính nó trước khi cộng.

---

## 4. Lời giải tham khảo
```python
dong1 = input().split()
if len(dong1) >= 3:
    a = int(dong1[0])
    b = int(dong1[1])
    c = int(dong1[2])
else:
    a = int(dong1[0])
    b = int(input().split()[0])
    c = int(input().split()[0])
if a * a + b * b == c * c or a * a + c * c == b * b or b * b + c * c == a * a:
    print("VUONG")
else:
    print("KHONG VUONG")
```
