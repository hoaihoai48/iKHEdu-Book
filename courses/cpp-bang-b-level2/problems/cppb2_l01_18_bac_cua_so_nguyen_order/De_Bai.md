# Bậc của số nguyên theo modulo m (multiplicative order)

## Bối cảnh
Cho hai số nguyên dương nguyên tố cùng nhau $A$ và $M$ ($\gcd(A, M) = 1$). Bậc của $A$ theo modulo $M$ (ký hiệu $\text{ord}_M(A)$) là số nguyên dương $k$ nhỏ nhất sao cho $A^k \equiv 1 \pmod M$. Theo định lý Euler, $k$ bắt buộc phải là một ước của $\phi(M)$.

## Nhiệm vụ
Hãy lập trình giải quyết bài toán Bậc Của Số Nguyên Theo Modulo M (multiplicative Order) với độ phức tạp tối ưu nhất.

## Input
- Dòng 1: Chứa số bộ test $T$ ($1 \le T \le 100$).
- $T$ dòng tiếp theo, mỗi dòng chứa hai số nguyên $A, M$ ($1 \le A < M \le 10^9, \gcd(A, M) = 1$).

## Output
- In ra $T$ dòng, mỗi dòng là bậc $\text{ord}_M(A)$.

## Sample 1
### Input
```text
2
2 7
3 10
```
### Output
```text
3
4
```
### Giải thích
* Modulo 7: $2^1=2, 2^2=4, 2^3=8 \equiv 1 \pmod 7 \implies k = 3$.
* Modulo 10: $3^1=3, 3^2=9, 3^3=27 \equiv 7, 3^4=81 \equiv 1 \pmod{10} \implies k = 4$.

## Ràng buộc
- $100\%$ số test có dữ liệu đầu vào nằm trong phạm vi cho phép.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
