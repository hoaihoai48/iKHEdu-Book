# Bài 10: Đếm số theo quy luật và số đặc biệt

## 1. Bài toán đếm — Nền tảng tư duy thuật toán

Trong lập trình, bài toán **đếm** là một trong những dạng xuất hiện nhiều nhất. Mục tiêu luôn là: *cho một tập hợp số, hãy đếm xem có bao nhiêu số thỏa mãn điều kiện nhất định*.

Có hai phương pháp tiếp cận chính:
- **Phương pháp duyệt:** Dùng vòng lặp `for` kiểm tra từng số một. Đơn giản nhưng chậm khi tập số lớn.
- **Phương pháp công thức toán học $\mathcal{O}(1)$:** Tính toán trực tiếp bằng công thức, không cần duyệt. Nhanh hơn vạn lần nhưng đòi hỏi hiểu sâu bản chất số học.

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

Để đếm bội số của $K$ trong đoạn $[A, B]$, ta sử dụng **kỹ thuật trừ tiền tố**:
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

> ⚠️ **Lưu ý quan trọng:** Phải dùng $(A - 1)$ chứ không phải $A$. Nếu dùng $A$, sẽ bỏ sót trường hợp $A$ chính nó là bội của $K$.

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

Nếu cộng trực tiếp số bội của $2$ và số bội của $3$, ta sẽ **đếm lặp** các số chia hết cho cả $2$ và $3$ (tức là bội của $6$). Công thức đúng:

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

> 💡 **Mẹo nhớ:** BCNN$(2, 3) = 6$. Chia hết cho cả $2$ **và** $3$ tức là chia hết cho BCNN của chúng.

---

## 4. Số đặc biệt — Khám phá các quy luật ẩn giấu

### 4.1. Số hoàn hảo

Một số tự nhiên $N > 1$ được gọi là **số hoàn hảo** nếu tổng tất cả các ước nhỏ hơn nó đúng bằng chính nó.

**Ví dụ:** $6 = 1 + 2 + 3$ (các ước nhỏ hơn $6$ là $1, 2, 3$).

| Số | Các ước nhỏ hơn nó | Tổng ước | Hoàn hảo? |
|---|---|---|---|
| $6$ | $1, 2, 3$ | $6$ | ✅ Đúng bằng $6$ |
| $12$ | $1, 2, 3, 4, 6$ | $16$ | ❌ Lớn hơn $12$ |
| $28$ | $1, 2, 4, 7, 14$ | $28$ | ✅ Đúng bằng $28$ |

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

> ⚠️ **Lưu ý:** Dùng `int(n ** 0.5)` thay vì `round(n ** 0.5)` để tránh lỗi làm tròn. Sau đó kiểm tra bằng phép nhân `k * k == n`, **tuyệt đối không dùng** `n ** 0.5 == int(n ** 0.5)` vì sai số số thực.

**Dãy số chính phương đầu tiên:** $1, 4, 9, 16, 25, 36, 49, 64, 81, 100, \dots$

**Tính chất đặc biệt của chữ số tận cùng:** Bình phương của số tự nhiên chỉ tận cùng bằng: $0, 1, 4, 5, 6, 9$. **Không bao giờ** tận cùng bằng $2, 3, 7, 8$.

### 4.4. Số Armstrong

Một số $N$ có $d$ chữ số được gọi là **số Armstrong bậc $d$** nếu tổng lũy thừa bậc $d$ của từng chữ số bằng chính nó.

**Ví dụ:** $153$ có $3$ chữ số: $1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153$. ✅

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

## 6. Tử huyệt và Bẫy lỗi lập trình kinh điển

### 6.1. Bẫy 1: Quên trừ $1$ trong công thức đếm đoạn $[A, B]$

```python
# ❌ SAI: Dùng A thay vì A-1
count = b // k - a // k  # Bỏ sót khi A chia hết cho K

# ✅ ĐÚNG:
count = b // k - (a - 1) // k
```

