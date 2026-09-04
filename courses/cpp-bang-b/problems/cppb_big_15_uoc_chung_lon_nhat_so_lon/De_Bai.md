# Ước Chung Lớn Nhất Số Lớn

## Bối cảnh
Trong việc rút gọn phân số chứa các hệ số siêu lớn, tìm ước chung lớn nhất gcd(A, B) giữa hai số nguyên lớn A và B bằng thuật toán Euclid kết hợp chia lấy dư BigInt là thao tác không thể thiếu.

## Nhiệm vụ
Cho 2 số nguyên dương lớn A và B. Hãy tìm ước chung lớn nhất gcd(A, B).

## Input
- Dòng 1: Chuỗi số $A$ ($1 \le |A| \le 1000$).
- Dòng 2: Chuỗi số $B$ ($1 \le |B| \le 1000$).

## Output
- In ra $\gcd(A, B)$.

## Sample 1
### Input
```text
12
18
```
### Output
```text
6
```
### Giải thích
gcd(12, 18) = 6.

## Ràng buộc
- $100\%$ số test có $|A|, |B| \le 1000$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
