# Lũy Thừa Nhị Phân Đệ Quy A^B mod M

## Bối cảnh
Bản chất toán học của lũy thừa nhị phân là hệ thức đệ quy: nếu B chẵn thì A^B = (A^(B/2))^2, nếu B lẻ thì A^B = A * A^(B - 1). Hãy cài đặt thuật toán lũy thừa nhị phân bằng hàm đệ quy thuần túy.

## Nhiệm vụ
Cho 3 số nguyên A, B, M. Hãy tính A^B mod M bằng hàm đệ quy.

## Input
- Một dòng chứa 3 số nguyên $A, B, M$ ($0 \le A, B \le 10^{18}, 1 \le M \le 10^9$).

## Output
- In ra giá trị $A^B \pmod M$.

## Sample 1
### Input
```text
3 5 100
```
### Output
```text
43
```
### Giải thích
3^5 = 243. 243 mod 100 = 43. Kết quả in ra: 43.

## Ràng buộc
- $100\%$ số test có $A, B \le 10^{18}, 1 \le M \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
