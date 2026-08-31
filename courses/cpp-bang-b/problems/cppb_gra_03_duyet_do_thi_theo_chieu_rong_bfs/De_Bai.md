# Duyệt Đồ Thị Theo Chiều Rộng (BFS Traversal)

## Bối cảnh
Duyệt đồ thị vô hướng từ đỉnh $S$ bằng BFS (ưu tiên các đỉnh kề có số hiệu nhỏ hơn).

## Nhiệm vụ
In ra thứ tự duyệt BFS.

## Input
- Dòng 1: $N, M, S$ ($1 \le N \le 10^5, 0 \le M \le 2 \cdot 10^5$).
- $M$ dòng tiếp theo: Các cạnh vô hướng.

## Output
- Thứ tự các đỉnh được thăm.

## Sample 1
### Input
```text
4 3 1
1 2
1 3
2 4
```
### Output
```text
1 2 3 4
```

## Ràng buộc
- $100\%$ số test có $1 \le N \le 10^5, 0 \le M \le 2 \cdot 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
