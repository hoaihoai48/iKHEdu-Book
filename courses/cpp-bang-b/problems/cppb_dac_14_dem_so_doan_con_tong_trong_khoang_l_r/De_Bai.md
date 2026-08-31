# Đếm Số Đoạn Con Tổng Trong Đoạn [L, R]

**Phân loại bài toán:** `Advanced`

## Bối cảnh
Cho mảng số nguyên $A$ gồm $N$ phần tử và hai số nguyên $Lower, Upper$. Hãy đếm số lượng đoạn con liên tiếp khác rỗng $A[i..j]$ ($1 \le i \le j \le N$) có tổng $\sum_{k=i}^j A_k$ nằm trong đoạn $[Lower, Upper]$ bằng Chia Để Trị trên mảng tiền tố (Prefix Sum Merge Count) trong $\mathcal{O}(N \log N)$.

## Input
- Dòng 1: 3 số nguyên $N, Lower, Upper$ ($1 \le N \le 10^5, -10^{14} \le Lower \le Upper \le 10^{14}$).
- Dòng 2: $N$ số nguyên $A_1, \dots, A_N$ ($|A_i| \le 10^9$).

## Output
- In ra số lượng đoạn con thỏa mãn.

## Sample 1
### Input
```text
3 -2 2
0 -3 1
```
### Output
```text
3
```
### Giải thích
Các đoạn con thỏa mãn: [0] (tổng 0), [1] (tổng 1), [0, -3, 1] (tổng -2).

## Ràng buộc
- 100% số test có $N \le 10^5, |A_i| \le 10^9$.
- Thời gian: 1.0s, Bộ nhớ: 256MB.
