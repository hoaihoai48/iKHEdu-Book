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
