# Đường Đi Chi Phí Nhỏ Nhất Trên Lưới

## Bối cảnh
Mỗi ô $(i, j)$ trên ma trận $N \times M$ có chi phí đi qua là $A_{i, j}$. Đi từ $(1, 1)$ đến $(N, M)$ chỉ sang phải hoặc xuống dưới.

## Nhiệm vụ
Tìm tổng chi phí nhỏ nhất của một đường đi.

## Input
- Dòng 1: Hai số nguyên $N, M$ ($1 \le N, M \le 1000$).
- $N$ dòng tiếp theo: Ma trận chi phí ($0 \le A_{i, j} \le 10^6$).

## Output
- Chi phí nhỏ nhất.

## Sample 1
### Input
```text
3 3
1 3 1
1 5 1
4 2 1
```
### Output
```text
7
```

## Ràng buộc
- $100\%$ số test có $1 \le N, M \le 1000, 0 \le A_{i, j} \le 10^6$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
