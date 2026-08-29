# Đếm Số Tam Giác Có Thể Tạo Thành

## Bối cảnh
Cho $N$ đoạn que với độ dài $A_1, A_2, \dots, A_N$. Hãy đếm số lượng bộ 3 que có thể ghép lại thành một tam giác không suy biến (tổng 2 cạnh bất kỳ lớn hơn cạnh còn lại).

## Input
- Dòng 1: Số nguyên dương $N$ ($3 \le N \le 3000$).
- Dòng 2: $N$ số nguyên dương $A_1, A_2, \dots, A_N$ ($1 \le A_i \le 10^9$).

## Output
- In ra một số nguyên duy nhất là số lượng tam giác tạo được.

## Sample 1
### Input
```text
4
4 6 3 7
```
### Output
```text
3
```
### Giải thích
Các bộ 3 tạo tam giác: $(3, 4, 6), (3, 6, 7), (4, 6, 7)$.

## Ràng buộc
- $100\%$ số test có $N \le 3000, 1 \le A_i \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
