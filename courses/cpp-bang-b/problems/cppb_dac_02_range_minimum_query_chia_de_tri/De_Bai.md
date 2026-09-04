# Tìm Min Trên Đoạn Bằng Chia Để Trị (RMQ D&C Cơ Bản)

## Bối cảnh
Để tìm giá trị nhỏ nhất trên đoạn [L, R] của một mảng số nguyên, phương pháp chia để trị chia đoạn thành hai nửa trái [L, Mid] và phải [Mid + 1, R], giải đệ quy tìm min từng nửa rồi kết hợp kết quả: Min(đoạn) = min(Min(trái), Min(phải)).

## Nhiệm vụ
Cho mảng N số nguyên và Q truy vấn [L, R]. Hãy tìm giá trị nhỏ nhất trong đoạn [L, R] bằng đệ quy chia để trị.

## Input
- Dòng 1: Chứa 2 số nguyên $N$ và $Q$ ($1 \le N, Q \le 10^4$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^9 \le A_i \le 10^9$).
- $Q$ dòng tiếp theo: Mỗi dòng gồm 2 số nguyên $L$ và $R$ ($1 \le L \le R \le N$).

## Output
- In ra $Q$ dòng, mỗi dòng là giá trị min trên đoạn tương ứng.

## Sample 1
### Input
```text
5 2
3 1 4 2 5
1 3
3 5
```
### Output
```text
1
2
```
### Giải thích
- Đoạn [1, 3] gồm {3, 1, 4} có min = 1.
- Đoạn [3, 5] gồm {4, 2, 5} có min = 2.

## Ràng buộc
- $100\%$ số test có $N, Q \le 10^4$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
