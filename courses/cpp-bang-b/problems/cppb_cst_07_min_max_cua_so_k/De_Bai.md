# Tìm Min Trong Mọi Cửa Sổ Độ Dài K

## Bối cảnh
Cho mảng gồm $N$ số nguyên và số nguyên $K$. Với mỗi cửa sổ gồm $K$ phần tử liên tiếp từ trái sang phải, hãy tìm giá trị nhỏ nhất trong cửa sổ đó.

## Input
- Dòng 1: Chứa 2 số nguyên $N$ và $K$ ($1 \le K \le N \le 10^4$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^9 \le A_i \le 10^9$).

## Output
- In ra $N - K + 1$ số nguyên cách nhau bởi khoảng trắng là giá trị nhỏ nhất của các cửa sổ.

## Sample 1
### Input
```text
6 3
4 2 12 3 5 1
```
### Output
```text
2 2 3 1
```

## Ràng buộc
- $100\%$ số test có $N \le 10^4, K \le N$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
