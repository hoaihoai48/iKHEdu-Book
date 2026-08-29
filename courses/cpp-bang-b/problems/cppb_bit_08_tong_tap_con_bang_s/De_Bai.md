# Bài Toán Tổng Tập Con Bằng S (Subset Sum)

## Bối cảnh
Cho một dãy gồm $N$ số nguyên dương $A_1, A_2, \dots, A_N$ và một số nguyên dương $S$. Hãy kiểm tra xem có tồn tại một tập con các phần tử có tổng đúng bằng $S$ hay không.

## Input
- Dòng 1: Gồm 2 số nguyên $N, S$ ($1 \le N \le 20, 1 \le S \le 10^9$).
- Dòng 2: $N$ số nguyên dương $A_1, A_2, \dots, A_N$ ($1 \le A_i \le 10^8$).

## Output
- In ra `YES` nếu tồn tại, ngược lại in `NO`.

## Sample 1
### Input
```text
5 12
3 34 4 12 5
```
### Output
```text
YES
```
*(Giải thích: Chọn tập $\{3, 4, 5\}$ hoặc $\{12\}$ có tổng bằng 12).*

## Ràng buộc
- $100\%$ số test có $N \le 20$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
