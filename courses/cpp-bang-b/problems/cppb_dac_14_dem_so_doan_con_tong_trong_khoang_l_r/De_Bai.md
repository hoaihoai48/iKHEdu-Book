# Đếm Số Đoạn Con Tổng Trong Đoạn [L, R]

## Bối cảnh
Bài toán đếm số lượng đoạn con liên tiếp có tổng nằm trong phạm vi [Lower, Upper] được chuyển hóa về bài toán đếm nghịch thế trên mảng tiền tố bằng phương pháp chia để trị trong O(N log N).

## Nhiệm vụ
Cho mảng N số nguyên và hai ngưỡng Lower, Upper. Hãy đếm số lượng đoạn con liên tiếp có tổng nằm trong đoạn [Lower, Upper].

## Input
- Dòng 1: Chứa 3 số nguyên $N, Lower, Upper$ ($1 \le N \le 10^5, -10^{14} \le Lower \le Upper \le 10^{14}$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^9 \le A_i \le 10^9$).

## Output
- In ra số lượng đoạn con thỏa mãn.

## Sample 1
### Input
```text
3 -2 2
0 -3 -3
```
### Output
```text
1
```
### Giải thích
Đoạn con [0] ở vị trí 1 có tổng là 0 nằm trong khoảng [-2, 2]. Tổng cộng có 1 đoạn con thỏa mãn.

## Ràng buộc
- $100\%$ số test có $N \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
