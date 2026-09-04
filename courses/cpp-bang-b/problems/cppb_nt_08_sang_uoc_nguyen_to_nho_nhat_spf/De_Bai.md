# Sàng Ước Nguyên Tố Nhỏ Nhất (SPF)

## Bối cảnh
Trong phân tích nhân tử nhanh O(log N) cho hàng triệu số nguyên, thuật toán Sàng ước nguyên tố nhỏ nhất (Smallest Prime Factor - SPF) là công cụ tối thượng để phân tích thừa số nguyên tố cực nhanh.

## Nhiệm vụ
Cho Q truy vấn, mỗi truy vấn chứa một số nguyên N (2 <= N <= 10^6). Hãy in ra ước số nguyên tố nhỏ nhất của N.

## Input
- Dòng 1: Số nguyên dương $Q$ ($1 \le Q \le 10^5$).
- $Q$ dòng tiếp theo: Mỗi dòng chứa một số nguyên $N$ ($2 \le N \le 10^6$).

## Output
- In ra $Q$ dòng, mỗi dòng là ước số nguyên tố nhỏ nhất của $N$.

## Sample 1
### Input
```text
3
15
7
20
```
### Output
```text
3
7
2
```
### Giải thích
- SPF(15) = 3 (vì 15 chia hết cho số nguyên tố nhỏ nhất là 3).
- SPF(7) = 7 (vì 7 là số nguyên tố).
- SPF(20) = 2 (vì 20 chia hết cho 2).

## Ràng buộc
- $100\%$ số test có $Q \le 10^5, N \le 10^6$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
