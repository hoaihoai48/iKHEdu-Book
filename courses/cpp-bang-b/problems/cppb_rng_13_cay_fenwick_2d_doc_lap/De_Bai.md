# Cây Fenwick 2D Tính Tổng Hình Chữ Nhật (2D BIT)

## Bối cảnh
Hỗ trợ `1 r c val` (cộng thêm `val` vào ô $(r, c)$) và `2 r1 c1 r2 c2` (tính tổng các phần tử trong hình chữ nhật con $[r_1, r_2] \times [c_1, c_2]$).

## Nhiệm vụ
In ra tổng hình chữ nhật cho mỗi truy vấn loại 2.

## Input
- Dòng 1: $N, M, Q$ ($1 \le N, M \le 1000, 1 \le Q \le 50000$).
- $Q$ dòng tiếp theo: Các truy vấn.

## Output
- Kết quả các truy vấn loại 2.

## Sample 1
### Input
```text
3 3 3
1 1 1 5
1 2 2 10
2 1 1 2 2
```
### Output
```text
15
```

## Ràng buộc
- $100\%$ số test có $1 \le N, M \le 1000, 1 \le Q \le 50000$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
