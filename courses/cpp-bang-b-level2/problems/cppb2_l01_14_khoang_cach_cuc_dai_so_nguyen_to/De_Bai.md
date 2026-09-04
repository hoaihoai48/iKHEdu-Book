# Khoảng cách lớn nhất giữa hai số nguyên tố liên tiếp

## Bối cảnh
Cho đoạn $[L, R]$ với $1 \le L \le R \le 10^9$ và $R - L \le 10^6$. Hãy tìm khoảng cách lớn nhất giữa hai số nguyên tố liên tiếp nằm trong đoạn này. Nếu trong đoạn có ít hơn 2 số nguyên tố, in ra `-1`.

## Nhiệm vụ
Cho đoạn $[L, R]$. Hãy lập trình tìm khoảng cách lớn nhất giữa hai số nguyên tố liên tiếp trong đoạn; in `-1` nếu đoạn có ít hơn $2$ số nguyên tố.

## Input
- Một dòng duy nhất chứa hai số nguyên dương $L, R$ ($1 \le L \le R \le 10^9, R - L \le 10^6$).

## Output
- In ra khoảng cách lớn nhất giữa 2 số nguyên tố liên tiếp, hoặc `-1` nếu không đủ 2 số nguyên tố.

## Sample 1
### Input
```text
1 30
```
### Output
```text
6
```
### Giải thích
* Các số nguyên tố là 2, 3, 5, 7, 11, 13, 17, 19, 23, 29. Khoảng cách lớn nhất là $29 - 23 = 6$ (và $23 - 17 = 6$).

## Ràng buộc
- $100\%$ số test có dữ liệu đầu vào nằm trong phạm vi cho phép.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
