# Phép Chia Đồng Dư A / B mod M

## Bối cảnh
Trong các bài toán đếm xác suất tổ hợp, phân số dạng A / B cần được biểu diễn dưới dạng số nguyên modulo M = 10^9 + 7. Hãy thực hiện phép chia đồng dư chuẩn xác.

## Nhiệm vụ
Cho 2 số nguyên A, B và số nguyên tố M = 10^9 + 7 (B không chia hết cho M). Hãy tính giá trị (A / B) mod M.

## Input
- Một dòng chứa 2 số nguyên $A$ và $B$ ($0 \le A, B \le 10^{18}, B \not\equiv 0 \pmod M$).

## Output
- In ra giá trị $(A / B) \pmod{10^9 + 7}$.

## Sample 1
### Input
```text
8 2
```
### Output
```text
4
```
### Giải thích
(8 / 2) mod M = 8 * 2^(M-2) mod M = 4.

## Ràng buộc
- $100\%$ số test có $A, B \le 10^{18}$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
