# Đếm Số Điểm Trong Hình Chữ Nhật (2D Range Query)

## Bối cảnh
Cho $N$ điểm trên mặt phẳng 2D. Cho $Q$ truy vấn hình chữ nhật $[X_1, X_2] \times [Y_1, Y_2]$.

## Nhiệm vụ
Đếm số lượng điểm nằm trong mỗi hình chữ nhật.

## Input
- Dòng 1: $N, Q$ ($1 \le N, Q \le 10000$).
- $N$ dòng tiếp theo: Tọa độ $X_i, Y_i$.
- $Q$ dòng tiếp theo: Các truy vấn $X_1, Y_1, X_2, Y_2$.

## Output
- Kết quả $Q$ truy vấn.

## Sample 1
### Input
```text
3 2
1 1
2 2
3 3
1 1 2 2
2 2 4 4
```
### Output
```text
2
2
```

## Ràng buộc
- $100\%$ số test có $1 \le N, Q \le 10000, 1 \le X_i, Y_i \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
