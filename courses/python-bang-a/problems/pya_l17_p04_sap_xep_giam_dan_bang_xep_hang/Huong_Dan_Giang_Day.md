# Hướng Dẫn Giảng Dạy: Sắp xếp giảm dần bảng xếp hạng
Chuyên đề: **Thống Kê Danh Sách & Sắp Xếp Nâng Cao**

---

## 1. Ý tưởng & Phân tích thuật toán

- Bản chất của bài này là xếp điểm từ cao xuống thấp để bạn điểm cao đứng trước trao giải.
- Với số mẫu `N = 5`, các điểm `20 80 40 100 60`: xếp lại thành `100 80 60 40 20`.
- Quy trình trong lời giải với các biến `n`, `a`:
  - Đọc `n = 5`, dãy `a = [20, 80, 40, 100, 60]`.
  - Gọi `a.sort(reverse=True)` được `[100, 80, 60, 40, 20]` rồi in ra.
- Giá trị biên cụ thể: `N = 1` thì in nguyên điểm đó; các bạn bằng điểm nhau thì đứng cạnh nhau theo thứ tự nào cũng đúng.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 5 / 20 80 40 100 60)

| Bước | Thao tác | Giá trị |
|------|----------|---------|
| 1 | Đọc `n` | `n = 5` |
| 2 | Đọc dãy `a` | `a = [20, 80, 40, 100, 60]` |
| 3 | Gọi `a.sort(reverse=True)` | `a = [100, 80, 60, 40, 20]` |
| 4 | In kết quả | màn hình hiện `100 80 60 40 20` |

Kết quả cuối cùng khớp với đáp án mẫu: `100 80 60 40 20`.

---

## 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — xếp tăng dần thay vì giảm dần:
```python
n = int(input().strip())
a = list(map(int, input().split()))
a.sort()
print(*a)
```
Với mẫu trên in ra `20 40 60 80 100` sai. Cách sửa: thêm `reverse=True`.
- Bẫy 2 — đảo dãy nhập mà không xếp:
```python
n = int(input().strip())
a = list(map(int, input().split()))
print(*(a[::-1]))
```
Với mẫu trên in ra `60 100 40 80 20` sai. Cách sửa: xếp giảm dần bằng `a.sort(reverse=True)`.
- Bẫy 3 — in cả ngoặc của danh sách:
```python
n = int(input().strip())
a = list(map(int, input().split()))
a.sort(reverse=True)
print(a)
```
Với mẫu trên in ra `[100, 80, 60, 40, 20]` có ngoặc và dấu phẩy, không khớp đáp án mẫu. Cách sửa: thêm dấu sao `print(*a)`.

---

## 4. Lời giải tham khảo

```python
n = int(input().strip())
a = list(map(int, input().split()))
a.sort(reverse=True)
print(*a)
```
