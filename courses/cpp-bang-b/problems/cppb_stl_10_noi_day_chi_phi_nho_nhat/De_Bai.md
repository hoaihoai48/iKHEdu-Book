# Nối Dây Chi Phí Nhỏ Nhất (Huffman Greedy)

## Bối cảnh
Có $N$ sợi dây với chiều dài $A_i$. Chi phí nối hai sợi dây có chiều dài $X$ và $Y$ là $X + Y$. Cần nối tất cả các sợi dây thành 1 sợi duy nhất.

## Nhiệm vụ
Tìm tổng chi phí nối dây nhỏ nhất.

## Input
- Dòng 1: Số nguyên $N$ ($1 \le N \le 50000$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \dots, A_N$ ($1 \le A_i \le 10^5$).

## Output
- Tổng chi phí nhỏ nhất.

## Sample 1
### Input
```text
4
4 3 2 6
```
### Output
```text
29
```

## Ràng buộc
- $100\%$ số test có $1 \le N \le 50000, 1 \le A_i \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
