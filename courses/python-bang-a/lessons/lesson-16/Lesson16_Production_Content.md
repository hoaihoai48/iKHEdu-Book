# Bài 16: Tổng ôn kiến thức và Đề thi thử

## 1. Bản đồ tổng ôn toàn bộ kiến thức Python Bảng A

Bài cuối cùng của khóa học là bài **tổng ôn** — hệ thống hóa lại toàn bộ kiến thức đã học từ Bài 01 đến Bài 15, kết hợp với các **đề thi thử mô phỏng** để luyện tập thực chiến.

### 1.1. Bản đồ kiến thức theo chương

| Chương | Nội dung cốt lõi | Kỹ năng then chốt |
|:---:|---|---|
| **CH.1** | Nhập/Xuất, Biến, Kiểu dữ liệu, Toán tử | `input()`, `print()`, `int()`, `float()`, `//`, `%` |
| **CH.2** | Rẽ nhánh `if-elif-else`, Vòng lặp `for`, `while` | Điều kiện logic, `range()`, `break`, `continue` |
| **CH.3** | Số học: Ước, Bội, Nguyên tố, Tách chữ số | `n % 10`, `n // 10`, `sqrt(n)` |
| **CH.4** | Danh sách, Thống kê, Sắp xếp | `list()`, `append()`, `sort()`, `max()`, `min()` |
| **CH.5** | Chuỗi ký tự, ASCII | `s[::-1]`, `ord()`, `chr()`, `split()`, `join()` |
| **CH.6** | Chiến lược thi đấu, Đề thi thử | Quy trình 5 bước, Edge Cases, Tối ưu |

### 1.2. Checklist kiểm tra trước khi vào phòng thi

- [ ] Thuộc lòng cú pháp nhập mảng: `a = list(map(int, input().split()))`
- [ ] Phân biệt rõ `//` (chia nguyên) và `/` (chia thực)
- [ ] Biết cách kiểm tra nguyên tố bằng duyệt đến $\sqrt{N}$
- [ ] Biết tách từng chữ số bằng `% 10` và `// 10`
- [ ] Biết đảo ngược chuỗi/danh sách bằng `[::-1]`
- [ ] Biết dùng `set()` để loại trùng
- [ ] Nhớ kiểm tra Edge Cases: $N = 0$, $N = 1$, mảng rỗng, chuỗi rỗng

---

## 2. Bảng tổng hợp công thức và mẫu code quan trọng

### 2.1. Công thức toán học

| Công thức | Cú pháp Python | Ứng dụng |
|---|---|---|
| Tổng $1 + 2 + \dots + N$ | `n * (n + 1) // 2` | Tính tổng dãy số |
| Đếm bội $K$ trong $[A, B]$ | `b // k - (a - 1) // k` | Đếm số chia hết |
| Kiểm tra chính phương | `int(n**0.5)**2 == n` | Số học |
| Giai thừa $N!$ | Vòng lặp `for` | Tổ hợp |

### 2.2. Kỹ thuật lập trình thường gặp

| Kỹ thuật | Mẫu code | Khi nào dùng |
|---|---|---|
| Biến đếm | `dem += 1` | Đếm phần tử thỏa điều kiện |
| Biến tích lũy | `tong += x` | Tính tổng |
| Biến cờ | `ok = True` → `ok = False` | Kiểm tra tính chất |
| Cuốn chiếu | `a, b = b, a + b` | Fibonacci, dãy số |
| Tách chữ số | `n % 10`, `n //= 10` | Xử lý từng chữ số |

---

## 3. Đề thi thử số 01 — Mô phỏng đề thi thành phố (90 phút, 4 bài)

### Bài 1 (30 điểm): Mua dụng cụ học tập

**Đề bài:** Mua $N$ quyển vở giá $P$ đồng/quyển. Mua từ 10 quyển trở lên giảm $10\%$. Tính số tiền phải trả (số nguyên).

**Input:** Một dòng chứa hai số nguyên $N$ và $P$ ($1 \le N \le 1000$, $1 \le P \le 100000$).

**Output:** Một số nguyên duy nhất — tổng số tiền phải trả.

**Code mẫu:**
```python
n, p = map(int, input().split())
tong = n * p
if n >= 10:
    tong = int(tong * 0.9)
print(tong)
```

**Phân tích:** Bài cơ bản, chỉ cần `if-else` và phép nhân. Lưu ý ép kiểu `int()` vì $0.9$ tạo ra số thực.

---

### Bài 2 (30 điểm): Số lộc phát đối xứng

**Đề bài:** Số lộc phát đối xứng là số đối xứng (palindrome) và chỉ chứa các chữ số $6$ hoặc $8$. Cho số $N$, kiểm tra xem có phải số lộc phát đối xứng không.

**Input:** Một dòng chứa số nguyên dương $N$ ($1 \le N \le 10^{18}$).

