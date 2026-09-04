# Bài 09: Ước số, bội số và số nguyên tố

## 1. Tóm tắt kiến thức trọng tâm
- Số nguyên tố là số $> 1$, chỉ có 2 ước là 1 và chính nó. Số 0 và 1 không phải là số nguyên tố. Số 2 là số nguyên tố chẵn duy nhất.
- **Thuật toán kiểm tra số nguyên tố tối ưu $\mathcal{O}(\sqrt{N})$:** Chỉ duyệt ước từ 2 đến $\lfloor\sqrt{N}
\rfloor$ (`int(n**0.5)`).
- **ƯCLN và BCNN:**
  ```python
  import math
  ucln = math.gcd(a, b)
  bcnn = (a * b) // ucln
  ```

## 2. Mẫu code chuẩn
```python
# Kiểm tra số nguyên tố
n = int(input())
la_nt = True
if n < 2:
    la_nt = False
else:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            la_nt = False
            break

print("YES" if la_nt else "NO")
```

## 3. Concept quiz: 15 câu trắc nghiệm bắt bẫy củng cố khái niệm

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
