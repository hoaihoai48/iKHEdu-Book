# Tìm Cặp Có Hiệu Đúng Bằng K

## Bối cảnh
Cho mảng gồm $N$ số nguyên và số nguyên không âm $K$. Hãy kiểm tra xem có tồn tại cặp chỉ số $(i, j)$ với $i \neq j$ sao cho $A_j - A_i = K$ hay không. Nếu có in ra `YES`, ngược lại in ra `NO`.

## Input
- Dòng 1: Chứa 2 số nguyên $N$ và $K$ ($2 \le N \le 10^5, 0 \le K \le 10^{18}$).
- Dòng 2: Chứa $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^9 \le A_i \le 10^9$).

## Output
- In ra `YES` hoặc `NO`.

## Sample 1
### Input
```text
5 3
1 8 5 3 2
```
### Output
```text
YES
```
### Giải thích
Cặp $(5, 8)$ hoặc $(2, 5)$ có hiệu $8 - 5 = 3 = K$.

## Ràng buộc
- $100\%$ số test có $N \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
