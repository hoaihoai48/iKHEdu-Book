# Cài Đặt Segment Tree Tìm Min Đoạn (RMQ)

## Bối cảnh
Hỗ trợ 2 thao tác: `1 pos val` (Gán $A[pos] = val$) và `2 L R` (Tìm giá trị nhỏ nhất trong đoạn $[L, R]$).

## Nhiệm vụ
In ra giá trị nhỏ nhất cho mỗi truy vấn loại 2.

## Input
- Dòng 1: $N, Q$ ($1 \le N, Q \le 10^5$).
- Dòng 2: $N$ số nguyên ban đầu ($1 \le A_i \le 10^9$).
- $Q$ dòng tiếp theo: Các truy vấn.

## Output
- Kết quả các truy vấn loại 2.

## Sample 1
### Input
```text
5 3
5 2 4 1 3
2 1 3
1 4 10
2 3 5
```
### Output
```text
2
3
```

## Ràng buộc
- $100\%$ số test có $1 \le N, Q \le 10^5, 1 \le A_i, val \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
