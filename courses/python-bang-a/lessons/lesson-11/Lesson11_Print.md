# Bài 11: Danh sách và thao tác cơ bản

## 1. Danh sách — Chiếc ngăn kéo thần kỳ chứa nhiều giá trị

Từ Bài 01 đến Bài 10, mỗi biến chỉ giữ được **một giá trị**. Nhưng thực tế ta hay cần xử lý **nhiều giá trị cùng lúc**: điểm cả lớp, nhiệt độ từng ngày, tên học sinh trong lớp...

**Danh sách** cho phép gom **nhiều giá trị vào một biến duy nhất**, như dãy ngăn kéo đánh số thứ tự.

```python
diem = [9, 7, 8, 10, 6]
```

Hình dung trực quan:

| Chỉ số (index) | `0` | `1` | `2` | `3` | `4` |
|---|:---:|:---:|:---:|:---:|:---:|
| Giá trị | $9$ | $7$ | $8$ | $10$ | $6$ |

> 💡 **Mẹo nhớ:** Chỉ số trong Python **luôn bắt đầu từ 0**. Phần tử đầu tiên là index `0`, phần tử tiếp theo là index `1`...

---

## 2. Khai báo và truy cập phần tử

### 2.1. Khai báo danh sách

```python
# Danh sách rỗng
a = []

# Danh sách có sẵn giá trị
diem = [9, 7, 8, 10, 6]
ten = ["An", "Binh", "Chi"]
```

### 2.2. Truy cập phần tử bằng chỉ số

```python
a = [10, 20, 30, 40, 50]
print(a[0])    # In ra: 10  (phần tử ĐẦU TIÊN)
print(a[2])    # In ra: 30  (phần tử thứ 3)
print(a[-1])   # In ra: 50  (phần tử CUỐI CÙNG)
print(a[-2])   # In ra: 40  (phần tử áp cuối)
```

**Quy tắc chỉ số âm:** Đếm ngược từ cuối danh sách. `-1` là cuối cùng, `-2` là áp cuối...

| Chỉ số dương | `0` | `1` | `2` | `3` | `4` |
|---|:---:|:---:|:---:|:---:|:---:|
| Giá trị | $10$ | $20$ | $30$ | $40$ | $50$ |
| Chỉ số âm | `-5` | `-4` | `-3` | `-2` | `-1` |

### 2.3. Thay đổi giá trị phần tử

Danh sách (`list`) **cho phép thay đổi giá trị tại bất kỳ vị trí nào**:

```python
a = [1, 2, 3]
a[1] = 99      # Gán đè phần tử thứ 2
print(a)       # In ra: [1, 99, 3]
```

---

## 3. Nhập danh sách từ bàn phím — Cú pháp phổ biến

### 3.1. Nhập danh sách số nguyên trên một dòng

Cú pháp **cần thuộc lòng**, gặp trong hầu hết các bài:

```python
a = list(map(int, input().split()))
```

**Từng bước hoạt động:**

| Bước | Biểu thức | Kết quả | Giải thích |
|------|-----------|---------|------------|
| 1 | `input()` | `"3 7 1 9"` | Đọc cả dòng dưới dạng chuỗi |
| 2 | `.split()` | `["3", "7", "1", "9"]` | Tách thành danh sách các chuỗi con |
| 3 | `map(int, ...)` | `map object` | Áp dụng `int()` lên từng chuỗi con |
| 4 | `list(...)` | `[3, 7, 1, 9]` | Chuyển thành danh sách số nguyên |

### 3.2. Nhập danh sách với $N$ phần tử mỗi dòng

```python
n = int(input())
a = []
for i in range(n):
    x = int(input())
    a.append(x)
```

### 3.3. Xuất danh sách trên một dòng cách nhau bởi dấu cách

```python
a = [3, 7, 1, 9]
print(*a)           # In ra: 3 7 1 9
# Hoặc tường minh:
print(*a, sep=" ")   # In ra: 3 7 1 9
```

