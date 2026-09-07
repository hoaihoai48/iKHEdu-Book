# Hướng Dẫn Giảng Dạy: Tìm vị trí đầu tiên của X
Chuyên đề: **Chiếc Hộp Thần Kỳ list & Thao Tác Cơ Bản**

---

## 1. Ý tưởng & Phân tích thuật toán

- Bản chất của bài này là quét dãy từ trái sang phải và dừng ngay khi gặp số `X` lần đầu, vị trí đếm từ 0.
- Với số mẫu `N = 5`, `X = 7`, dãy `3 5 7 9 7`: vị trí 0 là 3, vị trí 1 là 5, vị trí 2 là 7 nên đáp án là `2` (số 7 ở cuối không tính vì đã thấy ở vị trí 2).
- Quy trình trong lời giải với các biến `line`, `n`, `x`, `a`:
  - Tách dòng đầu `line` thành `n = 5`, `x = 7`.
  - Đọc dãy `a = [3, 5, 7, 9, 7]`.
  - Gọi `a.index(7)` được `2` rồi in `2`; nếu `X` vắng mặt thì `index` báo lỗi, phần `except ValueError` in `-1`.
- Giá trị biên cụ thể: `X` nằm ngay vị trí 0 thì in `0`; `X` không có trong dãy (mẫu phụ `4 10` và `1 2 3 4`) thì in `-1`.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 5 7 / 3 5 7 9 7)

| Bước | Thao tác | Giá trị |
|------|----------|---------|
| 1 | Tách dòng 1 `line = input().split()` | `["5", "7"]` |
| 2 | Lấy `n`, `x` | `n = 5`, `x = 7` |
| 3 | Đọc dãy `a` | `a = [3, 5, 7, 9, 7]` |
| 4 | Gọi `a.index(7)` | `2` (phần tử 7 đầu tiên ở vị trí 2) |
| 5 | In kết quả | màn hình hiện `2` |

Kết quả cuối cùng khớp với đáp án mẫu: `2`.

---

## 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — đếm vị trí từ 1 thay vì từ 0:
```python
line = input().split()
n, x = int(line[0]), int(line[1])
a = list(map(int, input().split()))
print(a.index(x) + 1)
```
Với mẫu trên in ra `3`, không khớp đáp án mẫu `2`. Cách sửa: in nguyên `a.index(x)`, không cộng 1.
- Bẫy 2 — quên xử lý khi `X` vắng mặt:
```python
line = input().split()
n, x = int(line[0]), int(line[1])
a = list(map(int, input().split()))
print(a.index(x))
```
Với mẫu phụ `4 10` và dãy `1 2 3 4`, lệnh `index` gây lỗi và chương trình dừng đột ngột thay vì in `-1`. Cách sửa: bọc trong `try ... except ValueError: print(-1)`.
- Bẫy 3 — quét hết dãy mà không dừng ở lần gặp đầu:
```python
line = input().split()
n, x = int(line[0]), int(line[1])
a = list(map(int, input().split()))
vitri = -1
for i in range(n):
    if a[i] == x:
        vitri = i
print(vitri)
```
Với mẫu trên vòng lặp ghi đè tới số 7 cuối cùng nên in ra `4` sai. Cách sửa: dừng ngay khi gặp lần đầu hoặc dùng `a.index(x)`.

---

## 4. Lời giải tham khảo

```python
line = input().split()
n, x = int(line[0]), int(line[1])
a = list(map(int, input().split()))
try:
    print(a.index(x))
except ValueError:
    print(-1)
```
