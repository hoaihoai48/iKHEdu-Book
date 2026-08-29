# Ghép Cặp Trẻ Em Và Bánh Quy

## Bối cảnh
Có $N$ đứa trẻ và $M$ chiếc bánh quy. Đứa trẻ thứ $i$ có mức độ thèm ăn $G_i$ (chỉ hài lòng nếu nhận được bánh có kích thước $\ge G_i$). Chiếc bánh thứ $j$ có kích thước $S_j$. Mỗi đứa trẻ nhận tối đa 1 bánh và mỗi bánh chỉ phát cho 1 trẻ. Hãy tính số lượng đứa trẻ tối đa có thể được thỏa mãn.

## Input
- Dòng 1: 2 số nguyên $N$ và $M$ ($1 \le N, M \le 10^5$).
- Dòng 2: $N$ số nguyên $G_1, G_2, \dots, G_N$ ($1 \le G_i \le 10^9$).
- Dòng 3: $M$ số nguyên $S_1, S_2, \dots, S_M$ ($1 \le S_j \le 10^9$).

## Output
- In ra số lượng đứa trẻ tối đa được thỏa mãn.

## Sample 1
### Input
```text
3 2
1 2 3
1 1
```
### Output
```text
1
```

## Ràng buộc
- $100\%$ số test có $N, M \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
