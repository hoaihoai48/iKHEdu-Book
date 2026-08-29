# Tìm Đỉnh Của Dãy Núi (Peak in Mountain Array)

## Bối cảnh
Một mảng $A$ gồm $N$ số nguyên ($N \ge 3$) được gọi là một **dãy núi** nếu tồn tại chỉ số đỉnh $P$ ($1 < P < N$) sao cho:
$$A_1 < A_2 < \dots < A_{P-1} < A_P > A_{P+1} > \dots > A_N$$

## Nhiệm vụ
Hãy tìm chỉ số $P$ (1-based) của đỉnh núi trong thời gian $\mathcal{O}(\log N)$.

## Input
- Dòng 1: Số nguyên dương $N$ ($3 \le N \le 10^5$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \dots, A_N$ ($0 \le A_i \le 10^9$).

## Output
- In ra một số nguyên duy nhất là chỉ số của đỉnh núi (1-based).

## Sample 1
### Input
```text
5
1 3 5 4 2
```
### Output
```text
3
```

## Ràng buộc
- $100\%$ số test có $3 \le N \le 10^5$. Dữ liệu đảm bảo mảng luôn có dạng dãy núi hợp lệ.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
