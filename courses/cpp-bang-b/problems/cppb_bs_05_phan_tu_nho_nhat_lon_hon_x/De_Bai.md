# Tìm Phần Tử Nhỏ Nhất Lớn Hơn X

## Bối cảnh
Cho một mảng gồm $N$ số nguyên đã được sắp xếp tăng dần. Có $Q$ truy vấn, mỗi truy vấn cho một số nguyên $X$. Hãy tìm giá trị của phần tử nhỏ nhất trong mảng có giá trị nghiêm ngặt lớn hơn $X$. Nếu không có phần tử nào lớn hơn $X$, in ra `-1`.

## Input
- Dòng 1: Gồm 2 số nguyên $N, Q$ ($1 \le N, Q \le 10^5$).
- Dòng 2: $N$ số nguyên đã sắp xếp $A_1, A_2, \dots, A_N$ ($|A_i| \le 10^9$).
- $Q$ dòng tiếp theo: Mỗi dòng gồm một số nguyên $X$ ($|X| \le 10^9$).

## Output
- In ra $Q$ dòng kết quả tương ứng.

## Sample 1
### Input
```text
5 3
2 4 6 8 10
5
8
11
```
### Output
```text
6
10
-1
```

## Ràng buộc
- $100\%$ số test có $N, Q \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
