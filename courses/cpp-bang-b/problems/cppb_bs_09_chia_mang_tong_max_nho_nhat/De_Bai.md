# Chia Mảng Thành K Đoạn Có Tổng Max Nhỏ Nhất

## Bối cảnh
Cho một dãy gồm $N$ số nguyên dương $A_1, A_2, \dots, A_N$. Hãy chia dãy số này thành đúng $K$ đoạn con liên tiếp sao cho **tổng lớn nhất của một đoạn con là nhỏ nhất có thể**.

## Input
- Dòng 1: Gồm 2 số nguyên $N, K$ ($1 \le K \le N \le 10^5$).
- Dòng 2: $N$ số nguyên dương $A_1, A_2, \dots, A_N$ ($1 \le A_i \le 10^9$).

## Output
- In ra một số nguyên duy nhất là tổng đoạn con lớn nhất nhỏ nhất có thể đạt được.

## Sample 1
### Input
```text
5 3
7 2 5 10 8
```
### Output
```text
14
```
*(Giải thích: Chia thành 3 đoạn: $[7, 2, 5]$ (tổng 14), $[10]$ (tổng 10), $[8]$ (tổng 8). Tổng lớn nhất là 14).*

## Ràng buộc
- $100\%$ số test có $N \le 10^5, A_i \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
