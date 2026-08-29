# Giá Trị Trung Bình Lớn Nhất Của Đoạn K

## Bối cảnh
Cho một dãy gồm $N$ số nguyên $A_1, A_2, \dots, A_N$ và số nguyên $K$ ($K \le N$). Hãy tìm giá trị trung bình cộng lớn nhất của một đoạn con gồm $K$ phần tử liên tiếp.

## Input
- Dòng 1: Chứa 2 số nguyên $N$ và $K$ ($1 \le K \le N \le 10^5$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^9 \le A_i \le 10^9$).

## Output
- In ra một số thực duy nhất là giá trị trung bình lớn nhất, làm tròn đúng 3 chữ số thập phân sau dấu phẩy.

## Sample 1
### Input
```text
4 2
1 12 -5 6
```
### Output
```text
6.500
```
### Giải thích
Đoạn $[1, 12]$ có trung bình $(1 + 12)/2 = 6.5$.

## Ràng buộc
- $100\%$ số test có $N \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
