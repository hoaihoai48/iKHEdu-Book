# 0-1 BFS Tìm Đường Đi Ngắn Nhất Trọng Số 0/1

## Bối cảnh
Cho đồ thị có trọng số trên các cạnh chỉ nhận giá trị 0 hoặc 1. Cần tìm đường đi ngắn nhất từ đỉnh 1 đến $N$ trong $\mathcal{O}(V + E)$.

## Nhiệm vụ
In ra tổng trọng số đường đi ngắn nhất hoặc -1 nếu không đến được.

## Input
- Dòng 1: $N, M$ ($1 \le N \le 10^5, 0 \le M \le 2 \cdot 10^5$).
- $M$ dòng tiếp theo: Mỗi dòng gồm $u, v, w$ ($w \in \{0, 1\}$).

## Output
- Chi phí ngắn nhất.

## Sample 1
### Input
```text
4 4
1 2 1
2 3 0
3 4 1
1 4 1
```
### Output
```text
1
```

## Ràng buộc
- $100\%$ số test có $1 \le N \le 10^5, 0 \le M \le 2 \cdot 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
