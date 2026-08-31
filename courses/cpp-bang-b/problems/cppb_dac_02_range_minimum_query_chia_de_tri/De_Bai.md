# Tìm Min Trên Đoạn Bằng Chia Để Trị (RMQ D&C Cơ Bản)

**Phân loại bài toán:** `Core Foundation`

## Bối cảnh
Cho mảng số nguyên $A$ gồm $N$ phần tử. Hãy cài đặt hàm đệ quy Chia để trị `queryMin(l, r)` để tìm giá trị nhỏ nhất trong mảng $A$.

## Input
- Dòng 1: Số nguyên dương $N$ ($1 \le N \le 10^5$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \dots, A_N$ ($|A_i| \le 10^9$).

## Output
- In ra giá trị nhỏ nhất trong mảng $A$.

## Sample 1
### Input
```text
6
4 2 7 1 9 3
```
### Output
```text
1
```
### Giải thích
Giá trị nhỏ nhất trong mảng là 1.

## Ràng buộc
- 100% số test có $N \le 10^5, |A_i| \le 10^9$.
- Thời gian: 1.0s, Bộ nhớ: 256MB.
