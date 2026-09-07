# Hướng Dẫn Giảng Dạy: Tìm số có đúng 3 ước số
Chuyên đề: **Ước Số, Bội Số & Số Nguyên Tố Cơ Bản**

---

## 1. Ý tưởng & Phân tích thuật toán
- Bản chất của bài này: số có đúng 3 ước chính là bình phương của một số nguyên tố (ví dụ `4 = 2 * 2`, `9 = 3 * 3`, `25 = 5 * 5`), nên chỉ cần đếm số nguyên tố tới căn bậc hai của `N`.
- Với `N = 30`: `gioi_han = int(30 ** 0.5) = 5`; sàng các số từ `2` tới `5` giữ lại `2, 3, 5`.
- Mỗi số nguyên tố `P` cho một đáp án `P * P <= 30`, vậy có đúng `3` số là `4, 9, 25`.
- Thầy cô cho các em kiểm tra tay: ước của `4` là `1, 2, 4`; ước của `9` là `1, 3, 9`; ước của `25` là `1, 5, 25`.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 30)
| Bước | Giá trị | Ghi chú |
| --- | --- | --- |
| Đọc | `n = 30` | |
| Giới hạn | `gioi_han = 5` | `int(30 ** 0.5)` |
| Sàng | `[True]*6`, đánh dấu `0, 1` sai | |
| Sàng `i = 2` | gạch `4` | `2 * 2 = 4` |
| Đếm | `2, 3, 5` còn đúng | `dem = 3` |

Kết quả in ra: `3`, khớp với kết quả mẫu.

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- Bẫy 1: đếm trực tiếp từng số từ `1` tới `N` rồi đếm ước. Với `N = 30` vẫn ra `3`, nhưng với `N` tới `10^9` vòng lặp không bao giờ xong. Sửa lại: chỉ sàng số nguyên tố tới căn bậc hai như bài giải.
- Bẫy 2: quên xử lý `gioi_han < 2` (tức `N = 1, 2, 3`). Khi đó danh sách sàng rỗng và dễ báo lỗi, trong khi đáp án đúng là `0`. Sửa lại: giữ nhánh `if gioi_han < 2: print(0)` như bài giải.
- Bẫy 3: đếm cả `1` thành số nguyên tố. Với mẫu `30` sẽ ra `4` thay vì `3`. Sửa lại: `la_snt[0] = False` và `la_snt[1] = False`.

---

## 4. Lời giải tham khảo
```python
n = int(input())
gioi_han = int(n ** 0.5)
if gioi_han < 2:
    print(0)
else:
    la_snt = [True] * (gioi_han + 1)
    la_snt[0] = False
    la_snt[1] = False
    for i in range(2, int(gioi_han ** 0.5) + 1):
        if la_snt[i]:
            for j in range(i * i, gioi_han + 1, i):
                la_snt[j] = False
    dem = 0
    for i in range(2, gioi_han + 1):
        if la_snt[i]:
            dem = dem + 1
    print(dem)
```
