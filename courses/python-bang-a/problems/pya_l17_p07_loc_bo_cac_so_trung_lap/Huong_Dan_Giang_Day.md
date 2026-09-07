# Hướng Dẫn Giảng Dạy: Lọc bỏ các số trùng lặp
Chuyên đề: **Thống Kê Danh Sách & Sắp Xếp Nâng Cao**

---

## 1. Ý tưởng & Phân tích thuật toán

- Bản chất của bài này là gom các số trùng thành một rồi xếp các số còn lại từ bé đến lớn.
- Với số mẫu `N = 7`, dãy `3 1 4 1 5 9 2`: số `1` xuất hiện hai lần nên gộp lại, còn `1 2 3 4 5 9` sau khi xếp tăng dần.
- Quy trình trong lời giải với các biến `n`, `a`, `unique`:
  - Đọc `n = 7`, dãy `a = [3, 1, 4, 1, 5, 9, 2]`.
  - Gom trùng bằng `set(a)` được `{1, 2, 3, 4, 5, 9}`, xếp lại bằng `sorted` được `[1, 2, 3, 4, 5, 9]`.
  - In ra `1 2 3 4 5 9`.
- Giá trị biên cụ thể: dãy toàn số giống nhau (ví dụ bảy số `4`) thì kết quả chỉ còn một số `4`.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 7 / 3 1 4 1 5 9 2)

| Bước | Thao tác | Giá trị |
|------|----------|---------|
| 1 | Đọc `n` | `n = 7` |
| 2 | Đọc dãy `a` | `a = [3, 1, 4, 1, 5, 9, 2]` |
| 3 | Gom trùng `set(a)` | `{1, 2, 3, 4, 5, 9}` (số `1` còn một) |
| 4 | Xếp `sorted` | `[1, 2, 3, 4, 5, 9]` |
| 5 | In kết quả | màn hình hiện `1 2 3 4 5 9` |

Kết quả cuối cùng khớp với đáp án mẫu: `1 2 3 4 5 9`.

---

## 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — gom trùng mà quên xếp lại:
```python
n = int(input().strip())
a = list(map(int, input().split()))
unique = list(set(a))
print(*unique)
```
Với mẫu trên thứ tự các số còn lại lộn xộn (ví dụ `1 2 3 4 5 9` theo thứ tự ngẫu nhiên của tập hợp), không đảm bảo tăng dần như đáp án mẫu. Cách sửa: bọc thêm `sorted`, tức `sorted(list(set(a)))`.
- Bẫy 2 — giữ nguyên thứ tự xuất hiện thay vì xếp tăng dần:
```python
n = int(input().strip())
a = list(map(int, input().split()))
unique = list(dict.fromkeys(a))
print(*unique)
```
Với mẫu trên in ra `3 1 4 5 9 2` sai. Cách sửa: xếp tăng dần bằng `sorted`.
- Bẫy 3 — xếp mà không gom trùng:
```python
n = int(input().strip())
a = list(map(int, input().split()))
unique = sorted(a)
print(*unique)
```
Với mẫu trên in ra `1 1 2 3 4 5 9` (số `1` còn hai lần), không khớp đáp án mẫu. Cách sửa: gom trùng bằng `set` trước khi xếp.

---

## 4. Lời giải tham khảo

```python
n = int(input().strip())
a = list(map(int, input().split()))
unique = sorted(list(set(a)))
print(*unique)
```
