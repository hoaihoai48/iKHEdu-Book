# Truy Vết Lộ Trình Ngắn Nhất Bằng BFS

## Bối cảnh
Tìm và in ra chính xác danh sách các đỉnh trên đường đi ngắn nhất từ đỉnh 1 đến đỉnh $N$.

## Nhiệm vụ
Dòng 1: Số đỉnh trên lộ trình. Dòng 2: Danh sách các đỉnh theo thứ tự đi từ 1 đến $N$. (Nếu không có đường đi in -1).

## Input
- Dòng 1: $N, M$ ($1 \le N \le 10^5, 0 \le M \le 2 \cdot 10^5$).
- $M$ dòng tiếp theo: Các cạnh vô hướng.

## Output
- Dòng 1: Số đỉnh.
- Dòng 2: Lộ trình các đỉnh.

## Sample 1
### Input
```text
5 5
1 2
2 3
3 5
1 4
4 5
```
### Output
```text
3
1 4 5
```

## Ràng buộc
- $100\%$ số test có $1 \le N \le 10^5, 0 \le M \le 2 \cdot 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
