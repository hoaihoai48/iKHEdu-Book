# Bài 12: Thống kê danh sách và sắp xếp

## 1. Sức mạnh của thống kê — Từ dữ liệu thô đến thông tin có giá trị

Ở bài trước, ta đã biết tạo, nhập và làm việc cơ bản với danh sách. Bài này học cách **khai thác dữ liệu**: tìm số lớn nhất, nhỏ nhất, tính trung bình, đếm theo điều kiện, và đặc biệt là **sắp xếp danh sách**.

Khi dữ liệu đã gọn gàng theo thứ tự, nhiều bài toán khó bỗng trở nên dễ hơn rất nhiều.

---

## 2. Các hàm thống kê tích hợp sẵn trong Python

Python có sẵn các hàm thống kê dùng được ngay trên danh sách:

| Hàm | Cú pháp | Kết quả | Ví dụ |
|---|---|---|---|
| **Tổng** | `sum(a)` | Tổng tất cả phần tử | `sum([3, 7, 2])` → `12` |
| **Lớn nhất** | `max(a)` | Phần tử lớn nhất | `max([3, 7, 2])` → `7` |
| **Nhỏ nhất** | `min(a)` | Phần tử nhỏ nhất | `min([3, 7, 2])` → `2` |
| **Số phần tử** | `len(a)` | Độ dài danh sách | `len([3, 7, 2])` → `3` |

### 2.1. Tính trung bình cộng

```python
a = list(map(int, input().split()))
trung_binh = sum(a) / len(a)
print(round(trung_binh, 2))
```

> **Lưu ý:** `sum(a) / len(a)` luôn ra số thực (`float`). Nếu bài yêu cầu số nguyên, em dùng `sum(a) // len(a)`.

### 2.2. Tự viết hàm tìm max (không dùng `max()`)

Nhiều bài tập yêu cầu tự viết các bước tìm kiếm, không dùng hàm có sẵn:

```python
a = list(map(int, input().split()))
lon_nhat = a[0]
vi_tri = 0
for i in range(1, len(a)):
    if a[i] > lon_nhat:
        lon_nhat = a[i]
        vi_tri = i
print("Max:", lon_nhat, "- Vi tri:", vi_tri)
```

**Cách nghĩ:** Tạm coi phần tử đầu là lớn nhất, rồi đi kiểm tra từng phần tử còn lại — gặp số lớn hơn thì ghi nhận lại.

---

## 3. Sắp xếp danh sách — Nền tảng của thuật toán

### 3.1. Sắp xếp bằng hàm tích hợp

Python có hai cách sắp xếp:

| Cách | Cú pháp | Thay đổi gốc? | Trả về |
|---|---|:---:|---|
| **Tại chỗ (in-place)** | `a.sort()` | Có | `None` |
| **Tạo bản mới** | `sorted(a)` | Không | Danh sách mới đã sắp |

```python
a = [5, 2, 8, 1, 9]

# Cách 1: Sắp xếp tại chỗ
a.sort()          # a = [1, 2, 5, 8, 9]

# Cách 2: Tạo bản sao đã sắp
b = [5, 2, 8, 1, 9]
c = sorted(b)     # c = [1, 2, 5, 8, 9], b VẪN = [5, 2, 8, 1, 9]
```

### 3.2. Sắp xếp giảm dần

```python
a = [5, 2, 8, 1, 9]
a.sort(reverse=True)   # a = [9, 8, 5, 2, 1]
# Hoặc:
c = sorted(a, reverse=True)
```

### 3.3. Minh họa trực quan quá trình sắp xếp

Dữ liệu ban đầu: `[5, 2, 8, 1, 9]`

| Bước | Trạng thái | Hành động |
|------|-----------|-----------|
| Ban đầu | `[5, 2, 8, 1, 9]` | — |
| Sau `sort()` | `[1, 2, 5, 8, 9]` | Sắp tăng dần |
| Sau `sort(reverse=True)` | `[9, 8, 5, 2, 1]` | Sắp giảm dần |

---

## 4. Lọc phần tử trùng lặp trong danh sách

### 4.1. Phương pháp chính chuẩn tư duy: Duyệt danh sách và kiểm tra `not in`

Cách tự nhiên và an toàn để bỏ chỗ trùng mà vẫn **giữ đúng thứ tự xuất hiện** là làm một danh sách kết quả mới, rồi duyệt từng phần tử để kiểm tra bằng `not in`:

```python
a = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
ket_qua = []

for x in a:
    if x not in ket_qua:
        ket_qua.append(x)

print(ket_qua)  # [3, 1, 4, 5, 9, 2, 6] (Giữ nguyên trật tự xuất hiện!)
```

### 4.2. Phương pháp sau khi sắp xếp: So sánh phần tử liền kề

Nếu danh sách đã tăng dần nhờ `a.sort()`, các số giống nhau sẽ đứng cạnh nhau. Ta chỉ cần bỏ qua số nào giống số ngay trước nó:

