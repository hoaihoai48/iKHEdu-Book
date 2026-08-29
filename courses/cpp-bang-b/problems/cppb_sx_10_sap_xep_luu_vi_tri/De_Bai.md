# Sắp Xếp Lưu Vị Trí Ban Đầu

## Bối cảnh
Cho một dãy gồm $N$ số nguyên $A_1, A_2, \dots, A_N$. Hãy sắp xếp các phần tử theo thứ tự tăng dần, đồng thời in ra vị trí ban đầu (chỉ số 1-indexed) của mỗi phần tử trong mảng gốc. Nếu hai phần tử có cùng giá trị, phần tử xuất hiện trước trong mảng gốc sẽ đứng trước.

## Input
- Dòng 1: Số nguyên dương $N$ ($1 \le N \le 10^5$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^9 \le A_i \le 10^9$).

## Output
- In ra $N$ dòng, mỗi dòng gồm 2 số nguyên biểu diễn giá trị phần tử và chỉ số ban đầu của nó.

## Sample 1
### Input
```text
5
40 10 20 10 30
```
### Output
```text
10 2
10 4
20 3
30 5
40 1
```

## Ràng buộc
- $100\%$ số test có $N \le 10^5, \vert A_i \vert \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
