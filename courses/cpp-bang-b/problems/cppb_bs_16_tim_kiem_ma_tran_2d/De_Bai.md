# Tìm Kiếm Trên Ma Trận 2D Đã Sắp Xếp (Matrix Search)

## Bối cảnh
Cho ma trận $A$ kích thước $N \times M$ với các tính chất:
1. Các số trên mỗi hàng được sắp xếp theo thứ tự tăng dần từ trái sang phải.
2. Số đầu tiên của mỗi hàng luôn nghiêm ngặt lớn hơn số cuối cùng của hàng ngay trước nó.

Có $Q$ truy vấn, mỗi truy vấn cho một số nguyên $X$. Hãy kiểm tra xem $X$ có xuất hiện trong ma trận hay không.

## Input
- Dòng 1: Gồm 3 số nguyên $N, M, Q$ ($1 \le N, M \le 1000, 1 \le Q \le 10^5$).
- $N$ dòng tiếp theo: Mỗi dòng gồm $M$ số nguyên $A_{i, j}$ ($|A_{i, j}| \le 10^9$).
- $Q$ dòng tiếp theo: Mỗi dòng gồm một số nguyên $X$ ($|X| \le 10^9$).

## Output
- In ra $Q$ dòng, mỗi dòng in `YES` nếu tìm thấy, ngược lại in `NO`.

## Sample 1
### Input
```text
3 4 2
1 3 5 7
10 11 16 20
23 30 34 60
3
13
```
### Output
```text
YES
NO
```

## Ràng buộc
- $100\%$ số test có $N, M \le 1000, Q \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
