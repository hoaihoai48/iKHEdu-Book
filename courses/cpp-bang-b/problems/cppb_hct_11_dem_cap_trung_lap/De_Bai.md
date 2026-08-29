# Đếm Cặp Tổng S Trên Mảng Trùng Lặp

## Bối cảnh
Cho mảng gồm $N$ số nguyên có thể chứa nhiều phần tử trùng lặp và số nguyên $S$. Hãy đếm số lượng cặp chỉ số $(i, j)$ với $1 \le i < j \le N$ sao cho $A_i + A_j = S$.

## Input
- Dòng 1: 2 số nguyên $N$ và $S$ ($2 \le N \le 2 \cdot 10^5, -10^{18} \le S \le 10^{18}$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^9 \le A_i \le 10^9$).

## Output
- In ra một số nguyên duy nhất là số lượng cặp chỉ số thỏa mãn.

## Sample 1
### Input
```text
6 6
3 3 3 3 3 3
```
### Output
```text
15
```

## Ràng buộc
- $100\%$ số test có $N \le 2 \cdot 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
