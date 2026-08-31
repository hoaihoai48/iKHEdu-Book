# Phân Tích Giai Thừa Ra Thừa Số (Định Lý Legendre)

## Bối cảnh
Cho số nguyên $N$ và số nguyên tố $P$. Hãy tìm số mũ lớn nhất $K$ sao cho $N!$ chia hết cho $P^K$.

## Input
- Một dòng duy nhất chứa 2 số nguyên $N$ và $P$ ($1 \le N \le 10^{18}, 2 \le P \le 10^6$, $P$ là số nguyên tố).

## Output
- In ra một số nguyên $K$ là số mũ tìm được.

## Sample 1
### Input
```text
10 3
```
### Output
```text
4
```
### Giải thích
10! chia hết cho 3^4 (floor(10/3) + floor(10/9) = 3 + 1 = 4).

## Ràng buộc
- $100\%$ số test có $N \le 10^{18}, P \le 10^6$.\n- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
