# Duyệt Đồ Thị Theo Chiều Sâu (DFS Traversal)

## Bối cảnh
Duyệt đồ thị vô hướng bắt đầu từ đỉnh $S$ bằng thuật toán DFS (ưu tiên thăm đỉnh có chỉ số nhỏ hơn trước).

## Nhiệm vụ
In ra thứ tự các đỉnh được thăm.

## Input
- Dòng 1: $N, M, S$ ($1 \le N \le 10^5, 0 \le M \le 2 \cdot 10^5, 1 \le S \le N$).
- $M$ dòng tiếp theo: Các cạnh vô hướng.

## Output
- Thứ tự các đỉnh được thăm.

## Sample 1
### Input
```text
4 3 1
1 2
2 3
1 4
```
### Output
```text
1 2 3 4
```

## Ràng buộc
- $100\%$ số test có $1 \le N \le 10^5, 0 \le M \le 2 \cdot 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
