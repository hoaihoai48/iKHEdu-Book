# Đoạn Con Có Tổng Bằng 0

## Bối cảnh
Cho mảng số nguyên gồm $N$ phần tử. Hãy kiểm tra xem có tồn tại ít nhất một đoạn con liên tiếp khác rỗng có tổng các phần tử bằng $0$ hay không.

## Input
- Dòng 1: Số nguyên dương $N$ ($1 \le N \le 10^5$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \dots, A_N$ ($|A_i| \le 10^9$).

## Output
- In ra `YES` nếu tồn tại đoạn con có tổng bằng 0, ngược lại in ra `NO`.

## Sample 1
### Input
```text
5
4 2 -3 1 6
```
### Output
```text
YES
```
*(Giải thích: Đoạn con $[2, -3, 1]$ có tổng là $2 + (-3) + 1 = 0$).*

## Ràng buộc
- $100\%$ số test có $N \le 10^5, |A_i| \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
