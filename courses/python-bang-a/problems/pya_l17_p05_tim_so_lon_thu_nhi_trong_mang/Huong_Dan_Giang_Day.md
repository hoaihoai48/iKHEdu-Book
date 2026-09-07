# Hướng Dẫn Giảng Dạy: Tìm số lớn thứ nhì trong mảng
Chuyên đề: **Thống Kê Danh Sách & Sắp Xếp Nâng Cao**

---

## 1. Ý tưởng & Phân tích thuật toán

- Bản chất của bài này là tìm số lớn nhất trước, rồi trong các số còn lại (nhỏ hơn số lớn nhất) tìm số lớn nhất tiếp theo.
- Với số mẫu `N = 5`, dãy `10 20 20 15 5`: số lớn nhất là `20`; các số nhỏ hơn `20` là `10`, `15`, `5`, lớn nhất trong đó là `15` nên đáp án là `15`.
- Quy trình trong lời giải với các biến `n`, `a`, `mx`, `candidates`, `x`:
  - Đọc `n = 5`, dãy `a = [10, 20, 20, 15, 5]`; lấy `mx = 20`.
  - Lọc các số nhỏ hơn `20` được `candidates = [10, 15, 5]`.
  - Vì danh sách lọc không rỗng nên in `max` của nó là `15`; nếu rỗng (mẫu phụ `5 5 5`) thì in `KHONG CO`.
- Giá trị biên cụ thể: `N = 2` với hai số khác nhau thì đáp án là số bé hơn; mọi số bằng nhau thì in đúng chữ `KHONG CO`.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 5 / 10 20 20 15 5)

| Bước | Thao tác | Giá trị |
|------|----------|---------|
| 1 | Đọc `n` | `n = 5` |
| 2 | Đọc dãy `a` | `a = [10, 20, 20, 15, 5]` |
| 3 | Lấy `mx = max(a)` | `mx = 20` |
| 4 | Lọc số nhỏ hơn `20` | `candidates = [10, 15, 5]` |
| 5 | In lớn nhất trong lọc | màn hình hiện `15` |

Kết quả cuối cùng khớp với đáp án mẫu: `15`.

---

## 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — xếp rồi lấy phần tử kế cuối mà không gộp trùng:
```python
n = int(input().strip())
a = list(map(int, input().split()))
a.sort()
print(a[-2])
```
Với mẫu trên, dãy xếp là `[5, 10, 15, 20, 20]` nên `a[-2]` là `20`, không khớp đáp án mẫu `15`. Cách sửa: lọc bỏ hết số bằng giá trị lớn nhất rồi mới lấy lớn nhất.
- Bẫy 2 — quên trường hợp mọi số bằng nhau:
```python
n = int(input().strip())
a = list(map(int, input().split()))
mx = max(a)
candidates = [x for x in a if x < mx]
print(max(candidates))
```
Với mẫu trên vẫn ra `15`, nhưng mẫu phụ `5 5 5` thì danh sách lọc rỗng và `max` rỗng gây lỗi thay vì in `KHONG CO`. Cách sửa: kiểm tra `if candidates` rồi mới in, ngược lại in `KHONG CO`.
- Bẫy 3 — lấy số bé nhất thay vì lớn thứ nhì:
```python
n = int(input().strip())
a = list(map(int, input().split()))
mx = max(a)
candidates = [x for x in a if x < mx]
if candidates:
    print(min(candidates))
else:
    print("KHONG CO")
```
Với mẫu trên in ra `5` sai. Cách sửa: in `max(candidates)`.

---

## 4. Lời giải tham khảo

```python
n = int(input().strip())
a = list(map(int, input().split()))
mx = max(a)
candidates = [x for x in a if x < mx]
if candidates:
    print(max(candidates))
else:
    print("KHONG CO")
```
