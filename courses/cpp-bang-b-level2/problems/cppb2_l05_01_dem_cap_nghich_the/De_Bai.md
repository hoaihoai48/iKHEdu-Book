# Đếm cặp nghịch thế

## Bối cảnh
Cho mảng $N$ phần tử. Đếm số cặp $(i, j)$ thỏa mãn $1 \le i < j \le N$ và $A_i > A_j$.

## Nhiệm vụ
Cho mảng $A$ gồm $N$ số nguyên. Hãy lập trình đếm số cặp $(i, j)$ thỏa mãn $1 \le i < j \le N$ và $A_i > A_j$, rồi in ra tổng số cặp đếm được.

## Input
- Dòng 1: $N$ ($1 \le N \le 10^5$). Dòng 2: $N$ số $A_i$ ($1 \le A_i \le 10^9$).

## Output
- In ra tổng số cặp nghịch thế.

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
Với mảng $[2, 4, 1, 3, 5]$, xét lần lượt từng vị trí đứng trước:
- Số $2$: trong các số đứng sau nó ($4, 1, 3, 5$), chỉ có $1$ nhỏ hơn $2$ nên đếm được $1$ cặp.
- Số $4$: trong các số đứng sau nó ($1, 3, 5$), có $1$ và $3$ nhỏ hơn $4$ nên đếm được $2$ cặp.
- Số $1$: không có số nào đứng sau nhỏ hơn $1$.
- Số $3$: số đứng sau duy nhất là $5$ lớn hơn $3$ nên không đếm thêm.
- Số $5$: là số cuối cùng nên không tạo cặp nào.

Cộng lại: $1 + 2 = 3$. Vậy đáp án là $3$.

## Ràng buộc
- $100\%$ số test có dữ liệu đầu vào nằm trong phạm vi cho phép.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
