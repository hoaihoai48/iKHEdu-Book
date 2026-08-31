# Min Mọi Cửa Sổ Trượt Bằng Monotonic Deque O(N)

## Bối cảnh
Cho mảng $A$ và số $K$. Tìm giá trị nhỏ nhất trong mỗi cửa sổ trượt độ dài $K$.

## Nhiệm vụ
In ra $N - K + 1$ số nguyên biểu diễn min từng cửa sổ.

## Input
- Dòng 1: Hai số $N$ và $K$ ($1 \le K \le N \le 10^5$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \dots, A_N$ ($1 \le A_i \le 10^9$).

## Output
- $N - K + 1$ số nguyên.

## Sample 1
### Input
```text
8 3
1 3 -1 -3 5 3 6 7
```
### Output
```text
-1 -3 -3 -3 3 3
```

## Ràng buộc
- $100\%$ số test có $1 \le K \le N \le 10^5, -10^9 \le A_i \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
