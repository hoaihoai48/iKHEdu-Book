# Hướng Dẫn Giảng Dạy: Lấy chữ số đơn vị & chục
Chuyên đề: **Bí Mật Tách Chữ Số (// 10 và % 10)**

---

## 1. Ý tưởng & Phân tích thuật toán

- Bản chất của bài này là tách số có 2 chữ số thành chữ số hàng chục và chữ số hàng đơn vị.
- Quy trình từng bước với đúng tên biến trong lời giải:
  - Bước 1: `n = int(input())` đọc số. Với mẫu, `n = 47`.
  - Bước 2: `don_vi = n % 10` lấy phần dư khi chia 10, tức chữ số cuối. Với mẫu, `don_vi = 7`.
  - Bước 3: sao chép `temp = n` rồi lặp `while temp >= 10: temp = temp // 10` để gọt dần tới khi còn chữ số đầu. Với mẫu, `temp` đi từ 47 về 4.
  - Bước 4: gán `chuc = temp` rồi in `print(chuc, don_vi)` được `4 7`.
- Giá trị biên cụ thể: số nhỏ nhất là 10 (chục 1, đơn vị 0), số lớn nhất là 99 (chục 9, đơn vị 9).

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 47)

| Bước | Lệnh chạy | `n` | `don_vi` | `temp` | `chuc` | In ra |
|---|---|---|---|---|---|---|
| 1 | `n = int(input())` với `47` | 47 | — | — | — | (chưa in) |
| 2 | `don_vi = 47 % 10` | 47 | 7 | — | — | (chưa in) |
| 3 | `temp = n` | 47 | 7 | 47 | — | (chưa in) |
| 4 | `47 >= 10` đúng nên `temp = 47 // 10` | 47 | 7 | 4 | — | (chưa in) |
| 5 | `4 >= 10` sai, dừng lặp | 47 | 7 | 4 | — | (chưa in) |
| 6 | `chuc = temp`, in `chuc, don_vi` | 47 | 7 | 4 | 4 | `4 7` |

- Kết quả cuối `4 7` trùng kết quả mẫu.

---

## 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1: in ngược thứ tự `print(don_vi, chuc)`. Với mẫu sẽ ra `7 4`, là kết quả sai vì đề bài yêu cầu chục trước đơn vị sau. Cách sửa: in `print(chuc, don_vi)`.
```python
n = int(input())
don_vi = n % 10
temp = n
while temp >= 10:
    temp = temp // 10
chuc = temp
print(don_vi, chuc)
```
- Bẫy 2: lấy chữ số chục bằng `n // 10` mà quên vòng lặp vẫn đúng với 2 chữ số, nhưng nếu viết `chuc = n % 10` nhầm thì cả hai đều là 7. Với mẫu sẽ in `7 7`, là kết quả sai. Cách sửa: chục lấy từ `temp` sau khi gọt, đơn vị lấy từ `n % 10`.
```python
n = int(input())
don_vi = n % 10
chuc = n % 10
print(chuc, don_vi)
```
- Bẫy 3: in mỗi chữ số một dòng bằng hai lệnh `print(chuc)` rồi `print(don_vi)`. Với mẫu sẽ in hai dòng `4` và `7`, là kết quả sai vì đề bài yêu cầu cùng một dòng. Cách sửa: in một lần `print(chuc, don_vi)`.
```python
n = int(input())
don_vi = n % 10
temp = n
while temp >= 10:
    temp = temp // 10
chuc = temp
print(chuc)
print(don_vi)
```

---

## 4. Lời giải tham khảo

```python
n = int(input())
don_vi = n % 10
temp = n
while temp >= 10:
    temp = temp // 10
chuc = temp
print(chuc, don_vi)
```
