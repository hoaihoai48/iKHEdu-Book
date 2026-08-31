# Lũy Thừa Ma Trận Chia Để Trị 2x2

**Phân loại bài toán:** `Core Foundation`

## Bối cảnh
Cho ma trận vuông $A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$ cấp $2 \times 2$ và số nguyên không âm $N$. Hãy tính ma trận $A^N \pmod M$ bằng thuật toán Lũy thừa nhị phân Chia Để Trị trong $\mathcal{O}(\log N)$.

## Input
- Dòng 1: 4 số nguyên $a, b, c, d$ ($0 \le a, b, c, d \le 10^9$).
- Dòng 2: Hai số nguyên $N, M$ ($0 \le N \le 10^{18}, 1 \le M \le 10^9 + 7$).

## Output
- In ra ma trận kết quả 2 dòng, mỗi dòng 2 phần tử cách nhau bởi dấu cách.

## Sample 1
### Input
```text
1 1
1 0
4 1000
```
### Output
```text
5 3
3 2
```
### Giải thích
Ma trận Fibonacci [[1,1],[1,0]]^4 = [[5,3],[3,2]].

## Ràng buộc
- 100% số test có $N \le 10^{18}, M \le 10^9 + 7$.
- Thời gian: 1.0s, Bộ nhớ: 256MB.
