# Thuật Toán Sắp Xếp Trộn (Merge Sort)

**Phân loại bài toán:** `Core Foundation`

## Bối cảnh
Cho mảng số nguyên $A$ gồm $N$ phần tử. Hãy tự cài đặt hoàn chỉnh thuật toán Sắp Xếp Trộn (Merge Sort) theo mô hình Chia Để Trị để sắp xếp mảng $A$ theo thứ tự tăng dần.

## Input
- Dòng 1: Số nguyên dương $N$ ($1 \le N \le 10^5$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \dots, A_N$ ($|A_i| \le 10^9$).

## Output
- In ra $N$ phần tử của mảng sau khi sắp xếp tăng dần, cách nhau bởi dấu cách.

## Sample 1
### Input
```text
7
38 27 43 3 9 82 10
```
### Output
```text
3 9 10 27 38 43 82
```
### Giải thích
Mảng sau khi sắp xếp tăng dần: 3 9 10 27 38 43 82.

## Ràng buộc
- 100% số test có $1 \le N \le 10^5, |A_i| \le 10^9$.
- Thời gian: 1.0s, Bộ nhớ: 256MB.
