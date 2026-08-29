# Đoạn Con Có Độ Chênh Lệch Max - Min Không Quá K

## Bối cảnh
Cho mảng gồm $N$ số nguyên và số nguyên không âm $K$. Hãy tìm độ dài của đoạn con liên tiếp dài nhất sao cho chênh lệch giữa phần tử lớn nhất và nhỏ nhất trong đoạn đó không vượt quá $K$ (tức $\max - \min \le K$).

## Input
- Dòng 1: Chứa 2 số nguyên $N$ và $K$ ($1 \le N \le 5000, 0 \le K \le 10^9$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^9 \le A_i \le 10^9$).

## Output
- In ra độ dài lớn nhất của đoạn con thỏa mãn.

## Sample 1
### Input
```text
6 3
8 2 4 7 3 9
```
### Output
```text
2
```
### Giải thích
Đoạn $[2, 4, 3]$ hoặc $[4, 7, 3]$ có chênh lệch $\max - \min \le 3$ với độ dài 3.

## Ràng buộc
- $100\%$ số test có $N \le 5000$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
