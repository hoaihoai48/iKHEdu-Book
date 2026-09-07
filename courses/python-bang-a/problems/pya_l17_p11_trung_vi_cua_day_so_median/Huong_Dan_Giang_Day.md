# Hướng Dẫn Giảng Dạy: Trung vị của dãy số (Median)
Chuyên đề: **Thống Kê Danh Sách & Sắp Xếp Nâng Cao**

---

## 1. Ý tưởng & Phân tích thuật toán

- Bản chất của bài này là xếp dãy tăng dần rồi nhặt bạn đứng chính giữa, vì `N` luôn là số lẻ nên lúc nào cũng có đúng một bạn giữa hàng.
- Với số mẫu `N = 5`, dãy `10 2 8 4 6`: xếp lại thành `2 4 6 8 10`, vị trí giữa (đếm từ 0 là vị trí `5 // 2 = 2`) là số `6`.
- Quy trình trong lời giải với các biến `n`, `a`:
  - Đọc `n = 5`, dãy `a = [10, 2, 8, 4, 6]`.
  - Gọi `a.sort()` được `[2, 4, 6, 8, 10]`.
  - Lấy `a[5 // 2]` tức `a[2]` được `6` rồi in ra.
- Giá trị biên cụ thể: `N = 1` thì trung vị chính là số duy nhất đó; `N` lẻ tới `10^5` thì vị trí giữa là `n // 2`.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 5 / 10 2 8 4 6)

| Bước | Thao tác | Giá trị |
|------|----------|---------|
| 1 | Đọc `n` | `n = 5` |
| 2 | Đọc dãy `a` | `a = [10, 2, 8, 4, 6]` |
| 3 | Gọi `a.sort()` | `a = [2, 4, 6, 8, 10]` |
| 4 | Tính vị trí giữa `n // 2` | `5 // 2 = 2` |
| 5 | Lấy `a[2]` và in | màn hình hiện `6` |

Kết quả cuối cùng khớp với đáp án mẫu: `6`.

---

## 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — lấy vị trí giữa mà quên xếp:
```python
n = int(input().strip())
a = list(map(int, input().split()))
print(a[n // 2])
```
Với mẫu trên, `a[2]` của dãy gốc là `8`, không khớp đáp án mẫu `6`. Cách sửa: gọi `a.sort()` trước khi lấy.
- Bẫy 2 — lấy lệch sang vị trí kế bên:
```python
n = int(input().strip())
a = list(map(int, input().split()))
a.sort()
print(a[n // 2 + 1])
```
Với mẫu trên in ra `a[3] = 8` sai. Cách sửa: vị trí giữa đếm từ 0 là `a[n // 2]`.
- Bẫy 3 — lấy trung bình của dãy thay vì bạn đứng giữa:
```python
n = int(input().strip())
a = list(map(int, input().split()))
print(sum(a) / n)
```
Với mẫu trên in ra `6.0` có dấu chấm, không khớp đáp án mẫu `6`. Cách sửa: xếp rồi nhặt phần tử giữa bằng `a[n // 2]`.

---

## 4. Lời giải tham khảo

```python
n = int(input().strip())
a = list(map(int, input().split()))
a.sort()
print(a[n // 2])
```
