# Sàng nguyên tố đoạn [l, r]

## Bối cảnh
Khi khoảng giá trị cần tìm số nguyên tố nằm rất xa gốc tọa độ ($L, R \le 10^{12}$), ta không thể sử dụng mảng đánh dấu kích thước $10^{12}$ do giới hạn bộ nhớ RAM. Tuy nhiên, nếu độ dài đoạn $R - L \le 10^6$, ta có thể áp dụng thuật toán **Sàng nguyên tố phân đoạn (Segmented Sieve)** bằng cách:
1. Sàng các số nguyên tố cơ sở $p \le \sqrt{R} \le 10^6$.
2. Ánh xạ đoạn $[L, R]$ về mảng kích thước $R - L + 1 \le 10^6 + 1$ và gạch các bội số của $p$ trong đoạn.

Cho hai số nguyên dương $L$ và $R$. Hãy đếm số lượng số nguyên tố nằm trong đoạn $[L, R]$.

## Nhiệm vụ
Hãy lập trình giải quyết bài toán Sàng Nguyên Tố Đoạn [l, R] với độ phức tạp tối ưu nhất.

## Input
- Gồm một dòng duy nhất chứa hai số nguyên dương $L$ và $R$ ($1 \le L \le R \le 10^{12}$, $R - L \le 10^6$), cách nhau bởi một dấu cách.

## Output
- In ra một số nguyên duy nhất là số lượng số nguyên tố trong đoạn $[L, R]$.

## Sample 1
### Input
```text
1 10
```
### Output
```text
4
```
### Giải thích
Trong đoạn $[1, 10]$, có 4 số nguyên tố là $2, 3, 5, 7$ (số 1 không phải số nguyên tố).

## Ràng buộc
- $100\%$ số test có dữ liệu đầu vào nằm trong phạm vi cho phép.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
