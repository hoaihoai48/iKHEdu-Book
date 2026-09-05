# Bài 08: Kỹ thuật tách chữ số và xử lý số nguyên qua vòng lặp while

## 1. Khái niệm & Tầm quan trọng của Xử lý chữ số trong lập trình thi đấu

Trong các kỳ thi lập trình, các bài toán xoay quanh **chữ số của một số nguyên** xuất hiện với tần suất dày đặc:
* Tính tổng, tích các chữ số.
* Đếm số lượng chữ số thỏa mãn tính chất (chẵn, lẻ, nguyên tố, chia hết).
* Tìm chữ số lớn nhất, chữ số nhỏ nhất, chữ số đầu tiên bên trái.
* Tạo số đảo ngược và kiểm tra số đối xứng.
* Kiểm tra số may mắn, số Armstrong, số tự mãn.

Bản chất cốt lõi của dạng toán này là: **Mỗi số nguyên trong hệ thập phân được cấu tạo từ các lũy thừa của 10**. Để bóc tách từng chữ số mà không làm tràn bộ nhớ hay phụ thuộc vào chuỗi ký tự, ta sử dụng cặp toán tử chia nguyên `//` và chia dư `%` cho 10 kết hợp với vòng lặp `while`.

---

## 2. Cặp toán tử "Thần thánh": `// 10` và `% 10`

### 2.1. Phép toán `N % 10` (Bóc chữ số hàng đơn vị)
Khi chia một số nguyên cho 10, phần dư thu được **chính xác là chữ số tận cùng bên phải** của số đó:
* $2026 \% 10 = \mathbf{6}$
* $789 \% 10 = \mathbf{9}$
* $5 \% 10 = \mathbf{5}$

### 2.2. Phép toán `N // 10` (Cắt bỏ chữ số hàng đơn vị)
Khi chia nguyên một số cho 10, phần thập phân bị loại bỏ, nghĩa là ta **vứt bỏ chữ số tận cùng bên phải** để thu gọn số lại:
* $2026 // 10 = \mathbf{202}$
* $789 // 10 = \mathbf{78}$
* $5 // 10 = \mathbf{0}$

---

## 3. Khung thuật toán chuẩn bóc tách chữ số

Bằng cách lặp lại liên tục hai thao tác trên trong vòng lặp `while N > 0:`, ta có thể duyệt qua từng chữ số của $N$ từ **phải sang trái** (từ hàng đơn vị lên hàng chục, hàng trăm, ...):

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
Một số nguyên được gọi là **số đối xứng** nếu đọc từ trái sang phải hay từ phải sang trái đều như nhau (ví dụ: $121, 1331, 2002, 7$).
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

## 6. Tử huyệt và Bẫy lỗi lập trình kinh điển

> ❌ **BẪY LỖI 1: QUÊN LƯU LẠI GIÁ TRỊ GỐC CỦA BIẾN $N$**
> * Khi chạy xong vòng lặp `while n > 0:`, biến `n` đã bị giảm dần về `0`.
> * Nếu sau đó học sinh viết `if dao == n:` thì chương trình luôn so sánh `dao` với `0` $\implies$ Sai kết quả hoàn toàn!
> * **Quy tắc:** Luôn gán một biến phụ lưu giá trị ban đầu: `goc = n` trước khi bước vào vòng lặp tách chữ số.

> ❌ **BẪY LỖI 2: QUÊN XỬ LÝ TRƯỜNG HỢP BIÊN $N = 0$**
> * Nếu $N = 0$, điều kiện `while n > 0:` sai ngay từ đầu nên vòng lặp không chạy bước nào.
> * Với bài toán "Đếm số chữ số", chương trình sẽ in ra `0` (sai vì số 0 có đúng 1 chữ số).
> * **Khắc phục:** Thêm kiểm tra đầu vào: `if n == 0: print(1)`.

