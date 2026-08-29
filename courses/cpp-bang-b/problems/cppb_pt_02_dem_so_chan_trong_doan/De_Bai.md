# Đếm Số Lượng Số Chẵn Trong Đoạn

## Bối cảnh
Cho một dãy gồm $N$ số nguyên. Có $Q$ câu hỏi dạng $[L, R]$, yêu cầu đếm xem trong đoạn từ vị trí $L$ đến $R$ có bao nhiêu số chẵn.

## Input
- Dòng 1: Gồm 2 số nguyên $N, Q$ ($1 \le N, Q \le 10^5$).
- Dòng 2: Gồm $N$ số nguyên $A_1, A_2, \dots, A_N$ ($|A_i| \le 10^9$).
- $Q$ dòng tiếp theo: Mỗi dòng gồm 2 số nguyên $L, R$ ($1 \le L \le R \le N$).

## Output
- In ra $Q$ dòng, mỗi dòng là số lượng số chẵn trong đoạn $[L \dots R]$.

## Sample 1
### Input
```text
6 3
1 2 4 5 6 7
1 4
2 5
1 6
```
### Output
```text
2
3
3
```

## Ràng buộc
- $100\%$ số test có $N, Q \le 10^5, |A_i| \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
