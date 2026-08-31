# Dãy Con Tăng Dài Nhất LIS Bằng Fenwick Tree

## Bối cảnh
Tính độ dài của dãy con tăng dài nhất bằng cách dùng Fenwick Tree làm bảng tra cứu max prefix trên mảng nén.

## Nhiệm vụ
In ra độ dài LIS.

## Input
- Dòng 1: Số nguyên $N$ ($1 \le N \le 10^5$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \dots, A_N$ ($1 \le A_i \le 10^9$).

## Output
- Độ dài LIS.

## Sample 1
### Input
```text
6
5 2 7 4 3 8
```
### Output
```text
3
```

## Ràng buộc
- $100\%$ số test có $1 \le N \le 10^5, 1 \le A_i \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
