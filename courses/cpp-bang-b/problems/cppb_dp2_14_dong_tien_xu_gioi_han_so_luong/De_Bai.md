# Đổi Tiền Giới Hạn Số Lượng (Bounded Knapsack)

## Bối cảnh
Có $N$ loại đồng xu, loại thứ $i$ có mệnh giá $V_i$ và số lượng giới hạn $C_i$.

## Nhiệm vụ
Tìm số lượng đồng xu ít nhất để tạo thành đúng số tiền $S$. Nếu không thể đổi in -1.

## Input
- Dòng 1: Hai số $N$ và $S$ ($1 \le N \le 100, 1 \le S \le 20000$).
- $N$ dòng tiếp theo: $V_i, C_i$ ($1 \le V_i \le 1000, 1 \le C_i \le 100$).

## Output
- Số đồng xu ít nhất hoặc -1.

## Sample 1
### Input
```text
3 11
1 2
5 2
6 1
```
### Output
```text
2
```

## Ràng buộc
- $100\%$ số test có $1 \le N \le 100, 1 \le S \le 20000$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
