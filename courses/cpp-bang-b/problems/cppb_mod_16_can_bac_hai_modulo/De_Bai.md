# Đồng Dư Cực Hạn: Căn Bậc Hai Modulo

**Phân loại bài toán:** `Advanced Challenge` (Thử thách mở rộng)
## Bối cảnh
Cho số nguyên $A$ và số nguyên tố $P = 10^9 + 7$. Hãy tìm số nguyên $X$ ($0 \le X < P$) nhỏ nhất sao cho $X^2 \equiv A \pmod P$. Nếu không tồn tại $X$, in `-1`.

## Input
- Một dòng duy nhất chứa số nguyên $A$ ($0 \le A < 10^9 + 7$).

## Output
- In ra nghiệm $X$ nhỏ nhất, hoặc `-1` nếu vô nghiệm.

## Sample 1
### Input
```text
4
```
### Output
```text
2
```
### Giải thích
2^2 = 4 mod (10^9 + 7).

## Ràng buộc
- $100\%$ số test có $A < 10^9 + 7$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
