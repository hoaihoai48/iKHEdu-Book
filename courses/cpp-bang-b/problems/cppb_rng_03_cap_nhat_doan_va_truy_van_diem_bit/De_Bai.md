# Cập Nhật Đoạn & Truy Vấn Điểm (Range Update Point Query)

## Bối cảnh
Hỗ trợ thao tác `1 L R val` (cộng thêm `val` vào mọi phần tử trong đoạn $[L, R]$) và `2 pos` (in ra giá trị hiện tại của $A[pos]$).

## Nhiệm vụ
In ra giá trị tại vị trí $pos$ cho các truy vấn loại 2.

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
1 2 3 4 5
1 2 4 5
2 3
2 1
```
### Output
```text
8
1
```

## Ràng buộc
- $100\%$ số test có $1 \le N, Q \le 10^5, 1 \le A_i, val \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
