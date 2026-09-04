# Đoạn Con Dài Nhất Có Độ Chênh Lệch Max-Min <= C

## Bối cảnh
Một dây chuyền kiểm soát chất lượng linh kiện điện tử quét qua một dãy gồm $N$ sản phẩm với chỉ số dung sai $A_1, A_2, \dots, A_N$. Một lô sản phẩm đạt chuẩn ổn định là một đoạn con các sản phẩm liên tiếp sao cho độ chênh lệch giữa sản phẩm có dung sai lớn nhất và sản phẩm có dung sai nhỏ nhất trong lô không vượt quá một ngưỡng cho phép $C$.

## Nhiệm vụ
Cho mảng $A$ gồm $N$ số nguyên và ngưỡng chênh lệch $C$. Hãy lập trình tìm độ dài lớn nhất của một đoạn con liên tiếp có $\max - \min \le C$.

## Input
- Dòng 1: Chứa hai số nguyên $N$ và $C$ ($1 \le N \le 10^5, 0 \le C \le 10^9$).
- Dòng 2: Chứa $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^9 \le A_i \le 10^9$).

## Output
- In ra trên một dòng duy nhất độ dài lớn nhất của đoạn con tìm được.

## Sample 1
### Input
```text
6 2
4 2 2 2 4 4
```
### Output
```text
6
```

### Giải thích
Với mảng $[8, 2, 4, 7]$ và ngưỡng $C = 4$:
Đoạn con $[2, 4]$ có $\max = 4, \min = 2$, độ chênh lệch là $4 - 2 = 2 \le 4$ có độ dài 2.
Đoạn con $[4, 7]$ có $\max = 7, \min = 4$, độ chênh lệch là $7 - 4 = 3 \le 4$ có độ dài 2.
Độ dài lớn nhất đạt được là 2.

## Ràng buộc
- $100\%$ số test có $1 \le N \le 10^5, 0 \le C, A_i \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
