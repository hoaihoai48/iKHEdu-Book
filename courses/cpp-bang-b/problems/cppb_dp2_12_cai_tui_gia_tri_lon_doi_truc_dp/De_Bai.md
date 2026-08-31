# Cái Túi Khối Lượng Cực Đại W <= 10^9 (Đổi Trục DP)

## Bối cảnh
Trong bài toán cái túi 0/1, khối lượng $W$ có thể lên tới $10^9$ nhưng số lượng đồ vật $N \le 100$ và mỗi giá trị $V_i \le 1000$ (tổng giá trị $\le 10^5$).

## Nhiệm vụ
Tìm tổng giá trị lớn nhất sao cho tổng khối lượng không vượt quá $W$.

## Input
- Dòng 1: Hai số $N$ và $W$ ($1 \le N \le 100, 1 \le W \le 10^9$).
- $N$ dòng tiếp theo: $W_i, V_i$ ($1 \le W_i \le 10^9, 1 \le V_i \le 1000$).

## Output
- Tổng giá trị lớn nhất.

## Sample 1
### Input
```text
3 8
3 30
4 50
5 60
```
### Output
```text
90
```

## Ràng buộc
- $100\%$ số test có $1 \le N \le 100, 1 \le W \le 10^9, 1 \le V_i \le 1000$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
