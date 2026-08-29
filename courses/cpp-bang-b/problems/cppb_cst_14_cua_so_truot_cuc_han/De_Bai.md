# Tối Ưu Cửa Sổ Trượt Tuyến Tính Khi N = 2.10⁵

## Bối cảnh
Cho mảng gồm $N$ số nguyên dương và số nguyên $S$. Hãy tìm số lượng đoạn con liên tiếp có tổng các phần tử **nằm trong đoạn $[A, B]$** (tức $A \le \text{tổng} \le B$).

## Input
- Dòng 1: Chứa 3 số nguyên $N, A, B$ ($1 \le N \le 2 \cdot 10^5, 1 \le A \le B \le 10^{14}$).
- Dòng 2: $N$ số nguyên dương $X_1, X_2, \dots, X_N$ ($1 \le X_i \le 10^9$).

## Output
- In ra một số nguyên duy nhất là số lượng đoạn con thỏa mãn.

## Sample 1
### Input
```text
4 3 6
1 2 3 4
```
### Output
```text
5
```
### Giải thích
Các đoạn con có tổng $\in [3, 6]$: $[1, 2]$ (3), $[3]$ (3), $[4]$ (4), $[1, 2, 3]$ (6), $[2, 3]$ (5), $[2, 4]$ không liên tiếp (chỉ tính liên tiếp), $[3]$... Tổng cộng 6 đoạn con.

## Ràng buộc
- $100\%$ số test có $N \le 2 \cdot 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
