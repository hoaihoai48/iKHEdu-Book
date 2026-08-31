# Chú Ếch Nhảy Chi Phí Nhỏ Nhất

## Bối cảnh
Có $N$ phiến đá đánh số từ $1$ đến $N$, phiến đá $i$ có độ cao $H_i$. Chú ếch ở phiến đá $1$ muốn nhảy tới phiến đá $N$. Từ phiến đá $i$, ếch có thể nhảy tới $i+1$ hoặc $i+2$ với chi phí $|H_i - H_j|$.

## Nhiệm vụ
Tìm tổng chi phí tối thiểu để ếch nhảy từ phiến đá $1$ tới $N$.

## Input
- Dòng 1: Số nguyên $N$ ($2 \le N \le 10^5$).
- Dòng 2: $N$ số nguyên $H_1, H_2, \dots, H_N$ ($1 \le H_i \le 10^4$).

## Output
- In ra tổng chi phí nhỏ nhất.

## Sample 1
### Input
```text
4
10 30 40 20
```
### Output
```text
30
```

## Ràng buộc
- $100\%$ số test có $2 \le N \le 10^5, 1 \le H_i \le 10^4$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
