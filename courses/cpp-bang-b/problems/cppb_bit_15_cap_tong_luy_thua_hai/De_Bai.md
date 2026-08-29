# Đếm Số Cặp Có Tổng Bằng Lũy Thừa Của 2

## Bối cảnh
Cho một dãy gồm $N$ số nguyên dương $A_1, A_2, \dots, A_N$. Hãy đếm số lượng cặp chỉ số $(i, j)$ thỏa mãn $1 \le i < j \le N$ sao cho tổng $A_i + A_j$ là một lũy thừa của 2 (tức $A_i + A_j = 2^k$ với $k \ge 1$).

## Input
- Dòng 1: Số nguyên dương $N$ ($1 \le N \le 10^5$).
- Dòng 2: $N$ số nguyên dương $A_1, A_2, \dots, A_N$ ($1 \le A_i \le 10^9$).

## Output
- In ra một số nguyên duy nhất là số lượng cặp thỏa mãn.

## Sample 1
### Input
```text
4
1 3 7 15
```
### Output
```text
3
```
*(Giải thích: Các cặp: $(1, 3) \to 4=2^2$, $(1, 7) \to 8=2^3$, $(1, 15) \to 16=2^4$, $(3, 7) \to 10$, $(3, 15) \to 18$, $(7, 15) \to 22$... và các cặp tương ứng).*

## Ràng buộc
- $100\%$ số test có $N \le 10^5, A_i \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
