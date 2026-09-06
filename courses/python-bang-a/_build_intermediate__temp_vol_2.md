# LỜI NÓI ĐẦU

Chào mừng các em học sinh và quý thầy cô đến với bộ giáo trình **Khóa học Python cơ bản — QUYỂN 2: SỐ HỌC VÀ DỮ LIỆU**.

Quyển sách này viết tiếp hành trình từ Quyển 1 (Nền tảng lập trình). Các em đã biết tính toán, ra quyết định và lặp lại công việc — giờ là lúc khám phá những ứng dụng thú vị hơn: bóc tách chữ số, quản lý danh sách và xử lý văn bản.

Phần nội dung này gồm **3 Chương trọng tâm (Chương 03 đến Chương 05)** với **8 Bài học** và **130 bài tập thực hành**. Học xong quyển này, các em sẽ giải được các bài toán số học hay, sắp xếp và thống kê điểm số, đếm từ và biến đổi câu văn.

Mỗi bài học được thiết kế theo cấu trúc sư phạm chặt chẽ:

- **Khái niệm và bản chất:** Giải thích trực quan, dễ hiểu kèm ví dụ minh họa sinh động.
- **Mô hình bài toán quen thuộc:** Các dạng bài gần gũi với đời sống hằng ngày của các em.
- **Mẫu code thường gặp:** Đoạn code Python ngắn gọn, trong sáng, đúng chuẩn để các em học theo.
- **Hệ thống bài tập thực hành:** Phân tầng từ dễ đến khó (P0 đến P3) để các em luyện tập từng bước.
- **Lời giải tham khảo chi tiết:** Phụ lục B cung cấp mã nguồn Python hoàn chỉnh cho toàn bộ bài tập trong sách.

Chúc các em học tập vui vẻ và ngày càng yêu thích môn Tin học!


# CHƯƠNG 03: BÀI TOÁN SỐ HỌC & TÁCH CHỮ SỐ


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


## Bài tập thực hành


### Bài 01 [pya_l09_p01_trao_doi_hai_chiec_coc]: Tráo đổi hai chiếc cốc

Bối cảnh: Trong bài toán quản lý bộ nhớ, hai biến lưu trữ giá trị $A$ và $B$ cần được hoán đổi nội dung cho nhau. Bài toán yêu cầu tráo đổi dữ liệu của hai biến và xuất ra màn hình theo đúng thứ tự mới.

Nhiệm vụ: Nhập vào 2 số nguyên $A$ và $B$. Hãy hoán đổi giá trị của chúng và in ra theo thứ tự $A$ trước, $B$ sau.

**Đầu vào (Input):**

Hai số nguyên $A$ và $B$ trên một dòng, cách nhau bởi khoảng trắng.

**Đầu ra (Output):**

Giá trị mới của $A$ và $B$ sau khi hoán đổi.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 5 12 | 12 5 |

**Giải thích:**

Ban đầu $A=5, B=12$. Sau khi đổi $A=12, B=5$.



### Bài 02 [pya_l09_p03_so_hang_day_cap_so_cong]: Số hạng dãy cấp số cộng

Bối cảnh: Cấp số cộng là dãy số mà hiệu giữa hai số liên tiếp luôn bằng nhau. Cho số hạng đầu $u_1$ và công sai $d$, tìm số hạng thứ $N$.

Nhiệm vụ: Cho một dãy số cách đều có số đầu tiên là $u_1$ và khoảng cách giữa 2 số liền kề là $d$. Cho số nguyên dương $N$. Hãy tìm số hạng thứ $N$ của dãy số.

**Đầu vào (Input):**

Ba số nguyên $u_1, d, N$ ($1 \le u_1, d, N \le 10^6$).

**Đầu ra (Output):**

Một số nguyên là số hạng thứ $N$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 3 4 5 | 19 |

**Giải thích:**

Dãy số là: 3, 7, 11, 15, 19. Số thứ 5 là 19.
* **Công thức toán học:** $u_N = u_1 + (N - 1) \times d$.



### Bài 03 [pya_l09_p04_so_fibonacci_thu_n]: Số Fibonacci thứ N

Bối cảnh: Dãy Fibonacci: $1, 1, 2, 3, 5, 8, 13, \dots$ — mỗi số bằng tổng hai số liền trước. Đây là dãy số kỳ diệu xuất hiện khắp nơi trong tự nhiên, từ cánh hoa hướng dương đến vỏ ốc biển.

Nhiệm vụ: Dãy Fibonacci được định nghĩa: $F_1 = 1, F_2 = 1, F_n = F_{n-1} + F_{n-2}$ với $n \ge 3$. Nhập vào số tự nhiên $N$. Hãy tìm và in ra số Fibonacci thứ $N$.

**Đầu vào (Input):**

Một số tự nhiên $N$ ($1 \le N \le 40$).

**Đầu ra (Output):**

Giá trị $F_N$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 6 | 8 |

**Giải thích:**

Dãy là 1, 1, 2, 3, 5, 8. Số thứ 6 là 8.



### Bài 04 [pya_l09_p06_tong_tich_hai_so_lien_nhau]: Tổng tích hai số liền nhau

Bối cảnh: Tính tổng hoặc tích của các cặp số liên tiếp trong một dãy số. Đây là bài toán luyện kỹ thuật cuốn chiếu (rolling variables).

Nhiệm vụ: Cho số nguyên dương $N$. Hãy tính tổng:
 $$S = 1 \times 2 + 2 \times 3 + 3 \times 4 + \dots + N \times (N + 1)$$

**Đầu vào (Input):**

Một số nguyên dương $N$ ($1 \le N \le 10^5$).

**Đầu ra (Output):**

Tổng $S$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 3 | 20 |

**Giải thích:**

$1 \times 2 + 2 \times 3 + 3 \times 4 = 2 + 6 + 12 = 20$.



### Bài 05 [pya_l09_p08_tam_giac_so_don_gian]: Tam giác số đơn giản

Bối cảnh: In ra tam giác số với chiều cao $N$: hàng thứ $i$ chứa các số từ 1 đến $i$. Đây là bài toán kinh điển rèn luyện vòng lặp lồng nhau.

Nhiệm vụ: In ra tháp tam giác số có $N$ dòng theo quy luật minh họa ở Sample 1 (dòng thứ $i$ in các số từ $1$ đến $i$).

**Đầu vào (Input):**

Một số tự nhiên $N$ ($1 \le N \le 20$).

**Đầu ra (Output):**

Tháp tam giác số có $N$ dòng đúng quy luật trên.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 4 | 1 <br> 1 2 <br> 1 2 3 <br> 1 2 3 4 |

**Giải thích:**

Với dữ liệu đầu vào là `4`, kết quả thu được tương ứng là `1
1 2
1 2 3
1 2 3 4`.



### Bài 06 [pya_l09_p12_ma_tran_so_ban_co_dan_xen]: Ma trận số bàn cờ đan xen

Bối cảnh: In bảng số $N \times M$ với các giá trị xen kẽ theo quy luật bàn cờ: ô đen ô trắng luân phiên.

Nhiệm vụ: In ra một bảng ma trận vuông kích thước $N \times N$ gồm các số $0$ và $1$ xếp so le như bàn cờ vua, với ô góc trên cùng bên trái luôn là số $1$.

**Đầu vào (Input):**

Một số tự nhiên $N$ ($1 \le N \le 50$).

**Đầu ra (Output):**

Ma trận vuông $N \times N$ đúng quy luật trên, mỗi dòng in $N$ số cách nhau một khoảng trắng.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 4 | 1 0 1 0 <br> 0 1 0 1 <br> 1 0 1 0 <br> 0 1 0 1 |

**Giải thích:**

Với dữ liệu đầu vào là `4`, kết quả thu được tương ứng là `1 0 1 0
0 1 0 1
1 0 1 0
0 1 0 1`.



### Bài 07 [pya_l09_p02_day_so_nhan_doi]: Dãy số nhân đôi

Bối cảnh: Thí sinh viết dãy số: bắt đầu từ 1, mỗi số tiếp theo gấp đôi số trước. Hãy in ra $N$ số đầu tiên của dãy.

Nhiệm vụ: Nhập số nguyên $N$ ($1 \le N \le 30$). Hãy in ra $N$ số đầu tiên của dãy số nhân đôi: $1, 2, 4, 8, 16, 32, \dots$ trên cùng một dòng.

**Đầu vào (Input):**

Một số nguyên $N$.

**Đầu ra (Output):**

Dãy $N$ số, cách nhau bởi dấu cách.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 5 | 1 2 4 8 16 |

**Giải thích:**

Với dữ liệu đầu vào là `5`, kết quả thu được tương ứng là `1 2 4 8 16`.



### Bài 08 [pya_l09_p05_day_so_dan_dau]: Dãy số đan dấu

Bối cảnh: Thí sinh tạo ra dãy số với quy luật đặc biệt: số đầu tiên cho trước, các số tiếp theo tuân theo một công thức biến đổi nhất định. Hãy in $N$ số đầu tiên.

Nhiệm vụ: Cho số nguyên dương $N$. Hãy tính tổng của dãy số đan dấu:
 $$S = 1 - 2 + 3 - 4 + 5 - 6 + \dots + (-1)^{N+1} N$$

**Đầu vào (Input):**

Một số nguyên $N$ ($1 \le N \le 10^6$).

**Đầu ra (Output):**

Giá trị của tổng $S$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 5 | 3 |

**Giải thích:**

$1 - 2 + 3 - 4 + 5 = 3$.

**Ví dụ mẫu (Sample 2):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 6 | -3 |

**Giải thích:**

$1 - 2 + 3 - 4 + 5 - 6 = -3$.



### Bài 09 [pya_l09_p09_tam_giac_sao_can]: Tam giác sao cân

Bối cảnh: Vẽ tam giác cân bằng dấu sao `*` với chiều cao $N$. Mỗi hàng cần tính số khoảng trắng và số sao phù hợp để hình tam giác cân đối.

Nhiệm vụ: In ra một tháp sao tam giác cân đối xứng có độ cao $N$.
* **Quy luật:** Dòng thứ $i$ (từ 1 đến $N$) có $(N - i)$ dấu cách phía trước, tiếp theo là $(2i - 1)$ dấu sao `*`.

**Đầu vào (Input):**

Độ cao $N$ của tam giác ($1 \le N \le 20$).

**Đầu ra (Output):**

Tháp sao tam giác cân có $N$ dòng đúng quy luật trên.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 3 | * <br>  *** <br> ***** |

**Giải thích:**

Với dữ liệu đầu vào là `3`, kết quả thu được tương ứng là `*
 ***
*****`.



### Bài 10 [pya_l09_p10_day_so_tam_giac_triangular_numbers]: Dãy số tam giác (triangular numbers)

Bối cảnh: Trong giờ kể chuyện lịch sử, cô giáo kể rằng người Hy Lạp cổ đại ngày xưa rất thích xếp các viên sỏi nhỏ thành hình tam giác đều để chơi:
 * Tầng 1: 1 viên
 * Tầng 2: 1 + 2 = 3 viên
 * Tầng 3: 1 + 2 + 3 = 6 viên
 * Tầng 4: 1 + 2 + 3 + 4 = 10 viên
Cả lớp ai cũng muốn tự xếp sỏi giống như vậy. Hãy giúp các bạn kiểm tra xem một số sỏi có xếp được thành hình tam giác không.

Nhiệm vụ: Cho số tự nhiên $K$. Hãy kiểm tra xem $K$ có phải là một "Số tam giác" hay không (nghĩa là có tồn tại số nguyên dương $N$ sao cho $\frac{N(N+1)}{2} = K$)? Nếu có, in ra `YES` và số $N$, ngược lại in `NO`.

**Đầu vào (Input):**

Một số nguyên $K$ ($1 \le K \le 10^9$).

**Đầu ra (Output):**

`YES <N>` hoặc `NO`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 10 | YES 4 |

**Giải thích:**

Với dữ liệu đầu vào là `10`, kết quả thu được tương ứng là `YES 4`.

**Ví dụ mẫu (Sample 2):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 8 | NO |



### Bài 11 [pya_l09_p14_tim_vi_tri_trong_day_tu_nhien_dai]: Tìm vị trí trong dãy tự nhiên dài

Bối cảnh: Giờ học vui, An lấy phấn viết liên tiếp các số tự nhiên bắt đầu từ 1 thành một dải số dài vô tận khắp sân trường:
 `123456789101112131415161718192021...`
Các bạn xúm lại đọc to từng chữ số, vừa đọc vừa cười khanh khách. Đến chữ số ở xa thì không ai đếm nổi bằng mắt nữa. Hãy tìm nhanh chữ số đó.

Nhiệm vụ: Cho số nguyên dương $K$ ($1 \le K \le 10^5$). Hãy xác định chữ số thứ $K$ trong dải số trên là chữ số nào?

**Đầu vào (Input):**

Một số nguyên $K$.

**Đầu ra (Output):**

Chữ số tại vị trí $K$ (đếm từ 1).

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 7 | 7 |

**Giải thích:**

Ký tự thứ 7 là số 7.

**Ví dụ mẫu (Sample 2):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 11 | 0 |

**Giải thích:**

Ký tự thứ 10 là '1', ký tự thứ 11 là '0' (của số 10).



### Bài 12 [pya_l09_p13_tam_giac_floyd]: Tam giác Floyd

Bối cảnh: Trong câu lạc bộ toán vui, bạn Xoài đố cả nhóm xếp một tháp số thật đẹp. Luật chơi là tam giác Floyd: một tam giác số vuông được điền liên tiếp các số tự nhiên tăng dần bắt đầu từ 1. Các bạn xếp mãi mà tháp cứ lệch, ai cũng bật cười vui vẻ. Hãy giúp nhóm bạn Xoài xếp tháp số này cho ngay ngắn.

Nhiệm vụ: In ra tam giác Floyd có $N$ dòng (điền liên tiếp các số tự nhiên từ 1 như minh họa ở Sample 1).

**Đầu vào (Input):**

Một số nguyên dương $N$ ($1 \le N \le 20$).

**Đầu ra (Output):**

Tam giác Floyd có $N$ dòng đúng quy luật trên.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 4 | 1 <br> 2 3 <br> 4 5 6 <br> 7 8 9 10 |

**Giải thích:**

Với dữ liệu đầu vào là `4`, kết quả thu được tương ứng là `1
2 3
4 5 6
7 8 9 10`.



### Bài 13 [pya_l09_p07_day_so_boi_ba_boi_nam]: Dãy số bội ba bội năm

Bối cảnh: Liệt kê các số từ 1 đến $N$ chia hết cho 3 hoặc chia hết cho 5. Đây là bài toán kinh điển rèn luyện điều kiện logic phức hợp.

Nhiệm vụ: Xét dãy các số nguyên dương chia hết cho 3 hoặc chia hết cho 5 theo thứ tự tăng dần: $3, 5, 6, 9, 10, 12, 15, \dots$. Cho số tự nhiên $N$. Hãy in ra $N$ số đầu tiên của dãy này.

**Đầu vào (Input):**

Một số nguyên dương $N$ ($1 \le N \le 10^4$).

**Đầu ra (Output):**

$N$ số đầu tiên của dãy trên một dòng, cách nhau bởi dấu cách.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 6 | 3 5 6 9 10 12 |

**Giải thích:**

Với dữ liệu đầu vào là `6`, kết quả thu được tương ứng là `3 5 6 9 10 12`.



### Bài 14 [pya_l09_p11_day_so_tribonacci]: Dãy số Tribonacci

Bối cảnh: Dãy Tribonacci mở rộng từ Fibonacci: mỗi số bằng tổng ba số liền trước. Hãy tính số hạng thứ $N$ của dãy.

Nhiệm vụ: Dãy Tribonacci mở rộng từ Fibonacci với 3 số đầu tiên là $1, 1, 2$. Kể từ số thứ tư, mỗi số bằng tổng của 3 số liền kề trước nó:
 $$T_1 = 1, T_2 = 1, T_3 = 2, \quad T_n = T_{n-1} + T_{n-2} + T_{n-3} \quad (n \ge 4)$$
 Nhập vào số tự nhiên $N$ ($1 \le N \le 35$). Hãy in ra số Tribonacci thứ $N$.

**Đầu vào (Input):**

Một số nguyên $N$.

**Đầu ra (Output):**

Giá trị $T_N$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 5 | 7 |

**Giải thích:**

Dãy là: 1, 1, 2, 4, 7... Số thứ 5 là $1+2+4=7$.



# Bài 08: Kỹ thuật tách chữ số và xử lý số nguyên qua vòng lặp while

## 1. Khái niệm & Tầm quan trọng của Xử lý chữ số trong lập trình

Các bài toán về **chữ số của một số nguyên** gặp rất thường xuyên trong bài tập lập trình:
* Tính tổng, tích các chữ số.
* Đếm số lượng chữ số thỏa mãn tính chất (chẵn, lẻ, nguyên tố, chia hết).
* Tìm chữ số lớn nhất, chữ số nhỏ nhất, chữ số đầu tiên bên trái.
* Tạo số đảo ngược và kiểm tra số đối xứng.
* Kiểm tra số may mắn, số Armstrong, số tự mãn.

Nhớ cho cô: mỗi số nguyên hệ thập phân đều ghép từ các lũy thừa của 10. Muốn bóc từng chữ số mà không cần chuỗi ký tự, các em dùng cặp chia nguyên `//` và chia dư `%` cho 10 cùng vòng lặp `while`.

---

## 2. Cặp toán tử "Thần thánh": `// 10` và `% 10`

### 2.1. Phép toán `N % 10` (Bóc chữ số hàng đơn vị)
Chia một số nguyên cho 10, phần dư **chính là chữ số tận cùng bên phải**:
* $2026 \% 10 = \mathbf{6}$
* $789 \% 10 = \mathbf{9}$
* $5 \% 10 = \mathbf{5}$

### 2.2. Phép toán `N // 10` (Cắt bỏ chữ số hàng đơn vị)
Chia nguyên cho 10 là **bỏ chữ số tận cùng bên phải** để thu gọn số lại:
* $2026 // 10 = \mathbf{202}$
* $789 // 10 = \mathbf{78}$
* $5 // 10 = \mathbf{0}$

---

## 3. Khung thuật toán chuẩn bóc tách chữ số

Lặp lại hai thao tác trên trong `while N > 0:`, các em duyệt từng chữ số của $N$ từ **phải sang trái**:

```python
n = int(input())

# Lưu ý: Luôn xử lý trường hợp số 0 nếu bài toán yêu cầu
if n == 0:
    # Xử lý riêng trường hợp đặc biệt n = 0
    pass
else:
    while n > 0:
        chu_so = n % 10   # 1. Bóc chữ số tận cùng
        # 2. Xử lý nghiệp vụ với chu_so ở đây
        n //= 10          # 3. Cắt bỏ chữ số tận cùng để chuẩn bị cho vòng tiếp theo
```

### Minh họa thứ tự tách chữ số:
Với $N = 375$:
1. Vòng 1: `chu_so = 375 % 10 = 5`, thu gọn `n = 375 // 10 = 37`
2. Vòng 2: `chu_so = 37 % 10 = 7`, thu gọn `n = 37 // 10 = 3`
3. Vòng 3: `chu_so = 3 % 10 = 3`, thu gọn `n = 3 // 10 = 0`
4. Điều kiện `n > 0` thành `False` $\implies$ Vòng lặp kết thúc!

---

## 4. Các dạng bài toán kinh điển trên chữ số

### 4.1. Đếm số lượng chữ số của số nguyên $N$
* **Trường hợp $N = 0$:** Số 0 có đúng 1 chữ số $\implies$ In ra 1.
* **Trường hợp $N > 0$:**
  ```python
  n = int(input())
  if n == 0:
      print(1)
  else:
      dem = 0
      while n > 0:
          dem += 1
          n //= 10
      print(dem)
  ```

### 4.2. Tính tổng và tích các chữ số
* **Tính tổng:** Khởi tạo `tong = 0`, mỗi bước cộng dồn `tong += chu_so`.
* **Tính tích các chữ số khác 0:** Khởi tạo `tich = 1`. Nếu `chu_so != 0` thì nhân dồn `tich *= chu_so`.
  ```python
  n = int(input())
  tong = 0
  tich = 1
  while n > 0:
      d = n % 10
      tong += d
      if d != 0:
          tich *= d
      n //= 10
  print(tong, tich)
  ```

### 4.3. Tìm chữ số lớn nhất và nhỏ nhất
Khởi tạo `max_d = 0` và `min_d = 9`. Duyệt qua từng chữ số và cập nhật cực trị:
```python
n = int(input())
if n == 0:
    print(0, 0)
else:
    max_d = 0
    min_d = 9
    while n > 0:
        d = n % 10
        if d > max_d: max_d = d
        if d < min_d: min_d = d
        n //= 10
    print(max_d, min_d)
```

### 4.4. Tạo số đảo ngược
* **Ý nghĩa:** Cho số $N = 1234$, số đảo ngược thu được là $4321$.
* **Bản chất toán học:** Mỗi khi có một chữ số mới $d$, số đảo ngược hiện tại phải được dịch sang trái một hàng (nhân với 10), rồi cộng thêm $d$ vào hàng đơn vị:
  $$\mathbf{dao = dao \times 10 + d}$$
```python
n = int(input())
dao = 0
while n > 0:
    d = n % 10
    dao = dao * 10 + d
    n //= 10
print(dao)
```

### 4.5. Kiểm tra số đối xứng (Số Palindrome)
Một số nguyên là **số đối xứng** nếu đọc xuôi hay ngược đều giống nhau (ví dụ: $121, 1331, 2002, 7$).
* **Thuật toán:**
  1. Giữ lại giá trị ban đầu vào biến tạm: `goc = n`.
  2. Tạo số đảo ngược `dao` của $n$.
  3. So sánh `if dao == goc:` $\implies$ Số đối xứng!

```python
n = int(input())
goc = n
dao = 0

while n > 0:
    dao = dao * 10 + (n % 10)
    n //= 10

if dao == goc:
    print("YES")
else:
    print("NO")
```

---

## 5. Bảng mô phỏng biến thiên ô nhớ

### Thuật toán: Tạo số đảo ngược của $N = 375$
```python
n = 375
dao = 0
```

### Bảng theo dõi trạng thái bộ nhớ RAM qua từng vòng lặp:

| Vòng Lặp | `n` Ban Đầu | Tách `chu_so = n % 10` | Cập Nhật `dao = dao * 10 + chu_so` | Cắt Bỏ `n //= 10` | Trạng thái điều kiện `n > 0` |
|:---:|:---:|:---:|---|:---:|:---:|
| **Khởi tạo** | $375$ | Chưa có | `dao = 0` | $375$ | $375 > 0$ (Đúng) |
| **Vòng 1** | $375$ | **`5`** | `dao = 0 * 10 + 5 = 5` | **`37`** | $37 > 0$ (Đúng) |
| **Vòng 2** | $37$ | **`7`** | `dao = 5 * 10 + 7 = 57` | **`3`** | $3 > 0$ (Đúng) |
| **Vòng 3** | $3$ | **`3`** | `dao = 57 * 10 + 3 = 573` | **`0`** | $0 > 0$ (**Sai**) |
| **Dừng lặp** | $0$ | *(Thoát lặp vì n = 0)* | Giữ nguyên: **`573`** | Giữ nguyên: `0` | Kết thúc vòng lặp |

$$\implies \text{Kết quả: Số đảo ngược của } 375 \text{ là } \mathbf{573}$$

---

## 6. Lỗi hay gặp và cách tránh

> **BẪY LỖI 1: QUÊN LƯU LẠI GIÁ TRỊ GỐC CỦA BIẾN $N$**
> * Chạy xong `while n > 0:`, biến `n` đã về `0`, nên `if dao == n:` là so `dao` với `0` $\implies$ Sai hẳn!
> * **Điều bắt buộc phải nhớ:** Giữ giá trị ban đầu bằng `goc = n` trước khi vào vòng lặp.

> **BẪY LỖI 2: QUÊN XỬ LÝ TRƯỜNG HỢP BIÊN $N = 0$**
> * Với $N = 0$, `while n > 0:` không chạy bước nào nên bài "Đếm số chữ số" in ra `0` là sai (số 0 có đúng 1 chữ số).
> * **Khắc phục:** Thêm `if n == 0: print(1)`.

> **BẪY LỖI 3: DÙNG KIỂU CHUỖI KHI BÀI YÊU CẦU THUẬT TOÁN SỐ**
> * Dù viết `s = str(n)` cũng được, các em vẫn nên làm chủ cặp `//` và `%` vì đó là tư duy thuật toán cốt lõi, code chạy nhanh và dễ chuyển sang ngôn ngữ khác (C++, Java).

---

## 7. Mẫu code thường gặp

### Mẫu 1: Tìm chữ số đầu tiên bên trái (hàng cao nhất) của số $N$
```python
n = int(input())
while n >= 10:
    n //= 10
print(n)
```

### Mẫu 2: Đếm số lượng chữ số chẵn và lẻ
```python
n = int(input())
chan = 0
le = 0

if n == 0:
    chan = 1
else:
    while n > 0:
        d = n % 10
        if d % 2 == 0:
            chan += 1
        else:
            le += 1
        n //= 10

print(chan, le)
```

### Mẫu 3: Đếm các số đối xứng trong đoạn $[A, B]$
```python
a, b = map(int, input().split())
dem = 0

for x in range(a, b + 1):
    goc = x
    dao = 0
    t = x
    while t > 0:
        dao = dao * 10 + (t % 10)
        t //= 10
    if dao == goc:
        dem += 1

print(dem)
```

---


## Bài tập thực hành


### Bài 01 [pya_l10_p01_lay_chu_so_don_vi_chuc]: Lấy chữ số đơn vị & chục

Bối cảnh: Trong hệ thống xử lý số liệu đo lường, mỗi con số gồm hai chữ số đều mang thông tin độc lập ở hàng chục và hàng đơn vị. Để chuẩn hóa dữ liệu, hệ thống cần tách riêng hai giá trị này.

Nhiệm vụ: Nhập một số nguyên dương $N$ có đúng 2 chữ số. Hãy in ra chữ số hàng chục và chữ số hàng đơn vị của $N$ trên cùng một dòng, cách nhau một khoảng trắng.

**Đầu vào (Input):**

Một số nguyên $N$ ($10 \le N \le 99$).

**Đầu ra (Output):**

Chữ số hàng chục, tiếp theo là chữ số hàng đơn vị.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 47 | 4 7 |

**Giải thích:**

Với dữ liệu đầu vào là `47`, kết quả thu được tương ứng là `4 7`.



### Bài 02 [pya_l10_p02_tong_chu_so_cua_so_3_chu_so]: Tổng chữ số của số 3 chữ số

Bối cảnh: Trong bài kiểm tra, người dùng cần tính nhanh tổng một dãy số. Hãy viết chương trình hỗ trợ tính toán.

Nhiệm vụ: Nhập một số nguyên dương $N$ có đúng 3 chữ số. Hãy tính tổng của 3 chữ số đó.

**Đầu vào (Input):**

Một số tự nhiên $N$ ($100 \le N \le 999$).

**Đầu ra (Output):**

Tổng 3 chữ số.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 358 | 16 |

**Giải thích:**

$3 + 5 + 8 = 16$.



### Bài 03 [pya_l10_p03_tong_cac_chu_so_cua_n]: Tổng các chữ số của N

Bối cảnh: Trong bài kiểm tra, người dùng cần tính nhanh tổng một dãy số. Hãy viết chương trình hỗ trợ tính toán.

Nhiệm vụ: Cho một số tự nhiên $N$ bất kỳ. Hãy tính tổng tất cả các chữ số cấu tạo nên số $N$.

**Đầu vào (Input):**

Một số nguyên $N$ ($0 \le N \le 10^{18}$).

**Đầu ra (Output):**

Tổng các chữ số của $N$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 2024 | 8 |

**Giải thích:**

$2 + 0 + 2 + 4 = 8$.

**Ví dụ mẫu (Sample 2):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 0 | 0 |

**Giải thích:**

Chữ số 0 có tổng bằng 0.



### Bài 04 [pya_l10_p08_so_dao_nguoc]: Số đảo ngược

Bối cảnh: Thao tác đảo ngược thứ tự các chữ số là nền tảng quan trọng trong các bài toán kiểm tra tính đối xứng và biến đổi số học.

Nhiệm vụ: Cho số nguyên dương $N$. Hãy in ra số đảo ngược của $N$ (bỏ qua các chữ số 0 ở đầu nếu có sau khi đảo).

**Đầu vào (Input):**

Một số tự nhiên $N$ ($1 \le N \le 10^{12}$).

**Đầu ra (Output):**

Số đảo ngược.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 1234 | 4321 |

**Giải thích:**

Đảo ngược các chữ số.

**Ví dụ mẫu (Sample 2):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 2500 | 52 |

**Giải thích:**

Đảo ngược là 0052, giá trị số học là 52.



### Bài 05 [pya_l10_p05_tich_cac_chu_so_khac_khong]: Tích các chữ số khác không

Bối cảnh: Trong một số thuật toán tạo mã băm và mã kiểm tra dữ liệu, tích của các chữ số có nghĩa (khác số 0) thường được dùng để tạo khóa đại diện cho số nguyên ban đầu.

Nhiệm vụ: Cho số nguyên dương $N$. Hãy tính tích của tất cả các chữ số **khác 0** của $N$.

**Đầu vào (Input):**

Một số tự nhiên $N$ ($1 \le N \le 10^9$).

**Đầu ra (Output):**

Tích các chữ số khác 0.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 205 | 10 |

**Giải thích:**

Bỏ qua chữ số 0, tích là $2 \times 5 = 10$.



### Bài 06 [pya_l10_p04_dem_so_luong_chu_so]: Đếm số lượng chữ số

