# Chọn Đoạn Tối Đa Không Quá K Phần Tử Liền Kề

## Bối cảnh
Cho mảng $A$ gồm $N$ số nguyên dương. Chọn một tập hợp các phần tử sao cho không có quá $K$ phần tử liên tiếp nào cùng được chọn.

## Nhiệm vụ
Tìm tổng giá trị lớn nhất có thể thu được.

## Input
- Dòng 1: Hai số $N$ và $K$ ($1 \le K \le N \le 10^5$).
- Dòng 2: $N$ số nguyên dương $A_1, A_2, \dots, A_N$ ($1 \le A_i \le 10^9$).

## Output
- Tổng lớn nhất.

## Sample 1
### Input
```text
5 2
1 2 3 4 5
```
### Output
```text
12
```

## Ràng buộc
- $100\%$ số test có $1 \le K \le N \le 10^5, 1 \le A_i \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
