# Đoạn Con Có Tổng Chia Hết Cho K

## Bối cảnh
Cho mảng số nguyên gồm $N$ phần tử và một số nguyên dương $K$. Hãy đếm số lượng đoạn con liên tiếp khác rỗng có tổng các phần tử chia hết cho $K$.

## Input
- Dòng 1: Gồm 2 số nguyên $N, K$ ($1 \le N \le 2 \cdot 10^5, 1 \le K \le 10^5$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \dots, A_N$ ($|A_i| \le 10^9$).

## Output
- In ra một số nguyên duy nhất là số lượng đoạn con có tổng chia hết cho $K$.

## Sample 1
### Input
```text
5 3
4 5 0 -2 -3
```
### Output
```text
7
```

## Ràng buộc
- $100\%$ số test có $N \le 2 \cdot 10^5, K \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
