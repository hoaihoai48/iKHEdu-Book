# Bộ Ba Số Có Tổng Bằng S (3-Sum)

## Bối cảnh
Cho mảng gồm $N$ số nguyên và một số nguyên $S$. Hãy tìm 3 phần tử ở 3 vị trí phân biệt trong mảng có tổng đúng bằng $S$. Nếu có nhiều bộ, in ra một bộ bất kỳ theo thứ tự tăng dần. Nếu không tồn tại, in ra `-1`.

## Input
- Dòng 1: Chứa 2 số nguyên $N$ và $S$ ($3 \le N \le 3000, -10^{18} \le S \le 10^{18}$).
- Dòng 2: Chứa $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^9 \le A_i \le 10^9$).

## Output
- In ra 3 số nguyên theo thứ tự tăng dần, hoặc `-1`.

## Sample 1
### Input
```text
6 15
2 7 5 1 8 4
```
### Output
```text
2 5 8
```

## Ràng buộc
- $100\%$ số test có $N \le 3000$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
