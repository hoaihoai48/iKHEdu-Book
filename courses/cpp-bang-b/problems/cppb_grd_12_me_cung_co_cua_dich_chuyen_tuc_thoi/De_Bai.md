# Cổng Dịch Chuyển Tức Thời (Teleport Maze)

## Bối cảnh
Các ô có cùng chữ cái in hoa `A` đến `Z` là các cổng dịch chuyển tức thời (bước vào cổng này có thể nhảy sang cổng cùng chữ cái khác trong 0 bước).

## Nhiệm vụ
Tìm số bước đi ngắn nhất từ ô $(0, 0)$ đến $(N-1, M-1)$.

## Input
- Dòng 1: $N, M$ ($1 \le N, M \le 500$).
- $N$ dòng tiếp theo biểu diễn ma trận.

## Output
- Số bước ngắn nhất.

## Sample 1
### Input
```text
3 3
..A
.##
A..
```
### Output
```text
2
```

## Ràng buộc
- $100\%$ số test có $1 \le N, M \le 500$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
