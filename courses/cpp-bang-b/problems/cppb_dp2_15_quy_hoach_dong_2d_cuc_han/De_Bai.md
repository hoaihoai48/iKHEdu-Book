# Tối Ưu Hóa Túi Đồ Hỗn Hợp (Hybrid Knapsack)

## Bối cảnh
Có $N$ món đồ thuộc 2 loại: Loại 1 (chỉ được dùng 1 lần) và Loại 2 (được dùng không giới hạn số lần). Chiếc túi có sức chứa tối đa $W$.

## Nhiệm vụ
Tìm tổng giá trị lớn nhất có thể thu được.

## Input
- Dòng 1: Hai số $N$ và $W$ ($1 \le N \le 100, 1 \le W \le 5000$).
- $N$ dòng tiếp theo: Mỗi dòng gồm 3 số `type`, `weight`, `val` ($type \in \{1, 2\}, 1 \le weight \le W, 1 \le val \le 10^6$).

## Output
- Tổng giá trị lớn nhất.

## Sample 1
### Input
```text
3 10
1 4 20
2 3 15
1 5 30
```
### Output
```text
50
```

## Ràng buộc
- $100\%$ số test có $1 \le N \le 100, 1 \le W \le 5000$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
