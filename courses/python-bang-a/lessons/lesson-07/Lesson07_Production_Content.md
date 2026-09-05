# Bài 07: Quy luật dãy số và tam giác số

## 1. Khái niệm & Bản chất của bài toán Dãy số trong lập trình thi đấu

Trong các kỳ thi lập trình, dạng bài **Dãy số & Tam giác số** chiếm tỉ trọng rất lớn. Mục tiêu cốt lõi của dạng toán này là rèn luyện cho học sinh:
* **Tư duy quy nạp toán học:** Nhìn vào các phần tử mẫu ban đầu để tìm ra quy luật biến thiên $u_n = f(u_{n-1})$ hoặc quy luật vị trí $u_n = f(n)$.
* **Kỹ thuật biến cuốn chiếu:** Tính toán trạng thái mới từ các trạng thái trước mà không cần cấp phát mảng bộ nhớ khổng lồ.
* **Cấu trúc vòng lặp lồng nhau:** Khám phá không gian 2 chiều qua việc điều khiển hàng và cột.
* **Tối ưu hóa độ phức tạp:** Nhận diện các bài toán có thể giải bằng công thức toán học $\mathcal{O}(1)$ thay vì chạy vòng lặp ngây thơ $\mathcal{O}(N)$ dẫn đến quá thời gian (TLE).

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
Dãy số Fibonacci là một trong những dãy số nổi tiếng nhất thế giới:
$$1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, \dots$$
* **Quy luật bất biến:** Kể từ số hạng thứ 3, mỗi số hạng luôn bằng **tổng của hai số hạng liền kề trước nó**:
  $$F_1 = 1, \quad F_2 = 1, \quad F_n = F_{n-1} + F_{n-2} \quad (n \ge 3)$$

#### Kỹ thuật biến cuốn chiếu siêu gọn trong Python:
Thay vì phải dùng mảng để lưu tất cả các số, ta chỉ cần duy trì hai biến đại diện cho hai số gần nhất:
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

Khi bài toán yêu cầu in ra một bảng số hoặc tam giác số 2 chiều, ta sử dụng **hai vòng lặp lồng nhau**:
* **Vòng lặp ngoài (`for i in range(...)`):** Điều khiển **Số hàng** (từ hàng 1 đến hàng $N$).
* **Vòng lặp trong (`for j in range(...)`):** Điều khiển **Số cột / Các số được in trên mỗi hàng**.
* **Lệnh xuống dòng `print()`:** Đặt ở cuối thân vòng lặp ngoài để chuyển sang hàng kế tiếp.

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

## 5. Tử huyệt và Bẫy lỗi lập trình kinh điển

> ❌ **BẪY LỖI 1: KHÔNG DÙNG PHÉP GÁN ĐỒNG THỜI KHI CUỐN CHIẾU**
> * Nếu viết:
>   ```python
>   a = b
>   b = a + b
>   ```
>   Thì khi gán `a = b`, biến `a` đã bị ghi đè mất giá trị cũ! Khi tính `b = a + b` thực chất máy tính đang tính `b = b + b` $\implies$ Sai lệch toàn bộ dãy số!
> * **Bắt buộc viết:** `a, b = b, a + b` (hoặc mượn biến tạm `tam = a; a = b; b = tam + b`).

> ❌ **BẪY LỖI 2: QUÊN LỆNH XUỐNG DÒNG `print()` TRONG VÒNG LẶP HÀNG**
> * Nếu quên dòng `print()` ở cuối vòng lặp ngoài, tất cả các số của các hàng trong tam giác sẽ dồn hết thành một hàng ngang dài ngoặc duy nhất.

> ❌ **BẪY LỖI 3: DÙNG VÒNG LẶP CHO BÀI TOÁN CÓ THỂ TÍNH BẰNG CÔNG THỨC $\mathcal{O}(1)$**
> * Với $N = 10^{12}$, nếu viết vòng lặp `for i in range(1, n + 1): s += i` chương trình chắc chắn bị lỗi `Time Limit Exceeded` (Quá thời gian 1.0 giây).
> * **Quy tắc:** Với cấp số cộng và dãy đan dấu, luôn ưu tiên dùng công thức toán học đóng.

