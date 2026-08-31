# Trọng Tâm Của Cây (Tree Centroid)

## Bối cảnh
Trọng tâm của cây là đỉnh mà khi loại bỏ nó, mỗi thành phần liên thông còn lại có số đỉnh không vượt quá $N / 2$.

## Nhiệm vụ
Tìm một trọng tâm của cây.

## Input
- Dòng 1: Số nguyên $N$ ($1 \le N \le 10^5$).
- $N - 1$ dòng tiếp theo: Các cạnh của cây.

## Output
- Số hiệu đỉnh trọng tâm.

## Sample 1
### Input
```text
5
1 2
2 3
3 4
3 5
```
### Output
```text
3
```

## Ràng buộc
- $100\%$ số test có $1 \le N \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
