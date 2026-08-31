# Đếm Số Cạnh Cầu Trên Đồ Thị (Bridges)

## Bối cảnh
Cạnh cầu là cạnh mà khi xóa bỏ nó, số thành phần liên thông của đồ thị sẽ tăng lên (thuật toán Tarjan cơ bản).

## Nhiệm vụ
In ra số lượng cạnh cầu trên đồ thị.

## Input
- Dòng 1: $N, M$ ($1 \le N \le 50000, 0 \le M \le 10^5$).
- $M$ dòng tiếp theo: Các cạnh vô hướng.

## Output
- Số lượng cạnh cầu.

## Sample 1
### Input
```text
5 5
1 2
2 3
3 1
3 4
4 5
```
### Output
```text
2
```

## Ràng buộc
- $100\%$ số test có $1 \le N \le 50000, 0 \le M \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
