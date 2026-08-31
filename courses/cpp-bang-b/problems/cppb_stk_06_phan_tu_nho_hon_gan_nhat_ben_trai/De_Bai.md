# Phần Tử Nhỏ Hơn Gần Nhất Bên Trái (Previous Smaller Element)

## Bối cảnh
Với mỗi vị trí $i$, tìm phần tử đầu tiên bên trái có giá trị nhỏ hơn $A[i]$.

## Nhiệm vụ
In ra giá trị của phần tử nhỏ hơn gần nhất bên trái (hoặc -1 nếu không có).

## Input
- Dòng 1: Số nguyên $N$ ($1 \le N \le 10^5$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \dots, A_N$ ($1 \le A_i \le 10^9$).

## Output
- $N$ số nguyên.

## Sample 1
### Input
```text
5
4 5 2 10 8
```
### Output
```text
-1 4 -1 2 2
```

## Ràng buộc
- $100\%$ số test có $1 \le N \le 10^5, 1 \le A_i \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
