# Tính Tổng Cấp Số Nhân Đồng Dư

**Phân loại bài toán:** `Core Foundation` (Bắt buộc)
## Bối cảnh
Cho $A, N$ và $M = 10^9 + 7$. Hãy tính tổng $S = 1 + A + A^2 + \dots + A^N \pmod M$.

## Input
- Một dòng duy nhất chứa 2 số nguyên $A, N$ ($0 \le A \le 10^9, 0 \le N \le 10^{18}$).

## Output
- In ra tổng $S \pmod{10^9 + 7}$.

## Sample 1
### Input
```text
2 3
```
### Output
```text
15
```
### Giải thích
S = 1 + 2 + 4 + 8 = 15.

## Ràng buộc
- $100\%$ số test có $A \le 10^9, N \le 10^{18}$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
