# Tìm Đoạn Con Có Trung Bình Lớn Nhất Độ Dài >= K

## Bối cảnh
Cho một dãy số nguyên gồm $N$ phần tử $A_1, A_2, \dots, A_N$ và một số nguyên $K$ ($1 \le K \le N$). Hãy tìm một đoạn con liên tiếp có độ dài ít nhất là $K$ sao cho giá trị trung bình cộng của các phần tử trong đoạn là **lớn nhất có thể**.

## Input
- Dòng 1: Gồm 2 số nguyên $N, K$ ($1 \le K \le N \le 10^5$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \dots, A_N$ ($0 \le A_i \le 10^6$).

## Output
- In ra giá trị trung bình lớn nhất lấy 4 chữ số thập phân.

## Sample 1
### Input
```text
4 2
6 8 1 3
```
### Output
```text
7.0000
```
*(Giải thích: Đoạn con $[6, 8]$ độ dài 2 có trung bình là $(6 + 8) / 2 = 7.0$).*

## Ràng buộc
- $100\%$ số test có $N \le 10^5, A_i \le 10^6$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
