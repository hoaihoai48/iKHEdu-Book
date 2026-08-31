# Chú Ếch Nhảy K Bước

## Bối cảnh
Tương tự bài toán chú ếch, nhưng từ phiến đá $i$, ếch có thể nhảy xa tối đa $K$ bước tới các phiến đá $i+1, i+2, \dots, i+K$.

## Nhiệm vụ
Tìm tổng chi phí tối thiểu để ếch nhảy từ phiến đá $1$ tới $N$.

## Input
- Dòng 1: Hai số nguyên $N$ và $K$ ($2 \le N \le 10^5, 1 \le K \le 100$).
- Dòng 2: $N$ số nguyên $H_1, H_2, \dots, H_N$ ($1 \le H_i \le 10^4$).

## Output
- In ra chi phí tối thiểu.

## Sample 1
### Input
```text
5 3
10 30 40 50 20
```
### Output
```text
30
```

## Ràng buộc
- $100\%$ số test có $2 \le N \le 10^5, 1 \le K \le 100$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
