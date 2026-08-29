# Tập Hợp Độc Lập Về Bit Lớn Nhất

## Bối cảnh
Cho một tập hợp gồm $N$ số nguyên dương $A_0, A_1, \dots, A_{N-1}$ ($N \le 22$). Hãy tìm kích thước của tập hợp con lớn nhất sao cho hai phần tử bất kỳ $A_i, A_j$ trong tập con đều **không có chung bất kỳ bit 1 nào** (tức $A_i \ \& \ A_j = 0$).

## Input
- Dòng 1: Số nguyên dương $N$ ($1 \le N \le 22$).
- Dòng 2: $N$ số nguyên dương $A_0, A_1, \dots, A_{N-1}$ ($1 \le A_i \le 10^9$).

## Output
- In ra một số nguyên duy nhất là kích thước lớn nhất của tập con độc lập về bit.

## Sample 1
### Input
```text
4
1 2 4 3
```
### Output
```text
3
```
*(Giải thích: Tập $\{1, 2, 4\}$ có biểu diễn nhị phân $001_2, 010_2, 100_2$, đôi một có tích AND bằng 0, kích thước 3).*

## Ràng buộc
- $100\%$ số test có $N \le 22, A_i \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
