# Thoát Khỏi Mê Cung Quái Vật (Monsters Maze)

## Bối cảnh
Bạn đứng ở `A`, có nhiều quái vật ở các vị trí `M`. Mỗi giây, bạn và quái vật cùng di chuyển 4 hướng. Bạn thoát thành công nếu đến được một ô biên của ma trận trước quái vật.

## Nhiệm vụ
In `YES` nếu có thể thoát hiểm, ngược lại in `NO`.

## Input
- Dòng 1: $N, M$ ($1 \le N, M \le 500$).
- $N$ dòng tiếp theo: Ma trận gồm `#`, `.`, `A`, `M`.

## Output
- `YES` hoặc `NO`.

## Sample 1
### Input
```text
5 8
########
#M..A..#
#.#.M#.#
#M#..#..#
#.######
```
### Output
```text
YES
```

## Ràng buộc
- $100\%$ số test có $1 \le N, M \le 500$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
