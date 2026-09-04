# Nghịch Đảo Modulo Bằng Fermat Nhỏ

## Bối cảnh
Khi chia hai số trong vành modulo nguyên tố M = 10^9 + 7, phép chia A / B được chuyển hóa thành phép nhân với nghịch đảo modulo: A * B^(M - 2) mod M theo định lý Fermat nhỏ. Hãy tìm nghịch đảo modulo của số nguyên A.

## Nhiệm vụ
Cho số nguyên A và số nguyên tố M = 10^9 + 7. Hãy tìm số nguyên X trong khoảng [1, M - 1] sao cho (A * X) mod M = 1.

## Input
- Một dòng duy nhất chứa số nguyên $A$ ($1 \le A < 10^9 + 7$).

## Output
- In ra số nghịch đảo modulo $A^{-1} \pmod{10^9 + 7}$.

## Sample 1
### Input
```text
2
```
### Output
```text
500000004
```
### Giải thích
2 * 500000004 = 1000000008 = (10^9 + 7) + 1 = 1 mod (10^9 + 7). Do đó nghịch đảo modulo của 2 là 500000004.

## Ràng buộc
- $100\%$ số test có $1 \le A < 10^9 + 7$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
