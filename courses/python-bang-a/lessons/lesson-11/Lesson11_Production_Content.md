# Bài 11: Ước số, bội số và số nguyên tố

---

## 1. Khởi động: Trò chơi chia kẹo & những con số bất khả chiến bại

* Giả sử em có 12 viên kẹo, em có thể chia đều cho những nhóm bạn có bao nhiêu người mà không bị thừa viên nào?
  * Chia cho 1 bạn $\implies$ mỗi bạn 12 viên.
  * Chia cho 2 bạn $\implies$ mỗi bạn 6 viên.
  * Chia cho 3 bạn $\implies$ mỗi bạn 4 viên.
  * Chia cho 4 bạn $\implies$ mỗi bạn 3 viên.
  * Chia cho 6 bạn $\implies$ mỗi bạn 2 viên.
  * Chia cho 12 bạn $\implies$ mỗi bạn 1 viên.
  $\implies$ Các số $1, 2, 3, 4, 6, 12$ được gọi là **CÁC ƯỚC SỐ** của số 12!

* Nhưng nếu em có **7 viên kẹo**?
  Em chỉ có thể chia đều cho đúng **1 người** hoặc chia cho **7 người**. Không thể chia đều cho 2, 3, 4, 5, hay 6 người được!
  $\implies$ Những con số kiên cường như số 7, chỉ chia hết cho 1 và chính nó, được gọi là **SỐ NGUYÊN TỐ (Prime Number)**!

Trong thế giới lập trình thi đấu, số nguyên tố và ước số là "linh hồn" của vô số bài toán từ cấp Trường cho đến Quốc gia.

---

## 2. Bí thuật đếm ước và tìm ước của một số $N$

### 2.1. Ước số là gì?
Số tự nhiên $d$ ($d \ge 1$) được gọi là **ước số** của $N$ nếu $N$ chia hết cho $d$ (tức là `N % d == 0`).

### 2.2. Thuật toán duyệt tìm ước cơ bản (dành cho tiểu học)
Ta dùng một vòng lặp `for` chạy từ $1$ đến $N$. Cứ mỗi khi thấy `N % i == 0`, ta đếm thêm 1 hoặc in số $i$ đó ra:

```python
n = int(input())
dem_uoc = 0
tong_uoc = 0

for i in range(1, n + 1):
    if n % i == 0:
        dem_uoc += 1
        tong_uoc += i
        print(i, end=" ")  # In ra từng ước số

print()
print("So luong uoc:", dem_uoc)
print("Tong cac uoc:", tong_uoc)
```

---

## 3. Bản chất của số nguyên tố & thuật toán kiểm tra

### 3.1. Định nghĩa chuẩn thi đấu:
Số nguyên tố là số tự nhiên **lớn hơn 1** và **chỉ có đúng 2 ước số** là 1 và chính nó.
* Các số nguyên tố đầu tiên: $2, 3, 5, 7, 11, 13, 17, 19, 23, 29, \dots$
* **Số 2 là số nguyên tố chẵn DUY NHẤT** và là số nguyên tố nhỏ nhất.
* **Số 0 và số 1 KHÔNG PHẢI là số nguyên tố!** (Đây là bẫy lỗi kinh điển nhất!).

### 3.2. Thuật toán kiểm tra số nguyên tố bằng cờ hiệu (flag)
```python
n = int(input())

if n < 2:
    print("KHONG PHAI SO NGUYEN TO")
else:
    la_nguyen_to = True  # Giả sử ban đầu n là số nguyên tố
    for i in range(2, n):
        if n % i == 0:
            la_nguyen_to = False  # Bị bắt quả tang chia hết cho số khác!
            break  # Không cần kiểm tra nữa, thoát ngay!

    if la_nguyen_to:
        print("LA SO NGUYEN TO")
    else:
        print("KHONG PHAI SO NGUYEN TO")
```

---

