# Đoạn Con Chứa Tối Đa K Số 0 (Lật Bit)

## Bối cảnh
Cho một mảng nhị phân $A$ gồm $N$ phần tử ($A_i \in \{0, 1\}$) và số nguyên không âm $K$. Bạn được phép đổi tối đa $K$ số 0 thành số 1. Hãy tìm độ dài lớn nhất của dãy số 1 liên tiếp có thể tạo được.

## Input
- Dòng 1: Chứa 2 số nguyên $N$ và $K$ ($1 \le N \le 10^5, 0 \le K \le N$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \dots, A_N$ ($A_i \in \{0, 1\}$).

## Output
- In ra độ dài lớn nhất tìm được.

## Sample 1
### Input
```text
5 1
1 0 1 1 0
```
### Output
```text
4
```
### Giải thích
Đổi số 0 tại vị trí thứ 2 thành 1 để thu được dãy $[1, 1, 1, 1]$ dài 4.

## Ràng buộc
- $100\%$ số test có $N \le 10^5, K \le N$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