**Ví dụ:** $A = 6, B = 12, K = 6$. Kết quả đúng: $2$ (gồm $6, 12$). Nếu dùng $A$ thay $A-1$: $(12 \mathbin{//} 6) - (6 \mathbin{//} 6) = 2 - 1 = 1$. ❌ Thiếu!

### 6.2. Bẫy 2: Kiểm tra số chính phương bằng so sánh số thực

```python
# ❌ SAI: Sai số số thực làm kết quả sai
import math
if math.sqrt(n) == int(math.sqrt(n)):  # SAI!

# ✅ ĐÚNG: Dùng phép nhân nguyên
k = int(n ** 0.5)
if k * k == n:  # Chính xác 100%
```

### 6.3. Bẫy 3: Duyệt ước quên bắt đầu từ $1$ (không phải $0$)

```python
# ❌ SAI: ZeroDivisionError vì n % 0 gây lỗi
for i in range(0, n):
    if n % i == 0: ...

# ✅ ĐÚNG: Bắt đầu từ 1
for i in range(1, n):
    if n % i == 0:
        tong_uoc += i
```

### 6.4. Bẫy 4: Nhầm lẫn "chia hết cho cả A và B" với "chia hết cho A hoặc B"

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

## 8. Concept Quiz: 15 câu trắc nghiệm bắt bẫy củng cố khái niệm

#### Câu 1: Số hoàn hảo nhỏ nhất là số nào?
- **A.** 1
- **B.** **[Đáp án đúng]** 6
- **C.** 12
- **D.** 28
- > *Giải thích:* Các ước nhỏ hơn 6 là 1, 2, 3 và $1 + 2 + 3 = 6$.

#### Câu 2: Số nào sau đây cũng là một số hoàn hảo?
- **A.** 10
- **B.** 20
- **C.** **[Đáp án đúng]** 28
- **D.** 32
- > *Giải thích:* Các ước nhỏ hơn 28 là 1, 2, 4, 7, 14. Tổng: $1 + 2 + 4 + 7 + 14 = 28$.

#### Câu 3: Số 153 là số Armstrong vì:
- **A.** $153$ chia hết cho 3
- **B.** $153$ là số nguyên tố
- **C.** **[Đáp án đúng]** $1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153$
- **D.** $1 + 5 + 3 = 9$
- > *Giải thích:* Số Armstrong bậc 3 có tổng lập phương các chữ số bằng chính nó.

#### Câu 4: Số lượng các số chia hết cho 5 trong đoạn từ 1 đến 100 là:
- **A.** 19
- **B.** **[Đáp án đúng]** 20
- **C.** 21
- **D.** 25
- > *Giải thích:* $100 \mathbin{//} 5 = 20$.

#### Câu 5: Số lượng các số chia hết cho 4 trong đoạn từ 10 đến 30 là bao nhiêu?
- **A.** 4
- **B.** **[Đáp án đúng]** 5 (gồm 12, 16, 20, 24, 28)
- **C.** 6
- **D.** 7
- > *Giải thích:* $(30 \mathbin{//} 4) - ((10 - 1) \mathbin{//} 4) = 7 - 2 = 5$.

#### Câu 6: Trong đoạn từ $1$ đến $N$, số lượng các số chia hết cho cả 2 và 3 (tức chia hết cho 6) là:
- **A.** `N // 2 + N // 3`
- **B.** **[Đáp án đúng]** `N // 6`
- **C.** `N // 5`
- **D.** `(N // 2) * (N // 3)`
- > *Giải thích:* Chia hết cho cả 2 và 3 tức là chia hết cho BCNN$(2, 3) = 6$.

#### Câu 7: Nguyên lý bao hàm – loại trừ dùng để đếm số chia hết cho 2 hoặc 3 trong $[1, N]$ là:
- **A.** `N // 2 + N // 3`
- **B.** **[Đáp án đúng]** `N // 2 + N // 3 - N // 6`
- **C.** `N // 6`
- **D.** `(N // 2) + (N // 3) + (N // 6)`
- > *Giải thích:* Cộng hai tập rồi trừ phần giao bị đếm lặp (bội của $6$).

#### Câu 8: Một số được gọi là "số phong phú" nếu tổng các ước nhỏ hơn nó:
- **A.** Bằng chính nó
- **B.** Nhỏ hơn chính nó
- **C.** **[Đáp án đúng]** Lớn hơn chính nó
- **D.** Bằng 0
- > *Giải thích:* Ví dụ $12$: ước nhỏ hơn là 1, 2, 3, 4, 6. Tổng $= 16 > 12$.

#### Câu 9: Số chính phương có chữ số tận cùng không thể là chữ số nào?
- **A.** 1
- **B.** 4
- **C.** 5
- **D.** **[Đáp án đúng]** 2 (cũng không thể là 3, 7, 8)
- > *Giải thích:* Bình phương số tự nhiên chỉ tận cùng bằng 0, 1, 4, 5, 6, 9.

#### Câu 10: Đoạn code sau đếm được điều gì?
```python
count = 0
for i in range(1, 101):
    if i % 3 == 0 and i % 5 != 0:
        count += 1
print(count)
```
- **A.** Đếm số chia hết cho 15
- **B.** **[Đáp án đúng]** Đếm các số chia hết cho 3 nhưng không chia hết cho 5 trong $[1, 100]$
- **C.** Đếm số chia hết cho 3 hoặc 5
- **D.** Luôn bằng 33
- > *Giải thích:* Biểu thức lọc bội của 3 nhưng loại trừ bội chung của 3 và 5.

#### Câu 11: Giá trị `count` ở câu 10 bằng bao nhiêu?
- **A.** 33
- **B.** 20
- **C.** **[Đáp án đúng]** 27
- **D.** 30
- > *Giải thích:* Bội của 3: $100 \mathbin{//} 3 = 33$. Bội chung của 15: $100 \mathbin{//} 15 = 6$. Kết quả: $33 - 6 = 27$.

#### Câu 12: Kiểm tra $n = 49$ có phải số chính phương không. Cách nào đúng?
- **A.** `49 ** 0.5 == 7.0`
- **B.** **[Đáp án đúng]** `int(49 ** 0.5) * int(49 ** 0.5) == 49`
- **C.** `49 / 7 == 7`
- **D.** `49 % 2 == 1`
- > *Giải thích:* Cách (A) tuy ra đúng với 49 nhưng không đáng tin với số lớn do sai số số thực. Cách (B) luôn chính xác.

#### Câu 13: Cặp số $(220, 284)$ được gọi là "cặp số thân thiết" vì:
- **A.** Cả hai đều chia hết cho 2
- **B.** **[Đáp án đúng]** Tổng các ước nhỏ hơn số này bằng số kia và ngược lại
- **C.** Hiệu bằng 64
- **D.** Tích là số chính phương
- > *Giải thích:* Tổng ước nhỏ hơn 220 bằng 284 và ngược lại.

#### Câu 14: Để đếm số lẻ trong đoạn $[A, B]$, công thức nào đúng nhất?
- **A.** `(B - A) // 2`
- **B.** **[Đáp án đúng]** `(B - A + 1) - (B // 2 - (A - 1) // 2)`
- **C.** Luôn bằng một nửa tổng phần tử
- **D.** `(B - A + 1) // 2`
- > *Giải thích:* Tổng phần tử trong đoạn trừ đi số chẵn. Cách (D) sai khi cả $A$ và $B$ đều lẻ.

#### Câu 15: Số Armstrong 3 chữ số nào trong danh sách sau?
- **A.** 100
- **B.** 123
- **C.** **[Đáp án đúng]** 370
- **D.** 999
- > *Giải thích:* $3^3 + 7^3 + 0^3 = 27 + 343 + 0 = 370$. ✅
