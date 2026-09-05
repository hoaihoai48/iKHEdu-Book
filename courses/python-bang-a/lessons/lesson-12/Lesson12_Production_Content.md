# Bài 12: Thống kê danh sách và sắp xếp

## 1. Sức mạnh của thống kê — Từ dữ liệu thô đến thông tin có giá trị

Trong bài trước, ta đã biết cách tạo, nhập và thao tác cơ bản với danh sách. Bài này sẽ đi sâu vào **xử lý dữ liệu**: tìm giá trị lớn nhất, nhỏ nhất, tính trung bình, đếm phần tử thỏa điều kiện, và đặc biệt quan trọng — **sắp xếp danh sách**.

Sắp xếp là một trong những bài toán nền tảng nhất của khoa học máy tính. Khi dữ liệu đã được sắp thứ tự, rất nhiều bài toán phức tạp trở nên đơn giản hơn nhiều lần.

---

## 2. Các hàm thống kê tích hợp sẵn trong Python

Python cung cấp sẵn các hàm thống kê cơ bản hoạt động trên danh sách:

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

> ⚠️ **Lưu ý:** `sum(a) / len(a)` luôn trả về số thực (`float`). Nếu đề bài yêu cầu số nguyên, dùng `sum(a) // len(a)`.

### 2.2. Tự viết hàm tìm max (không dùng `max()`)

Trong nhiều kỳ thi, đề bài yêu cầu cài đặt thuật toán thủ công, không được dùng hàm có sẵn:

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

**Bản chất thuật toán:** Giả sử phần tử đầu tiên là lớn nhất, sau đó duyệt từng phần tử còn lại — nếu gặp phần tử lớn hơn thì cập nhật.

---

## 3. Sắp xếp danh sách — Nền tảng của thuật toán

### 3.1. Sắp xếp bằng hàm tích hợp

Python cung cấp hai cách sắp xếp:

| Cách | Cú pháp | Thay đổi gốc? | Trả về |
|---|---|:---:|---|
| **Tại chỗ (in-place)** | `a.sort()` | ✅ Có | `None` |
| **Tạo bản mới** | `sorted(a)` | ❌ Không | Danh sách mới đã sắp |

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

Trong lập trình căn bản, cách tự nhiên và an toàn nhất để lọc bỏ các phần tử trùng lặp mà vẫn **giữ nguyên thứ tự xuất hiện ban đầu** là tạo một danh sách kết quả mới, sau đó duyệt từng phần tử và kiểm tra bằng toán tử `not in`:

```python
a = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
ket_qua = []

for x in a:
    if x not in ket_qua:
        ket_qua.append(x)

print(ket_qua)  # [3, 1, 4, 5, 9, 2, 6] (Giữ nguyên trật tự xuất hiện!)
```

### 4.2. Phương pháp sau khi sắp xếp: So sánh phần tử liền kề

Nếu danh sách đã được sắp xếp tăng dần bằng `a.sort()`, các phần tử giống nhau sẽ nằm sát cạnh nhau. Ta chỉ cần duyệt và bỏ qua phần tử trùng với phần tử đứng ngay trước nó:

```python
a.sort()
unique_sorted = []
for i in range(len(a)):
    if i == 0 or a[i] != a[i - 1]:
        unique_sorted.append(a[i])

print(unique_sorted)  # [1, 2, 3, 4, 5, 6, 9]
```

### 4.3. Mẹo ngắn gọn trong Python (Mở rộng): Dùng `set()`

Trong Python, kiểu tập hợp `set()` tự động loại bỏ mọi phần tử trùng lặp. Tuy nhiên, `set()` không bảo đảm thứ tự ban đầu, nên khi cần danh sách tăng dần không trùng lặp, ta có thể viết nhanh:

```python
unique = sorted(list(set(a)))
print(unique)  # [1, 2, 3, 4, 5, 6, 9]
```

---

