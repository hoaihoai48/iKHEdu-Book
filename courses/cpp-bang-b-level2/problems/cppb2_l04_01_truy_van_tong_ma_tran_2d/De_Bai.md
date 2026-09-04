# Truy vấn tổng ma trận con 2d

## Bối cảnh
Cho ma trận $A$ kích thước $N \times M$. Có $Q$ truy vấn tính tổng hình chữ nhật từ $(x_1, y_1)$ đến $(x_2, y_2)$.

## Nhiệm vụ

Cho ma trận $A$ kích thước $N \times M$ và $Q$ truy vấn hình chữ nhật $(x_1, y_1)$ đến $(x_2, y_2)$. Hãy lập trình tính tổng các ô trong mỗi hình chữ nhật được hỏi.

## Input
- Dòng 1: $N, M, Q$ ($1 \le N, M \le 1000, 1 \le Q \le 10^5$). $N$ dòng tiếp theo chứa ma trận. $Q$ dòng sau: $x_1, y_1, x_2, y_2$.

## Output
- In ra tổng mỗi hình chữ nhật con trên một dòng.

## Sample 1
### Input
```text
3 3 2
1 2 3
4 5 6
7 8 9
1 1 2 2
2 2 3 3
```
### Output
```text
12
28
```

### Giải thích
* Truy vấn 1 $(1, 1)$ đến $(2, 2)$ gồm các ô $1, 2, 4, 5$ nên tổng là $1 + 2 + 4 + 5 = 12$.
* Truy vấn 2 $(2, 2)$ đến $(3, 3)$ gồm các ô $5, 6, 8, 9$ nên tổng là $5 + 6 + 8 + 9 = 28$.

## Ràng buộc
- $100\%$ số test có dữ liệu đầu vào nằm trong phạm vi cho phép.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
