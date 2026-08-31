# Phát Hiện Chu Trình Trên Đồ Thị Vô Hướng

## Bối cảnh
Kiểm tra xem đồ thị vô hướng $N$ đỉnh $M$ cạnh có chứa chu trình hay không.

## Nhiệm vụ
In `YES` nếu có chu trình, ngược lại in `NO`.

## Input
- Dòng 1: $N, M$ ($1 \le N \le 10^5, 0 \le M \le 2 \cdot 10^5$).
- $M$ dòng tiếp theo: Các cạnh vô hướng.

## Output
- `YES` hoặc `NO`.

## Sample 1
### Input
```text
3 3
1 2
2 3
3 1
```
### Output
```text
YES
```

## Ràng buộc
- $100\%$ số test có $1 \le N \le 10^5, 0 \le M \le 2 \cdot 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
