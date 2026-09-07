# Hướng Dẫn Giảng Dạy: Xoay vòng danh sách sang phải
Chuyên đề: **Chiếc Hộp Thần Kỳ list & Thao Tác Cơ Bản**

---

## 1. Ý tưởng & Phân tích thuật toán

- Bản chất của bài này là nhấc `K` bạn cuối hàng đem lên đứng đầu hàng, thứ tự trong nhóm được nhấc giữ nguyên.
- Với số mẫu `N = 5`, `K = 2`, dãy `1 2 3 4 5`: hai số cuối là `4 5` lên đầu, còn `1 2 3` lùi xuống sau, được `4 5 1 2 3`.
- Quy trình trong lời giải với các biến `line`, `n`, `k`, `a`:
  - Tách dòng đầu thành `n = 5`, `k = 2`.
  - Đọc dãy `a = [1, 2, 3, 4, 5]`, rút gọn `k %= n` được `2`.
  - Vì `k` khác 0 nên in `a[-2:] + a[:-2]` tức `[4, 5] + [1, 2, 3]`.
- Giá trị biên cụ thể: `K = N` (xoay cả hàng) thì `k %= n` thành `0` và dãy giữ nguyên.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 5 2 / 1 2 3 4 5)

| Bước | Thao tác | Giá trị |
|------|----------|---------|
| 1 | Tách dòng 1 | `["5", "2"]` |
| 2 | Lấy `n`, `k` | `n = 5`, `k = 2` |
| 3 | Đọc dãy `a` | `a = [1, 2, 3, 4, 5]` |
| 4 | Rút gọn `k %= n` | `k = 2` |
| 5 | Lấy `a[-2:]` | `[4, 5]` |
| 6 | Lấy `a[:-2]` | `[1, 2, 3]` |
| 7 | In nối lại | màn hình hiện `4 5 1 2 3` |

Kết quả cuối cùng khớp với đáp án mẫu: `4 5 1 2 3`.

---

## 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — xoay sang trái thay vì sang phải:
```python
line = input().split()
n, k = int(line[0]), int(line[1])
a = list(map(int, input().split()))
k %= n
print(*(a[k:] + a[:k]))
```
Với mẫu trên in ra `3 4 5 1 2` (đem 2 số đầu xuống cuối) sai. Cách sửa: đem `K` số cuối lên đầu bằng `a[-k:] + a[:-k]`.
- Bẫy 2 — quên rút gọn `K` khi `K` bằng `N`:
```python
line = input().split()
n, k = int(line[0]), int(line[1])
a = list(map(int, input().split()))
print(*(a[-k:] + a[:-k]))
```
Với mẫu trên vẫn ra `4 5 1 2 3`, nhưng khi `K = N = 5` thì `a[:-5]` thành rỗng và kết quả sai. Cách sửa: rút gọn `k %= n` và giữ nguyên dãy khi `k == 0`.
- Bẫy 3 — lặp `K` lần mỗi lần nhấc 1 số:
```python
line = input().split()
n, k = int(line[0]), int(line[1])
a = list(map(int, input().split()))
for _ in range(k):
    a = [a[-1]] + a[:-1]
print(*a)
```
Với mẫu trên vẫn ra `4 5 1 2 3`, nhưng mỗi lần nhấc chép lại cả dãy nên với `N` tới `10^5` sẽ rất chậm. Cách sửa: cắt một nhát bằng `a[-k:] + a[:-k]`.

---

## 4. Lời giải tham khảo

```python
line = input().split()
n, k = int(line[0]), int(line[1])
a = list(map(int, input().split()))
k %= n
if k == 0:
    print(*a)
else:
    print(*(a[-k:] + a[:-k]))
```