**Output:** `YES` hoặc `NO`.

**Code mẫu:**
```python
s = input()
if s == s[::-1] and all(c in "68" for c in s):
    print("YES")
else:
    print("NO")
```

**Phân tích:** Đọc $N$ dưới dạng chuỗi (vì $N$ có thể rất lớn). Kiểm tra đối xứng bằng `s[::-1]`, kiểm tra chữ số bằng `all()`.

---

### Bài 3 (25 điểm): Đếm từ độc nhất trong văn bản

**Đề bài:** Cho một câu văn. Đếm số lượng từ khác nhau xuất hiện (không phân biệt hoa thường).

**Input:** Một dòng chuỗi ký tự.

**Output:** Một số nguyên — số lượng từ khác nhau.

**Code mẫu:**
```python
s = input().lower()
tu = s.split()
print(len(set(tu)))
```

**Phân tích:** Chuyển thành chữ thường `.lower()`, tách từ `.split()`, loại trùng `set()`, đếm `len()`.

---

### Bài 4 (15 điểm — Phân loại): Bước nhảy chú cào cào

**Đề bài:** Chú cào cào xuất phát từ vị trí $0$, cần nhảy đến vị trí $X$. Mỗi bước nhảy xa tối đa $K$ mét. Tìm số bước nhảy ít nhất.

**Input:** Một dòng chứa hai số nguyên $X$ và $K$ ($1 \le X, K \le 10^9$).

**Output:** Một số nguyên — số bước nhảy ít nhất.

**Code mẫu:**
```python
x, k = map(int, input().split())
ans = (x + k - 1) // k
print(ans)
```

