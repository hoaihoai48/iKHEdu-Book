# Dãy Con Giảm Dài Nhất (LDS)

## Bối cảnh
Cho mảng $A$ gồm $N$ số nguyên. Cần tìm độ dài của dãy con giảm nghiêm ngặt dài nhất ($A_{i_1} > A_{i_2} > \dots > A_{i_k}$).

## Nhiệm vụ
In ra độ dài của dãy con giảm dài nhất.

## Input
- Dòng 1: Số nguyên $N$ ($1 \le N \le 10^5$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \dots, A_N$ ($1 \le A_i \le 10^9$).

## Output
- Độ dài lớn nhất của dãy con giảm.

## Sample 1
### Input
```text
5
10 9 2 5 3 7 101 18
```
### Output
```text
4
```

## Ràng buộc
- $100\%$ số test có $1 \le N \le 10^5, 1 \le A_i \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
