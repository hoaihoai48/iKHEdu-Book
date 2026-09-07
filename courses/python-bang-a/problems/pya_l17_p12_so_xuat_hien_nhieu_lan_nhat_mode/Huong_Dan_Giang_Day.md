# Hướng Dẫn Giảng Dạy: Số xuất hiện nhiều lần nhất (Mode)
Chuyên đề: **Thống Kê Danh Sách & Sắp Xếp Nâng Cao**

---

## 1. Ý tưởng & Phân tích thuật toán

- Bản chất của bài này là đếm số lần xuất hiện của từng số rồi chọn số xuất hiện nhiều nhất; nếu hòa thì chọn số bé hơn.
- Với số mẫu `N = 7`, dãy `2 3 5 2 3 7 2`: số `2` xuất hiện 3 lần, số `3` xuất hiện 2 lần, số `5` và `7` mỗi số 1 lần, nên đáp án là `2`.
- Quy trình trong lời giải với các biến `n`, `a`, `counts`, `x`, `max_c`, `candidates`, `k`, `v`:
  - Đọc `n = 7`, dãy `a = [2, 3, 5, 2, 3, 7, 2]`.
  - Đếm được `counts = {2: 3, 3: 2, 5: 1, 7: 1}`, số lần nhiều nhất `max_c = 3`.
  - Các số đạt `3` lần là `[2]`, lấy nhỏ nhất được `2` rồi in ra.
- Giá trị biên cụ thể: mọi số xuất hiện 1 lần (hòa toàn bộ) thì đáp án là số bé nhất dãy; `N = 1` thì đáp án là số duy nhất đó.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 7 / 2 3 5 2 3 7 2)

| Bước | Thao tác | Giá trị |
|------|----------|---------|
| 1 | Đọc `n` | `n = 7` |
| 2 | Đọc dãy `a` | `a = [2, 3, 5, 2, 3, 7, 2]` |
| 3 | Đếm từng số | `2` có 3, `3` có 2, `5` có 1, `7` có 1 |
| 4 | Lấy `max_c` | `max_c = 3` |
| 5 | Lọc số đạt `3` lần | `candidates = [2]` |
| 6 | In nhỏ nhất | màn hình hiện `2` |

Kết quả cuối cùng khớp với đáp án mẫu: `2`.

---

## 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — lấy số lớn nhất trong dãy thay vì số xuất hiện nhiều nhất:
```python
n = int(input().strip())
a = list(map(int, input().split()))
print(max(a))
```
Với mẫu trên in ra `7`, không khớp đáp án mẫu `2`. Cách sửa: đếm tần suất rồi chọn số có lượt đếm cao nhất.
- Bẫy 2 — lấy khóa lớn nhất của bảng đếm:
```python
n = int(input().strip())
a = list(map(int, input().split()))
counts = {}
for x in a:
    counts[x] = counts.get(x, 0) + 1
print(max(counts))
```
Với mẫu trên in ra `7` (khóa lớn nhất), không khớp đáp án mẫu `2`. Cách sửa: so sánh lượt đếm `max(counts.values())` rồi lọc số đạt mức đó.
- Bẫy 3 — hòa lượt đếm mà lấy số gặp trước:
```python
n = int(input().strip())
a = list(map(int, input().split()))
counts = {}
for x in a:
    counts[x] = counts.get(x, 0) + 1
print(max(counts, key=counts.get))
```
Với mẫu trên vẫn ra `2`, nhưng dãy như `3 3 2 2` (cùng 2 lần) thì cách này trả `3` trong khi đáp án đúng phải là `2`. Cách sửa: lọc mọi số đạt lượt cao nhất rồi lấy `min`.

---

## 4. Lời giải tham khảo

```python
n = int(input().strip())
a = list(map(int, input().split()))
counts = {}
for x in a:
    counts[x] = counts.get(x, 0) + 1
max_c = max(counts.values())
candidates = [k for k, v in counts.items() if v == max_c]
print(min(candidates))
```