---

## 6. Mẫu code chuẩn thi đấu

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

## 7. Concept Quiz: 15 câu trắc nghiệm kiểm tra sâu khái niệm

#### Câu 1 (Đặc trưng dãy Fibonacci):
Quy luật của dãy số Fibonacci $1, 1, 2, 3, 5, 8, 13, \dots$ là:
- **A.** Số sau bằng số trước nhân đôi
- **B.** **[Đáp án đúng]** Số sau bằng tổng của hai số đứng ngay trước nó
- **C.** Số sau bằng số trước cộng 3
- **D.** Dãy các số nguyên tố
> *Giải thích:* Theo định nghĩa: $F_n = F_{n-1} + F_{n-2}$ với mọi $n \ge 3$.

#### Câu 2 (Phép gán hoán đổi biến trong Python):
Để hoán đổi giá trị của hai biến `a` và `b` trong Python mà không cần dùng biến phụ, ta viết:
- **A.** `a = b; b = a`
- **B.** **[Đáp án đúng]** `a, b = b, a`
- **C.** `swap(a, b)`
- **D.** `a == b`
> *Giải thích:* Cơ chế tuple packing/unpacking của Python cho phép tráo đổi đồng thời hai biến cực kỳ an toàn.

#### Câu 3 (Bẫy cuốn chiếu sai thứ tự):
Xét đoạn mã:
```python
a = 1
b = 2
a = b
b = a + b
```
Sau khi chạy xong, giá trị của `b` là bao nhiêu?
- **A.** 3
- **B.** **[Đáp án đúng]** 4
- **C.** 2
- **D.** 1
> *Giải thích:* Lệnh `a = b` làm $a$ thành 2. Sau đó `b = a + b` thành $2 + 2 = 4$. Giá trị cũ $a = 1$ đã bị mất.

#### Câu 4 (Số hạng thứ N của Cấp số cộng):
Cấp số cộng có số hạng đầu $u_1 = 3$, công sai $d = 4$. Số hạng thứ $N = 10$ là:
- **A.** 40
- **B.** **[Đáp án đúng]** 39
- **C.** 43
- **D.** 36
> *Giải thích:* $u_{10} = u_1 + 9 \times d = 3 + 9 \times 4 = 39$.

#### Câu 5 (Tổng dãy số tự nhiên liên tiếp):
Tổng $S = 1 + 2 + 3 + \dots + 100$ có giá trị là:
- **A.** 5000
- **B.** **[Đáp án đúng]** 5050
- **C.** 5100
- **D.** 10100
> *Giải thích:* $S = \frac{100 \times 101}{2} = 5050$.

#### Câu 6 (Vòng lặp trong tam giác số):
Trong thuật toán in tam giác vuông số gồm $N$ hàng, vòng lặp ngoài thường dùng để:
- **A.** In từng số trên cùng một hàng
- **B.** **[Đáp án đúng]** Quản lý chỉ số hàng từ 1 đến $N$
- **C.** Đổi dấu các số
- **D.** Tính tổng các số
> *Giải thích:* Vòng lặp ngoài duyệt qua các hàng, vòng lặp trong duyệt qua các cột của từng hàng.

#### Câu 7 (Vai trò của print() không đối số):
Lệnh `print()` không có tham số bên trong đặt ở cuối thân vòng lặp ngoài nhằm mục đích gì?
- **A.** Xóa màn hình
- **B.** In ra số 0
- **C.** **[Đáp án đúng]** Xuống dòng mới để bắt đầu in hàng tiếp theo
- **D.** Dừng chương trình
> *Giải thích:* Mặc định `print()` in ký tự xuống dòng `\n`.