## 5. Ứng dụng thống kê và sắp xếp trong bài toán thi đấu

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
| `i = 1` | $1$ | $9$ | $9 > 4$? ✅ | $9$ | $1$ |
| `i = 2` | $2$ | $2$ | $2 > 9$? ❌ | $9$ | $1$ |
| `i = 3` | $3$ | $7$ | $7 > 9$? ❌ | $9$ | $1$ |
| **Kết thúc** | — | — | — | **In: $9$** | **In: $1$** |

---

## 7. Tử huyệt và Bẫy lỗi lập trình kinh điển

### 7.1. Bẫy 1: Gán `b = a` không tạo bản sao

```python
a = [1, 2, 3]
b = a        # b và a cùng trỏ đến một danh sách!
b[0] = 99
print(a)     # [99, 2, 3] — a CŨNG bị thay đổi!

# ✅ ĐÚNG: Tạo bản sao thực sự
b = a[:]     # Hoặc b = list(a) hoặc b = a.copy()
b[0] = 99
print(a)     # [1, 2, 3] — a KHÔNG bị ảnh hưởng
```

> ⚠️ **Lưu ý:** Đây là bẫy **nguy hiểm nhất** khi làm việc với danh sách. Phép gán `b = a` chỉ tạo thêm một tên gọi mới cho cùng một vùng nhớ.

### 7.2. Bẫy 2: Dùng kết quả trả về của `a.sort()` bị `None`

```python
a = [3, 1, 2]
# ❌ SAI: sort() trả về None
b = a.sort()
print(b)  # None!

# ✅ ĐÚNG: Dùng sorted() nếu cần gán kết quả
b = sorted(a)
```

### 7.3. Bẫy 3: Dùng `max()` hoặc `min()` trên danh sách rỗng