## 4. Số chính phương & ước chung lớn nhất (`math.gcd`)

### 4.1. Số chính phương (square number)
Số chính phương là số bằng bình phương của một số tự nhiên ($0^2=0, 1^2=1, 2^2=4, 3^2=9, 4^2=16, 5^2=25 \dots$).
> 💡 **Tính chất kỳ diệu:** Số chính phương là số duy nhất có **số lượng ước số là một số LẺ**! (Ví dụ: số 9 có 3 ước là 1, 3, 9).

### 4.2. Ước chung lớn nhất (ưcln / GCD)
Trong Python, ta có thể dùng thư viện `math` với hàm `math.gcd(a, b)` để tìm ước chung lớn nhất trong 1 mili-giây:
```python
import math

a = 12
b = 18
print(math.gcd(a, b))  # In ra 6
```

---

## 5. Concept quiz: 15 câu trắc nghiệm bắt bẫy củng cố khái niệm

#### Câu 1: Số nào sau đây là số nguyên tố nhỏ nhất?
- **A.** 0
- **B.** 1
- **C.** **[Đáp án đúng]** 2
- **D.** 3
- > *Giải thích:* Số 2 là số nguyên tố nhỏ nhất và cũng là số nguyên tố chẵn duy nhất.

#### Câu 2: Số 1 có phải là số nguyên tố không?
- **A.** Có, vì 1 chỉ chia hết cho 1
- **B.** **[Đáp án đúng]** Không, vì định nghĩa số nguyên tố bắt buộc phải lớn hơn 1 (có đúng 2 ước phân biệt)
- **C.** Tùy trường hợp
- **D.** Số 1 là số nguyên tố đặc biệt
- > *Giải thích:* Bẫy kinh điển: Số 1 chỉ có đúng 1 ước duy nhất là chính nó nên không phải số nguyên tố.

#### Câu 3: Số 9 có bao nhiêu ước số tự nhiên?
- **A.** 2
- **B.** **[Đáp án đúng]** 3 (gồm 1, 3, 9)
- **C.** 4
- **D.** 1
- > *Giải thích:* Các ước của 9 là 1, 3, 9.

#### Câu 4: Một số tự nhiên có số lượng ước số là một số lẻ thì số đó chắc chắn là:
- **A.** Số lẻ
- **B.** Số nguyên tố
- **C.** **[Đáp án đúng]** Số chính phương
- **D.** Số chẵn
- > *Giải thích:* Các ước thường đi theo cặp $(d, N/d)$. Chỉ có số chính phương khi gặp căn bậc 2 thì $d = N/d$ ghép thành 1 ước đơn, tạo thành số lượng ước lẻ.

#### Câu 5: Số nào sau đây không phải là số nguyên tố?
- **A.** 11
- **B.** 13
- **C.** **[Đáp án đúng]** 15
- **D.** 17
- > *Giải thích:* Số 15 chia hết cho 1, 3, 5, 15 (có 4 ước).

#### Câu 6: Trong Python, để tìm ước chung lớn nhất của 2 số `a` và `b`, ta dùng thư viện nào?
- **A.** `import random`
- **B.** `import time`
- **C.** **[Đáp án đúng]** `import math` và dùng `math.gcd(a, b)`
- **D.** `import turtle`
- > *Giải thích:* `gcd` là viết tắt của Greatest Common Divisor trong thư viện `math`.

#### Câu 7: Bội chung nhỏ nhất (bcnn / lcm) của 2 số $A$ và $B$ liên hệ với ưcln thế nào?
- **A.** $\text{LCM} = A + B - \text{GCD}$
- **B.** **[Đáp án đúng]** $\text{LCM} = (A \times B) // \text{GCD}(A, B)$
- **C.** $\text{LCM} = A \times B \times \text{GCD}$
- **D.** $\text{LCM} = A \times B$
- > *Giải thích:* Tích của hai số bằng tích của ƯCLN và BCNN của chúng: $A \times B = \text{GCD} \times \text{LCM}$.

