# Hướng Dẫn Giảng Dạy: Ghép hai dãy đã sắp xếp
Chuyên đề: **Thống Kê Danh Sách & Sắp Xếp Nâng Cao**

---

## 1. Ý tưởng & Phân tích thuật toán

- Bản chất của bài này là trộn hai dãy thành một dãy chung rồi xếp từ bé đến lớn.
- Với số mẫu `N = 3`, `M = 4`, dãy `A = 1 4 7`, dãy `B = 2 3 5 8`: trộn lại được `1 4 7 2 3 5 8`, xếp lại thành `1 2 3 4 5 7 8`.
- Quy trình trong lời giải với các biến `n`, `m`, `a`, `b`, `res`:
  - Đọc `n = 3`, `m = 4`; đọc `a = [1, 4, 7]`, `b = [2, 3, 5, 8]`.
  - Nối hai dãy `a + b` rồi gọi `sorted` được `[1, 2, 3, 4, 5, 7, 8]`.
  - In ra `1 2 3 4 5 7 8`.
- Giá trị biên cụ thể: dãy hợp nhất có `N + M` phần tử; `N, M` tới `10^5` nên dãy chung tới hai trăm nghìn số, phép xếp có sẵn vẫn làm kịp.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 3 4 / 1 4 7 / 2 3 5 8)

| Bước | Thao tác | Giá trị |
|------|----------|---------|
| 1 | Đọc `n, m` | `n = 3`, `m = 4` |
| 2 | Đọc `a`, `b` | `a = [1, 4, 7]`, `b = [2, 3, 5, 8]` |
| 3 | Nối `a + b` | `[1, 4, 7, 2, 3, 5, 8]` |
| 4 | Gọi `sorted` | `[1, 2, 3, 4, 5, 7, 8]` |
| 5 | In kết quả | màn hình hiện `1 2 3 4 5 7 8` |

Kết quả cuối cùng khớp với đáp án mẫu: `1 2 3 4 5 7 8`.

---

## 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — chỉ nối mà quên xếp:
```python
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(*(a + b))
```
Với mẫu trên in ra `1 4 7 2 3 5 8` sai. Cách sửa: xếp lại bằng `sorted(a + b)`.
- Bẫy 2 — đọc hai dãy chung một dòng:
```python
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
res = sorted(a + b)
print(*res)
```
Bản thân cách này đúng với mẫu, nhưng nếu gom nhầm số của dãy `B` sang dòng dãy `A` thì kết quả lệch. Bẫy thật sự: đọc thiếu dòng thứ ba nên `b` rỗng, in ra `1 4 7` thiếu bốn số. Cách sửa: đọc đủ ba dòng theo đúng thứ tự `n m`, rồi `a`, rồi `b`.
- Bẫy 3 — in hai dãy riêng thay vì dãy chung:
```python
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(*a)
print(*b)
```
Với mẫu trên in ra hai dòng `1 4 7` rồi `2 3 5 8`, không khớp đáp án mẫu một dòng. Cách sửa: trộn rồi xếp thành một dãy `res` và in một dòng.

---

## 4. Lời giải tham khảo

```python
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
res = sorted(a + b)
print(*res)
```