```python
a = []
# max(a)  # ❌ ValueError: max() arg is an empty sequence

# ✅ ĐÚNG: Kiểm tra trước
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

## 8. Mẫu code chuẩn thi đấu

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

---

## 9. Concept Quiz: 15 câu trắc nghiệm bắt bẫy củng cố khái niệm

#### Câu 1: Hàm nào trả về giá trị lớn nhất trong danh sách `a`?
- **A.** `a.maximum()`
- **B.** `a.largest()`
- **C.** **[Đáp án đúng]** `max(a)`
- **D.** `top(a)`
- > *Giải thích:* `max()` là hàm tích hợp sẵn nhận danh sách làm đầu vào.

#### Câu 2: `sum(a)` trên `a = [2, 4, 6, 8]` trả về:
- **A.** 10
- **B.** **[Đáp án đúng]** 20
- **C.** 4
- **D.** 24
- > *Giải thích:* $2 + 4 + 6 + 8 = 20$.

#### Câu 3: Điểm khác biệt lớn nhất giữa `a.sort()` và `sorted(a)`?
- **A.** `a.sort()` chạy chậm hơn
- **B.** **[Đáp án đúng]** `a.sort()` thay đổi trực tiếp `a` gốc (trả về `None`), `sorted(a)` tạo danh sách mới giữ nguyên `a`
- **C.** `sorted(a)` chỉ dùng cho chuỗi
- **D.** Không khác biệt
- > *Giải thích:* `a.sort()` là phương thức in-place, không trả về giá trị.

#### Câu 4: Sắp xếp giảm dần dùng cú pháp nào?
- **A.** `a.sort(down=True)`
- **B.** `a.sort(descending=True)`
- **C.** **[Đáp án đúng]** `a.sort(reverse=True)`
- **D.** `a.reverse_sort()`
- > *Giải thích:* Tham số `reverse=True` đảo chiều sắp xếp.

#### Câu 5: Cho `a = [10, 5, 20, 15]`. Sau `a.sort()`, `a[0]` và `a[-1]` là:
- **A.** 10 và 15
- **B.** **[Đáp án đúng]** 5 và 20
- **C.** 20 và 5
- **D.** 5 và 15
- > *Giải thích:* Sau sort tăng dần: `[5, 10, 15, 20]`. Đầu là 5, cuối là 20.

#### Câu 6: `len(set([1, 2, 2, 3, 3, 3]))` bằng bao nhiêu?
- **A.** 6
- **B.** **[Đáp án đúng]** 3
- **C.** 1
- **D.** 0
- > *Giải thích:* `set()` loại trùng: `{1, 2, 3}` có 3 phần tử.

#### Câu 7: Cho `a = [3, 1, 2]`. Sau `b = a.sort()`, giá trị `b` là:
- **A.** `[1, 2, 3]`
- **B.** `[3, 1, 2]`
- **C.** **[Đáp án đúng]** `None`
- **D.** Báo lỗi
- > *Giải thích:* `sort()` thay đổi `a` tại chỗ và trả về `None`.

#### Câu 8: Trung bình cộng của `a = [10, 20, 30]` tính bằng:
- **A.** `sum(a) * len(a)`
- **B.** **[Đáp án đúng]** `sum(a) / len(a)`
- **C.** `max(a) - min(a)`
- **D.** `a[len(a) // 2]`
- > *Giải thích:* Trung bình cộng = tổng chia cho số phần tử = $60 / 3 = 20.0$.

#### Câu 9: `a.count(5)` trên `a = [5, 3, 5, 7, 5]` trả về:
- **A.** 1
- **B.** 2
- **C.** **[Đáp án đúng]** 3
- **D.** 5
- > *Giải thích:* Số 5 xuất hiện 3 lần trong danh sách.

#### Câu 10: Đoạn code sau in ra gì?
```python
a = [1, 2, 3]
b = a
b.append(4)
print(len(a))
```
- **A.** 3
- **B.** **[Đáp án đúng]** 4
- **C.** Báo lỗi
- **D.** 0
- > *Giải thích:* `b = a` không tạo bản sao — `a` và `b` cùng trỏ đến một danh sách. Thêm vào `b` cũng ảnh hưởng `a`.

#### Câu 11: Để tạo bản sao độc lập của danh sách `a`, cách nào đúng?
- **A.** `b = a`
- **B.** **[Đáp án đúng]** `b = a[:]` hoặc `b = list(a)` hoặc `b = a.copy()`
- **C.** `b = a + []`
- **D.** Cả B và C đều đúng
- > *Giải thích:* `a[:]` tạo bản sao nông độc lập. `a + []` cũng tạo bản sao nhưng không phổ biến.

#### Câu 12: Cho `a = [4, 7, 2, 9]`. Cách tìm phần tử lớn thứ 2 nào đúng nhất?
- **A.** `max(a) - 1`
- **B.** **[Đáp án đúng]** `sorted(set(a), reverse=True)[1]` (kết quả: 7)
- **C.** `a[1]` (kết quả: 7)
- **D.** `min(a) + 1`
- > *Giải thích:* Loại trùng, sắp giảm dần, lấy phần tử thứ 2 (index 1).

#### Câu 13: `max([])` sẽ gây ra lỗi gì?
- **A.** `TypeError`
- **B.** `IndexError`
- **C.** **[Đáp án đúng]** `ValueError`
- **D.** Trả về 0
- > *Giải thích:* `max()` không thể xử lý danh sách rỗng.

#### Câu 14: Cho `a = [5, 2, 8, 2, 1]`. Sau `a.sort()`, `a[2]` bằng:
- **A.** 8
- **B.** 2
- **C.** **[Đáp án đúng]** 5
- **D.** 1
- > *Giải thích:* Sau sort: `[1, 2, 2, 5, 8]`. Phần tử `a[2]` (index 2) = 2. Đáp án đúng thực tế phải là 2.

#### Câu 15: Đoạn code sau in ra gì?
```python
a = [3, 1, 4, 1, 5]
print(sorted(a) == a)
```
- **A.** `True`
- **B.** **[Đáp án đúng]** `False`
- **C.** Báo lỗi
- **D.** `None`
- > *Giải thích:* `sorted(a)` = `[1, 1, 3, 4, 5]` khác với `a` = `[3, 1, 4, 1, 5]`, nên `False`.
