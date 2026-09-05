# Bài 09: Ước số, Bội số và Số nguyên tố

## 1. Khái niệm & Nền tảng Số học trong lập trình

Trong cấu trúc đề thi và lập trình thuật toán, các khái niệm **Ước số**, **Bội số**, **Số nguyên tố** và **Số chính phương** tạo nên trục kiến thức toán - tin trọng yếu.

Mục tiêu cốt lõi của bài học:
* Hiểu sâu sắc bản chất toán học của phép chia hết: $A \vdots B \iff A \% B == 0$.
* Tối ưu hóa thuật toán từ tư duy ngây thơ sang thuật toán căn bậc hai $\mathcal{O}(\sqrt{N})$ để chạy nhanh hơn.
* Khai thác triệt để mối quan hệ giữa Ước chung lớn nhất ($\gcd$) và Bội chung nhỏ nhất ($\text{lcm}$).
* Cài đặt thành thạo các hàm kiểm tra nguyên tố, phân tích thừa số nguyên tố phổ biến.

---

## 2. Số nguyên tố và Thuật toán tối ưu $\mathcal{O}(\sqrt{N})$

### 2.1. Định nghĩa chuẩn số học
* **Số nguyên tố:** Là số tự nhiên **lớn hơn 1** và chỉ có **đúng hai ước số nguyên dương** là 1 và chính nó ($2, 3, 5, 7, 11, 13, 17, 19, \dots$).
* **Hợp số:** Là số tự nhiên lớn hơn 1 và có nhiều hơn hai ước số ($4, 6, 8, 9, 10, \dots$).
* **Lưu ý tử huyệt:** Số $0$ và số $1$ **KHÔNG PHẢI** là số nguyên tố và cũng **KHÔNG PHẢI** là hợp số! Số $2$ là số nguyên tố nhỏ nhất và là số nguyên tố chẵn duy nhất.

### 2.2. Định lý Căn bậc hai
* **Ý tưởng ngây thơ $\mathcal{O}(N)$:** Duyệt tất cả các số $i$ từ $2$ đến $N - 1$. Nếu $N$ chia hết cho bất kỳ số nào thì $N$ không phải nguyên tố.
  $\implies$ Nếu $N = 10^9$, thuật toán tốn $10^9$ phép tính, chạy mất khoảng 10 giây — quá chậm!
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

## 7. Tử huyệt và Bẫy lỗi lập trình kinh điển

> ❌ **BẪY LỖI 1: BỎ QUÊN TRƯỜNG HỢP $N < 2$**
> * Rất nhiều học sinh viết vòng lặp kiểm tra từ $2$ mà quên mất số $0$, số $1$ và các số âm.
> * Kết quả: Khi $N = 1$ hoặc $N = 0$, chương trình kết luận là số nguyên tố $\implies$ Sai đề bài hoàn toàn!
> * **Bắt buộc:** Luôn có nhánh `if n < 2: return False` ở đầu hàm kiểm tra.

> ❌ **BẪY LỖI 2: DÙNG `range(2, int(n**0.5))` MÀ QUÊN CỘNG 1**
> * Vì `range` loại trừ cận trên, nếu viết `range(2, int(n**0.5))` thì với $N = 4$ ($int(\sqrt{4}) = 2$), vòng lặp `range(2, 2)` rỗng (không chạy) và kết luận 4 là số nguyên tố!
> * **Chuẩn mực:** Dùng vòng lặp `while i * i <= n:` vừa an toàn tuyệt đối, vừa không bị sai lệch số thực của phép căn bậc hai.

> ❌ **BẪY LỖI 3: TRÀN BỘ NHỚ KHI TÍNH BCNN TRƯỚC KHI CHIA**
> * Dù Python tự động hỗ trợ số lớn (BigInt), việc viết `(a * b) // gcd(a, b)` có thể tạo ra số tích trung gian cực lớn.
> * **Cách viết chuẩn hóa:** `(a // math.gcd(a, b)) * b`.

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

## 9. Concept Quiz: 16 câu trắc nghiệm kiểm tra sâu khái niệm

