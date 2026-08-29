# Đoạn Con Cân Bằng Số Lượng 0 và 1

## Bối cảnh
Cho một mảng nhị phân gồm $N$ phần tử chỉ chứa các số 0 và 1. Hãy tìm độ dài của đoạn con liên tiếp dài nhất chứa số lượng số 0 bằng đúng số lượng số 1.

## Input
- Dòng 1: Số nguyên dương $N$ ($1 \le N \le 2 \cdot 10^5$).
- Dòng 2: $N$ số nhị phân $A_1, A_2, \dots, A_N$ ($A_i \in \{0, 1\}$).

## Output
- In ra một số nguyên duy nhất là độ dài lớn nhất tìm được. Nếu không có đoạn nào, in ra `0`.

## Sample 1
### Input
```text
6
0 1 0 0 1 1
```
### Output
```text
6
```

## Ràng buộc
- $100\%$ số test có $N \le 2 \cdot 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
