# Đếm Số Lượng Số Không Tận Cùng Của N!

## Bối cảnh
Cho số nguyên dương $N$. Hãy đếm số lượng chữ số $0$ liên tiếp tận cùng trong biểu diễn thập phân của $N!$.

## Input
- Một dòng duy nhất chứa số nguyên dương $N$ ($1 \le N \le 10^{18}$).

## Output
- In ra số lượng chữ số 0 tận cùng của $N!$.

## Sample 1
### Input
```text
100
```
### Output
```text
24
```
### Giải thích
100! có floor(100/5) + floor(100/25) = 20 + 4 = 24 chữ số 0 tận cùng.

## Ràng buộc
- $100\%$ số test có $N \le 10^{18}$.\n- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
