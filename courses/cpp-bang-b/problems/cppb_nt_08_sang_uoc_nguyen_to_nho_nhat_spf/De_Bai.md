# Sàng Ước Nguyên Tố Nhỏ Nhất (SPF)

## Bối cảnh
Cho $Q$ truy vấn, mỗi truy vấn chứa một số nguyên $N$. Hãy in ra ước số nguyên tố nhỏ nhất của $N$.

## Input
- Dòng 1: Số nguyên dương $Q$ ($1 \le Q \le 10^5$).\n- Dòng 2: $Q$ số nguyên $N_1, N_2, \dots, N_Q$ ($2 \le N_i \le 10^6$).

## Output
- In ra $Q$ số nguyên là ước nguyên tố nhỏ nhất tương ứng trên một dòng.

## Sample 1
### Input
```text
4\n15 49 13 100
```
### Output
```text
3 7 13 2
```
### Giải thích
spf(15)=3, spf(49)=7, spf(13)=13, spf(100)=2.

## Ràng buộc
- $100\%$ số test có $Q \le 10^5, N_i \le 10^6$.\n- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
