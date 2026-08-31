# Đường Đi Ngắn Nhất Trên Đồ Thị Không Trọng Số

## Bối cảnh
Tìm số cạnh ít nhất trên đường đi từ đỉnh $1$ đến đỉnh $N$ bằng BFS.

## Nhiệm vụ
In ra số cạnh ít nhất hoặc -1 nếu không đến được.

## Input
- Dòng 1: $N, M$ ($1 \le N \le 10^5, 0 \le M \le 2 \cdot 10^5$).
- $M$ dòng tiếp theo: Các cạnh vô hướng.

## Output
- Khoảng cách ngắn nhất.

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
