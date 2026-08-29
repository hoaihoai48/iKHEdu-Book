# Tìm Hình Vuông K x K Có Tổng Lớn Nhất

## Bối cảnh
Cho ma trận $A$ kích thước $N \times M$ và một số nguyên dương $K$ ($K \le \min(N, M)$). Hãy tìm hình vuông con kích thước $K \times K$ có tổng các phần tử lớn nhất.

## Input
- Dòng 1: Gồm 3 số nguyên $N, M, K$ ($1 \le N, M \le 1000, 1 \le K \le \min(N, M)$).
- $N$ dòng tiếp theo: Mỗi dòng gồm $M$ số nguyên $A_{i, j}$ ($|A_{i, j}| \le 10^9$).

## Output
- In ra một số nguyên duy nhất là tổng lớn nhất của hình vuông $K \times K$.

## Sample 1
### Input
```text
3 3 2
1 1 1
1 2 2
1 2 2
```
### Output
```text
8
```

## Ràng buộc
- $100\%$ số test có $N, M \le 1000, |A_{i,j}| \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
