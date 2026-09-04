# Đếm Số Cặp A_i > 2 * A_j (Significant Inversions)

## Bối cảnh
Trong phân tích sai lệch dữ liệu tài chính quy mô lớn, một nghịch thế có ý nghĩa thống kê (Significant Inversion) là cặp chỉ số i < j thỏa mãn A[i] > 2 * A[j]. Thuật toán Merge Sort nâng cao cho phép đếm số lượng cặp này trong O(N log N).

## Nhiệm vụ
Cho mảng N số nguyên. Hãy đếm số cặp chỉ số (i, j) với 1 <= i < j <= N thỏa mãn A[i] > 2 * A[j].

## Input
- Dòng 1: Số nguyên dương $N$ ($1 \le N \le 10^5$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^9 \le A_i \le 10^9$).

## Output
- In ra số lượng cặp nghịch thế có ý nghĩa.

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
Các cặp thỏa mãn là: (3, 1) tại vị trí (2, 5) vì 3 > 2*1; và (3, 1) tại vị trí (4, 5) vì 3 > 2*1. Tổng cộng có 2 cặp.

## Ràng buộc
- $100\%$ số test có $N \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
