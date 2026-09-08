# Đếm Số Cặp Có Tổng Bằng Lũy Thừa Của 2

## Bối cảnh
Trong một hệ thống tính toán lượng tử, hai trạng thái qubit có năng lượng A[i] và A[j] chỉ có thể tương tác cộng hưởng nếu tổng năng lượng của chúng đúng bằng một lũy thừa của 2 (nghĩa là A[i] + A[j] = 2^k với k >= 0). Hãy đếm số lượng cặp trạng thái có thể tương tác cộng hưởng.

## Nhiệm vụ
Cho dãy gồm N số nguyên dương. Hãy đếm số lượng cặp chỉ số (i, j) với 1 <= i < j <= N sao cho A[i] + A[j] là một lũy thừa của 2.

## Input
- Dòng 1: Số nguyên dương $N$ ($2 \le N \le 10^5$).
- Dòng 2: $N$ số nguyên dương $A_1, A_2, \dots, A_N$ ($1 \le A_i \le 10^9$).

## Output
- In ra số lượng cặp thỏa mãn.

## Sample 1
### Input
```text
4
1 1 3 3
```
### Output
```text
4
```
### Giải thích
Các cặp chỉ số $(i, j)$ có tổng là lũy thừa của 2 gồm 3 cặp:

- $(1, 3)$: tổng $1 + 3 = 4 = 2^2$.
- $(1, 7)$: tổng $1 + 7 = 8 = 2^3$.
- $(1, 15)$: tổng $1 + 15 = 16 = 2^4$.
Vậy có đúng 3 cặp thỏa mãn.

## Ràng buộc
- $100\%$ số test có $N \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
