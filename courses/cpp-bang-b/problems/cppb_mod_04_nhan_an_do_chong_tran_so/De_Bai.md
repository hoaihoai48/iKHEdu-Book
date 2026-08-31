# Nhân Ấn Độ Chống Tràn Số 64-bit

> [!NOTE]
> **Phân loại bài toán:** `Core Foundation` (Bắt buộc)
## Bối cảnh
Cho 3 số nguyên $A, B, M$ ($0 \le A, B, M \le 10^{18}, M > 0$). Hãy tính $(A \times B) \pmod M$ mà không bị tràn số.

## Input
- Một dòng duy nhất chứa 3 số nguyên $A, B, M$.

## Output
- In ra một số nguyên là kết quả $(A \times B) \pmod M$.

## Sample 1
### Input
```text
1000000000000000000 1000000000000000000 1000000000000000007
```
### Output
```text
49
```
### Giải thích
A = -7 mod M, B = -7 mod M -> A * B = 49 mod M.

## Ràng buộc
- $100\%$ số test có $A, B, M \le 10^{18}$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
