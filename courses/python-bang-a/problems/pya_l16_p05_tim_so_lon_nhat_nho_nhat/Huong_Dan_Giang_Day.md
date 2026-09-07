# Hướng Dẫn Giảng Dạy: Tìm số lớn nhất & nhỏ nhất
Chuyên đề: **Chiếc Hộp Thần Kỳ list & Thao Tác Cơ Bản**

---

## 1. Ý tưởng & Phân tích thuật toán

- Bản chất của bài này là lướt một lượt qua danh sách để nhặt ra số to nhất và số bé nhất.
- Với số mẫu `N = 5`, dãy `12 5 89 3 45`: số lớn nhất là `89`, số nhỏ nhất là `3` nên đáp án là `89 3`.
- Quy trình trong lời giải với các biến `n`, `a`:
  - Đọc `n = 5`.
  - Đọc dãy `a = [12, 5, 89, 3, 45]`.
  - Gọi `max(a)` được `89`, `min(a)` được `3`, in ra `89 3`.
- Giá trị biên cụ thể: `N = 1` thì số lớn nhất và nhỏ nhất trùng nhau (ví dụ dãy `7` thì in `7 7`).

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 5 / 12 5 89 3 45)

| Bước | Thao tác | Giá trị |
|------|----------|---------|
| 1 | Đọc `n` | `n = 5` |
| 2 | Đọc dãy `a` | `a = [12, 5, 89, 3, 45]` |
| 3 | Tính `max(a)` | `89` |
| 4 | Tính `min(a)` | `3` |
| 5 | In kết quả | màn hình hiện `89 3` |

Kết quả cuối cùng khớp với đáp án mẫu: `89 3`.

---

## 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — in ngược thứ tự nhỏ trước lớn sau:
```python
n = int(input().strip())
a = list(map(int, input().split()))
print(min(a), max(a))
```
Với mẫu trên in ra `3 89`, không khớp đáp án mẫu `89 3`. Cách sửa: in `print(max(a), min(a))`.
- Bẫy 2 — tự đặt số lớn nhất ban đầu là 0:
```python
n = int(input().strip())
a = list(map(int, input().split()))
lon = 0
for x in a:
    if x > lon:
        lon = x
print(lon, min(a))
```
Với mẫu trên vẫn ra `89 3`, nhưng nếu dãy toàn số âm thì `lon` kẹt ở `0` sai. Cách sửa: dùng `max(a)` có sẵn.
- Bẫy 3 — in mỗi số một dòng:
```python
n = int(input().strip())
a = list(map(int, input().split()))
print(max(a))
print(min(a))
```
Với mẫu trên in ra hai dòng `89` rồi `3`, không khớp đáp án mẫu `89 3` trên một dòng. Cách sửa: in chung một lệnh `print(max(a), min(a))`.

---

## 4. Lời giải tham khảo

```python
n = int(input().strip())
a = list(map(int, input().split()))
print(max(a), min(a))
```
