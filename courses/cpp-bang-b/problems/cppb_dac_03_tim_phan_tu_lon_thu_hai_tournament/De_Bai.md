# Tìm Phần Tử Lớn Thứ Hai (Tournament Tree)

**Phân loại bài toán:** `Core Foundation`

## Bối cảnh
Cho mảng số nguyên $A$ gồm $N$ phần tử đôi một phân biệt. Hãy sử dụng mô hình cây thi đấu Chia Để Trị (Tournament Tree) để tìm phần tử lớn thứ hai trong mảng với số phép so sánh tối ưu $N + \lceil \log_2 N \rceil - 2$.

## Input
- Dòng 1: Số nguyên dương $N$ ($2 \le N \le 10^5$).
- Dòng 2: $N$ số nguyên phân biệt $A_1, \dots, A_N$ ($|A_i| \le 10^9$).

## Output
- In ra giá trị của phần tử lớn thứ hai trong mảng.

## Sample 1
### Input
```text
5
8 3 10 5 7
```
### Output
```text
8
```
### Giải thích
Phần tử lớn nhất là 10, lớn thứ hai là 8.

## Ràng buộc
- 100% số test có $2 \le N \le 10^5, |A_i| \le 10^9$.
- Thời gian: 1.0s, Bộ nhớ: 256MB.
