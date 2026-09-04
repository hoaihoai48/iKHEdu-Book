# Bài 10: Đếm số theo quy luật và số đặc biệt

## 1. Tóm tắt kiến thức trọng tâm
- **Công thức đếm bội số trong đoạn $[A, B]$ với $\mathcal{O}(1)$:**
  $$\mathbf{count(A, B, K) = (B // K) - ((A - 1) // K)}$$
- **Số hoàn hảo:** Tổng các ước nhỏ hơn nó bằng chính nó ($6, 28, 496$).
- **Số chính phương:** Số có căn bậc 2 là số nguyên: `int(n**0.5)**2 == n`.

---


## 2. Concept quiz: 14 câu trắc nghiệm bắt bẫy củng cố khái niệm

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
- > *Giải thích:* Các ước nhỏ hơn 28 là 1, 2, 4, 7, 14. Tổng của chúng: $1 + 2 + 4 + 7 + 14 = 28$.

#### Câu 3: Số 153 là số armstrong vì:
- **A.** $153$ chia hết cho 3
- **B.** $153$ là số nguyên tố
- **C.** **[Đáp án đúng]** $1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153$
- **D.** $1 + 5 + 3 = 9$
- > *Giải thích:* Định nghĩa số Armstrong bậc 3 là bằng tổng lập phương các chữ số của chính nó.

#### Câu 4: Số lượng các số chia hết cho 5 trong đoạn từ 1 đến 100 là:
- **A.** 19
- **B.** **[Đáp án đúng]** 20
- **C.** 21
- **D.** 25
- > *Giải thích:* $100 // 5 = 20$.

#### Câu 5: Số lượng các số chia hết cho 4 trong đoạn từ 10 đến 30 là bao nhiêu?
- **A.** 4
- **B.** **[Đáp án đúng]** 5 (gồm 12, 16, 20, 24, 28)
- **C.** 6
- **D.** 7
- > *Giải thích:* Áp dụng công thức: $(30 // 4) - ((10 - 1) // 4) = 7 - (9 // 4) = 7 - 2 = 5$.

#### Câu 6: Trong đoạn từ $1$ đến $N$, số lượng các số chia hết cho cả 2 và 3 (tức là chia hết cho 6) là:
- **A.** `N // 2 + N // 3`
- **B.** **[Đáp án đúng]** `N // 6`
- **C.** `N // 5`
- **D.** `(N // 2) * (N // 3)`
- > *Giải thích:* Một số chia hết cho cả 2 và 3 khi và chỉ khi nó chia hết cho $\text{BCNN}(2, 3) = 6$.

#### Câu 7: Nguyên lý bao hàm - loại trừ (inclusion-exclusion) dùng để đếm số lượng các số chia hết cho 2 hoặc 3 trong đoạn $[1, N]$ là:
- **A.** `N // 2 + N // 3`
- **B.** **[Đáp án đúng]** `N // 2 + N // 3 - N // 6`
- **C.** `N // 6`
- **D.** `(N // 2) + (N // 3) + (N // 6)`
- > *Giải thích:* Lấy tập chia hết cho 2 cộng tập chia hết cho 3, rồi trừ đi phần giao bị đếm lặp 2 lần (các số chia hết cho 6).

#### Câu 8: Một số được gọi là "số phong phú" (abundant number) nếu tổng các ước nhỏ hơn nó:
- **A.** Bằng chính nó
- **B.** Nhỏ hơn chính nó
- **C.** **[Đáp án đúng]** Lớn hơn chính nó
- **D.** Bằng 0
- > *Giải thích:* Ví dụ số 12: các ước nhỏ hơn nó là 1, 2, 3, 4, 6 có tổng $1+2+3+4+6 = 16 > 12$.

#### Câu 9: Cặp số $(220, 284)$ được gọi là "cặp số thân thiết" (amicable numbers) vì:
- **A.** Cả hai đều chia hết cho 2
- **B.** **[Đáp án đúng]** Tổng các ước của số này bằng số kia và ngược lại
- **C.** Hiệu của chúng bằng 64
- **D.** Tích của chúng là số chính phương
- > *Giải thích:* Tổng các ước nhỏ hơn 220 bằng 284, và tổng các ước nhỏ hơn 284 lại đúng bằng 220.

#### Câu 10: Số chính phương có chữ số tận cùng không thể là chữ số nào sau đây?
- **A.** 1
- **B.** 4
- **C.** 5
- **D.** **[Đáp án đúng]** 2 (hoặc 3, 7, 8)
- > *Giải thích:* Bình phương của một số tự nhiên chỉ có thể tận cùng bằng 0, 1, 4, 5, 6, 9. Không bao giờ tận cùng bằng 2, 3, 7, 8.

#### Câu 11: Để đếm có bao nhiêu số lẻ trong đoạn từ $A$ đến $B$ (với $A \le B$), cách tính tổng quát chuẩn nhất là:
- **A.** `(B - A) // 2`
- **B.** **[Đáp án đúng]** Tổng số phần tử trừ đi số lượng số chẵn trong đoạn
- **C.** Luôn bằng một nửa
- **D.** `(B - A + 1) // 2`
- > *Giải thích:* Đoạn $[A, B]$ có tổng $(B - A + 1)$ số. Số lượng số chẵn là $(B // 2) - ((A - 1) // 2)$. Số lượng số lẻ bằng tổng trừ đi số chẵn.

#### Câu 12: Số tự nhiên $N$ được gọi là "số smith" nếu:
- **A.** $N$ là số nguyên tố
- **B.** **[Đáp án đúng]** $N$ là hợp số và tổng chữ số của nó bằng tổng các chữ số của các thừa số nguyên tố cấu tạo nên nó
- **C.** $N$ chia hết cho 9
- **D.** $N$ là số đối xứng
- > *Giải thích:* Ví dụ $4 \to 2 \times 2$: tổng chữ số 4 bằng $2 + 2 = 4$.

#### Câu 13: Đoạn code sau tính điều gì?
```python
count = 0
for i in range(1, 101):
    if i % 3 == 0 and i % 5 != 0:
        count += 1
print(count)
```
- **A.** Đếm số chia hết cho 15
- **B.** **[Đáp án đúng]** Đếm các số chia hết cho 3 nhưng không chia hết cho 5 trong đoạn 1 đến 100
- **C.** Đếm số chia hết cho 3 hoặc 5
- **D.** Luôn bằng 33
- > *Giải thích:* Biểu thức `i % 3 == 0 and i % 5 != 0` lọc chính xác các bội của 3 loại trừ các bội chung của 3 và 5.

#### Câu 14: Giá trị `count` ở câu 13 bằng bao nhiêu?
- **A.** 33
- **B.** 20
- **C.** **[Đáp án đúng]** 27
- **D.** 30
- > *Giải thích:* Số lượng số chia hết cho 3 là $100 // 3 = 33$. Số lượng số chia hết cho cả 3 và 5 (tức 15) là $100 // 15 = 6$. Vậy $33 - 6 = 27$.
