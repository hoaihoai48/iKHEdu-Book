# Lũy Thừa Chuỗi Số Lớn

**Phân loại bài toán:** `Core Foundation` (Bắt buộc)
## Bối cảnh
Cho số nguyên $A$ và số nguyên $B$ rất lớn được biểu diễn dưới dạng chuỗi có thể lên tới $10^5$ chữ số. Cho $M = 10^9 + 7$. Hãy tính $A^B \pmod M$.

## Input
- Dòng 1: Số nguyên $A$ ($0 \le A \le 10^9$).
- Dòng 2: Chuỗi ký tự số $B$ ($1 \le |B| \le 10^5$).

## Output
- In ra một số nguyên là $A^B \pmod{10^9 + 7}$.

## Sample 1
### Input
```text
2
10
```
### Output
```text
1024
```
### Giải thích
2^10 = 1024 % (10^9 + 7) = 1024.

## Ràng buộc
- $100\%$ số test có $A \le 10^9, |B| \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
