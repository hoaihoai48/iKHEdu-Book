# Hướng Dẫn Giảng Dạy: Kiểm tra số chính phương
Chuyên đề: **Ước Số, Bội Số & Số Nguyên Tố Cơ Bản**

---

## 1. Ý tưởng & Phân tích thuật toán
- Bản chất của bài này: số chính phương là số mà căn bậc hai của nó là số tự nhiên; `25 = 5 * 5` nên đáp án là `YES`.
- Chương trình đoán `r = int(25 ** 0.5) = 5`, rồi hiệu chỉnh lên xuống hai vòng lặp để `r` thành căn nguyên chính xác của `25`.
- Vì `5 * 5 == 25` nên điều kiện `r * r == n` đúng và in `YES`.
- Hai vòng hiệu chỉnh giúp tránh sai số của phép tính căn với số lớn tới `10^9`.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 25)
| Bước | `r` | Kiểm tra | Ghi chú |
| --- | --- | --- | --- |
| Đoán đầu | 5 | `int(25 ** 0.5)` | |
| Hiệu chỉnh lên | 5 | `(5 + 1) * (5 + 1) = 36 > 25` | không tăng |
| Hiệu chỉnh xuống | 5 | `5 * 5 = 25`, không lớn hơn `25` | không giảm |
| So sánh | 5 | `5 * 5 == 25` đúng | in `YES` |

Kết quả in ra: `YES`, khớp với kết quả mẫu.

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- Bẫy 1: so sánh số thực trực tiếp:
```python
import math
if math.sqrt(25) == int(math.sqrt(25)):
    print("YES")
```
với số lớn tới `10^9` phép căn có thể lệch một chút ở phần thập phân, cho kết quả sai. Sửa lại: hiệu chỉnh `r` rồi so `r * r == n` như bài giải.
- Bẫy 2: quên hiệu chỉnh, chỉ lấy `r = int(n ** 0.5)`. Với một số mẫu lớn, `r` có thể lệch 1 đơn vị và kết luận sai. Sửa lại: giữ nguyên hai vòng lặp hiệu chỉnh của bài giải.
- Bẫy 3: in `True`/`False` thay vì `YES`/`NO`. Với mẫu `25` sẽ in `True`, chương trình kiểm tra không chấp nhận. Sửa lại: `print("YES")` và `print("NO")`.

---

## 4. Lời giải tham khảo
```python
n = int(input())
r = int(n ** 0.5)
while (r + 1) * (r + 1) <= n:
    r = r + 1
while r * r > n:
    r = r - 1
if r * r == n:
    print("YES")
else:
    print("NO")
```
