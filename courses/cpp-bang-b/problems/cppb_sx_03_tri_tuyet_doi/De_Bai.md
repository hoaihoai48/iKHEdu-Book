# Sắp Xếp Theo Trị Tuyệt Đối

## Bối cảnh
Cho một dãy gồm $N$ số nguyên. Hãy sắp xếp các phần tử theo giá trị tuyệt đối tăng dần. Nếu hai phần tử có cùng giá trị tuyệt đối, số âm phải đứng trước số dương.

## Input
- Dòng 1: Số nguyên dương $N$ ($1 \le N \le 10^5$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^9 \le A_i \le 10^9$).

## Output
- In ra dãy số sau khi sắp xếp, cách nhau bởi một khoảng trắng.

## Sample 1
### Input
```text
5
5 -8 2 -3 8
```
### Output
```text
2 -3 5 -8 8
```

## Ràng buộc
- $40\%$ số test có $N \le 1000$.
- $60\%$ số test có $N \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
