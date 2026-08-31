# Cặp Số Nguyên Tố Sinh Đôi (Twin Primes)

## Bối cảnh
Một cặp số $(p, p+2)$ được gọi là số nguyên tố sinh đôi nếu cả $p$ và $p+2$ đều là số nguyên tố. Cho số nguyên $N$, hãy đếm số lượng cặp nguyên tố sinh đôi mà $p+2 \le N$.

## Input
- Một dòng duy nhất chứa số nguyên dương $N$ ($1 \le N \le 10^7$).

## Output
- In ra một số nguyên là số lượng cặp nguyên tố sinh đôi.

## Sample 1
### Input
```text
20
```
### Output
```text
4
```
### Giải thích
Các cặp nguyên tố sinh đôi <= 20: (3, 5), (5, 7), (11, 13), (17, 19) -> 4 cặp.

## Ràng buộc
- $100\%$ số test có $N \le 10^7$.\n- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
