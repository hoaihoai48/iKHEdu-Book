# Số Học Cực Hạn: Cặp Nguyên Tố Cùng Nhau & Phi Hàm Euler

## Bối cảnh
Cho số nguyên dương $N$. Hãy đếm số lượng cặp số nguyên $(x, y)$ thỏa mãn $1 \le x, y \le N$ và $\gcd(x, y) = 1$.

## Input
- Một dòng duy nhất chứa số nguyên dương $N$ ($1 \le N \le 10^6$).

## Output
- In ra tổng số lượng cặp $(x, y)$ nguyên tố cùng nhau.

## Sample 1
### Input
```text
3
```
### Output
```text
7
```
### Giải thích
Các cặp nguyên tố cùng nhau trong {1..3}: (1,1), (1,2), (1,3), (2,1), (2,3), (3,1), (3,2) -> 7 cặp.

## Ràng buộc
- $100\%$ số test có $N \le 10^6$.\n- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