**Phân tích:** Đây là bài toán chia lấy trần. Công thức: $\lceil X / K \rceil = (X + K - 1) \mathbin{//} K$.

---

## 4. Đề thi thử số 02 — Nâng cao (90 phút, 4 bài)

### Bài 1 (25 điểm): Tổng chữ số của $N$

**Đề bài:** Cho số nguyên dương $N$. Tính tổng các chữ số.

**Input:** Số nguyên $N$ ($1 \le N \le 10^{18}$).

**Output:** Tổng chữ số.

```python
s = input()
tong = 0
for ch in s:
    tong += int(ch)
print(tong)
```

---

### Bài 2 (25 điểm): Số hoàn hảo trong đoạn

**Đề bài:** Cho hai số $A, B$. Liệt kê tất cả các số hoàn hảo trong đoạn $[A, B]$.

**Input:** Hai số $A, B$ ($1 \le A \le B \le 10000$).

**Output:** Các số hoàn hảo trên các dòng riêng. Nếu không có, in `KHONG CO`.

```python
a, b = map(int, input().split())
found = False
for n in range(a, b + 1):
    if n < 2:
        continue
    tong_uoc = 0
    for i in range(1, n):
        if n % i == 0:
            tong_uoc += i
    if tong_uoc == n:
        print(n)
        found = True
if not found:
    print("KHONG CO")
```

---

### Bài 3 (30 điểm): Chuỗi đối xứng dài nhất

**Đề bài:** Cho chuỗi $S$ chỉ chứa chữ cái thường. Tìm chuỗi con liên tiếp đối xứng (palindrome) dài nhất.

**Input:** Chuỗi $S$ ($1 \le |S| \le 1000$).

**Output:** Độ dài chuỗi con đối xứng dài nhất.

```python
s = input()
max_len = 1
for i in range(len(s)):
    for j in range(i + 1, len(s) + 1):
        sub = s[i:j]
        if sub == sub[::-1]:
            max_len = max(max_len, len(sub))
print(max_len)
```

---

### Bài 4 (20 điểm — Phân loại): Dãy Fibonacci chia hết

**Đề bài:** Đếm có bao nhiêu số Fibonacci $\le N$ chia hết cho $K$.

**Input:** Hai số $N, K$ ($1 \le N \le 10^{18}$, $2 \le K \le 100$).

**Output:** Số lượng số Fibonacci thỏa mãn.

```python
n, k = map(int, input().split())
a, b = 1, 1
dem = 0
while a <= n:
    if a % k == 0:
        dem += 1
    a, b = b, a + b
print(dem)
```

---

## 5. Concept Quiz: 15 câu trắc nghiệm tổng ôn toàn diện

#### Câu 1: `input()` trong Python luôn trả về kiểu dữ liệu gì?
- **A.** `int`
- **B.** `float`
- **C.** **[Đáp án đúng]** `str`
- **D.** Phụ thuộc vào dữ liệu nhập
- > *Giải thích:* `input()` luôn đọc dưới dạng chuỗi. Cần ép kiểu bằng `int()` hoặc `float()`.

#### Câu 2: `17 // 5` và `17 % 5` lần lượt cho kết quả:
- **A.** 3.4 và 2
- **B.** **[Đáp án đúng]** 3 và 2
- **C.** 3 và 0
- **D.** 4 và 2
- > *Giải thích:* $17 = 5 \times 3 + 2$. Phần nguyên = 3, phần dư = 2.

#### Câu 3: Kiểm tra $N$ chẵn hay lẻ dùng biểu thức nào?
- **A.** `N / 2 == 0`
- **B.** **[Đáp án đúng]** `N % 2 == 0`
- **C.** `N // 2 == 0`
- **D.** `N == 2`
- > *Giải thích:* `N % 2` trả về phần dư khi chia cho 2. Nếu = 0 thì chẵn.

#### Câu 4: `range(5, 0, -1)` tạo ra dãy số:
- **A.** `5, 4, 3, 2, 1, 0`
- **B.** **[Đáp án đúng]** `5, 4, 3, 2, 1`
- **C.** `0, 1, 2, 3, 4, 5`
- **D.** `1, 2, 3, 4, 5`
- > *Giải thích:* `range(5, 0, -1)` đếm ngược từ 5 xuống 1, không bao gồm 0.

#### Câu 5: `[1, 2, 3] + [4, 5]` cho kết quả:
- **A.** `[5, 7]`
- **B.** `[1, 2, 3, 4, 5]`
- **C.** **[Đáp án đúng]** `[1, 2, 3, 4, 5]`
- **D.** Báo lỗi
- > *Giải thích:* Phép `+` trên danh sách nối hai danh sách thành một.

#### Câu 6: Để đảo ngược chuỗi `s`, cú pháp đúng là:
- **A.** `s.reverse()`
- **B.** **[Đáp án đúng]** `s[::-1]`
- **C.** `reverse(s)`
- **D.** `s[-1:0]`
- > *Giải thích:* `[::-1]` là slicing với bước nhảy -1. `reverse()` chỉ dùng cho List.

#### Câu 7: `ord('a') - ord('A')` bằng:
- **A.** 26
- **B.** **[Đáp án đúng]** 32
- **C.** 0
- **D.** 97
- > *Giải thích:* $97 - 65 = 32$.

#### Câu 8: Kiểm tra nguyên tố chỉ cần duyệt đến:
- **A.** $N$
- **B.** $N / 2$
- **C.** **[Đáp án đúng]** $\sqrt{N}$
- **D.** $N - 1$
- > *Giải thích:* Nếu $N$ có ước $d > \sqrt{N}$ thì $N/d < \sqrt{N}$ đã được kiểm tra.

#### Câu 9: `"hello".upper()` trả về:
- **A.** `"hello"`
- **B.** `"Hello"`
- **C.** **[Đáp án đúng]** `"HELLO"`
- **D.** `"hELLO"`
- > *Giải thích:* `upper()` chuyển toàn bộ thành chữ in hoa.

#### Câu 10: `len(set([1, 1, 2, 2, 3]))` bằng:
- **A.** 5
- **B.** 2
- **C.** **[Đáp án đúng]** 3
- **D.** 0
- > *Giải thích:* `set()` loại trùng: `{1, 2, 3}` có 3 phần tử.

#### Câu 11: Công thức chia lấy trần $\lceil A / B \rceil$ trong Python là:
- **A.** `A / B`
- **B.** `A // B`
- **C.** **[Đáp án đúng]** `(A + B - 1) // B`
- **D.** `A % B`
- > *Giải thích:* Thêm $B - 1$ trước khi chia nguyên để "làm tròn lên".

#### Câu 12: `a.sort()` trả về giá trị gì?
- **A.** Danh sách đã sắp
- **B.** `True`
- **C.** **[Đáp án đúng]** `None`
- **D.** Số phần tử
- > *Giải thích:* `sort()` thay đổi danh sách tại chỗ, trả về `None`.

#### Câu 13: Biến cờ thường dùng để:
- **A.** Đếm số lần lặp
- **B.** **[Đáp án đúng]** Đánh dấu trạng thái True/False trong quá trình duyệt
- **C.** Lưu giá trị lớn nhất
- **D.** In kết quả
- > *Giải thích:* Flag chuyển từ `True` sang `False` (hoặc ngược lại) khi gặp điều kiện.

#### Câu 14: `"abc" * 3` cho kết quả:
- **A.** `"abc3"`
- **B.** `"aabbcc"`
- **C.** **[Đáp án đúng]** `"abcabcabc"`
- **D.** Báo lỗi
- > *Giải thích:* Phép nhân chuỗi với số nguyên lặp lại chuỗi.

#### Câu 15: Trong phòng thi, nên giải bài theo thứ tự nào?
- **A.** Bài khó trước
- **B.** **[Đáp án đúng]** Bài dễ trước lấy điểm chắc, bài khó giải sau
- **C.** Bài cuối trước
- **D.** Ngẫu nhiên
- > *Giải thích:* Chiến lược "dễ trước khó sau" tối đa hóa tổng điểm.
