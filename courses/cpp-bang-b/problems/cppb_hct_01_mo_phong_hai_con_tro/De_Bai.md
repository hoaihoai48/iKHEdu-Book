# Mô Phỏng Hai Con Trỏ Đối Đầu

## Bối cảnh
Cho mảng $N$ số nguyên đã sắp xếp tăng dần và một số nguyên $S$. Hãy kiểm tra xem trong mảng có tồn tại cặp chỉ số $(i, j)$ với $i < j$ sao cho $A_i + A_j = S$ hay không. Nếu có, in ra `YES`, ngược lại in ra `NO`.

## Input
- Dòng 1: Chứa 2 số nguyên $N$ và $S$ ($2 \le N \le 10^5, -10^{18} \le S \le 10^{18}$).
- Dòng 2: Chứa $N$ số nguyên đã sắp xếp tăng dần $A_1 \le A_2 \le \dots \le A_N$ ($-10^9 \le A_i \le 10^9$).

## Output
- In ra `YES` nếu tồn tại cặp số có tổng bằng $S$, ngược lại in ra `NO`.

## Sample 1
### Input
```text
5 20
2 5 8 12 19
```
### Output
```text
YES
```

## Ràng buộc
- $40\%$ số test có $N \le 1000$.
- $60\%$ số test có $N \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
