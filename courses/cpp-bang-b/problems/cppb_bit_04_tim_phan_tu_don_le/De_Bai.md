# Tìm Phần Tử Xuất Hiện 1 Lần Duy Nhất

## Bối cảnh
Cho một mảng gồm $2N + 1$ số nguyên. Trong đó, có đúng một phần tử xuất hiện đúng 1 lần duy nhất, còn tất cả các phần tử khác đều xuất hiện đúng 2 lần.

## Nhiệm vụ
Hãy tìm giá trị của phần tử xuất hiện 1 lần duy nhất đó với độ phức tạp thời gian $\mathcal{O}(N)$ và bộ nhớ $\mathcal{O}(1)$.

## Input
- Dòng 1: Số nguyên dương $N$ ($1 \le N \le 10^5$, mảng có $2N+1$ phần tử).
- Dòng 2: $2N + 1$ số nguyên $A_1, A_2, \dots, A_{2N+1}$ ($0 \le A_i \le 10^9$).

## Output
- In ra một số nguyên duy nhất là phần tử xuất hiện 1 lần.

## Sample 1
### Input
```text
2
4 1 2 1 2
```
### Output
```text
4
```

## Ràng buộc
- $100\%$ số test có $N \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
