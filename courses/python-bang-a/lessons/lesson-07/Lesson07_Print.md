# Bài 07: Quy luật dãy số và tam giác số

## 1. Khái niệm & Bản chất của bài toán Dãy số trong lập trình

Dạng bài **Dãy số & Tam giác số** gặp rất nhiều trong bài tập lập trình. Các em học được cách nhìn vài số đầu để đoán quy luật, cách dùng biến cuốn chiếu thay cho mảng lớn, cách điều khiển hàng và cột bằng vòng lặp lồng nhau, và cách dùng công thức toán học cho nhanh thay vì lặp quá nhiều.

---

## 2. Các quy luật dãy số kinh điển

### 2.1. Cấp số cộng
* **Quy luật:** Mỗi số hạng sau bằng số hạng ngay trước nó cộng với một hằng số khoảng cách $d$:
  $$u_n = u_{n-1} + d$$
* **Công thức tổng quát tính số hạng thứ $N$:**
  $$u_N = u_1 + (N - 1) \times d$$
  *Mã Python tính tức thì $\mathcal{O}(1)$:*
  ```python
  u_n = u1 + (n - 1) * d
  ```
* **Công thức tính tổng $N$ số hạng đầu tiên:**
  $$S_N = \frac{N \times (u_1 + u_N)}{2}$$
  *Mã Python:*
  ```python
  tong = (n * (u1 + u_n)) // 2
  ```

### 2.2. Dãy số nhân đôi (Cấp số nhân với công bội $q = 2$)
* **Dãy số:** $1, 2, 4, 8, 16, 32, 64, \dots$
* **Quy luật:** $u_n = u_{n-1} \times 2$. Mỗi phần tử thực chất là lũy thừa của 2: $u_n = 2^{n-1}$.
* **Cách sinh dãy bằng vòng lặp:**
  ```python
  n = int(input())
  val = 1
  for i in range(n):
      print(val, end=" ")
      val *= 2
  ```

### 2.3. Dãy số Fibonacci và Kỹ thuật Cuốn chiếu
Dãy Fibonacci rất nổi tiếng, các em ghi nhớ dãy sau:
$$1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, \dots$$
* **Quy luật bất biến:** Kể từ số hạng thứ 3, mỗi số hạng luôn bằng **tổng của hai số hạng liền kề trước nó**:
  $$F_1 = 1, \quad F_2 = 1, \quad F_n = F_{n-1} + F_{n-2} \quad (n \ge 3)$$

#### Kỹ thuật biến cuốn chiếu siêu gọn trong Python:
Ta không cần mảng lưu hết các số, chỉ cần giữ hai số gần nhất:
```python
n = int(input())
if n <= 2:
    print(1)
else:
    a = 1  # F1
    b = 1  # F2
    for _ in range(3, n + 1):
        a, b = b, a + b  # Cuốn chiếu: b mới = a cũ + b cũ, a mới nhận b cũ
    print(b)
```

### 2.4. Dãy số Tribonacci (Ba biến cuốn chiếu)
* **Quy luật:** Mỗi số hạng sau bằng tổng của 3 số hạng đứng ngay trước nó:
  $$T_1 = 1, \quad T_2 = 1, \quad T_3 = 2, \quad T_n = T_{n-1} + T_{n-2} + T_{n-3} \quad (n \ge 4)$$
* **Dãy số:** $1, 1, 2, 4, 7, 13, 24, 44, 81, \dots$
* **Cài đặt cuốn chiếu 3 biến:**
  ```python
  n = int(input())
  if n <= 2:
      print(1)
  elif n == 3:
      print(2)
  else:
      a, b, c = 1, 1, 2
      for _ in range(4, n + 1):
          a, b, c = b, c, a + b + c
      print(c)
  ```

### 2.5. Dãy số đan dấu
* **Dãy số:** $S = 1 - 2 + 3 - 4 + 5 - 6 + \dots \pm N$
* **Nhận xét toán học:**
  - Nếu $N$ chẵn: Các cặp $(1 - 2) + (3 - 4) + \dots + ((N-1) - N)$ đều có giá trị là $-1$. Có đúng $\frac{N}{2}$ cặp $\implies S = -\frac{N}{2}$.
  - Nếu $N$ lẻ: $S = (1 - 2 + \dots - (N-1)) + N = -\frac{N-1}{2} + N = \frac{N+1}{2}$.
* **Cài đặt tối ưu $\mathcal{O}(1)$:**
  ```python
  n = int(input())
  if n % 2 == 0:
      print(-(n // 2))
  else:
      print((n + 1) // 2)
  ```

---

## 3. Bản chất của Vòng lặp lồng nhau & Vẽ Tam giác số

Muốn in bảng số hay tam giác số 2 chiều, các em dùng **hai vòng lặp lồng nhau**: vòng ngoài đếm **hàng** từ 1 đến $N$, vòng trong in **các số trên mỗi hàng**, rồi gọi `print()` ở cuối vòng ngoài để xuống hàng mới.

### 3.1. Tam giác số tăng dần trên mỗi hàng
In tam giác có chiều cao $N = 4$:
```text
1
1 2
1 2 3
1 2 3 4
```
**Quy luật:** Ở hàng thứ $i$, in các số từ $1$ đến $i$:
```python
n = int(input())
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()  # Xuống dòng sau khi in hết hàng i
```

### 3.2. Tam giác số lặp lại chỉ số hàng
In tam giác có chiều cao $N = 4$:
```text
1
2 2
3 3 3
4 4 4 4
```
**Quy luật:** Ở hàng thứ $i$, in đúng $i$ lần giá trị $i$:
```python
n = int(input())
for i in range(1, n + 1):
    for j in range(i):
        print(i, end=" ")
    print()
```