Bối cảnh: Trong lưu trữ dữ liệu số học, việc xác định độ dài số lượng chữ số của một số nguyên giúp hệ thống cấp phát bộ nhớ và căn chỉnh bảng biểu một cách chính xác.

Nhiệm vụ: Cho số nguyên không âm $N$. Hãy cho biết số $N$ có bao nhiêu chữ số.

**Đầu vào (Input):**

Một số nguyên $N$ ($0 \le N \le 10^{18}$).

**Đầu ra (Output):**

Số lượng chữ số.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 123456 | 6 |

**Giải thích:**

Có 6 chữ số.

**Ví dụ mẫu (Sample 2):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 0 | 1 |

**Giải thích:**

Số 0 có đúng 1 chữ số.
* **Lưu ý:** Chú ý xử lý trường hợp đặc biệt $N = 0$.



### Bài 07 [pya_l10_p09_kiem_tra_so_doi_xung_palindrome]: Kiểm tra số đối xứng (palindrome)

Bối cảnh: Na rất thích soi gương vì trong gương mọi thứ trông giống hệt ở ngoài. Một hôm, bạn Tí đố Na tìm những con số cũng "soi gương" được như vậy. Đó chính là số đối xứng (Palindrome): số đọc từ trái sang phải hay từ phải sang trái đều thu được số giống hệt nhau (ví dụ: $121$, $1331$, $5$, $88$). Na loay hoay mãi chưa kiểm tra hết, hãy bạn ấy.

Nhiệm vụ: Nhập vào số tự nhiên $N$. Kiểm tra xem $N$ có phải số đối xứng không. Nếu có in `YES`, ngược lại in `NO`.

**Đầu vào (Input):**

Một số nguyên $N$ ($1 \le N \le 10^{15}$).

**Đầu ra (Output):**

`YES` hoặc `NO`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 12321 | YES |

**Giải thích:**

Với dữ liệu đầu vào là `12321`, kết quả thu được tương ứng là `YES`.

**Ví dụ mẫu (Sample 2):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 1234 | NO |



### Bài 08 [pya_l10_p13_can_bac_so_hoc_digital_root]: Căn bậc số học (digital root)

Bối cảnh: Bạn Mít chơi trò "gộp hạt đậu": mỗi lần bạn ấy cộng dồn liên tục các chữ số của một số tự nhiên cho đến khi chỉ còn lại đúng **một chữ số duy nhất**, và bạn ấy gọi đó là căn bậc số học của số đó.
 Ví dụ: $9875 \to 9 + 8 + 7 + 5 = 29 \to 2 + 9 = 11 \to 1 + 1 = 2$. Căn bậc số học của 9875 là 2. Mít cộng mãi mà vẫn hay nhầm, hãy bạn ấy tính thật nhanh.

Nhiệm vụ: Nhập vào số tự nhiên $N$. Hãy tìm căn bậc số học của $N$.

**Đầu vào (Input):**

Một số tự nhiên $N$ ($1 \le N \le 10^{18}$).

**Đầu ra (Output):**

Một chữ số duy nhất (từ 1 đến 9).

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 9875 | 2 |

**Giải thích:**

Với dữ liệu đầu vào là `9875`, kết quả thu được tương ứng là `2`.



### Bài 09 [pya_l10_p07_chu_so_lon_nhat_nho_nhat]: Chữ số lớn nhất & nhỏ nhất

Bối cảnh: Thí sinh cần tìm giá trị lớn nhất hoặc nhỏ nhất trong một tập dữ liệu. Hãy viết chương trình tìm kiếm.

Nhiệm vụ: Cho số nguyên dương $N$. Hãy tìm chữ số lớn nhất và chữ số nhỏ nhất xuất hiện trong số $N$.

**Đầu vào (Input):**

Một số nguyên $N$ ($1 \le N \le 10^{12}$).

**Đầu ra (Output):**

Chữ số lớn nhất, theo sau là chữ số nhỏ nhất, cách nhau một khoảng trắng.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 9418 | 9 1 |

**Giải thích:**

Chữ số lớn nhất là 9, nhỏ nhất là 1.



### Bài 10 [pya_l10_p11_so_may_man_chua_so_7]: Số may mắn chứa số 7

Bối cảnh: Trong hệ thống lọc vé thưởng tự động, các số thẻ có chứa chữ số 7 được coi là thỏa mãn điều kiện nhận mã ưu tiên. Hệ thống cần kiểm tra nhanh tính chất này trên mỗi số thẻ.

Nhiệm vụ: An coi số 7 là con số mang lại may mắn. Một số tự nhiên $N$ được gọi là "May mắn" nếu trong các chữ số của nó có ít nhất một chữ số 7. Cho số $N$, hãy kiểm tra xem $N$ có may mắn không. In `YES` nếu có, `NO` nếu không.

**Đầu vào (Input):**

Số nguyên $N$ ($1 \le N \le 10^9$).

**Đầu ra (Output):**

`YES` hoặc `NO`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 372 | YES |

**Giải thích:**

Với dữ liệu đầu vào là `372`, kết quả thu được tương ứng là `YES`.

**Ví dụ mẫu (Sample 2):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 2024 | NO |



### Bài 11 [pya_l10_p06_dem_chu_so_chan_va_le]: Đếm chữ số chẵn và lẻ

Bối cảnh: Phân tích cấu trúc chẵn lẻ của các chữ số là bước kiểm định tính cân bằng số học trong các hệ thống mã hóa và kiểm thử dữ liệu đầu vào.

Nhiệm vụ: Cho số nguyên dương $N$. Hãy đếm xem trong số $N$ có bao nhiêu chữ số chẵn (0, 2, 4, 6, 8) và bao nhiêu chữ số lẻ (1, 3, 5, 7, 9).

**Đầu vào (Input):**

Một số tự nhiên $N$ ($1 \le N \le 10^{12}$).

**Đầu ra (Output):**

In hai số nguyên cách nhau một khoảng trắng: số lượng chữ số chẵn trước, số lượng chữ số lẻ sau.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 2035 | 2 2 |

**Giải thích:**

Chữ số chẵn: 2, 0 (2 số). Chữ số lẻ: 3, 5 (2 số).



### Bài 12 [pya_l10_p14_so_tang_giam_dep]: Số tăng giảm đẹp

Bối cảnh: Bạn Cún thích xếp những bậc thang bằng các chữ số. Có hôm bạn ấy xếp được cầu thang đi lên thật đẹp, có hôm lại xếp được cầu thang đi xuống thật gọn. Cô giáo gọi đó là:
 * **Số Tăng Dần:** Nếu mỗi chữ số đứng sau luôn lớn hơn chữ số đứng trước nó (ví dụ: $1379, 258$).
 * **Số Giảm Dần:** Nếu mỗi chữ số đứng sau luôn nhỏ hơn chữ số đứng trước nó (ví dụ: $9641, 852$). Cún nhờ em nhìn giúp xem mỗi con số là cầu thang lên, cầu thang xuống hay không phải cầu thang.

Nhiệm vụ: Cho số $N$. In ra `TANG` nếu $N$ là số tăng dần, in `GIAM` nếu $N$ là số giảm dần, và in `KHONG` nếu không thỏa mãn cả 2 tính chất trên.

**Đầu vào (Input):**

Một số nguyên $N$ ($10 \le N \le 10^{12}$).

**Đầu ra (Output):**

`TANG`, `GIAM` hoặc `KHONG`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 1379 | TANG |

**Giải thích:**

Với dữ liệu đầu vào là `1379`, kết quả thu được tương ứng là `TANG`.

**Ví dụ mẫu (Sample 2):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 9520 | GIAM |

**Ví dụ mẫu (Sample 3):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 1335 | `KHONG` (Có hai chữ số 3 bằng nhau) |



### Bài 13 [pya_l10_p10_so_toan_chan_hoac_toan_le]: Số toàn chẵn hoặc toàn lẻ

Bối cảnh: Lớp của Bi chia thành hai đội chơi xếp số rất vui. Đội Chẵn chỉ thích những số "Toàn chẵn", tức là số mà mọi chữ số của nó đều là số chẵn. Đội Lẻ lại mê những số "Toàn lẻ", tức là số mà mọi chữ số của nó đều là số lẻ. Trọng tài Tí nhờ em giúp phân xử mỗi con số, hãy bạn ấy.

Nhiệm vụ: Nhập số nguyên dương $N$. In ra `TOAN CHAN` nếu $N$ là số toàn chẵn, in `TOAN LE` nếu $N$ toàn lẻ, ngược lại in `BINH THUONG`.

**Đầu vào (Input):**

Một số tự nhiên $N$ ($1 \le N \le 10^{15}$).

**Đầu ra (Output):**

`TOAN CHAN`, `TOAN LE` hoặc `BINH THUONG`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 2468 | TOAN CHAN |

**Giải thích:**

Với dữ liệu đầu vào là `2468`, kết quả thu được tương ứng là `TOAN CHAN`.

**Ví dụ mẫu (Sample 2):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 1395 | TOAN LE |

**Ví dụ mẫu (Sample 3):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 2418 | BINH THUONG |



### Bài 14 [pya_l10_p12_dem_so_luong_so_doi_xung_trong_doan]: Đếm số lượng số đối xứng trong đoạn

Bối cảnh: Các số đối xứng (palindrome) sở hữu tính cân bằng cấu trúc đặc biệt và xuất hiện thường xuyên trong bài toán sinh mã định danh và nén số liệu.

Nhiệm vụ: Cho hai số nguyên dương $A$ và $B$ ($1 \le A \le B \le 10^5$). Hãy đếm xem có bao nhiêu số đối xứng nằm trong đoạn từ $A$ đến $B$ (tính cả $A$ và $B$).

**Đầu vào (Input):**

Hai số nguyên $A, B$ trên cùng một dòng.

**Đầu ra (Output):**

Số lượng số đối xứng trong đoạn $[A, B]$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 1 20 | 10 |

**Giải thích:**

Các số đối xứng là: 1, 2, 3, 4, 5, 6, 7, 8, 9, 11 (tổng cộng 10 số).



# Bài 09: Ước số, Bội số và Số nguyên tố

## 1. Khái niệm & Nền tảng Số học trong lập trình

Các khái niệm **Ước số**, **Bội số**, **Số nguyên tố** và **Số chính phương** là trục kiến thức toán - tin rất quan trọng.

Các em sẽ học: bản chất phép chia hết $A \vdots B \iff A \% B == 0$; cách tăng tốc từ cách duyệt ngây thơ sang thuật toán căn bậc hai $\mathcal{O}(\sqrt{N})$; mối quan hệ giữa Ước chung lớn nhất ($\gcd$) và Bội chung nhỏ nhất ($\text{lcm}$); cách viết hàm kiểm tra nguyên tố và phân tích thừa số nguyên tố.

---

## 2. Số nguyên tố và Thuật toán tối ưu $\mathcal{O}(\sqrt{N})$

### 2.1. Định nghĩa chuẩn số học
* **Số nguyên tố:** Là số tự nhiên **lớn hơn 1** và chỉ có **đúng hai ước số nguyên dương** là 1 và chính nó ($2, 3, 5, 7, 11, 13, 17, 19, \dots$).
* **Hợp số:** Là số tự nhiên lớn hơn 1 và có nhiều hơn hai ước số ($4, 6, 8, 9, 10, \dots$).
* **Điều bắt buộc phải nhớ:** Số $0$ và số $1$ **KHÔNG PHẢI** là số nguyên tố và cũng **KHÔNG PHẢI** là hợp số! Số $2$ là số nguyên tố nhỏ nhất và là số nguyên tố chẵn duy nhất.

### 2.2. Định lý Căn bậc hai
* **Cách duyệt ngây thơ $\mathcal{O}(N)$:** Duyệt mọi $i$ từ $2$ đến $N - 1$; thấy số nào chia hết $N$ thì $N$ không nguyên tố. Với $N = 10^9$ cần tới $10^9$ phép tính — quá chậm!
* **Định lý toán học:** Nếu một số tự nhiên $N$ là hợp số, nó luôn có thể phân tích thành tích của hai thừa số: $N = a \times b$. Khi đó, **chắc chắn phải có ít nhất một thừa số nhỏ hơn hoặc bằng $\sqrt{N}$** (bởi vì nếu cả $a > \sqrt{N}$ và $b > \sqrt{N}$ thì $a \times b > N$, mâu thuẫn!).
* $\implies$ Để kiểm tra tính nguyên tố của $N$, ta **chỉ cần duyệt $i$ từ $2$ đến $\lfloor\sqrt{N}\rfloor$** (tương đương điều kiện $i \times i \le N$). Nếu không tìm thấy ước nào trong đoạn này thì $N$ chắc chắn là số nguyên tố!

#### Cài đặt kiểm tra nguyên tố phổ biến:
```python
def la_so_nguyen_to(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True
```
* **Độ phức tạp:** Giảm từ $10^9$ bước xuống còn $\sqrt{10^9} \approx 31622$ bước $\implies$ Chạy trong $0.001$ giây!

---

## 3. Thuật toán đếm và liệt kê toàn bộ Ước số

### 3.1. Kỹ thuật ghép cặp ước số theo $\mathcal{O}(\sqrt{N})$
Các ước số nguyên dương của $N$ luôn xuất hiện theo từng cặp đối xứng:
$$i \quad \text{và} \quad \frac{N}{i} \quad (\text{với } i \times \frac{N}{i} = N)$$

Ví dụ với $N = 36$:
* $i = 1 \implies$ Cặp $(1, 36)$
* $i = 2 \implies$ Cặp $(2, 18)$
* $i = 3 \implies$ Cặp $(3, 12)$
* $i = 4 \implies$ Cặp $(4, 9)$
* $i = 6 \implies 6 \times 6 = 36$ (ước đơn lẻ vì hai ước trùng nhau)

### 3.2. Thuật toán đếm số lượng ước số của $N$:
```python
n = int(input())
dem_uoc = 0

i = 1
while i * i <= n:
    if n % i == 0:
        if i * i == n:
            dem_uoc += 1      # Hai ước trùng nhau (chính là căn bậc 2)
        else:
            dem_uoc += 2      # Thu được 1 cặp ước phân biệt: i và n // i
    i += 1

print(dem_uoc)
```

### 3.3. Nhận định vàng về Số chính phương
* Một số nguyên dương $N$ có **tổng số lượng ước là một số lẻ** khi và chỉ khi **$N$ là số chính phương**!
* **Cách kiểm tra số chính phương trong $\mathcal{O}(1)$:**
  ```python
  can = int(n ** 0.5)
  if can * can == n:
      print("LA SO CHINH PHUONG")
  ```

---

## 4. Ước chung lớn nhất ($\gcd$) và Bội chung nhỏ nhất ($\text{lcm}$)

### 4.1. Mối quan hệ mật thiết
Cho hai số nguyên dương $A$ và $B$:
$$\mathbf{\gcd(A, B) \times \text{lcm}(A, B) = A \times B} \implies \mathbf{\text{lcm}(A, B) = \frac{A \times B}{\gcd(A, B)}}$$

### 4.2. Khái niệm Nguyên tố cùng nhau
Hai số $A$ và $B$ được gọi là **nguyên tố cùng nhau** khi và chỉ khi Ước chung lớn nhất của chúng bằng 1:
$$\gcd(A, B) == 1$$

### 4.3. Cài đặt qua thư viện chuẩn `math`:
Trong Python 3, thư viện `math` tích hợp sẵn hàm tính toán tối ưu theo thuật toán Euclid:
```python
import math

a, b = map(int, input().split())

ucln = math.gcd(a, b)
bcnn = (a * b) // ucln

print(ucln, bcnn)
```

---

## 5. Phân tích một số ra Thừa số nguyên tố

Theo định lý cơ bản của số học, mọi số tự nhiên $N \ge 2$ đều biểu diễn được duy nhất dưới dạng:
$$N = p_1^{k_1} \times p_2^{k_2} \times \dots \times p_m^{k_m}$$
(trong đó $p_1 < p_2 < \dots < p_m$ là các số nguyên tố, $k_i \ge 1$).

### Thuật toán phân tích tối ưu $\mathcal{O}(\sqrt{N})$:
```python
n = int(input())
d = 2

while d * d <= n:
    while n % d == 0:
        print(d, end=" ")
        n //= d
    d += 1

if n > 1:
    print(n)  # Phần dư nguyên tố cuối cùng lớn hơn sqrt(N)
```

---

## 6. Bảng mô phỏng từng bước

### 6.1. Mô phỏng kiểm tra tính nguyên tố của $N = 37$
* Ngưỡng dừng: $i \times i \le 37 \implies i \le 6$ (vì $6 \times 6 = 36 \le 37$, $7 \times 7 = 49 > 37$).

| Bước Lặp $i$ | Kiểm Tra $i \times i \le 37$ | Phép Chia Dư $37 \% i$ | Có Chia Hết Không? | Hành Động |
|:---:|:---:|:---:|:---:|---|
| **$i = 2$** | $4 \le 37$ (Đúng) | $37 \% 2 = 1$ | Không | Tăng $i = 3$ |
| **$i = 3$** | $9 \le 37$ (Đúng) | $37 \% 3 = 1$ | Không | Tăng $i = 4$ |
| **$i = 4$** | $16 \le 37$ (Đúng) | $37 \% 4 = 1$ | Không | Tăng $i = 5$ |
| **$i = 5$** | $25 \le 37$ (Đúng) | $37 \% 5 = 2$ | Không | Tăng $i = 6$ |
| **$i = 6$** | $36 \le 37$ (Đúng) | $37 \% 6 = 1$ | Không | Tăng $i = 7$ |
| **$i = 7$** | $49 \le 37$ (**Sai**) | *(Không chạy)* | — | **Dừng lặp!** |

$$\implies \text{Không tìm thấy bất kỳ ước nào trong đoạn } [2, 6] \implies \mathbf{37\text{ là số nguyên tố!}}$$

### 6.2. Mô phỏng phân tích thừa số nguyên tố $N = 60$

| Bước | Thừa số $d$ | Điều kiện $60 \% d == 0$ | Thao tác | Giá trị $N$ sau khi chia |
|:---:|:---:|:---:|---|:---:|
| Khởi tạo | $d = 2$ | — | Khởi tạo | $60$ |
| Lần 1 | $d = 2$ | $60 \% 2 == 0$ (Đúng) | In `2 `, chia `60 // 2` | $30$ |
| Lần 2 | $d = 2$ | $30 \% 2 == 0$ (Đúng) | In `2 `, chia `30 // 2` | $15$ |
| Lần 3 | $d = 2$ | $15 \% 2 == 0$ (Sai) | Tăng $d = 3$ | $15$ |
| Lần 4 | $d = 3$ | $15 \% 3 == 0$ (Đúng) | In `3 `, chia `15 // 3` | $5$ |
| Lần 5 | $d = 3$ | $5 \% 3 == 0$ (Sai) | Tăng $d = 4$ | $5$ |
| Lần 6 | $d = 4$ | $4 \times 4 = 16 > 5$ | Thoát vòng `while d*d <= n` | $5$ |
| Sau vòng lặp | $n = 5 > 1$ | Số nguyên tố còn lại | In nốt `5 ` | $1$ |

$$\implies \text{Kết quả phân tích: } 60 = 2 \times 2 \times 3 \times 5$$

---

## 7. Lỗi hay gặp và cách tránh

> **BẪY LỖI 1: BỎ QUÊN TRƯỜNG HỢP $N < 2$**
> * Nhiều bạn chỉ kiểm tra từ $2$ mà quên số $0$, số $1$ và số âm, nên với $N = 1$ hay $N = 0$ lại kết luận là nguyên tố $\implies$ Sai hẳn!
> * **Điều bắt buộc phải nhớ:** Luôn mở đầu hàm bằng `if n < 2: return False`.

> **BẪY LỖI 2: DÙNG `range(2, int(n**0.5))` MÀ QUÊN CỘNG 1**
> * `range` bỏ cận trên nên với $N = 4$ vòng `range(2, 2)` rỗng và kết luận sai 4 là nguyên tố!
> * **Điều bắt buộc phải nhớ:** Dùng `while i * i <= n:` cho an toàn, khỏi lo sai số căn bậc hai.

> **BẪY LỖI 3: TRÀN BỘ NHỚ KHI TÍNH BCNN TRƯỚC KHI CHIA**
> * Dù Python hỗ trợ số lớn, `(a * b) // gcd(a, b)` vẫn tạo tích trung gian cực lớn.
> * **Cách viết chuẩn:** `(a // math.gcd(a, b)) * b`.

---

## 8. Mẫu code thường gặp

### Mẫu 1: Đếm số lượng số nguyên tố trong đoạn $[A, B]$
```python
import math

def la_nguyen_to(x):
    if x < 2:
        return False
    i = 2
    while i * i <= x:
        if x % i == 0:
            return False
        i += 1
    return True

a, b = map(int, input().split())
dem = 0
for x in range(a, b + 1):
    if la_nguyen_to(x):
        dem += 1
print(dem)
```

### Mẫu 2: Liệt kê tất cả các ước số theo thứ tự tăng dần
```python
n = int(input())
uoc_nho = []
uoc_lon = []

i = 1
while i * i <= n:
    if n % i == 0:
        uoc_nho.append(i)
        if i * i != n:
            uoc_lon.append(n // i)
    i += 1

# Ghép uoc_nho (tăng dần) với uoc_lon (đảo ngược để tăng dần)
tat_ca_uoc = uoc_nho + uoc_lon[::-1]
print(*(tat_ca_uoc))
```

---


## Bài tập thực hành


### Bài 01 [pya_l11_p06_uoc_chung_lon_nhat_bcnn]: Ước chung lớn nhất & BCNN

Bối cảnh: Thí sinh cần tìm giá trị lớn nhất hoặc nhỏ nhất trong một tập dữ liệu. Hãy viết chương trình tìm kiếm.

Nhiệm vụ: Cho 2 số nguyên dương $A$ và $B$. Hãy tìm Ước chung lớn nhất ($\text{GCD}$) và Bội chung nhỏ nhất ($\text{LCM}$) của 2 số này.

**Đầu vào (Input):**

Hai số nguyên $A, B$ cách nhau bởi khoảng trắng ($1 \le A, B \le 10^9$).

**Đầu ra (Output):**

Hai số nguyên: $\text{GCD}$ trước, $\text{LCM}$ sau, cách nhau một khoảng trắng.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 12 18 | 6 36 |

**Giải thích:**

$\text{GCD}(12, 18) = 6$, $\text{LCM}(12, 18) = (12 \times 18) // 6 = 36$.



### Bài 02 [pya_l11_p02_dem_so_luong_uoc_so]: Đếm số lượng ước số

Bối cảnh: Số lượng ước số là chỉ số quan trọng phản ánh tính chia hết của một số nguyên, đồng thời là cơ sở nhận biết số nguyên tố và số chính phương.

Nhiệm vụ: Cho số tự nhiên $N$. Hãy cho biết số $N$ có tất cả bao nhiêu ước số nguyên dương.

**Đầu vào (Input):**

Một số tự nhiên $N$ ($1 \le N \le 10^5$).

**Đầu ra (Output):**

Một số nguyên duy nhất là số lượng ước số của $N$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 10 | 4 |

**Giải thích:**

Số 10 có 4 ước: 1, 2, 5, 10.



### Bài 03 [pya_l11_p03_tinh_tong_cac_uoc_so]: Tính tổng các ước số

Bối cảnh: Trong bài kiểm tra, người dùng cần tính nhanh tổng một dãy số. Hãy viết chương trình hỗ trợ tính toán.

Nhiệm vụ: Cho số nguyên dương $N$. Hãy tính tổng tất cả các ước số của $N$.

**Đầu vào (Input):**

Một số nguyên $N$ ($1 \le N \le 10^5$).

**Đầu ra (Output):**

Tổng các ước số của $N$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 6 | 12 |

**Giải thích:**

Các ước là 1, 2, 3, 6 $\implies 1 + 2 + 3 + 6 = 12$.



### Bài 04 [pya_l11_p10_hai_so_nguyen_to_cung_nhau]: Hai số nguyên tố cùng nhau

Bối cảnh: An và Bình mỗi bạn có một rổ bi. Hai bạn muốn biết hai rổ bi của mình có "hợp nhau" không. Cô giáo bảo hai số $A$ và $B$ được gọi là nguyên tố cùng nhau nếu Ước chung lớn nhất của chúng bằng 1 ($\text{GCD}(A, B) = 1$). Hai bạn đếm mãi chưa xong, hãy hai bạn kiểm tra.

Nhiệm vụ: Cho 2 số nguyên dương $A$ và $B$. In ra `YES` nếu chúng nguyên tố cùng nhau, ngược lại in `NO`.

**Đầu vào (Input):**

Hai số $A, B$ ($1 \le A, B \le 10^9$).

**Đầu ra (Output):**

`YES` hoặc `NO`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 8 9 | YES |

**Giải thích:**

Với dữ liệu đầu vào là `8 9`, kết quả thu được tương ứng là `YES`.

**Ví dụ mẫu (Sample 2):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 12 18 | NO |



### Bài 05 [pya_l11_p01_liet_ke_tat_ca_uoc_so]: Liệt kê tất cả ước số

Bối cảnh: Xác định toàn bộ các ước số nguyên dương của một số nguyên là phép phân tích cơ bản trong số học, giúp giải quyết các bài toán chia đều tài nguyên và phân nhóm phần tử.

Nhiệm vụ: Nhập một số tự nhiên $N$. Hãy in ra tất cả các ước số nguyên dương của $N$ theo thứ tự tăng dần trên một dòng, cách nhau bởi khoảng trắng.

**Đầu vào (Input):**

Một số tự nhiên $N$ ($1 \le N \le 1000$).

**Đầu ra (Output):**

Dãy các ước số của $N$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 12 | 1 2 3 4 6 12 |

**Giải thích:**

Với dữ liệu đầu vào là `12`, kết quả thu được tương ứng là `1 2 3 4 6 12`.



### Bài 06 [pya_l11_p07_dem_uoc_chan_cua_n]: Đếm ước chẵn của N

Bối cảnh: Trong phân tích chia nhóm chẵn lẻ, việc xác định các ước số chẵn giúp tối ưu hóa việc phân chia tài nguyên thành các phần có kích thước chia hết cho 2.

Nhiệm vụ: Cho số nguyên dương $N$. Hãy đếm xem có bao nhiêu ước số của $N$ là số chẵn.

**Đầu vào (Input):**

Một số tự nhiên $N$ ($1 \le N \le 10^6$).

**Đầu ra (Output):**

Số lượng ước chẵn của $N$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 12 | 4 |

**Giải thích:**

Các ước của 12 là: 1, 2, 3, 4, 6, 12. Trong đó các ước chẵn là: 2, 4, 6, 12 (có 4 số).



### Bài 07 [pya_l11_p08_tim_uoc_so_lon_thu_hai]: Tìm ước số lớn thứ hai

Bối cảnh: Thí sinh đang tìm kiếm một giá trị đặc biệt trong tập dữ liệu. Hãy viết chương trình tìm kiếm hiệu quả.

Nhiệm vụ: Cho số nguyên dương $N$ ($N \ge 2$). Ước số lớn nhất của $N$ luôn là chính nó ($N$). Hãy tìm ước số lớn thứ hai của $N$ (tức là ước số lớn nhất nhưng nhỏ hơn $N$).

**Đầu vào (Input):**

Một số tự nhiên $N$ ($2 \le N \le 10^9$).

**Đầu ra (Output):**

Ước số lớn thứ hai của $N$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 24 | 12 |

**Giải thích:**

Ước lớn nhất là 24, lớn thứ hai là 12.

**Ví dụ mẫu (Sample 2):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 7 | 1 |

**Giải thích:**

Ước của 7 là 1 và 7, lớn thứ hai là 1.



### Bài 08 [pya_l11_p05_kiem_tra_so_chinh_phuong]: Kiểm tra số chính phương

Bối cảnh: Giờ xếp hình, Bo xếp các viên gạch thành một ô vuông thật ngay ngắn. Cô giáo cười và bảo những số gạch xếp được thành hình vuông như vậy gọi là số chính phương: số bằng bình phương của một số tự nhiên (ví dụ: $0, 1, 4, 9, 16, 25, \dots$). Bo có một đống gạch mà chưa biết có xếp vuông được không, hãy bạn ấy kiểm tra.

Nhiệm vụ: Nhập số nguyên dương $N$. Kiểm tra $N$ có phải số chính phương không. Nếu đúng in `YES`, ngược lại in `NO`.

**Đầu vào (Input):**

Một số nguyên $N$ ($1 \le N \le 10^9$).

**Đầu ra (Output):**

`YES` hoặc `NO`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 25 | YES |

**Giải thích:**

Với dữ liệu đầu vào là `25`, kết quả thu được tương ứng là `YES`.

**Ví dụ mẫu (Sample 2):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 20 | NO |



### Bài 09 [pya_l11_p13_phan_tich_ra_thua_so_nguyen_to]: Phân tích ra thừa số nguyên tố

Bối cảnh: Định lý cơ bản của số học khẳng định mọi số tự nhiên lớn hơn 1 đều phân tích được duy nhất thành tích các thừa số nguyên tố. Phép phân tích này đóng vai trò cốt lõi trong mật mã học.

Nhiệm vụ: Mọi số tự nhiên $N \ge 2$ đều có thể phân tích thành tích của các thừa số nguyên tố. Cho số tự nhiên $N$. Hãy in ra dạng phân tích của $N$.

**Đầu vào (Input):**

Một số tự nhiên $N$ ($2 \le N \le 10^6$).

**Đầu ra (Output):**

Dãy các thừa số nguyên tố tăng dần theo định dạng `p1 * p2 * ...`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 60 | 2 * 2 * 3 * 5 |