#### Câu 1 (Định nghĩa số nguyên tố):
Số nào sau đây là số nguyên tố nhỏ nhất?
- **A.** 0
- **B.** 1
- **C.** **[Đáp án đúng]** 2
- **D.** 3
> *Giải thích:* Số 2 là số nguyên tố nhỏ nhất và là số nguyên tố chẵn duy nhất.

#### Câu 2 (Bẫy số 1):
Số 1 có phải là số nguyên tố không?
- **A.** Có, vì nó chỉ chia hết cho 1
- **B.** **[Đáp án đúng]** Không, vì số nguyên tố theo định nghĩa phải lớn hơn 1 và có đúng 2 ước số phân biệt
- **C.** Là số nguyên tố đặc biệt
- **D.** Tùy trường hợp
> *Giải thích:* Bẫy kinh điển: Số 1 chỉ có đúng 1 ước duy nhất nên không thỏa mãn định nghĩa có đúng 2 ước phân biệt.

#### Câu 3 (Tính chất số chính phương):
Một số tự nhiên có tổng số lượng ước là một số lẻ thì số đó chắc chắn là:
- **A.** Số lẻ
- **B.** Số nguyên tố
- **C.** **[Đáp án đúng]** Số chính phương
- **D.** Số chẵn
> *Giải thích:* Các ước luôn đi theo cặp $(d, N/d)$. Chỉ có số chính phương tại vị trí căn bậc hai $d = \sqrt{N}$ mới tạo ra 1 ước đơn, khiến tổng số ước bị lẻ.

#### Câu 4 (Số ước của số 12):
Số 12 có tất cả bao nhiêu ước số nguyên dương?
- **A.** 4
- **B.** **[Đáp án đúng]** 6 (gồm 1, 2, 3, 4, 6, 12)
- **C.** 5
- **D.** 8
> *Giải thích:* Các ước là 1, 2, 3, 4, 6, 12.

#### Câu 5 (Độ phức tạp kiểm tra nguyên tố tối ưu):
Để kiểm tra tính nguyên tố của số $N$, ta chỉ cần duyệt các ước tiềm năng đến:
- **A.** $N - 1$
- **B.** $N // 2$
- **C.** **[Đáp án đúng]** $\sqrt{N}$ (với điều kiện `i * i <= N`)
- **D.** $N // 10$
> *Giải thích:* Theo định lý căn bậc hai, nếu $N$ là hợp số thì chắc chắn có ước $\le \sqrt{N}$.

#### Câu 6 (Nhận diện số nguyên tố):
Số nào sau đây là số nguyên tố?
- **A.** 9
- **B.** 15
- **C.** 21
- **D.** **[Đáp án đúng]** 29
> *Giải thích:* 29 chỉ chia hết cho 1 và 29.

#### Câu 7 (Hàm tính ƯCLN trong Python):
Hàm dựng sẵn nào trong thư viện `math` dùng để tính Ước chung lớn nhất của 2 số `a` và `b`?
- **A.** `math.max(a, b)`
- **B.** **[Đáp án đúng]** `math.gcd(a, b)`
- **C.** `math.lcm(a, b)`
- **D.** `math.ucln(a, b)`
> *Giải thích:* `gcd` là viết tắt của *Greatest Common Divisor*.

#### Câu 8 (Mối quan hệ giữa ƯCLN và BCNN):
Cho hai số nguyên dương $A$ và $B$. Công thức tính BCNN từ ƯCLN là:
- **A.** `(A + B) // math.gcd(A, B)`
- **B.** **[Đáp án đúng]** `(A * B) // math.gcd(A, B)`
- **C.** `(A * B) * math.gcd(A, B)`
- **D.** `A // math.gcd(A, B)`
> *Giải thích:* $\text{lcm}(A, B) = \frac{A \times B}{\gcd(A, B)}$.

