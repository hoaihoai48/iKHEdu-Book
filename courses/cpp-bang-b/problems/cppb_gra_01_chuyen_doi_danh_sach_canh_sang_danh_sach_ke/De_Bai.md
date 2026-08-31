# Chuyển Danh Sách Cạnh Sang Danh Sách Kề

## Bối cảnh
Cho đồ thị vô hướng $N$ đỉnh $M$ cạnh. Cần chuyển đổi biểu diễn đồ thị sang danh sách kề.

## Nhiệm vụ
In ra $N$ dòng: Mỗi dòng gồm bậc của đỉnh và danh sách các đỉnh kề tăng dần.

## Input
- Dòng 1: $N, M$ ($1 \le N \le 10000, 0 \le M \le 20000$).
- $M$ dòng tiếp theo: Mỗi dòng gồm 2 đỉnh $u, v$.

## Output
- $N$ dòng biểu diễn danh sách kề.

## Sample 1
### Input
```text
3 2
1 2
1 3
```
### Output
```text
2 2 3
1 1
1 1
```

## Ràng buộc
- $100\%$ số test có $1 \le N \le 10000, 0 \le M \le 20000$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
