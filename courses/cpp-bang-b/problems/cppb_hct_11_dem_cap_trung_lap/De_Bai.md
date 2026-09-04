# Đếm Cặp Tổng S Trên Mảng Trùng Lặp

## Bối cảnh
Một sàn giao dịch tài chính phân tích sổ lệnh khớp giá của N giao dịch diễn ra trong phiên mở cửa. Mỗi giao dịch có giá trị khớp lệnh là một số nguyên, và có rất nhiều giao dịch có cùng một mức giá (mảng chứa nhiều phần tử trùng lặp). Thuật toán thị trường cần kiểm tra xem có bao nhiêu cặp lệnh giao dịch ở hai thời điểm khác nhau (i < j) có tổng giá trị giao dịch đạt đúng mức chỉ số S.

## Nhiệm vụ
Cho mảng gồm N số nguyên có thể chứa nhiều phần tử trùng lặp và số nguyên S. Hãy đếm số lượng cặp chỉ số (i, j) với 1 <= i < j <= N sao cho A[i] + A[j] = S.

## Input
- Dòng 1: 2 số nguyên $N$ và $S$ ($2 \le N \le 2 \cdot 10^5, -10^{18} \le S \le 10^{18}$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^9 \le A_i \le 10^9$).

## Output
- In ra một số nguyên duy nhất là số lượng cặp chỉ số thỏa mãn.

## Sample 1
### Input
```text
6 6
3 3 3 3 3 3
```
### Output
```text
15
```
### Giải thích
Mảng gồm 6 phần tử đều bằng 3 và mục tiêu S = 6. Vì mọi cặp chỉ số (i, j) với 1 <= i < j <= 6 đều có tổng A[i] + A[j] = 3 + 3 = 6, nên số lượng cặp thỏa mãn chính là số cách chọn 2 phần tử từ 6 phần tử: C(6, 2) = 6 * 5 / 2 = 15 cặp.

## Ràng buộc
- $100\%$ số test có $N \le 2 \cdot 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
