# Tính Tổng Cấp Số Nhân D&C

## Bối cảnh
Bằng công thức chia để trị S(N) = 1 + A + ... + A^N = (1 + A^(N/2 + 1)) * S(N/2), tổng cấp số nhân có thể được tính theo bất kỳ modulo M nào trong O(log N) mà không cần chia đồng dư.

## Nhiệm vụ
Cho 3 số nguyên A, N, M. Hãy tính tổng cấp số nhân S(N) = A^0 + A^1 + ... + A^N mod M bằng chia để trị.

## Input
- Một dòng chứa 3 số nguyên $A, N, M$ ($0 \le A, N \le 10^9, 1 \le M \le 10^9$).

## Output
- In ra giá trị $S(N) \pmod M$.

## Sample 1
### Input
```text
2 3 100
```
### Output
```text
15
```
### Giải thích
S(3) = 1 + 2 + 4 + 8 = 15 mod 100 = 15.

## Ràng buộc
- $100\%$ số test có $A, N \le 10^9, M \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
