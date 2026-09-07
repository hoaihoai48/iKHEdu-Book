# Hướng Dẫn Giảng Dạy: Cặp số thân thiết
Chuyên đề: **Đếm Số Theo Quy Luật & Các Con Số Đặc Biệt**

---

## 1. Ý tưởng & Phân tích thuật toán
- Bản chất của bài này: hai số thân thiết là hai số khác nhau mà tổng ước nhỏ hơn của số này bằng số kia, và ngược lại.
- Tính `tong_a` cho `a = 220`: các ước nhỏ hơn `220` gồm `1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110`, tổng đúng bằng `284`.
- Tính `tong_b` cho `b = 284`: các ước nhỏ hơn `284` gồm `1, 2, 4, 71, 142`, tổng đúng bằng `220`.
- Vì `220 != 284`, `tong_a == 284` và `tong_b == 220` nên in `YES`.
- Thầy cô cho các em cộng tay `1 + 2 + 4 + 71 + 142 = 220` để tin vào chiều ngược lại.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 220 284)
| Biến | Tính | Giá trị |
| --- | --- | --- |
| `tong_a` | tổng ước nhỏ hơn `220` | `284` |
| `tong_b` | tổng ước nhỏ hơn `284` (`1 + 2 + 4 + 71 + 142`) | `220` |
| So sánh | `220 != 284`, `284 == 284`, `220 == 220` | cả ba đúng, in `YES` |

Kết quả in ra: `YES`, khớp với kết quả mẫu.

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- Bẫy 1: quên kiểm tra `a != b`. Với cặp `6 6` (số hoàn hảo), tổng ước mỗi bên đều bằng `6` nên làm sai sẽ in `YES`, trong khi đáp án đúng là `NO`. Sửa lại: giữ `a != b` như bài giải.
- Bẫy 2: chỉ kiểm tra một chiều (`tong_a == b`) mà bỏ chiều còn lại. Với cặp `10 20` làm sai có thể kết luận vội, đáp án đúng phải kiểm tra cả hai chiều. Sửa lại: `tong_a == b and tong_b == a`.
- Bẫy 3: cộng cả chính số vào tổng ước. Với mẫu `220 284`, `tong_a` thành `504` nên in nhầm `NO`. Sửa lại: chỉ cộng khi `i < a` và `j < a` (tương tự với `b`) như bài giải.

---

## 4. Lời giải tham khảo
```python
a, b = map(int, input().split())
tong_a = 0
for i in range(1, int(a ** 0.5) + 1):
    if a % i == 0:
        j = a // i
        if i < a:
            tong_a = tong_a + i
        if j != i and j < a:
            tong_a = tong_a + j
tong_b = 0
for i in range(1, int(b ** 0.5) + 1):
    if b % i == 0:
        j = b // i
        if i < b:
            tong_b = tong_b + i
        if j != i and j < b:
            tong_b = tong_b + j
if a != b and tong_a == b and tong_b == a:
    print("YES")
else:
    print("NO")
```
