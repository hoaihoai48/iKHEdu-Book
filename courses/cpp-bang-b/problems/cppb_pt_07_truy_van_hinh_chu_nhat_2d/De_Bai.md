# Truy Vấn Tổng Hình Chữ Nhật 2D

## Bối cảnh
Cho ma trận số nguyên $A$ kích thước $N \times M$. Hãy trả lời $Q$ truy vấn, mỗi truy vấn yêu cầu tính tổng các phần tử trong hình chữ nhật có góc trái trên tại $(x_1, y_1)$ và góc phải dưới tại $(x_2, y_2)$.

## Input
- Dòng 1: Gồm 3 số nguyên $N, M, Q$ ($1 \le N, M \le 1000, 1 \le Q \le 10^5$).
- $N$ dòng tiếp theo: Mỗi dòng gồm $M$ số nguyên $A_{i, j}$ ($|A_{i, j}| \le 10^9$).
- $Q$ dòng tiếp theo: Mỗi dòng gồm 4 số nguyên $x_1, y_1, x_2, y_2$ ($1 \le x_1 \le x_2 \le N, 1 \le y_1 \le y_2 \le M$).

## Output
- In ra $Q$ dòng, mỗi dòng là tổng hình chữ nhật tương ứng.

## Sample 1
### Input
```text
3 3 2
1 2 3
4 5 6
7 8 9
1 1 2 2
2 2 3 3
```
### Output
```text
12
28
```

## Ràng buộc
- $100\%$ số test có $N, M \le 1000, Q \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
