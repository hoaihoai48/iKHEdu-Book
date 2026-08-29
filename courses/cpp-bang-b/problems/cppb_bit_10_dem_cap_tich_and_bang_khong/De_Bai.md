# Đếm Cặp Có Tích Bit AND Bằng 0

## Bối cảnh
Cho một dãy gồm $N$ số nguyên không âm $A_1, A_2, \dots, A_N$. Hãy đếm số lượng cặp chỉ số $(i, j)$ thỏa mãn $1 \le i < j \le N$ và $A_i \ \& \ A_j = 0$.

## Input
- Dòng 1: Số nguyên dương $N$ ($1 \le N \le 10^5$).
- Dòng 2: $N$ số nguyên không âm $A_1, A_2, \dots, A_N$ ($0 \le A_i < 2^{12} = 4096$).

## Output
- In ra một số nguyên duy nhất là số lượng cặp thỏa mãn.

## Sample 1
### Input
```text
4
1 2 3 4
```
### Output
```text
3
```
*(Giải thích: Các cặp: $(1, 2) \implies 1 \& 2 = 0$, $(1, 4) \implies 1 \& 4 = 0$, $(2, 4) \implies 2 \& 4 = 0$).*

## Ràng buộc
- $100\%$ số test có $N \le 10^5, A_i < 4096$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
