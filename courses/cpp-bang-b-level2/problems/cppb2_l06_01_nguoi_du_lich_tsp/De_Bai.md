# Bài toán người du lịch (tsp)

## Bối cảnh
Cho ma trận khoảng cách giữa $N$ thành phố ($N \le 18$). Tìm chi phí nhỏ nhất xuất phát từ thành phố 0, thăm tất cả các thành phố đúng 1 lần rồi quay về 0.

## Nhiệm vụ
Hãy lập trình giải quyết bài toán Bài Toán Người Du Lịch (tsp) với độ phức tạp tối ưu nhất.

## Input
- Dòng 1: $N$. $N$ dòng tiếp theo: Ma trận khoảng cách $C_{i, j}$.

## Output
- In ra chi phí nhỏ nhất.

## Sample 1
### Input
```text
4
0 10 15 20
10 0 35 25
15 35 0 30
20 25 30 0
```
### Output
```text
80
```

## Ràng buộc
- $100\%$ số test có dữ liệu đầu vào nằm trong phạm vi cho phép.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
