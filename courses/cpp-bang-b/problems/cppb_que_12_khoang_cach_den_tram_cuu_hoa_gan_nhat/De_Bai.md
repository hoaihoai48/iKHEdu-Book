# Khoảng Cách Đến Trạm Cứu Hỏa Gần Nhất (Multi-Source BFS)

## Bối cảnh
Trong thành phố có $N$ ngôi nhà và $K$ trạm cứu hỏa. Cần tính khoảng cách ngắn nhất từ mỗi ngôi nhà đến trạm cứu hỏa gần nhất.

## Nhiệm vụ
In ra khoảng cách của từng ngôi nhà từ 1 đến $N$.

## Input
- Dòng 1: $N, M, K$ ($1 \le N \le 10^5, 0 \le M \le 2 \cdot 10^5, 1 \le K \le N$).
- Dòng 2: Danh sách $K$ trạm cứu hỏa.
- $M$ dòng tiếp theo: Các con đường nối giữa hai nhà.

## Output
- $N$ số nguyên.

## Sample 1
### Input
```text
4 3 2
1 4
1 2
2 3
3 4
```
### Output
```text
0 1 1 0
```

## Ràng buộc
- $100\%$ số test có $1 \le N \le 10^5, 0 \le M \le 2 \cdot 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
