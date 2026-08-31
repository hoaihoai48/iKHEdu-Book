# Lũy Thừa Nhị Phân Cơ Bản

> [!NOTE]
> **Phân loại bài toán:** `Core Foundation` (Bắt buộc)
## Bối cảnh
Cho 3 số nguyên $A, B, M$. Hãy tính $A^B \pmod M$ bằng thuật toán Lũy thừa nhị phân $\mathcal{O}(\log B)$.

## Input
- Một dòng duy nhất chứa 3 số nguyên $A, B, M$ ($0 \le A \le 10^{18}, 0 \le B \le 10^{18}, 1 \le M \le 10^9 + 7$).

## Output
- In ra một số nguyên duy nhất là kết quả $A^B \pmod M$.

## Sample 1
### Input
```text
3 13 1000
```
### Output
```text
323
```
### Giải thích
3^13 = 1594323 -> 1594323 % 1000 = 323.

## Ràng buộc
- $100\%$ số test có $A, B \le 10^{18}, M \le 10^9 + 7$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
