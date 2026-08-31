# Dãy Con Tăng Dài Nhất LIS O(N log N)

## Bối cảnh
Cho dãy số $A$ có kích thước lên tới $10^5$. Thuật toán $\mathcal{O}(N^2)$ sẽ bị quá thời gian.

## Nhiệm vụ
Tìm độ dài của dãy con tăng nghiêm ngặt dài nhất bằng kỹ thuật tìm kiếm nhị phân trên mảng tails $\mathcal{O}(N \log N)$.

## Input
- Dòng 1: Số nguyên $N$ ($1 \le N \le 10^5$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \dots, A_N$ ($1 \le A_i \le 10^9$).

## Output
- In ra độ dài lớn nhất của dãy con tăng.

## Sample 1
### Input
```text
6
5 2 7 4 3 8
```
### Output
```text
3
```

## Ràng buộc
- $100\%$ số test có $1 \le N \le 10^5, 1 \le A_i \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
