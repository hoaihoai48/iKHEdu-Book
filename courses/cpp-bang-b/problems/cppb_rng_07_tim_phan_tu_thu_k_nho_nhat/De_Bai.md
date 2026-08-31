# Tìm Phần Tử Thứ K Nhỏ Nhất (K-th Element on BIT)

## Bối cảnh
Hỗ trợ thao tác `1 x` (thêm phần tử x vào tập đa trùng lặp) và `2 k` (tìm phần tử nhỏ thứ k trong tập).

## Nhiệm vụ
In ra giá trị phần tử thứ k cho các truy vấn loại 2.

## Input
- Dòng 1: Số nguyên $Q$ ($1 \le Q \le 50000$).
- $Q$ dòng tiếp theo: Các truy vấn ($1 \le x \le 2 \cdot 10^5$).

## Output
- Kết quả các truy vấn loại 2.

## Sample 1
### Input
```text
5
1 10
1 20
1 15
2 2
2 3
```
### Output
```text
15
20
```

## Ràng buộc
- $100\%$ số test có $1 \le Q \le 50000, 1 \le x \le 2 \cdot 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