**Giải thích:**

Với dữ liệu đầu vào là `60`, kết quả thu được tương ứng là `2 * 2 * 3 * 5`.

**Ví dụ mẫu (Sample 2):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 17 | 17 |



### Bài 10 [pya_l11_p04_kiem_tra_so_nguyen_to]: Kiểm tra số nguyên tố

Bối cảnh: Trong giờ lập trình, thầy giáo đưa ra một bài toán kiểm tra tính chất của số. Hãy viết chương trình kiểm tra tự động.

Nhiệm vụ: Nhập vào số nguyên $N$. Hãy kiểm tra xem $N$ có phải là số nguyên tố hay không. Nếu có in `YES`, nếu không in `NO`.

**Đầu vào (Input):**

Một số nguyên $N$ ($0 \le N \le 10^7$).

**Đầu ra (Output):**

`YES` hoặc `NO`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 7 | YES |

**Giải thích:**

Với dữ liệu đầu vào là `7`, kết quả thu được tương ứng là `YES`.

**Ví dụ mẫu (Sample 2):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 1 | NO |

**Ví dụ mẫu (Sample 3):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 9 | NO |



### Bài 11 [pya_l11_p09_dem_so_nguyen_to_trong_doan]: Đếm số nguyên tố trong đoạn

Bối cảnh: Đếm số lượng số nguyên tố trong một khoảng giá trị cho trước là dạng toán kinh điển đánh giá hiệu quả của các thuật toán sàng lọc và kiểm tra số nguyên tố.

Nhiệm vụ: Cho hai số nguyên dương $A$ và $B$ ($1 \le A \le B \le 10^4$). Hãy đếm xem có bao nhiêu số nguyên tố nằm trong đoạn từ $A$ đến $B$ (tính cả $A$ và $B$).

**Đầu vào (Input):**

Hai số $A, B$ trên cùng một dòng.

**Đầu ra (Output):**

Số lượng số nguyên tố trong đoạn $[A, B]$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 10 20 | 4 |

**Giải thích:**

Có 4 số nguyên tố: 11, 13, 17, 19.



### Bài 12 [pya_l11_p14_tim_so_co_dung_3_uoc_so]: Tìm số có đúng 3 ước số

Bối cảnh: Bạn Xoài mở một câu lạc bộ sưu tầm những viên đá rất kén chọn. Bạn ấy chỉ giữ lại những viên đá mang số $X$ đặc biệt: một số tự nhiên $X$ có đúng 3 ước số nguyên dương khi và chỉ khi $X$ là bình phương của một số nguyên tố ($X = P^2$, ví dụ: $4 = 2^2, 9 = 3^2, 25 = 5^2, 49 = 7^2$). Xoài có cả một hộp đá mà đếm mãi chưa xong, hãy bạn ấy đếm.

Nhiệm vụ: Cho số nguyên dương $N$. Hãy đếm xem có bao nhiêu số nhỏ hơn hoặc bằng $N$ mà có **đúng 3 ước số**.

**Đầu vào (Input):**

Một số tự nhiên $N$ ($1 \le N \le 10^9$).

**Đầu ra (Output):**

Số lượng các số có đúng 3 ước số $\le N$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 30 | 3 |

**Giải thích:**

Có 3 số là: 4 ($2^2$), 9 ($3^2$), 25 ($5^2$).



### Bài 13 [pya_l11_p12_so_sieu_nguyen_to_super_prime]: Số siêu nguyên tố (super prime)

Bối cảnh: Bi có một chiếc tàu lượn bằng các chữ số rất lạ. Mỗi lần tàu chạy qua, chữ số ở cuối toa lại rơi xuống một cái. Bạn ấy reo lên khi phát hiện có những con số gọi là "Siêu nguyên tố": bản thân nó là số nguyên tố, và khi ta lần lượt xóa bớt chữ số tận cùng bên phải thì các số thu được vẫn luôn là số nguyên tố!
 * Ví dụ: Số $239$ là số nguyên tố.
 * Cắt đuôi 9 còn $23$ (vẫn là số nguyên tố).
 * Cắt đuôi 3 còn $2$ (vẫn là số nguyên tố).
 $\implies 239$ là một Siêu nguyên tố! Bi đố em tìm thêm thật nhiều số đặc biệt như vậy, hãy bạn ấy.

Nhiệm vụ: Cho số tự nhiên $N$. Hãy kiểm tra xem $N$ có phải là Siêu nguyên tố hay không. In `YES` hoặc `NO`.

**Đầu vào (Input):**

Một số tự nhiên $N$ ($1 \le N \le 10^7$).

**Đầu ra (Output):**

`YES` hoặc `NO`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 239 | YES |

**Giải thích:**

Với dữ liệu đầu vào là `239`, kết quả thu được tương ứng là `YES`.

**Ví dụ mẫu (Sample 2):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 23 | YES |

**Ví dụ mẫu (Sample 3):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 27 | NO |



### Bài 14 [pya_l11_p11_cap_so_nguyen_to_sinh_doi]: Cặp số nguyên tố sinh đôi

Bối cảnh: Hai chị em Song sinh nhà bạn Tí lúc nào cũng ngồi cạnh nhau thật thân thiết. Nghe chuyện đó, cô giáo đố cả lớp tìm những cặp số nguyên tố cũng "sinh đôi" như vậy. Hai số nguyên tố được gọi là "Sinh đôi" (Twin Primes) nếu chúng hơn kém nhau đúng 2 đơn vị (ví dụ: $(3, 5), (5, 7), (11, 13), (17, 19)$). Cả lớp tìm mãi chưa đủ, hãy các bạn liệt kê.

Nhiệm vụ: Cho số tự nhiên $N$ ($1 \le N \le 10^4$). Hãy in ra tất cả các cặp số nguyên tố sinh đôi $(P, P+2)$ sao cho $P+2 \le N$.

**Đầu vào (Input):**

Một số nguyên $N$.

**Đầu ra (Output):**

Mỗi dòng in một cặp số nguyên tố sinh đôi cách nhau bởi khoảng trắng, theo thứ tự tăng dần.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 15 | 3 5 <br> 5 7 <br> 11 13 |

**Giải thích:**

Với dữ liệu đầu vào là `15`, kết quả thu được tương ứng là `3 5
5 7
11 13`.



# Bài 10: Đếm số theo quy luật và số đặc biệt

## 1. Bài toán đếm — Nền tảng tư duy thuật toán

Bài toán **đếm** gặp rất nhiều trong lập trình: *cho một tập hợp số, đếm xem có bao nhiêu số thỏa điều kiện*.

Có hai cách làm: **duyệt** bằng `for` từng số một (dễ hiểu nhưng chậm khi tập số lớn), và **công thức toán học $\mathcal{O}(1)$** tính thẳng không cần duyệt (nhanh hơn rất nhiều, chỉ cần hiểu kỹ bản chất số học).

---

## 2. Công thức đếm bội số trong đoạn $[A, B]$ — Vũ khí $\mathcal{O}(1)$

### 2.1. Bài toán nền: Đếm bội số của $K$ trong đoạn $[1, N]$

