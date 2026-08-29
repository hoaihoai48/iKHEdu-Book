# Tìm Vị Trí Cân Bằng Của Mảng

## Bối cảnh
Một vị trí $i$ ($1 \le i \le N$) trong dãy số $A$ được gọi là **vị trí cân bằng** nếu tổng các phần tử đứng trước nó bằng tổng các phần tử đứng sau nó:
$$\sum_{k=1}^{i-1} A_k = \sum_{k=i+1}^{N} A_k$$
(Quy ước nếu trước $i$ hoặc sau $i$ không có phần tử nào thì tổng tương ứng bằng $0$).

## Nhiệm vụ
Tìm vị trí cân bằng đầu tiên (chỉ số nhỏ nhất). Nếu không có, in ra `-1`.

## Input
- Dòng 1: Số nguyên dương $N$ ($1 \le N \le 2 \cdot 10^5$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \dots, A_N$ ($|A_i| \le 10^9$).

## Output
- In ra chỉ số cân bằng nhỏ nhất (1-based), hoặc `-1` nếu không tồn tại.

## Sample 1
### Input
```text
7
-7 1 5 2 -4 3 0
```
### Output
```text
4
```
*(Giải thích: Tại vị trí 4 có giá trị 2: Tổng trái $(-7+1+5= -1)$, tổng phải $(-4+3+0 = -1)$).*

## Ràng buộc
- $100\%$ số test có $N \le 2 \cdot 10^5, |A_i| \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
