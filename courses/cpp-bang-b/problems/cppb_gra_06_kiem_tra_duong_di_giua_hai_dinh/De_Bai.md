# Kiểm Tra Đường Đi Giữa Hai Đỉnh

## Bối cảnh
Kiểm tra xem có tồn tại đường đi từ đỉnh $S$ đến đỉnh $T$ trên đồ thị vô hướng hay không.

## Nhiệm vụ
In `YES` nếu có đường đi, ngược lại in `NO`.

## Input
- Dòng 1: $N, M, S, T$ ($1 \le N \le 10^5, 0 \le M \le 2 \cdot 10^5, 1 \le S, T \le N$).
- $M$ dòng tiếp theo: Các cạnh vô hướng.

## Output
- `YES` hoặc `NO`.

## Sample 1
### Input
```text
4 2 1 4
1 2
2 3
```
### Output
```text
NO
```

## Ràng buộc
- $100\%$ số test có $1 \le N \le 10^5, 0 \le M \le 2 \cdot 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
