# Max Mọi Cửa Sổ Trượt Bằng Monotonic Deque O(N)

## Bối cảnh
Tìm giá trị lớn nhất trong mỗi cửa sổ trượt độ dài $K$ bằng Deque đơn điệu giảm dần $\mathcal{O}(N)$.

## Nhiệm vụ
In ra $N - K + 1$ giá trị lớn nhất.

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
3 3 5 5 6 7
```

## Ràng buộc
- $100\%$ số test có $1 \le K \le N \le 10^5, -10^9 \le A_i \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
