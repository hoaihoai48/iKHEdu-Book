# Tìm Hai Số Xuất Hiện 1 Lần Duy Nhất

## Bối cảnh
Cho một mảng gồm $2N + 2$ số nguyên. Trong mảng có đúng hai số nguyên $X$ và $Y$ ($X < Y$) xuất hiện đúng 1 lần duy nhất, còn tất cả các số khác đều xuất hiện đúng 2 lần.

## Nhiệm vụ
Hãy tìm hai số $X$ và $Y$.

## Input
- Dòng 1: Số nguyên dương $N$ ($1 \le N \le 10^5$, tổng số phần tử là $2N+2$).
- Dòng 2: $2N + 2$ số nguyên $A_1, A_2, \dots, A_{2N+2}$ ($0 \le A_i \le 10^9$).

## Output
- In ra hai số $X$ và $Y$ ($X < Y$) cách nhau bởi khoảng trắng.

## Sample 1
### Input
```text
2
1 2 1 3 2 5
```
### Output
```text
3 5
```

## Ràng buộc
- $100\%$ số test có $N \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
