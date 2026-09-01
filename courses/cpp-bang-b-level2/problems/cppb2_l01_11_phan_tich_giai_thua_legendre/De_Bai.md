# Phân tích thừa số nguyên tố của giai thừa (định lý Legendre)

## Bối cảnh
Cho số nguyên dương $N$ và một số nguyên tố $P$. Cần tìm số mũ lớn nhất $K$ sao cho $N!$ chia hết cho $P^K$ (ký hiệu $v_P(N!)$). Áp dụng công thức Legendre: $v_P(N!) = \sum_{i=1}^{\infty} \lfloor \frac{N}{P^i} \rfloor$, thuật toán cho phép tính $K$ trong thời gian $\mathcal{O}(\log_P N)$ mà không cần tính trực tiếp giá trị khổng lồ của $N!$.

## Nhiệm vụ
Hãy lập trình giải quyết bài toán Phân Tích Thừa Số Nguyên Tố Của Giai Thừa (định Lý Legendre) với độ phức tạp tối ưu nhất.

## Input
- Một dòng duy nhất chứa hai số nguyên $N$ và $P$ ($1 \le N \le 10^{18}$, $2 \le P \le 10^9$, $P$ là số nguyên tố).

## Output
- In ra một số nguyên duy nhất là số mũ $K$ lớn nhất.

## Sample 1
### Input
```text
100 5
```
### Output
```text
24
```
### Giải thích
* $v_5(100!) = \lfloor 100/5 \rfloor + \lfloor 100/25 \rfloor = 20 + 4 = 24$.

## Ràng buộc
- $100\%$ số test có dữ liệu đầu vào nằm trong phạm vi cho phép.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