```python
a.sort()
unique_sorted = []
for i in range(len(a)):
    if i == 0 or a[i] != a[i - 1]:
        unique_sorted.append(a[i])

print(unique_sorted)  # [1, 2, 3, 4, 5, 6, 9]
```

### 4.3. Mẹo ngắn gọn trong Python (Mở rộng): Dùng `set()`

Kiểu `set()` tự bỏ chỗ trùng. Nhưng `set()` không giữ thứ tự ban đầu, nên khi cần danh sách tăng dần không trùng, em có thể viết gọn:

```python
unique = sorted(list(set(a)))
print(unique)  # [1, 2, 3, 4, 5, 6, 9]
```

---

## 5. Ứng dụng thống kê và sắp xếp trong bài toán thực tế

### 5.1. Tìm phần tử lớn thứ 2

```python
a = list(map(int, input().split()))
unique = sorted(set(a), reverse=True)
if len(unique) >= 2:
    print(unique[1])
else:
    print("Khong ton tai")
```

### 5.2. Tính khoảng cách giữa phần tử lớn nhất và nhỏ nhất

```python
a = list(map(int, input().split()))
print(max(a) - min(a))
```

### 5.3. Đếm tần suất xuất hiện của từng phần tử

```python
a = list(map(int, input().split()))
for x in sorted(set(a)):
    print(x, "xuat hien", a.count(x), "lan")
```

---

## 6. Bảng mô phỏng biến thiên ô nhớ

### Chương trình tìm max và vị trí của max

```python
a = [4, 9, 2, 7]
lon_nhat = a[0]
vi_tri = 0
for i in range(1, len(a)):
    if a[i] > lon_nhat:
        lon_nhat = a[i]
        vi_tri = i
print(lon_nhat, vi_tri)
```

| Vòng lặp | `i` | `a[i]` | `a[i] > lon_nhat`? | `lon_nhat` | `vi_tri` |
|---|:---:|:---:|:---:|:---:|:---:|
| Ban đầu | — | — | — | $4$ | $0$ |
| `i = 1` | $1$ | $9$ | $9 > 4$? Đúng | $9$ | $1$ |
| `i = 2` | $2$ | $2$ | $2 > 9$? Sai | $9$ | $1$ |
| `i = 3` | $3$ | $7$ | $7 > 9$? Sai | $9$ | $1$ |
| **Kết thúc** | — | — | — | **In: $9$** | **In: $1$** |

---

## 7. Lỗi hay gặp và bẫy lỗi kinh điển

### 7.1. Bẫy 1: Gán `b = a` không tạo bản sao

```python
a = [1, 2, 3]
b = a        # b và a cùng trỏ đến một danh sách!
b[0] = 99
print(a)     # [99, 2, 3] — a CŨNG bị thay đổi!

# ĐÚNG: Tạo bản sao thực sự
b = a[:]     # Hoặc b = list(a) hoặc b = a.copy()
b[0] = 99
print(a)     # [1, 2, 3] — a KHÔNG bị ảnh hưởng
```

> **Lưu ý:** Đây là bẫy **dễ mắc nhất** khi làm việc với danh sách. Phép gán `b = a` chỉ tạo thêm một tên gọi mới cho cùng một vùng nhớ.

### 7.2. Bẫy 2: Dùng kết quả trả về của `a.sort()` bị `None`

```python
a = [3, 1, 2]
# SAI: sort() trả về None
b = a.sort()
print(b)  # None!

# ĐÚNG: Dùng sorted() nếu cần gán kết quả
b = sorted(a)
```

### 7.3. Bẫy 3: Dùng `max()` hoặc `min()` trên danh sách rỗng

```python
a = []
# max(a)  # ValueError: max() arg is an empty sequence

# ĐÚNG: Kiểm tra trước
if len(a) > 0:
    print(max(a))
```

### 7.4. Bẫy 4: Nhầm `count()` với `len()`

```python
a = [1, 2, 2, 3, 2]
print(a.count(2))   # 3 — Đếm SỐ LẦN xuất hiện của giá trị 2
print(len(a))        # 5 — Tổng số phần tử trong danh sách
```

---

## 8. Mẫu code thường gặp

### 8.1. Nhập mảng, in max, min và mảng sắp xếp tăng dần

```python
a = list(map(int, input().split()))
print("Max:", max(a))
print("Min:", min(a))
a.sort()
print("Sap xep:", *a)
```

### 8.2. Tìm phần tử xuất hiện nhiều nhất

```python
a = list(map(int, input().split()))
max_count = 0
ket_qua = a[0]
for x in set(a):
    if a.count(x) > max_count:
        max_count = a.count(x)
        ket_qua = x
print(ket_qua, max_count)
```

### 8.3. In danh sách phần tử duy nhất (chỉ xuất hiện đúng 1 lần)

```python
a = list(map(int, input().split()))
for x in a:
    if a.count(x) == 1:
        print(x, end=" ")
```
