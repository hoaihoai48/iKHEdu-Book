# Lũy Thừa Tầng (Tower of Powers)

## Bối cảnh
Trong bài toán tháp lũy thừa A^(B^C) mod M với M = 10^9 + 7, theo định lý Fermat nhỏ, số mũ B^C ở trên tầng tháp phải được tính theo modulo phi(M) = M - 1 = 10^9 + 6 trước khi hạ xuống làm số mũ cho cơ số A.

## Nhiệm vụ
Cho 3 số nguyên A, B, C. Hãy tính giá trị của tháp lũy thừa A^(B^C) theo modulo 10^9 + 7.

## Input
- Một dòng chứa 3 số nguyên $A, B, C$ ($0 \le A, B, C \le 10^9$).

## Output
- In ra giá trị của $A^{B^C} \pmod{10^9 + 7}$.

## Sample 1
### Input
```text
3 2 2
```
### Output
```text
81
```
### Giải thích
B^C = 2^2 = 4. Do đó A^(B^C) = 3^4 = 81. Kết quả in ra: 81.

## Ràng buộc
- $100\%$ số test có $A, B, C \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
