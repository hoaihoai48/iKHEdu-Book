# Truy vấn tổng ma trận con 2d

## Bối cảnh
Cho ma trận $A$ kích thước $N \times M$. Có $Q$ truy vấn tính tổng hình chữ nhật từ $(x_1, y_1)$ đến $(x_2, y_2)$.

## Nhiệm vụ
Hãy lập trình giải quyết bài toán Truy Vấn Tổng Ma Trận Con 2d với độ phức tạp tối ưu nhất.

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

## Ràng buộc
- $100\%$ số test có dữ liệu đầu vào nằm trong phạm vi cho phép.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
