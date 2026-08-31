# Đoạn Con Có Tổng Lớn Nhất Trên Đoạn (Maximum Subarray Query)

## Bối cảnh
Hỗ trợ cập nhật điểm và truy vấn `2 L R` tìm tổng lớn nhất của một đoạn con liên tiếp nằm trọn trong đoạn $[L, R]$.

## Nhiệm vụ
In ra tổng đoạn con lớn nhất cho mỗi truy vấn loại 2.

## Input
- Dòng 1: $N, Q$ ($1 \le N, Q \le 10^5$).
- Dòng 2: $N$ số nguyên ($-10^9 \le A_i \le 10^9$).
- $Q$ dòng tiếp theo: Các truy vấn.

## Output
- Kết quả các truy vấn loại 2.

## Sample 1
### Input
```text
5 3
1 2 -5 4 5
2 1 5
1 3 10
2 1 5
```
### Output
```text
9
22
```

## Ràng buộc
- $100\%$ số test có $1 \le N, Q \le 10^5, -10^9 \le A_i, val \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
