# Hướng Dẫn Giảng Dạy: Điểm trung bình môn học
Chuyên đề: **Thống Kê Danh Sách & Sắp Xếp Nâng Cao**

---

## 1. Ý tưởng & Phân tích thuật toán

- Bản chất của bài này là cộng mọi điểm rồi chia cho số bài, sau đó in với đúng 2 chữ số sau dấu chấm.
- Với số mẫu `N = 4`, các điểm `8 9 7 10`: tổng `34` chia `4` được `8.5`, viết đủ 2 chữ số thành `8.50`.
- Quy trình trong lời giải với các biến `n`, `a`, `tb`:
  - Đọc `n = 4`, dãy điểm `a = [8.0, 9.0, 7.0, 10.0]`.
  - Tính `tb = 34.0 / 4 = 8.5`.
  - In theo mẫu 2 chữ số được `8.50`.
- Giá trị biên cụ thể: `N = 1` thì trung bình chính là điểm duy nhất đó (ví dụ `7` thì in `7.00`).

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 4 / 8 9 7 10)

| Bước | Thao tác | Giá trị |
|------|----------|---------|
| 1 | Đọc `n` | `n = 4` |
| 2 | Đọc dãy `a` | `a = [8.0, 9.0, 7.0, 10.0]` |
| 3 | Tính `tb = sum(a) / n` | `34.0 / 4 = 8.5` |
| 4 | In với 2 chữ số | màn hình hiện `8.50` |

Kết quả cuối cùng khớp với đáp án mẫu: `8.50`.

---

## 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — in trực tiếp nên thiếu số 0 cuối:
```python
n = int(input().strip())
a = list(map(float, input().split()))
tb = sum(a) / n
print(tb)
```
Với mẫu trên in ra `8.5`, không khớp đáp án mẫu `8.50`. Cách sửa: in bằng `print(f"{tb:.2f}")`.
- Bẫy 2 — chia nguyên làm mất phần lẻ:
```python
n = int(input().strip())
a = list(map(float, input().split()))
tb = sum(a) // n
print(f"{tb:.2f}")
```
Với mẫu trên `34.0 // 4 = 8.0` nên in ra `8.00` sai. Cách sửa: chia thực bằng `/`.
- Bẫy 3 — đọc điểm bằng số nguyên nên lỗi khi gặp điểm lẻ:
```python
n = int(input().strip())
a = list(map(int, input().split()))
tb = sum(a) / n
print(f"{tb:.2f}")
```
Với mẫu toàn điểm nguyên vẫn ra `8.50`, nhưng điểm `7.5` trong đề là số thực nên `int("7.5")` gây lỗi chương trình. Cách sửa: đọc bằng `map(float, input().split())`.

---

## 4. Lời giải tham khảo

```python
n = int(input().strip())
a = list(map(float, input().split()))
tb = sum(a) / n
print(f"{tb:.2f}")
```
