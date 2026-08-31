# Tìm Phần Tử Đa Số (Majority Element) D&C

**Phân loại bài toán:** `Core Foundation`

## Bối cảnh
Cho mảng số nguyên $A$ gồm $N$ phần tử. Phần tử đa số là phần tử xuất hiện nhiều hơn $\lfloor N / 2 \rfloor$ lần. Hãy sử dụng thuật toán Chia Để Trị để tìm phần tử đa số. Nếu không tồn tại, in ra `-1`.

## Input
- Dòng 1: Số nguyên dương $N$ ($1 \le N \le 10^5$).
- Dòng 2: $N$ số nguyên $A_1, \dots, A_N$ ($|A_i| \le 10^9$).

## Output
- In ra phần tử đa số, hoặc `-1` nếu không có.

## Sample 1
### Input
```text
7
2 2 1 1 2 2 3
```
### Output
```text
2
```
### Giải thích
Số 2 xuất hiện 4 lần (> 7/2 = 3).

## Ràng buộc
- 100% số test có $N \le 10^5, |A_i| \le 10^9$.
- Thời gian: 1.0s, Bộ nhớ: 256MB.