#### Câu 8 (Đặc điểm tam giác Floyd):
Hàng thứ 4 của tam giác Floyd bắt đầu bằng số nào?
- **A.** 5
- **B.** 6
- **C.** **[Đáp án đúng]** 7
- **D.** 8
> *Giải thích:* Hàng 1: [1]; Hàng 2: [2, 3]; Hàng 3: [4, 5, 6]; Hàng 4: [7, 8, 9, 10].

#### Câu 9 (Dãy số đan dấu):
Giá trị của biểu thức $S = 1 - 2 + 3 - 4 + 5 - 6 + \dots - 100$ là:
- **A.** 0
- **B.** **[Đáp án đúng]** -50
- **C.** 50
- **D.** -100
> *Giải thích:* Có 50 cặp, mỗi cặp có giá trị $-1$. $50 \times (-1) = -50$.

#### Câu 10 (Công thức ma trận bàn cờ):
Để tạo ô bàn cờ đan xen giá trị 0 và 1 tại tọa độ hàng `i`, cột `j`, công thức chuẩn là:
- **A.** `(i * j) % 2`
- **B.** **[Đáp án đúng]** `(i + j) % 2`
- **C.** `(i - j) % 2`
- **D.** `i % 2 + j % 2`
> *Giải thích:* Khi di chuyển sang ô bên cạnh (tăng $i$ hoặc $j$ thêm 1), tổng $(i + j)$ đổi tính chẵn lẻ, tạo nên hoa văn so le 0 và 1.

#### Câu 11 (Dãy số Tribonacci):
Ba số đầu của Tribonacci là $1, 1, 2$. Số hạng thứ 5 của dãy là:
- **A.** 4
- **B.** 6
- **C.** **[Đáp án đúng]** 7
- **D.** 8
> *Giải thích:* $T_4 = 1 + 1 + 2 = 4$; $T_5 = 1 + 2 + 4 = 7$.

#### Câu 12 (Số phần tử trên hàng i của tam giác vuông):
Trong một tam giác vuông có chiều cao $N$, hàng thứ $i$ ($1 \le i \le N$) có bao nhiêu phần tử?
- **A.** $N$ phần tử
- **B.** **[Đáp án đúng]** $i$ phần tử
- **C.** $2i$ phần tử
- **D.** $i - 1$ phần tử
> *Giải thích:* Hàng 1 có 1 phần tử, hàng 2 có 2 phần tử, ..., hàng $i$ có đúng $i$ phần tử.

#### Câu 13 (Độ phức tạp in tam giác số):
Thuật toán in tam giác số chiều cao $N$ dùng hai vòng lặp lồng nhau có độ phức tạp thời gian là:
- **A.** $\mathcal{O}(N)$
- **B.** **[Đáp án đúng]** $\mathcal{O}(N^2)$
- **C.** $\mathcal{O}(1)$
- **D.** $\mathcal{O}(N^3)$
> *Giải thích:* Tổng số phần tử cần in là $1 + 2 + \dots + N = \frac{N(N+1)}{2} \approx \mathcal{O}(N^2)$.

#### Câu 14 (Số hạng tam giác - Triangular Numbers):
Số lượng chấm tròn xếp thành hình tam giác đều cạnh $N$ được tính theo công thức nào?
- **A.** $N^2$
- **B.** **[Đáp án đúng]** $\frac{N(N+1)}{2}$
- **C.** $2^N$
- **D.** $N(N-1)$
> *Giải thích:* $T_n = 1 + 2 + \dots + N = \frac{N(N+1)}{2}$.

#### Câu 15 (Số Fibonacci thứ 7):
Số hạng thứ 7 của dãy Fibonacci $1, 1, 2, 3, 5, 8, \dots$ là:
- **A.** 11
- **B.** **[Đáp án đúng]** 13
- **C.** 15
- **D.** 21
> *Giải thích:* Dãy số: $F_1=1, F_2=1, F_3=2, F_4=3, F_5=5, F_6=8, F_7=13$.
