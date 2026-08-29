# Đếm Số Lượng Đoạn Con Có Tổng Không Quá S

## Bối cảnh
Cho mảng gồm $N$ số nguyên **không âm** $A_1, A_2, \dots, A_N$ và số nguyên $S$. Hãy đếm số lượng đoạn con liên tiếp $[L, R]$ ($1 \le L \le R \le N$) có tổng các phần tử $\le S$.

## Input
- Dòng 1: Chứa 2 số nguyên $N$ và $S$ ($1 \le N \le 2 \cdot 10^5, 0 \le S \le 10^{14}$).
- Dòng 2: $N$ số nguyên không âm $A_1, A_2, \dots, A_N$ ($0 \le A_i \le 10^9$).

## Output
- In ra một số nguyên duy nhất là số lượng đoạn con thỏa mãn.

## Sample 1
### Input
```text
4 5
1 3 2 1
```
### Output
```text
8
```
### Giải thích
Các đoạn con có tổng $\le 5$: $[1], [3], [2], [1], [1, 3], [3, 2], [2, 1], [1, 3, 2]$... Tổng cộng có 8 đoạn.

## Ràng buộc
- $100\%$ số test có $N \le 2 \cdot 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
