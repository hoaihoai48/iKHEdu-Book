# Lũy Thừa Ma Trận Chia Để Trị 2x2

## Bối cảnh
Để tìm số Fibonacci thứ N với N lên tới 10^18 trong thời gian O(log N), ma trận chuyển trạng thái 2x2 được nâng lên lũy thừa N bằng thuật toán chia để trị (nhân ma trận nhị phân).

## Nhiệm vụ
Cho ma trận vuông 2x2 gồm các hệ số a, b, c, d và số nguyên N. Hãy tính A^N mod (10^9 + 7).

## Input
- Dòng 1: 4 số nguyên $a, b, c, d$ ($0 \le a, b, c, d \le 10^9$).
- Dòng 2: Số nguyên $N$ ($0 \le N \le 10^{18}$).

## Output
- In ra 4 số nguyên trên 2 dòng biểu diễn ma trận $A^N \pmod{10^9 + 7}$.

## Sample 1
### Input
```text
1 1
1 0
2
```
### Output
```text
2 1
1 1
```
### Giải thích
A^2 = [[1, 1], [1, 0]] * [[1, 1], [1, 0]] = [[2, 1], [1, 1]].

## Ràng buộc
- $100\%$ số test có $N \le 10^{18}$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
