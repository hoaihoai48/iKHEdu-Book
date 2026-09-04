# Đếm Số Cặp Nghịch Thế (Inversion Count)

## Bối cảnh
Trong phân tích thứ tự xếp hạng (Ranking similarity), một cặp chỉ số (i, j) với i < j được gọi là một nghịch thế nếu A[i] > A[j]. Số lượng cặp nghịch thế phản ánh mức độ 'mất trật tự' của dãy số so với trạng thái đã sắp xếp hoàn hảo. Thuật toán Merge Sort cải tiến cho phép đếm số nghịch thế trong O(N log N).

## Nhiệm vụ
Cho mảng N số nguyên. Hãy đếm số lượng cặp chỉ số (i, j) với 1 <= i < j <= N sao cho A[i] > A[j].

## Input
- Dòng 1: Số nguyên dương $N$ ($1 \le N \le 10^5$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^9 \le A_i \le 10^9$).

## Output
- In ra một số nguyên duy nhất là số lượng cặp nghịch thế.

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
Các cặp nghịch thế gồm: (2, 1) tại vị trí (1, 3); (4, 1) tại vị trí (2, 3); và (4, 3) tại vị trí (2, 4). Tổng cộng có 3 cặp nghịch thế.

## Ràng buộc
- $100\%$ số test có $N \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