> ❌ **BẪY LỖI 3: DÙNG KIỂU CHUỖI ĐỂ TÍNH TOÁN SỐ HỌC KHI ĐỀ YÊU CẦU THUẬT TOÁN SỐ**
> * Dù có thể viết `s = str(n)` để làm việc với chuỗi, nhưng việc làm chủ cặp phép toán `//` và `%` là chuẩn mực tư duy thuật toán cốt lõi của lập trình thi đấu, giúp code chạy nhanh hơn và sẵn sàng chuyển giao sang các ngôn ngữ khác (C++, Java).

---

## 7. Mẫu code chuẩn thi đấu

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

## 8. Concept Quiz: 16 câu trắc nghiệm kiểm tra sâu khái niệm

#### Câu 1 (Toán tử lấy chữ số cuối):
Phép toán nào sau đây dùng để lấy ra chữ số hàng đơn vị của số nguyên dương $N$?
- **A.** `N // 10`
- **B.** **[Đáp án đúng]** `N % 10`
- **C.** `N / 10`
- **D.** `N ** 10`
> *Giải thích:* Chia dư cho 10 luôn trả về chữ số hàng đơn vị.

#### Câu 2 (Toán tử cắt chữ số cuối):
Để loại bỏ chữ số tận cùng của số nguyên $N = 2026$ và nhận lại $202$, ta dùng lệnh:
- **A.** **[Đáp án đúng]** `N = N // 10`
- **B.** `N = N % 10`
- **C.** `N = N - 6`
- **D.** `N = N / 10`
> *Giải thích:* Chia nguyên cho 10 làm biến số mất đi chữ số hàng đơn vị.

#### Câu 3 (Thứ tự tách chữ số):
Khi sử dụng vòng lặp `while n > 0:` với phép `% 10`, các chữ số của $N$ được tách ra theo thứ tự nào?
- **A.** Từ trái sang phải
- **B.** **[Đáp án đúng]** Từ phải sang trái (từ hàng đơn vị lên các hàng cao hơn)
- **C.** Ngẫu nhiên
- **D.** Tăng dần theo giá trị
> *Giải thích:* Phép chia dư `% 10` luôn bóc chữ số tận cùng bên phải trước.

#### Câu 4 (Công thức tạo số đảo ngược):
Mỗi khi tách được chữ số mới `d`, công thức để ghép `d` vào số đảo ngược `dao` là:
- **A.** `dao = dao + d`
- **B.** **[Đáp án đúng]** `dao = dao * 10 + d`
- **C.** `dao = dao + d * 10`
- **D.** `dao = dao * d + 10`
> *Giải thích:* Dịch số cũ sang trái 1 hàng (nhân 10) rồi cộng chữ số mới vào hàng đơn vị.

#### Câu 5 (Định nghĩa số đối xứng - Palindrome):
Số nào sau đây là số đối xứng?
- **A.** 1234
- **B.** 2026
- **C.** **[Đáp án đúng]** 12321
- **D.** 12210
> *Giải thích:* 12321 đọc xuôi hay ngược đều là 12321.

#### Câu 6 (Điều kiện dừng của vòng lặp tách chữ số):
Vòng lặp `while n > 0:` dùng để tách chữ số sẽ dừng lại khi nào?
- **A.** Khi $n = 1$
- **B.** **[Đáp án đúng]** Khi $n = 0$
- **C.** Khi gặp chữ số 0
- **D.** Không bao giờ dừng
> *Giải thích:* Sau nhiều lần chia nguyên cho 10, số $n$ sẽ giảm về 0 và làm điều kiện $n > 0$ thành `False`.

#### Câu 7 (Tổng chữ số của 987):
Tổng các chữ số của số nguyên $N = 987$ là:
- **A.** 21
- **B.** **[Đáp án đúng]** 24
- **C.** 25
- **D.** 27
> *Giải thích:* $9 + 8 + 7 = 24$.

#### Câu 8 (Bẫy mất giá trị biến n):
Sau khi chạy xong đoạn code sau, giá trị của biến `n` là bao nhiêu?
```python
n = 567
s = 0
while n > 0:
    s += n % 10
    n //= 10
```
- **A.** 567
- **B.** 5
- **C.** **[Đáp án đúng]** 0
- **D.** 18
> *Giải thích:* Vòng lặp dừng lại khi $n = 0$, do đó giá trị cuối cùng của biến `n` là 0.

