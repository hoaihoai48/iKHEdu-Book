# Truy Vấn Ma Trận Đa Vùng Cực Đại

## Bối cảnh
Cho một ma trận $N \times M$. Mỗi truy vấn cung cấp tọa độ hai hình chữ nhật rời nhau $R_1$ và $R_2$. Hãy tính tổng của tất cả các phần tử thuộc cả hai hình chữ nhật này.

## Input
- Dòng 1: Gồm 3 số nguyên $N, M, Q$ ($1 \le N, M \le 1500, 1 \le Q \le 10^5$).
- $N$ dòng tiếp theo: Mỗi dòng gồm $M$ số nguyên $A_{i, j}$ ($|A_{i, j}| \le 10^9$).
- $Q$ dòng tiếp theo: Mỗi dòng gồm 8 số $x_1, y_1, x_2, y_2, u_1, v_1, u_2, v_2$ mô tả hình chữ nhật 1 và hình chữ nhật 2.

## Output
- In ra $Q$ dòng kết quả.

## Sample 1
### Input
```text
3 3 1
1 2 3
4 5 6
7 8 9
1 1 1 1 3 3 3 3
```
### Output
```text
10
```
*(Giải thích: Ô $(1, 1)$ có giá trị 1 và ô $(3, 3)$ có giá trị 9, tổng là $1 + 9 = 10$).*

## Ràng buộc
- $100\%$ số test có $N, M \le 1500, Q \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
