# Hướng Dẫn Giảng Dạy: Xếp hàng chiều cao
Chuyên đề: **Chiếc Hộp Thần Kỳ list & Thao Tác Cơ Bản**

---

## 1. Ý tưởng & Phân tích thuật toán

- Bản chất của bài này là sắp xếp các chiều cao từ thấp đến cao.
- Với số mẫu `N = 5`, các chiều cao `160 150 175 165 155`: xếp lại thành `150 155 160 165 175`.
- Quy trình trong lời giải với các biến `n`, `data`:
  - Đọc `n = 5`.
  - Gom đủ 5 số vào `data = [160, 150, 175, 165, 155]` (vòng lặp gom đề phòng các số nằm rải rác nhiều dòng).
  - Gọi `sorted` được `[150, 155, 160, 165, 175]` rồi in ra cách nhau bởi dấu cách.
- Giá trị biên cụ thể: `N = 1` thì in nguyên chiều cao đó; `N` tới `10^5` vẫn sắp xếp kịp.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 5 / 160 150 175 165 155)

| Bước | Thao tác | Giá trị |
|------|----------|---------|
| 1 | Đọc `n` | `n = 5` |
| 2 | Gom `data` | `data = [160, 150, 175, 165, 155]` |
| 3 | Gọi `sorted` | `[150, 155, 160, 165, 175]` |
| 4 | In kết quả | màn hình hiện `150 155 160 165 175` |

Kết quả cuối cùng khớp với đáp án mẫu: `150 155 160 165 175`.

---

## 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — sắp giảm dần thay vì tăng dần:
```python
n = int(input())
data = []
while len(data) < n:
    data += list(map(int, input().split()))
data = sorted(data[:n], reverse=True)
print(" ".join(map(str, data)))
```
Với mẫu trên in ra `175 165 160 155 150` sai. Cách sửa: sắp tăng dần mặc định, không dùng `reverse=True`.
- Bẫy 2 — in cả danh sách kèm ngoặc:
```python
n = int(input())
data = []
while len(data) < n:
    data += list(map(int, input().split()))
data = sorted(data[:n])
print(data)
```
Với mẫu trên in ra `[150, 155, 160, 165, 175]` có ngoặc và dấu phẩy, không khớp đáp án mẫu. Cách sửa: in bằng `" ".join(map(str, data))`.
- Bẫy 3 — loại trùng bằng tập hợp:
```python
n = int(input())
data = []
while len(data) < n:
    data += list(map(int, input().split()))
data = sorted(set(data))
print(" ".join(map(str, data)))
```
Nếu hai bạn cao bằng nhau thì một bạn bị mất khỏi hàng. Cách sửa: sắp trực tiếp danh sách, không dùng `set`.

---

## 4. Lời giải tham khảo

```python
n = int(input())
data = []
while len(data) < n:
    data += list(map(int, input().split()))
data = sorted(data[:n])
print(" ".join(map(str, data)))
```
