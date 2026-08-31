# Nước Tràn Mê Cung (Multi-Source BFS)

## Bối cảnh
Nước biển tràn vào mê cung từ nhiều nguồn xuất phát cùng lúc. Mỗi giây, nước lan sang các ô lân cận 4 hướng.

## Nhiệm vụ
Tính thời gian ít nhất để nước ngập đến vị trí đích (hoặc -1).

## Input
- Dòng 1: $N, M$ ($1 \le N, M \le 1000$).
- $N$ dòng tiếp theo: Ma trận với `W` (nguồn nước), `E` (đích), `.` (đường), `#` (tường).

## Output
- Thời gian ngập hoặc -1.

## Sample 1
### Input
```text
3 3
W..
.##
..E
```
### Output
```text
4
```

## Ràng buộc
- $100\%$ số test có $1 \le N, M \le 1000$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
