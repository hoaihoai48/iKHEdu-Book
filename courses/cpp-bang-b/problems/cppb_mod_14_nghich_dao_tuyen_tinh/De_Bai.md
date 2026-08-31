# Nghịch Đảo Tuyến Tính 1..N Trong O(N)

> [!NOTE]
> **Phân loại bài toán:** `Advanced Challenge` (Thử thách mở rộng)
## Bối cảnh
Cho số nguyên $N$ và $M = 10^9 + 7$. Hãy tính nghịch đảo modulo của tất cả các số từ $1$ đến $N$ trong thời gian $\mathcal{O}(N)$.

## Input
- Một dòng duy nhất chứa số nguyên $N$ ($1 \le N \le 10^7$).

## Output
- In ra tổng của tất cả các nghịch đảo modulo $\sum_{i=1}^N i^{-1} \pmod M$.

## Sample 1
### Input
```text
3
```
### Output
```text
833333341
```
### Giải thích
inv(1) = 1, inv(2) = 500000004, inv(3) = 333333336 -> Tổng mod M = 833333341.

## Ràng buộc
- $100\%$ số test có $N \le 10^7$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