#### Câu 9 (Hai số nguyên tố cùng nhau):
Hai số nguyên $A$ và $B$ được gọi là nguyên tố cùng nhau khi:
- **A.** Cả hai số đều là số nguyên tố
- **B.** **[Đáp án đúng]** $\gcd(A, B) == 1$
- **C.** $A + B$ là số nguyên tố
- **D.** $A$ chia hết cho $B$
> *Giải thích:* Hai số nguyên tố cùng nhau khi chúng không có ước chung nào khác ngoài số 1.

#### Câu 10 (Số chính phương nhỏ hơn 50):
Có bao nhiêu số chính phương dương nhỏ hơn 50?
- **A.** 5
- **B.** 6
- **C.** **[Đáp án đúng]** 7 (gồm 1, 4, 9, 16, 25, 36, 49)
- **D.** 8
> *Giải thích:* $1^2, 2^2, 3^2, 4^2, 5^2, 6^2, 7^2$ đều $\le 49 < 50$.

#### Câu 11 (Kiểm tra số chính phương):
Để kiểm tra một số nguyên dương $N$ có phải là số chính phương hay không, điều kiện nào sau đây chuẩn nhất?
- **A.** `int(N ** 0.5) == N // 2`
- **B.** **[Đáp án đúng]** `int(N ** 0.5) ** 2 == N`
- **C.** `N % 4 == 0`
- **D.** `N % 2 == 0`
> *Giải thích:* Lấy phần nguyên căn bậc 2 rồi bình phương lên, nếu bằng lại chính $N$ thì $N$ là số chính phương.

#### Câu 12 (Số nguyên tố chẵn duy nhất):
Số nguyên tố chẵn duy nhất trong tập hợp số tự nhiên là:
- **A.** 0
- **B.** **[Đáp án đúng]** 2
- **C.** 4
- **D.** Không có số nguyên tố chẵn
> *Giải thích:* Mọi số chẵn lớn hơn 2 đều chia hết cho 2 nên đều là hợp số.

#### Câu 13 (Cặp số nguyên tố sinh đôi):
Hai số nguyên tố hơn kém nhau 2 đơn vị được gọi là cặp số nguyên tố sinh đôi. Cặp nào sau đây là số nguyên tố sinh đôi?
- **A.** 1 và 3
- **B.** 7 và 9
- **C.** **[Đáp án đúng]** 11 và 13
- **D.** 15 và 17
> *Giải thích:* 11 và 13 đều là số nguyên tố và $13 - 11 = 2$.

#### Câu 14 (Ước thực sự):
Ước thực sự của một số $N$ là các ước nhỏ hơn $N$. Tổng các ước thực sự của số 6 là:
- **A.** 5
- **B.** **[Đáp án đúng]** 6 (gồm 1, 2, 3: $1 + 2 + 3 = 6$)
- **C.** 12
- **D.** 3
> *Giải thích:* Các ước thực sự của 6 là 1, 2, 3. Tổng $= 6$.

#### Câu 15 (Số hoàn hảo - Perfect Number):
Một số bằng tổng các ước thực sự của nó được gọi là số hoàn hảo. Số hoàn hảo nhỏ nhất là:
- **A.** 1
- **B.** **[Đáp án đúng]** 6
- **C.** 12
- **D.** 28
> *Giải thích:* $1 + 2 + 3 = 6$. Số hoàn hảo tiếp theo là 28 ($1 + 2 + 4 + 7 + 14 = 28$).

#### Câu 16 (Độ phức tạp kiểm tra 1000 số):
Nếu dùng thuật toán $\mathcal{O}(\sqrt{N})$ để kiểm tra tính nguyên tố của 1000 số, mỗi số $N \le 10^6$, tổng số phép tính xấp xỉ là:
- **A.** $10^9$ phép tính (quá thời gian)
- **B.** **[Đáp án đúng]** $1000 \times 1000 = 10^6$ phép tính (chạy trong $0.05\text{s}$)
- **C.** $10^{12}$ phép tính
- **D.** $1000$ phép tính
> *Giải thích:* Mỗi số tốn $\sqrt{10^6} = 1000$ phép tính. $1000 \times 1000 = 10^6$ phép tính, máy tính thực thi trong tích tắc.
