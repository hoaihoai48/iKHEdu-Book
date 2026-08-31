# Phép Chia Đồng Dư A / B mod M

**Phân loại bài toán:** `Core Foundation` (Bắt buộc)
## Bối cảnh
Cho 2 số nguyên $A, B$ và số nguyên tố $M = 10^9 + 7$ ($B 
ot\equiv 0 \pmod M$). Hãy tính giá trị $\frac{A}{B} \pmod M$.

## Input
- Một dòng duy nhất chứa 2 số nguyên $A, B$ ($0 \le A \le 10^{18}, 1 \le B \le 10^{18}$).

## Output
- In ra giá trị $\frac{A}{B} \pmod{10^9 + 7}$.

## Sample 1
### Input
```text
10 2
```
### Output
```text
5
```
### Giải thích
10 / 2 = 5.

## Ràng buộc
- $100\%$ số test có $A, B \le 10^{18}$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
