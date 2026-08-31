# Cài Đặt Fenwick Tree Tính Tổng Đoạn (Range Sum)

## Bối cảnh
Hỗ trợ $Q$ thao tác trên mảng $N$ phần tử: `1 pos val` (cộng thêm `val` vào $A[pos]$) và `2 L R` (tính tổng các phần tử từ $L$ đến $R$).

## Nhiệm vụ
Với thao tác loại 2, in ra tổng của đoạn $[L, R]$.

## Input
- Dòng 1: $N, Q$ ($1 \le N, Q \le 10^5$).
- Dòng 2: $N$ số nguyên ban đầu ($1 \le A_i \le 10^9$).
- $Q$ dòng tiếp theo: Các truy vấn loại 1 và 2.

## Output
- Kết quả các truy vấn loại 2.

## Sample 1
### Input
```text
5 3
1 2 3 4 5
2 1 3
1 2 10
2 1 3
```
### Output
```text
6
16
```

## Ràng buộc
- $100\%$ số test có $1 \le N, Q \le 10^5, 1 \le A_i, val \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
