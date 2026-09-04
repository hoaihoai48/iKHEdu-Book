# Nghịch Đảo Modulo Bằng Euclid Mở Rộng

## Bối cảnh
Khi modulo M không nhất thiết phải là số nguyên tố mà chỉ cần nguyên tố cùng nhau với A (gcd(A, M) = 1), định lý Fermat nhỏ không áp dụng được. Thuật toán Euclid mở rộng (Extended Euclidean Algorithm) giải phương trình Diophantine A*x + M*y = 1 để tìm nghịch đảo modulo x.

## Nhiệm vụ
Cho hai số nguyên dương A và M với gcd(A, M) = 1. Hãy tìm nghịch đảo modulo của A theo modulo M.

## Input
- Một dòng chứa 2 số nguyên dương $A$ và $M$ ($1 \le A < M \le 10^9$).

## Output
- In ra nghịch đảo modulo của $A$ trong đoạn $[0, M - 1]$.

## Sample 1
### Input
```text
3 11
```
### Output
```text
4
```
### Giải thích
3 * 4 = 12 = 1 * 11 + 1 = 1 mod 11. Vì vậy nghịch đảo modulo của 3 theo mod 11 là 4.

## Ràng buộc
- $100\%$ số test có $A < M \le 10^9, \gcd(A, M) = 1$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
