# Tìm Cặp Có XOR Lớn Nhất Trong Mảng

## Bối cảnh
Cho một mảng gồm $N$ số nguyên không âm $A_1, A_2, \dots, A_N$. Hãy tìm giá trị lớn nhất của biểu thức $A_i \oplus A_j$ với $1 \le i < j \le N$.

## Input
- Dòng 1: Số nguyên dương $N$ ($2 \le N \le 10^5$).
- Dòng 2: $N$ số nguyên không âm $A_1, A_2, \dots, A_N$ ($0 \le A_i \le 10^9$).

## Output
- In ra giá trị XOR lớn nhất tìm được.

## Sample 1
### Input
```text
4
3 10 5 25
```
### Output
```text
28
```
*(Giải thích: Cặp $5 \oplus 25 = 28$).*

## Ràng buộc
- $100\%$ số test có $N \le 10^5, A_i \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
