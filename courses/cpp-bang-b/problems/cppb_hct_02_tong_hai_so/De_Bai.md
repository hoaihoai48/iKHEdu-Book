# Cặp Số Có Tổng Bằng S (Two Sum)

## Bối cảnh
Cho một mảng gồm $N$ số nguyên và một số nguyên $S$. Hãy tìm hai phần tử ở hai vị trí khác nhau trong mảng có tổng đúng bằng $S$. Nếu có nhiều cặp thỏa mãn, in ra một cặp bất kỳ theo thứ tự tăng dần. Nếu không tồn tại, in ra `-1`.

## Input
- Dòng 1: Chứa 2 số nguyên $N$ và $S$ ($2 \le N \le 10^5, -10^{18} \le S \le 10^{18}$).
- Dòng 2: Chứa $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^9 \le A_i \le 10^9$).

## Output
- In ra 2 số nguyên là giá trị của 2 phần tử tìm được theo thứ tự tăng dần, hoặc `-1` nếu không có nghiệm.

## Sample 1
### Input
```text
5 20
19 2 8 12 5
```
### Output
```text
8 12
```

## Ràng buộc
- $40\%$ số test có $N \le 1000$.
- $60\%$ số test có $N \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
