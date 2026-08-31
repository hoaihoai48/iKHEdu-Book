# Lũy Thừa Tầng (Tower of Powers)

> [!NOTE]
> **Phân loại bài toán:** `Advanced Challenge` (Thử thách mở rộng)
## Bối cảnh
Cho 3 số nguyên $A, B, C$. Hãy tính $A^{B^C} \pmod{10^9 + 7}$.

## Input
- Một dòng duy nhất chứa 3 số nguyên $A, B, C$ ($0 \le A, B, C \le 10^9$).

## Output
- In ra $A^{B^C} \pmod{10^9 + 7}$.

## Sample 1
### Input
```text
3 2 3
```
### Output
```text
6561
```
### Giải thích
2^3 = 8 -> 3^8 = 6561.

## Ràng buộc
- $100\%$ số test có $A, B, C \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
