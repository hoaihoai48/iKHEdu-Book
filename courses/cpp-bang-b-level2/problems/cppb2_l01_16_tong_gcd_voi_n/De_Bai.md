# Tính Tổng Gcd Của N Với Tất Cả Các Số Từ 1 Đến N

## Bối cảnh
Cho số nguyên dương $N$. Hãy tính giá trị của tổng $S(N) = \sum_{i=1}^N \gcd(i, N)$. Bằng cách gom nhóm các số $i$ theo giá trị $d = \gcd(i, N)$, ta có công thức tối ưu: $S(N) = \sum_{d | N} d \cdot \phi(N / d)$. Thuật toán cho phép tính $S(N)$ trong $\mathcal{O}(\sqrt{N})$.

## Nhiệm vụ
Hãy lập trình giải quyết bài toán Tính Tổng Gcd Của N Với Tất Cả Các Số Từ 1 Đến N với độ phức tạp tối ưu nhất.

## Input
- Một dòng duy nhất chứa số nguyên dương $N$ ($1 \le N \le 10^{12}$).

## Output
- In ra giá trị tổng $S(N)$.

## Sample 1
### Input
```text
6
```
### Output
```text
15
```
### Giải thích
* $\gcd(1,6) + \gcd(2,6) + \gcd(3,6) + \gcd(4,6) + \gcd(5,6) + \gcd(6,6) = 1 + 2 + 3 + 2 + 1 + 6 = 15$.

## Ràng buộc
- $100\%$ số test có dữ liệu đầu vào nằm trong phạm vi cho phép.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
