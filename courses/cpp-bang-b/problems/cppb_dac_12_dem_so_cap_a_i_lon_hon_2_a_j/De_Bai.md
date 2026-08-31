# Đếm Số Cặp A_i > 2 * A_j (Significant Inversions)

**Phân loại bài toán:** `Core Foundation`

## Bối cảnh
Cho mảng số nguyên $A$ gồm $N$ phần tử. Hãy đếm số cặp chỉ số $(i, j)$ thỏa mãn $1 \le i < j \le N$ và $A_i > 2 \times A_j$ bằng biến thể Merge Sort Chia Để Trị trong $\mathcal{O}(N \log N)$.

## Input
- Dòng 1: Số nguyên dương $N$ ($1 \le N \le 10^5$).
- Dòng 2: $N$ số nguyên $A_1, \dots, A_N$ ($|A_i| \le 10^9$).

## Output
- In ra số lượng cặp thỏa mãn điều kiện.

## Sample 1
### Input
```text
5
1 3 2 3 1
```
### Output
```text
2
```
### Giải thích
Có 2 cặp thỏa mãn: (3, 1) tại vị trí (2, 5) và (3, 1) tại vị trí (4, 5).

## Ràng buộc
- 100% số test có $N \le 10^5, |A_i| \le 10^9$.
- Thời gian: 1.0s, Bộ nhớ: 256MB.
