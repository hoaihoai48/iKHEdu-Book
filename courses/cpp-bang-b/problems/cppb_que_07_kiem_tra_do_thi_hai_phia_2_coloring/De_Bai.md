# Kiểm Tra Đồ Thị Hai Phía (Bipartite Graph)

## Bối cảnh
Đồ thị hai phía là đồ thị có thể tô màu toàn bộ các đỉnh bằng 2 màu sao cho không có 2 đỉnh kề nhau nào cùng màu.

## Nhiệm vụ
In `YES` nếu đồ thị là hai phía, ngược lại in `NO`.

## Input
- Dòng 1: $N, M$ ($1 \le N \le 10^5, 0 \le M \le 2 \cdot 10^5$).
- $M$ dòng tiếp theo: Các cạnh vô hướng.

## Output
- `YES` hoặc `NO`.

## Sample 1
### Input
```text
4 4
1 2
2 3
3 4
4 1
```
### Output
```text
YES
```

## Ràng buộc
- $100\%$ số test có $1 \le N \le 10^5, 0 \le M \le 2 \cdot 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