> 💡 **Mẹo nhớ:** Dấu sao `*` trước tên danh sách nghĩa là "tách ra": `*a` thành `3, 7, 1, 9` — các giá trị riêng lẻ đưa cho `print()`.

---

## 4. Các phương thức thao tác danh sách quan trọng

### 4.1. Bảng tổng hợp phương thức

| Phương thức | Cú pháp | Ý nghĩa | Ví dụ |
|---|---|---|---|
| **Thêm cuối** | `a.append(x)` | Nối $x$ vào cuối danh sách | `a.append(5)` |
| **Chèn vào vị trí** | `a.insert(i, x)` | Chèn $x$ vào vị trí index $i$ | `a.insert(0, 100)` |
| **Xóa theo giá trị** | `a.remove(x)` | Xóa phần tử **đầu tiên** có giá trị $x$ | `a.remove(20)` |
| **Xóa theo vị trí** | `a.pop(i)` | Xóa và trả về phần tử tại index $i$ | `a.pop(0)` |
| **Xóa cuối** | `a.pop()` | Xóa và trả về phần tử cuối cùng | `a.pop()` |
| **Độ dài** | `len(a)` | Số lượng phần tử | `len([1,2,3])` → `3` |
| **Kiểm tra tồn tại** | `x in a` | `True` nếu $x$ có trong `a` | `5 in [1,5,9]` → `True` |
| **Đảo ngược** | `a.reverse()` | Đảo thứ tự tại chỗ | `[1,2,3]` → `[3,2,1]` |
| **Xóa sạch** | `a.clear()` | Xóa toàn bộ, `a` thành `[]` | `a.clear()` |
| **Nối hai danh sách** | `a + b` | Tạo danh sách mới ghép nối | `[1,2] + [3]` → `[1,2,3]` |
| **Nhân bản** | `a * k` | Lặp lại danh sách $k$ lần | `[1,2] * 3` → `[1,2,1,2,1,2]` |

### 4.2. Minh họa chi tiết `remove()` — Chỉ xóa phần tử đầu tiên

```python
a = [10, 20, 30, 20, 40]
a.remove(20)
print(a)  # [10, 30, 20, 40] — CHỈ xóa số 20 ĐẦU TIÊN gặp được
```

> **Lưu ý:** Nếu giá trị không có trong danh sách, `remove()` sẽ gây lỗi `ValueError`. Em kiểm tra `if x in a:` trước khi gọi nhé.

---

## 5. Duyệt danh sách bằng vòng lặp

### 5.1. Duyệt trực tiếp từng phần tử (`for x in a`)

```python
a = [3, 7, 1, 9, 5]
for x in a:
    print(x, end=" ")
# In ra: 3 7 1 9 5
```

### 5.2. Duyệt theo chỉ số (`for i in range(len(a))`)

```python
a = [3, 7, 1, 9, 5]
for i in range(len(a)):
    print(f"a[{i}] = {a[i]}")
```

Kết quả:
```text
a[0] = 3
a[1] = 7
a[2] = 1
a[3] = 9
a[4] = 5
```

### 5.3. Tính tổng, đếm, tìm max/min bằng vòng lặp

```python
a = list(map(int, input().split()))
tong = 0
dem_chan = 0
for x in a:
    tong += x
    if x % 2 == 0:
        dem_chan += 1
print("Tong:", tong)
print("So phan tu chan:", dem_chan)
```

---

## 6. Cắt danh sách

Cú pháp cắt danh sách giống hệt cắt chuỗi:

```python
a = [10, 20, 30, 40, 50]
print(a[1:3])    # [20, 30]     — Từ index 1 đến 2 (không lấy 3)
print(a[:3])     # [10, 20, 30] — Từ đầu đến index 2
print(a[2:])     # [30, 40, 50] — Từ index 2 đến hết
print(a[::2])    # [10, 30, 50] — Cách 2 phần tử
print(a[::-1])   # [50, 40, 30, 20, 10] — Đảo ngược
```

