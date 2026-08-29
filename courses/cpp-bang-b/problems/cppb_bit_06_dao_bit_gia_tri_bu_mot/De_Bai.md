# Đảo Bit Và Giá Trị Bù 1

## Bối cảnh
Cho một số nguyên dương $N$. Biểu diễn $N$ dưới dạng nhị phân không có các số 0 vô nghĩa ở đầu. Hãy tìm số nguyên thu được sau khi đảo ngược tất cả các bit của $N$ (biến bit 0 thành 1, và bit 1 thành 0).

## Input
- Dòng 1: Số nguyên dương $N$ ($1 \le N \le 10^9$).

## Output
- In ra một số nguyên duy nhất sau khi đảo bit.

## Sample 1
### Input
```text
5
```
### Output
```text
2
```
*(Giải thích: $5 = 101_2$. Đảo bit thành $010_2 = 2$).*

## Ràng buộc
- $100\%$ số test có $N \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
