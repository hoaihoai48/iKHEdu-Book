# Hướng Dẫn Giảng Dạy: Đếm kẹo chẵn lẻ
Chuyên đề: **Chiếc Hộp Thần Kỳ list & Thao Tác Cơ Bản**

---

## 1. Ý tưởng & Phân tích thuật toán

- Bản chất của bài này là đếm gói chẵn rồi suy ra gói lẻ bằng phép trừ, vì mỗi gói chỉ thuộc một mâm.
- Với số mẫu `N = 6`, các gói `1 2 3 4 5 6`: các gói chẵn là `2`, `4`, `6` (3 gói); gói lẻ là `6 - 3 = 3` gói. Đáp án là `3 3`.
- Quy trình trong lời giải với các biến `n`, `data`, `c`, `x`:
  - Đọc `n = 6`, gom đủ 6 số vào `data`, đặt `c = 0`.
  - Với mỗi `x`, nếu `x % 2 == 0` thì tăng `c`: `1` bỏ, `2` đếm 1, `3` bỏ, `4` đếm 2, `5` bỏ, `6` đếm 3.
  - In `c` và `n - c` tức `3 3`.
- Giá trị biên cụ thể: mỗi gói có thể có `0` viên kẹo mà `0` là số chẵn nên vẫn đếm vào mâm chẵn.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 6 / 1 2 3 4 5 6)

| Bước | Thao tác | Giá trị |
|------|----------|---------|
| 1 | Đọc `n` | `n = 6` |
| 2 | Gom `data` | `data = [1, 2, 3, 4, 5, 6]`, `c = 0` |
| 3 | Xét `1`, `2` | `2` chẵn nên `c = 1` |
| 4 | Xét `3`, `4` | `4` chẵn nên `c = 2` |
| 5 | Xét `5`, `6` | `6` chẵn nên `c = 3` |
| 6 | In `c` và `n - c` | màn hình hiện `3 3` |

Kết quả cuối cùng khớp với đáp án mẫu: `3 3`.

---

## 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — đếm gói lẻ bằng vòng lặp riêng nhưng quên chia hai mâm:
```python
n = int(input())
data = []
while len(data) < n:
    data += list(map(int, input().split()))
print(len([x for x in data[:n] if x % 2 == 0]))
```
Với mẫu trên chỉ in ra `3`, thiếu số gói lẻ phía sau. Cách sửa: in cả hai số `print(str(c) + " " + str(n - c))`.
- Bẫy 2 — in mỗi số một dòng:
```python
n = int(input())
data = []
while len(data) < n:
    data += list(map(int, input().split()))
c = 0
for x in data[:n]:
    if x % 2 == 0:
        c += 1
print(c)
print(n - c)
```
Với mẫu trên in ra hai dòng `3` rồi `3`, không khớp đáp án mẫu `3 3` trên một dòng. Cách sửa: in chung một dòng cách nhau bởi dấu cách.
- Bẫy 3 — coi gói `0` viên là gói lẻ:
```python
n = int(input())
data = []
while len(data) < n:
    data += list(map(int, input().split()))
c = 0
for x in data[:n]:
    if x % 2 == 0 and x > 0:
        c += 1
print(str(c) + " " + str(n - c))
```
Với mẫu trên vẫn ra `3 3`, nhưng dãy có gói `0` viên thì gói đó bị đẩy sang mâm lẻ sai. Cách sửa: điều kiện đúng chỉ là `x % 2 == 0`.

---

## 4. Lời giải tham khảo

```python
n = int(input())
data = []
while len(data) < n:
    data += list(map(int, input().split()))
c = 0
for x in data[:n]:
    if x % 2 == 0:
        c += 1
print(str(c) + " " + str(n - c))
```
