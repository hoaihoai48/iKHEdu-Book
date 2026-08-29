# Đoạn Con Dài Nhất Có Tổng Không Quá S

## Bối cảnh
Cho dãy gồm $N$ số nguyên **không âm** $A_1, A_2, \dots, A_N$ và một số nguyên dương $S$. Hãy tìm độ dài lớn nhất của một đoạn con liên tiếp có tổng các phần tử $\le S$.

## Input
- Dòng 1: Chứa 2 số nguyên $N$ và $S$ ($1 \le N \le 2 \cdot 10^5, 1 \le S \le 10^{14}$).
- Dòng 2: $N$ số nguyên không âm $A_1, A_2, \dots, A_N$ ($0 \le A_i \le 10^9$).

## Output
- In ra một số nguyên duy nhất là độ dài lớn nhất của đoạn con thỏa mãn.

## Sample 1
### Input
```text
5 7
3 1 2 1 4
```
### Output
```text
4
```
### Giải thích
Đoạn $[3, 1, 2, 1]$ có tổng là $7 \le 7$ với độ dài là 4.

## Ràng buộc
- $100\%$ số test có $N \le 2 \cdot 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
