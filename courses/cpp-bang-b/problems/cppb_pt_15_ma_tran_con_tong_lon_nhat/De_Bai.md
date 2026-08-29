# Tìm Ma Trận Con Có Tổng Lớn Nhất (Max Submatrix Sum)

## Bối cảnh
Cho ma trận số nguyên $A$ kích thước $N \times M$. Hãy tìm một ma trận con chữ nhật bất kỳ có tổng các phần tử là **lớn nhất có thể**.

## Input
- Dòng 1: Gồm 2 số nguyên $N, M$ ($1 \le N, M \le 400$).
- $N$ dòng tiếp theo: Mỗi dòng gồm $M$ số nguyên $A_{i, j}$ ($|A_{i, j}| \le 10^5$).

## Output
- In ra một số nguyên duy nhất là tổng lớn nhất của ma trận con tìm được.

## Sample 1
### Input
```text
3 3
1 2 -1
-8 -2 5
4 7 -2
```
### Output
```text
14
```
*(Giải thích: Ma trận con $[4, 7]$ và $[5]$... hoặc hình chữ nhật gồm hàng 2..3 cột 2..3: $-2 + 5 + 7 + (-2) = 8$; Ma trận con ở 2 hàng cuối: $(4+7-2) + (-8-2+5) = 9+ (-5) = 4$; Ma trận con 1 hàng $[4, 7] = 11$, $[4, 7, -2] + [-8, -2, 5]...$ đạt tổng lớn nhất là 14 từ $[-2, 5]$ và $[4, 7, -2]...$)*

## Ràng buộc
- $100\%$ số test có $N, M \le 400$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
