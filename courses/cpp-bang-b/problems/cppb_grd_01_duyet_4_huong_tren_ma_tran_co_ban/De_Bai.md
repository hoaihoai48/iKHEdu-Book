# Đếm Số Ô Kề Cạnh Hợp Lệ (4 Hướng)

## Bối cảnh
Cho ma trận $N \times M$ với các ô có chỉ số 0-based từ $(0, 0)$ đến $(N-1, M-1)$. Cho tọa độ $(r, c)$.

## Nhiệm vụ
Đếm số ô kề cạnh (trên, dưới, trái, phải) của ô $(r, c)$ nằm hoàn toàn bên trong ma trận.

## Input
- Một dòng chứa 4 số nguyên $N, M, r, c$ ($1 \le N, M \le 1000, 0 \le r < N, 0 \le c < M$).

## Output
- Số lượng ô kề hợp lệ.

## Sample 1
### Input
```text
3 3 0 0
```
### Output
```text
2
```

## Ràng buộc
- $100\%$ số test có $1 \le N, M \le 1000$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
