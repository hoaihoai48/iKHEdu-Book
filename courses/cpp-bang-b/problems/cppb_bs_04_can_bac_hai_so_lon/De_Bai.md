# Tìm Căn Bậc Hai Số Nguyên Lớn

## Bối cảnh
Cho một số nguyên dương $N$ ($1 \le N \le 10^{18}$). Hãy tìm số nguyên dương $X$ lớn nhất sao cho $X^2 \le N$ (phần nguyên của căn bậc hai $\lfloor \sqrt{N} \rfloor$).

## Input
- Dòng 1: Số nguyên dương $T$ ($1 \le T \le 10^5$) là số lượng testcase.
- $T$ dòng tiếp theo: Mỗi dòng gồm một số nguyên dương $N$ ($1 \le N \le 10^{18}$).

## Output
- In ra $T$ dòng kết quả tương ứng.

## Sample 1
### Input
```text
3
16
20
1000000000000000000
```
### Output
```text
4
4
1000000000
```

## Ràng buộc
- $100\%$ số test có $N \le 10^{18}$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
