# Hướng Dẫn Giảng Dạy: Điểm olympic bỏ max bỏ min
Chuyên đề: **Thống Kê Danh Sách & Sắp Xếp Nâng Cao**

---

## 1. Ý tưởng & Phân tích thuật toán

- Bản chất của bài này là gạch đi một điểm cao nhất và một điểm thấp nhất rồi tính trung bình các điểm còn lại.
- Với số mẫu `N = 5`, các điểm `7.0 9.0 8.0 10.0 6.0`: bỏ thấp nhất `6.0` và cao nhất `10.0`, còn `7.0 8.0 9.0`, tổng `24.0` chia `3` được `8.0`, viết đủ 2 chữ số thành `8.00`.
- Quy trình trong lời giải với các biến `n`, `a`, `trimmed`, `tb`:
  - Đọc `n = 5`, dãy `a = [7.0, 9.0, 8.0, 10.0, 6.0]`; gọi `a.sort()` được `[6.0, 7.0, 8.0, 9.0, 10.0]`.
  - Cắt hai đầu `a[1:-1]` được `trimmed = [7.0, 8.0, 9.0]`; tính `tb = 24.0 / 3 = 8.0`.
  - In `8.00`.
- Giá trị biên cụ thể: `N = 3` thì sau khi bỏ còn đúng 1 điểm ở giữa; nhiều điểm trùng cao nhất hoặc thấp nhất thì mỗi đầu chỉ bỏ đúng một điểm.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 5 / 7.0 9.0 8.0 10.0 6.0)

| Bước | Thao tác | Giá trị |
|------|----------|---------|
| 1 | Đọc `n` | `n = 5` |
| 2 | Đọc dãy `a` | `a = [7.0, 9.0, 8.0, 10.0, 6.0]` |
| 3 | Gọi `a.sort()` | `a = [6.0, 7.0, 8.0, 9.0, 10.0]` |
| 4 | Cắt `a[1:-1]` | `trimmed = [7.0, 8.0, 9.0]` |
| 5 | Tính `tb` | `24.0 / 3 = 8.0` |
| 6 | In với 2 chữ số | màn hình hiện `8.00` |

Kết quả cuối cùng khớp với đáp án mẫu: `8.00`.

---

## 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — chia cho `N` thay vì số điểm còn lại:
```python
n = int(input().strip())
a = list(map(float, input().split()))
a.sort()
trimmed = a[1:-1]
tb = sum(trimmed) / n
print(f"{tb:.2f}")
```
Với mẫu trên in ra `24.0 / 5 = 4.80` sai. Cách sửa: chia cho `len(trimmed)`.
- Bẫy 2 — quên bỏ hai đầu mà tính trung bình cả dãy:
```python
n = int(input().strip())
a = list(map(float, input().split()))
tb = sum(a) / n
print(f"{tb:.2f}")
```
Với mẫu trên in ra `40.0 / 5 = 8.00` trùng cờ đáp án, nhưng bản chất sai: chưa bỏ `6.0` và `10.0`. Với dãy mà điểm giữa lệch khỏi trung bình chung, cách này cho kết quả sai. Cách sửa: xếp rồi cắt `a[1:-1]` trước khi tính.
- Bẫy 3 — in thiếu chữ số thập phân:
```python
n = int(input().strip())
a = list(map(float, input().split()))
a.sort()
trimmed = a[1:-1]
tb = sum(trimmed) / len(trimmed)
print(tb)
```
Với mẫu trên in ra `8.0`, không khớp đáp án mẫu `8.00`. Cách sửa: in bằng `print(f"{tb:.2f}")`.

---

## 4. Lời giải tham khảo

```python
n = int(input().strip())
a = list(map(float, input().split()))
a.sort()
trimmed = a[1:-1]
tb = sum(trimmed) / len(trimmed)
print(f"{tb:.2f}")
```