Số lượng các số chia hết cho $K$ trong đoạn từ $1$ đến $N$ chính xác bằng:
$$\text{count}(1, N, K) = N \mathbin{//} K$$

**Ví dụ:** Đếm các bội của $5$ trong đoạn $[1, 30]$:
$$30 \mathbin{//} 5 = 6 \quad \text{(gồm 5, 10, 15, 20, 25, 30)}$$

```python
n = int(input())
k = int(input())
print(n // k)
```

### 2.2. Mở rộng: Đếm bội số trong đoạn bất kỳ $[A, B]$

Để đếm bội số của $K$ trong đoạn $[A, B]$, các em dùng **kỹ thuật trừ tiền tố**:
$$\text{count}(A, B, K) = (B \mathbin{//} K) - ((A - 1) \mathbin{//} K)$$

**Bản chất:** Lấy tổng số bội trong $[1, B]$ trừ đi số bội trong $[1, A-1]$, phần còn lại chính là số bội nằm trong $[A, B]$.

| Bước | Biểu thức | Giá trị | Ý nghĩa |
|------|-----------|---------|----------|
| Bội trong $[1, B]$ | $30 \mathbin{//} 4$ | $7$ | Gồm 4, 8, 12, 16, 20, 24, 28 |
| Bội trong $[1, A-1]$ | $(10 - 1) \mathbin{//} 4 = 9 \mathbin{//} 4$ | $2$ | Gồm 4, 8 |
| **Kết quả** | $7 - 2$ | **$5$** | Gồm 12, 16, 20, 24, 28 |

```python
a, b = map(int, input().split())
k = int(input())
print(b // k - (a - 1) // k)
```

> **Lưu ý quan trọng:** Phải dùng $(A - 1)$ chứ không phải $A$, kẻo bỏ sót khi $A$ chính là bội của $K$.

### 2.3. Đếm số chẵn, số lẻ trong đoạn

- **Số chẵn trong $[A, B]$** = Số bội của $2$ = $(B \mathbin{//} 2) - ((A - 1) \mathbin{//} 2)$
- **Số lẻ trong $[A, B]$** = Tổng phần tử trừ đi số chẵn = $(B - A + 1) - \text{(số chẵn)}$

```python
a, b = map(int, input().split())
chan = b // 2 - (a - 1) // 2
le = (b - a + 1) - chan
print("Chan:", chan)
print("Le:", le)
```

---

## 3. Nguyên lý Bao hàm – Loại trừ (Inclusion-Exclusion)

### 3.1. Bài toán: Đếm số chia hết cho $2$ **hoặc** $3$ trong $[1, N]$

Cộng thẳng số bội của $2$ với số bội của $3$ sẽ **đếm lặp** các số chia hết cho cả hai (tức bội của $6$). Công thức đúng:

$$|A \cup B| = |A| + |B| - |A \cap B|$$

Áp dụng vào bài toán:
$$\text{count} = (N \mathbin{//} 2) + (N \mathbin{//} 3) - (N \mathbin{//} 6)$$

**Mô phỏng với $N = 30$:**

| Tập hợp | Biểu thức | Giá trị |
|---------|-----------|---------|
| Bội của $2$ | $30 \mathbin{//} 2$ | $15$ |
| Bội của $3$ | $30 \mathbin{//} 3$ | $10$ |
| Bội chung ($6$) | $30 \mathbin{//} 6$ | $5$ |
| **Kết quả** | $15 + 10 - 5$ | **$20$** |

```python
n = int(input())
count = n // 2 + n // 3 - n // 6
print(count)
```

> **Mẹo nhớ:** BCNN$(2, 3) = 6$. Chia hết cho cả $2$ **và** $3$ tức là chia hết cho BCNN của chúng.

---

## 4. Số đặc biệt — Khám phá các quy luật ẩn giấu

### 4.1. Số hoàn hảo

Một số tự nhiên $N > 1$ được gọi là **số hoàn hảo** nếu tổng tất cả các ước nhỏ hơn nó đúng bằng chính nó.

**Ví dụ:** $6 = 1 + 2 + 3$ (các ước nhỏ hơn $6$ là $1, 2, 3$).

| Số | Các ước nhỏ hơn nó | Tổng ước | Hoàn hảo? |
|---|---|---|---|
| $6$ | $1, 2, 3$ | $6$ | Đúng bằng $6$ |
| $12$ | $1, 2, 3, 4, 6$ | $16$ | Lớn hơn $12$ |
| $28$ | $1, 2, 4, 7, 14$ | $28$ | Đúng bằng $28$ |

```python
n = int(input())
tong_uoc = 0
for i in range(1, n):
    if n % i == 0:
        tong_uoc += i
if tong_uoc == n:
    print("HOAN HAO")
else:
    print("KHONG HOAN HAO")
```

### 4.2. Số phong phú và Số thiếu hụt

Dựa trên mối quan hệ giữa tổng ước và chính số đó:
- **Số phong phú:** Tổng ước $>$ chính nó. Ví dụ: $12$ (tổng ước $= 16 > 12$).
- **Số thiếu hụt:** Tổng ước $<$ chính nó. Ví dụ: $8$ (ước: $1, 2, 4$, tổng $= 7 < 8$).
- **Số hoàn hảo:** Tổng ước $=$ chính nó.

### 4.3. Số chính phương

Một số $N$ là **số chính phương** nếu tồn tại một số nguyên $k$ sao cho $k^2 = N$.

**Kiểm tra bằng Python:** Lấy căn bậc hai rồi kiểm tra xem bình phương lại có bằng $N$ không:

```python
n = int(input())
k = int(n ** 0.5)
if k * k == n:
    print("CHINH PHUONG")
else:
    print("KHONG CHINH PHUONG")
```

> **Lưu ý:** Dùng `int(n ** 0.5)` thay vì `round(n ** 0.5)` cho khỏi lỗi làm tròn, rồi kiểm tra bằng `k * k == n`; **tuyệt đối không dùng** `n ** 0.5 == int(n ** 0.5)` vì sai số số thực.

**Dãy số chính phương đầu tiên:** $1, 4, 9, 16, 25, 36, 49, 64, 81, 100, \dots$

**Tính chất đặc biệt của chữ số tận cùng:** Bình phương của số tự nhiên chỉ tận cùng bằng: $0, 1, 4, 5, 6, 9$. **Không bao giờ** tận cùng bằng $2, 3, 7, 8$.

### 4.4. Số Armstrong

Một số $N$ có $d$ chữ số được gọi là **số Armstrong bậc $d$** nếu tổng lũy thừa bậc $d$ của từng chữ số bằng chính nó.

**Ví dụ:** $153$ có $3$ chữ số: $1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153$.

```python
n = int(input())
temp = n
d = len(str(n))
tong = 0
while temp > 0:
    chu_so = temp % 10
    tong += chu_so ** d
    temp //= 10
if tong == n:
    print("ARMSTRONG")
else:
    print("KHONG ARMSTRONG")
```

---

## 5. Bảng mô phỏng biến thiên ô nhớ

### 5.1. Dry Run: Kiểm tra $N = 153$ có phải số Armstrong

| Bước | `temp` | `chu_so = temp % 10` | `tong += chu_so ** 3` | `temp //= 10` |
|------|--------|-----------------------|------------------------|----------------|
| Ban đầu | $153$ | — | $0$ | — |
| Vòng 1 | $153$ | $3$ | $0 + 27 = 27$ | $15$ |
| Vòng 2 | $15$ | $5$ | $27 + 125 = 152$ | $1$ |
| Vòng 3 | $1$ | $1$ | $152 + 1 = 153$ | $0$ |
| Kết thúc | $0$ | — | **$153 = N$** → `ARMSTRONG` | — |

### 5.2. Dry Run: Đếm bội của $7$ trong $[15, 50]$

| Bước | Biểu thức | Giá trị |
|------|-----------|---------|
| Bội trong $[1, 50]$ | $50 \mathbin{//} 7$ | $7$ |
| Bội trong $[1, 14]$ | $(15 - 1) \mathbin{//} 7 = 14 \mathbin{//} 7$ | $2$ |
| **Kết quả** | $7 - 2$ | **$5$** (gồm $21, 28, 35, 42, 49$) |

---

## 6. Lỗi hay gặp và cách tránh

### 6.1. Lỗi hay gặp 1: Quên trừ $1$ trong công thức đếm đoạn $[A, B]$

```python
# SAI: Dùng A thay vì A-1
count = b // k - a // k  # Bỏ sót khi A chia hết cho K

# ĐÚNG:
count = b // k - (a - 1) // k
```

**Ví dụ:** $A = 6, B = 12, K = 6$. Kết quả đúng: $2$ (gồm $6, 12$). Nếu dùng $A$ thay $A-1$: $(12 \mathbin{//} 6) - (6 \mathbin{//} 6) = 2 - 1 = 1$. Thiếu mất một số!

### 6.2. Lỗi hay gặp 2: Kiểm tra số chính phương bằng so sánh số thực

```python
# SAI: Sai số số thực làm kết quả sai
import math
if math.sqrt(n) == int(math.sqrt(n)):  # SAI!

# ĐÚNG: Dùng phép nhân nguyên
k = int(n ** 0.5)
if k * k == n:  # Chính xác 100%
```

### 6.3. Lỗi hay gặp 3: Duyệt ước quên bắt đầu từ $1$ (không phải $0$)

```python
# SAI: ZeroDivisionError vì n % 0 gây lỗi
for i in range(0, n):
    if n % i == 0: ...

# ĐÚNG: Bắt đầu từ 1
for i in range(1, n):
    if n % i == 0:
        tong_uoc += i
```

### 6.4. Lỗi hay gặp 4: Nhầm lẫn "chia hết cho cả A và B" với "chia hết cho A hoặc B"

```python
# Chia hết cho CẢ 2 VÀ 3 → dùng BCNN
count_and = n // 6

# Chia hết cho 2 HOẶC 3 → dùng Bao hàm - Loại trừ
count_or = n // 2 + n // 3 - n // 6
```

---

## 7. Mẫu code thường gặp

### 7.1. Liệt kê tất cả số hoàn hảo nhỏ hơn $N$

```python
n = int(input())
for so in range(2, n):
    tong_uoc = 0
    for i in range(1, so):
        if so % i == 0:
            tong_uoc += i
    if tong_uoc == so:
        print(so)
```

### 7.2. Đếm bội chung của $3$ và $5$ trong đoạn $[A, B]$

```python
a, b = map(int, input().split())
k = 15
print(b // k - (a - 1) // k)
```

### 7.3. Liệt kê số Armstrong ba chữ số

```python
for n in range(100, 1000):
    d1 = n // 100
    d2 = n // 10 % 10
    d3 = n % 10
    if d1 ** 3 + d2 ** 3 + d3 ** 3 == n:
        print(n)
```

---


## Bài tập thực hành


### Bài 01 [pya_l12_p01_dem_so_chia_het_cho_k]: Đếm số chia hết cho K

Bối cảnh: Bài toán đếm số phần tử chia hết cho một số nguyên $K$ trong một khoảng số liên tiếp là nền tảng xây dựng các thuật toán tối ưu thời gian $\mathcal{O}(1)$.

Nhiệm vụ: Cho 2 số nguyên dương $N$ và $K$. Hãy đếm xem trong các số từ $1$ đến $N$, có bao nhiêu số chia hết cho $K$.

**Đầu vào (Input):**

Hai số nguyên $N$ và $K$ ($1 \le N, K \le 10^9$) cách nhau bởi khoảng trắng.

**Đầu ra (Output):**

Một số nguyên duy nhất là số lượng các số chia hết cho $K$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 20 3 | 6 |

**Giải thích:**

Có 6 số: 3, 6, 9, 12, 15, 18.



### Bài 02 [pya_l12_p07_dem_so_chia_het_cho_2_hoac_3]: Đếm số chia hết cho 2 hoặc 3

Bối cảnh: Bài toán đếm số lượng phần tử thỏa mãn ít nhất một trong hai điều kiện chia hết là bài toán mẫu mực áp dụng Nguyên lý Bao hàm – Loại trừ (Inclusion-Exclusion).

Nhiệm vụ: Cho số nguyên dương $N$ ($1 \le N \le 10^{12}$). Hãy đếm xem từ 1 đến $N$ có bao nhiêu số chia hết cho 2 hoặc chia hết cho 3.

**Đầu vào (Input):**

Một số nguyên $N$.

**Đầu ra (Output):**

Số lượng số thỏa mãn.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 10 | 7 |

**Giải thích:**

Các số là: 2, 3, 4, 6, 8, 9, 10 (có 7 số).



### Bài 03 [pya_l12_p02_dem_so_le_trong_doan]: Đếm số lẻ trong đoạn

Bối cảnh: Trong thống kê dữ liệu liên tục, việc xác định số lượng phần tử lẻ trong một đoạn đóng vai trò kiểm tra tính phân bố đều của tập số liệu.

Nhiệm vụ: Cho 2 số nguyên dương $A$ và $B$ ($1 \le A \le B \le 10^9$). Hãy đếm xem có bao nhiêu số lẻ nằm trong đoạn từ $A$ đến $B$ (tính cả $A$ và $B$).

**Đầu vào (Input):**

Hai số $A, B$ trên cùng một dòng.

**Đầu ra (Output):**

Số lượng số lẻ.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 3 8 | 3 |

**Giải thích:**

Có 3 số lẻ là: 3, 5, 7.



### Bài 04 [pya_l12_p06_dem_boi_cua_3_nhung_khong_chia_het_cho_5]: Đếm bội của 3 nhưng không chia hết cho 5

Bối cảnh: Trong lý thuyết tập hợp, bài toán xác định các phần tử thuộc tập này nhưng không thuộc tập khác đòi hỏi kỹ thuật trừ tập hợp chính xác để tránh đếm lặp.

Nhiệm vụ: Cho 2 số nguyên dương $A$ và $B$ ($1 \le A \le B \le 10^{12}$). Hãy đếm xem trong đoạn từ $A$ đến $B$ có bao nhiêu số chia hết cho 3 nhưng **không chia hết cho 5**.

**Đầu vào (Input):**

Hai số $A$ và $B$ cách nhau bởi khoảng trắng.

**Đầu ra (Output):**

Số lượng số thỏa mãn.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 1 30 | 8 |

**Giải thích:**

Với dữ liệu đầu vào là `1 30`, kết quả thu được tương ứng là `8`.



### Bài 05 [pya_l12_p04_so_armstrong_ba_chu_so]: Số Armstrong ba chữ số

Bối cảnh: Bạn Tôm tìm thấy một chiếc hộp phép thuật có khóa bằng số. Trên hộp ghi rằng chỉ những số Armstrong mới mở được khóa. Số Armstrong có 3 chữ số là số tự nhiên có dạng $\overline{abc}$ thỏa mãn $a^3 + b^3 + c^3 = \overline{abc}$. Tôm thử mãi chưa mở được hộp, hãy bạn ấy kiểm tra.

Nhiệm vụ: Cho một số có đúng 3 chữ số $N$. Kiểm tra xem $N$ có phải là số Armstrong không. In `YES` hoặc `NO`.

**Đầu vào (Input):**

Một số nguyên $N$ ($100 \le N \le 999$).

**Đầu ra (Output):**

`YES` hoặc `NO`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 153 | YES |

**Giải thích:**

Với dữ liệu đầu vào là `153`, kết quả thu được tương ứng là `YES`.

**Ví dụ mẫu (Sample 2):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 200 | NO |



### Bài 06 [pya_l12_p12_so_tu_man_narcissistic_number_k_chu_so]: Số tự mãn (Narcissistic number K chữ số)

Bối cảnh: Bạn Kiến rất tự hào vì mỗi bạn kiến trong đàn đều góp sức làm nên tổ lớn. Bạn ấy nghe cô kể về những con số cũng "tự hào" như vậy. Một số tự nhiên $N$ có $K$ chữ số được gọi là "Số tự mãn" (Narcissistic number) nếu tổng lũy thừa bậc $K$ của các chữ số của nó đúng bằng chính số $N$.
 Ví dụ:
 * $N = 153$ có 3 chữ số: $1^3 + 5^3 + 3^3 = 153$ $\implies$ Thỏa mãn.
 * $N = 1634$ có 4 chữ số: $1^4 + 6^4 + 3^4 + 4^4 = 1 + 1296 + 81 + 256 = 1634$ $\implies$ Thỏa mãn. Kiến đố em tìm thêm những con số đặc biệt này, hãy bạn ấy.

Nhiệm vụ: Cho số nguyên dương $N$ ($1 \le N \le 10^9$). Hãy kiểm tra xem $N$ có phải là số tự mãn không. In `YES` nếu đúng, ngược lại in `NO`.

**Đầu vào (Input):**

Một số nguyên $N$.

**Đầu ra (Output):**

`YES` hoặc `NO`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 1634 | YES |

**Giải thích:**

Với dữ liệu đầu vào là `1634`, kết quả thu được tương ứng là `YES`.

**Ví dụ mẫu (Sample 2):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 2024 | NO |



### Bài 07 [pya_l12_p10_dem_so_khong_chua_chu_so_0]: Đếm số không chứa chữ số 0

Bối cảnh: Trong thiết kế hệ thống hiển thị số không hỗ trợ ký tự 0, các số chỉ tạo bởi các chữ số từ 1 đến 9 được coi là số hợp lệ cần được thống kê chính xác.

Nhiệm vụ: Cho số nguyên dương $N$. Hãy đếm xem từ 1 đến $N$ có bao nhiêu số mà trong cách ghi thập phân của nó **không chứa bất kỳ chữ số 0 nào**.

**Đầu vào (Input):**

Một số nguyên $N$ ($1 \le N \le 10^6$).

**Đầu ra (Output):**

Số lượng số thỏa mãn.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 15 | 14 |

**Giải thích:**

Từ 1 đến 15 chỉ có duy nhất số 10 chứa chữ số 0. Vậy có $15 - 1 = 14$ số.



### Bài 08 [pya_l12_p03_kiem_tra_so_hoan_hao]: Kiểm tra số hoàn hảo

Bối cảnh: Bạn Mèo chia những chiếc kẹo cho các bạn búp bê của mình. Có hôm bạn ấy ngạc nhiên vì số kẹo chia ra vừa khít, không thừa chiếc nào. Cô giáo bảo đó chính là "Số hoàn hảo": một số nguyên dương $N$ được gọi là "Số hoàn hảo" nếu tổng tất cả các ước số nguyên dương nhỏ hơn $N$ bằng chính số $N$. Mèo có nhiều gói kẹo mà kiểm tra mãi chưa hết, hãy bạn ấy.

Nhiệm vụ: Nhập số nguyên dương $N$. Kiểm tra $N$ có phải số hoàn hảo không. In `YES` nếu đúng, ngược lại in `NO`.

**Đầu vào (Input):**

Một số nguyên $N$ ($1 \le N \le 10^6$).

**Đầu ra (Output):**

`YES` hoặc `NO`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 6 | YES |

**Giải thích:**

Với dữ liệu đầu vào là `6`, kết quả thu được tương ứng là `YES`.

**Ví dụ mẫu (Sample 2):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 10 | NO |



### Bài 09 [pya_l12_p11_dem_so_chinh_phuong_trong_doan]: Đếm số chính phương trong đoạn

Bối cảnh: Xác định số lượng số chính phương trong một phạm vi lớn là bài toán tối ưu quan trọng, yêu cầu chuyển đổi từ duyệt từng phần tử sang phương pháp tính giải tích bằng căn bậc hai.

Nhiệm vụ: Cho 2 số nguyên dương $A$ và $B$ ($1 \le A \le B \le 10^{14}$). Hãy đếm xem có bao nhiêu số chính phương nằm trong đoạn từ $A$ đến $B$.

**Đầu vào (Input):**

Hai số nguyên $A, B$ trên cùng một dòng.

**Đầu ra (Output):**

Số lượng số chính phương trong đoạn $[A, B]$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 5 25 | 3 |

**Giải thích:**

Có 3 số chính phương là 9, 16, 25.



### Bài 10 [pya_l12_p05_tim_tat_ca_so_hoan_hao_nho_hon_n]: Tìm tất cả số hoàn hảo nhỏ hơn N

Bối cảnh: Thí sinh đang tìm kiếm một giá trị đặc biệt trong tập dữ liệu. Hãy viết chương trình tìm kiếm hiệu quả.

Nhiệm vụ: Cho số nguyên dương $N$ ($1 \le N \le 10^4$). Hãy in ra tất cả các số hoàn hảo nhỏ hơn hoặc bằng $N$ theo thứ tự tăng dần.

**Đầu vào (Input):**

Một số nguyên $N$.

**Đầu ra (Output):**

Các số hoàn hảo, cách nhau bởi khoảng trắng.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 30 | 6 28 |

**Giải thích:**

Với dữ liệu đầu vào là `30`, kết quả thu được tương ứng là `6 28`.



### Bài 11 [pya_l12_p09_so_phong_phu_abundant_number]: Số phong phú (abundant number)

Bối cảnh: Bạn Ổi có một giỏ đầy những quả ngọt để chia cho bạn bè. Có những con số cũng "rộng rãi" giống như giỏ quả của Ổi vậy. Một số tự nhiên được gọi là "Số phong phú" nếu tổng các ước số nhỏ hơn nó lớn hơn chính nó (ví dụ: số 12 có tổng các ước nhỏ hơn nó là $1+2+3+4+6=16 > 12$). Ổi muốn tìm thật nhiều con số rộng rãi như thế, hãy bạn ấy.

Nhiệm vụ: Nhập số nguyên dương $N$. Hãy in ra tất cả các số phong phú nhỏ hơn hoặc bằng $N$.

**Đầu vào (Input):**

Số nguyên $N$ ($1 \le N \le 10^4$).

**Đầu ra (Output):**

Dãy các số phong phú tăng dần trên một dòng.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 20 | 12 18 20 |

**Giải thích:**

Với dữ liệu đầu vào là `20`, kết quả thu được tương ứng là `12 18 20`.



### Bài 12 [pya_l12_p08_cap_so_than_thiet]: Cặp số thân thiết

Bối cảnh: Hai bạn thân Nấm và Mít chơi trò chia kẹo công bằng cho nhau. Cô giáo kể rằng trong thế giới các con số cũng có những đôi bạn như vậy. Hai số $A$ và $B$ ($A \ne B$) được gọi là "Cặp số thân thiết" nếu tổng các ước số nhỏ hơn $A$ bằng $B$, và tổng các ước số nhỏ hơn $B$ bằng $A$. Hai bạn tìm mãi chưa ra các cặp số thân nhau, hãy hai bạn kiểm tra.

Nhiệm vụ: Cho 2 số nguyên dương $A$ và $B$. In ra `YES` nếu chúng là cặp số thân thiết, ngược lại in `NO`.

**Đầu vào (Input):**

Hai số $A, B$ ($1 \le A, B \le 10^5$).

**Đầu ra (Output):**

`YES` hoặc `NO`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 220 284 | YES |

**Giải thích:**

Với dữ liệu đầu vào là `220 284`, kết quả thu được tương ứng là `YES`.

**Ví dụ mẫu (Sample 2):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 10 20 | NO |



# CHƯƠNG 04: DANH SÁCH (LIST) & THỐNG KÊ


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


## Bài tập thực hành


### Bài 01 [pya_l16_p23_thuong_doc_sach]: Thưởng đọc sách

Bối cảnh: Để khuyến khích đọc sách, thư viện treo giải: bạn nào đọc hết $N$ quyển sách sẽ được thưởng sao. Quyển thứ 1 được 1 sao, quyển thứ 2 được 2 sao, cứ thế quyển thứ $N$ được $N$ sao. An quyết tâm đọc hết $N$ quyển và muốn biết trước mình sẽ nhận được bao nhiêu sao.

Nhiệm vụ: Cho số $N$. Hãy tính tổng số sao từ quyển 1 đến quyển $N$.

**Đầu vào (Input):**

Một số nguyên $N$ ($1 \le N \le 10^{12}$).

**Đầu ra (Output):**

In ra một số nguyên duy nhất là tổng số sao.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 5 | 15 |

**Giải thích:**

$1 + 2 + 3 + 4 + 5 = 15$ sao.



### Bài 02 [pya_l16_p21_so_ghe_doi_xung]: Số ghế đối xứng

Bối cảnh: Rạp xiếc trong thành phố có một hàng ghế đặc biệt: những ghế mang số đối xứng (đọc từ trái sang phải hay từ phải sang trái đều giống nhau, như 121 hay 44) được gọi là ghế vàng và ngồi xem rất rõ. Mi mua được vé ghế số $N$ và muốn biết ghế của mình có phải ghế vàng không.

Nhiệm vụ: Hãy kiểm tra số $N$ có phải số đối xứng không. In `YES` nếu đúng, ngược lại in `NO`.

**Đầu vào (Input):**

Một số tự nhiên $N$ ($1 \le N \le 10^{18}$).

**Đầu ra (Output):**

In ra `YES` hoặc `NO`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 121 | YES |

**Giải thích:**

Số 121 đọc xuôi là 121, đọc ngược cũng là 121 nên đây là ghế vàng.



### Bài 03 [pya_l16_p08_tim_vi_tri_dau_tien_cua_x]: Tìm vị trí đầu tiên của X

Bối cảnh: Thí sinh đang tìm kiếm một giá trị đặc biệt trong tập dữ liệu. Hãy viết chương trình tìm kiếm hiệu quả.

Nhiệm vụ: Cho dãy $N$ số nguyên và số $X$. Hãy tìm vị trí (chỉ số index từ 0) xuất hiện **đầu tiên** của số $X$ trong dãy. Nếu số $X$ không có trong dãy, in ra `-1`.

**Đầu vào (Input):**

* Dòng 1: Hai số nguyên $N$ và $X$.
 * Dòng 2: $N$ số nguyên.

**Đầu ra (Output):**

Vị trí index đầu tiên của $X$, hoặc `-1`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 5 7 <br> 3 5 7 9 7 | 2 |

**Giải thích:**

Với dữ liệu đầu vào là `5 7
3 5 7 9 7`, kết quả thu được tương ứng là `2`.

**Ví dụ mẫu (Sample 2):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 4 10 <br> 1 2 3 4 | -1 |



### Bài 04 [pya_l16_p01_nhap_day_so_in_phan_tu_dau_cuoi]: Nhập dãy số & in phần tử đầu - cuối

Bối cảnh: Truy xuất phần tử biên (đầu dãy và cuối dãy) là thao tác truy cập nhanh có độ phức tạp $\mathcal{O}(1)$ trên cấu trúc dữ liệu danh sách.

Nhiệm vụ: Cho một dãy gồm $N$ số nguyên. Hãy in ra phần tử đầu tiên và phần tử cuối cùng của dãy số đó.

**Đầu vào (Input):**

* Dòng 1: Số nguyên dương $N$ ($1 \le N \le 1000$).
 * Dòng 2: Gồm $N$ số nguyên cách nhau bởi khoảng trắng.

**Đầu ra (Output):**

In phần tử đầu tiên và phần tử cuối cùng trên một dòng, cách nhau một khoảng trắng.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 5 <br> 10 25 3 47 99 | 10 99 |

**Giải thích:**

Với dữ liệu đầu vào là `5
10 25 3 47 99`, kết quả thu được tương ứng là `10 99`.



### Bài 05 [pya_l16_p03_tinh_tong_cac_phan_tu_trong_day]: Tính tổng các phần tử trong dãy

Bối cảnh: Trong bài kiểm tra, người dùng cần tính nhanh tổng một dãy số. Hãy viết chương trình hỗ trợ tính toán.

Nhiệm vụ: Cho một dãy gồm $N$ số nguyên. Hãy tính tổng tất cả các phần tử trong dãy số.

**Đầu vào (Input):**

* Dòng 1: Số nguyên dương $N$ ($1 \le N \le 10^5$).
 * Dòng 2: $N$ số nguyên ($|A_i| \le 10^9$).

**Đầu ra (Output):**

Tổng các phần tử trong dãy.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 4 <br> 10 20 30 40 | 100 |

**Giải thích:**

Với dữ liệu đầu vào là `4
10 20 30 40`, kết quả thu được tương ứng là `100`.



### Bài 06 [pya_l16_p05_tim_so_lon_nhat_nho_nhat]: Tìm số lớn nhất & nhỏ nhất

Bối cảnh: Thí sinh đang tìm kiếm một giá trị đặc biệt trong tập dữ liệu. Hãy viết chương trình tìm kiếm hiệu quả.

Nhiệm vụ: Cho dãy $N$ số nguyên. Hãy tìm giá trị lớn nhất và giá trị nhỏ nhất trong dãy số.

**Đầu vào (Input):**

* Dòng 1: Số nguyên $N$ ($1 \le N \le 10^5$).
 * Dòng 2: $N$ số nguyên.

**Đầu ra (Output):**

Giá trị lớn nhất, theo sau là giá trị nhỏ nhất, cách nhau một khoảng trắng.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 5 <br> 12 5 89 3 45 | 89 3 |

**Giải thích:**

Với dữ liệu đầu vào là `5
12 5 89 3 45`, kết quả thu được tương ứng là `89 3`.



### Bài 07 [pya_l16_p06_in_day_so_theo_thu_tu_dao_nguoc]: In dãy số theo thứ tự đảo ngược

Bối cảnh: Đảo ngược thứ tự các phần tử trong danh sách dữ liệu thường được yêu cầu khi cần phân tích luồng sự kiện theo trình tự thời gian từ mới nhất về cũ nhất.

Nhiệm vụ: Cho dãy $N$ số nguyên. Hãy in ra dãy số theo thứ tự ngược lại (từ phần tử cuối cùng về phần tử đầu tiên).

**Đầu vào (Input):**

* Dòng 1: Số nguyên $N$ ($1 \le N \le 10^5$).
 * Dòng 2: $N$ số nguyên.

**Đầu ra (Output):**

Dãy số sau khi đảo ngược trên một dòng.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 4 <br> 1 2 3 4 | 4 3 2 1 |

**Giải thích:**

Với dữ liệu đầu vào là `4
1 2 3 4`, kết quả thu được tương ứng là `4 3 2 1`.



### Bài 08 [pya_l16_p07_dem_so_lan_xuat_hien_cua_x]: Đếm số lần xuất hiện của X

Bối cảnh: Đếm số lần xuất hiện của một giá trị mục tiêu trong danh sách hỗ trợ xác định tần suất dữ liệu và kiểm tra trùng lặp.

Nhiệm vụ: Cho dãy $N$ số nguyên và một số nguyên $X$. Hãy đếm xem số $X$ xuất hiện bao nhiêu lần trong dãy số.

**Đầu vào (Input):**

* Dòng 1: Hai số nguyên $N$ và $X$ ($1 \le N \le 10^5$).
 * Dòng 2: $N$ số nguyên.

**Đầu ra (Output):**

Số lần xuất hiện của $X$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 6 5 <br> 5 2 5 7 5 9 | 3 |

**Giải thích:**

Với dữ liệu đầu vào là `6 5
5 2 5 7 5 9`, kết quả thu được tương ứng là `3`.



### Bài 09 [pya_l16_p11_thay_the_tat_ca_so_am_bang_so_0]: Thay thế tất cả số âm bằng số 0

Bối cảnh: Trong chuẩn hóa tín hiệu số, các giá trị âm không hợp lệ thường được quy chuẩn về ngưỡng giá trị sàn bằng 0.

Nhiệm vụ: Cho dãy $N$ số nguyên gồm cả số âm và số dương. Hãy thay thế toàn bộ các số âm trong dãy bằng số 0 và in ra dãy mới.

**Đầu vào (Input):**

* Dòng 1: Số nguyên $N$ ($1 \le N \le 10^5$).
 * Dòng 2: $N$ số nguyên.

**Đầu ra (Output):**

Dãy số sau khi thay thế.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 5 <br> 3 -5 8 -2 0 | 3 0 8 0 0 |

**Giải thích:**

Với dữ liệu đầu vào là `5
3 -5 8 -2 0`, kết quả thu được tương ứng là `3 0 8 0 0`.



### Bài 10 [pya_l16_p15_heo_dat_tiet_kiem]: Heo đất tiết kiệm

Bối cảnh: Na có một chú heo đất màu hồng rất xinh. Mỗi ngày, nhỏ bỏ vào heo $A$ đồng tiền ăn sáng để dành. Đặc biệt, cứ vào các ngày chẵn (ngày thứ 2, 4, 6, ...) nhỏ còn được mẹ thưởng thêm $B$ đồng vì chăm ngoan. Sau $N$ ngày, Na hồi hộp muốn biết trong heo có tất cả bao nhiêu tiền.

Nhiệm vụ: Hãy tính tổng số tiền trong heo đất sau $N$ ngày.

**Đầu vào (Input):**

Một dòng gồm ba số nguyên $N$, $A$, $B$ ($1 \le N \le 10^6$, $1 \le A, B \le 10^4$).

**Đầu ra (Output):**

In ra một số nguyên duy nhất là tổng số tiền.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 5 10 3 | 56 |

**Giải thích:**

5 ngày, mỗi ngày 10 đồng được 50 đồng. Các ngày chẵn là ngày 2 và ngày 4, được thưởng thêm $2 \times 3 = 6$ đồng. Tổng cộng $50 + 6 = 56$ đồng.



### Bài 11 [pya_l16_p04_dem_so_luong_so_chan_trong_mang]: Đếm số lượng số chẵn trong mảng

Bối cảnh: Thống kê số lượng phần tử chẵn trong mảng dữ liệu là bài toán lọc dữ liệu cơ bản để phân loại luồng số liệu đầu vào.

Nhiệm vụ: Cho một dãy gồm $N$ số nguyên dương. Hãy đếm xem có bao nhiêu số chẵn trong dãy.

**Đầu vào (Input):**

* Dòng 1: Số nguyên $N$ ($1 \le N \le 10^5$).
 * Dòng 2: $N$ số nguyên.

**Đầu ra (Output):**

Số lượng số chẵn.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 5 <br> 2 5 8 10 13 | 3 |

**Giải thích:**

Với dữ liệu đầu vào là `5
2 5 8 10 13`, kết quả thu được tương ứng là `3`.



### Bài 12 [pya_l16_p02_them_diem_vao_danh_sach]: Thêm điểm vào danh sách

Bối cảnh: Lớp của bạn Na vừa làm bài kiểm tra nên cô giáo có một danh sách điểm kiểm tra ban đầu. Sáng nay, bạn Tí nộp bài muộn và cô đã chấm cho bạn điểm $X$. Cô muốn viết thêm điểm $X$ này vào cuối danh sách mà không làm mất điểm của các bạn khác. Hãy giúp cô thêm điểm mới vào danh sách.

Nhiệm vụ: Cho danh sách các số nguyên ban đầu và số $X$. Hãy thêm $X$ vào cuối danh sách và in ra toàn bộ danh sách mới.

**Đầu vào (Input):**

* Dòng 1: Danh sách các số nguyên cách nhau bởi khoảng trắng.
 * Dòng 2: Số nguyên $X$.

**Đầu ra (Output):**

Danh sách các số sau khi thêm $X$, cách nhau bởi khoảng trắng.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 8 9 7 10 <br> 9 | 8 9 7 10 9 |

**Giải thích:**

Với dữ liệu đầu vào là `8 9 7 10
9`, kết quả thu được tương ứng là `8 9 7 10 9`.



### Bài 13 [pya_l16_p12_chen_so_vao_vi_tri_k]: Chèn số vào vị trí K

Bối cảnh: Chèn thêm phần tử mới vào một vị trí chỉ định trong danh sách là thao tác cấu trúc dữ liệu phổ biến khi bổ sung dữ liệu có thứ tự.

Nhiệm vụ: Cho dãy $N$ số nguyên, số nguyên $X$ và vị trí index $K$ ($0 \le K \le N$). Hãy chèn số $X$ vào đúng vị trí $K$ của dãy số và in ra dãy mới gồm $(N + 1)$ phần tử.

**Đầu vào (Input):**

* Dòng 1: Số nguyên $N$.
 * Dòng 2: $N$ số nguyên.
 * Dòng 3: Hai số nguyên $X$ và $K$.

**Đầu ra (Output):**

Dãy số sau khi chèn.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 4 <br> 10 20 30 40 <br> 99 1 | 10 99 20 30 40 |

**Giải thích:**

Với dữ liệu đầu vào là `4
10 20 30 40
99 1`, kết quả thu được tương ứng là `10 99 20 30 40`.



### Bài 14 [pya_l16_p18_mat_khau_bi_an]: Mật khẩu bị ẩn

Bối cảnh: Bo đặt mật khẩu cho nhật ký điện tử của mình bằng một chuỗi gồm chữ cái và chữ số, ví dụ như `Abc123x`. Để kiểm tra độ mạnh, nhỏ muốn biết mật khẩu của mình chứa bao nhiêu ký tự là chữ số. Hãy đếm.

Nhiệm vụ: Cho chuỗi $S$. Hãy đếm xem có bao nhiêu ký tự trong $S$ là chữ số từ `0` đến `9`.

**Đầu vào (Input):**

Một dòng chứa chuỗi $S$ ($1 \le |S| \le 10^5$, gồm chữ cái, chữ số và khoảng trắng).

**Đầu ra (Output):**

In ra một số nguyên duy nhất là số lượng chữ số.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| Abc123x | 3 |

**Giải thích:**

Trong chuỗi `Abc123x` có 3 ký tự là chữ số: `1`, `2` và `3`.



### Bài 15 [pya_l16_p22_xep_hang_chieu_cao]: Xếp hàng chiều cao

Bối cảnh: Giờ thể dục, thầy giáo yêu cầu $N$ người dùng xếp thành một hàng từ thấp đến cao để tập đội hình đội ngũ. Thầy đọc chiều cao của từng bạn và nhờ Na xếp lại giúp. Hãy in ra chiều cao của các bạn theo thứ tự tăng dần.

Nhiệm vụ: Cho chiều cao của $N$ bạn. Hãy in ra chiều cao theo thứ tự tăng dần, cách nhau bởi một dấu cách.

**Đầu vào (Input):**

Dòng 1: số nguyên $N$ ($1 \le N \le 10^5$). Dòng 2: $N$ số nguyên là chiều cao ($100 \le A_i \le 200$).

**Đầu ra (Output):**

In ra $N$ số theo thứ tự tăng dần trên một dòng.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 5 <br> 160 150 175 165 155 | 150 155 160 165 175 |

**Giải thích:**

Sắp xếp 5 chiều cao từ thấp đến cao được dãy 150 155 160 165 175.



### Bài 16 [pya_l16_p10_xoa_phan_tu_dau_tien_bang_x]: Xóa phần tử đầu tiên bằng X

Bối cảnh: Xóa phần tử đầu tiên thỏa mãn điều kiện là thao tác cơ bản trong quản lý danh sách đợi và cập nhật trạng thái dữ liệu.

Nhiệm vụ: Cho dãy $N$ số nguyên và số $X$. Nếu $X$ có trong dãy, hãy xóa phần tử đầu tiên có giá trị bằng $X$ và in ra dãy số còn lại. Nếu $X$ không có trong dãy, in ra `KHONG CO`.

**Đầu vào (Input):**

* Dòng 1: Hai số $N, X$.
 * Dòng 2: $N$ số nguyên.

**Đầu ra (Output):**

Dãy số sau khi xóa, hoặc `KHONG CO`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 5 3 <br> 1 3 5 3 7 | 1 5 3 7 |

**Giải thích:**

Với dữ liệu đầu vào là `5 3
1 3 5 3 7`, kết quả thu được tương ứng là `1 5 3 7`.



### Bài 17 [pya_l16_p13_xoay_vong_danh_sach_sang_phai]: Xoay vòng danh sách sang phải

Bối cảnh: Các người dùng lớp 3A đang chơi trò đoàn tàu, mỗi bạn cầm một tấm thẻ số và nối đuôi nhau thành một hàng dài. Cô giáo hô hiệu lệnh "xoay phải $K$ vị trí", nghĩa là cả lớp sẽ nhấc $K$ phần tử cuối cùng của mảng đem gắn lên đầu mảng. Các người dùng xoay xong thì rối hết cả hàng mà vẫn cười khúc khích. Hãy giúp cả lớp tìm xem sau trò chơi, hàng thẻ số sẽ trông như thế nào.

Nhiệm vụ: Cho dãy $N$ số nguyên và số $K$ ($1 \le K \le N \le 10^5$). Hãy in ra dãy số sau khi xoay phải $K$ vị trí.

**Đầu vào (Input):**

* Dòng 1: Hai số $N$ và $K$.
 * Dòng 2: $N$ số nguyên.

**Đầu ra (Output):**

Dãy số sau khi xoay phải.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 5 2 <br> 1 2 3 4 5 | 4 5 1 2 3 |

**Giải thích:**

Hai phần tử cuối là 4, 5 được đưa lên đầu.



### Bài 18 [pya_l16_p09_tach_mang_chan_va_mang_le]: Tách mảng chẵn và mảng lẻ

Bối cảnh: Tách một mảng tổng hợp thành hai luồng số chẵn và số lẻ độc lập giúp tối ưu hóa việc phân luồng xử lý dữ liệu chuyên biệt.

Nhiệm vụ: Cho dãy $N$ số nguyên. Hãy tách dãy thành 2 danh sách: một danh sách gồm các số chẵn, một danh sách gồm các số lẻ (giữ nguyên thứ tự xuất hiện ban đầu).

**Đầu vào (Input):**

* Dòng 1: Số nguyên $N$ ($1 \le N \le 10^5$).
 * Dòng 2: $N$ số nguyên.

**Đầu ra (Output):**

* Dòng 1: Các số chẵn (cách nhau bởi khoảng trắng).
 * Dòng 2: Các số lẻ (cách nhau bởi khoảng trắng).

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 6 <br> 1 4 7 8 2 9 | 4 8 2 <br> 1 7 9 |

**Giải thích:**

Với dữ liệu đầu vào là `6
1 4 7 8 2 9`, kết quả thu được tương ứng là `4 8 2
1 7 9`.



### Bài 19 [pya_l16_p24_dem_tu_dai]: Đếm từ dài

Bối cảnh: Cô giáo ra trò chơi: cho một câu văn và một số $K$, bạn nào đếm đúng có bao nhiêu từ dài hơn $K$ ký tự sẽ được điểm 10. Từ là một nhóm ký tự liền nhau, các từ cách nhau bởi dấu cách. Na nhờ em đếm giúp để chắc chắn được điểm 10.

Nhiệm vụ: Cho số $K$ và câu văn $S$. Hãy đếm số từ có độ dài lớn hơn $K$.

**Đầu vào (Input):**

Dòng 1: số nguyên $K$ ($0 \le K \le 100$). Dòng 2: câu văn $S$ ($1 \le |S| \le 10^4$).

**Đầu ra (Output):**

In ra một số nguyên duy nhất là số từ thỏa mãn.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 3 <br> Hom nay Bin di hoc cung ban Na | 1 |

**Giải thích:**

Các từ là: Hom, nay, Bin, di, hoc, cung, ban, Na. Chỉ có từ `cung` dài 4 ký tự, lớn hơn 3 nên đáp án là 1.



### Bài 20 [pya_l16_p17_bang_diem_lop_hoc]: Bảng điểm lớp học

Bối cảnh: Cuối tuần, cô giáo muốn tổng kết điểm thi đua của cả lớp. Cả lớp có $N$ bạn, mỗi bạn có một điểm số là số nguyên từ 0 đến 10. Cô nhờ Na tìm giúp điểm cao nhất, điểm thấp nhất và điểm trung bình của cả lớp để ghi vào sổ thi đua.

Nhiệm vụ: Cho điểm của $N$ bạn. Hãy in ra điểm cao nhất, điểm thấp nhất và điểm trung bình (lấy 1 chữ số thập phân).

**Đầu vào (Input):**

Dòng 1: số nguyên $N$ ($1 \le N \le 10^5$). Dòng 2: $N$ số nguyên là điểm của các bạn ($0 \le A_i \le 10$).

**Đầu ra (Output):**

In ra 3 dòng: dòng 1 là điểm cao nhất, dòng 2 là điểm thấp nhất, dòng 3 là điểm trung bình với đúng 1 chữ số thập phân.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 5 <br> 8 7 10 6 9 | 10 <br> 6 <br> 8.0 |

**Giải thích:**

Điểm cao nhất là 10, thấp nhất là 6. Trung bình là $(8 + 7 + 10 + 6 + 9) / 5 = 8.0$.



### Bài 21 [pya_l16_p14_cap_so_co_tong_bang_s]: Cặp số có tổng bằng S

Bối cảnh: Trong bài kiểm tra, người dùng cần tính nhanh tổng một dãy số. Hãy viết chương trình hỗ trợ tính toán.

Nhiệm vụ: Cho dãy gồm $N$ số nguyên đôi một khác nhau và một số nguyên mục tiêu $S$. Hãy đếm xem có bao nhiêu cặp chỉ số $(i, j)$ với $i < j$ thỏa mãn:
 $$A_i + A_j = S$$

**Đầu vào (Input):**

* Dòng 1: Hai số nguyên $N$ và $S$ ($1 \le N \le 10^4, |S| \le 10^9$).
 * Dòng 2: $N$ số nguyên.

**Đầu ra (Output):**

Số lượng cặp thỏa mãn.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 5 10 <br> 2 4 6 8 3 | 2 |

**Giải thích:**

Có 2 cặp là $(2, 8)$ và $(4, 6)$.



### Bài 22 [pya_l16_p16_ve_so_may_man]: Vé số may mắn

Bối cảnh: Hội chợ trường em tổ chức trò chơi quay số trúng thưởng. Mỗi người dùng được phát một tấm vé in một số tự nhiên $N$. Ban tổ chức gọi đó là vé may mắn nếu tổng các chữ số của $N$ chia hết cho $7$. Một khối hộp cầm vé số $1234$ trên tay, hồi hộp không biết mình có trúng thưởng không.

Nhiệm vụ: Hãy kiểm tra xem tấm vé số $N$ có phải là vé may mắn không. In `YES` nếu đúng, ngược lại in `NO`.

**Đầu vào (Input):**

Một số tự nhiên $N$ ($1 \le N \le 10^{18}$).

**Đầu ra (Output):**

In ra `YES` hoặc `NO`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 1234 | NO |

**Giải thích:**

Tổng các chữ số là $1 + 2 + 3 + 4 = 10$. Vì 10 không chia hết cho 7 nên đáp án là `NO`. (Ví dụ vé số $16$ có tổng là 7 nên đáp án là `YES`.)



### Bài 23 [pya_l16_p26_chuyen_tau_vuot_deo]: Chuyến tàu vượt đèo

Bối cảnh: Một đoàn tàu đồ chơi chạy qua $N$ ngọn đèo, ngọn thứ $i$ cao $A_i$ mét. Học sinh lái tàu reo lên mỗi khi tàu chinh phục một ngọn đèo cao hơn tất cả các ngọn đèo đã đi qua trước đó (ngọn đầu tiên luôn được reo một lần). Hãy đếm xem nhỏ reo lên tất cả bao nhiêu lần.

Nhiệm vụ: Cho dãy $N$ số. Hãy đếm số lần phần tử lớn hơn tất cả các phần tử đứng trước nó.

**Đầu vào (Input):**

Dòng 1: số nguyên $N$ ($1 \le N \le 10^5$). Dòng 2: $N$ số nguyên ($|A_i| \le 10^9$).

**Đầu ra (Output):**

In ra một số nguyên duy nhất là số lần reo.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 6 <br> 1 3 5 2 4 7 | 4 |

**Giải thích:**

Các kỷ lục mới là 1, 3, 5 rồi 7, tổng cộng 4 lần reo.



### Bài 24 [pya_l16_p20_tong_chu_so_lon_nhat]: Tổng chữ số lớn nhất

Bối cảnh: Trong giờ ra chơi, các bạn thi nhau khoe số báo danh của mình. Bạn nào có tổng các chữ số lớn nhất sẽ được làm lớp trưởng ngày mai. Có $N$ bạn tham gia, mỗi bạn có một số báo danh. Nếu hai bạn có tổng chữ số bằng nhau thì bạn có số báo danh nhỏ hơn sẽ thắng.

Nhiệm vụ: Hãy tìm số báo danh của bạn thắng cuộc.

**Đầu vào (Input):**

Dòng 1: số nguyên $N$ ($1 \le N \le 10^5$). Dòng 2: $N$ số tự nhiên ($0 \le A_i \le 10^{18}$).

**Đầu ra (Output):**

In ra số báo danh thắng cuộc.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 5 <br> 12 99 45 100 38 | 99 |

**Giải thích:**

Tổng chữ số của 12 là 3, của 99 là 18, của 45 là 9, của 100 là 1, của 38 là 11. Tổng lớn nhất là 18 của số 99.



### Bài 25 [pya_l16_p19_dem_keo_chan_le]: Đếm kẹo chẵn lẻ

Bối cảnh: Liên hoan cuối năm, cô giáo mua $N$ gói kẹo, mỗi gói có $A_i$ viên kẹo. Cô muốn chia các gói kẹo thành hai mâm: mâm gói chẵn (số kẹo là số chẵn) và mâm gói lẻ (số kẹo là số lẻ). Hãy giúp cô đếm xem mỗi mâm có bao nhiêu gói.

Nhiệm vụ: Cho $N$ số nguyên. Hãy đếm số lượng số chẵn và số lượng số lẻ, in trên một dòng.

**Đầu vào (Input):**

Dòng 1: số nguyên $N$ ($1 \le N \le 10^5$). Dòng 2: $N$ số nguyên ($0 \le A_i \le 10^9$).

**Đầu ra (Output):**

In ra hai số trên một dòng: số lượng số chẵn trước, số lượng số lẻ sau.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 6 <br> 1 2 3 4 5 6 | 3 3 |

**Giải thích:**

Các số chẵn là 2, 4, 6 (3 gói). Các số lẻ là 1, 3, 5 (3 gói).



### Bài 26 [pya_l16_p25_dem_sao_nguyen_to]: Đếm sao nguyên tố

Bối cảnh: Đêm hội trăng rằm, các người dùng dán lên bầu trời giấy $N$ ngôi sao được đánh số từ 1 đến $N$. Thầy giáo đố: có bao nhiêu ngôi sao mang số nguyên tố (số chỉ chia hết cho 1 và chính nó, số 1 không phải số nguyên tố)? Bạn nào đếm đúng sẽ được rước đèn đầu tiên.

Nhiệm vụ: Cho số $N$. Hãy đếm có bao nhiêu số nguyên tố từ 1 đến $N$.

**Đầu vào (Input):**

Một số nguyên $N$ ($1 \le N \le 10^6$).

**Đầu ra (Output):**

In ra một số nguyên duy nhất là số lượng số nguyên tố.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 10 | 4 |

**Giải thích:**

Từ 1 đến 10 có 4 số nguyên tố là 2, 3, 5 và 7.



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


## Bài tập thực hành


### Bài 01 [pya_l17_p01_diem_so_cao_nhat_thap_nhat]: Điểm số cao nhất & thấp nhất

Bối cảnh: Xác định giá trị cực đại và cực tiểu trong tập số liệu điểm số là chỉ số đánh giá tổng quan phổ điểm của một đợt khảo sát.

Nhiệm vụ: Cho danh sách điểm thi của $N$ bạn học sinh. Hãy in ra điểm số cao nhất và điểm số thấp nhất trong danh sách.

**Đầu vào (Input):**

* Dòng 1: Số nguyên $N$ ($1 \le N \le 1000$).
 * Dòng 2: $N$ số nguyên là điểm của các bạn ($0 \le A_i \le 100$).

**Đầu ra (Output):**

Điểm cao nhất, theo sau là điểm thấp nhất.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 5 <br> 80 95 60 100 75 | 100 60 |

**Giải thích:**

Với dữ liệu đầu vào là `5
80 95 60 100 75`, kết quả thu được tương ứng là `100 60`.



### Bài 02 [pya_l17_p07_loc_bo_cac_so_trung_lap]: Lọc bỏ các số trùng lặp

Bối cảnh: Loại bỏ các phần tử trùng lặp và sắp xếp lại tập hợp là bước tiền xử lý quan trọng trong làm sạch dữ liệu.

Nhiệm vụ: Cho dãy gồm $N$ số nguyên có thể chứa nhiều số bị trùng lặp. Hãy lọc bỏ các phần tử trùng lặp và in ra các số độc nhất theo thứ tự tăng dần.

**Đầu vào (Input):**

* Dòng 1: Số nguyên $N$ ($1 \le N \le 10^5$).
 * Dòng 2: $N$ số nguyên.

**Đầu ra (Output):**

Các số độc nhất sắp xếp tăng dần trên một dòng.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 7 <br> 3 1 4 1 5 9 2 | 1 2 3 4 5 9 |

**Giải thích:**

Với dữ liệu đầu vào là `7
3 1 4 1 5 9 2`, kết quả thu được tương ứng là `1 2 3 4 5 9`.



### Bài 03 [pya_l17_p09_sap_xep_ten_theo_thu_tu_bang_chu_cai]: Sắp xếp tên theo thứ tự bảng chữ cái

Bối cảnh: Cô giáo cần sắp xếp lại danh sách điểm số của học sinh theo thứ tự. Hãy viết chương trình sắp xếp.

Nhiệm vụ: Cho danh sách gồm $N$ từ tiếng Anh. Hãy sắp xếp danh sách từ theo thứ tự từ điển A-Z (tăng dần).

**Đầu vào (Input):**

* Dòng 1: Số nguyên $N$ ($1 \le N \le 1000$).
 * Dòng 2: $N$ từ viết thường cách nhau bởi khoảng trắng.

**Đầu ra (Output):**

Danh sách từ sau khi sắp xếp trên một dòng.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 4 <br> orange apple banana grape | apple banana grape orange |

**Giải thích:**

Với dữ liệu đầu vào là `4
orange apple banana grape`, kết quả thu được tương ứng là `apple banana grape orange`.



### Bài 04 [pya_l17_p13_ghep_hai_day_da_sap_xep]: Ghép hai dãy đã sắp xếp

Bối cảnh: Cô giáo cần sắp xếp lại danh sách điểm số của học sinh theo thứ tự. Hãy viết chương trình sắp xếp.

Nhiệm vụ: Cho hai dãy số nguyên $A$ (gồm $N$ phần tử) và $B$ (gồm $M$ phần tử) đều đã được sắp xếp tăng dần. Hãy ghép hai dãy lại thành một dãy duy nhất gồm $(N + M)$ phần tử cũng được sắp xếp tăng dần.

**Đầu vào (Input):**

* Dòng 1: Hai số $N$ và $M$ ($1 \le N, M \le 10^5$).
 * Dòng 2: $N$ số nguyên của dãy $A$.
 * Dòng 3: $M$ số nguyên của dãy $B$.

**Đầu ra (Output):**

Dãy hợp nhất gồm $(N + M)$ phần tử tăng dần trên một dòng.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 3 4 <br> 1 4 7 <br> 2 3 5 8 | 1 2 3 4 5 7 8 |

**Giải thích:**

Với dữ liệu đầu vào là `3 4
1 4 7
2 3 5 8`, kết quả thu được tương ứng là `1 2 3 4 5 7 8`.



### Bài 05 [pya_l17_p06_dem_so_luong_hoc_sinh_tren_diem_trung_binh]: Đếm số lượng học sinh trên điểm trung bình

Bối cảnh: So sánh từng phần tử với giá trị trung bình của cả tập hợp giúp đánh giá độ phân tán và chất lượng của các chỉ số thành phần.

Nhiệm vụ: Cho điểm thi của $N$ học sinh. Hãy đếm xem có bao nhiêu bạn học sinh có điểm số lớn hơn hoặc bằng điểm trung bình cộng của cả lớp.

**Đầu vào (Input):**

* Dòng 1: Số nguyên $N$ ($1 \le N \le 10^5$).
 * Dòng 2: $N$ số thực.

**Đầu ra (Output):**

Số lượng học sinh đạt điểm $\ge$ điểm trung bình.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 4 <br> 8 6 10 4 | 2 |

**Giải thích:**

Điểm TB: $(8+6+10+4)/4 = 7.0$. Các bạn có điểm $\ge 7$ là 8 và 10 (có 2 bạn).



### Bài 06 [pya_l17_p02_sap_xep_tang_dan_don_gian]: Sắp xếp tăng dần đơn giản

Bối cảnh: Cô giáo cần sắp xếp lại danh sách điểm số của học sinh theo thứ tự. Yêu cầu sắp xếp dãy số tăng dần để phục vụ thống kê và tra cứu.

Nhiệm vụ: Cho dãy $N$ số nguyên. Hãy sắp xếp dãy số theo thứ tự tăng dần và in ra màn hình trên một dòng.

**Đầu vào (Input):**

* Dòng 1: Số nguyên $N$ ($1 \le N \le 1000$).
 * Dòng 2: $N$ số nguyên.

**Đầu ra (Output):**

Dãy số sau khi sắp xếp tăng dần, cách nhau bởi khoảng trắng.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 5 <br> 9 2 7 1 5 | 1 2 5 7 9 |

**Giải thích:**

Với dữ liệu đầu vào là `5
9 2 7 1 5`, kết quả thu được tương ứng là `1 2 5 7 9`.



### Bài 07 [pya_l17_p04_sap_xep_giam_dan_bang_xep_hang]: Sắp xếp giảm dần bảng xếp hạng

Bối cảnh: Cô giáo cần sắp xếp lại danh sách điểm số của học sinh theo thứ tự. Hãy viết chương trình sắp xếp.

Nhiệm vụ: Cho danh sách điểm số của $N$ thí sinh tham gia cuộc thi. Hãy sắp xếp bảng điểm theo thứ tự từ cao xuống thấp (giảm dần) để trao giải.

**Đầu vào (Input):**

* Dòng 1: Số nguyên $N$ ($1 \le N \le 10^5$).
 * Dòng 2: $N$ số nguyên.

**Đầu ra (Output):**

Bảng điểm sắp xếp giảm dần trên một dòng.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 5 <br> 20 80 40 100 60 | 100 80 60 40 20 |

**Giải thích:**

Với dữ liệu đầu vào là `5
20 80 40 100 60`, kết quả thu được tương ứng là `100 80 60 40 20`.



### Bài 08 [pya_l17_p11_trung_vi_cua_day_so_median]: Trung vị của dãy số (Median)

Bối cảnh: Giờ ra chơi, các người dùng xếp thành một hàng dọc gồm $N$ bạn, trong đó $N$ là số lẻ. Cô giáo muốn tìm bạn đứng chính giữa sau khi cả hàng đã xếp theo chiều cao tăng dần, và bạn đó được gọi là trung vị của dãy: tức là phần tử nằm chính giữa sau khi dãy đã được sắp xếp tăng dần. Các bạn cứ nhốn nháo đổi chỗ mãi không xong. Hãy giúp cô tìm ra bạn đứng ở vị trí chính giữa.

Nhiệm vụ: Cho dãy $N$ số nguyên ($N$ lẻ). Hãy tìm số trung vị của dãy số.

**Đầu vào (Input):**

* Dòng 1: Số nguyên lẻ $N$ ($1 \le N \le 10^5$).
 * Dòng 2: $N$ số nguyên.

**Đầu ra (Output):**

Giá trị trung vị.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 5 <br> 10 2 8 4 6 | 6 |

**Giải thích:**

Sắp xếp: [2, 4, 6, 8, 10]. Số chính giữa là 6.



### Bài 09 [pya_l17_p05_tim_so_lon_thu_nhi_trong_mang]: Tìm số lớn thứ nhì trong mảng

Bối cảnh: Thí sinh đang tìm kiếm một giá trị đặc biệt trong tập dữ liệu. Hãy viết chương trình tìm kiếm hiệu quả.

Nhiệm vụ: Cho dãy $N$ số nguyên. Hãy tìm giá trị lớn thứ nhì trong dãy số (nghĩa là giá trị lớn nhất trong số các phần tử nhỏ hơn giá trị cực đại). Nếu tất cả các phần tử trong mảng đều bằng nhau, in ra `KHONG CO`.

**Đầu vào (Input):**

* Dòng 1: Số nguyên $N$ ($2 \le N \le 10^5$).
 * Dòng 2: $N$ số nguyên.

**Đầu ra (Output):**

Giá trị lớn thứ nhì, hoặc `KHONG CO`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 5 <br> 10 20 20 15 5 | 15 |

**Giải thích:**

Số lớn nhất là 20. Số lớn thứ hai nhỏ hơn 20 là 15.

**Ví dụ mẫu (Sample 2):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 3 <br> 5 5 5 | KHONG CO |

**Giải thích:**

Tất cả bằng nhau.



### Bài 10 [pya_l17_p03_diem_trung_binh_mon_hoc]: Điểm trung bình môn học

Bối cảnh: Tính trung bình cộng của một tập hợp giá trị đo lường là phép toán thống kê cơ bản nhất trong xử lý số liệu thực nghiệm.

Nhiệm vụ: Cho danh sách điểm kiểm tra của $N$ bài thi. Hãy tính điểm trung bình cộng của các bài thi và in ra với đúng 2 chữ số sau dấu phẩy.

**Đầu vào (Input):**

* Dòng 1: Số nguyên $N$ ($1 \le N \le 1000$).
 * Dòng 2: $N$ số thực hoặc số nguyên là điểm các bài thi.

**Đầu ra (Output):**

Điểm trung bình cộng (định dạng `f"{tb:.2f}"`).

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 4 <br> 8 9 7 10 | 8.50 |

**Giải thích:**

$(8 + 9 + 7 + 10) / 4 = 8.5$.



### Bài 11 [pya_l17_p10_chenh_lech_nho_nhat_giua_hai_so]: Chênh lệch nhỏ nhất giữa hai số

Bối cảnh: Thí sinh cần tìm giá trị lớn nhất hoặc nhỏ nhất trong một tập dữ liệu. Hãy viết chương trình tìm kiếm.

Nhiệm vụ: Cho dãy $N$ số nguyên đôi một khác nhau. Hãy tìm độ chênh lệch nhỏ nhất giữa 2 phần tử bất kỳ trong dãy (tức là giá trị $|A_i - A_j|$ nhỏ nhất với $i \ne j$).

**Đầu vào (Input):**

* Dòng 1: Số nguyên $N$ ($2 \le N \le 10^5$).
 * Dòng 2: $N$ số nguyên.

**Đầu ra (Output):**

Độ chênh lệch nhỏ nhất.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 4 <br> 10 1 8 15 | 2 |

**Giải thích:**

Sắp xếp: [1, 8, 10, 15]. Chênh lệch giữa 8 và 10 là $



### Bài 12 [pya_l17_p12_so_xuat_hien_nhieu_lan_nhat_mode]: Số xuất hiện nhiều lần nhất (Mode)

Bối cảnh: Tìm giá trị có tần số xuất hiện cao nhất (giá trị mốt - mode) là bài toán thống kê đặc trưng để nhận diện xu hướng dữ liệu phổ biến nhất.

Nhiệm vụ: Cho dãy $N$ số nguyên. Hãy tìm số xuất hiện nhiều lần nhất trong dãy. Nếu có nhiều số có cùng số lần xuất hiện nhiều nhất, hãy in ra số có giá trị nhỏ nhất trong các số đó.

**Đầu vào (Input):**

* Dòng 1: Số nguyên $N$ ($1 \le N \le 10^5$).
 * Dòng 2: $N$ số nguyên.

**Đầu ra (Output):**

Số xuất hiện nhiều nhất.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 7 <br> 2 3 5 2 3 7 2 | 2 |

**Giải thích:**

Với dữ liệu đầu vào là `7
2 3 5 2 3 7 2`, kết quả thu được tương ứng là `2`.



### Bài 13 [pya_l17_p08_diem_olympic_bo_max_bo_min]: Điểm olympic bỏ max bỏ min

Bối cảnh: Cuối tuần này, trường em tổ chức hội thi Bơi lội Olympic thật vui nhộn. Có $N$ giám khảo cùng ngồi chấm điểm cho mỗi người dùng ($N \ge 3$). Để cho thật công bằng, điểm số chính thức của vận động viên sẽ là trung bình cộng sau khi đã **bỏ đi một điểm cao nhất và một điểm thấp nhất**. Trọng tài đang lúng túng với đống bảng điểm nên hãy bác ấy tính điểm thật chính xác.

Nhiệm vụ: Cho $N$ điểm số. Hãy tính điểm chính thức của vận động viên (làm tròn 2 chữ số thập phân).

**Đầu vào (Input):**

* Dòng 1: Số nguyên $N$ ($3 \le N \le 1000$).
 * Dòng 2: $N$ số thực cách nhau bởi khoảng trắng.

**Đầu ra (Output):**

Điểm trung bình sau khi loại bỏ 1 điểm max và 1 điểm min.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 5 <br> 7.0 9.0 8.0 10.0 6.0 | 8.00 |

**Giải thích:**

Bỏ min là 6.0, bỏ max là 10.0. Còn lại: 7.0, 8.0, 9.0. Trung bình là 8.00.



### Bài 14 [pya_l17_p14_xep_hang_mua_tra_sua_greedy]: Xếp hàng mua trà sữa (Greedy)

Bối cảnh: Giờ tan học, có $N$ bạn học sinh cùng ríu rít xếp hàng mua trà sữa ở căng tin trường. Bạn thứ $i$ cần $T_i$ phút để người bán hàng pha chế xong cốc trà sữa của mình. Tổng thời gian chờ đợi của tất cả các bạn sẽ là tổng thời gian mà mỗi bạn phải đứng xếp hàng chờ cho đến khi nhận được trà sữa. Nhìn hàng dài mà các bạn ai cũng mỏi chân, hãy cô bán hàng tìm cách xếp hàng sao cho mọi người chờ ít nhất.

Nhiệm vụ: Hãy tìm cách sắp xếp thứ tự các bạn vào mua trà sữa sao cho **tổng thời gian chờ đợi của tất cả các bạn là NHỎ NHẤT CÓ THỂ**. Hãy in ra tổng thời gian chờ đợi nhỏ nhất đó.

**Đầu vào (Input):**

* Dòng 1: Số nguyên $N$ ($1 \le N \le 10^5$).
 * Dòng 2: $N$ số nguyên $T_i$ ($1 \le T_i \le 1000$).

**Đầu ra (Output):**

Một số nguyên duy nhất là tổng thời gian chờ đợi nhỏ nhất.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 3 <br> 3 1 2 | 10 |

**Giải thích:**

Sắp xếp người làm nhanh lên trước: thời gian làm lần lượt là 1, 2, 3.
- Bạn 1 chờ 1 phút.
- Bạn 2 chờ $1 + 2 = 3$ phút.
- Bạn 3 chờ $1 + 2 + 3 = 6$ phút.
Tổng thời gian chờ: $1 + 3 + 6 = 10$ phút (tối ưu nhất).



# CHƯƠNG 05: XỬ LÝ CHUỖI KÝ TỰ


# Bài 13: Chuỗi ký tự — Chỉ số, cắt lát và duyệt ký tự

## 1. Bản chất khoa học máy tính: Chuỗi ký tự trong bộ nhớ RAM

Chuỗi ký tự (`str`) là một **dãy các ký tự xếp liền nhau theo thứ tự** trong bộ nhớ. Mỗi ký tự có một vị trí cố định gọi là **chỉ số (index)**. Python dùng hai chiều chỉ số rất thuận tiện:
* **Chỉ số dương:** Bắt đầu từ $0$ ở ký tự đầu bên trái, tăng dần đến $\text{len}(s) - 1$ ở ký tự cuối.
* **Chỉ số âm:** Bắt đầu từ $-1$ ở ký tự cuối bên phải, giảm dần về $-\text{len}(s)$ ở ký tự đầu.



![](/Users/vu/Developer/ikhEdu_lessons/courses/python-bang-a/assets_png/l13_string_indexing.png)



### Bảng tra cứu chỉ số chuỗi với ví dụ `s = "PYTHON"`:

| Chiều duyệt | Ký tự 1 | Ký tự 2 | Ký tự 3 | Ký tự 4 | Ký tự 5 | Ký tự 6 |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
| **Ký tự thực tế** | `'P'` | `'Y'` | `'T'` | `'H'` | `'O'` | `'N'` |
| **Chỉ số dương (Từ trái sang phải)** | `0` | `1` | `2` | `3` | `4` | `5` |
| **Chỉ số âm (Từ phải sang trái)** | `-6` | `-5` | `-4` | `-3` | `-2` | `-1` |

### Các cú pháp truy cập cơ bản:

```python
s = "PYTHON"

print(s[0])     # In ra: 'P'  (Ký tự đầu tiên)
print(s[5])     # In ra: 'N'  (Ký tự cuối cùng: index = len(s) - 1)
print(s[-1])    # In ra: 'N'  (Ký tự cuối cùng dùng chỉ số âm)
print(s[-2])    # In ra: 'O'  (Ký tự áp chót)
print(len(s))   # In ra: 6    (Độ dài chuỗi - tổng số lượng ký tự)
```

> **Điều bắt buộc phải nhớ: Lỗi vượt quá chỉ số (`IndexError`)**
> * Nếu chuỗi có độ dài $N = \text{len}(s)$, chỉ số dương hợp lệ chỉ nằm trong đoạn $[0, N - 1]$.
> * Truy cập vào `s[N]` hoặc `s[len(s)]` sẽ khiến chương trình dừng đột ngột với lỗi: `IndexError: string index out of range`.
> * Với chuỗi rỗng `s = ""`, độ dài bằng 0, mọi thao tác truy cập `s[0]` đều gây lỗi ngay.

---

## 2. Kỹ thuật cắt lát chuỗi — Trích xuất chuỗi con

Cắt lát giúp lấy ra một đoạn ký tự liên tiếp hoặc cách quãng từ chuỗi ban đầu để tạo chuỗi con mới.

### Cú pháp tổng quát:
$$\mathbf{s[\text{start} : \text{stop} : \text{step}]}$$

* `start`: Vị trí bắt đầu lấy (mặc định là $0$ nếu để trống).
* `stop`: Vị trí kết thúc (nhưng **luôn bị loại trừ**, chỉ lấy đến $\text{stop} - 1$).
* `step`: Bước nhảy (mặc định là $1$). Bước nhảy âm nghĩa là đi lùi.

### Bảng các mẫu cắt lát kinh điển khi làm bài:

| Cú pháp cắt lát | Quy tắc trích xuất | Ví dụ với `s = "ABCDEFGH"` | Chuỗi con kết quả |
|---|---|---|:---:|
| `s[2:5]` | Lấy từ vị trí $2$ đến vị trí $4$ | `s[2:5]` | `"CDE"` |
| `s[:4]` | Bỏ trống `start`: Lấy từ đầu đến vị trí $3$ | `s[:4]` | `"ABCD"` |
| `s[3:]` | Bỏ trống `stop`: Lấy từ vị trí $3$ đến hết chuỗi | `s[3:]` | `"DEFGH"` |
| `s[::2]` | Lấy từ đầu đến cuối với bước nhảy $2$ | `s[::2]` | `"ACEG"` |
| `s[1::2]` | Lấy từ vị trí $1$ với bước nhảy $2$ (vị trí lẻ) | `s[1::2]` | `"BDFH"` |
| `s[::-1]` | **Bí thuật đảo ngược chuỗi**: Bước nhảy $-1$ | `s[::-1]` | `"HGFEDCBA"` |

```python
s = "iKHEDU2026"

print(s[0:6])   # "iKHEDU" (Lấy 6 ký tự đầu tiên)
print(s[:6])    # "iKHEDU" (Cách viết gọn tương đương)
print(s[6:])    # "2026"   (Lấy từ vị trí thứ 6 đến hết)
print(s[::-1])  # "6202UDEHKi" (Đảo ngược toàn bộ chuỗi)
```

> 💡 **Quy tắc khoảng bán mở $[start, stop)$:**
> Quy tắc cận trên `stop` bị loại trừ dùng chung cho `range(start, stop)` và `s[start:stop]`. Số ký tự lấy ra khi `step = 1` luôn bằng: $\text{stop} - \text{start}$.

---

## 3. Đặc tính bất biến của chuỗi ký tự

Đây là điểm khác nhau quan trọng nhất giữa chuỗi (`str`) và danh sách (`list`):

* **Chuỗi trong Python là bất biến:** Khi chuỗi đã có trong bộ nhớ, ta **không thể sửa hay gán đè trực tiếp** từng ký tự của nó.

```python
s = "HELLO"

# Cố gắng sửa chữ 'H' thành chữ 'J':
# s[0] = "J"
# Báo lỗi nghiêm trọng: TypeError: 'str' object does not support item assignment
```

### Cách xử lý chuẩn xác khi muốn thay đổi ký tự trong chuỗi:
Ta phải **tạo một chuỗi hoàn toàn mới** bằng phép ghép (`+`) hoặc cắt lát:

```python
s = "HELLO"

# ĐÚNG: Ghép ký tự mới với phần đuôi còn lại của chuỗi
s = "J" + s[1:]
print(s)  # In ra: "JELLO"
```

---

## 4. Các phương thức duyệt chuỗi bằng vòng lặp

Duyệt chuỗi là đi thăm từng ký tự để kiểm tra, đếm hoặc tính toán.

### 4.1. Duyệt trực tiếp từng ký tự bằng `for ... in`
Dùng khi chỉ cần quan tâm giá trị từng ký tự, không cần biết vị trí:

```python
s = input()
for ch in s:
    print(ch)
```

### 4.2. Duyệt qua chỉ số bằng `for i in range(len(s))`
Dùng khi cần dựa vào vị trí, ví dụ: xét ký tự cạnh nhau, hoặc chỉ xét vị trí chẵn/lẻ:

```python
s = input()
for i in range(len(s)):
    # s[i] là ký tự tại vị trí thứ i
    if i % 2 == 0:
        print(f"Ký tự tại vị trí chẵn {i}: {s[i]}")
```

### 4.3. Duyệt cặp ký tự liền kề
Mẫu kiểm tra hai ký tự giống nhau đứng cạnh nhau:

```python
s = input()
dem_trung = 0
for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        dem_trung += 1
print(dem_trung)
```

---

## 5. Bảng mô phỏng biến thiên ô nhớ

### Thuật toán: Kiểm tra chuỗi có đối xứng hay không bằng hai con trỏ

```python
s = "RADAR"
la_doi_xung = True
n = len(s)

for i in range(n // 2):
    if s[i] != s[n - 1 - i]:
        la_doi_xung = False
        break

if la_doi_xung:
    print("YES")
else:
    print("NO")
```

| Bước | Vòng lặp `i` | So sánh `s[i]` và `s[n - 1 - i]` | Kết quả so sánh | Biến `la_doi_xung` | Trạng thái thực thi |
|:---:|:---:|:---:|:---:|:---:|---|
| Khởi tạo | — | — | — | `True` | $n = 5$, vòng lặp chạy $i \in [0, 1]$ |
| 1 | $i = 0$ | `s[0]` ('R') so với `s[4]` ('R') | `'R' == 'R'` | `True` | Thỏa mãn, tiếp tục vòng lặp |
| 2 | $i = 1$ | `s[1]` ('A') so với `s[3]` ('A') | `'A' == 'A'` | `True` | Thỏa mãn, tiếp tục vòng lặp |
| Kết thúc | — | — | — | `True` | Hết vòng lặp, in ra `YES` |

---

## 6. Lỗi hay gặp và bẫy lỗi kinh điển

> **Lỗi hay gặp 1: Tìm kiếm bằng `find()` trả về `-1`**
> * `s.find(sub)` tìm vị trí đầu tiên của `sub` trong `s`. Nếu không thấy, hàm trả về `-1` (chương trình vẫn chạy tiếp).
> * Nếu viết `if s.find("a"):` sẽ sai! Vì số `-1` được coi là `True` trong biểu thức điều kiện.
> * **Cách viết an toàn:** `if s.find("a") != -1:` hoặc: `if "a" in s:`.

> **Lỗi hay gặp 2: Nhầm lẫn giữa phép nối chuỗi và cộng số**
> * Khi đọc bằng `input()`, nhập số `12` thì ta vẫn nhận được chuỗi `"12"`.
> * `"12" + "34"` cho ra `"1234"` (ghép chuỗi).
> * **Cách viết an toàn:** Đổi sang số nguyên bằng `int()` trước khi tính toán.

> **Lỗi hay gặp 3: Phân biệt chữ hoa và chữ thường trong phép so sánh**
> * Trong Python, `'A' == 'a'` luôn cho `False`.
> * Khi bài yêu cầu không phân biệt hoa thường, em chuẩn hóa về một dạng: `if s1.lower() == s2.lower():`.

---

## 7. Mẫu code thường gặp

### 7.1. Mẫu kiểm tra chuỗi đối xứng
```python
s = input()
if s == s[::-1]:
    print("YES")
else:
    print("NO")
```

### 7.2. Mẫu xóa bỏ ký tự tại vị trí chỉ định $K$
```python
s = input()
k = int(input())
# Trích xuất đoạn trước k và đoạn sau k rồi ghép lại
ket_qua = s[:k] + s[k + 1:]
print(ket_qua)
```

### 7.3. Mẫu đếm số lần xuất hiện của một ký tự bằng vòng lặp
```python
s = input()
ky_tu_can_tim = input()
dem = 0

for ch in s:
    if ch == ky_tu_can_tim:
        dem += 1

print(dem)
```


## Bài tập thực hành


### Bài 01 [pya_l13_p02_do_dai_cua_chuoi]: Độ dài của chuỗi

Bối cảnh: Độ dài chuỗi ký tự là thông số cơ bản nhất để kiểm soát giới hạn bộ đệm và tính hợp lệ của dữ liệu chuỗi đầu vào.

Nhiệm vụ: Nhập một dòng văn bản $S$ từ bàn phím. Hãy đếm và in ra xem chuỗi $S$ có bao nhiêu ký tự (tính cả các ký tự khoảng trắng nếu có).

**Đầu vào (Input):**

Một chuỗi ký tự $S$.

**Đầu ra (Output):**

Một số nguyên là độ dài chuỗi.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| Python | 6 |

**Giải thích:**

Với dữ liệu đầu vào là `Python`, kết quả thu được tương ứng là `6`.



### Bài 02 [pya_l13_p03_cat_ba_ky_tu_dau_tien]: Cắt ba ký tự đầu tiên

Bối cảnh: Trong các hệ thống phân loại mã bưu chính hoặc mã vùng, ba ký tự đầu tiên thường đại diện cho mã quốc gia hoặc mã tiền tố phân luồng.

Nhiệm vụ: Nhập vào một chuỗi $S$ có ít nhất 3 ký tự. Hãy in ra 3 ký tự đầu tiên của chuỗi đó.

**Đầu vào (Input):**

Một chuỗi $S$ ($3 \le |S| \le 100$).

**Đầu ra (Output):**

3 ký tự đầu tiên.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| VIETNAM | VIE |

**Giải thích:**

Với dữ liệu đầu vào là `VIETNAM`, kết quả thu được tương ứng là `VIE`.



### Bài 03 [pya_l13_p04_dao_nguoc_ten_rieng]: Đảo ngược tên riêng

Bối cảnh: Bạn Bo có một cuốn sổ để viết tên của mình và các bạn trong lớp. Một hôm, Bo nghĩ ra trò đọc ngược tên để tạo biệt danh bí mật cho vui. Cả lớp cười vang khi nghe tên mình bị đọc ngược lại thật ngộ nghĩnh. Hãy viết chương trình đọc ngược mọi cái tên.

Nhiệm vụ: Nhập một chuỗi ký tự $S$. Hãy in ra chuỗi đảo ngược của $S$.

**Đầu vào (Input):**

Một chuỗi ký tự $S$.

**Đầu ra (Output):**

Chuỗi $S$ sau khi đảo ngược.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| DORAEMON | NOMEAROD |

**Giải thích:**

Với dữ liệu đầu vào là `DORAEMON`, kết quả thu được tương ứng là `NOMEAROD`.



### Bài 04 [pya_l13_p08_ky_tu_o_vi_tri_chan]: Ký tự Ở vị trí chẵn

Bối cảnh: Trích xuất các ký tự tại các vị trí chỉ số chẵn là phương pháp lấy mẫu tín hiệu rời rạc phổ biến trong xử lý chuỗi văn bản.

Nhiệm vụ: Cho một chuỗi $S$. Hãy tạo ra một chuỗi mới chỉ gồm các ký tự nằm ở **chỉ số index chẵn** ($0, 2, 4, 6 \dots$) của chuỗi $S$.

**Đầu vào (Input):**

Một chuỗi ký tự $S$ ($1 \le |S| \le 1000$).

**Đầu ra (Output):**

Chuỗi mới thu được.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ABCDEF | ACE |

**Giải thích:**

Lấy các vị trí 0 ('A'), 2 ('C'), 4 ('E').



### Bài 05 [pya_l13_p07_rut_trich_ten_mien_email]: Rút trích tên miền email

Bối cảnh: Cô giáo dạy Tin học viết lên bảng một địa chỉ thư điện tử dạng `tentaikhoan@domain.com` để cả lớp cùng xem. Cô đố cả lớp phần đứng sau ký tự `@` được gọi là tên miền (domain). Bạn nào tìm đúng tên miền sẽ được một sticker ngôi sao. Hãy giúp cả lớp viết chương trình tìm tên miền thật nhanh.

Nhiệm vụ: Cho một địa chỉ email hợp lệ. Hãy in ra phần tên miền của địa chỉ đó.

**Đầu vào (Input):**

Một chuỗi email chứa đúng 1 ký tự `@`.

**Đầu ra (Output):**

Phần tên miền đứng sau `@`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| hocsinh@ikhedu.vn | ikhedu.vn |

**Giải thích:**

Với dữ liệu đầu vào là `hocsinh@ikhedu.vn`, kết quả thu được tương ứng là `ikhedu.vn`.



### Bài 06 [pya_l13_p01_ky_tu_dau_ky_tu_cuoi]: Ký tự đầu & ký tự cuối

Bối cảnh: Trong xử lý văn bản, việc trích xuất ký tự mở đầu và kết thúc của một từ mã giúp hệ thống nhanh chóng kiểm tra định dạng khung truyền tin.

Nhiệm vụ: Nhập vào một chuỗi ký tự $S$ không chứa dấu cách. Hãy in ra ký tự đầu tiên và ký tự cuối cùng của chuỗi $S$, cách nhau bởi một dấu cách.

**Đầu vào (Input):**

Một chuỗi ký tự $S$ ($1 \le |S| \le 100$).

**Đầu ra (Output):**

Ký tự đầu và ký tự cuối.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| PYTHON | P N |

**Giải thích:**

Với dữ liệu đầu vào là `PYTHON`, kết quả thu được tương ứng là `P N`.



### Bài 07 [pya_l13_p11_dich_chuyen_vong_quanh_left_rotation]: Dịch chuyển vòng quanh (left rotation)

Bối cảnh: Trong trò chơi xếp chữ, bạn Bi rủ cả lớp chơi trò tàu lửa nối đuôi nhau. Phép dịch trái chuỗi $K$ vị trí là thao tác nhấc $K$ ký tự đầu tiên của chuỗi đem gắn ra phía sau cùng.
 Ví dụ: Chuỗi `ABCDE` dịch trái 2 ký tự sẽ thành `CDEAB`.
Cả lớp reo lên vì đoàn tàu chữ chạy vòng quanh thật vui. Hãy giúp bạn Bi viết chương trình chạy đoàn tàu chữ này.

Nhiệm vụ: Cho chuỗi $S$ và số nguyên $K$ ($1 \le K \le |S| \le 10^5$). Hãy in ra chuỗi $S$ sau khi dịch trái $K$ vị trí.

**Đầu vào (Input):**

Dòng 1 chứa chuỗi $S$. Dòng 2 chứa số $K$.

**Đầu ra (Output):**

Chuỗi sau khi dịch.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ABCDE <br> 2 | CDEAB |

**Giải thích:**

Với dữ liệu đầu vào là `ABCDE
2`, kết quả thu được tương ứng là `CDEAB`.



### Bài 08 [pya_l13_p06_cat_doi_chuoi_ky_tu]: Cắt đôi chuỗi ký tự

Bối cảnh: Kỹ thuật chia đôi văn bản là bước khởi đầu trong nhiều thuật toán nén dữ liệu và mã hóa hai nửa đối xứng.

Nhiệm vụ: Cho một chuỗi $S$ có độ dài chẵn. Hãy chia chuỗi $S$ thành 2 nửa bằng nhau và in mỗi nửa trên một dòng.

**Đầu vào (Input):**

Một chuỗi $S$ có độ dài chẵn ($2 \le |S| \le 1000$).

**Đầu ra (Output):**

Dòng 1 in nửa đầu, dòng 2 in nửa sau.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| PYTHON | PYT <br> HON |

**Giải thích:**

Với dữ liệu đầu vào là `PYTHON`, kết quả thu được tương ứng là `PYT
HON`.



### Bài 09 [pya_l13_p09_hoan_doi_nua_dau_nua_sau]: Hoán đổi nửa đầu nửa sau

Bối cảnh: Phép tráo đổi hai nửa của một chuỗi dữ liệu có độ dài chẵn thường được ứng dụng trong các giao thức hoán vị thông tin cơ bản.

Nhiệm vụ: Cho chuỗi ký tự $S$ có độ dài chẵn $2N$. Hãy hoán đổi vị trí của nửa đầu chuỗi và nửa sau chuỗi với nhau.

**Đầu vào (Input):**

Một chuỗi $S$ có độ dài chẵn ($2 \le |S| \le 10^5$).

**Đầu ra (Output):**

Chuỗi sau khi hoán đổi 2 nửa.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ABCDEF | DEFABC |

**Giải thích:**

Với dữ liệu đầu vào là `ABCDEF`, kết quả thu được tương ứng là `DEFABC`.



### Bài 10 [pya_l13_p10_xoa_ky_tu_o_vi_tri_k]: Xóa ký tự ở vị trí K

Bối cảnh: Bạn Tí viết tên mình lên bảng rồi lỡ viết thừa một chữ cái ở giữa. Tí nhớ rằng chuỗi trong Python là bất biến (không thể dùng lệnh xóa trực tiếp `del s[k]`). Vì vậy Tí phải dùng kỹ thuật cắt lát ghép chuỗi để bỏ chữ thừa đi. Hãy giúp Tí viết chương trình xóa chữ thừa thật gọn.

Nhiệm vụ: Cho chuỗi $S$ và chỉ số nguyên $K$ ($0 \le K < |S|$). Hãy xóa ký tự tại vị trí $K$ và in ra chuỗi còn lại.

**Đầu vào (Input):**

Dòng 1 chứa chuỗi $S$. Dòng 2 chứa số nguyên $K$.

**Đầu ra (Output):**

Chuỗi sau khi xóa ký tự thứ $K$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| PYTHON <br> 2 | PYHON |

**Giải thích:**

Xóa ký tự tại index 2 là chữ 'T'.



### Bài 11 [pya_l13_p05_kiem_tra_tu_doi_xung_palindrome]: Kiểm tra từ đối xứng (palindrome)

Bối cảnh: Trong giờ ra chơi, bạn Na rủ cả lớp chơi trò soi gương với các con chữ. Na phát hiện một từ được gọi là từ đối xứng nếu đọc xuôi hay đọc ngược đều hoàn toàn giống nhau (ví dụ: `radar`, `level`, `madam`, `noon`). Cả lớp thi nhau tìm thêm thật nhiều từ ngộ nghĩnh như vậy. Hãy viết chương trình kiểm tra xem một từ có đối xứng hay không.

Nhiệm vụ: Cho một từ $S$. Kiểm tra xem $S$ có phải từ đối xứng không. In `YES` nếu đúng, ngược lại in `NO`.

**Đầu vào (Input):**

Một chuỗi $S$ viết liền ($1 \le |S| \le 1000$).

**Đầu ra (Output):**

`YES` hoặc `NO`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| RADAR | YES |

**Giải thích:**

Với dữ liệu đầu vào là `RADAR`, kết quả thu được tương ứng là `YES`.

**Ví dụ mẫu (Sample 2):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ROBOT | NO |



### Bài 12 [pya_l13_p12_chuoi_con_doi_xung_dai_nhat]: Chuỗi con đối xứng dài nhất

Bối cảnh: Bạn Mít có một vòng hạt với nhiều chữ cái xinh xắn xâu liền nhau. Cô giáo nói một chuỗi con là một đoạn các ký tự liên tiếp nhau của chuỗi ban đầu. Mít muốn tìm đoạn hạt đọc xuôi ngược giống nhau mà dài nhất để làm mặt dây chuyền. Hãy giúp bạn Mít tìm đoạn hạt đặc biệt đó.

Nhiệm vụ: Cho một chuỗi ký tự $S$. Hãy tìm độ dài của chuỗi con liên tiếp đối xứng dài nhất nằm trong chuỗi $S$.

**Đầu vào (Input):**

Một chuỗi ký tự $S$ ($1 \le |S| \le 200$).

**Đầu ra (Output):**

Độ dài lớn nhất tìm được.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ABCBADE | 5 |

**Giải thích:**

Chuỗi con đối xứng dài nhất là `ABCBA` có độ dài 5.



# Bài 14: Duyệt chuỗi, biến đổi ký tự và tách từ

## 1. Khái niệm & Bản chất của Xử lý chuỗi nâng cao

Ở bài trước, ta đã biết đánh chỉ số và cắt lát chuỗi (`s[i]`, `s[a:b]`). Nhưng văn bản thực tế thường rối hơn: mật mã, câu văn, cụm từ, số lẫn chữ cái.

Để làm tốt dạng này, em cần nắm 4 kỹ năng chính:
1. **Duyệt từng ký tự**: Xem từng ký tự là chữ cái, chữ số hay ký hiệu đặc biệt.
2. **Biến đổi ký tự**: Đổi qua lại giữa chữ hoa và chữ thường, thay ký tự.
3. **Bản chất mã ASCII**: Hiểu mối liên hệ giữa ký tự và số nguyên trong máy (`ord` và `chr`).
4. **Tách từ và chuẩn hóa văn bản**: Dùng `split()` và `join()` để tách từ trong câu.



![](/Users/vu/Developer/ikhEdu_lessons/courses/python-bang-a/assets_png/l14_string_ascii_methods.png)



---

## 2. Kiểm tra và phân loại ký tự

Python có sẵn các cách kiểm tra ký tự rất tiện, trả về `True` hoặc `False`:

| Phương thức | Ý nghĩa kỹ thuật | Ví dụ kiểm tra | Kết quả |
|---|---|---|:---:|
| `ch.isdigit()` | Ký tự `ch` có phải là chữ số (`'0'` đến `'9'`) không? | `'7'.isdigit()` | `True` |
| `ch.isalpha()` | Ký tự `ch` có phải là chữ cái (`'a'-'z'`, `'A'-'Z'`) không? | `'k'.isalpha()` | `True` |
| `ch.isupper()` | Ký tự `ch` có phải là chữ cái in hoa không? | `'A'.isupper()` | `True` |
| `ch.islower()` | Ký tự `ch` có phải là chữ cái in thường không? | `'b'.islower()` | `True` |
| `ch.isspace()` | Ký tự `ch` có phải là khoảng trắng (space, tab, enter) không? | `' '.isspace()` | `True` |

> **Lưu ý quan trọng:** Các cách kiểm tra trên chỉ đúng khi `ch` là một ký tự đơn hoặc chuỗi con cùng loại. Chuỗi rỗng `""` luôn cho `False`. Dấu cách `' '` không phải chữ cái, cũng không phải chữ số!

### Ứng dụng: Lọc và trích xuất chữ số từ văn bản hỗn hợp
```python
s = input()
chu_so = ""
for ch in s:
    if ch.isdigit():
        chu_so += ch
print(chu_so)
```

---

## 3. Biến đổi ký tự và chuỗi

Vì chuỗi trong Python **không đổi được trực tiếp**, các phép biến đổi **không sửa chuỗi gốc**, mà luôn tạo ra một **chuỗi mới**:

### 3.1. Chuyển đổi hoa — thường
* `s.upper()`: Tạo chuỗi mới, mọi chữ cái thành **in hoa**.
* `s.lower()`: Tạo chuỗi mới, mọi chữ cái thành **in thường**.
* `s.swapcase()`: Đảo lại: hoa thành thường, thường thành hoa.

```python
s = "Python 2026"
print(s.upper())     # "PYTHON 2026"
print(s.lower())     # "python 2026"
print(s.swapcase())  # "pYTHON 2026"
print(s)             # Vẫn là "Python 2026" (chuỗi gốc không đổi)
```

### 3.2. Thay thế chuỗi con với `s.replace(old, new)`
* Cú pháp: `s.replace(chuoi_cu, chuoi_moi)`
* Thay mọi chỗ `chuoi_cu` bằng `chuoi_moi`:
```python
s = "lap-trinh-python"
s_moi = s.replace("-", " ")
print(s_moi)  # "lap trinh python"
```

---

## 4. Bản chất mã ASCII: Cầu nối giữa Chữ cái và Con số

Trong máy, mỗi ký tự được ghi bằng một số nguyên từ $0$ đến $127$ (gọi là mã ASCII).

### 4.1. Bảng mã ASCII chuẩn mực cần nhớ nằm lòng

| Ký tự | Mã ASCII (`ord`) | Quy luật & Ứng dụng |
|:---:|:---:|---|
| `'0'` đến `'9'` | $48$ đến $57$ | Muốn đổi ký tự số sang số nguyên: `int(ch)` hoặc `ord(ch) - 48` |
| `'A'` đến `'Z'` | $65$ đến $90$ | Chữ hoa liên tiếp cách nhau đúng 1 đơn vị |
| `'a'` đến `'z'` | $97$ đến $122$ | Chữ thường liên tiếp cách nhau đúng 1 đơn vị |
| `' '` (space) | $32$ | Khoảng trắng |

> 💡 **Hằng số vàng 32:**
> $$\mathbf{ord('a') - ord('A') = 97 - 65 = 32}$$
> Chữ thường luôn lớn hơn chữ hoa tương ứng đúng **32 đơn vị**.
> Do đó:
> * Đổi hoa sang thường: `chr(ord(ch) + 32)`
> * Đổi thường sang hoa: `chr(ord(ch) - 32)`

### 4.2. Hai hàm chuyển đổi: `ord()` và `chr()`
* `ord(ch)`: Nhận **1 ký tự**, trả về **mã số ASCII** của nó.
* `chr(code)`: Nhận **mã số**, trả về **ký tự** tương ứng.

```python
print(ord('A'))         # In ra: 65
print(chr(65))          # In ra: 'A'
print(chr(ord('A') + 1)) # In ra: 'B' (Ký tự kế tiếp)
```

---

## 5. Tách từ (`split`) và Ghép từ (`join`) — Chuẩn hóa câu văn

Xử lý từ ngữ là dạng bài quen thuộc: đếm số từ, tìm từ dài nhất, đảo từ trong câu.

### 5.1. Phương thức `s.split()` thần thánh
* Khi gọi `s.split()` không kèm gì thêm, Python sẽ:
  1. Tự tìm mọi cụm khoảng trắng (1 dấu cách, nhiều dấu cách liền nhau, cách ở đầu/cuối).
  2. Tách câu thành một **danh sách (`list`) các từ riêng**.

```python
s = "   Ha    Noi   mua    thu   "
danh_sach_tu = s.split()
print(danh_sach_tu)      # ['Ha', 'Noi', 'mua', 'thu']
print(len(danh_sach_tu)) # In ra: 4 (Đếm số từ cực kỳ chính xác!)
```

### 5.2. Phương thức ghép chuỗi `sep.join(list)`
* Nối mọi chuỗi trong danh sách lại, ngăn cách bằng `sep`:
```python
tu = ['Python', 'la', 'ngon', 'ngu', 'tuyet', 'voi']
cau = " ".join(tu)
print(cau)  # "Python la ngon ngu tuyet voi"
```

---

## 6. Bảng mô phỏng biến thiên ô nhớ

### Chương trình: Tính tổng các chữ số xuất hiện trong một chuỗi hỗn hợp

```python
s = "A3B7C2"
tong = 0
for ch in s:
    if ch.isdigit():
        tong += int(ch)
print(tong)
```

| Bước | Vòng lặp `ch` | `ch.isdigit()`? | Thao tác thực hiện | Giá trị `tong` trong RAM |
|:---:|:---:|:---:|---|:---:|
| Khởi tạo | — | — | Khởi tạo biến tích lũy `tong = 0` | $0$ |
| $1$ | `'A'` | `False` | Không phải số, bỏ qua | $0$ |
| $2$ | `'3'` | `True` | `tong += int('3')` $\implies 0 + 3 = 3$ | $3$ |
| $3$ | `'B'` | `False` | Không phải số, bỏ qua | $3$ |
| $4$ | `'7'` | `True` | `tong += int('7')` $\implies 3 + 7 = 10$ | $10$ |
| $5$ | `'C'` | `False` | Không phải số, bỏ qua | $10$ |
| $6$ | `'2'` | `True` | `tong += int('2')` $\implies 10 + 2 = 12$ | $12$ |
| **Kết thúc** | — | — | In giá trị `tong` ra màn hình | **In: $12$** |

---

## 7. Lỗi hay gặp và bẫy lỗi kinh điển

> **Lỗi hay gặp 1: Nối chuỗi thay vì cộng số**
> * Khi duyệt các ký tự số, nếu viết:
>   ```python
>   tong += ch  # ch vẫn là kiểu chuỗi '3', '7'
>   ```
>   Thì máy sẽ ghép chuỗi: `"0" + "3" + "7" = "037"`, chứ không cộng số!
> * **Cách viết an toàn:** Luôn đổi kiểu `int(ch)` trước khi cộng: `tong += int(ch)`.

> **Lỗi hay gặp 2: Đếm số từ bằng cách đếm dấu cách**
> * Có bạn dùng cách: `so_tu = s.count(' ') + 1`.
> * Nếu văn bản có 2 dấu cách liền nhau `"Ha  Noi"`, cách trên đếm ra 3 từ — **sai hẳn!**
> * **Quy tắc vàng:** Luôn dùng `len(s.split())` để đếm từ đúng hẳn.

> **Lỗi hay gặp 3: Quên rằng `s.upper()` không đổi chuỗi gốc**
> * Viết:
>   ```python
>   s = "abc"
>   s.upper()
>   print(s)  # Vẫn in ra: "abc"
>   ```
> * **Nhớ gán lại:** `s = s.upper()`.

---

## 8. Mẫu code thường gặp

### 8.1. Đếm số lượng chữ cái in hoa, in thường và chữ số
```python
s = input()
hoa = 0
thuong = 0
so = 0

for ch in s:
    if ch.isupper():
        hoa += 1
    elif ch.islower():
        thuong += 1
    elif ch.isdigit():
        so += 1

print(hoa, thuong, so)
```

### 8.2. Chuẩn hóa câu văn (Xóa khoảng trắng thừa, viết hoa chữ cái đầu)
```python
s = input()
tu = s.split()
tu_chuan = [w.capitalize() for w in tu]
print(" ".join(tu_chuan))
```


## Bài tập thực hành


### Bài 01 [pya_l14_p02_chuyen_toan_bo_thanh_chu_hoa]: Chuyển toàn bộ thành chữ hoa

Bối cảnh: Chuẩn hóa toàn bộ văn bản sang dạng chữ in hoa giúp việc đối sánh chuỗi trong các cơ sở dữ liệu không bị ảnh hưởng bởi quy cách gõ phím.

Nhiệm vụ: Nhập một dòng văn bản $S$. Hãy chuyển tất cả các chữ cái trong $S$ thành chữ in hoa và in ra màn hình.

**Đầu vào (Input):**

Một dòng văn bản $S$.

**Đầu ra (Output):**

Chuỗi sau khi đã in hoa toàn bộ.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ikhedu vietnam | IKHEDU VIETNAM |

**Giải thích:**

Với dữ liệu đầu vào là `ikhedu vietnam`, kết quả thu được tương ứng là `IKHEDU VIETNAM`.



### Bài 02 [pya_l14_p08_thay_the_ky_tu_bi_mat]: Thay thế ký tự bí mật

Bối cảnh: Để chuẩn hóa định dạng văn bản cho đường dẫn liên kết, hệ thống cần thay thế toàn bộ khoảng trống bằng ký tự gạch dưới phân tách.

Nhiệm vụ: Nhập một chuỗi $S$. Hãy thay thế tất cả các ký tự khoảng trắng `" "` trong $S$ bằng dấu gạch dưới `"_"` và in ra kết quả.

**Đầu vào (Input):**

Một chuỗi $S$.

**Đầu ra (Output):**

Chuỗi sau khi thay thế.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| hoc lap trinh de vui | hoc_lap_trinh_de_vui |

**Giải thích:**

Với dữ liệu đầu vào là `hoc lap trinh de vui`, kết quả thu được tương ứng là `hoc_lap_trinh_de_vui`.



### Bài 03 [pya_l14_p09_xoa_bo_toan_bo_dau_cach]: Xóa bỏ toàn bộ dấu cách

Bối cảnh: Loại bỏ toàn bộ khoảng trắng thừa giúp nén kích thước chuỗi và chuẩn hóa dữ liệu khóa tìm kiếm.

Nhiệm vụ: Cho một dòng văn bản $S$. Hãy xóa bỏ tất cả các ký tự khoảng trắng trong chuỗi để thu được một chuỗi viết liền hoàn toàn.

**Đầu vào (Input):**

Một dòng văn bản $S$ ($1 \le |S| \le 10^5$).

**Đầu ra (Output):**

Chuỗi viết liền không còn khoảng trắng.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| Lap Trinh Python Bang A | LapTrinhPythonBangA |

**Giải thích:**

Với dữ liệu đầu vào là `Lap Trinh Python Bang A`, kết quả thu được tương ứng là `LapTrinhPythonBangA`.



### Bài 04 [pya_l15_p03_ma_ascii_cua_ky_tu]: Mã ASCII của ký tự

Bối cảnh: Mỗi ký tự hiển thị trên máy tính đều được mã hóa bằng một số nguyên duy nhất theo chuẩn ASCII. Việc tra cứu mã này là kiến thức cốt lõi về biểu diễn dữ liệu.

Nhiệm vụ: Nhập một ký tự bất kỳ từ bàn phím. Hãy in ra mã số ASCII của ký tự đó.

**Đầu vào (Input):**

Một ký tự duy nhất $C$.

**Đầu ra (Output):**

Một số nguyên là mã ASCII.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| A | 65 |

**Giải thích:**

Với dữ liệu đầu vào là `A`, kết quả thu được tương ứng là `65`.

**Ví dụ mẫu (Sample 2):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| a | 97 |



### Bài 05 [pya_l15_p01_dem_so_tu_trong_cau]: Đếm số từ trong câu

Bối cảnh: Đếm số lượng từ trong một đoạn văn bản là chỉ số cơ bản nhất của các phần mềm xử lý soạn thảo và phân tích ngôn ngữ tự nhiên.

Nhiệm vụ: Nhập một dòng văn bản $S$ có thể chứa nhiều khoảng trắng thừa ở đầu, cuối hoặc giữa các từ. Hãy đếm xem câu văn đó có bao nhiêu từ.

**Đầu vào (Input):**

Một dòng văn bản $S$ ($1 \le |S| \le 1000$).

**Đầu ra (Output):**

Số lượng từ trong câu.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| Chuc mung nam moi | 4 |

**Giải thích:**

Có 4 từ: 'Chuc', 'mung', 'nam', 'moi'.



### Bài 06 [pya_l15_p05_tim_tu_dai_nhat_trong_cau]: Tìm từ dài nhất trong câu

Bối cảnh: Thí sinh đang tìm kiếm một giá trị đặc biệt trong tập dữ liệu. Hãy viết chương trình tìm kiếm hiệu quả.

Nhiệm vụ: Cho một câu văn $S$. Hãy tìm và in ra từ có độ dài dài nhất trong câu. Nếu có nhiều từ cùng độ dài dài nhất, in ra từ đầu tiên xuất hiện.

**Đầu vào (Input):**

Một dòng văn bản $S$.

**Đầu ra (Output):**

Từ dài nhất tìm được.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| Hoc lap trinh rat thu vi | trinh |

**Giải thích:**

Từ 'trinh' có 5 chữ cái (dài nhất).



### Bài 07 [pya_l15_p04_ky_tu_ke_tiep_trong_bang_chu_cai]: Ký tự kế tiếp trong bảng chữ cái

Bối cảnh: Xác định ký tự liền sau trong bảng chữ cái dựa trên phép tịnh tiến mã số ASCII là nền tảng của nhiều thuật toán sinh khóa và mã hóa cổ điển.

Nhiệm vụ: Nhập vào một chữ cái in hoa từ `'A'` đến `'Y'`. Hãy in ra chữ cái đứng ngay liền sau nó trong bảng chữ cái tiếng Anh.

**Đầu vào (Input):**

Một ký tự in hoa $C \in ['A' \dots 'Y']$.

**Đầu ra (Output):**

Chữ cái liền sau.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| C | D |

**Giải thích:**

Với dữ liệu đầu vào là `C`, kết quả thu được tương ứng là `D`.



### Bài 08 [pya_l15_p02_tu_dau_tien_tu_cuoi_cung]: Từ đầu tiên & từ cuối cùng

Bối cảnh: Trích xuất từ mở đầu và từ kết thúc hỗ trợ xác định cấu trúc ngữ pháp và tiêu đề của một câu lệnh truy vấn.

Nhiệm vụ: Cho một câu văn $S$. Hãy in ra từ đầu tiên và từ cuối cùng của câu văn đó trên 2 dòng riêng biệt.

**Đầu vào (Input):**

Một dòng văn bản có ít nhất 1 từ.

**Đầu ra (Output):**

Dòng 1 in từ đầu tiên, dòng 2 in từ cuối cùng.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| Hoc Python cuc vui | Hoc <br> vui |

**Giải thích:**

Với dữ liệu đầu vào là `Hoc Python cuc vui`, kết quả thu được tương ứng là `Hoc
vui`.



### Bài 09 [pya_l15_p06_chuan_hoa_khoang_trang]: Chuẩn hóa khoảng trắng

Bối cảnh: Na tập đánh máy để viết thiệp mời sinh nhật cho cả lớp. Khi đánh máy, một bạn học sinh lỡ tay bấm rất nhiều dấu cách thừa giữa các từ và ở hai đầu câu văn. Tấm thiệp trông rời rạc và chưa đẹp mắt chút nào. Hãy giúp Na dọn dẹp tấm thiệp cho gọn gàng.

Nhiệm vụ: Cho chuỗi văn bản $S$. Hãy chuẩn hóa câu văn sao cho: không còn khoảng trắng ở đầu và cuối câu, giữa mỗi từ chỉ có duy nhất **một dấu cách**.

**Đầu vào (Input):**

Một dòng văn bản $S$ ($1 \le |S| \le 1000$).

**Đầu ra (Output):**

Câu văn chuẩn hóa.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| Python rat la tuyet | Python rat la tuyet |

**Giải thích:**

Với dữ liệu đầu vào là `Python rat la tuyet`, kết quả thu được tương ứng là `Python rat la tuyet`.



### Bài 10 [pya_l14_p01_in_tung_chu_cai_xuong_dong]: In từng chữ cái xuống dòng

Bối cảnh: Duyệt tuần tự qua từng ký tự của văn bản là thao tác nền tảng để phân tích cú pháp và kiểm định luồng dữ liệu ký tự.

Nhiệm vụ: Nhập vào một từ $S$. Hãy in ra từng chữ cái của từ đó, mỗi chữ cái nằm trên một dòng riêng biệt.

**Đầu vào (Input):**

Một chuỗi ký tự $S$ ($1 \le |S| \le 100$).

**Đầu ra (Output):**

Mỗi ký tự trên một dòng.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| CAT | C <br> A <br> T |

**Giải thích:**

Với dữ liệu đầu vào là `CAT`, kết quả thu được tương ứng là `C
A
T`.



### Bài 11 [pya_l15_p07_viet_hoa_chu_cai_dau_moi_tu_title_case]: Viết hoa chữ cái đầu mỗi từ (title case)

Bối cảnh: Quy tắc viết hoa chữ cái đầu mỗi từ là chuẩn mực định dạng bắt buộc khi lưu trữ danh tính người dùng trong hệ thống cơ sở dữ liệu.

Nhiệm vụ: Nhập họ và tên của một bạn học sinh viết chưa đúng quy tắc (ví dụ: `nguyen van an`). Hãy chuẩn hóa họ tên bằng cách viết hoa chữ cái đầu tiên của mỗi từ và viết thường các chữ cái còn lại.

**Đầu vào (Input):**

Một chuỗi họ tên.

**Đầu ra (Output):**

Họ tên sau khi chuẩn hóa.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| nguyen van an | Nguyen Van An |

**Giải thích:**

Với dữ liệu đầu vào là `nguyen van an`, kết quả thu được tương ứng là `Nguyen Van An`.



### Bài 12 [pya_l15_p08_dao_nguoc_tung_tu_trong_cau]: Đảo ngược từng từ trong câu

Bối cảnh: Đảo ngược các ký tự nội bộ của từng từ trong khi vẫn bảo toàn thứ tự các từ trong câu là bài toán rèn luyện kỹ năng kết hợp tách từ và cắt lát chuỗi.

Nhiệm vụ: Cho một câu văn. Hãy đảo ngược thứ tự các chữ cái trong từng từ một, nhưng giữ nguyên vị trí của các từ trong câu.

**Đầu vào (Input):**

Một dòng văn bản.

**Đầu ra (Output):**

Câu văn mới với từng từ bị đảo ngược.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| Toi yeu Viet Nam | ioT uey teiV maN |

**Giải thích:**

'Toi' -> 'ioT', 'yeu' -> 'uey'...



### Bài 13 [pya_l15_p12_mat_ma_thay_the_hoan_vi_anagram]: Mật mã thay thế hoán vị (anagram)

Bối cảnh: Trong giờ thủ công, hai bạn cùng xáo trộn các thẻ chữ cái để xếp thành từ mới. Hai từ được gọi là "Anagram" (hoán vị ký tự của nhau) nếu chúng có thể tạo thành từ nhau bằng cách xáo trộn lại thứ tự các chữ cái (ví dụ: `silent` và `listen`, `heart` và `earth`). Cả lớp thi xem ai xếp được cặp từ trùng khớp nhau. Hãy giúp các bạn kiểm tra xem hai từ có phải Anagram không.

Nhiệm vụ: Cho 2 từ $S_1$ và $S_2$. Kiểm tra xem chúng có phải là Anagram của nhau không. In `YES` nếu đúng, ngược lại in `NO`.

**Đầu vào (Input):**

Hai dòng, mỗi dòng chứa một từ viết thường ($1 \le |S_1|, |S_2| \le 10^5$).

**Đầu ra (Output):**

`YES` hoặc `NO`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| listen <br> silent | YES |

**Giải thích:**

Với dữ liệu đầu vào là `listen
silent`, kết quả thu được tương ứng là `YES`.

**Ví dụ mẫu (Sample 2):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| hello <br> world | NO |



### Bài 14 [pya_l15_p11_tu_xuat_hien_nhieu_nhat_trong_doan]: Từ xuất hiện nhiều nhất trong đoạn

Bối cảnh: Tìm từ xuất hiện với tần suất cao nhất trong một văn bản là bài toán quan trọng trong trích xuất từ khóa và khai phá dữ liệu văn bản.

Nhiệm vụ: Cho một đoạn văn bản chỉ gồm các từ cách nhau bởi khoảng trắng. Hãy tìm xem từ nào xuất hiện nhiều lần nhất trong đoạn văn đó và xuất hiện bao nhiêu lần. Dữ liệu đảm bảo chỉ có 1 từ xuất hiện nhiều nhất.

**Đầu vào (Input):**

Một đoạn văn bản $S$ gồm các chữ cái viết thường.

**Đầu ra (Output):**

Từ xuất hiện nhiều nhất và số lần xuất hiện, cách nhau một khoảng trắng.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| cam quyt mit dua cam xoai cam dua | cam 3 |

**Giải thích:**

Với dữ liệu đầu vào là `cam quyt mit dua cam xoai cam dua`, kết quả thu được tương ứng là `cam 3`.



### Bài 15 [pya_l14_p10_dem_so_luong_nguyen_am]: Đếm số lượng nguyên âm

Bối cảnh: Trong giờ tiếng Anh, cô giáo dạy cả lớp bài hát về các chữ cái vui nhộn. Cô nói trong tiếng Anh, 5 chữ cái: `A, E, I, O, U` (cả hoa lẫn thường) được gọi là nguyên âm (vowels). Bạn nào đếm đúng số nguyên âm trong một từ sẽ được hát trước cả lớp. Hãy giúp cả lớp đếm số nguyên âm thật nhanh.

Nhiệm vụ: Cho một chuỗi ký tự $S$. Hãy đếm xem có bao nhiêu ký tự nguyên âm trong chuỗi $S$.

**Đầu vào (Input):**

Chuỗi văn bản $S$ ($1 \le |S| \le 1000$).

**Đầu ra (Output):**

Số lượng nguyên âm.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| EDUCATION | 5 |

**Giải thích:**

Các nguyên âm: E, U, A, I, O (có 5 nguyên âm).



### Bài 16 [pya_l14_p03_dem_ky_tu_a_ca_hoa_lan_thuong]: Đếm ký tự 'A' (cả hoa lẫn thường)

Bối cảnh: Thống kê tần suất xuất hiện của một chữ cái cụ thể (không phân biệt hoa thường) là thao tác căn bản trong phân tích văn bản ngôn ngữ.

Nhiệm vụ: Cho một chuỗi ký tự $S$. Hãy đếm xem có bao nhiêu chữ cái `'A'` hoặc `'a'` xuất hiện trong chuỗi $S$.

**Đầu vào (Input):**

Một chuỗi văn bản $S$ ($1 \le |S| \le 1000$).

**Đầu ra (Output):**

Số lượng chữ cái 'A' hoặc 'a'.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| An va Ba hoc bai | 4 |

**Giải thích:**

Gồm chữ 'A' (1 lần) và 'a' (3 lần trong 'va', 'Ba', 'bai').



### Bài 17 [pya_l14_p06_tinh_tong_cac_chu_so_trong_chuoi]: Tính tổng các chữ số trong chuỗi

Bối cảnh: Trong bài kiểm tra, người dùng cần tính nhanh tổng một dãy số. Hãy viết chương trình hỗ trợ tính toán.

Nhiệm vụ: Cho một chuỗi văn bản $S$. Hãy tính tổng giá trị của tất cả các chữ số xuất hiện trong chuỗi đó.

**Đầu vào (Input):**

Chuỗi văn bản $S$ ($1 \le |S| \le 10^5$).

**Đầu ra (Output):**

Một số nguyên duy nhất là tổng các chữ số.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| A1B2C3D4 | 10 |

**Giải thích:**

$1 + 2 + 3 + 4 = 10$.



### Bài 18 [pya_l14_p05_tach_rieng_chu_so_ra_khoi_van_ban]: Tách riêng chữ số ra khỏi văn bản

Bối cảnh: Bạn An nhận được một bức thư mật mã, trong đó có các chữ số bị giấu lẫn vào giữa các chữ cái. An phải thật tinh mắt mới thấy những con số trốn kỹ trong dòng chữ. Cả nhóm bạn quyết tâm nhặt hết các chữ số ra để đọc mật thư. Hãy giúp bạn An nhặt hết các chữ số bí mật này.

Nhiệm vụ: Cho chuỗi $S$. Hãy nhặt ra toàn bộ các ký tự là chữ số ('0' - '9') và ghép chúng lại theo thứ tự ban đầu để in ra màn hình. Nếu không có chữ số nào, in ra `KHONG CO`.

**Đầu vào (Input):**

Chuỗi văn bản $S$ ($1 \le |S| \le 1000$).

**Đầu ra (Output):**

Chuỗi các chữ số ghép lại, hoặc `KHONG CO`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| Toi sinh nam 2014 vao thang 08 | 201408 |

**Giải thích:**

Với dữ liệu đầu vào là `Toi sinh nam 2014 vao thang 08`, kết quả thu được tương ứng là `201408`.



### Bài 19 [pya_l14_p11_nen_chuoi_ky_tu_runlength_encoding]: Nén chuỗi ký tự (Run-Length encoding)

Bối cảnh: Bạn Nam gấp thật nhiều ngôi sao giấy cùng màu rồi xếp chúng thành hàng dài trên bàn. Cô giáo dạy thuật toán nén chuỗi đơn giản thay thế một dãy các ký tự giống nhau liên tiếp bằng ký tự đó kèm theo số lần lặp lại.
 Ví dụ: `AAABBC` nén thành `A3B2C1`.
Nam muốn ghi lại hàng ngôi sao thật gọn vào sổ. Hãy giúp bạn Nam viết chương trình nén chuỗi thật gọn.

Nhiệm vụ: Cho một chuỗi $S$ chỉ gồm các chữ cái in hoa. Hãy in ra dạng nén của chuỗi $S$.

**Đầu vào (Input):**

Một chuỗi $S$ ($1 \le |S| \le 1000$).

**Đầu ra (Output):**

Chuỗi sau khi nén.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| AAABBCCCC | A3B2C4 |

**Giải thích:**

Với dữ liệu đầu vào là `AAABBCCCC`, kết quả thu được tương ứng là `A3B2C4`.



### Bài 20 [pya_l14_p04_dem_chu_cai_in_hoa_in_thuong]: Đếm chữ cái in hoa & in thường

Bối cảnh: Đo lường tỉ lệ giữa chữ cái in hoa và in thường giúp hệ thống tự động đánh giá độ phức tạp và độ an toàn của mật khẩu.

Nhiệm vụ: Cho một chuỗi $S$. Hãy đếm xem có bao nhiêu chữ cái in hoa và bao nhiêu chữ cái in thường trong chuỗi đó.

**Đầu vào (Input):**

Chuỗi ký tự $S$.

**Đầu ra (Output):**

Hai số nguyên cách nhau một khoảng trắng: số lượng chữ in hoa trước, số lượng chữ in thường sau.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| Lap Trinh Python | 3 11 |

**Giải thích:**

Chữ in hoa: 'L', 'T', 'P' (3 chữ).



### Bài 21 [pya_l15_p09_mat_ma_caesar_dich_chuyen_k]: Mật mã Caesar dịch chuyển K

Bối cảnh: Bạn Bin và cả nhóm chơi trò điệp viên gửi thư bí mật cho nhau trong sân trường. Hoàng đế Caesar mã hóa bức thư gồm các chữ cái in hoa (`'A'` đến `'Z'`) bằng cách dịch chuyển mỗi chữ cái sang phải $K$ bước theo vòng tròn 26 chữ cái ($A \to B \dots Z \to A$). Cả nhóm háo hức muốn tự mã hóa thư của riêng mình. Hãy giúp bạn Bin viết chương trình mã hóa thư.

Nhiệm vụ: Cho chuỗi $S$ chỉ gồm các chữ cái in hoa và số nguyên $K$ ($1 \le K \le 25$). Hãy in ra bản mật mã sau khi mã hóa.

**Đầu vào (Input):**

Dòng 1 chứa chuỗi $S$. Dòng 2 chứa số $K$.

**Đầu ra (Output):**

Chuỗi sau khi mã hóa.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| ABCXYZ <br> 3 | DEFABC |

**Giải thích:**

'A'->'D', 'B'->'E', 'X'->'A', 'Y'->'B', 'Z'->'C'.
* **Công thức toán học:** `chr((ord(ch) - ord('A') + k) % 26 + ord('A'))`.



### Bài 22 [pya_l15_p10_giai_ma_mat_thu_caesar]: Giải mã mật thư Caesar

Bối cảnh: Mật mã Caesar là một trong những phương pháp mã hóa thay thế lâu đời nhất, hoạt động bằng cách dịch chuyển từng chữ cái trong bảng mã theo một bước nhảy cố định.

Nhiệm vụ: Cho một bản mật mã $S$ (chỉ gồm các chữ cái in hoa) đã bị mã hóa Caesar với bước nhảy $K$. Hãy giải mã để tìm lại thông điệp ban đầu.

**Đầu vào (Input):**

Dòng 1 chứa bản mật mã $S$. Dòng 2 chứa số nguyên $K$ ($1 \le K \le 25$).

**Đầu ra (Output):**

Thông điệp ban đầu trước khi mã hóa.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| DEFABC <br> 3 | ABCXYZ |

**Giải thích:**

Với dữ liệu đầu vào là `DEFABC
3`, kết quả thu được tương ứng là `ABCXYZ`.



### Bài 23 [pya_l14_p07_doi_chu_hoa_thanh_thuong_nguoc_lai]: Đổi chữ hoa thành thường & ngược lại

Bối cảnh: Đảo ngược trạng thái viết hoa và viết thường trên toàn bộ văn bản là thao tác chuyển đổi định dạng thường gặp trong các trình biên tập mã nguồn.

Nhiệm vụ: Cho chuỗi ký tự $S$. Hãy biến đổi chuỗi bằng quy tắc: chữ hoa đổi thành chữ thường, chữ thường đổi thành chữ hoa, các ký tự khác (số, dấu câu, khoảng trắng) giữ nguyên.

**Đầu vào (Input):**

Một chuỗi văn bản $S$.

**Đầu ra (Output):**

Chuỗi sau khi biến đổi.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| Hello World 123 | hELLO wORLD 123 |

**Giải thích:**

Với dữ liệu đầu vào là `Hello World 123`, kết quả thu được tương ứng là `hELLO wORLD 123`.



### Bài 24 [pya_l14_p12_trich_xuat_so_lon_nhat_trong_van_ban]: Trích xuất số lớn nhất trong văn bản

Bối cảnh: Lớp trưởng ghi một bài báo cáo, trong đó có các con số nằm rải rác giữa các câu chữ. Một con số có thể có nhiều chữ số liên tiếp nhau. Cả lớp muốn biết con số nào to nhất để khen bạn được điểm cao. Hãy giúp lớp trưởng tìm ra con số lớn nhất trong bài báo cáo.

Nhiệm vụ: Cho chuỗi văn bản $S$. Hãy tìm và in ra giá trị của **con số nguyên lớn nhất** xuất hiện trong chuỗi đó. Dữ liệu đảm bảo có ít nhất 1 chữ số.

**Đầu vào (Input):**

Một chuỗi văn bản $S$ ($1 \le |S| \le 1000$).

**Đầu ra (Output):**

Số nguyên lớn nhất tìm được.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| Lop 5A co 38 hoc sinh va 105 quyen sach | 105 |

**Giải thích:**

Các con số xuất hiện là: 5, 38, 105. Số lớn nhất là 105.



# Phụ lục A: Nền tảng Python
## 1. KHUNG TƯ DUY CỦA MỌI BÀI LẬP TRÌNH
### Mô hình Input – Process – Output
| Bước | Em tự hỏi | Ghi ra giấy |
|------|-----------|-------------|
| Đầu vào | Đề cho gì? | Tên từng số, từng dòng |
| Xử lý | Tính gì, theo bước nào? | Công thức từng bước |
| Đầu ra | In ra cái gì? | Đúng thứ tự cần in |
```python
n = int(input())
tong = n + 10
print(tong)
```
### Công thức trước code
| Bước | Việc làm |
|------|----------|
| 1 | Gạch chân các số đề cho |
| 2 | Viết cách tính bằng lời của em |
| 3 | Tính tay một ví dụ nhỏ rồi mới viết code |
### Chuỗi ghi nhớ nền tảng
> Đọc vào — tính toán — in ra — thử lại.
```python
a = int(input())
b = int(input())
print(a + b)
```
## 2. KHUNG CHƯƠNG TRÌNH PYTHON TỐI THIỂU
| Việc | Mẫu |
|------|-----|
| Đọc vào | `n = int(input())` |
| Tính toán | `ket_qua = n + 5` |
| In ra | `print(ket_qua)` |
Hai số trên một dòng, cách nhau bằng dấu cách:
```python
a, b = map(int, input().split())
print(a + b)
```
## 3. BIẾN VÀ KIỂU DỮ LIỆU
### Quy tắc đặt tên biến
| Quy tắc | Đúng | Chưa đúng |
|---------|------|-----------|
| Chữ, số, dấu gạch dưới | `diem_toan` | `điểm-toán` |
| Bắt đầu bằng chữ | `tong_1` | `1_tong` |
| Ngắn mà rõ nghĩa, không trùng từ của Python | `tuoi` | `print` |
```python
tuoi = 10
ten = "Na"
print(tuoi)
```
### Các kiểu int, float, str, bool, list
| Kiểu | Nghĩa | Ví dụ |
|------|-------|-------|
| `int` | Số nguyên | `5`, `-3` |
| `float` | Số có phần lẻ | `2.5` |
| `str` | Chuỗi chữ | `"xin chào"` |
| `bool` | Đúng hoặc sai | `True`, `False` |
| `list` | Nhiều giá trị | `[2, 4, 6]` |
```python
tuoi = 10
ten = "Na"
diem = [8, 9, 10]
print(ten)
```
### Khởi tạo biến tích lũy
| Muốn làm gì | Viết lúc đầu |
|-------------|--------------|
| Tính tổng | `tong = 0` |
| Đếm số lượng | `dem = 0` |
| Tìm số to nhất | `lon_nhat = 0` |
| Ghép chữ | `cau = ""` |
## 4. NHẬP VÀ XUẤT DỮ LIỆU
### Ba lưu ý thường gặp
| Lưu ý | Mẫu đúng |
|-------|----------|
| Chữ đọc vào luôn là chuỗi | `ten = input()` |
| Muốn tính phải đổi kiểu | `n = int(input())` |
| Một dòng nhiều số thì tách ra | `a, b = map(int, input().split())` |
```python
n = int(input())
print(n + 1)
```
Đọc số có phần lẻ, đọc hai số một dòng, in theo ý muốn:
```python
x = float(input())
a, b = map(int, input().split())
print(3, 4, 5, sep="-")
print("xin", end=" ")
print("chào")
```
In kèm lời giải thích:
```python
tuoi = 10
print(f"Năm nay em {tuoi} tuổi.")
```
## 5. TOÁN TỬ VÀ BIỂU THỨC
### Toán tử số học
| Viết | Nghĩa | Kết quả của `5` và `2` |
|------|-------|------------------------|
| `+ - * /` | Cộng trừ nhân chia | `7, 3, 10, 2.5` |
| `//` | Chia lấy phần nguyên | `5 // 2` cho `2` |
| `%` | Chia lấy phần dư | `5 % 2` cho `1` |
| `**` | Lũy thừa | `2 ** 3` cho `8` |
```python
print(3 + 2)
print(5 // 2)
print(2 ** 3)
```
### Chia nguyên và phần dư
| Muốn biết | Dùng |
|-----------|------|
| Mỗi bạn được mấy cái | `7 // 2` cho `3` |
| Còn thừa mấy cái | `7 % 2` cho `1` |
| Số có chẵn không | `n % 2 == 0` |
### Toán tử so sánh
| Viết | Nghĩa |
|------|-------|
| `==` / `!=` | Bằng nhau / khác nhau |
| `>` / `<` | Lớn hơn / nhỏ hơn |
| `>=` / `<=` | Lớn hơn hoặc bằng / nhỏ hơn hoặc bằng |
```python
print(5 > 3)
print(4 == 5)
```
### Toán tử logic
| Viết | Nghĩa | Ví dụ |
|------|-------|-------|
| `and` | Cả hai đều đúng | `a > 0 and b > 0` |
| `or` | Một cái đúng là đủ | `a > 0 or b > 0` |
| `not` | Đổi đúng thành sai | `not (a > 0)` |
```python
tuoi = 10
print(tuoi > 5 and tuoi < 15)
```
### Thứ tự ưu tiên
| Trước | Sau |
|-------|-----|
| Ngoặc `( )`, rồi `**` | Nhân chia `* / // %` |
| Cộng trừ `+ -` | So sánh, `not`, `and`, `or` |
```python
print(2 + 3 * 4)
print((2 + 3) * 4)
```
## 6. ĐIỀU KIỆN — RẼ NHÁNH
### Mẫu if / if-else / if-elif-else
| Mẫu | Khi nào dùng |
|-----|--------------|
| `if` | Chỉ làm khi đúng |
| `if-else` | Chọn một trong hai |
| `if-elif-else` | Xếp nhiều mức |
```python
diem = int(input())
if diem >= 9:
    print("giỏi")
elif diem >= 7:
    print("khá")
else:
    print("cố gắng thêm")
```
### Quy tắc thụt lề
| Quy tắc | Nhớ |
|---------|-----|
| Sau dấu `:` thụt vào 4 dấu cách | Dòng trong nhánh lùi vào |
| Cùng nhánh thì thẳng hàng | Hết nhánh thì hết thụt lề |
```python
n = int(input())
if n > 0:
    print("số dương")
print("xong")
```
### Lỗi thường gặp
| Lỗi | Cách sửa |
|-----|----------|
| Quên dấu `:` sau `if` | Thêm `:` cuối dòng điều kiện |
| Viết `=` khi so sánh | So sánh viết `==` |
| Thụt lề lệch nhau | Căn thẳng hàng, mỗi lần 4 dấu cách |
```python
n = 5
if n == 5:
    print("đúng rồi")
```
## 7. VÒNG LẶP
### for và range
| Viết | Chạy qua |
|------|----------|
| `range(5)` | `0, 1, 2, 3, 4` |
| `range(1, 6)` | `1, 2, 3, 4, 5` |
| `range(2, 10, 2)` | `2, 4, 6, 8` |
```python
tong = 0
for i in range(1, 101):
    tong = tong + i
print(tong)
```
### while
```python
n = 5
while n > 0:
    print(n)
    n = n - 1
```
### break và continue
| Lệnh | Nghĩa |
|------|-------|
| `break` | Dừng hẳn vòng lặp |
| `continue` | Bỏ lượt này, sang lượt sau |
```python
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)
```
### Vòng lặp lồng nhau
```python
for i in range(3):
    for j in range(5):
        print("*", end="")
    print()
```
## 8. BỐN MẪU TÍCH LŨY
| Mẫu | Bắt đầu | Trong vòng lặp |
|-----|---------|----------------|
| Tổng | `tong = 0` | `tong = tong + x` |
| Đếm | `dem = 0` | `dem = dem + 1` |
| To nhất | `lon_nhat = 0` | `if x > lon_nhat:` rồi gán |
| Nhỏ nhất | `nho_nhat = danh_sach[0]` | `if x < nho_nhat:` rồi gán |
### Tính tổng
```python
tong = 0
for i in range(1, 6):
    tong = tong + i
print(tong)
```
### Đếm phần tử
```python
dem = 0
for i in range(1, 11):
    if i % 2 == 0:
        dem = dem + 1
print(dem)
```
### Tìm giá trị lớn nhất
```python
lon_nhat = 0
for x in [3, 7, 2, 9, 4]:
    if x > lon_nhat:
        lon_nhat = x
print(lon_nhat)
```
### Tìm giá trị nhỏ nhất
```python
danh_sach = [3, 7, 2, 9, 4]
nho_nhat = danh_sach[0]
for x in danh_sach:
    if x < nho_nhat:
        nho_nhat = x
print(nho_nhat)
```
## 9. DANH SÁCH VÀ CHUỖI
### Danh sách và chỉ số
Vị trí đầu là `0`, vị trí cuối là `-1`.
```python
ban = ["An", "Bình", "Chi"]
print(ban[0])
print(ban[-1])
print(len(ban))
```
### Đọc và duyệt danh sách
```python
n = int(input())
danh_sach = []
for i in range(n):
    danh_sach.append(int(input()))
for i in range(len(danh_sach)):
    print(i, danh_sach[i])
```
### Các thao tác cơ bản
| Muốn làm gì | Mẫu |
|-------------|-----|
| Thêm vào cuối | `danh_sach.append(x)` |
| Cộng tổng / to nhất / nhỏ nhất | `sum(...)` / `max(...)` / `min(...)` |
| Sắp xếp / đếm số lượng | `sort()` / `len(...)` |
### Xử lý chuỗi
| Muốn làm gì | Mẫu |
|-------------|-----|
| Đếm số chữ / lấy chữ đầu | `len(ten)` / `ten[0]` |
| Tách câu thành từ | `cau.split()` |
| So sánh hai chuỗi | `if a == b:` |
```python
cau = input()
tu = cau.split()
print(len(tu))
print(tu)
```
## 10. GỠ LỖI VÀ KIỂM THỬ
### In giá trị trung gian
```python
n = int(input())
print(n)
tong = n * 2
print(tong)
```
| Muốn xem gì | In thêm dòng nào |
|-------------|------------------|
| Giá trị đọc vào | `print(n)` sau `input()` |
| Trong vòng lặp | `print(i, tong)` trong vòng lặp |
### Bộ test tối thiểu
| Nhóm | Ví dụ với bài chẵn lẻ |
|------|-----------------------|
| Nhỏ nhất | `1` |
| Hay gặp | `4`, `7` |
| Chỗ dễ đổi kết quả | `0`, số âm `-2` |
```python
n = int(input())
if n % 2 == 0:
    print("số chẵn")
else:
    print("số lẻ")
```
## TÓM TẮT MỘT TRANG
| Việc cần làm | Mẫu nhanh |
|--------------|-----------|
| Đọc một số nguyên / hai số một dòng | `n = int(input())` / `a, b = map(int, input().split())` |
| In kết quả / in kèm chữ | `print(kq)` / `print(f"Tổng là {tong}")` |
| Cộng trừ nhân chia / nguyên, dư | `+ - * /` / `// %` |
| So sánh / kết hợp | `== != > < >= <=` / `and or not` |
| Rẽ nhánh / lặp | `if / elif / else:` / `for i in range(n):` / `while ...:` |
| Dừng hẳn / bỏ lượt này | `break / continue` |
| Tổng / đếm / to nhất, nhỏ nhất | `tong + x` / `dem + 1` / `max(...) min(...)` |
| Danh sách / số lượng | `append(x)` / `len(...)` |


# Phụ lục B: Lời giải bài tập tham khảo


> Phần này cung cấp mã nguồn Python 3 tham khảo hoàn chỉnh cho toàn bộ bài tập trong sách.


## Chương 03 — Bài 07: Quy luật dãy số và tam giác số


### pya_l09_p01_trao_doi_hai_chiec_coc — Tráo đổi hai chiếc cốc


```python
a, b = map(int, input().split())
print(b, a)
```


### pya_l09_p03_so_hang_day_cap_so_cong — Số hạng dãy cấp số cộng


```python
u1, d, n = map(int, input().split())
print(u1 + (n - 1) * d)
```


### pya_l09_p04_so_fibonacci_thu_n — Số Fibonacci thứ N


```python
n = int(input().strip())
a, b = 1, 1
for _ in range(n - 1):
    a, b = b, a + b
print(a)
```


### pya_l09_p06_tong_tich_hai_so_lien_nhau — Tổng tích hai số liền nhau


```python
n = int(input().strip())
s = 0
for i in range(1, n + 1):
    s += i * (i + 1)
print(s)
```


### pya_l09_p08_tam_giac_so_don_gian — Tam giác số đơn giản


```python
n = int(input().strip())
for i in range(1, n + 1):
    print(" ".join(str(j) for j in range(1, i + 1)))
```


### pya_l09_p12_ma_tran_so_ban_co_dan_xen — Ma trận số bàn cờ đan xen


```python
n = int(input())
for i in range(n):
    print(" ".join(str((i + j + 1) % 2) for j in range(n)))
```


### pya_l09_p02_day_so_nhan_doi — Dãy số nhân đôi


```python
n = int(input().strip())
val = 1
res = []
for _ in range(n):
    res.append(str(val))
    val *= 2
print(" ".join(res))
```


### pya_l09_p05_day_so_dan_dau — Dãy số đan dấu


```python
n = int(input().strip())
if n % 2 == 0:
    print(-n // 2)
else:
    print((n + 1) // 2)
```


### pya_l09_p09_tam_giac_sao_can — Tam giác sao cân


```python
n = int(input().strip())
for i in range(1, n + 1):
    spaces = " " * (n - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars)
```


### pya_l09_p10_day_so_tam_giac_triangular_numbers — Dãy số tam giác (triangular numbers)


```python
k = int(input())
n = 1
while n * (n + 1) // 2 < k:
    n += 1
if n * (n + 1) // 2 == k:
    print("YES", n)
else:
    print("NO")
```


### pya_l09_p14_tim_vi_tri_trong_day_tu_nhien_dai — Tìm vị trí trong dãy tự nhiên dài


```python
k = int(input().strip())
length = 1
count = 9
start = 1
while k > length * count:
    k -= length * count
    length += 1
    count *= 10
    start *= 10
num = start + (k - 1) // length
idx = (k - 1) % length
print(str(num)[idx])
```


### pya_l09_p13_tam_giac_floyd — Tam giác Floyd


```python
n = int(input().strip())
cur = 1
for i in range(1, n + 1):
    row = []
    for _ in range(i):
        row.append(str(cur))
        cur += 1
    print(" ".join(row))
```


### pya_l09_p07_day_so_boi_ba_boi_nam — Dãy số bội ba bội năm


```python
n = int(input().strip())
res = []
num = 1
while len(res) < n:
    if num % 3 == 0 or num % 5 == 0:
        res.append(str(num))
    num += 1
print(" ".join(res))
```


### pya_l09_p11_day_so_tribonacci — Dãy số Tribonacci


```python
n = int(input().strip())
a, b, c = 1, 1, 2
if n == 1 or n == 2:
    print(1)
elif n == 3:
    print(2)
else:
    for _ in range(n - 3):
        a, b, c = b, c, a + b + c
    print(c)
```


## Chương 03 — Bài 08: Kỹ thuật tách chữ số và xử lý số nguyên qua vòng lặp while


### pya_l10_p01_lay_chu_so_don_vi_chuc — Lấy chữ số đơn vị & chục


```python
n = int(input())
don_vi = n % 10
temp = n
while temp >= 10:
    temp = temp // 10
chuc = temp
print(chuc, don_vi)
```


### pya_l10_p02_tong_chu_so_cua_so_3_chu_so — Tổng chữ số của số 3 chữ số


```python
n = int(input())
tong = 0
while n > 0:
    tong = tong + n % 10
    n = n // 10
print(tong)
```


### pya_l10_p03_tong_cac_chu_so_cua_n — Tổng các chữ số của N


```python
n = int(input())
tong = 0
while n > 0:
    tong = tong + n % 10
    n = n // 10
print(tong)
```


### pya_l10_p08_so_dao_nguoc — Số đảo ngược


```python
n = int(input())
dao = 0
while n > 0:
    dao = dao * 10 + n % 10
    n = n // 10
print(dao)
```


### pya_l10_p05_tich_cac_chu_so_khac_khong — Tích các chữ số khác không


```python
n = int(input())
tich = 1
while n > 0:
    d = n % 10
    if d != 0:
        tich = tich * d
    n = n // 10
print(tich)
```


### pya_l10_p04_dem_so_luong_chu_so — Đếm số lượng chữ số


```python
n = int(input())
if n == 0:
    print(1)
else:
    dem = 0
    while n > 0:
        du = n % 10
        dem = dem + 1
        n = n // 10
    print(dem)
```


### pya_l10_p09_kiem_tra_so_doi_xung_palindrome — Kiểm tra số đối xứng (palindrome)


```python
n = int(input().strip())
orig = n
rev = 0
while n > 0:
    rev = rev * 10 + n % 10
    n = n // 10
if rev == orig:
    print("YES")
else:
    print("NO")
```


### pya_l10_p13_can_bac_so_hoc_digital_root — Căn bậc số học (digital root)


```python
n = int(input())
while n >= 10:
    tong = 0
    temp = n
    while temp > 0:
        tong = tong + temp % 10
        temp = temp // 10
    n = tong
print(n)
```


### pya_l10_p07_chu_so_lon_nhat_nho_nhat — Chữ số lớn nhất & nhỏ nhất


```python
n = int(input())
lon = -1
nho = 10
while n > 0:
    d = n % 10
    if d > lon:
        lon = d
    if d < nho:
        nho = d
    n = n // 10
print(lon, nho)
```


### pya_l10_p11_so_may_man_chua_so_7 — Số may mắn chứa số 7


```python
n = int(input())
tim_thay = False
while n > 0:
    if n % 10 == 7:
        tim_thay = True
    n = n // 10
if tim_thay:
    print("YES")
else:
    print("NO")
```


### pya_l10_p06_dem_chu_so_chan_va_le — Đếm chữ số chẵn và lẻ


```python
n = int(input())
chan = 0
le = 0
while n > 0:
    d = n % 10
    if d % 2 == 0:
        chan = chan + 1
    else:
        le = le + 1
    n = n // 10
print(chan, le)
```


### pya_l10_p14_so_tang_giam_dep — Số tăng giảm đẹp


```python
n = int(input())
digits = []
while n > 0:
    digits.append(n % 10)
    n //= 10
digits = digits[::-1]
tang = all(digits[i] < digits[i + 1] for i in range(len(digits) - 1))
giam = all(digits[i] > digits[i + 1] for i in range(len(digits) - 1))
if tang:
    print("TANG")
elif giam:
    print("GIAM")
else:
    print("KHONG")
```


### pya_l10_p10_so_toan_chan_hoac_toan_le — Số toàn chẵn hoặc toàn lẻ


```python
n = int(input())
toan_chan = True
toan_le = True
while n > 0:
    d = n % 10
    if d % 2 == 0:
        toan_le = False
    else:
        toan_chan = False
    n = n // 10
if toan_chan:
    print("TOAN CHAN")
elif toan_le:
    print("TOAN LE")
else:
    print("BINH THUONG")
```


### pya_l10_p12_dem_so_luong_so_doi_xung_trong_doan — Đếm số lượng số đối xứng trong đoạn


```python
a, b = map(int, input().split())
dem = 0
for i in range(a, b + 1):
    goc = i
    dao = 0
    temp = i
    while temp > 0:
        dao = dao * 10 + temp % 10
        temp = temp // 10
    if dao == goc:
        dem = dem + 1
print(dem)
```


## Chương 03 — Bài 09: Ước số, Bội số và Số nguyên tố


### pya_l11_p06_uoc_chung_lon_nhat_bcnn — Ước chung lớn nhất & BCNN


```python
a, b = map(int, input().split())
x = a
y = b
while y != 0:
    x, y = y, x % y
gcd = x
lcm = a // gcd * b
print(gcd, lcm)
```


### pya_l11_p02_dem_so_luong_uoc_so — Đếm số lượng ước số


```python
n = int(input())
dem = 0
for i in range(1, n + 1):
    if n % i == 0:
        dem = dem + 1
print(dem)
```


### pya_l11_p03_tinh_tong_cac_uoc_so — Tính tổng các ước số


```python
n = int(input())
tong = 0
for i in range(1, n + 1):
    if n % i == 0:
        tong = tong + i
print(tong)
```


### pya_l11_p10_hai_so_nguyen_to_cung_nhau — Hai số nguyên tố cùng nhau


```python
a, b = map(int, input().split())
x = a
y = b
while y != 0:
    x, y = y, x % y
if x == 1:
    print("YES")
else:
    print("NO")
```


### pya_l11_p01_liet_ke_tat_ca_uoc_so — Liệt kê tất cả ước số


```python
n = int(input())
uoc = []
for i in range(1, n + 1):
    if n % i == 0:
        uoc.append(str(i))
print(" ".join(uoc))
```


### pya_l11_p07_dem_uoc_chan_cua_n — Đếm ước chẵn của N


```python
n = int(input())
dem = 0
for i in range(1, n + 1):
    if n % i == 0 and i % 2 == 0:
        dem = dem + 1
print(dem)
```


### pya_l11_p08_tim_uoc_so_lon_thu_hai — Tìm ước số lớn thứ hai


```python
n = int(input())
ket_qua = 1
for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
        ket_qua = n // i
        break
print(ket_qua)
```


### pya_l11_p05_kiem_tra_so_chinh_phuong — Kiểm tra số chính phương


```python
n = int(input())
r = int(n ** 0.5)
while (r + 1) * (r + 1) <= n:
    r = r + 1
while r * r > n:
    r = r - 1
if r * r == n:
    print("YES")
else:
    print("NO")
```


### pya_l11_p13_phan_tich_ra_thua_so_nguyen_to — Phân tích ra thừa số nguyên tố


```python
n = int(input())
thua_so = []
temp = n
d = 2
while d * d <= temp:
    while temp % d == 0:
        thua_so.append(str(d))
        temp = temp // d
    d = d + 1
if temp > 1:
    thua_so.append(str(temp))
print(" * ".join(thua_so))
```


### pya_l11_p04_kiem_tra_so_nguyen_to — Kiểm tra số nguyên tố


```python
n = int(input())
if n < 2:
    print("NO")
else:
    la_snt = True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            la_snt = False
            break
    if la_snt:
        print("YES")
    else:
        print("NO")
```


### pya_l11_p09_dem_so_nguyen_to_trong_doan — Đếm số nguyên tố trong đoạn


```python
a, b = map(int, input().split())
dem = 0
for num in range(a, b + 1):
    if num < 2:
        continue
    la_snt = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            la_snt = False
            break
    if la_snt:
        dem = dem + 1
print(dem)
```


### pya_l11_p14_tim_so_co_dung_3_uoc_so — Tìm số có đúng 3 ước số


```python
n = int(input())
gioi_han = int(n ** 0.5)
if gioi_han < 2:
    print(0)
else:
    la_snt = [True] * (gioi_han + 1)
    la_snt[0] = False
    la_snt[1] = False
    for i in range(2, int(gioi_han ** 0.5) + 1):
        if la_snt[i]:
            for j in range(i * i, gioi_han + 1, i):
                la_snt[j] = False
    dem = 0
    for i in range(2, gioi_han + 1):
        if la_snt[i]:
            dem = dem + 1
    print(dem)
```


### pya_l11_p12_so_sieu_nguyen_to_super_prime — Số siêu nguyên tố (super prime)


```python
n = int(input())
sieu = True
if n < 2:
    sieu = False
else:
    temp = n
    while temp > 0:
        if temp < 2:
            sieu = False
            break
        la_snt = True
        for i in range(2, int(temp ** 0.5) + 1):
            if temp % i == 0:
                la_snt = False
                break
        if not la_snt:
            sieu = False
            break
        temp = temp // 10
if sieu:
    print("YES")
else:
    print("NO")
```


### pya_l11_p11_cap_so_nguyen_to_sinh_doi — Cặp số nguyên tố sinh đôi


```python
n = int(input())
for p in range(2, n - 1):
    la_snt_p = True
    if p < 2:
        la_snt_p = False
    else:
        for i in range(2, int(p ** 0.5) + 1):
            if p % i == 0:
                la_snt_p = False
                break
    q = p + 2
    la_snt_q = True
    for i in range(2, int(q ** 0.5) + 1):
        if q % i == 0:
            la_snt_q = False
            break
    if la_snt_p and la_snt_q and q <= n:
        print(p, q)
```


## Chương 03 — Bài 10: Đếm số theo quy luật và số đặc biệt


### pya_l12_p01_dem_so_chia_het_cho_k — Đếm số chia hết cho K


```python
n, k = map(int, input().split())
print(n // k)
```


### pya_l12_p07_dem_so_chia_het_cho_2_hoac_3 — Đếm số chia hết cho 2 hoặc 3


```python
n = int(input())
print(n // 2 + n // 3 - n // 6)
```


### pya_l12_p02_dem_so_le_trong_doan — Đếm số lẻ trong đoạn


```python
a, b = map(int, input().split())
print((b + 1) // 2 - a // 2)
```


### pya_l12_p06_dem_boi_cua_3_nhung_khong_chia_het_cho_5 — Đếm bội của 3 nhưng không chia hết cho 5


```python
a, b = map(int, input().split())
dem3 = b // 3 - (a - 1) // 3
dem15 = b // 15 - (a - 1) // 15
print(dem3 - dem15)
```


### pya_l12_p04_so_armstrong_ba_chu_so — Số Armstrong ba chữ số


```python
n = int(input())
tram = n // 100
chuc = (n // 10) % 10
don_vi = n % 10
if tram ** 3 + chuc ** 3 + don_vi ** 3 == n:
    print("YES")
else:
    print("NO")
```


### pya_l12_p12_so_tu_man_narcissistic_number_k_chu_so — Số tự mãn (Narcissistic number K chữ số)


```python
n = int(input())
temp = n
k = 0
while temp > 0:
    k = k + 1
    temp = temp // 10
tong = 0
temp = n
while temp > 0:
    d = temp % 10
    tong = tong + d ** k
    temp = temp // 10
if tong == n:
    print("YES")
else:
    print("NO")
```


### pya_l12_p10_dem_so_khong_chua_chu_so_0 — Đếm số không chứa chữ số 0


```python
n = int(input())
dem = 0
for i in range(1, n + 1):
    temp = i
    co_so_0 = False
    while temp > 0:
        if temp % 10 == 0:
            co_so_0 = True
            break
        temp = temp // 10
    if not co_so_0:
        dem = dem + 1
print(dem)
```


### pya_l12_p03_kiem_tra_so_hoan_hao — Kiểm tra số hoàn hảo


```python
n = int(input())
if n <= 1:
    print("NO")
else:
    tong = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            j = n // i
            if i < n:
                tong = tong + i
            if j != i and j < n:
                tong = tong + j
    if tong == n:
        print("YES")
    else:
        print("NO")
```


### pya_l12_p11_dem_so_chinh_phuong_trong_doan — Đếm số chính phương trong đoạn


```python
a, b = map(int, input().split())
i = int(a ** 0.5)
while i * i < a:
    i = i + 1
while (i - 1) * (i - 1) >= a:
    i = i - 1
j = int(b ** 0.5)
while (j + 1) * (j + 1) <= b:
    j = j + 1
while j * j > b:
    j = j - 1
if j < i:
    print(0)
else:
    print(j - i + 1)
```


### pya_l12_p05_tim_tat_ca_so_hoan_hao_nho_hon_n — Tìm tất cả số hoàn hảo nhỏ hơn N


```python
n = int(input())
ket_qua = []
for num in range(2, n + 1):
    tong = 0
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            j = num // i
            if i < num:
                tong = tong + i
            if j != i and j < num:
                tong = tong + j
    if tong == num:
        ket_qua.append(str(num))
if ket_qua:
    print(" ".join(ket_qua))
```


### pya_l12_p09_so_phong_phu_abundant_number — Số phong phú (abundant number)


```python
n = int(input())
ket_qua = []
for num in range(1, n + 1):
    tong = 0
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            j = num // i
            if i < num:
                tong = tong + i
            if j != i and j < num:
                tong = tong + j
    if tong > num:
        ket_qua.append(str(num))
if ket_qua:
    print(" ".join(ket_qua))
```


### pya_l12_p08_cap_so_than_thiet — Cặp số thân thiết


```python
a, b = map(int, input().split())
tong_a = 0
for i in range(1, int(a ** 0.5) + 1):
    if a % i == 0:
        j = a // i
        if i < a:
            tong_a = tong_a + i
        if j != i and j < a:
            tong_a = tong_a + j
tong_b = 0
for i in range(1, int(b ** 0.5) + 1):
    if b % i == 0:
        j = b // i
        if i < b:
            tong_b = tong_b + i
        if j != i and j < b:
            tong_b = tong_b + j
if a != b and tong_a == b and tong_b == a:
    print("YES")
else:
    print("NO")
```


## Chương 04 — Bài 11: Danh sách và thao tác cơ bản


### pya_l16_p23_thuong_doc_sach — Thưởng đọc sách


```python
n = int(input())
print(n * (n + 1) // 2)
```


### pya_l16_p21_so_ghe_doi_xung — Số ghế đối xứng


```python
s = input().strip()
if s == s[::-1]:
    print("YES")
else:
    print("NO")
```


### pya_l16_p08_tim_vi_tri_dau_tien_cua_x — Tìm vị trí đầu tiên của X


```python
line = input().split()
n, x = int(line[0]), int(line[1])
a = list(map(int, input().split()))
try:
    print(a.index(x))
except ValueError:
    print(-1)
```


### pya_l16_p01_nhap_day_so_in_phan_tu_dau_cuoi — Nhập dãy số & in phần tử đầu - cuối


```python
n = int(input().strip())
a = list(map(int, input().split()))
print(a[0], a[-1])
```


### pya_l16_p03_tinh_tong_cac_phan_tu_trong_day — Tính tổng các phần tử trong dãy


```python
n = int(input().strip())
a = list(map(int, input().split()))
print(sum(a))
```


### pya_l16_p05_tim_so_lon_nhat_nho_nhat — Tìm số lớn nhất & nhỏ nhất


```python
n = int(input().strip())
a = list(map(int, input().split()))
print(max(a), min(a))
```


### pya_l16_p06_in_day_so_theo_thu_tu_dao_nguoc — In dãy số theo thứ tự đảo ngược


```python
n = int(input().strip())
a = list(map(int, input().split()))
print(*(a[::-1]))
```


### pya_l16_p07_dem_so_lan_xuat_hien_cua_x — Đếm số lần xuất hiện của X


```python
line = input().split()
n, x = int(line[0]), int(line[1])
a = list(map(int, input().split()))
print(a.count(x))
```


### pya_l16_p11_thay_the_tat_ca_so_am_bang_so_0 — Thay thế tất cả số âm bằng số 0


```python
n = int(input().strip())
a = list(map(int, input().split()))
res = [0 if x < 0 else x for x in a]
print(*res)
```


### pya_l16_p15_heo_dat_tiet_kiem — Heo đất tiết kiệm


```python
n, a, b = map(int, input().split())
print(n * a + (n // 2) * b)
```


### pya_l16_p04_dem_so_luong_so_chan_trong_mang — Đếm số lượng số chẵn trong mảng


```python
n = int(input().strip())
a = list(map(int, input().split()))
print(sum(1 for x in a if x % 2 == 0))
```


### pya_l16_p02_them_diem_vao_danh_sach — Thêm điểm vào danh sách


```python
a = list(map(int, input().split()))
x = int(input().strip())
a.append(x)
print(*a)
```


### pya_l16_p12_chen_so_vao_vi_tri_k — Chèn số vào vị trí K


```python
n = int(input().strip())
a = list(map(int, input().split()))
line = input().split()
x, k = int(line[0]), int(line[1])
a.insert(k, x)
print(*a)
```


### pya_l16_p18_mat_khau_bi_an — Mật khẩu bị ẩn


```python
s = input()
d = 0
for c in s:
    if "0" <= c <= "9":
        d += 1
print(d)
```


### pya_l16_p22_xep_hang_chieu_cao — Xếp hàng chiều cao


```python
n = int(input())
data = []
while len(data) < n:
    data += list(map(int, input().split()))
data = sorted(data[:n])
print(" ".join(map(str, data)))
```


### pya_l16_p10_xoa_phan_tu_dau_tien_bang_x — Xóa phần tử đầu tiên bằng X


```python
line = input().split()
n, x = int(line[0]), int(line[1])
a = list(map(int, input().split()))
if x in a:
    a.remove(x)
    print(*a)
else:
    print("KHONG CO")
```


### pya_l16_p13_xoay_vong_danh_sach_sang_phai — Xoay vòng danh sách sang phải


```python
line = input().split()
n, k = int(line[0]), int(line[1])
a = list(map(int, input().split()))
k %= n
if k == 0:
    print(*a)
else:
    print(*(a[-k:] + a[:-k]))
```


### pya_l16_p09_tach_mang_chan_va_mang_le — Tách mảng chẵn và mảng lẻ


```python
n = int(input().strip())
a = list(map(int, input().split()))
chan = [x for x in a if x % 2 == 0]
le = [x for x in a if x % 2 != 0]
print(*chan)
print(*le)
```


### pya_l16_p24_dem_tu_dai — Đếm từ dài


```python
k = int(input())
s = input().split()
c = 0
for w in s:
    if len(w) > k:
        c += 1
print(c)
```


### pya_l16_p17_bang_diem_lop_hoc — Bảng điểm lớp học


```python
n = int(input())
data = []
while len(data) < n:
    data += list(map(int, input().split()))
data = data[:n]
print(max(data))
print(min(data))
print(f"{sum(data) / n:.1f}")
```


### pya_l16_p14_cap_so_co_tong_bang_s — Cặp số có tổng bằng S


```python
line = input().split()
n, s = int(line[0]), int(line[1])
a = list(map(int, input().split()))
seen = set()
cnt = 0
for x in a:
    if (s - x) in seen:
        cnt += 1
    seen.add(x)
print(cnt)
```


### pya_l16_p16_ve_so_may_man — Vé số may mắn


```python
s = input().strip()
t = 0
for c in s:
    if "0" <= c <= "9":
        t += ord(c) - ord("0")
if t % 7 == 0:
    print("YES")
else:
    print("NO")
```


### pya_l16_p26_chuyen_tau_vuot_deo — Chuyến tàu vượt đèo


```python
n = int(input())
data = []
while len(data) < n:
    data += list(map(int, input().split()))
data = data[:n]
best = data[0]
c = 1
for x in data[1:]:
    if x > best:
        best = x
        c += 1
print(c)
```


### pya_l16_p20_tong_chu_so_lon_nhat — Tổng chữ số lớn nhất


```python
n = int(input())
data = []
while len(data) < n:
    data += list(map(int, input().split()))
data = data[:n]
best = data[0]
bs = sum(map(int, str(best)))
for x in data[1:]:
    s = sum(map(int, str(x)))
    if s > bs or (s == bs and x < best):
        best = x
        bs = s
print(best)
```


### pya_l16_p19_dem_keo_chan_le — Đếm kẹo chẵn lẻ


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


### pya_l16_p25_dem_sao_nguyen_to — Đếm sao nguyên tố


```python
n = int(input())
if n < 2:
    print(0)
else:
    is_p = [True] * (n + 1)
    is_p[0] = False
    is_p[1] = False
    i = 2
    while i * i <= n:
        if is_p[i]:
            j = i * i
            while j <= n:
                is_p[j] = False
                j += i
        i += 1
    print(sum(is_p))
```


## Chương 04 — Bài 12: Thống kê danh sách và sắp xếp


### pya_l17_p01_diem_so_cao_nhat_thap_nhat — Điểm số cao nhất & thấp nhất


```python
n = int(input().strip())
a = list(map(int, input().split()))
print(max(a), min(a))
```


### pya_l17_p07_loc_bo_cac_so_trung_lap — Lọc bỏ các số trùng lặp


```python
n = int(input().strip())
a = list(map(int, input().split()))
unique = sorted(list(set(a)))
print(*unique)
```


### pya_l17_p09_sap_xep_ten_theo_thu_tu_bang_chu_cai — Sắp xếp tên theo thứ tự bảng chữ cái


```python
n = int(input().strip())
words = input().split()
words.sort()
print(*words)
```


### pya_l17_p13_ghep_hai_day_da_sap_xep — Ghép hai dãy đã sắp xếp


```python
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
res = sorted(a + b)
print(*res)
```


### pya_l17_p06_dem_so_luong_hoc_sinh_tren_diem_trung_binh — Đếm số lượng học sinh trên điểm trung bình


```python
n = int(input().strip())
a = list(map(float, input().split()))
tb = sum(a) / n
print(sum(1 for x in a if x >= tb))
```


### pya_l17_p02_sap_xep_tang_dan_don_gian — Sắp xếp tăng dần đơn giản


```python
n = int(input().strip())
a = list(map(int, input().split()))
a.sort()
print(*a)
```


### pya_l17_p04_sap_xep_giam_dan_bang_xep_hang — Sắp xếp giảm dần bảng xếp hạng


```python
n = int(input().strip())
a = list(map(int, input().split()))
a.sort(reverse=True)
print(*a)
```


### pya_l17_p11_trung_vi_cua_day_so_median — Trung vị của dãy số (Median)


```python
n = int(input().strip())
a = list(map(int, input().split()))
a.sort()
print(a[n // 2])
```


### pya_l17_p05_tim_so_lon_thu_nhi_trong_mang — Tìm số lớn thứ nhì trong mảng


```python
n = int(input().strip())
a = list(map(int, input().split()))
mx = max(a)
candidates = [x for x in a if x < mx]
if candidates:
    print(max(candidates))
else:
    print("KHONG CO")
```


### pya_l17_p03_diem_trung_binh_mon_hoc — Điểm trung bình môn học


```python
n = int(input().strip())
a = list(map(float, input().split()))
tb = sum(a) / n
print(f"{tb:.2f}")
```


### pya_l17_p10_chenh_lech_nho_nhat_giua_hai_so — Chênh lệch nhỏ nhất giữa hai số


```python
n = int(input().strip())
a = list(map(int, input().split()))
a.sort()
min_diff = min(a[i + 1] - a[i] for i in range(n - 1))
print(min_diff)
```


### pya_l17_p12_so_xuat_hien_nhieu_lan_nhat_mode — Số xuất hiện nhiều lần nhất (Mode)


```python
n = int(input().strip())
a = list(map(int, input().split()))
counts = {}
for x in a:
    counts[x] = counts.get(x, 0) + 1
max_c = max(counts.values())
candidates = [k for k, v in counts.items() if v == max_c]
print(min(candidates))
```


### pya_l17_p08_diem_olympic_bo_max_bo_min — Điểm olympic bỏ max bỏ min


```python
n = int(input().strip())
a = list(map(float, input().split()))
a.sort()
trimmed = a[1:-1]
tb = sum(trimmed) / len(trimmed)
print(f"{tb:.2f}")
```


### pya_l17_p14_xep_hang_mua_tra_sua_greedy — Xếp hàng mua trà sữa (Greedy)


```python
n = int(input().split()[0])
cac_so = []
while len(cac_so) < n:
    try:
        cac_so.extend(map(int, input().split()))
    except EOFError:
        break
cac_so = sorted(cac_so)
tong = 0
da_cho = 0
for t in cac_so:
    da_cho = da_cho + t
    tong = tong + da_cho
print(tong)
```


## Chương 05 — Bài 13: Chuỗi ký tự — Chỉ số, cắt lát và duyệt ký tự


### pya_l13_p02_do_dai_cua_chuoi — Độ dài của chuỗi


```python
s = input()
print(len(s))
```


### pya_l13_p03_cat_ba_ky_tu_dau_tien — Cắt ba ký tự đầu tiên


```python
s = input()
print(s[:3])
```


### pya_l13_p04_dao_nguoc_ten_rieng — Đảo ngược tên riêng


```python
s = input()
print(s[::-1])
```


### pya_l13_p08_ky_tu_o_vi_tri_chan — Ký tự Ở vị trí chẵn


```python
s = input()
print(s[::2])
```


### pya_l13_p07_rut_trich_ten_mien_email — Rút trích tên miền email


```python
s = input()
print(s[s.index('@') + 1:])
```


### pya_l13_p01_ky_tu_dau_ky_tu_cuoi — Ký tự đầu & ký tự cuối


```python
s = input()
print(s[0] + ' ' + s[-1])
```


### pya_l13_p11_dich_chuyen_vong_quanh_left_rotation — Dịch chuyển vòng quanh (left rotation)


```python
s = input()
k = int(input())
print(s[k:] + s[:k])
```


### pya_l13_p06_cat_doi_chuoi_ky_tu — Cắt đôi chuỗi ký tự


```python
s = input()
n = len(s) // 2
print(s[:n])
print(s[n:])
```


### pya_l13_p09_hoan_doi_nua_dau_nua_sau — Hoán đổi nửa đầu nửa sau


```python
s = input()
n = len(s) // 2
print(s[n:] + s[:n])
```


### pya_l13_p10_xoa_ky_tu_o_vi_tri_k — Xóa ký tự ở vị trí K


```python
s = input()
k = int(input())
print(s[:k] + s[k + 1:])
```


### pya_l13_p05_kiem_tra_tu_doi_xung_palindrome — Kiểm tra từ đối xứng (palindrome)


```python
s = input()
if s == s[::-1]:
    print('YES')
else:
    print('NO')
```


### pya_l13_p12_chuoi_con_doi_xung_dai_nhat — Chuỗi con đối xứng dài nhất


```python
s = input()
n = len(s)
dai_nhat = 1
for i in range(n):
    for j in range(i + 1, n + 1):
        doan = s[i:j]
        if doan == doan[::-1]:
            if len(doan) > dai_nhat:
                dai_nhat = len(doan)
print(dai_nhat)
```


## Chương 05 — Bài 14: Duyệt chuỗi, biến đổi ký tự và tách từ


### pya_l14_p02_chuyen_toan_bo_thanh_chu_hoa — Chuyển toàn bộ thành chữ hoa


```python
s = input()
print(s.upper())
```


### pya_l14_p08_thay_the_ky_tu_bi_mat — Thay thế ký tự bí mật


```python
s = input()
print(s.replace(' ', '_'))
```


### pya_l14_p09_xoa_bo_toan_bo_dau_cach — Xóa bỏ toàn bộ dấu cách


```python
s = input()
print(s.replace(' ', ''))
```


### pya_l15_p03_ma_ascii_cua_ky_tu — Mã ASCII của ký tự


```python
ch = input().strip()
print(ord(ch))
```


### pya_l15_p01_dem_so_tu_trong_cau — Đếm số từ trong câu


```python
s = input()
words = s.split()
print(len(words))
```


### pya_l15_p05_tim_tu_dai_nhat_trong_cau — Tìm từ dài nhất trong câu


```python
s = input()
words = s.split()
longest = max(words, key=len)
print(longest)
```


### pya_l15_p04_ky_tu_ke_tiep_trong_bang_chu_cai — Ký tự kế tiếp trong bảng chữ cái


```python
ch = input().strip()
print(chr(ord(ch) + 1))
```


### pya_l15_p02_tu_dau_tien_tu_cuoi_cung — Từ đầu tiên & từ cuối cùng


```python
s = input()
words = s.split()
print(words[0])
print(words[-1])
```


### pya_l15_p06_chuan_hoa_khoang_trang — Chuẩn hóa khoảng trắng


```python
s = input()
print(" ".join(s.split()))
```


### pya_l14_p01_in_tung_chu_cai_xuong_dong — In từng chữ cái xuống dòng


```python
s = input()
for ch in s:
    print(ch)
```


### pya_l15_p07_viet_hoa_chu_cai_dau_moi_tu_title_case — Viết hoa chữ cái đầu mỗi từ (title case)


```python
s = input()
words = [w.capitalize() for w in s.split()]
print(" ".join(words))
```


### pya_l15_p08_dao_nguoc_tung_tu_trong_cau — Đảo ngược từng từ trong câu


```python
s = input()
words = [w[::-1] for w in s.split()]
print(" ".join(words))
```


### pya_l15_p12_mat_ma_thay_the_hoan_vi_anagram — Mật mã thay thế hoán vị (anagram)


```python
s1 = input().strip()
s2 = input().strip()
if sorted(s1) == sorted(s2):
    print("YES")
else:
    print("NO")
```


### pya_l15_p11_tu_xuat_hien_nhieu_nhat_trong_doan — Từ xuất hiện nhiều nhất trong đoạn


```python
s = input()
words = s.split()
counts = {}
for w in words:
    counts[w] = counts.get(w, 0) + 1
best_word = max(counts, key=counts.get)
print(best_word, counts[best_word])
```


### pya_l14_p10_dem_so_luong_nguyen_am — Đếm số lượng nguyên âm


```python
s = input()
dem = 0
for ch in s:
    if ch in 'AEIOUaeiou':
        dem = dem + 1
print(dem)
```


### pya_l14_p03_dem_ky_tu_a_ca_hoa_lan_thuong — Đếm ký tự 'A' (cả hoa lẫn thường)


```python
s = input()
dem = 0
for ch in s:
    if ch == 'a' or ch == 'A':
        dem = dem + 1
print(dem)
```


### pya_l14_p06_tinh_tong_cac_chu_so_trong_chuoi — Tính tổng các chữ số trong chuỗi


```python
s = input()
tong = 0
for ch in s:
    if ch.isdigit():
        tong = tong + int(ch)
print(tong)
```


### pya_l14_p05_tach_rieng_chu_so_ra_khoi_van_ban — Tách riêng chữ số ra khỏi văn bản


```python
s = input()
kq = ''
for ch in s:
    if ch.isdigit():
        kq = kq + ch
if kq == '':
    print('KHONG CO')
else:
    print(kq)
```


### pya_l14_p11_nen_chuoi_ky_tu_runlength_encoding — Nén chuỗi ký tự (Run-Length encoding)


```python
s = input()
kq = ''
dem = 1
for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        dem = dem + 1
    else:
        kq = kq + s[i - 1] + str(dem)
        dem = 1
kq = kq + s[-1] + str(dem)
print(kq)
```


### pya_l14_p04_dem_chu_cai_in_hoa_in_thuong — Đếm chữ cái in hoa & in thường


```python
s = input()
hoa = 0
thuong = 0
for ch in s:
    if ch.isupper():
        hoa = hoa + 1
    elif ch.islower():
        thuong = thuong + 1
print(str(hoa) + ' ' + str(thuong))
```


### pya_l15_p09_mat_ma_caesar_dich_chuyen_k — Mật mã Caesar dịch chuyển K


```python
s = input().strip()
k = int(input().strip())
res = []
for ch in s:
    if 'A' <= ch <= 'Z':
        res.append(chr((ord(ch) - ord('A') + k) % 26 + ord('A')))
    else:
        res.append(ch)
print("".join(res))
```


### pya_l15_p10_giai_ma_mat_thu_caesar — Giải mã mật thư Caesar


```python
s = input().strip()
k = int(input().strip())
res = []
for ch in s:
    if 'A' <= ch <= 'Z':
        res.append(chr((ord(ch) - ord('A') - k) % 26 + ord('A')))
    else:
        res.append(ch)
print("".join(res))
```


### pya_l14_p07_doi_chu_hoa_thanh_thuong_nguoc_lai — Đổi chữ hoa thành thường & ngược lại


```python
s = input()
kq = ''
for ch in s:
    if ch.isupper():
        kq = kq + ch.lower()
    elif ch.islower():
        kq = kq + ch.upper()
    else:
        kq = kq + ch
print(kq)
```


### pya_l14_p12_trich_xuat_so_lon_nhat_trong_van_ban — Trích xuất số lớn nhất trong văn bản


```python
s = input()
lon_nhat = -1
so_hien_tai = ''
for ch in s + ' ':
    if ch.isdigit():
        so_hien_tai = so_hien_tai + ch
    else:
        if so_hien_tai != '':
            if int(so_hien_tai) > lon_nhat:
                lon_nhat = int(so_hien_tai)
            so_hien_tai = ''
print(lon_nhat)
```


# Mục lục

