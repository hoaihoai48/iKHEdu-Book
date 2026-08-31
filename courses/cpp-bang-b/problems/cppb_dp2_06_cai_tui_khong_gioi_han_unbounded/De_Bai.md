# Cái Túi Không Giới Hạn (Unbounded Knapsack)

## Bối cảnh
Có $N$ loại đồ vật với khối lượng $W_i$ và giá trị $V_i$. Mỗi loại đồ vật có thể chọn số lượng không giới hạn.

## Nhiệm vụ
Tìm tổng giá trị lớn nhất sao cho tổng khối lượng không vượt quá $W$.

## Input
- Dòng 1: Hai số $N$ và $W$ ($1 \le N \le 1000, 1 \le W \le 10^4$).
- $N$ dòng tiếp theo: $W_i, V_i$ ($1 \le W_i \le W, 1 \le V_i \le 10^6$).

## Output
- Tổng giá trị lớn nhất.

## Sample 1
### Input
```text
3 8
2 10
3 15
4 40
```
### Output
```text
80
```

## Ràng buộc
- $100\%$ số test có $1 \le N \le 1000, 1 \le W \le 10^4$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
