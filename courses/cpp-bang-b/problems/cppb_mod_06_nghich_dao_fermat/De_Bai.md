# Nghịch Đảo Modulo Bằng Fermat Nhỏ

> [!NOTE]
> **Phân loại bài toán:** `Core Foundation` (Bắt buộc)
## Bối cảnh
Cho số nguyên $A$ và số nguyên tố $M = 10^9 + 7$. Hãy tìm nghịch đảo modulo $A^{-1} \pmod M$ ($1 \le A < M$).

## Input
- Một dòng duy nhất chứa số nguyên $A$ ($1 \le A < 10^9 + 7$).

## Output
- In ra một số nguyên $X$ là nghịch đảo modulo thỏa $(A \times X) \pmod M = 1$.

## Sample 1
### Input
```text
3
```
### Output
```text
333333336
```
### Giải thích
(3 * 333333336) = 1000000008 = 1 mod (10^9+7).

## Ràng buộc
- $100\%$ số test có $1 \le A < 10^9 + 7$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
