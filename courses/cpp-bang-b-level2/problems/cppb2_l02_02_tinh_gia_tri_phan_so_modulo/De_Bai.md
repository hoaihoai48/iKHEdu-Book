# Tính giá trị phân số modulo

## Bối cảnh
Cho hai số nguyên $P, Q$ ($Q \not\equiv 0 \pmod{10^9+7}$). Hãy tính $(P \times Q^{-1}) \bmod (10^9+7)$.

## Nhiệm vụ
Hãy lập trình giải quyết bài toán Tính Giá Trị Phân Số Modulo với độ phức tạp tối ưu nhất.

## Input
- Dòng 1: $T$ ($1 \le T \le 10^5$). $T$ dòng sau: $P, Q$ ($0 \le P \le 10^9, 1 \le Q \le 10^9$).

## Output
- In ra $(P / Q) \bmod (10^9+7)$ trên mỗi dòng.

## Sample 1
### Input
```text
2
1 2
3 7
```
### Output
```text
500000004
428571432
```

## Ràng buộc
- $100\%$ số test có dữ liệu đầu vào nằm trong phạm vi cho phép.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
