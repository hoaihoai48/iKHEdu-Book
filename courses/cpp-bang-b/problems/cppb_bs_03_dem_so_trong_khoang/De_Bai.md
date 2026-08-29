# Đếm Số Phần Tử Trong Đoạn [L, R]

## Bối cảnh
Cho mảng gồm $N$ số nguyên (chưa sắp xếp). Có $Q$ câu hỏi, mỗi câu hỏi gồm 2 số $L, R$ ($L \le R$), yêu cầu đếm xem trong mảng có bao nhiêu phần tử có giá trị nằm trong đoạn $[L \dots R]$ (tức $L \le A_i \le R$).

## Input
- Dòng 1: Gồm 2 số nguyên $N, Q$ ($1 \le N, Q \le 10^5$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \dots, A_N$ ($|A_i| \le 10^9$).
- $Q$ dòng tiếp theo: Mỗi dòng gồm 2 số $L, R$ ($|L|, |R| \le 10^9, L \le R$).

## Output
- In ra $Q$ dòng, mỗi dòng là số lượng phần tử thỏa mãn.

## Sample 1
### Input
```text
5 2
5 1 9 3 7
2 8
10 20
```
### Output
```text
3
0
```

## Ràng buộc
- $100\%$ số test có $N, Q \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
