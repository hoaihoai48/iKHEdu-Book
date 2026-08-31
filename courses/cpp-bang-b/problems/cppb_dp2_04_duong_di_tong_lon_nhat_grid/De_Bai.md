# Nhặt Vàng Trên Lưới

## Bối cảnh
Mỗi ô $(i, j)$ chứa $A_{i, j}$ lượng vàng. Đi từ $(1, 1)$ đến $(N, M)$ chỉ sang phải hoặc xuống dưới.

## Nhiệm vụ
Tìm tổng lượng vàng lớn nhất có thể thu thập được.

## Input
- Dòng 1: Hai số $N, M$ ($1 \le N, M \le 1000$).
- $N$ dòng tiếp theo: Ma trận lượng vàng ($0 \le A_{i, j} \le 10^6$).

## Output
- Lượng vàng lớn nhất.

## Sample 1
### Input
```text
3 3
1 2 3
0 5 0
4 1 2
```
### Output
```text
13
```

## Ràng buộc
- $100\%$ số test có $1 \le N, M \le 1000, 0 \le A_{i, j} \le 10^6$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
