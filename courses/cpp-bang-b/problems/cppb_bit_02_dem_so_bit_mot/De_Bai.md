# Đếm Số Lượng Bit 1 (Popcount)

## Bối cảnh
Cho một số nguyên không âm $N$ ($0 \le N \le 10^{18}$). Hãy đếm số lượng bit có giá trị bằng $1$ trong biểu diễn nhị phân của số $N$.

## Input
- Dòng 1: Số nguyên dương $T$ ($1 \le T \le 10^5$) là số lượng testcase.
- $T$ dòng tiếp theo: Mỗi dòng gồm một số nguyên $N$ ($0 \le N \le 10^{18}$).

## Output
- In ra $T$ dòng, mỗi dòng là số lượng bit 1 của số $N$ tương ứng.

## Sample 1
### Input
```text
3
5
15
0
```
### Output
```text
2
4
0
```
*(Giải thích: $5 = 101_2$ có 2 bit 1; $15 = 1111_2$ có 4 bit 1; $0$ có 0 bit 1).*

## Ràng buộc
- $100\%$ số test có $N \le 10^{18}, T \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
