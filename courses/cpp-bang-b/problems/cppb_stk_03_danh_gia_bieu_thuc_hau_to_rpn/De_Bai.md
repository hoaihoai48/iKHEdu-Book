# Đánh Giá Biểu Thức Hậu Tố (Reverse Polish Notation)

## Bối cảnh
Cho danh sách $N$ token biểu diễn một biểu thức toán học dưới dạng Hậu tố (RPN) gồm các số nguyên và 3 toán tử `+`, `-`, `*`.

## Nhiệm vụ
Tính và in ra giá trị của biểu thức.

## Input
- Dòng 1: Số nguyên $N$ ($1 \le N \le 10^5$).
- Dòng 2: $N$ token cách nhau bởi khoảng trắng.

## Output
- Giá trị số nguyên của biểu thức.

## Sample 1
### Input
```text
5
2 1 + 3 *
```
### Output
```text
9
```

## Ràng buộc
- $100\%$ số test có $1 \le N \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
