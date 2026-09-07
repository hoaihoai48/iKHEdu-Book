# Hướng Dẫn Giảng Dạy: Ba cạnh tam giác hợp lệ
Chuyên đề: **Liên Minh Điều Kiện (and - or - not)**

---

## 1. Ý tưởng & Phân tích thuật toán
- Bản chất của bài này là quy tắc tam giác: tổng hai cạnh bất kỳ phải lớn hơn cạnh còn lại, cả ba cặp đều phải đúng.
- Cách làm của lời giải mẫu: đọc `a, b, c` mỗi số một dòng, nếu `a + b > c and a + c > b and b + c > a` thì in `HOP LE`, ngược lại in `KHONG HOP LE`. Với mẫu `3, 4, 5`: `3 + 4 = 7 > 5` đúng, `3 + 5 = 8 > 4` đúng, `4 + 5 = 9 > 3` đúng nên in `HOP LE`.
- Xử lý biên: ràng buộc `1 <= a, b, c <= 10^9`. Thầy cô cho thử `2, 3, 6`: `2 + 3 = 5` không lớn hơn `6` nên in `KHONG HOP LE`.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 3 rồi 4 rồi 5)
Sample 1 với input mẫu: `3` rồi `4` rồi `5`.
| Bước | Việc làm | Giá trị các biến | In ra |
|---|---|---|---|
| 1 | Đọc ba dòng | `a = 3, b = 4, c = 5` | — |
| 2 | Kiểm tra `3 + 4 > 5`? `7 > 5` đúng | tiếp tục | — |
| 3 | Kiểm tra `3 + 5 > 4`? `8 > 4` đúng | tiếp tục | — |
| 4 | Kiểm tra `4 + 5 > 3`? `9 > 3` đúng, cả ba đúng | rẽ nhánh `if` | — |
| 5 | In kết quả | — | `HOP LE` |

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- Bẫy 1 — chỉ kiểm tra một cặp: bạn nhỏ viết `if a + b > c`. Với `2, 3, 6` thì `2 + 3 = 5 > 6` sai nên trùng cờ vẫn đúng, nhưng với `a = 10, b = 2, c = 3` thì `10 + 2 > 3` đúng mà tam giác vẫn sai. Cách sửa: kiểm tra đủ cả ba cặp nối bằng `and`.
- Bẫy 2 — dùng `>=` thay vì `>`: bạn nhỏ viết `a + b >= c`. Với `2, 3, 5` (ba que thẳng hàng) sẽ in `HOP LE`, sai vì tổng phải lớn hơn hẳn. Cách sửa: dùng `>` như lời giải mẫu.
- Bẫy 3 — in sai chữ: bạn nhỏ in `HOPLE` liền nhau. Với mẫu `3, 4, 5`, chương trình kiểm tra sẽ báo kết quả sai. Cách sửa: in đúng `HOP LE` có khoảng trắng ở giữa.

---

## 4. Lời giải tham khảo
```python
a = int(input())
b = int(input())
c = int(input())
if a + b > c and a + c > b and b + c > a:
    print("HOP LE")
else:
    print("KHONG HOP LE")
```
