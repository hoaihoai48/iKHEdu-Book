# Tính Tổng Cấp Số Nhân D&C

**Phân loại bài toán:** `Core Foundation`

## Bối cảnh
Cho 3 số nguyên $A, N, M$. Hãy tính tổng cấp số nhân $S(N) = A^0 + A^1 + A^2 + \cdots + A^N \pmod M$ bằng kỹ thuật Chia Để Trị trong $\mathcal{O}(\log N)$ theo hệ thức $S(2k+1) = S(k) \times (1 + A^{k+1})$.

## Input
- Một dòng duy nhất chứa 3 số nguyên $A, N, M$ ($0 \le A, N \le 10^9, 1 \le M \le 10^9 + 7$).

## Output
- In ra giá trị $S(N) \pmod M$.

## Sample 1
### Input
```text
2 3 1000
```
### Output
```text
15
```
### Giải thích
2^0 + 2^1 + 2^2 + 2^3 = 1 + 2 + 4 + 8 = 15.

## Ràng buộc
- 100% số test có $N \le 10^9, M \le 10^9 + 7$.
- Thời gian: 1.0s, Bộ nhớ: 256MB.
