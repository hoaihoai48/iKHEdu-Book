# Phần Tử Thứ K Của Hai Mảng Đã Sắp Xếp

## Bối cảnh
Cho hai mảng số nguyên $A$ và $B$ có kích thước lần lượt là $N$ và $M$, cả hai đều đã được sắp xếp theo thứ tự tăng dần. Hãy tìm phần tử nhỏ thứ $K$ ($1 \le K \le N + M$) khi gộp chung hai mảng lại với nhau.

## Input
- Dòng 1: Gồm 3 số nguyên $N, M, K$ ($1 \le N, M \le 10^5, 1 \le K \le N + M$).
- Dòng 2: $N$ số nguyên đã sắp xếp $A_1, A_2, \dots, A_N$ ($|A_i| \le 10^9$).
- Dòng 3: $M$ số nguyên đã sắp xếp $B_1, B_2, \dots, B_M$ ($|B_i| \le 10^9$).

## Output
- In ra một số nguyên duy nhất là giá trị của phần tử nhỏ thứ $K$.

## Sample 1
### Input
```text
5 4 5
2 3 6 7 9
1 4 8 10
```
### Output
```text
6
```
*(Giải thích: Mảng sau khi gộp là $[1, 2, 3, 4, 6, 7, 8, 9, 10]$. Phần tử thứ 5 là 6).*

## Ràng buộc
- $100\%$ số test có $N, M \le 10^5, |A_i|, |B_i| \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
