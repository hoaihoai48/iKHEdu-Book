# BFS Tìm Bước Đi Ngắn Nhất Đồ Thị

## Bối cảnh
Cho đồ thị vô hướng $N$ đỉnh $M$ cạnh không có trọng số. Cần tìm số cạnh ít nhất trên đường đi từ đỉnh 1 đến đỉnh $N$.

## Nhiệm vụ
In ra khoảng cách ngắn nhất hoặc -1 nếu không có đường đi.

## Input
- Dòng 1: Hai số $N$ và $M$ ($1 \le N \le 10^5, 0 \le M \le 2 \cdot 10^5$).
- $M$ dòng tiếp theo: Mỗi dòng gồm 2 đỉnh $u, v$.

## Output
- Số cạnh ít nhất hoặc -1.

## Sample 1
### Input
```text
4 4
1 2
2 3
3 4
1 3
```
### Output
```text
2
```

## Ràng buộc
- $100\%$ số test có $1 \le N \le 10^5, 0 \le M \le 2 \cdot 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
