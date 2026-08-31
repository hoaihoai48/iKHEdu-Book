# Đếm Số Nguyên Tố Trong Đoạn [L, R]

## Bối cảnh
Cho $Q$ truy vấn, mỗi truy vấn gồm 2 số nguyên $L, R$. Hãy đếm số lượng số nguyên tố trong đoạn $[L, R]$.

## Input
- Dòng 1: Số nguyên dương $Q$ ($1 \le Q \le 10^5$).\n- $Q$ dòng tiếp theo: Mỗi dòng chứa 2 số nguyên $L, R$ ($1 \le L \le R \le 10^6$).

## Output
- In ra $Q$ dòng, mỗi dòng là số lượng số nguyên tố tương ứng.

## Sample 1
### Input
```text
3\n1 10\n11 20\n1 20
```
### Output
```text
4\n4\n8
```
### Giải thích
[1, 10] có 4 số {2, 3, 5, 7}. [11, 20] có 4 số {11, 13, 17, 19}. [1, 20] có 8 số.

## Ràng buộc
- $100\%$ số test có $Q \le 10^5, R \le 10^6$.\n- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
