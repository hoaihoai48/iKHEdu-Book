# Ước Chung & Bội Chung Cơ Bản

## Bối cảnh
Trong các kỳ thi lập trình thi đấu, việc tìm **Ước chung lớn nhất ($\gcd$)** và **Bội chung nhỏ nhất ($\text{lcm}$)** là một trong những khối xử lý cơ sở nền tảng nhất. Tuy nhiên, khi các số đầu vào có giá trị lớn (lên tới $10^9$), việc tính toán bất cẩn phép nhân trong $\text{lcm}$ rất dễ dẫn đến lỗi tràn số nguyên 64-bit (`long long`).

Cho $T$ bộ dữ liệu, mỗi bộ gồm hai số nguyên dương $A$ và $B$.

## Nhiệm vụ
Nhiệm vụ của bạn là tính và in ra $\gcd(A, B)$ và $\text{lcm}(A, B)$.

## Input
- Dòng đầu tiên chứa số nguyên dương $T$ ($1 \le T \le 10^5$) — số lượng bộ dữ liệu cần xử lý.
- $T$ dòng tiếp theo, mỗi dòng chứa hai số nguyên dương $A$ và $B$ ($1 \le A, B \le 10^9$), cách nhau bởi một dấu cách.

## Output
- Gồm $T$ dòng, mỗi dòng in ra hai số nguyên cách nhau bởi một dấu cách: số đầu tiên là $\gcd(A, B)$, số thứ hai là $\text{lcm}(A, B)$.

## Sample 1
### Input
```text
3
12 18
6 9
1000000000 1000000000
```
### Output
```text
6 36
3 18
1000000000 1000000000
```
### Giải thích
* Với cặp $(12, 18)$: $\gcd(12, 18) = 6$, $\text{lcm}(12, 18) = \frac{12}{6} \times 18 = 36$.
* Với cặp $(6, 9)$: $\gcd(6, 9) = 3$, $\text{lcm}(6, 9) = \frac{6}{3} \times 9 = 18$.
* Với cặp $(10^9, 10^9)$: $\gcd = 10^9, \text{lcm} = 10^9$.

## Ràng buộc
- $100\%$ số test có dữ liệu đầu vào nằm trong phạm vi cho phép.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
