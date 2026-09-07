# Hướng Dẫn Giảng Dạy: Số siêu nguyên tố (super prime)
Chuyên đề: **Ước Số, Bội Số & Số Nguyên Tố Cơ Bản**

---

## 1. Ý tưởng & Phân tích thuật toán
- Bản chất của bài này: số siêu nguyên tố là số mà bản thân nó và từng số cắt đuôi bên phải đều là số nguyên tố; với `239` cần kiểm tra `239`, `23`, `2`.
- Biến `temp` đi từ `239` xuống `23` rồi `2`, mỗi nấc thử chia từ `2` tới căn bậc hai; cả ba nấc đều vượt qua nên cờ `sieu` giữ nguyên `True`.
- Phép cắt đuôi là `temp = temp // 10`: `239 // 10 = 23`, `23 // 10 = 2`, `2 // 10 = 0` thì dừng.
- Thầy cô cho các em kiểm tra tay: `239` không chia hết cho số nào tới `15`, `23` không chia hết cho số nào tới `4`, `2` là số nguyên tố nhỏ nhất.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 239)
| `temp` | Thử chia | Kết luận nấc |
| --- | --- | --- |
| 239 | thử 2..15, `239 % 2 = 1`, `% 3 = 2`, `% 5 = 4`, `% 7 = 1`, `% 11 = 8`, `% 13 = 5` | nguyên tố, cắt tiếp |
| 23 | thử 2..4, `23 % 2 = 1`, `% 3 = 2`, `% 4 = 3` | nguyên tố, cắt tiếp |
| 2 | `range(2, 2)` rỗng | nguyên tố, cắt tiếp |
| 0 | dừng vòng lặp | xong |

Vì cả ba nấc đều đạt nên in ra `YES`, khớp với kết quả mẫu.

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- Bẫy 1: chỉ kiểm tra số gốc `239` mà quên các nấc cắt đuôi. Với `27` cách làm sai vẫn thấy `27` là hợp số nên trùng cờ ra `NO`, nhưng với `23` thì thiếu kiểm tra nấc `2`. Sửa lại: giữ vòng lặp `while temp > 0` cắt đuôi như bài giải.
- Bẫy 2: cắt đuôi bằng `temp / 10` (chia thực). Với mẫu `239` sẽ được `23.9` rồi lỗi ở phép chia lấy dư. Sửa lại: `temp = temp // 10`.
- Bẫy 3: quên loại số nhỏ hơn `2`. Với `N = 1` vòng lặp không chạy mà cờ `sieu` vẫn `True` nên in nhầm `YES`. Sửa lại: giữ nhánh `if n < 2: sieu = False` như bài giải.

---

## 4. Lời giải tham khảo
```python
n = int(input())
sieu = True
if n < 2:
    sieu = False
else:
    temp = n
    while temp > 0:
        if temp < 2:
            sieu = False
            break
        la_snt = True
        for i in range(2, int(temp ** 0.5) + 1):
            if temp % i == 0:
                la_snt = False
                break
        if not la_snt:
            sieu = False
            break
        temp = temp // 10
if sieu:
    print("YES")
else:
    print("NO")
```
