# Truy Vấn Ước Chung Lớn Nhất Đoạn (Range GCD)

## Bối cảnh
Hỗ trợ cập nhật điểm `1 pos val` và truy vấn `2 L R` tính $\text{GCD}(A[L \dots R])$.

## Nhiệm vụ
In ra GCD của đoạn $[L, R]$.

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
2 4 6 8 10
2 1 3
1 2 12
2 1 3
```
### Output
```text
2
2
```

## Ràng buộc
- $100\%$ số test có $1 \le N, Q \le 10^5, 1 \le A_i, val \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
