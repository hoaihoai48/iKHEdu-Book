# Tìm Cặp Có Tổng Gần S Nhất

## Bối cảnh
Cho mảng gồm $N$ số nguyên và một số nguyên $S$. Hãy tìm một cặp số $(A_i, A_j)$ với $i < j$ sao cho tổng $A_i + A_j$ có độ chênh lệch $|(A_i + A_j) - S|$ là nhỏ nhất có thể. Nếu có nhiều cặp, in ra cặp có tổng nhỏ hơn.

## Input
- Dòng 1: Chứa 2 số nguyên $N$ và $S$ ($2 \le N \le 10^5, -10^{18} \le S \le 10^{18}$).
- Dòng 2: Chứa $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^9 \le A_i \le 10^9$).

## Output
- In ra 2 số nguyên biểu diễn cặp số tìm được theo thứ tự tăng dần.

## Sample 1
### Input
```text
5 20
2 8 13 4 25
```
### Output
```text
4 13
```
### Giải thích
Sắp xếp: $[2, 4, 8, 13, 25]$. Cặp $(4, 13)$ có tổng là 17 (chênh lệch với 20 là 3, nhỏ nhất).

## Ràng buộc
- $100\%$ số test có $N \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
