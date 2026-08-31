# Đếm Cặp Số Có Hiệu Bằng K

## Bối cảnh
Cho mảng $A$ gồm $N$ số nguyên lớn. Cần đếm số cặp chỉ số $(i, j)$ với $i < j$ sao cho $|A_i - A_j| = K$.

## Nhiệm vụ
In ra số lượng cặp thỏa mãn.

## Input
- Dòng 1: Hai số $N$ và $K$ ($1 \le N \le 10^5, 0 \le K \le 10^9$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \dots, A_N$ ($1 \le A_i \le 10^9$).

## Output
- Số cặp thỏa mãn.

## Sample 1
### Input
```text
5 2
1 5 3 4 2
```
### Output
```text
3
```

## Ràng buộc
- $100\%$ số test có $1 \le N \le 10^5, 0 \le K, A_i \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
