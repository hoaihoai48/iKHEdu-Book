# Phân Phối Tài Nguyên Không Gian Tuyến Tính

## Bối cảnh
Cho dãy số $N$ phần tử ban đầu toàn số 0. Có $Q$ thao tác, mỗi thao tác cộng vào đoạn $[L \dots R]$ một cấp số cộng bắt đầu từ giá trị $S$ và tăng dần theo bước nhảy $D$ (tức vị trí $L$ cộng $S$, vị trí $L+1$ cộng $S+D$, ..., vị trí $R$ cộng $S + (R-L)D$).

## Nhiệm vụ
Hãy in ra mảng kết quả cuối cùng sau khi hoàn thành $Q$ thao tác.

## Input
- Dòng 1: Gồm 2 số nguyên $N, Q$ ($1 \le N, Q \le 2 \cdot 10^5$).
- $Q$ dòng tiếp theo: Mỗi dòng gồm 4 số nguyên $L, R, S, D$ ($1 \le L \le R \le N, |S|, |D| \le 10^4$).

## Output
- In ra $N$ số nguyên trên một dòng biểu diễn mảng cuối cùng.

## Sample 1
### Input
```text
5 2
1 3 2 1
2 4 1 2
```
### Output
```text
2 4 7 5 0
```
*(Giải thích: Thao tác 1 cộng $[2, 3, 4, 0, 0]$; Thao tác 2 cộng $[0, 1, 3, 5, 0]$. Tổng là $[2, 4, 7, 5, 0]$).*

## Ràng buộc
- $100\%$ số test có $N, Q \le 2 \cdot 10^5, |S|, |D| \le 10^4$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
