# Hướng Dẫn Giảng Dạy: Cặp số nguyên tố sinh đôi
Chuyên đề: **Ước Số, Bội Số & Số Nguyên Tố Cơ Bản**

---

## 1. Ý tưởng & Phân tích thuật toán
- Bản chất của bài này: cặp sinh đôi là hai số nguyên tố hơn kém nhau đúng `2` đơn vị, tức `(p, p + 2)` với `p + 2 <= 15`.
- Chương trình cho `p` chạy từ `2` tới `13`, mỗi `p` kiểm tra cả `p` và `q = p + 2` có phải số nguyên tố không.
- Với `N = 15`: `p = 3` cho cặp `3 5`, `p = 5` cho cặp `5 7`, `p = 11` cho cặp `11 13`; các `p` còn lại có ít nhất một số là hợp số.
- Mỗi cặp in trên một dòng theo thứ tự tăng dần của `p`.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 15)
| `p` | `q = p + 2` | Kiểm tra | In? |
| --- | --- | --- | --- |
| 2 | 4 | `4 % 2 == 0`, hợp số | không |
| 3 | 5 | cả hai nguyên tố | in `3 5` |
| 4 | 6 | `4 % 2 == 0`, hợp số | không |
| 5 | 7 | cả hai nguyên tố | in `5 7` |
| 6–10 | 8–12 | `p` hoặc `q` chẵn, hợp số | không |
| 11 | 13 | cả hai nguyên tố | in `11 13` |
| 12 | 14 | hợp số | không |
| 13 | 15 | `15 % 3 == 0`, hợp số | không |

Kết quả in ra ba dòng `3 5`, `5 7`, `11 13`, khớp với kết quả mẫu.

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- Bẫy 1: quên điều kiện `q <= n`. Với mẫu `15`, `p = 13` cho `q = 15` là hợp số nên không sao, nhưng với `N = 14` mà thiếu điều kiện, cặp `13 15` vẫn bị xét. Sửa lại: giữ `if la_snt_p and la_snt_q and q <= n`.
- Bẫy 2: in hai số trên cùng một dòng cách nhau bởi dấu phẩy. Với mẫu `15` dòng đầu thành `3, 5`, chương trình kiểm tra không chấp nhận. Sửa lại: `print(p, q)` (mặc định cách nhau một khoảng trắng).
- Bẫy 3: chỉ kiểm tra `p` mà quên kiểm tra `q`. Với mẫu `15`, `p = 7` là nguyên tố nhưng `q = 9` là hợp số, làm sai sẽ in thêm dòng `7 9`. Sửa lại: kiểm tra cả hai cờ như bài giải.

---

## 4. Lời giải tham khảo
```python
n = int(input())
for p in range(2, n - 1):
    la_snt_p = True
    if p < 2:
        la_snt_p = False
    else:
        for i in range(2, int(p ** 0.5) + 1):
            if p % i == 0:
                la_snt_p = False
                break
    q = p + 2
    la_snt_q = True
    for i in range(2, int(q ** 0.5) + 1):
        if q % i == 0:
            la_snt_q = False
            break
    if la_snt_p and la_snt_q and q <= n:
        print(p, q)
```
