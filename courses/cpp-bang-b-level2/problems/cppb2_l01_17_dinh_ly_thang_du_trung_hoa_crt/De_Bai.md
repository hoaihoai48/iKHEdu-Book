# Định lý thặng dư trung hoa (chinese remainder theorem — CRT)

## Bối cảnh
Trong lý thuyết số học và mật mã học, Định lý thặng dư Trung Hoa (CRT) giải quyết bài toán tìm số nguyên $x$ thỏa mãn một hệ phương trình đồng dư: $x \equiv r_i \pmod{m_i}$ ($1 \le i \le K$) với các modulo $m_i$ đôi một nguyên tố cùng nhau. Nghiệm $x$ duy nhất trong modulo $M = \prod m_i$ được tính bằng công thức: $x = \sum r_i \cdot M_i \cdot M_i^{-1} \pmod M$.

## Nhiệm vụ
Hãy lập trình giải quyết bài toán Định Lý Thặng Dư Trung Hoa (chinese Remainder Theorem — Crt) với độ phức tạp tối ưu nhất.

## Input
- Dòng 1: Chứa số nguyên $K$ ($2 \le K \le 10$).
- $K$ dòng tiếp theo, mỗi dòng chứa 2 số nguyên $r_i, m_i$ ($0 \le r_i < m_i \le 1000$, $\gcd(m_i, m_j) = 1$).

## Output
- In ra số nguyên dương $x$ nhỏ nhất ($0 \le x < \prod m_i$) thỏa mãn hệ phương trình.

## Sample 1
### Input
```text
3
2 3
3 5
2 7
```
### Output
```text
23
```
### Giải thích
* $23 \equiv 2 \pmod 3$, $23 \equiv 3 \pmod 5$, $23 \equiv 2 \pmod 7$.

## Ràng buộc
- $100\%$ số test có dữ liệu đầu vào nằm trong phạm vi cho phép.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
