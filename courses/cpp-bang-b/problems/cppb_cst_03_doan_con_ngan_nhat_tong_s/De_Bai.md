# Đoạn Con Ngắn Nhất Có Tổng Đạt S

## Bối cảnh
Cho dãy gồm $N$ số nguyên **không âm** $A_1, A_2, \dots, A_N$ và một số nguyên dương $S$. Hãy tìm độ dài nhỏ nhất của một đoạn con liên tiếp có tổng các phần tử $\ge S$. Nếu không có đoạn con nào thỏa mãn, in ra `-1`.

## Input
- Dòng 1: Chứa 2 số nguyên $N$ và $S$ ($1 \le N \le 10^5, 1 \le S \le 10^{14}$).
- Dòng 2: $N$ số nguyên không âm $A_1, A_2, \dots, A_N$ ($0 \le A_i \le 10^9$).

## Output
- In ra độ dài ngắn nhất hoặc `-1`.

## Sample 1
### Input
```text
6 7
2 3 1 2 4 3
```
### Output
```text
2
```
### Giải thích
Đoạn $[4, 3]$ có tổng là $7 \ge 7$ với độ dài là 2.

## Ràng buộc
- $100\%$ số test có $N \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