### 3.3. Tam giác Floyd (Điền số liên tục tăng dần)
Tam giác Floyd là một tam giác vuông được điền liên tiếp các số tự nhiên bắt đầu từ 1:
```text
1
2 3
4 5 6
7 8 9 10
```
**Quy luật:** Duy trì một biến đếm toàn cục `dem = 1`. Mỗi khi in một số, ta tăng `dem += 1`:
```python
n = int(input())
dem = 1
for i in range(1, n + 1):
    for j in range(i):
        print(dem, end=" ")
        dem += 1
    print()
```

### 3.4. Ma trận bàn cờ số đan xen 0 và 1
In bảng số kích thước $N \times N$ gồm các số 0 và 1 xen kẽ:
```text
0 1 0 1
1 0 1 0
0 1 0 1
1 0 1 0
```
**Quy luật toán học:** Giá trị tại ô hàng $i$, cột $j$ phụ thuộc vào tính chẵn lẻ của tổng chỉ số:
$$(i + j) \% 2$$
```python
n = int(input())
for i in range(n):
    for j in range(n):
        print((i + j) % 2, end=" ")
    print()
```

---

## 4. Bảng mô phỏng biến thiên ô nhớ

### 4.1. Mô phỏng thuật toán cuốn chiếu Fibonacci ($F_5$)
```python
a, b = 1, 1
for i in range(3, 6):
    a, b = b, a + b
```

| Vòng Lặp $i$ | Giá Trị Cũ Của `a` | Giá Trị Cũ Của `b` | Thao Tác Tính Toán `a, b = b, a + b` | Giá Trị Mới Của `a` | Giá Trị Mới Của `b` |
|:---:|:---:|:---:|---|:---:|:---:|
| **Khởi tạo** | $1$ | $1$ | Khởi tạo $F_1 = 1, F_2 = 1$ | 1 | 1 |
| **$i = 3$** | $1$ | $1$ | $a = 1, \ b = 1 + 1 = 2$ | **1** | **2** ($F_3$) |
| **$i = 4$** | $1$ | $2$ | $a = 2, \ b = 1 + 2 = 3$ | **2** | **3** ($F_4$) |
| **$i = 5$** | $2$ | $3$ | $a = 3, \ b = 2 + 3 = 5$ | **3** | **5** ($F_5$) |

$$\implies \text{Kết quả: Số hạng thứ 5 của dãy Fibonacci là } F_5 = \mathbf{5}$$

### 4.2. Mô phỏng in Tam giác Floyd ($N = 3$)

| Hàng $i$ | Cột $j$ | Giá trị biến `dem` trước khi in | In ra màn hình | Thao tác | `dem` sau khi in |
|:---:|:---:|:---:|:---:|---|:---:|
| **$i = 1$** | $0$ | $1$ | `1 ` | Xuống dòng sau hàng | $2$ |
| **$i = 2$** | $0$ | $2$ | `2 ` | Tiếp tục cùng hàng | $3$ |
| | $1$ | $3$ | `3 ` | Xuống dòng sau hàng | $4$ |
| **$i = 3$** | $0$ | $4$ | `4 ` | Tiếp tục cùng hàng | $5$ |
| | $1$ | $5$ | `5 ` | Tiếp tục cùng hàng | $6$ |
| | $2$ | $6$ | `6 ` | Xuống dòng sau hàng | $7$ |

---

## 5. Lỗi hay gặp và cách tránh

> **BẪY LỖI 1: KHÔNG DÙNG PHÉP GÁN ĐỒNG THỜI KHI CUỐN CHIẾU**
> * Nếu viết:
>   ```python
>   a = b
>   b = a + b
>   ```
>   Khi gán `a = b`, biến `a` mất giá trị cũ nên `b = a + b` hóa ra tính `b = b + b` $\implies$ Sai cả dãy số!
> * **Bắt buộc viết:** `a, b = b, a + b` (hoặc mượn biến tạm `tam = a; a = b; b = tam + b`).

> **BẪY LỖI 2: QUÊN LỆNH XUỐNG DÒNG `print()` TRONG VÒNG LẶP HÀNG**
> * Quên `print()` ở cuối vòng ngoài thì mọi hàng dồn thành một hàng ngang duy nhất.

> **BẪY LỖI 3: DÙNG VÒNG LẶP CHO BÀI TOÁN CÓ CÔNG THỨC $\mathcal{O}(1)$**
> * Với $N = 10^{12}$, vòng lặp `for i in range(1, n + 1): s += i` chạy quá thời gian cho phép.
> * **Điều bắt buộc phải nhớ:** Với cấp số cộng và dãy đan dấu, luôn ưu tiên công thức toán học.

---

## 6. Mẫu code thường gặp

### Mẫu 1: In tam giác Floyd kích thước $N$
```python
n = int(input())
val = 1
for i in range(1, n + 1):
    for j in range(i):
        print(val, end=" ")
        val += 1
    print()
```

### Mẫu 2: Tính số Fibonacci thứ $N$ bằng cuốn chiếu
```python
n = int(input())
if n <= 2:
    print(1)
else:
    a, b = 1, 1
    for _ in range(3, n + 1):
        a, b = b, a + b
    print(b)
```

### Mẫu 3: In hình kim tự tháp dấu sao căn giữa
```python
n = int(input())
for i in range(1, n + 1):
    # In khoảng trắng lùi vào lề
    print(" " * (n - i), end="")
    # In các ký tự sao
    print("*" * (2 * i - 1))
```

---
