# Đếm Số Lượng Đoạn Con Có Tổng Đúng Bằng S

## Bối cảnh
Cho mảng gồm $N$ số nguyên **dương** $A_1, A_2, \dots, A_N$ ($A_i > 0$) và số nguyên dương $S$. Hãy đếm số lượng đoạn con liên tiếp có tổng đúng bằng $S$.

## Input
- Dòng 1: Chứa 2 số nguyên $N$ và $S$ ($1 \le N \le 2 \cdot 10^5, 1 \le S \le 10^{14}$).
- Dòng 2: $N$ số nguyên dương $A_1, A_2, \dots, A_N$ ($1 \le A_i \le 10^9$).

## Output
- In ra một số nguyên duy nhất là số lượng đoạn con có tổng bằng $S$.

## Sample 1
### Input
```text
5 7
2 4 1 2 7
```
### Output
```text
3
```
### Giải thích
Các đoạn con có tổng bằng 7 là: $[2, 4, 1]$ và $[7]$.

## Ràng buộc
- $100\%$ số test có $N \le 2 \cdot 10^5, A_i > 0$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