| Cú pháp | Bắt đầu | Kết thúc | Bước nhảy | Kết quả |
|---|:---:|:---:|:---:|---|
| `a[1:3]` | 1 | 3 | 1 | `[20, 30]` |
| `a[:3]` | 0 | 3 | 1 | `[10, 20, 30]` |
| `a[2:]` | 2 | hết | 1 | `[30, 40, 50]` |
| `a[::2]` | 0 | hết | 2 | `[10, 30, 50]` |
| `a[::-1]` | cuối | đầu | -1 | `[50, 40, 30, 20, 10]` |

---

## 7. Bảng mô phỏng biến thiên ô nhớ

### Chương trình đếm số lẻ trong danh sách

```python
a = [4, 7, 2, 9, 6]
dem = 0
for x in a:
    if x % 2 == 1:
        dem += 1
print(dem)
```

| Vòng lặp | `x` | `x % 2 == 1` | `dem` |
|---|:---:|:---:|:---:|
| Ban đầu | — | — | $0$ |
| Lần 1 | $4$ | `False` | $0$ |
| Lần 2 | $7$ | `True` | $1$ |
| Lần 3 | $2$ | `False` | $1$ |
| Lần 4 | $9$ | `True` | $2$ |
| Lần 5 | $6$ | `False` | $2$ |
| **Kết thúc** | — | — | **In ra: $2$** |

---

## 8. Lỗi hay gặp và bẫy lỗi kinh điển

### 8.1. Bẫy 1: Truy cập index vượt phạm vi (IndexError)

```python
a = [10, 20, 30]
print(a[3])  # IndexError! Chỉ có index 0, 1, 2
print(a[2])  # Phần tử cuối cùng
```

> **Lưu ý:** Danh sách $n$ phần tử có index từ $0$ đến $n - 1$. Index $n$ luôn gây lỗi.

### 8.2. Bẫy 2: Quên ép kiểu khi nhập danh sách

```python
# SAI: Tạo danh sách các chuỗi, không phải số
a = input().split()  # ["3", "7", "1"]
print(a[0] + a[1])   # "37" (nối chuỗi, không phải cộng số!)

# ĐÚNG: Ép kiểu int
a = list(map(int, input().split()))
print(a[0] + a[1])   # 10 (cộng số)
```

### 8.3. Bẫy 3: Dùng `remove()` khi giá trị không tồn tại

```python
a = [1, 2, 3]
# a.remove(99)  # ValueError: list.remove(x): x not in list

# ĐÚNG: Kiểm tra trước
if 99 in a:
    a.remove(99)
```

### 8.4. Bẫy 4: Nhầm lẫn `a.sort()` và `sorted(a)`

```python
a = [3, 1, 2]

# a.sort() thay đổi trực tiếp danh sách gốc
a.sort()      # a = [1, 2, 3]

# sorted(a) tạo danh sách MỚI, giữ nguyên gốc
b = [3, 1, 2]
c = sorted(b)  # c = [1, 2, 3], b VẪN = [3, 1, 2]
```

### 8.5. Bẫy 5: Xóa phần tử trong khi đang duyệt

```python
# SAI: Bỏ sót phần tử khi xóa
a = [1, 2, 3, 2, 4]
for x in a:
    if x == 2:
        a.remove(x)
print(a)  # [1, 3, 4]? KHÔNG! Kết quả là [1, 3, 2, 4] — bỏ sót 1 số 2

# ĐÚNG: Tạo danh sách mới
a = [1, 2, 3, 2, 4]
a = [x for x in a if x != 2]
print(a)  # [1, 3, 4]
```

---

## 9. Mẫu code thường gặp

### 9.1. Tìm giá trị lớn nhất trong danh sách (không dùng `max()`)

```python
a = list(map(int, input().split()))
lon_nhat = a[0]
for i in range(1, len(a)):
    if a[i] > lon_nhat:
        lon_nhat = a[i]
print(lon_nhat)
```

### 9.2. Đếm phần tử thỏa điều kiện

```python
a = list(map(int, input().split()))
dem = 0
for x in a:
    if x > 0:
        dem += 1
print(dem)
```

### 9.3. Đảo ngược danh sách và in

```python
a = list(map(int, input().split()))
print(*a[::-1])
```
