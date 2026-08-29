# Đếm Cặp Có Tổng Lớn Hơn Hoặc Bằng S

## Bối cảnh
Cho mảng gồm $N$ số nguyên và một số nguyên $S$. Hãy đếm số lượng cặp chỉ số $(i, j)$ với $1 \le i < j \le N$ thỏa mãn:
$$A_i + A_j \ge S$$

## Input
- Dòng 1: Chứa 2 số nguyên $N$ và $S$ ($2 \le N \le 2 \cdot 10^5, -10^{18} \le S \le 10^{18}$).
- Dòng 2: Chứa $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^9 \le A_i \le 10^9$).

## Output
- In ra một số nguyên duy nhất là số lượng cặp thỏa mãn.

## Sample 1
### Input
```text
5 8
2 5 1 4 3
```
### Output
```text
2
```
### Giải thích
Sắp xếp mảng: $[1, 2, 3, 4, 5]$. Các cặp có tổng $\ge 8$ là: $(3, 5)$ (tổng 8), $(4, 5)$ (tổng 9). Tổng cộng có 2 cặp.

## Ràng buộc
- $100\%$ số test có $N \le 2 \cdot 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
