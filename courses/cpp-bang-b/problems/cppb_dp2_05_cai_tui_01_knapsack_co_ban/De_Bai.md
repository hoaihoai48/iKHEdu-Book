# Cái Túi 0/1 Cơ Bản (0/1 Knapsack)

## Bối cảnh
Có $N$ món đồ, món thứ $i$ có khối lượng $W_i$ và giá trị $V_i$. Chiếc túi có sức chứa tối đa $W$. Mỗi món chỉ được chọn tối đa 1 lần.

## Nhiệm vụ
Tìm tổng giá trị lớn nhất của các món đồ được chọn sao cho tổng khối lượng không vượt quá $W$.

## Input
- Dòng 1: Hai số nguyên $N$ và $W$ ($1 \le N \le 1000, 1 \le W \le 10^4$).
- $N$ dòng tiếp theo: Mỗi dòng chứa 2 số $W_i, V_i$ ($1 \le W_i \le W, 1 \le V_i \le 10^6$).

## Output
- Giá trị lớn nhất tìm được.

## Sample 1
### Input
```text
4 7
1 1
3 4
4 5
5 7
```
### Output
```text
9
```

## Ràng buộc
- $100\%$ số test có $1 \le N \le 1000, 1 \le W \le 10^4$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
