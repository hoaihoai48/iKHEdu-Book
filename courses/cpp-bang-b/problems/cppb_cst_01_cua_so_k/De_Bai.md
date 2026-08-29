# Tổng Cửa Sổ Cố Định K

## Bối cảnh
Cho một dãy gồm $N$ số nguyên $A_1, A_2, \dots, A_N$ và một số nguyên dương $K$ ($K \le N$). Hãy tìm tổng lớn nhất của một đoạn con gồm đúng $K$ phần tử liên tiếp.

## Input
- Dòng 1: Chứa 2 số nguyên $N$ và $K$ ($1 \le K \le N \le 10^5$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^9 \le A_i \le 10^9$).

## Output
- In ra một số nguyên duy nhất là tổng lớn nhất của đoạn $K$ phần tử liên tiếp.

## Sample 1
### Input
```text
6 3
2 1 5 1 3 2
```
### Output
```text
9
```
### Giải thích
Đoạn $[5, 1, 3]$ có tổng $5 + 1 + 3 = 9$ là lớn nhất.

## Ràng buộc
- $100\%$ số test có $N \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
