# Tổng Giá Trị Nhỏ Nhất Của Mọi Đoạn Con

## Bối cảnh
Cho mảng $A$ gồm $N$ phần tử. Với mỗi đoạn con $[i, j]$ ($1 \le i \le j \le N$), gọi $\min(A[i..j])$ là giá trị nhỏ nhất của đoạn đó.

## Nhiệm vụ
Tính tổng giá trị nhỏ nhất của tất cả các đoạn con lấy dư cho $10^9+7$.

## Input
- Dòng 1: Số nguyên $N$ ($1 \le N \le 10^5$).
- Dòng 2: $N$ số nguyên dương $A_1, A_2, \dots, A_N$ ($1 \le A_i \le 10^9$).

## Output
- Tổng theo modulo $10^9 + 7$.

## Sample 1
### Input
```text
4
3 1 2 4
```
### Output
```text
17
```

## Ràng buộc
- $100\%$ số test có $1 \le N \le 10^5, 1 \le A_i \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
