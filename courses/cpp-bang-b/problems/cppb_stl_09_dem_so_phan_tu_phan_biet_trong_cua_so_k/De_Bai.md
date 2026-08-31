# Đếm Số Phần Tử Phân Biệt Trong Cửa Sổ K

## Bối cảnh
Cho mảng $A$ và số $K$. Tính số lượng phần tử phân biệt trong mỗi cửa sổ trượt độ dài $K$.

## Nhiệm vụ
In ra số lượng phần tử phân biệt trong từng cửa sổ.

## Input
- Dòng 1: Hai số $N$ và $K$ ($1 \le K \le N \le 10^5$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \dots, A_N$ ($1 \le A_i \le 10^9$).

## Output
- $N - K + 1$ số nguyên.

## Sample 1
### Input
```text
7 4
1 2 1 3 4 2 3
```
### Output
```text
3 4 4 3
```

## Ràng buộc
- $100\%$ số test có $1 \le K \le N \le 10^5, 1 \le A_i \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
