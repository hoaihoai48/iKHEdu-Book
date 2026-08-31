# Sàng Phân Đoạn (Segmented Sieve)

## Bối cảnh
Cho hai số nguyên $L, R$. Hãy đếm số lượng số nguyên tố trong đoạn $[L, R]$.

## Input
- Một dòng duy nhất chứa 2 số nguyên $L, R$ ($1 \le L \le R \le 10^{12}, R - L \le 10^6$).

## Output
- In ra một số nguyên duy nhất là số lượng số nguyên tố.

## Sample 1
### Input
```text
100 120
```
### Output
```text
5
```
### Giải thích
Các số nguyên tố trong [100, 120] là {101, 103, 107, 109, 113} -> 5 số.

## Ràng buộc
- $100\%$ số test có $R \le 10^{12}, R - L \le 10^6$.\n- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
