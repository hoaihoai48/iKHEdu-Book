# Tìm Dãy Con Có Tổng XOR Bằng K

## Bối cảnh
Cho một tập hợp gồm $N$ số nguyên dương $A_1, A_2, \dots, A_N$ và một số nguyên $K$. Hãy đếm số lượng tập con khác rỗng có tích XOR của tất cả các phần tử đúng bằng $K$.

## Input
- Dòng 1: Gồm 2 số nguyên $N, K$ ($1 \le N \le 20, 0 \le K \le 10^9$).
- Dòng 2: $N$ số nguyên dương $A_1, A_2, \dots, A_N$ ($1 \le A_i \le 10^9$).

## Output
- In ra một số nguyên duy nhất là số lượng tập con thỏa mãn.

## Sample 1
### Input
```text
3 3
1 2 3
```
### Output
```text
2
```
*(Giải thích: Tập $\{3\}$ có $\text{XOR} = 3$; Tập $\{1, 2\}$ có $1 \oplus 2 = 3$. Tổng cộng 2 tập).*

## Ràng buộc
- $100\%$ số test có $N \le 20$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
