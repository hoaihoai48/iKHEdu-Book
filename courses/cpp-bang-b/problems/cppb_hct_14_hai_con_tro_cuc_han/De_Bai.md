# Cặp Số Tối Ưu Với Chênh Lệch Cực Hạn

## Bối cảnh
Cho 2 dãy số nguyên $A$ gồm $N$ phần tử và $B$ gồm $M$ phần tử. Hãy tìm một phần tử $A_i$ và một phần tử $B_j$ sao cho độ chênh lệch $|A_i - B_j|$ là nhỏ nhất có thể.

## Input
- Dòng 1: 2 số nguyên $N$ và $M$ ($1 \le N, M \le 2 \cdot 10^5$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^{18} \le A_i \le 10^{18}$).
- Dòng 3: $M$ số nguyên $B_1, B_2, \dots, B_M$ ($-10^{18} \le B_j \le 10^{18}$).

## Output
- In ra một số nguyên duy nhất là giá trị chênh lệch nhỏ nhất $|A_i - B_j|$.

## Sample 1
### Input
```text
3 3
1 5 10
2 8 14
```
### Output
```text
1
```
### Giải thích
Chọn $A_1 = 1, B_1 = 2$ có chênh lệch $|1 - 2| = 1$.

## Ràng buộc
- $100\%$ số test có $N, M \le 2 \cdot 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
