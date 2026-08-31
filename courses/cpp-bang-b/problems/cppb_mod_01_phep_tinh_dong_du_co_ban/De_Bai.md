# Phép Tính Đồng Dư Cơ Bản (+, -, *)

> [!NOTE]
> **Phân loại bài toán:** `Core Foundation` (Bắt buộc)
## Bối cảnh
Cho 2 số nguyên $A, B$ và số nguyên dương $M = 10^9 + 7$. Hãy tính $(A + B) \pmod M$, $(A - B) \pmod M$ và $(A \times B) \pmod M$ sao cho kết quả luôn thuộc $[0, M - 1]$.

## Input
- Một dòng duy nhất chứa 2 số nguyên $A, B$ ($0 \le A, B \le 10^{18}$).

## Output
- In ra 3 số nguyên cách nhau bởi dấu cách lần lượt là $(A + B) \pmod M$, $(A - B) \pmod M$ và $(A \times B) \pmod M$.

## Sample 1
### Input
```text
1000000008 3
```
### Output
```text
4 1000000005 3
```
### Giải thích
1000000008 % M = 1. (1 + 3) % M = 4. (1 - 3 + M) % M = 1000000005. (1 * 3) % M = 3.

## Ràng buộc
- $100\%$ số test có $A, B \le 10^{18}$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
