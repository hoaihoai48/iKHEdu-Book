# Đếm Số Cặp Nghịch Thế (Inversion Count)

## Bối cảnh
Cặp số $(i, j)$ với $i < j$ được gọi là cặp nghịch thế nếu $A[i] > A[j]$.

## Nhiệm vụ
Tính tổng số cặp nghịch thế trong mảng bằng Cây Fenwick kết hợp nén tọa độ.

## Input
- Dòng 1: Số nguyên $N$ ($1 \le N \le 10^5$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \dots, A_N$ ($1 \le A_i \le 10^9$).

## Output
- Số lượng cặp nghịch thế.

## Sample 1
### Input
```text
5
2 4 1 3 5
```
### Output
```text
3
```

## Ràng buộc
- $100\%$ số test có $1 \le N \le 10^5, 1 \le A_i \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
