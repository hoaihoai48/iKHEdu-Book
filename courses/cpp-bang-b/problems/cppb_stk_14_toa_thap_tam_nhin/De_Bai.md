# Tầm Nhìn Tòa Tháp (Stock Span)

## Bối cảnh
Có $N$ tòa tháp xếp thành một hàng. Tầm nhìn sang trái của tòa tháp $i$ là số lượng tòa tháp liên tiếp về phía trước có chiều cao $\le H_i$ (tính cả chính nó).

## Nhiệm vụ
In ra tầm nhìn của từng tòa tháp.

## Input
- Dòng 1: Số nguyên $N$ ($1 \le N \le 10^5$).
- Dòng 2: $N$ số nguyên $H_1, H_2, \dots, H_N$ ($1 \le H_i \le 10^9$).

## Output
- $N$ số nguyên.

## Sample 1
### Input
```text
7
100 80 60 70 60 75 85
```
### Output
```text
1 1 1 2 1 4 6
```

## Ràng buộc
- $100\%$ số test có $1 \le N \le 10^5, 1 \le H_i \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
