# Nghịch Đảo Modulo Bằng Euclid Mở Rộng

**Phân loại bài toán:** `Core Foundation` (Bắt buộc)
## Bối cảnh
Cho hai số nguyên dương $A, M$ với $\gcd(A, M) = 1$. Hãy tìm nghịch đảo modulo $A^{-1} \pmod M$ bằng thuật toán Euclid mở rộng.

## Input
- Một dòng duy nhất chứa 2 số nguyên $A, M$ ($1 \le A, M \le 10^9, \gcd(A, M) = 1$).

## Output
- In ra một số nguyên $X \in [0, M - 1]$ thỏa $(A \times X) \pmod M = 1$.

## Sample 1
### Input
```text
3 7
```
### Output
```text
5
```
### Giải thích
3 * 5 = 15 = 1 mod 7.

## Ràng buộc
- $100\%$ số test có $A, M \le 10^9, \gcd(A, M) = 1$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
