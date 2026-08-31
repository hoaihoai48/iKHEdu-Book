# Số Catalan Đồng Dư

> [!NOTE]
> **Phân loại bài toán:** `Advanced Challenge` (Thử thách mở rộng)
## Bối cảnh
Số Catalan $C_N = \frac{1}{N + 1} C(2N, N)$. Cho số nguyên $N$, hãy tính $C_N \pmod{10^9 + 7}$.

## Input
- Một dòng duy nhất chứa số nguyên $N$ ($0 \le N \le 10^6$).

## Output
- In ra $C_N \pmod{10^9 + 7}$.

## Sample 1
### Input
```text
3
```
### Output
```text
5
```
### Giải thích
C(3) = 1/4 * C(6, 3) = 1/4 * 20 = 5.

## Ràng buộc
- $100\%$ số test có $N \le 10^6$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