#### Câu 9 (Đếm số chữ số chẵn):
Trong số $N = 24578$, có bao nhiêu chữ số chẵn?
- **A.** 2
- **B.** **[Đáp án đúng]** 3 (các chữ số 2, 4, 8)
- **C.** 4
- **D.** 5
> *Giải thích:* Các chữ số chia hết cho 2 là 2, 4, 8.

#### Câu 10 (Trường hợp biên số 0):
Nếu đầu vào là số $N = 0$, thuật toán `while n > 0: dem += 1; n //= 10` sẽ cho kết quả `dem` bằng bao nhiêu?
- **A.** 1
- **B.** **[Đáp án đúng]** 0 (sai với thực tế vì số 0 có 1 chữ số)
- **C.** Báo lỗi
- **D.** Vô tận
> *Giải thích:* $0 > 0$ sai ngay từ đầu nên vòng lặp không chạy. Vì thế cần xử lý riêng nếu $N = 0$.

#### Câu 11 (Tích các chữ số):
Tích các chữ số của số $N = 205$ là bao nhiêu?
- **A.** 10
- **B.** **[Đáp án đúng]** 0
- **C.** 7
- **D.** 25
> *Giải thích:* $2 \times 0 \times 5 = 0$ (vì có chữ số 0).

#### Câu 12 (Tách số có 2 chữ số không dùng vòng lặp):
Cho số nguyên dương $N$ có đúng 2 chữ số. Chữ số hàng chục được tính bằng:
- **A.** `N % 10`
- **B.** **[Đáp án đúng]** `N // 10`
- **C.** `N // 100`
- **D.** `N - 10`
> *Giải thích:* Với số có 2 chữ số, chia nguyên cho 10 sẽ thu được ngay chữ số hàng chục.

#### Câu 13 (Số đảo ngược của số có chữ số tận cùng bằng 0):
Số đảo ngược theo dạng toán học của số $N = 350$ là:
- **A.** 053
- **B.** **[Đáp án đúng]** 53
- **C.** 35
- **D.** 350
> *Giải thích:* $0 \times 100 + 5 \times 10 + 3 = 53$.

#### Câu 14 (Chữ số đầu tiên bên trái):
Để tìm chữ số đầu tiên bên trái (hàng cao nhất) của số $N$, ta:
- **A.** Lấy $N \% 10$ ngay từ đầu
- **B.** **[Đáp án đúng]** Chia nguyên cho 10 liên tục cho đến khi $N < 10$
- **C.** Lấy $N // 10$ một lần duy nhất
- **D.** Nhân $N$ với 10
> *Giải thích:* Chữ số còn sót lại cuối cùng khi $N < 10$ chính là chữ số đầu tiên bên trái.

#### Câu 15 (Số may mắn Lucky Number):
Một số được gọi là số may mắn nếu tổng các chữ số của nó chia hết cho 9. Số nào sau đây là số may mắn?
- **A.** 125
- **B.** 341
- **C.** **[Đáp án đúng]** 468
- **D.** 555
> *Giải thích:* $4 + 6 + 8 = 18$ chia hết cho 9.

#### Câu 16 (Độ phức tạp thuật toán tách chữ số):
Số nguyên $N$ có độ dài $d$ chữ số. Vòng lặp `while n > 0: n //= 10` sẽ chạy bao nhiêu bước?
- **A.** $\mathcal{O}(N)$ bước
- **B.** **[Đáp án đúng]** $\mathcal{O}(\log_{10} N)$ bước (đúng $d$ bước)
- **C.** $\mathcal{O}(1)$ bước
- **D.** $\mathcal{O}(N^2)$ bước
> *Giải thích:* Mỗi bước số $N$ giảm đi 10 lần, do đó số bước lặp tỉ lệ thuận với số chữ số $d \approx \log_{10} N$.
