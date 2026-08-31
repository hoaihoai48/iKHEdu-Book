# Đếm Số Cặp Nghịch Thế (Inversion Count)

**Phân loại bài toán:** `Core Foundation`

## Bối cảnh
Cho mảng số nguyên $A$ gồm $N$ phần tử. Cặp chỉ số $(i, j)$ được gọi là một cặp nghịch thế nếu $1 \le i < j \le N$ và $A_i > A_j$. Hãy tính tổng số cặp nghịch thế trong mảng bằng thuật toán Merge Sort $\mathcal{O}(N \log N)$.

## Input
- Dòng 1: Số nguyên dương $N$ ($1 \le N \le 10^5$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \dots, A_N$ ($|A_i| \le 10^9$).

## Output
- In ra một số nguyên duy nhất là tổng số cặp nghịch thế trong mảng.

## Sample 1
### Input
```text
5
2 4 1 3 5
```
### Output
```text
3
```
### Giải thích
Có 3 cặp nghịch thế: (2, 1), (4, 1), (4, 3).

## Ràng buộc
- 100% số test có $1 \le N \le 10^5, |A_i| \le 10^9$.
- Thời gian: 1.0s, Bộ nhớ: 256MB.
