# Sắp Xếp Đoạn Thẳng Không Giao Lỗi

## Bối cảnh
Cho $N$ đoạn thẳng $[L_i, R_i]$ trên trục số. Hãy sắp xếp các đoạn thẳng theo tiêu chí:
1. Tọa độ đầu mút $L_i$ tăng dần.
2. Nếu cùng $L_i$, tọa độ $R_i$ giảm dần.
3. Nếu trùng cả $L_i$ và $R_i$, giữ nguyên thứ tự ban đầu (sắp xếp ổn định).

## Input
- Dòng 1: Số nguyên dương $N$ ($1 \le N \le 2 \cdot 10^5$).
- $N$ dòng tiếp theo: Mỗi dòng gồm 2 số nguyên $L_i, R_i$ ($-10^9 \le L_i \le R_i \le 10^9$).

## Output
- In ra $N$ dòng, mỗi dòng gồm 2 số $L_i, R_i$ sau khi sắp xếp.

## Sample 1
### Input
```text
3
2 8
1 5
2 10
```
### Output
```text
1 5
2 10
2 8
```

## Ràng buộc
- $100\%$ số test có $N \le 2 \cdot 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
