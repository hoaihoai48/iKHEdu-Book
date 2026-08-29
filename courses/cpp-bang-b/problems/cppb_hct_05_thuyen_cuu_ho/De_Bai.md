# Ghép Thuyền Cứu Hộ Tối Ưu

## Bối cảnh
Có $N$ người cần qua sông bằng thuyền cứu hộ. Mỗi người thứ $i$ có cân nặng $W_i$. Mỗi chiếc thuyền chở tối đa **2 người** và tổng cân nặng không vượt quá $C$. Hãy tìm số thuyền ít nhất.

## Input
- Dòng 1: 2 số nguyên $N$ và $C$ ($1 \le N \le 10^5, 1 \le C \le 10^9$).
- Dòng 2: $N$ số nguyên $W_1, W_2, \dots, W_N$ ($1 \le W_i \le C$).

## Output
- In ra một số nguyên duy nhất là số thuyền ít nhất cần dùng.

## Sample 1
### Input
```text
4 50
30 20 40 50
```
### Output
```text
3
```

## Ràng buộc
- $100\%$ số test có $N \le 10^5, C \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
