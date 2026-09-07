# Hướng Dẫn Giảng Dạy: Phân tích ra thừa số nguyên tố
Chuyên đề: **Ước Số, Bội Số & Số Nguyên Tố Cơ Bản**

---

## 1. Ý tưởng & Phân tích thuật toán
- Bản chất của bài này: chia dần `temp = 60` cho các ước `d = 2, 3, ...`, mỗi lần chia hết thì ghi `d` vào danh sách `thua_so`.
- Vòng lặp ngoài chạy khi `d * d <= temp`; vòng lặp trong chia hết cỡ cho cùng một `d` nên thừa số lặp lại được giữ đủ (số `2` xuất hiện hai lần).
- Với `60`: chia cho `2` hai lần còn `15`, chia cho `3` một lần còn `5`, số `5` còn lại lớn hơn `1` nên được ghi nốt.
- Danh sách cuối là `["2", "2", "3", "5"]`, nối bằng `" * "` thành `2 * 2 * 3 * 5`.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 60)
| `d` | `temp` trước | Diễn biến | `thua_so` sau |
| --- | --- | --- | --- |
| 2 | 60 | `60 % 2 == 0`, ghi 2, còn 30 | `["2"]` |
| 2 | 30 | `30 % 2 == 0`, ghi 2, còn 15 | `["2", "2"]` |
| 2 | 15 | `15 % 2 != 0`, tăng `d` | không đổi |
| 3 | 15 | `15 % 3 == 0`, ghi 3, còn 5 | `["2", "2", "3"]` |
| 4 | 5 | `4 * 4 = 16 > 5`, dừng | không đổi |
| còn lại | 5 | `5 > 1`, ghi nốt 5 | `["2", "2", "3", "5"]` |

Kết quả in ra: `2 * 2 * 3 * 5`, khớp với kết quả mẫu.

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- Bẫy 1: mỗi `d` chỉ chia một lần (thiếu vòng lặp trong). Với mẫu `60` thì `d = 2` chỉ ghi một lần, còn `30` trôi tiếp và ra `2 * 3 * 5`, thiếu một số `2`. Sửa lại: giữ vòng lặp `while temp % d == 0` như bài giải.
- Bẫy 2: quên ghi phần còn lại `temp > 1`. Với mẫu `60` số `5` cuối bị mất, chỉ in `2 * 2 * 3`. Sửa lại: giữ khối `if temp > 1` ở cuối.
- Bẫy 3: nối bằng `"*"` không có khoảng trắng. Với mẫu `60` sẽ in `2*2*3*5`, chương trình kiểm tra không chấp nhận. Sửa lại: `" * ".join(thua_so)`.

---

## 4. Lời giải tham khảo
```python
n = int(input())
thua_so = []
temp = n
d = 2
while d * d <= temp:
    while temp % d == 0:
        thua_so.append(str(d))
        temp = temp // d
    d = d + 1
if temp > 1:
    thua_so.append(str(temp))
print(" * ".join(thua_so))
```