#### Câu 8: Điều kiện để một số $i$ là ước số của $N$ trong Python được viết là:
- **A.** `n / i == 0`
- **B.** `n // i == 0`
- **C.** **[Đáp án đúng]** `n % i == 0`
- **D.** `i % n == 0`
- > *Giải thích:* Phép chia dư bằng 0 biểu thị phép chia hết.

#### Câu 9: Ước số lớn nhất của số $N$ (với $N > 0$) luôn luôn bằng:
- **A.** $N - 1$
- **B.** **[Đáp án đúng]** Chính nó ($N$)
- **C.** 1
- **D.** $N // 2$
- > *Giải thích:* Mọi số tự nhiên $N > 0$ đều chia hết cho chính nó, và không thể chia hết cho số nào lớn hơn $N$.

#### Câu 10: Ước số dương nhỏ nhất của mọi số tự nhiên $N > 0$ luôn luôn là:
- **A.** 0
- **B.** **[Đáp án đúng]** 1
- **C.** 2
- **D.** Chính nó
- > *Giải thích:* Mọi số tự nhiên đều chia hết cho 1.

#### Câu 11: Có bao nhiêu số nguyên tố nằm trong khoảng từ 1 đến 10?
- **A.** 3
- **B.** **[Đáp án đúng]** 4 (gồm 2, 3, 5, 7)
- **C.** 5
- **D.** 2
- > *Giải thích:* Có 4 số nguyên tố là 2, 3, 5, 7.

#### Câu 12: Để tối ưu hóa thuật toán kiểm tra số nguyên tố $N$, ta chỉ cần cho vòng lặp kiểm tra ước số chạy đến đâu?
- **A.** Đến $N - 1$
- **B.** Đến $N // 2$
- **C.** **[Đáp án đúng]** Đến $\sqrt{N}$ (căn bậc 2 của $N$, tức là `int(n**0.5)`)
- **D.** Đến 100
- > *Giải thích:* Nếu $N$ có ước lớn hơn $\sqrt{N}$ thì chắc chắn phải có ước tương ứng nhỏ hơn $\sqrt{N}$.

#### Câu 13: Đoạn code sau in ra kết quả gì?
```python
n = 16
can = int(n ** 0.5)
if can * can == n:
    print("YES")
else:
    print("NO")
```
- **A.** NO
- **B.** **[Đáp án đúng]** YES
- **C.** Báo lỗi
- **D.** 4
- > *Giải thích:* $16 = 4^2$ là một số chính phương nên in ra YES.

#### Câu 14: Hai số được gọi là "nguyên tố cùng nhau" khi nào?
- **A.** Cả hai số đều là số nguyên tố
- **B.** **[Đáp án đúng]** Ước chung lớn nhất của chúng bằng 1 (`math.gcd(a, b) == 1`)
- **C.** Hai số bằng nhau
- **D.** Tổng của chúng là số nguyên tố
- > *Giải thích:* Định nghĩa 2 số nguyên tố cùng nhau (ví dụ: 8 và 9, dù cả 8 và 9 đều là hợp số nhưng $\text{gcd}(8, 9) = 1$).

#### Câu 15: Một học sinh viết kiểm tra số nguyên tố và bỏ qua trường hợp `n < 2`. Khi người chấm thi nhập vào `n = 1`, chương trình sẽ cho kết quả sai là:
- **A.** Báo lỗi cú pháp
- **B.** **[Đáp án đúng]** Nhận nhầm 1 là số nguyên tố
- **C.** In ra không xác định
- **D.** Lặp vô tận
- > *Giải thích:* Vì vòng lặp `range(2, 1)` sẽ không chạy lần nào, cờ `la_nguyen_to` vẫn giữ nguyên là `True`, dẫn đến kết luận sai rằng 1 là số nguyên tố!
