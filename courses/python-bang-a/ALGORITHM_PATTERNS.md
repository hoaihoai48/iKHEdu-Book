# ALGORITHM PATTERNS — PYTHON BẢNG A LEVEL 1

Các mẫu dưới đây là thẻ nhớ dùng xuyên suốt khóa học. Học sinh cần nhận ra mẫu, hiểu điều kiện dùng và tự thay đổi phần điều kiện hoặc phép cập nhật.

## 1. Input → Process → Output

```python
du_lieu = int(input())
ket_qua = du_lieu + 5
print(ket_qua)
```

## 2. Counting

```python
dem = 0
for x in day:
    if dieu_kien(x):
        dem += 1
```

## 3. Sum / Accumulator

```python
tong = 0
for x in day:
    tong += x
```

## 4. Maximum hoặc minimum

```python
lon_nhat = day[0]
for x in day[1:]:
    if x > lon_nhat:
        lon_nhat = x
```

## 5. Flag / Search

```python
found = False
for x in day:
    if dieu_kien(x):
        found = True
        break
```

## 6. Digit extraction

```python
while n > 0:
    digit = n % 10
    n //= 10
```

## 7. Nested loop

```python
for i in range(so_hang):
    for j in range(so_cot):
        xu_ly(i, j)
```

Hai vòng lặp lồng nhau thường cần kiểm tra lại với giới hạn $N$ trước khi dùng.

## 8. Rolling variables

```python
a, b = b, a + b
```

Mẫu này phù hợp với Fibonacci và các dãy mà trạng thái mới phụ thuộc vào một vài trạng thái ngay trước đó.

## 9. String traversal

```python
for ch in s:
    xu_ly(ch)
```

Khi cần vị trí, dùng `for i in range(len(s))`.

## 10. List traversal

```python
for x in a:
    xu_ly(x)

for i in range(len(a)):
    a[i] = bien_doi(a[i])
```

Dùng cách thứ nhất khi chỉ cần giá trị; dùng cách thứ hai khi cần index hoặc thay đổi phần tử.

## 11. Nghĩ về tốc độ

| Dấu hiệu | Mẫu thường gặp | Cần nhớ |
|---|---|---|
| Không phụ thuộc $N$ | Công thức trực tiếp | $\mathcal{O}(1)$ |
| Duyệt một lần | Một vòng lặp qua $N$ phần tử | $\mathcal{O}(N)$ |
| Duyệt lồng nhau | Hai vòng lặp theo $N$ | $\mathcal{O}(N^2)$ |
| Mỗi bước giảm một phần | Tách chữ số hoặc chia đôi | Thường nhỏ hơn $\mathcal{O}(N)$ |

Trước khi chọn vòng lặp, luôn hỏi: $N$ lớn đến đâu và số lần lặp thực tế là bao nhiêu?