# Đếm Số Cách Phân Tích Số N Thành Tổng Bằng Đệ Quy

## Bối cảnh
Bài toán phân tích số nguyên N thành tổng của các số nguyên dương (Integer Partition) là một bài toán kinh điển của Euler. Hãy đếm số cách viết số nguyên N thành tổng các số nguyên dương không giảm (ví dụ 4 = 1+1+1+1 = 1+1+2 = 1+3 = 2+2 = 4).

## Nhiệm vụ
Cho số nguyên dương N (1 <= N <= 40). Hãy đếm số cách phân tích N thành tổng của các số nguyên dương.

## Input
- Một dòng duy nhất chứa số nguyên dương $N$ ($1 \le N \le 40$).

## Output
- In ra số cách phân tích.

## Sample 1
### Input
```text
4
```
### Output
```text
5
```
### Giải thích
5 cách phân tích số 4 gồm: 4 = 1+1+1+1 = 1+1+2 = 1+3 = 2+2 = 4. Kết quả in ra: 5.

## Ràng buộc
- $100\%$ số test có $N \le 40$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
