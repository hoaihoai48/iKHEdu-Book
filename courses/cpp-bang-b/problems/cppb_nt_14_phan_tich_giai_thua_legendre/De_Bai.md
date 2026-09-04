# Phân Tích Giai Thừa Ra Thừa Số (Định Lý Legendre)

## Bối cảnh
Định lý Legendre cung cấp công thức tính chính xác số mũ của thừa số nguyên tố P trong khai triển giai thừa N! mà không cần tính trực tiếp giá trị N! (vốn khổng lồ và tràn số). Kỹ sư cần tính số mũ lớn nhất K sao cho N! chia hết cho P^K.

## Nhiệm vụ
Cho số nguyên dương N và số nguyên tố P. Hãy tìm số mũ lớn nhất K sao cho N! chia hết cho P^K bằng công thức Legendre.

## Input
- Một dòng chứa 2 số nguyên $N$ và $P$ ($1 \le N \le 10^9, 2 \le P \le 10^9$, $P$ là số nguyên tố).

## Output
- In ra số mũ $K$ lớn nhất.

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
Áp dụng công thức Legendre: floor(10/3) + floor(10/9) = 3 + 1 = 4. Do đó 10! chia hết cho 3^4 và K = 4.

## Ràng buộc
- $100\%$ số test có $N, P \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
